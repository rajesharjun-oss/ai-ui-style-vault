param(
  [string]$MotionRoot = ".\motion",
  [string]$CatalogJson = ".\motion\motion-catalog.json"
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

function Resolve-RepoPath([string]$Path) {
  if ([System.IO.Path]::IsPathRooted($Path)) { return $Path }
  return (Join-Path (Get-Location) $Path)
}

$motionPath = Resolve-RepoPath $MotionRoot
$catalogPath = Resolve-RepoPath $CatalogJson
$errors = [System.Collections.Generic.List[string]]::new()

$requiredFiles = @(
  "motion/README.md",
  "motion/LANDING_PAGE_MOTION_GUIDE.md",
  "motion/MOTION_REFERENCES.md",
  "motion/motion-catalog.json",
  "scripts/generate-motion-catalog.ps1",
  "scripts/select-motion-references.ps1",
  "scripts/validate-motion-catalog.ps1"
)

foreach ($file in $requiredFiles) {
  $path = Join-Path (Get-Location) $file
  if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
    $errors.Add("missing $file")
  }
}

if (-not (Test-Path -LiteralPath $motionPath -PathType Container)) {
  $errors.Add("missing motion root $MotionRoot")
}

$catalog = $null
if (Test-Path -LiteralPath $catalogPath -PathType Leaf) {
  try {
    $catalog = Get-Content -LiteralPath $catalogPath -Raw | ConvertFrom-Json
  } catch {
    $errors.Add("invalid motion catalog JSON: $($_.Exception.Message)")
  }
} else {
  $errors.Add("missing motion catalog $CatalogJson")
}

if ($null -ne $catalog) {
  if ([int]$catalog.totals.styleReferences -lt 100) {
    $errors.Add("motion catalog has too few style references: $($catalog.totals.styleReferences)")
  }
  if ([int]$catalog.totals.styleReferencesWithPreviewVideo -lt 100) {
    $errors.Add("motion catalog has too few video-capable references: $($catalog.totals.styleReferencesWithPreviewVideo)")
  }
  if ([int]$catalog.totals.motionPatterns -lt 8) {
    $errors.Add("motion catalog has too few motion patterns: $($catalog.totals.motionPatterns)")
  }
  if ([int]$catalog.totals.implementationResources -lt 5) {
    $errors.Add("motion catalog has too few implementation resources: $($catalog.totals.implementationResources)")
  }
  if ($catalog.policy.mediaStorage -ne "remote-links-only") {
    $errors.Add("motion catalog media policy must be remote-links-only")
  }

  foreach ($ref in @($catalog.styleReferences)) {
    if (-not $ref.name) { $errors.Add("style reference missing name") }
    if (-not $ref.path) { $errors.Add("style reference missing path: $($ref.name)") }
    if ($ref.path -and -not (Test-Path -LiteralPath (Join-Path (Get-Location) ([string]$ref.path)) -PathType Container)) {
      $errors.Add("style reference path missing: $($ref.path)")
    }
    if (-not $ref.requiredReadFiles -or @($ref.requiredReadFiles).Count -lt 1) {
      $errors.Add("style reference missing required read files: $($ref.name)")
    }
  }

  foreach ($pattern in @($catalog.patterns)) {
    if (-not $pattern.id) { $errors.Add("motion pattern missing id") }
    if (-not $pattern.name) { $errors.Add("motion pattern missing name") }
    if (-not $pattern.useWhen) { $errors.Add("motion pattern missing useWhen: $($pattern.id)") }
    if (-not $pattern.reducedMotion) { $errors.Add("motion pattern missing reducedMotion guidance: $($pattern.id)") }
  }

  foreach ($resource in @($catalog.implementationResources)) {
    if (-not $resource.name) { $errors.Add("implementation resource missing name") }
    if (-not $resource.url -or $resource.url -notmatch "^https://") {
      $errors.Add("implementation resource missing https URL: $($resource.name)")
    }
  }
}

if (Test-Path -LiteralPath $motionPath -PathType Container) {
  $vendoredMedia = @(Get-ChildItem -LiteralPath $motionPath -Recurse -File |
    Where-Object { $_.Extension -match "^\.(mp4|webm|mov|gif|avi|m4v)$" })
  foreach ($file in $vendoredMedia) {
    $errors.Add("vendored motion media is not allowed: $($file.FullName)")
  }
}

if ($null -ne $catalog) {
  Write-Output "MOTION_REFERENCES=$($catalog.totals.styleReferences)"
  Write-Output "HIGH_SIGNAL=$($catalog.totals.highSignalStyleReferences)"
  Write-Output "WITH_PREVIEW_VIDEO=$($catalog.totals.styleReferencesWithPreviewVideo)"
  Write-Output "PATTERNS=$($catalog.totals.motionPatterns)"
}

if ($errors.Count -gt 0) {
  Write-Output "VALIDATION=FAIL"
  Write-Output "ERRORS=$($errors.Count)"
  $errors | ForEach-Object { Write-Output $_ }
  exit 1
}

Write-Output "VALIDATION=PASS"
