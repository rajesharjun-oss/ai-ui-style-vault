param(
  [string]$VaultRoot = ".\outputs\ai-ui-style-vault\styles\refero-styles",
  [string]$TempRoot = "C:\tmp"
)

$ErrorActionPreference = "Stop"

$styles = @(
  @{ id = "01d6013d-a176-4a22-b7dd-fbd113592956"; short = "01d6013d" },
  @{ id = "03e03554-d7aa-40da-9764-79320ecfa1d0"; short = "03e03554" },
  @{ id = "0769ff4c-f719-4865-98df-de2f44c694a6"; short = "0769ff4c" },
  @{ id = "08c8700c-f278-42bc-812e-f60dc6ce996e"; short = "08c8700c" },
  @{ id = "0acef011-07da-4416-b874-ccdd675140f6"; short = "0acef011" },
  @{ id = "0b9da6ef-bec5-4073-90af-66c67e72f2a4"; short = "0b9da6ef" },
  @{ id = "0c0b6140-2b6c-44f8-8bba-4ecfcadba420"; short = "0c0b6140" },
  @{ id = "0ed4e85f-f3e9-438c-bc34-2a726863c602"; short = "0ed4e85f" },
  @{ id = "0f0d4cb7-5109-4e81-8c8d-f6bd0441b27c"; short = "0f0d4cb7" },
  @{ id = "14f10100-a102-427a-88d1-7cc80cbb332d"; short = "14f10100" },
  @{ id = "16a8de02-a4c6-4077-9d3a-ef6b5c10db12"; short = "16a8de02" },
  @{ id = "16be276a-d8ce-484e-8f7a-cbbb09f717f7"; short = "16be276a" },
  @{ id = "186775da-7568-49e5-8110-4fd0bbc7bbe3"; short = "186775da" },
  @{ id = "19d4103a-9f4a-49f0-ad7d-af6588bab904"; short = "19d4103a" },
  @{ id = "1ad4f49f-275a-4268-8ed1-677dc3c6e475"; short = "1ad4f49f" },
  @{ id = "1b010453-80df-406a-8b1a-72630c4a5165"; short = "1b010453" }
)
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

function Slugify([string]$Name) {
  $slug = (Normalize-Ascii $Name).ToLowerInvariant()
  $slug = $slug -replace '&', ' and '
  $slug = $slug -replace '[^a-z0-9]+', '-'
  $slug = $slug -replace '^-|-$', ''
  if (-not $slug) { $slug = "refero-style" }
  return $slug
}

function Unique-Slug([string]$BaseSlug, [string]$Root, [string]$Id) {
  $slug = $BaseSlug
  $n = 2
  while (Test-Path -LiteralPath (Join-Path $Root $slug)) {
    $existingJson = Join-Path (Join-Path $Root $slug) "style.json"
    if (Test-Path -LiteralPath $existingJson) {
      try {
        $existing = Get-Content -LiteralPath $existingJson -Raw | ConvertFrom-Json
        if ($existing.id -eq $Id) { return $slug }
      } catch {}
    }
    $slug = "$BaseSlug-$n"
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

foreach ($styleRef in $styles) {
  $id = $styleRef.id
  $htmlPath = Join-Path $TempRoot ("refero-detail-{0}.html" -f $styleRef.short)
  if (-not (Test-Path -LiteralPath $htmlPath)) {
    throw "Missing fetched Refero HTML: $htmlPath"
  }

  $html = [Text.Encoding]::UTF8.GetString([IO.File]::ReadAllBytes($htmlPath))
  $codeMatch = [regex]::Match($html, '<pre[^>]*><code[^>]*>(.*?)</code></pre>', 'Singleline')
  if (-not $codeMatch.Success) {
    throw "Could not find DESIGN.md code block for $id"
  }

  $designRaw = [Net.WebUtility]::HtmlDecode($codeMatch.Groups[1].Value)
  $design = Normalize-Ascii ($designRaw -replace "`r", "")

  $title = Normalize-Ascii (Get-MatchValue $design '^#\s+(.+?)\s+-\s+Style Reference')
  if (-not $title) { $title = Normalize-Ascii (Get-MatchValue $design '^#\s+(.+)$') }
  $northStar = Normalize-Ascii ([regex]::Match($design, '(?m)^>\s*(.+)$').Groups[1].Value)
  $theme = Normalize-Ascii (Get-MatchValue $design '\*\*Theme:\*\*\s*([^\r\n]+)')

  $referenceSite = Get-MatchValue $html '\\\"meta\\\":\{\\\"url\\\":\\\"([^\\]+)'
  $siteName = Normalize-Ascii (Get-MatchValue $html '\\\"meta\\\":\{\\\"url\\\":\\\"[^\\]+\\\",\\\"siteName\\\":\\\"([^\\]+)')
  if (-not $siteName) { $siteName = $title }
  $publishedAt = Get-MatchValue $html 'property\\\":\\\"article:published_time\\\",\\\"content\\\":\\\"([^\\]+)'
  $modifiedAt = Get-MatchValue $html 'property\\\":\\\"article:modified_time\\\",\\\"content\\\":\\\"([^\\]+)'
  $category = Normalize-Ascii (Get-MatchValue $html 'property\\\":\\\"article:section\\\",\\\"content\\\":\\\"([^\\]+)')
  $summary = Normalize-Ascii (Get-MatchValue $html 'name\\\":\\\"description\\\",\\\"content\\\":\\\"([^\\]+)')

  $media = [ordered]@{}
  foreach ($key in @("screenshotUrl","previewVideoUrl","previewVideoPosterUrl","previewVideoDetailUrl","previewVideoDetailPosterUrl","iconUrl")) {
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

  $slug = Unique-Slug (Slugify $siteName) $VaultRoot $id
  $root = Join-Path $VaultRoot $slug
  New-Item -ItemType Directory -Path $root -Force | Out-Null
  foreach ($sub in @("tokens","code","screenshots")) {
    New-Item -ItemType Directory -Path (Join-Path $root $sub) -Force | Out-Null
  }

  $sourceUrl = "https://styles.refero.design/style/$id"
  $capturedAt = "2026-07-29"

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
- Discovery mode: autonomous Refero gallery pick
- Duplicate status: new at capture time
- Vault slug: $slug
- Theme: $theme
- Category: $category
- Refero published timestamp: $publishedAt
- Refero article modified timestamp: $modifiedAt

## Reference Media

- Primary schema screenshot: $($media.screenshotUrl)
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

This bundle is a source-derived implementation reference for AI-assisted UI building. It captures the design tokens, component behavior, media references, and usage guidance needed to recreate the style without mirroring the full Refero page verbatim.
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
- Preview poster: $($media.previewVideoPosterUrl)
- Preview video: $($media.previewVideoUrl)
- Detail poster: $($media.previewVideoDetailPosterUrl)
- Detail video: $($media.previewVideoDetailUrl)
- Icon: $($media.iconUrl)
"@

  "CAPTURED $slug | $siteName"
}

