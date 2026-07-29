param(
  [string]$StylesRoot = ".\styles\refero-styles"
)

$ErrorActionPreference = "Stop"

$requiredFiles = @(
  "README.md",
  "source.md",
  "DESIGN.md",
  "implementation-prompt.md",
  "style.json",
  "tokens/colors.md",
  "tokens/typography.md",
  "tokens/spacing-shape.md",
  "tokens/components.md",
  "tokens/guidelines.md",
  "tokens/layout-imagery.md",
  "code/css-variables.css",
  "code/tailwind-v4.css",
  "code/design-tokens.json",
  "screenshots/README.md"
)

function Read-Text([string]$Path) { return Get-Content -LiteralPath $Path -Raw }
function Has-MeaningfulText([string]$Text, [string[]]$Needles) {
  foreach ($needle in $Needles) { if ($Text -match $needle) { return $true } }
  return $false
}
function First-Text([object[]]$Values) {
  foreach ($value in $Values) {
    $text = ([string]$value).Trim()
    if (-not [string]::IsNullOrWhiteSpace($text)) { return $text }
  }
  return ""
}

$root = Resolve-Path -LiteralPath $StylesRoot
$styleDirs = Get-ChildItem -LiteralPath $root -Directory | Sort-Object Name
$errors = [System.Collections.Generic.List[string]]::new()

