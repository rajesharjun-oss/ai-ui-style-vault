param(
  [string[]]$Ids = @(),
  [string]$IdsFile = "",
  [string]$VaultRoot = ".\styles\refero-styles",
  [string]$TempRoot = "C:\tmp",
  [int]$Limit = 50,
  [int]$DelayMs = 350,
  [switch]$Force
)

$ErrorActionPreference = "Stop"

$MaxSlugLength = 80

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
  foreach ($key in $replacements.Keys) {
    $text = $text.Replace([string]$key, [string]$replacements[$key])
  }
  $normalized = $text.Normalize([Text.NormalizationForm]::FormD)
  $sb = [Text.StringBuilder]::new()
  foreach ($ch in $normalized.ToCharArray()) {
    $category = [Globalization.CharUnicodeInfo]::GetUnicodeCategory($ch)
    if ($category -eq [Globalization.UnicodeCategory]::NonSpacingMark) { continue }
    $code = [int][char]$ch
    if ($code -le 127) {
      [void]$sb.Append($ch)
    } else {
      [void]$sb.Append(" ")
    }
  }
  return ($sb.ToString() -replace '[ ]{2,}', ' ').TrimEnd()
}

function Get-MatchValue([string]$Text, [string]$Pattern, [int]$Group = 1) {
  $m = [regex]::Match($Text, $Pattern, "Singleline")
  if ($m.Success) { return $m.Groups[$Group].Value }
  return ""
}

function Get-Section([string]$Markdown, [string]$Heading) {
  $escaped = [regex]::Escape($Heading)
  $pattern = "(?ms)^## $escaped\s*(.*?)(?=^## |\z)"
  $m = [regex]::Match($Markdown, $pattern)
  if ($m.Success) { return $m.Groups[1].Value.Trim() }
  return ""
}

function Get-Subsection([string]$Markdown, [string]$Heading) {
  $escaped = [regex]::Escape($Heading)
  $pattern = "(?ms)^### $escaped\s*(.*?)(?=^### |^## |\z)"
  $m = [regex]::Match($Markdown, $pattern)
  if ($m.Success) { return $m.Groups[1].Value.Trim() }
  return ""
}

function Limit-Slug([string]$Slug, [int]$MaxLength = $MaxSlugLength) {
  if (-not $Slug) { return "refero-style" }
  if ($Slug.Length -le $MaxLength) { return $Slug }
  $trimmed = $Slug.Substring(0, $MaxLength) -replace '-+$', ''
  if (-not $trimmed) { return $Slug.Substring(0, [Math]::Min($Slug.Length, $MaxLength)) }
  return $trimmed
}

function Slugify([string]$Name) {
  $slug = (Normalize-Ascii $Name).ToLowerInvariant()
  $slug = $slug -replace '&', ' and '
  $slug = $slug -replace '[^a-z0-9]+', '-'
  $slug = $slug -replace '^-|-$', ''
  if (-not $slug) { $slug = "refero-style" }
  return (Limit-Slug $slug)
}

function Unique-Slug([string]$BaseSlug, [string]$Root, [string]$Id) {
  $base = Limit-Slug $BaseSlug
  $slug = $base
  $n = 2
  while (Test-Path -LiteralPath (Join-Path $Root $slug)) {
    $existingText = ""
    foreach ($name in @("style.json", "source.md", "README.md")) {
      $path = Join-Path (Join-Path $Root $slug) $name
      if (Test-Path -LiteralPath $path) {
        $existingText += "`n" + (Get-Content -LiteralPath $path -Raw)
      }
    }
    if ($existingText -match [regex]::Escape($Id)) { return $slug }
    $suffix = "-$n"
    $stem = Limit-Slug $base ([Math]::Max(1, $MaxSlugLength - $suffix.Length))
    $slug = "$stem$suffix"
    $n += 1
  }
  return $slug
}

