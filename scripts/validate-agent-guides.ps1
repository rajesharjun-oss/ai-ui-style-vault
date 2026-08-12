$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

$requiredFiles = @(
  "PRD.md",
  "AGENTS.md",
  "CLAUDE.md",
  "GEMINI.md",
  "PROMPTS.md",
  "prompts/SENIOR_PRODUCT_TEAM_PROMPT.md",
  "prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md",
  "prompts/REFINE_EXISTING_BUSINESS_WEBSITE.md",
  "prompts/VISUAL_QA_AND_REVISION.md",
  "prompts/prompt-index.json",
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
$promptIndex = Get-Content -LiteralPath (Join-Path $root "prompts/prompt-index.json") -Raw | ConvertFrom-Json
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

if (-not $promptIndex.prompts -or $promptIndex.prompts.Count -lt 4) {
  Write-Host "VALIDATION=FAIL"
  Write-Host "PROMPT_INDEX_INCOMPLETE"
  exit 1
}

$promptIds = @($promptIndex.prompts | ForEach-Object { $_.id })
if (($promptIds | Sort-Object -Unique).Count -ne $promptIds.Count) {
  Write-Host "VALIDATION=FAIL"
  Write-Host "PROMPT_INDEX_DUPLICATE_IDS"
  exit 1
}

foreach ($prompt in $promptIndex.prompts) {
  $promptPath = Join-Path $root $prompt.path
  if (-not (Test-Path -LiteralPath $promptPath -PathType Leaf)) {
    Write-Host "VALIDATION=FAIL"
    Write-Host "PROMPT_PATH_NOT_FOUND=$($prompt.path)"
    exit 1
  }
}

$claude = Get-Content -LiteralPath (Join-Path $root "CLAUDE.md") -Raw
$gemini = Get-Content -LiteralPath (Join-Path $root "GEMINI.md") -Raw
$agents = Get-Content -LiteralPath (Join-Path $root "AGENTS.md") -Raw
$businessPrompt = Get-Content -LiteralPath (Join-Path $root "prompts/BUILD_PREMIUM_BUSINESS_WEBSITE.md") -Raw
$qaPrompt = Get-Content -LiteralPath (Join-Path $root "prompts/VISUAL_QA_AND_REVISION.md") -Raw

foreach ($adapter in @(
  @{ Name = "CLAUDE.md"; Content = $claude },
  @{ Name = "GEMINI.md"; Content = $gemini }
)) {
  if ($adapter.Content -notmatch "AGENTS\.md") {
    Write-Host "VALIDATION=FAIL"
    Write-Host "ADAPTER_MISSING_CANONICAL_IMPORT=$($adapter.Name)"
    exit 1
  }
  if ($adapter.Content -notmatch "BUILD_PREMIUM_BUSINESS_WEBSITE\.md") {
    Write-Host "VALIDATION=FAIL"
    Write-Host "ADAPTER_MISSING_BUSINESS_PROMPT=$($adapter.Name)"
    exit 1
  }
  if ($adapter.Content -notmatch "VISUAL_QA_AND_REVISION\.md") {
    Write-Host "VALIDATION=FAIL"
    Write-Host "ADAPTER_MISSING_VISUAL_QA_PROMPT=$($adapter.Name)"
    exit 1
  }
}

foreach ($requiredSignal in @(
  "Prompt Discovery and Routing",
  "BUILD_PREMIUM_BUSINESS_WEBSITE.md",
  "VISUAL_QA_AND_REVISION.md",
  "Localhost Truthfulness Rule"
)) {
  if ($agents -notmatch [regex]::Escape($requiredSignal)) {
    Write-Host "VALIDATION=FAIL"
    Write-Host "AGENTS_MISSING_SIGNAL=$requiredSignal"
    exit 1
  }
}

foreach ($requiredSignal in @(
  "BUSINESS_RESEARCH.md",
  "ASSET_PLAN.md",
  "VAULT_SELECTION.md",
  "localhost",
  "1440",
  "390",
  "verified facts",
  "repeated imagery"
)) {
  if ($businessPrompt -notmatch [regex]::Escape($requiredSignal)) {
    Write-Host "VALIDATION=FAIL"
    Write-Host "BUSINESS_PROMPT_MISSING_SIGNAL=$requiredSignal"
    exit 1
  }
}

foreach ($requiredSignal in @(
  "1440",
  "1280",
  "390",
  "sticky",
  "horizontal overflow",
  "reduced-motion",
  "Revision loop"
)) {
  if ($qaPrompt -notmatch [regex]::Escape($requiredSignal)) {
    Write-Host "VALIDATION=FAIL"
    Write-Host "VISUAL_QA_PROMPT_MISSING_SIGNAL=$requiredSignal"
    exit 1
  }
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
Write-Host "TASK_PROMPTS=$($promptIndex.prompts.Count)"
Write-Host "CROSS_AGENT_ADAPTERS=PASS"
Write-Host "AGENT_GUIDES=PASS"
Write-Host "VALIDATION=PASS"