foreach ($dir in $styleDirs) {
  $slug = $dir.Name
  $style = $null

  foreach ($rel in $requiredFiles) {
    $path = Join-Path $dir.FullName $rel
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { $errors.Add("$slug missing $rel") }
  }

  $styleJsonPath = Join-Path $dir.FullName "style.json"
  if (Test-Path -LiteralPath $styleJsonPath -PathType Leaf) {
    try { $style = Read-Text $styleJsonPath | ConvertFrom-Json } catch { $errors.Add("$slug invalid JSON style.json: $($_.Exception.Message)") }
  }

  $designTokensPath = Join-Path $dir.FullName "code/design-tokens.json"
  if (Test-Path -LiteralPath $designTokensPath -PathType Leaf) {
    try { Read-Text $designTokensPath | ConvertFrom-Json | Out-Null } catch { $errors.Add("$slug invalid JSON code/design-tokens.json: $($_.Exception.Message)") }
  }

  $cssPath = Join-Path $dir.FullName "code/css-variables.css"
  if (Test-Path -LiteralPath $cssPath -PathType Leaf) {
    $css = Read-Text $cssPath
    if ($css -notmatch ":root\s*\{") { $errors.Add("$slug css missing :root") }
    if (-not (Has-MeaningfulText $css @("--[a-zA-Z0-9-]*color[a-zA-Z0-9-]*\s*:", "#[0-9a-fA-F]{6}"))) { $errors.Add("$slug css missing color tokens") }
  }

  $tailwindPath = Join-Path $dir.FullName "code/tailwind-v4.css"
  if (Test-Path -LiteralPath $tailwindPath -PathType Leaf) {
    $tailwind = Read-Text $tailwindPath
    if ($tailwind -notmatch "@theme\s*\{") { $errors.Add("$slug tailwind missing @theme") }
    if (-not (Has-MeaningfulText $tailwind @("--[a-zA-Z0-9-]*color[a-zA-Z0-9-]*\s*:", "#[0-9a-fA-F]{6}"))) { $errors.Add("$slug tailwind missing color tokens") }
  }

  $designPath = Join-Path $dir.FullName "DESIGN.md"
  if (Test-Path -LiteralPath $designPath -PathType Leaf) {
    $design = Read-Text $designPath
    if (-not (Has-MeaningfulText $design @("(?m)^## ", "(?i)color", "(?i)typography", "(?i)layout"))) { $errors.Add("$slug DESIGN lacks expected design sections") }
  }

  $componentsPath = Join-Path $dir.FullName "tokens/components.md"
  if (Test-Path -LiteralPath $componentsPath -PathType Leaf) {
    $components = Read-Text $componentsPath
    if (-not (Has-MeaningfulText $components @("(?i)component", "(?i)button", "(?i)card", "(?i)hero", "(?i)nav"))) { $errors.Add("$slug components token lacks component guidance") }
  }

  $guidelinesPath = Join-Path $dir.FullName "tokens/guidelines.md"
  if (Test-Path -LiteralPath $guidelinesPath -PathType Leaf) {
    $guidelines = Read-Text $guidelinesPath
    if (-not (Has-MeaningfulText $guidelines @("(?mi)^##+\s*Do\b", "(?i)\bdos?\b", "(?i)use "))) { $errors.Add("$slug guidelines missing do guidance") }
    if (-not (Has-MeaningfulText $guidelines @("(?mi)^##+\s*(Don't|Do Not|Avoid)", "(?i)do not", "(?i)avoid", "(?i)dont"))) { $errors.Add("$slug guidelines missing avoid guidance") }
  }

  $promptPath = Join-Path $dir.FullName "implementation-prompt.md"
  if (Test-Path -LiteralPath $promptPath -PathType Leaf) {
    $prompt = Read-Text $promptPath
    if (-not (Has-MeaningfulText $prompt @("(?i)use ", "(?i)create ", "(?i)build "))) { $errors.Add("$slug prompt missing implementation directive") }
    if (-not (Has-MeaningfulText $prompt @("(?i)avoid", "(?i)do not", "(?i)don't", "(?i)before finishing", "(?i)check that", "(?i)\bno\s+", "(?i)only one"))) { $errors.Add("$slug prompt missing constraint guidance") }
  }

  $sourcePath = Join-Path $dir.FullName "source.md"
  if (Test-Path -LiteralPath $sourcePath -PathType Leaf) {
    $source = Read-Text $sourcePath
    $styleUrl = ""
    $reference = ""
    $captured = ""
    if ($null -ne $style) {
      $styleUrl = First-Text @($style.source.referoUrl, $style.sourceUrl, $style.url)
      $reference = First-Text @($style.source.referenceSite, $style.referenceSite, $style.referenceUrl)
      $captured = First-Text @($style.source.capturedAt, $style.capturedAt, $style.capturedOn)
    }
    if ($source -notmatch "https://styles\.refero\.design/style/" -and -not $styleUrl) { $errors.Add("$slug source missing Refero URL") }
    if (-not (Has-MeaningfulText $source @("(?i)reference site", "(?i)referenced site", "(?i)reference url", "(?i)related product url")) -and -not $reference) { Write-Verbose "$slug has no separate reference site recorded" }
    if (-not (Has-MeaningfulText $source @("(?i)captured", "(?i)capture method", "(?i)discovery")) -and -not $captured) { $errors.Add("$slug source missing capture/discovery note") }
  }

  $screenshotsPath = Join-Path $dir.FullName "screenshots/README.md"
  if (Test-Path -LiteralPath $screenshotsPath -PathType Leaf) {
    $screens = Read-Text $screenshotsPath
    if (-not (Has-MeaningfulText $screens @("(?i)screenshot", "(?i)media", "(?i)reference"))) { $errors.Add("$slug screenshots README missing media note") }
  }

  foreach ($file in Get-ChildItem -LiteralPath $dir.FullName -Recurse -File) {
    $content = Read-Text $file.FullName
    if ($content -match "[^\x00-\x7F]") { $errors.Add("$slug non-ASCII $($file.FullName)") }
    if ($content -match "\`$slug|\`$\(|System\.Collections\.Specialized\.OrderedDictionary") { $errors.Add("$slug artifact marker $($file.FullName)") }
  }
}

Write-Output "TOTAL_STYLES=$(@($styleDirs).Count)"
Write-Output "REQUIRED_FILES_PER_STYLE=$($requiredFiles.Count)"
if ($errors.Count -gt 0) {
  Write-Output "VALIDATION=FAIL"
  Write-Output "ERRORS=$($errors.Count)"
  $errors | ForEach-Object { Write-Output $_ }
  exit 1
}
Write-Output "VALIDATION=PASS"