function Parse-TableRows([string]$Section) {
  $rows = @()
  foreach ($line in ($Section -split "`n")) {
    $trim = $line.Trim()
    if (-not $trim.StartsWith("|")) { continue }
    if ($trim -match '^\|[-\s|]+\|$') { continue }
    $cells = $trim.Trim("|") -split "\|"
    $cells = @($cells | ForEach-Object { $_.Trim() })
    if ($cells.Count -gt 0 -and $cells[0] -match '^(Name|Role|Element|Level)$') { continue }
    if ($cells.Count -gt 0) { $rows += ,$cells }
  }
  return $rows
}

function Extract-CssBlock([string]$Markdown, [string]$Heading) {
  $marker = "### $Heading"
  $start = $Markdown.IndexOf($marker)
  if ($start -lt 0) { return "" }
  $tick = [char]96
  $codeFence = "$tick$tick$tick" + "css"
  $endFence = "$tick$tick$tick"
  $codeStart = $Markdown.IndexOf($codeFence, $start)
  if ($codeStart -lt 0) { return "" }
  $contentStart = $codeStart + $codeFence.Length
  $codeEnd = $Markdown.IndexOf($endFence, $contentStart)
  if ($codeEnd -lt 0) { return "" }
  return $Markdown.Substring($contentStart, $codeEnd - $contentStart).Trim() + "`r`n"
}

function Write-AsciiFile([string]$Path, [string]$Content) {
  $dir = Split-Path -Parent $Path
  if ($dir -and -not (Test-Path -LiteralPath $dir)) {
    New-Item -ItemType Directory -Path $dir -Force | Out-Null
  }
  Set-Content -LiteralPath $Path -Value (Normalize-Ascii $Content) -Encoding ascii
}

function Get-ExistingReferoIds([string]$Root) {
  $ids = @{}
  if (-not (Test-Path -LiteralPath $Root)) { return $ids }
  $files = Get-ChildItem -LiteralPath $Root -Recurse -File -Include "style.json", "source.md", "README.md", "DESIGN.md"
  foreach ($file in $files) {
    $text = Get-Content -LiteralPath $file.FullName -Raw
    foreach ($m in [regex]::Matches($text, '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')) {
      $ids[$m.Value] = $true
    }
  }
  return $ids
}

function Get-InputIds {
  $items = @()
  foreach ($id in $Ids) { if ($id) { $items += $id } }
  if ($IdsFile) {
    $items += Get-Content -LiteralPath $IdsFile | Where-Object { $_ -match '[0-9a-f-]{36}' }
  }
  $items |
    ForEach-Object { if ($_ -match '([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})') { $Matches[1] } } |
    Select-Object -Unique |
    Select-Object -First $Limit
}

$styleIds = @(Get-InputIds)
if ($styleIds.Count -eq 0) { throw "No Refero style IDs were provided." }

$vaultRootPath = (Resolve-Path -LiteralPath $VaultRoot).Path
$existingIds = Get-ExistingReferoIds $vaultRootPath
$capturedAt = Get-Date -Format "yyyy-MM-dd"
$captured = 0
$skipped = 0
$failed = 0

