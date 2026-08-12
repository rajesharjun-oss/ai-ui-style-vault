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
  "motion/PREMIUM_MOTION_SOURCES.md",
  "motion/premium-motion-sources.json",
  "scripts/select-premium-motion-sources.ps1",
  "scripts/validate-premium-motion-sources.ps1",
  "motion/MOTIONSITES_PROMPT_REFERENCES.md",
  "motion/motionsites-prompt-catalog.json",
  "scripts/select-prompt-references.ps1",
  "scripts/validate-prompt-references.ps1",
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
$premiumMotionSources = Get-Content -LiteralPath (Join-Path $root "motion/premium-motion-sources.json") -Raw | ConvertFrom-Json
$motionSitesPromptReferences = Get-Content -LiteralPath (Join-Path $root "motion/motionsites-prompt-catalog.json") -Raw | ConvertFrom-Json
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

if ($agentIndex.inventory.premiumMotionSources -ne $premiumMotionSources.totals.sources) {
  Write-Host "VALIDATION=FAIL"
  Write-Host "PREMIUM_MOTION_SOURCE_COUNT_MISMATCH agent-index.json=$($agentIndex.inventory.premiumMotionSources) premium-motion-sources.json=$($premiumMotionSources.totals.sources)"
  exit 1
}

if ($agentIndex.inventory.motionSitesPromptReferences -ne $motionSitesPromptReferences.totals.references) {
  Write-Host "VALIDATION=FAIL"
  Write-Host "MOTIONSITES_PROMPT_REFERENCE_COUNT_MISMATCH agent-index.json=$($agentIndex.inventory.motionSitesPromptReferences) motionsites-prompt-catalog.json=$($motionSitesPromptReferences.totals.references)"
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
  "motionCatalogValidator",
  "premiumMotionSourceGuide",
  "premiumMotionSourceCatalog",
  "premiumMotionSourceSelector",
  "premiumMotionSourceValidator",
  "motionSitesPromptReferences",
  "motionSitesPromptCatalog",
  "promptReferenceSelector",
  "promptReferenceValidator"
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
Write-Host "TOTAL_PREMIUM_MOTION_SOURCES=$($premiumMotionSources.totals.sources)"
Write-Host "TOTAL_MOTIONSITES_PROMPT_REFERENCES=$($motionSitesPromptReferences.totals.references)"
Write-Host "AGENT_GUIDES=PASS"
Write-Host "VALIDATION=PASS"