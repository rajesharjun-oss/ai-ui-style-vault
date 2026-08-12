$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$catalogPath = Join-Path $root "motion/motionsites-prompt-catalog.json"
$guidePath = Join-Path $root "motion/MOTIONSITES_PROMPT_REFERENCES.md"

if (-not (Test-Path -LiteralPath $catalogPath -PathType Leaf)) {
  Write-Host "VALIDATION=FAIL"
  Write-Host "MISSING_FILE=motion/motionsites-prompt-catalog.json"
  exit 1
}
if (-not (Test-Path -LiteralPath $guidePath -PathType Leaf)) {
  Write-Host "VALIDATION=FAIL"
  Write-Host "MISSING_FILE=motion/MOTIONSITES_PROMPT_REFERENCES.md"
  exit 1
}

$catalog = Get-Content -LiteralPath $catalogPath -Raw | ConvertFrom-Json
$references = @($catalog.references)
if ($references.Count -ne $catalog.totals.references) {
  Write-Host "VALIDATION=FAIL"
  Write-Host "REFERENCE_COUNT_MISMATCH references=$($references.Count) totals=$($catalog.totals.references)"
  exit 1
}
if ($catalog.totals.references -lt 1) {
  Write-Host "VALIDATION=FAIL"
  Write-Host "NO_REFERENCES"
  exit 1
}

$ids = @{}
foreach ($ref in $references) {
  foreach ($field in @("id", "source", "sourceType", "title", "category", "access", "sourceUrl", "promptDigest", "mediaPolicy")) {
    if (-not $ref.$field -or [string]::IsNullOrWhiteSpace([string]$ref.$field)) {
      Write-Host "VALIDATION=FAIL"
      Write-Host "MISSING_FIELD=$field REF=$($ref.id)"
      exit 1
    }
  }
  if ($ids.ContainsKey($ref.id)) {
    Write-Host "VALIDATION=FAIL"
    Write-Host "DUPLICATE_ID=$($ref.id)"
    exit 1
  }
  $ids[$ref.id] = $true
  if ([string]$ref.sourceUrl -notmatch '^https://motionsites\.ai/') {
    Write-Host "VALIDATION=FAIL"
    Write-Host "UNEXPECTED_SOURCE_URL=$($ref.sourceUrl)"
    exit 1
  }
  $json = $ref | ConvertTo-Json -Depth 20
  if ($json -match 'fullPrompt|promptBody|premiumPromptText|copiedCode|sourceCode') {
    Write-Host "VALIDATION=FAIL"
    Write-Host "DISALLOWED_PROMPT_OR_CODE_FIELD=$($ref.id)"
    exit 1
  }
}

$promptCards = @($references | Where-Object { $_.sourceType -ne "animated-background-reference" })
$backgrounds = @($references | Where-Object { $_.sourceType -eq "animated-background-reference" })
if ($promptCards.Count -ne $catalog.totals.promptCards) {
  Write-Host "VALIDATION=FAIL"
  Write-Host "PROMPT_CARD_COUNT_MISMATCH promptCards=$($promptCards.Count) totals=$($catalog.totals.promptCards)"
  exit 1
}
if ($backgrounds.Count -ne $catalog.totals.animatedBackgrounds) {
  Write-Host "VALIDATION=FAIL"
  Write-Host "BACKGROUND_COUNT_MISMATCH backgrounds=$($backgrounds.Count) totals=$($catalog.totals.animatedBackgrounds)"
  exit 1
}

Write-Host "TOTAL_MOTIONSITES_REFERENCES=$($catalog.totals.references)"
Write-Host "TOTAL_MOTIONSITES_PROMPT_CARDS=$($catalog.totals.promptCards)"
Write-Host "TOTAL_MOTIONSITES_BACKGROUNDS=$($catalog.totals.animatedBackgrounds)"
Write-Host "MOTIONSITES_PROMPT_REFERENCES=PASS"
Write-Host "VALIDATION=PASS"
