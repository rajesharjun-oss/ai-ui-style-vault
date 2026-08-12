param(
  [string]$Brief = "",
  [string]$BriefFile = "",
  [string]$ProjectPath = "",
  [string]$CatalogJson = ".\motion\premium-motion-sources.json",
  [string]$OutputPath = ".\PREMIUM_MOTION_SOURCE_SELECTION.generated.md",
  [int]$TopSources = 8,
  [switch]$PassThruJson
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$script:RepoRoot = Split-Path -Parent $PSScriptRoot
$script:StopWords = @{}
foreach ($word in @("about","also","and","are","build","can","for","from","have","into","like","make","more","need","needs","site","that","the","this","tool","use","using","with","would","website","your")) { $script:StopWords[$word] = $true }

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
  return (($Text -replace "\|", "\\|") -replace "`r?`n", " ").Trim()
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
  if (Test-Path -LiteralPath $resolvedBriefFile -PathType Leaf) { $briefText += "`n" + (Get-Content -LiteralPath $resolvedBriefFile -Raw) }
}
$projectSignals = Read-ProjectSignals $ProjectPath
$combinedText = ($briefText + " " + ($projectSignals -join " ")).Trim()
$combinedNormalized = Normalize-Text $combinedText
$terms = Get-Terms $combinedText

$catalogPath = Resolve-VaultPath $CatalogJson
if (-not (Test-Path -LiteralPath $catalogPath -PathType Leaf)) { throw "Missing premium motion source catalog: $catalogPath" }
$catalog = Get-Content -LiteralPath $catalogPath -Raw | ConvertFrom-Json

$rows = foreach ($source in @($catalog.sources)) {
  $search = Normalize-Text (Convert-ToSearchText $source)
  $score = [int]$source.priority * 8
  $why = [System.Collections.Generic.List[string]]::new()
  [void]$why.Add("priority $($source.priority)")
  $matches = @($terms | Where-Object { $_.Length -gt 3 -and $search.Contains($_) } | Select-Object -Unique -First 8)
  if ($matches.Count -gt 0) { $score += [Math]::Min(32, $matches.Count * 5); [void]$why.Add("term match: " + ($matches -join ", ")) }
  if ($combinedNormalized -match "saas|startup|ai|product") {
    if ($source.id -in @("godly-sites","motion-examples","motion-react-docs","react-bits","framer-marketplace")) { $score += 25; [void]$why.Add("SaaS/product fit") }
  }
  if ($combinedNormalized -match "cinematic|wedding|restaurant|venue|hospitality|real estate|showroom|video") {
    if ($source.id -in @("awwwards","the-fwa","motion-array","storyblocks-motion-backgrounds","jitter-templates")) { $score += 25; [void]$why.Add("cinematic/media fit") }
  }
  if ($combinedNormalized -match "3d|webgl|hardware|game|spatial") {
    if ($source.id -in @("spline","spline-community","threejs-examples","gsap-showcase")) { $score += 30; [void]$why.Add("3D/WebGL fit") }
  }
  if ($combinedNormalized -match "lottie|illustration|empty state|onboarding") {
    if ($source.id -in @("lottiefiles-marketplace","rive","rive-marketplace-docs","motion-examples")) { $score += 30; [void]$why.Add("Lottie/Rive/onboarding fit") }
  }
  if ($combinedNormalized -match "react|next|vite") {
    if ($source.id -in @("motion-examples","motion-react-docs","react-bits","gsap-docs")) { $score += 20; [void]$why.Add("React stack fit") }
  }
  if ($combinedNormalized -match "template|asset|stock|licensed") {
    if ($source.sourceType -match "asset|template") { $score += 20; [void]$why.Add("asset/template need") }
  }
  [pscustomobject][ordered]@{
    score = [Math]::Min(100, $score)
    id = [string]$source.id
    name = [string]$source.name
    url = [string]$source.url
    sourceType = [string]$source.sourceType
    accessModel = [string]$source.accessModel
    useFor = @($source.useFor)
    licenseRule = [string]$source.licenseRule
    agentUse = [string]$source.agentUse
    why = (($why | Select-Object -Unique) -join "; ")
  }
}
$selected = @($rows | Sort-Object -Property @{ Expression = "score"; Descending = $true }, @{ Expression = "name"; Descending = $false } | Select-Object -First $TopSources)
$resolvedOutput = $OutputPath
if (-not [System.IO.Path]::IsPathRooted($resolvedOutput)) { $resolvedOutput = Join-Path (Get-Location) $OutputPath }
$outputParent = Split-Path -Parent $resolvedOutput
if ($outputParent -and -not (Test-Path -LiteralPath $outputParent)) { New-Item -ItemType Directory -Path $outputParent -Force | Out-Null }
$md = [System.Text.StringBuilder]::new()
[void]$md.AppendLine("# Premium Motion Source Selection")
[void]$md.AppendLine("")
[void]$md.AppendLine("Generated by scripts/select-premium-motion-sources.ps1 on $(Get-Date -Format yyyy-MM-dd).")
[void]$md.AppendLine("")
[void]$md.AppendLine("## Target")
[void]$md.AppendLine("")
[void]$md.AppendLine("- Brief: $briefText")
[void]$md.AppendLine("- Target repo or output path: $(if ([string]::IsNullOrWhiteSpace($ProjectPath)) { 'Not provided' } else { $ProjectPath })")
[void]$md.AppendLine("")
[void]$md.AppendLine("## Selected Sources")
[void]$md.AppendLine("")
[void]$md.AppendLine("| Score | Source | Type | Use For | License Rule | Why |")
[void]$md.AppendLine("|---:|---|---|---|---|---|")
foreach ($row in $selected) {
  [void]$md.AppendLine(("| {0} | [{1}]({2}) | {3} | {4} | {5} | {6} |" -f $row.score, (Escape-MarkdownCell $row.name), $row.url, $row.sourceType, (Escape-MarkdownCell (($row.useFor | Select-Object -First 5) -join ', ')), (Escape-MarkdownCell $row.licenseRule), (Escape-MarkdownCell $row.why)))
}
[void]$md.AppendLine("")
[void]$md.AppendLine("## Use Rules")
[void]$md.AppendLine("")
[void]$md.AppendLine("- Use award and gallery sources for ideas only.")
[void]$md.AppendLine("- Use asset and template sources only after confirming the exact license.")
[void]$md.AppendLine("- Record source URLs and license notes in VAULT_SELECTION.md before implementation.")
[void]$md.AppendLine("- Do not copy exact videos, screenshots, logos, product copy, animation files, or proprietary motion sequences.")
[void]$md.AppendLine("- Add reduced-motion behavior for autoplay, scroll, video, canvas, WebGL, Lottie, Rive, and loops.")
[void]$md.AppendLine("")
[void]$md.AppendLine("## Read Before Implementation")
[void]$md.AppendLine("")
[void]$md.AppendLine("- motion/PREMIUM_MOTION_SOURCES.md")
[void]$md.AppendLine("- motion/premium-motion-sources.json")
[void]$md.AppendLine("- motion/LANDING_PAGE_MOTION_GUIDE.md")
[System.IO.File]::WriteAllText($resolvedOutput, $md.ToString(), [System.Text.UTF8Encoding]::new($false))
Write-Output "PREMIUM_MOTION_SOURCES=$($selected.Count)"
Write-Output "OUTPUT=$resolvedOutput"
if ($PassThruJson) { $selected | ConvertTo-Json -Depth 8 }