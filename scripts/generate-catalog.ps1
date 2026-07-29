param(
  [string]$StylesRoot = ".\styles\refero-styles",
  [string]$CatalogJson = ".\catalog.json",
  [string]$CatalogMarkdown = ".\CAPTURED_STYLES.md"
)

$ErrorActionPreference = "Stop"

function Normalize-Ascii([string]$Text) {
  if ($null -eq $Text) { return "" }
  $text = $Text
  $replacements = @{
    [char]0x2013 = "-"; [char]0x2014 = "-"; [char]0x2015 = "-"; [char]0x2212 = "-"
    [char]0x2018 = "'"; [char]0x2019 = "'"; [char]0x201A = "'"; [char]0x201B = "'"
    [char]0x201C = '"'; [char]0x201D = '"'; [char]0x201E = '"'
    [char]0x2026 = "..."; [char]0x00B7 = "-"; [char]0x00D7 = "x"
    [char]0x00A0 = " "; [char]0x2122 = "TM"; [char]0x00AE = "(R)"; [char]0x00A9 = "(C)"
  }
  foreach ($key in $replacements.Keys) { $text = $text.Replace([string]$key, [string]$replacements[$key]) }
  $normalized = $text.Normalize([Text.NormalizationForm]::FormD)
  $sb = [Text.StringBuilder]::new()
  foreach ($ch in $normalized.ToCharArray()) {
    if ([Globalization.CharUnicodeInfo]::GetUnicodeCategory($ch) -eq [Globalization.UnicodeCategory]::NonSpacingMark) { continue }
    if ([int][char]$ch -le 127) { [void]$sb.Append($ch) } else { [void]$sb.Append(" ") }
  }
  return ($sb.ToString() -replace '[ ]{2,}', ' ').Trim()
}

function Clean-Text([object]$Value) { return ((Normalize-Ascii ([string]$Value)) -replace '\s+', ' ').Trim() }
function Markdown-Cell([object]$Value) { $text = Clean-Text $Value; if ([string]::IsNullOrWhiteSpace($text)) { return "-" }; return $text.Replace("|", "\|") }
function String-Array([object]$Value) {
  $items = @()
  if ($null -eq $Value) { return $items }
  foreach ($item in @($Value)) {
    $text = Clean-Text $item
    if (-not [string]::IsNullOrWhiteSpace($text) -and -not $items.Contains($text)) { $items += $text }
  }
  return $items
}
function First-Text([object[]]$Values) {
  foreach ($value in $Values) {
    $text = Clean-Text $value
    if (-not [string]::IsNullOrWhiteSpace($text)) { return $text }
  }
  return ""
}
function Color-Summary($Colors) {
  $items = @()
  if ($null -eq $Colors) { return $items }
  if ($Colors -is [array]) {
    foreach ($color in @($Colors)) {
      $name = First-Text @($color.name, $color.token)
      $value = First-Text @($color.value)
      if ($name -and $value) { $items += "$name $value" }
    }
  } else {
    foreach ($prop in $Colors.PSObject.Properties) {
      $value = $prop.Value
      if ($value -is [string]) {
        if ($value -match '#[0-9a-fA-F]{3,8}') { $items += "$(Clean-Text $prop.Name) $value" }
      } else {
        $hex = First-Text @($value.value, $value.hex)
        if ($hex) { $items += "$(Clean-Text $prop.Name) $hex" }
      }
    }
  }
  return $items | Select-Object -First 8
}
function Font-Summary($Typography) {
  $items = @()
  if ($null -eq $Typography) { return $items }
  foreach ($font in @($Typography.fonts)) {
    $name = Clean-Text $font.name
    if ($name -and -not $items.Contains($name)) { $items += $name }
  }
  foreach ($value in @($Typography.primary, $Typography.fallback, $Typography.displayFamily, $Typography.bodyFamily, $Typography.displaySubstitute, $Typography.bodySubstitute)) {
    $text = Clean-Text $value
    if ($text -and -not $items.Contains($text)) { $items += $text }
  }
  if ($Typography.families) {
    foreach ($prop in $Typography.families.PSObject.Properties) {
      $text = Clean-Text $prop.Value
      if ($text -and -not $items.Contains($text)) { $items += $text }
    }
  }
  return $items | Select-Object -First 8
}

$stylesRootPath = Resolve-Path -LiteralPath $StylesRoot
$styleDirs = Get-ChildItem -LiteralPath $stylesRootPath -Directory | Sort-Object Name
$styles = @()

