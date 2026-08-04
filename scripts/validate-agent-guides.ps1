$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

$requiredFiles = @(
  "AGENTS.md",
  "guides/AGENT_USAGE.md",
  "guides/AGENT_BUILD_CHECKLIST.md",
  "guides/STYLE_SELECTION_GUIDE.md",
  "guides/WEB_TOOL_DESIGN_MATRIX.md",
  "templates/VAULT_SELECTION.md",
  "scripts/validate-generated-site.ps1",
  "agent-index.json",
  "catalog.json",
  "screen-catalog.json",
  "motion/README.md",
  "motion/LANDING_PAGE_MOTION_GUIDE.md",
  "motion/MOTION_REFERENCES.md",
  "motion/motion-catalog.json",
  "scripts/generate-motion-catalog.ps1",
  "scripts/select-motion-references.ps1",
  "scripts/validate-motion-catalog.ps1",
  "sources.json"
)

$missing = @()
foreach ($file in $requiredFiles) {
  $path = Join-Path $root $file
  if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
    $missing += $file
  }
}

if ($missing.Count -gt 0) {
  Write-Host "VALIDATION=FAIL"
  Write-Host "MISSING_FILES=$($missing -join ', ')"
  exit 1
}

$agentIndex = Get-Content -LiteralPath (Join-Path $root "agent-index.json") -Raw | ConvertFrom-Json
$catalog = Get-Content -LiteralPath (Join-Path $root "catalog.json") -Raw | ConvertFrom-Json
$screenCatalog = Get-Content -LiteralPath (Join-Path $root "screen-catalog.json") -Raw | ConvertFrom-Json
$motionCatalog = Get-Content -LiteralPath (Join-Path $root "motion/motion-catalog.json") -Raw | ConvertFrom-Json
$sources = Get-Content -LiteralPath (Join-Path $root "sources.json") -Raw | ConvertFrom-Json

if ($agentIndex.inventory.styleBundles -ne $catalog.totalStyles) {
  Write-Host "VALIDATION=FAIL"
  Write-Host "STYLE_COUNT_MISMATCH agent-index.json=$($agentIndex.inventory.styleBundles) catalog.json=$($catalog.totalStyles)"
  exit 1
}

if ($agentIndex.inventory.screenReferences -ne $screenCatalog.totalScreenReferences) {
  Write-Host "VALIDATION=FAIL"
  Write-Host "SCREEN_COUNT_MISMATCH agent-index.json=$($agentIndex.inventory.screenReferences) screen-catalog.json=$($screenCatalog.totalScreenReferences)"
  exit 1
}

if ($agentIndex.inventory.motionStyleReferences -ne $motionCatalog.totals.styleReferences) {
  Write-Host "VALIDATION=FAIL"
  Write-Host "MOTION_COUNT_MISMATCH agent-index.json=$($agentIndex.inventory.motionStyleReferences) motion-catalog.json=$($motionCatalog.totals.styleReferences)"
  exit 1
}

if (-not $sources.sources -or $sources.sources.Count -lt 1) {
  Write-Host "VALIDATION=FAIL"
  Write-Host "SOURCES_EMPTY"
  exit 1
}

$requiredEntryPoints = @(
  "agentInstructions",
  "agentUsageGuide",
  "buildChecklist",
  "styleSelectionGuide",
  "webToolDesignMatrix",
  "generatedSiteValidator",
  "styleCatalog",
  "screenCatalog",
  "motionReadme",
  "motionGuide",
  "motionCatalog",
  "motionReferences",
  "motionSelector",
  "motionCatalogGenerator",
  "motionCatalogValidator"
)

foreach ($entryPoint in $requiredEntryPoints) {
  if (-not $agentIndex.entryPoints.$entryPoint) {
    Write-Host "VALIDATION=FAIL"
    Write-Host "MISSING_ENTRY_POINT=$entryPoint"
    exit 1
  }
}

Write-Host "TOTAL_STYLES=$($catalog.totalStyles)"
Write-Host "TOTAL_SCREEN_REFERENCES=$($screenCatalog.totalScreenReferences)"
Write-Host "TOTAL_MOTION_REFERENCES=$($motionCatalog.totals.styleReferences)"
Write-Host "AGENT_GUIDES=PASS"
Write-Host "VALIDATION=PASS"