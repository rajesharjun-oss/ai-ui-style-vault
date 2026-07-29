param(
  [Parameter(Mandatory = $true)]
  [string]$SiteRoot,

  [string]$BlockedAssetHost = "",

  [string]$Url = "",

  [switch]$AllowExternalImages,

  [switch]$AllowMissingVaultSelection
)

$ErrorActionPreference = "Stop"

function Add-Issue([System.Collections.Generic.List[string]]$List, [string]$Message) {
  $List.Add($Message) | Out-Null
}

function Read-Text([string]$Path) {
  return Get-Content -LiteralPath $Path -Raw
}

function Get-LocalRelativePath([string]$BasePath, [string]$ChildPath) {
  $baseFull = [System.IO.Path]::GetFullPath($BasePath).TrimEnd([System.IO.Path]::DirectorySeparatorChar, [System.IO.Path]::AltDirectorySeparatorChar) + [System.IO.Path]::DirectorySeparatorChar
  $childFull = [System.IO.Path]::GetFullPath($ChildPath)
  if ($childFull.StartsWith($baseFull, [StringComparison]::OrdinalIgnoreCase)) {
    return $childFull.Substring($baseFull.Length)
  }
  return $childFull
}

$errors = [System.Collections.Generic.List[string]]::new()
$warnings = [System.Collections.Generic.List[string]]::new()

if (-not (Test-Path -LiteralPath $SiteRoot -PathType Container)) {
  Write-Host "VALIDATION=FAIL"
  Write-Host "ERROR=SiteRoot not found: $SiteRoot"
  exit 1
}

$root = (Resolve-Path -LiteralPath $SiteRoot).Path
$indexPath = Join-Path $root "index.html"
$selectionPath = Join-Path $root "VAULT_SELECTION.md"

if (-not (Test-Path -LiteralPath $indexPath -PathType Leaf)) {
  Add-Issue $warnings "index.html not found; validator will only scan available files."
}

if (-not $AllowMissingVaultSelection -and -not (Test-Path -LiteralPath $selectionPath -PathType Leaf)) {
  Add-Issue $errors "Missing VAULT_SELECTION.md. Copy templates/VAULT_SELECTION.md into the build and fill it before handoff."
}

if (Test-Path -LiteralPath $selectionPath -PathType Leaf) {
  $selection = Read-Text $selectionPath
  foreach ($needle in @("Primary style", "Supporting", "Asset Policy", "QA")) {
    if ($selection -notmatch [regex]::Escape($needle)) {
      Add-Issue $warnings "VAULT_SELECTION.md may be incomplete; missing section hint: $needle"
    }
  }
}

$scanExtensions = @(".html", ".css", ".js", ".jsx", ".ts", ".tsx", ".md", ".json")
$files = Get-ChildItem -LiteralPath $root -Recurse -File |
  Where-Object {
    $lowerPath = $_.FullName.ToLowerInvariant()
    ($scanExtensions -contains $_.Extension.ToLowerInvariant()) -and
      ($lowerPath -notmatch "\\(\.git|node_modules|dist|build|\.next)\\") -and
      ($lowerPath -notmatch "\\output\\playwright\\")
  }

$debugPattern = "(?i)\bTODO\b|lorem ipsum|console\.log"
$placeholderMarkerPattern = "\bPLACEHOLDER\b"
$externalImagePattern = "(?i)<img[^>]+src\s*=\s*['""]https?://"
$httpSrcPattern = "(?i)\bsrc\s*=\s*['""]https?://"
$fixedOrStickyPattern = "(?i)position\s*:\s*(fixed|sticky)"

foreach ($file in $files) {
  $relative = Get-LocalRelativePath $root $file.FullName
  $text = Read-Text $file.FullName

  if ($relative -ne "VAULT_SELECTION.md" -and (($text -match $debugPattern) -or ($text -cmatch $placeholderMarkerPattern))) {
    Add-Issue $errors "Placeholder/debug text found in $relative"
  }

  if (-not $AllowExternalImages -and $text -match $externalImagePattern) {
    Add-Issue $errors "External image source found in $relative. Use local, generated, user-provided, owned, or licensed assets."
  }

  if (-not [string]::IsNullOrWhiteSpace($BlockedAssetHost) -and $text.IndexOf($BlockedAssetHost, [StringComparison]::OrdinalIgnoreCase) -ge 0) {
    Add-Issue $errors "Blocked asset host found in ${relative}: $BlockedAssetHost"
  }

  if ($text.IndexOf("wp-content", [StringComparison]::OrdinalIgnoreCase) -ge 0) {
    Add-Issue $errors "WordPress asset path found in $relative. Verify this is not copied target-site media."
  }

  if ($file.Extension.ToLowerInvariant() -eq ".css" -and $text -match $fixedOrStickyPattern) {
    Add-Issue $warnings "Fixed or sticky positioning found in $relative. Manually verify it does not cover anchors, headings, forms, or cards."
  }

  if ($file.Extension.ToLowerInvariant() -eq ".html" -and -not $AllowExternalImages -and $text -match $httpSrcPattern) {
    Add-Issue $warnings "External src attribute found in $relative. Verify it is not target-site media."
  }
}

if (-not [string]::IsNullOrWhiteSpace($Url)) {
  try {
    $response = Invoke-WebRequest -Uri $Url -UseBasicParsing -TimeoutSec 10
    if ($response.StatusCode -lt 200 -or $response.StatusCode -ge 400) {
      Add-Issue $errors "URL returned non-success status $($response.StatusCode): $Url"
    }
  } catch {
    Add-Issue $errors "URL check failed for ${Url}: $($_.Exception.Message)"
  }
}

Write-Host "SITE_ROOT=$root"
Write-Host "FILES_SCANNED=$($files.Count)"
Write-Host "ERRORS=$($errors.Count)"
Write-Host "WARNINGS=$($warnings.Count)"

if ($warnings.Count -gt 0) {
  Write-Host "WARNING_DETAILS:"
  foreach ($warning in $warnings) { Write-Host "- $warning" }
}

if ($errors.Count -gt 0) {
  Write-Host "VALIDATION=FAIL"
  Write-Host "ERROR_DETAILS:"
  foreach ($errorItem in $errors) { Write-Host "- $errorItem" }
  exit 1
}

Write-Host "VALIDATION=PASS"
