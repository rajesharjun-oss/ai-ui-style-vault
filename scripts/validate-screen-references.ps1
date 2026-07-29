param(
  [string]$ScreensRoot = ".\screens\refero",
  [string]$CatalogJson = ".\screen-catalog.json"
)

$ErrorActionPreference = "Stop"

$requiredFiles = @(
  "README.md",
  "source.md",
  "implementation-prompt.md",
  "screen.json",
  "tokens/colors.md",
  "tokens/page-elements.md",
  "code/css-variables.css",
  "code/design-tokens.json",
  "screenshots/README.md"
)

function Read-Text([string]$Path) { return Get-Content -LiteralPath $Path -Raw }
function Has-Text([string]$Text, [string[]]$Needles) {
  foreach ($needle in $Needles) {
    if ($Text -match $needle) { return $true }
  }
  return $false
}

$root = Resolve-Path -LiteralPath $ScreensRoot
$referenceDirs = Get-ChildItem -LiteralPath $root -Directory -Recurse |
  Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName "screen.json") -PathType Leaf } |
  Sort-Object FullName

$errors = [System.Collections.Generic.List[string]]::new()

foreach ($dir in $referenceDirs) {
  $rel = Resolve-Path -LiteralPath $dir.FullName -Relative
  foreach ($required in $requiredFiles) {
    if (-not (Test-Path -LiteralPath (Join-Path $dir.FullName $required) -PathType Leaf)) {
      $errors.Add("$rel missing $required")
    }
  }

  $screen = $null
  $screenJson = Join-Path $dir.FullName "screen.json"
  if (Test-Path -LiteralPath $screenJson -PathType Leaf) {
    try { $screen = Read-Text $screenJson | ConvertFrom-Json } catch { $errors.Add("$rel invalid screen.json: $($_.Exception.Message)") }
  }

  $tokensJson = Join-Path $dir.FullName "code/design-tokens.json"
  if (Test-Path -LiteralPath $tokensJson -PathType Leaf) {
    try { Read-Text $tokensJson | ConvertFrom-Json | Out-Null } catch { $errors.Add("$rel invalid code/design-tokens.json: $($_.Exception.Message)") }
  }

  $sourcePath = Join-Path $dir.FullName "source.md"
  if (Test-Path -LiteralPath $sourcePath -PathType Leaf) {
    $source = Read-Text $sourcePath
    if (-not (Has-Text $source @("https://refero\.design/", "https://api\.refero\.design/"))) { $errors.Add("$rel source missing Refero links") }
    if (-not (Has-Text $source @("images\.refero\.design", "Primary media URL", "Thumbnail URL"))) { $errors.Add("$rel source missing media reference") }
    if (-not (Has-Text $source @("inspiration-only", "License status"))) { $errors.Add("$rel source missing usage/license note") }
  }

  $promptPath = Join-Path $dir.FullName "implementation-prompt.md"
  if (Test-Path -LiteralPath $promptPath -PathType Leaf) {
    $prompt = Read-Text $promptPath
    if (-not (Has-Text $prompt @("Build an original", "Use these signals"))) { $errors.Add("$rel prompt missing build directive") }
    if (-not (Has-Text $prompt @("Do not copy", "Replace all brand"))) { $errors.Add("$rel prompt missing copy constraint") }
  }

  $cssPath = Join-Path $dir.FullName "code/css-variables.css"
  if (Test-Path -LiteralPath $cssPath -PathType Leaf) {
    $css = Read-Text $cssPath
    if ($css -notmatch ":root\s*\{") { $errors.Add("$rel css missing :root") }
    if (@($screen.colors).Count -gt 0 -and -not (Has-Text $css @("#[0-9a-fA-F]{6}", "--refero-"))) { $errors.Add("$rel css missing screen color token") }
  }

  $screensPath = Join-Path $dir.FullName "screenshots/README.md"
  if (Test-Path -LiteralPath $screensPath -PathType Leaf) {
    $screens = Read-Text $screensPath
    if (-not (Has-Text $screens @("images\.refero\.design", "Image URLs", "Thumbnail URL"))) { $errors.Add("$rel screenshots README missing image links") }
    if ($screens -match "!\[") { $errors.Add("$rel screenshots README embeds remote images instead of linking them") }
  }

  foreach ($file in Get-ChildItem -LiteralPath $dir.FullName -Recurse -File) {
    $content = Read-Text $file.FullName
    if ($content -match "[^\x00-\x7F]") { $errors.Add("$rel non-ASCII $($file.FullName)") }
    if ($content -match "\`$slug|\`$\(|System\.Collections\.Specialized\.OrderedDictionary") { $errors.Add("$rel artifact marker $($file.FullName)") }
  }

  if ($null -ne $screen) {
    if (-not $screen.id) { $errors.Add("$rel screen missing id") }
    if (-not $screen.pageType.name) { $errors.Add("$rel screen missing page type") }
    if (-not $screen.entity.name) { $errors.Add("$rel screen missing entity") }
    if (-not $screen.thumbnailUrl -and -not $screen.previewUrl -and @($screen.imageUrls).Count -eq 0) { $errors.Add("$rel screen missing media URL") }
  }
}

if (Test-Path -LiteralPath $CatalogJson -PathType Leaf) {
  try {
    $catalog = Read-Text $CatalogJson | ConvertFrom-Json
    if ([int]$catalog.totalScreenReferences -ne @($referenceDirs).Count) {
      $errors.Add("catalog totalScreenReferences $($catalog.totalScreenReferences) does not match folders $(@($referenceDirs).Count)")
    }
  } catch {
    $errors.Add("invalid screen catalog: $($_.Exception.Message)")
  }
} else {
  $errors.Add("missing $CatalogJson")
}

Write-Output "TOTAL_SCREEN_REFERENCES=$(@($referenceDirs).Count)"
Write-Output "REQUIRED_FILES_PER_REFERENCE=$($requiredFiles.Count)"
if ($errors.Count -gt 0) {
  Write-Output "VALIDATION=FAIL"
  Write-Output "ERRORS=$($errors.Count)"
  $errors | ForEach-Object { Write-Output $_ }
  exit 1
}
Write-Output "VALIDATION=PASS"
