param(
  [string]$CatalogJson = ".\motion\premium-motion-sources.json"
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

function Resolve-RepoPath([string]$Path) {
  if ([System.IO.Path]::IsPathRooted($Path)) { return $Path }
  return (Join-Path (Get-Location) $Path)
}

$errors = [System.Collections.Generic.List[string]]::new()
$requiredFiles = @(
  "motion/PREMIUM_MOTION_SOURCES.md",
  "motion/premium-motion-sources.json",
  "scripts/select-premium-motion-sources.ps1",
  "scripts/validate-premium-motion-sources.ps1"
)
foreach ($file in $requiredFiles) {
  if (-not (Test-Path -LiteralPath (Join-Path (Get-Location) $file) -PathType Leaf)) { $errors.Add("missing $file") }
}
$catalogPath = Resolve-RepoPath $CatalogJson
$catalog = $null
if (Test-Path -LiteralPath $catalogPath -PathType Leaf) {
  try { $catalog = Get-Content -LiteralPath $catalogPath -Raw | ConvertFrom-Json } catch { $errors.Add("invalid JSON: $($_.Exception.Message)") }
} else {
  $errors.Add("missing catalog $CatalogJson")
}
if ($null -ne $catalog) {
  $sources = @($catalog.sources)
  if ($sources.Count -lt 25) { $errors.Add("premium source catalog must contain at least 25 sources; found $($sources.Count)") }
  if ($catalog.policy.mediaStorage -ne "remote-links-only") { $errors.Add("premium source media policy must be remote-links-only") }
  if (-not $catalog.policy.licenseReviewRequired) { $errors.Add("premium source catalog must require license review") }
  foreach ($source in $sources) {
    foreach ($field in @("id","name","url","sourceType","accessModel","licenseRule","agentUse")) {
      if (-not $source.$field) { $errors.Add("$($source.id) missing $field") }
    }
    if ($source.url -and $source.url -notmatch "^https://") { $errors.Add("$($source.id) URL must use https: $($source.url)") }
    if (@($source.useFor).Count -lt 1) { $errors.Add("$($source.id) missing useFor entries") }
    if (@($source.tags).Count -lt 1) { $errors.Add("$($source.id) missing tags") }
  }
  $ids = @($sources | ForEach-Object { $_.id })
  $dupes = @($ids | Group-Object | Where-Object { $_.Count -gt 1 } | ForEach-Object { $_.Name })
  if ($dupes.Count -gt 0) { $errors.Add("duplicate source ids: $($dupes -join ', ')") }
  Write-Output "PREMIUM_MOTION_SOURCES=$($sources.Count)"
  Write-Output "INSPIRATION_SOURCES=$($catalog.totals.inspirationSources)"
  Write-Output "IMPLEMENTATION_SOURCES=$($catalog.totals.implementationSources)"
  Write-Output "ASSET_SOURCES=$($catalog.totals.assetSources)"
}
if ($errors.Count -gt 0) {
  Write-Output "VALIDATION=FAIL"
  Write-Output "ERRORS=$($errors.Count)"
  $errors | ForEach-Object { Write-Output $_ }
  exit 1
}
Write-Output "VALIDATION=PASS"