foreach ($id in $styleIds) {
  if (-not $Force -and $existingIds.ContainsKey($id)) {
    Write-Output "SKIPPED_EXISTING $id"
    $skipped += 1
    continue
  }

  try {
    $short = $id.Substring(0, 8)
    $sourceUrl = "https://styles.refero.design/style/$id"
    $htmlPath = Join-Path $TempRoot ("refero-detail-{0}.html" -f $short)

    if (-not (Test-Path -LiteralPath $htmlPath)) {
      $response = Invoke-WebRequest -Uri $sourceUrl -UseBasicParsing -TimeoutSec 45
      [IO.File]::WriteAllText($htmlPath, $response.Content, [Text.Encoding]::UTF8)
      Start-Sleep -Milliseconds $DelayMs
    }

    $html = [Text.Encoding]::UTF8.GetString([IO.File]::ReadAllBytes($htmlPath))
    $codeMatch = [regex]::Match($html, '<pre[^>]*><code[^>]*>(.*?)</code></pre>', 'Singleline')
    if (-not $codeMatch.Success) {
      throw "Could not find DESIGN.md code block"
    }

    $designRaw = [Net.WebUtility]::HtmlDecode($codeMatch.Groups[1].Value)
    $design = Normalize-Ascii ($designRaw -replace "`r", "")

    $heading = [regex]::Match($design, '(?m)^#\s*(.*?)\s*$').Groups[1].Value
    $title = Normalize-Ascii ($heading -replace '\s+-\s+Style Reference\s*$', '')
    if (-not $title -or $title -match '^\s*-?\s*Style Reference\s*$') {
      $nameFromBody = [regex]::Match($design, '(?m)^([A-Z][A-Za-z0-9][A-Za-z0-9 .&''()+/-]{1,80}?)\s+is\s+(?:a|an|the)\s+').Groups[1].Value
      $title = Normalize-Ascii $nameFromBody
    }
    if (-not $title) { $title = "Refero Style $short" }
    $northStar = Normalize-Ascii ([regex]::Match($design, '(?m)^>\s*(.+)$').Groups[1].Value)
    $theme = Normalize-Ascii (Get-MatchValue $design '\*\*Theme:\*\*\s*([^\r\n]+)')

    $referenceSite = Get-MatchValue $html ('\\"id\\":\\"{0}\\".*?\\"url\\":\\"([^\\]+)' -f [regex]::Escape($id))
    if (-not $referenceSite) { $referenceSite = Get-MatchValue $html '\\\"meta\\\":\{\\\"url\\\":\\\"([^\\]+)' }
    $siteName = Normalize-Ascii (Get-MatchValue $html ('\\"id\\":\\"{0}\\".*?\\"siteName\\":\\"([^\\]+)' -f [regex]::Escape($id)))
    if (-not $siteName) { $siteName = Normalize-Ascii (Get-MatchValue $html '\\\"meta\\\":\{\\\"url\\\":\\\"[^\\]+\\\",\\\"siteName\\\":\\\"([^\\]+)') }
    if (-not $siteName) { $siteName = $title }

    $publishedAt = Get-MatchValue $html 'property\\\":\\\"article:published_time\\\",\\\"content\\\":\\\"([^\\]+)'
    $modifiedAt = Get-MatchValue $html 'property\\\":\\\"article:modified_time\\\",\\\"content\\\":\\\"([^\\]+)'
    $category = Normalize-Ascii (Get-MatchValue $html 'property\\\":\\\"article:section\\\",\\\"content\\\":\\\"([^\\]+)')
    $summary = Normalize-Ascii (Get-MatchValue $html 'name\\\":\\\"description\\\",\\\"content\\\":\\\"([^\\]+)')

    $media = [ordered]@{}
    foreach ($key in @("screenshotUrl","thumbnailUrl","previewVideoUrl","previewVideoPosterUrl","previewVideoDetailUrl","previewVideoDetailPosterUrl","iconUrl")) {
      $value = Get-MatchValue $html ('\\"{0}\\":\\"([^\\]+)' -f $key)
      if ($value) { $media[$key] = $value }
    }

    $colorsSection = Get-Section $design "Tokens - Colors"
    $typographySection = Get-Section $design "Tokens - Typography"
    $spacingSection = Get-Section $design "Tokens - Spacing & Shapes"
    $componentsSection = Get-Section $design "Components"
    $guidelinesSection = Get-Section $design "Do's and Don'ts"
    $surfacesSection = Get-Section $design "Surfaces"
    $elevationSection = Get-Section $design "Elevation"
    $imagerySection = Get-Section $design "Imagery"
    $layoutSection = Get-Section $design "Layout"
    $agentPromptSection = Get-Section $design "Agent Prompt Guide"

    $colors = @()
    foreach ($row in (Parse-TableRows $colorsSection)) {
      if ($row.Count -ge 4 -and $row[1] -match '`?(#[0-9a-fA-F]{6})`?') {
        $colors += [ordered]@{
          name = Normalize-Ascii $row[0]
          value = $Matches[1].ToLowerInvariant()
          token = (($row[2] -replace '`','').Trim())
          role = Normalize-Ascii $row[3]
        }
      }
    }

    $typeScale = @()
    $typeScaleSection = Get-Subsection $typographySection "Type Scale"
    foreach ($row in (Parse-TableRows $typeScaleSection)) {
      if ($row.Count -ge 5) {
        $typeScale += ,@(
          (Normalize-Ascii $row[0]),
          (Normalize-Ascii $row[1]),
          (Normalize-Ascii $row[2]),
          (Normalize-Ascii $row[3]),
          (($row[4] -replace '`','').Trim())
        )
      }
    }

    $fonts = @()
    foreach ($m in [regex]::Matches($typographySection, '(?m)^###\s+(.+?)\s+-\s+(.+?)\s+-\s+`(--font-[^`]+)`')) {
      $fonts += [ordered]@{
        name = Normalize-Ascii $m.Groups[1].Value
        token = $m.Groups[3].Value
        role = Normalize-Ascii $m.Groups[2].Value
      }
    }
    if ($fonts.Count -eq 0) {
      foreach ($m in [regex]::Matches($typographySection, '(--font-[a-z0-9-]+)')) {
        $fonts += [ordered]@{
          name = (($m.Groups[1].Value -replace '^--font-','') -replace '-', ' ')
          token = $m.Groups[1].Value
          role = "Source typography token"
        }
      }
    }

    $spacingRows = Parse-TableRows (Get-Subsection $spacingSection "Spacing Scale")
    $radiiRows = Parse-TableRows (Get-Subsection $spacingSection "Border Radius")
    $baseUnit = Normalize-Ascii (Get-MatchValue $spacingSection '\*\*Base unit:\*\*\s*([^\r\n]+)')
    $density = Normalize-Ascii (Get-MatchValue $spacingSection '\*\*Density:\*\*\s*([^\r\n]+)')
    $maxWidth = Normalize-Ascii (Get-MatchValue $spacingSection '\*\*Page max-width:\*\*\s*([^\r\n]+)')
    $sectionGap = Normalize-Ascii (Get-MatchValue $spacingSection '\*\*Section gap:\*\*\s*([^\r\n]+)')
    $cardPadding = Normalize-Ascii (Get-MatchValue $spacingSection '\*\*Card padding:\*\*\s*([^\r\n]+)')
    $elementGap = Normalize-Ascii (Get-MatchValue $spacingSection '\*\*Element gap:\*\*\s*([^\r\n]+)')

    $components = @()
    foreach ($m in [regex]::Matches($componentsSection, '(?ms)^###\s+(.+?)\s*\n\*\*Role:\*\*\s*(.*?)(?=\n\n|$)')) {
      $components += [ordered]@{
        name = Normalize-Ascii $m.Groups[1].Value
        role = Normalize-Ascii $m.Groups[2].Value
      }
    }

    $doText = Get-Subsection $guidelinesSection "Do"
    $dontText = Get-Subsection $guidelinesSection "Don't"
    $dos = @($doText -split "`n" | Where-Object { $_.Trim().StartsWith("- ") } | ForEach-Object { Normalize-Ascii ($_.Trim() -replace '^- ', '') })
    $donts = @($dontText -split "`n" | Where-Object { $_.Trim().StartsWith("- ") } | ForEach-Object { Normalize-Ascii ($_.Trim() -replace '^- ', '') })

    $cssVariables = Normalize-Ascii (Extract-CssBlock $design "CSS Custom Properties")
    $tailwind = Normalize-Ascii (Extract-CssBlock $design "Tailwind v4")

    $slug = Unique-Slug (Slugify $siteName) $vaultRootPath $id
    $root = Join-Path $vaultRootPath $slug
    New-Item -ItemType Directory -Path $root -Force | Out-Null
    foreach ($sub in @("tokens","code","screenshots")) {
      New-Item -ItemType Directory -Path (Join-Path $root $sub) -Force | Out-Null
    }

    $styleJson = [ordered]@{
      id = $id
      name = $siteName
      slug = $slug
      source = [ordered]@{
        referoUrl = $sourceUrl
        referenceSite = $referenceSite
        capturedAt = $capturedAt
        publishedAt = $publishedAt
        articleModifiedAt = $modifiedAt
        media = $media
      }
      classification = [ordered]@{
        theme = $theme
        category = $category
        mood = @("source-derived")
        bestFor = @($category, "AI-assisted UI implementation") | Where-Object { $_ }
      }
      northStar = $northStar
      summary = $summary
      colors = $colors
      typography = [ordered]@{
        fonts = $fonts
        typeScale = $typeScale
      }
      spacing = [ordered]@{
        baseUnit = $baseUnit
        density = $density
        maxWidth = $maxWidth
        sectionGap = $sectionGap
        cardPadding = $cardPadding
        elementGap = $elementGap
        scale = $spacingRows
      }
      shape = [ordered]@{
        radii = $radiiRows
      }
      components = $components
      dos = $dos
      donts = $donts
      surfaces = $surfacesSection
      elevation = $elevationSection
      imagery = $imagerySection
      layout = $layoutSection
    }

    $tokensJson = [ordered]@{
      name = $siteName
      slug = $slug
      colors = $colors
      fonts = $fonts
      typeScale = $typeScale
      spacing = $styleJson.spacing
      radii = $radiiRows
      components = $components
      guidelines = [ordered]@{ do = $dos; doNot = $donts }
      source = $styleJson.source
    }

    $colorBullets = ($colors | ForEach-Object { ('- {0} `{1}` for {2}' -f $_.name, $_.value, $_.role) }) -join "`n"
    $fontBullets = ($fonts | ForEach-Object { ('- {0} `{1}` for {2}' -f $_.name, $_.token, $_.role) }) -join "`n"
    $componentBullets = ($components | Select-Object -First 12 | ForEach-Object { "- $($_.name): $($_.role)" }) -join "`n"
    $doBullets = ($dos | ForEach-Object { "- $_" }) -join "`n"
    $dontBullets = ($donts | ForEach-Object { "- $_" }) -join "`n"

    Write-AsciiFile (Join-Path $root "DESIGN.md") $design
    Write-AsciiFile (Join-Path $root "README.md") @"
# $siteName

Source: [Refero Style]($sourceUrl)
Reference site: [$referenceSite]($referenceSite)
Captured: $capturedAt
Refero published: $publishedAt
Refero modified: $modifiedAt
Theme: $theme
Category: $category

## Style Summary

$summary

North star: $northStar

## What To Borrow

$colorBullets

$fontBullets

## Avoid

$dontBullets

## Bundle Contents

- [DESIGN.md](DESIGN.md): full source-derived implementation reference.
- [implementation-prompt.md](implementation-prompt.md): ready-to-paste prompt for an AI builder.
- [style.json](style.json): structured style metadata and token summary.
- [tokens/colors.md](tokens/colors.md): palette and surface rules.
- [tokens/typography.md](tokens/typography.md): type scale and font rules.
- [tokens/spacing-shape.md](tokens/spacing-shape.md): spacing and radius rules.
- [tokens/components.md](tokens/components.md): component recipes.
- [tokens/guidelines.md](tokens/guidelines.md): do and do-not guidance.
- [tokens/layout-imagery.md](tokens/layout-imagery.md): layout and imagery direction.
- [code/css-variables.css](code/css-variables.css): CSS variable starter.
- [code/tailwind-v4.css](code/tailwind-v4.css): Tailwind v4 token starter.
- [code/design-tokens.json](code/design-tokens.json): portable token JSON.
- [screenshots/README.md](screenshots/README.md): source media references.
"@

    Write-AsciiFile (Join-Path $root "source.md") @"
# Source Metadata

## Links

- Refero style URL: $sourceUrl
- Reference site: $referenceSite
- Refero title: $siteName design system | Refero Styles

## Capture

- Captured by Codex: $capturedAt
- Discovery mode: public Refero styles sitemap
- Duplicate status: new at capture time
- Vault slug: $slug
- Theme: $theme
- Category: $category
- Refero published timestamp: $publishedAt
- Refero article modified timestamp: $modifiedAt

## Reference Media

- Primary schema screenshot: $($media.screenshotUrl)
- Thumbnail: $($media.thumbnailUrl)
- Social/inline preview image: $($media.previewVideoPosterUrl)
- Inline preview video: $($media.previewVideoUrl)
- Detail preview poster: $($media.previewVideoDetailPosterUrl)
- Detail preview video: $($media.previewVideoDetailUrl)
- Icon: $($media.iconUrl)

## Source Signals

- North star: $northStar
- Primary colors: $((@($colors | ForEach-Object { $_.name }) | Select-Object -First 8) -join ', ')
- Primary fonts: $((@($fonts | ForEach-Object { $_.name }) | Select-Object -First 6) -join ', ')
- Base spacing: $baseUnit
- Density: $density

## Notes

This bundle is a source-derived implementation reference for AI-assisted UI building. It captures design tokens, component behavior, remote media references, and usage guidance needed to recreate the style without mirroring the full Refero page verbatim.
"@

    Write-AsciiFile (Join-Path $root "implementation-prompt.md") @"
# AI Implementation Prompt

Build a $siteName-inspired interface using this source-derived style bundle.

Reference site: $referenceSite
Theme: $theme
Category: $category
North star: $northStar

Use these palette anchors:

$colorBullets

Use these typography anchors:

$fontBullets

Use these layout rules:

- Base spacing: $baseUnit.
- Density: $density.
- Page max-width: $maxWidth.
- Section gap: $sectionGap.
- Card padding: $cardPadding.
- Element gap: $elementGap.

Build these component patterns where relevant:

$componentBullets

Do:

$doBullets

Avoid:

$dontBullets

Source prompt cues:

$agentPromptSection

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
"@

    Write-AsciiFile (Join-Path $root "tokens/colors.md") "# Colors`n`n$colorsSection`n"
    Write-AsciiFile (Join-Path $root "tokens/typography.md") "# Typography`n`n$typographySection`n"
    Write-AsciiFile (Join-Path $root "tokens/spacing-shape.md") "# Spacing & Shape`n`n$spacingSection`n"
    Write-AsciiFile (Join-Path $root "tokens/components.md") "# Components`n`n$componentsSection`n"
    Write-AsciiFile (Join-Path $root "tokens/guidelines.md") @"
# Guidelines

$guidelinesSection

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
"@
    Write-AsciiFile (Join-Path $root "tokens/layout-imagery.md") @"
# Layout & Imagery

## Layout

$layoutSection

## Surfaces

$surfacesSection

## Elevation

$elevationSection

## Imagery

$imagerySection
"@
    Write-AsciiFile (Join-Path $root "code/css-variables.css") $cssVariables
    Write-AsciiFile (Join-Path $root "code/tailwind-v4.css") $tailwind
    Write-AsciiFile (Join-Path $root "code/design-tokens.json") (($tokensJson | ConvertTo-Json -Depth 20) + "`n")
    Write-AsciiFile (Join-Path $root "style.json") (($styleJson | ConvertTo-Json -Depth 20) + "`n")
    Write-AsciiFile (Join-Path $root "screenshots/README.md") @"
# Source Media

The binary media files are not downloaded into the vault. Use these Refero-hosted public references when visual inspection is needed.

- Screenshot: $($media.screenshotUrl)
- Thumbnail: $($media.thumbnailUrl)
- Preview poster: $($media.previewVideoPosterUrl)
- Preview video: $($media.previewVideoUrl)
- Detail poster: $($media.previewVideoDetailPosterUrl)
- Detail video: $($media.previewVideoDetailUrl)
- Icon: $($media.iconUrl)
"@

    $existingIds[$id] = $true
    $captured += 1
    Write-Output "CAPTURED $slug | $siteName | $id"
  } catch {
    $failed += 1
    Write-Warning "FAILED $id | $($_.Exception.Message)"
  }
}

Write-Output "CAPTURED_COUNT=$captured"
Write-Output "SKIPPED_COUNT=$skipped"
Write-Output "FAILED_COUNT=$failed"