foreach ($dir in $styleDirs) {
  $styleJsonPath = Join-Path $dir.FullName "style.json"
  if (-not (Test-Path -LiteralPath $styleJsonPath -PathType Leaf)) { Write-Warning "Skipping $($dir.Name): missing style.json"; continue }
  $style = Get-Content -LiteralPath $styleJsonPath -Raw | ConvertFrom-Json

  $theme = First-Text @($style.classification.theme, $style.theme)
  $categoryValues = String-Array (First-Text @($style.classification.category, $style.category))
  if ($categoryValues.Count -eq 0) { $categoryValues = String-Array $style.classification.industry }
  if ($categoryValues.Count -eq 0) { $categoryValues = String-Array $style.industry }
  $category = (($categoryValues | Select-Object -First 3) -join ", ")
  $bestFor = String-Array (First-Text @($style.classification.bestFor, $style.bestFor))
  if ($bestFor.Count -eq 0) { $bestFor = String-Array $style.classification.bestFor }
  if ($bestFor.Count -eq 0) { $bestFor = String-Array $style.bestFor }

  $sourceUrl = First-Text @($style.source.referoUrl, $style.sourceUrl, $style.url)
  $referenceSite = First-Text @($style.source.referenceSite, $style.referenceSite, $style.referenceUrl)
  $capturedOn = First-Text @($style.source.capturedAt, $style.capturedAt, $style.capturedOn)
  $publishedAt = First-Text @($style.source.publishedAt, $style.publishedAt)
  $modifiedAt = First-Text @($style.source.articleModifiedAt, $style.source.schemaModifiedAt, $style.articleModifiedAt)

  $tags = @()
  foreach ($value in @($theme, $category)) { if ($value) { $tags += $value.ToLowerInvariant() } }
  foreach ($value in String-Array $style.tags) { if (-not $tags.Contains($value.ToLowerInvariant())) { $tags += $value.ToLowerInvariant() } }
  foreach ($value in $bestFor) { if (-not $tags.Contains($value.ToLowerInvariant())) { $tags += $value.ToLowerInvariant() } }

  $styles += [ordered]@{
    id = Clean-Text $style.id
    name = First-Text @($style.name, $dir.Name)
    slug = First-Text @($style.slug, $dir.Name)
    source = "Refero Styles"
    sourceSlug = "refero-styles"
    sourceUrl = $sourceUrl
    referenceSite = $referenceSite
    capturedOn = $capturedOn
    publishedAt = $publishedAt
    articleModifiedAt = $modifiedAt
    theme = $theme
    category = $category
    northStar = First-Text @($style.northStar, $style.mood)
    summary = Clean-Text $style.summary
    bestFor = $bestFor
    tags = $tags
    primaryColors = Color-Summary $style.colors
    fonts = Font-Summary $style.typography
    path = "styles/refero-styles/$($dir.Name)"
    files = [ordered]@{
      readme = "styles/refero-styles/$($dir.Name)/README.md"
      source = "styles/refero-styles/$($dir.Name)/source.md"
      design = "styles/refero-styles/$($dir.Name)/DESIGN.md"
      prompt = "styles/refero-styles/$($dir.Name)/implementation-prompt.md"
      cssVariables = "styles/refero-styles/$($dir.Name)/code/css-variables.css"
      tailwind = "styles/refero-styles/$($dir.Name)/code/tailwind-v4.css"
      designTokens = "styles/refero-styles/$($dir.Name)/code/design-tokens.json"
    }
  }
}

$catalog = [ordered]@{
  name = "AI UI Style Vault"
  generatedAt = (Get-Date -Format "yyyy-MM-dd")
  totalStyles = @($styles).Count
  sources = @([ordered]@{ name = "Refero Styles"; slug = "refero-styles"; url = "https://styles.refero.design/"; count = @($styles).Count; licenseStatus = "inspiration-only-unless-explicitly-licensed" })
  styles = $styles
}

$jsonPath = Join-Path (Resolve-Path -LiteralPath (Split-Path -Parent $CatalogJson)).Path (Split-Path -Leaf $CatalogJson)
[IO.File]::WriteAllText($jsonPath, (($catalog | ConvertTo-Json -Depth 24) + [Environment]::NewLine), [Text.UTF8Encoding]::new($false))

$md = [Text.StringBuilder]::new()
[void]$md.AppendLine("# Captured Styles")
[void]$md.AppendLine("")
[void]$md.AppendLine("Total styles: $(@($styles).Count)")
[void]$md.AppendLine("")
[void]$md.AppendLine("Each entry links to a local source-derived bundle with design notes, implementation prompt, tokens, code artifacts, source metadata, and media handling notes.")
[void]$md.AppendLine("")
[void]$md.AppendLine("| Style | Theme | Category | Best For | Source | Folder |")
[void]$md.AppendLine("|---|---|---|---|---|---|")
foreach ($style in $styles) {
  $bestForText = (($style.bestFor | Select-Object -First 4) -join ", ")
  $folder = $style.path
  $sourceCell = "Refero"
  if ($style.sourceUrl) { $sourceCell = "[Refero]($($style.sourceUrl))" }
  [void]$md.AppendLine("| [$(Markdown-Cell $style.name)]($folder/) | $(Markdown-Cell $style.theme) | $(Markdown-Cell $style.category) | $(Markdown-Cell $bestForText) | $sourceCell | `$folder/` |")
}
$mdPath = Join-Path (Resolve-Path -LiteralPath (Split-Path -Parent $CatalogMarkdown)).Path (Split-Path -Leaf $CatalogMarkdown)
[IO.File]::WriteAllText($mdPath, (Normalize-Ascii $md.ToString()) + [Environment]::NewLine, [Text.UTF8Encoding]::new($false))

Write-Output "CATALOG_STYLES=$(@($styles).Count)"
Write-Output "WROTE=$CatalogJson"
Write-Output "WROTE=$CatalogMarkdown"