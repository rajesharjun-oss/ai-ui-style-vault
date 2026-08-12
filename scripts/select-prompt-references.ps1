param(
  [string]$Brief = "",
  [string]$BriefFile = "",
  [string]$ProjectPath = "",
  [string]$CatalogJson = ".\motion\motionsites-prompt-catalog.json",
  [string]$OutputPath = ".\PROMPT_REFERENCE_SELECTION.generated.md",
  [int]$TopReferences = 12,
  [switch]$IncludeBackgrounds,
  [switch]$PassThruJson
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$script:RepoRoot = Split-Path -Parent $PSScriptRoot
$script:StopWords = @{}
foreach ($word in @("about","also","and","are","build","can","for","from","have","into","like","make","more","need","needs","site","that","the","this","tool","use","using","with","would","website","your","page","pages","landing")) { $script:StopWords[$word] = $true }

function Resolve-VaultPath([string]$Path) {
  if ([System.IO.Path]::IsPathRooted($Path)) { return $Path }
  return (Join-Path $script:RepoRoot $Path)
}
function Normalize-Text([string]$Text) {
  if ([string]::IsNullOrWhiteSpace($Text)) { return "" }
  return (($Text.ToLowerInvariant() -replace "[^a-z0-9+#&.]+", " ") -replace "\s+", " ").Trim()
}
function Get-Terms([string]$Text) {
  $normalized = Normalize-Text $Text
  if ([string]::IsNullOrWhiteSpace($normalized)) { return @() }
  return @($normalized -split "\s+" | Where-Object { $_.Length -ge 3 -and -not $script:StopWords.ContainsKey($_) } | Select-Object -Unique)
}
function Convert-ToSearchText($Value) {
  if ($null -eq $Value) { return "" }
  if ($Value -is [string]) { return $Value }
  if ($Value -is [System.Array]) { return (($Value | ForEach-Object { Convert-ToSearchText $_ }) -join " ") }
  if ($Value -is [System.Management.Automation.PSCustomObject]) { return (($Value.PSObject.Properties | ForEach-Object { Convert-ToSearchText $_.Value }) -join " ") }
  return [string]$Value
}
function Escape-MarkdownCell([string]$Text) {
  if ($null -eq $Text) { return "" }
  return (($Text -replace "\|", "\\|") -replace "\r?\n", " ").Trim()
}
function Read-ProjectSignals([string]$Path) {
  $signals = [System.Collections.Generic.List[string]]::new()
  if ([string]::IsNullOrWhiteSpace($Path) -or -not (Test-Path -LiteralPath $Path -PathType Container)) { return @($signals) }
  $packagePath = Join-Path $Path "package.json"
  if (Test-Path -LiteralPath $packagePath -PathType Leaf) {
    try {
      $pkg = Get-Content -LiteralPath $packagePath -Raw | ConvertFrom-Json
      $deps = @()
      if ($pkg.dependencies) { $deps += $pkg.dependencies.PSObject.Properties.Name }
      if ($pkg.devDependencies) { $deps += $pkg.devDependencies.PSObject.Properties.Name }
      foreach ($dep in $deps) {
        if ($dep -match "react|next|vite|framer-motion|motion|gsap|three|rive|lottie|animejs|webflow") { [void]$signals.Add($dep) }
      }
    } catch {}
  }
  foreach ($file in @("README.md", "app/page.tsx", "src/App.tsx", "src/main.tsx")) {
    $candidate = Join-Path $Path $file
    if (Test-Path -LiteralPath $candidate -PathType Leaf) {
      try { [void]$signals.Add((Get-Content -LiteralPath $candidate -Raw)) } catch {}
    }
  }
  return @($signals)
}

$briefText = $Brief
if (-not [string]::IsNullOrWhiteSpace($BriefFile)) {
  $resolvedBriefFile = Resolve-VaultPath $BriefFile
  if (Test-Path -LiteralPath $resolvedBriefFile -PathType Leaf) { $briefText = $briefText + [Environment]::NewLine + (Get-Content -LiteralPath $resolvedBriefFile -Raw) }
}
$projectSignals = Read-ProjectSignals $ProjectPath
$combinedText = ($briefText + " " + ($projectSignals -join " ")).Trim()
$combinedNormalized = Normalize-Text $combinedText
$terms = Get-Terms $combinedText

$catalogPath = Resolve-VaultPath $CatalogJson
if (-not (Test-Path -LiteralPath $catalogPath -PathType Leaf)) { throw "Missing MotionSites prompt catalog: $catalogPath" }
$catalog = Get-Content -LiteralPath $catalogPath -Raw | ConvertFrom-Json

$references = @($catalog.references)
if (-not $IncludeBackgrounds) {
  $references = @($references | Where-Object { $_.sourceType -ne "animated-background-reference" })
}

$rows = foreach ($ref in $references) {
  $search = Normalize-Text (Convert-ToSearchText $ref)
  $score = 10
  $why = [System.Collections.Generic.List[string]]::new()
  $matches = @($terms | Where-Object { $_.Length -gt 3 -and $search.Contains($_) } | Select-Object -Unique -First 10)
  if ($matches.Count -gt 0) { $score += [Math]::Min(40, $matches.Count * 5); [void]$why.Add("term match: " + ($matches -join ", ")) }
  if ($ref.access -eq "copy") { $score += 10; [void]$why.Add("copy-access prompt observed") }
  if ($combinedNormalized -match "saas|startup|ai|product|software|dashboard") {
    if ($search -match "saas|ai|startup|product|platform|dashboard|analytics|app|tool") { $score += 25; [void]$why.Add("SaaS/product fit") }
  }
  if ($combinedNormalized -match "landing|hero|pricing|testimonial|faq|features|section") {
    if ($ref.sourceType -in @("site-prompt-reference", "section-prompt-reference")) { $score += 18; [void]$why.Add("landing/section prompt fit") }
  }
  if ($combinedNormalized -match "app|web tool|dashboard|portal|admin|login") {
    if ($ref.sourceType -eq "app-prompt-reference" -or $search -match "app|dashboard|tool|admin|login") { $score += 22; [void]$why.Add("app/tool prompt fit") }
  }
  if ($combinedNormalized -match "motion|animated|cinematic|3d|webgl|background|hero") {
    if ($search -match "motion|animated|3d|webgl|cinematic|background|hero|vortex|particle|aurora") { $score += 25; [void]$why.Add("motion-heavy fit") }
  }
  if ($combinedNormalized -match "background|loading|ambient|immersive") {
    if ($ref.sourceType -eq "animated-background-reference") { $score += 30; [void]$why.Add("animated background fit") }
  }
  if ($why.Count -eq 0) { [void]$why.Add("general composition reference") }
  [pscustomobject][ordered]@{
    score = [Math]::Min(100, $score)
    id = [string]$ref.id
    title = [string]$ref.title
    sourceType = [string]$ref.sourceType
    category = [string]$ref.category
    access = [string]$ref.access
    sourceUrl = [string]$ref.sourceUrl
    bestFor = @($ref.bestFor)
    motionSignals = @($ref.motionSignals)
    promptDigest = [string]$ref.promptDigest
    why = (($why | Select-Object -Unique) -join "; ")
  }
}
$selected = @($rows | Sort-Object -Property @{ Expression = "score"; Descending = $true }, @{ Expression = "title"; Descending = $false } | Select-Object -First $TopReferences)
$resolvedOutput = $OutputPath
if (-not [System.IO.Path]::IsPathRooted($resolvedOutput)) { $resolvedOutput = Join-Path (Get-Location) $OutputPath }
$outputParent = Split-Path -Parent $resolvedOutput
if ($outputParent -and -not (Test-Path -LiteralPath $outputParent)) { New-Item -ItemType Directory -Path $outputParent -Force | Out-Null }
$md = [System.Text.StringBuilder]::new()
[void]$md.AppendLine("# MotionSites Prompt Reference Selection")
[void]$md.AppendLine("")
[void]$md.AppendLine("Generated by scripts/select-prompt-references.ps1 on $(Get-Date -Format yyyy-MM-dd).")
[void]$md.AppendLine("")
[void]$md.AppendLine("## Target")
[void]$md.AppendLine("")
[void]$md.AppendLine("- Brief: $briefText")
[void]$md.AppendLine("- Target repo or output path: $(if ([string]::IsNullOrWhiteSpace($ProjectPath)) { 'Not provided' } else { $ProjectPath })")
[void]$md.AppendLine("- Background references included: $([bool]$IncludeBackgrounds)")
[void]$md.AppendLine("")
[void]$md.AppendLine("## Selected References")
[void]$md.AppendLine("")
[void]$md.AppendLine("| Score | Reference | Type | Category | Access | Why |")
[void]$md.AppendLine("|---:|---|---|---|---|---|")
foreach ($row in $selected) {
  [void]$md.AppendLine(("| {0} | [{1}]({2}) | {3} | {4} | {5} | {6} |" -f $row.score, (Escape-MarkdownCell $row.title), $row.sourceUrl, $row.sourceType, (Escape-MarkdownCell $row.category), $row.access, (Escape-MarkdownCell $row.why)))
}
[void]$md.AppendLine("")
[void]$md.AppendLine("## Use Rules")
[void]$md.AppendLine("")
[void]$md.AppendLine("- Use these as prompt-direction and composition references only.")
[void]$md.AppendLine("- Do not republish MotionSites prompt text, premium prompt text, screenshots, videos, assets, generated output, or copied code.")
[void]$md.AppendLine("- For premium references, visit MotionSites and confirm access/license before copying any prompt or media.")
[void]$md.AppendLine("- Pair with motion/LANDING_PAGE_MOTION_GUIDE.md and selected vault style/screen references.")
[void]$md.AppendLine("- Record source/license notes, original adaptation plan, and reduced-motion behavior in VAULT_SELECTION.md.")
[void]$md.AppendLine("")
[void]$md.AppendLine("## Read Before Implementation")
[void]$md.AppendLine("")
[void]$md.AppendLine("- motion/MOTIONSITES_PROMPT_REFERENCES.md")
[void]$md.AppendLine("- motion/motionsites-prompt-catalog.json")
[void]$md.AppendLine("- motion/LANDING_PAGE_MOTION_GUIDE.md")
[System.IO.File]::WriteAllText($resolvedOutput, $md.ToString(), [System.Text.UTF8Encoding]::new($false))
Write-Output "PROMPT_REFERENCES=$($selected.Count)"
Write-Output "OUTPUT=$resolvedOutput"
if ($PassThruJson) { $selected | ConvertTo-Json -Depth 8 }
