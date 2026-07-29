param(
  [string]$InputRoot = "C:\tmp",
  [string]$OutputRoot = ".\screens\refero",
  [string]$CatalogJson = ".\screen-catalog.json",
  [string]$CatalogMarkdown = ".\SCREEN_REFERENCES.md",
  [int]$PerChannelPerType = 2
)

$ErrorActionPreference = "Stop"

$pageTypes = @(
  [ordered]@{ id = 28; name = "Dashboard"; slug = "dashboard"; mode = "apps-first" },
  [ordered]@{ id = 44; name = "Product Page & Landing"; slug = "product-page-landing"; mode = "web-first" },
  [ordered]@{ id = 13; name = "Paywall & Subscription"; slug = "paywall-subscription"; mode = "apps-first" },
  [ordered]@{ id = 18; name = "Log In"; slug = "login"; mode = "apps-first" },
  [ordered]@{ id = 47; name = "Product Details"; slug = "product-details"; mode = "apps-first" },
  [ordered]@{ id = 15; name = "Profile & Account"; slug = "profile-account"; mode = "apps-first" },
  [ordered]@{ id = 41; name = "404 Page"; slug = "404-page"; mode = "web-first" },
  [ordered]@{ id = 5; name = "Catalog Page"; slug = "catalog-page"; mode = "apps-first" },
  [ordered]@{ id = 46; name = "Blog"; slug = "blog"; mode = "web-first" },
  [ordered]@{ id = 33; name = "About"; slug = "about"; mode = "web-first" },
  [ordered]@{ id = 35; name = "Careers"; slug = "careers"; mode = "web-first" },
  [ordered]@{ id = 34; name = "Contacts"; slug = "contacts"; mode = "web-first" },
  [ordered]@{ id = 39; name = "Developers Page"; slug = "developers-page"; mode = "web-first" },
  [ordered]@{ id = 40; name = "Integration Page"; slug = "integration-page"; mode = "web-first" },
  [ordered]@{ id = 36; name = "Media Kit"; slug = "media-kit"; mode = "web-first" }
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
  foreach ($key in $replacements.Keys) { $text = $text.Replace([string]$key, [string]$replacements[$key]) }
  $normalized = $text.Normalize([Text.NormalizationForm]::FormD)
  $sb = [Text.StringBuilder]::new()
  foreach ($ch in $normalized.ToCharArray()) {
    if ([Globalization.CharUnicodeInfo]::GetUnicodeCategory($ch) -eq [Globalization.UnicodeCategory]::NonSpacingMark) { continue }
    if ([int][char]$ch -le 127) { [void]$sb.Append($ch) } else { [void]$sb.Append(" ") }
  }
  return ($sb.ToString() -replace '[ ]{2,}', ' ').Trim()
}

function Clean-Text([object]$Value) {
  return ((Normalize-Ascii ([string]$Value)) -replace '\s+', ' ').Trim()
}

function Slugify([object]$Value) {
  $text = (Clean-Text $Value).ToLowerInvariant()
  $text = $text -replace '&', ' and '
  $text = $text -replace '[^a-z0-9]+', '-'
  $text = $text.Trim('-')
  if ([string]::IsNullOrWhiteSpace($text)) { return "untitled" }
  return $text
}

function First-Text([object[]]$Values) {
  foreach ($value in $Values) {
    $text = Clean-Text $value
    if (-not [string]::IsNullOrWhiteSpace($text)) { return $text }
  }
  return ""
}

function String-List([object]$Value) {
  $items = @()
  if ($null -eq $Value) { return $items }
  foreach ($item in @($Value)) {
    $text = Clean-Text $item
    if ($text -and -not $items.Contains($text)) { $items += $text }
  }
  return $items
}

function Rgb-ToHex([object]$Rgb) {
  $channels = @($Rgb)
  if ($channels.Count -lt 3) { return "" }
  try {
    return ("#{0:x2}{1:x2}{2:x2}" -f [int]$channels[0], [int]$channels[1], [int]$channels[2])
  } catch {
    return ""
  }
}

function Url-List([object]$Value) {
  $items = @()
  if ($null -eq $Value) { return $items }
  if ($Value -is [array]) {
    foreach ($item in @($Value)) {
      $text = Clean-Text $item
      if ($text) { $items += $text }
    }
  } else {
    $text = Clean-Text $Value
    if ($text) { $items += $text }
  }
  return $items
}

function Names-FromRecords([object]$Records) {
  $items = @()
  foreach ($record in @($Records)) {
    $name = First-Text @($record.name, $record.display_name)
    if ($name -and -not $items.Contains($name)) { $items += $name }
  }
  return $items
}

function Ensure-Directory([string]$Path) {
  if (-not (Test-Path -LiteralPath $Path -PathType Container)) {
    New-Item -ItemType Directory -Path $Path | Out-Null
  }
}

function Write-Text([string]$Path, [string]$Text) {
  $dir = Split-Path -Parent $Path
  Ensure-Directory $dir
  [IO.File]::WriteAllText($Path, (Normalize-Ascii $Text) + [Environment]::NewLine, [Text.UTF8Encoding]::new($false))
}

function Markdown-Cell([object]$Value) {
  $text = Clean-Text $Value
  if ([string]::IsNullOrWhiteSpace($text)) { return "-" }
  return $text.Replace("|", "\|")
}

function Channel-SearchUrl([string]$Channel, [int]$PageTypeId) {
  if ($Channel -eq "ios-apps") { return "https://refero.design/apps/search?page_types[id][]=$PageTypeId&order=trending" }
  return "https://refero.design/search?page_types[id][]=$PageTypeId&order=trending"
}

function Api-SearchUrl([string]$Channel, [int]$PageTypeId) {
  if ($Channel -eq "ios-apps") { return "https://api.refero.design/v1/search/apps?page_types[id][]=$PageTypeId" }
  return "https://api.refero.design/v1/search?page_types[id][]=$PageTypeId"
}

function Entity-Info([object]$Record, [string]$Channel) {
  if ($Channel -eq "ios-apps") {
    return [ordered]@{
      kind = "iOS app"
      name = First-Text @($Record.app.name, "Unknown app")
      description = First-Text @($Record.app.description)
      url = First-Text @($Record.app.store_url)
      iconUrl = First-Text @($Record.app.icon_url)
      backgroundColor = First-Text @($Record.app.background_color)
      id = First-Text @($Record.app.id)
    }
  }
  $domain = First-Text @($Record.site.domain)
  $siteUrl = First-Text @($Record.page_url)
  if (-not $siteUrl -and $domain) { $siteUrl = "https://$domain" }
  return [ordered]@{
    kind = "website"
    name = First-Text @($Record.site.name, $domain, "Unknown site")
    description = First-Text @($Record.site.description)
    url = $siteUrl
    iconUrl = First-Text @($Record.site.favicon_url)
    backgroundColor = ""
    id = First-Text @($Record.site.id)
  }
}

function Selected-Record([object]$Record, [hashtable]$PageType, [string]$Channel) {
  $entity = Entity-Info $Record $Channel
  $imageUrls = Url-List $Record.url
  $colors = @()
  $index = 1
  foreach ($rgb in @($Record.colors)) {
    $hex = Rgb-ToHex $rgb
    if ($hex) {
      $colors += [ordered]@{ name = "screen-color-$index"; value = $hex; rgb = @($rgb) }
      $index++
    }
  }
  $patterns = Names-FromRecords $Record.design_patterns
  $elements = Names-FromRecords $Record.page_elements
  $types = Names-FromRecords $Record.page_types
  $fonts = Names-FromRecords $Record.fonts
  $uuid = First-Text @($Record.uuid)
  $referoViewUrl = ""
  if ($uuid) { $referoViewUrl = "https://refero.design/view/$uuid" }
  return [ordered]@{
    id = First-Text @($Record.id)
    uuid = $uuid
    source = "Refero"
    channel = $Channel
    pageType = [ordered]@{ id = $PageType.id; name = $PageType.name; slug = $PageType.slug }
    entity = $entity
    createdAt = First-Text @($Record.created_at)
    referoViewUrl = $referoViewUrl
    referoSearchUrl = Channel-SearchUrl $Channel $PageType.id
    referoApiSearchUrl = Api-SearchUrl $Channel $PageType.id
    thumbnailUrl = First-Text @($Record.thumbnail_url)
    previewUrl = First-Text @($Record.preview_url)
    imageUrls = $imageUrls
    videoUrl = First-Text @($Record.video_url)
    videoPreviewUrl = First-Text @($Record.video_preview_url)
    singleScreen = [bool]$Record.single_screen
    colors = $colors
    designPatterns = $patterns
    pageElements = $elements
    pageTypes = $types
    fonts = $fonts
    licenseStatus = "inspiration-only-unless-explicitly-licensed"
  }
}

function Write-ReferenceFiles([object]$Item, [string]$FolderPath, [string]$RelativePath) {
  $title = "$($Item.entity.name) - $($Item.pageType.name)"
  $channelLabel = if ($Item.channel -eq "ios-apps") { "Refero iOS Apps" } else { "Refero Web Screens" }
  $surface = if ($Item.channel -eq "ios-apps") { "mobile app screen" } else { "web page screenshot set" }
  $colorSummary = if (@($Item.colors).Count -gt 0) { (@($Item.colors | ForEach-Object { "$($_.name) $($_.value)" }) -join ", ") } else { "No palette extracted." }
  $patterns = if (@($Item.designPatterns).Count -gt 0) { $Item.designPatterns -join ", " } else { "Not tagged." }
  $elements = if (@($Item.pageElements).Count -gt 0) { $Item.pageElements -join ", " } else { "Not tagged." }
  $fonts = if (@($Item.fonts).Count -gt 0) { $Item.fonts -join ", " } else { "Not detected." }
  $primaryImage = First-Text @($Item.previewUrl, $Item.thumbnailUrl, @($Item.imageUrls | Select-Object -First 1))

  $readme = @"
# $title

## Summary

- Source: $channelLabel
- Channel: $($Item.channel)
- Page type: $($Item.pageType.name)
- Entity: $($Item.entity.name)
- Surface: $surface
- Refero view: $($Item.referoViewUrl)
- Refero search: $($Item.referoSearchUrl)
- Entity URL: $($Item.entity.url)
- Captured on: $(Get-Date -Format "yyyy-MM-dd")
- License status: $($Item.licenseStatus)

## AI Usage

Use this as visual direction for an original $($Item.pageType.name) implementation. Preserve the broad UX signals, palette relationship, density, component priorities, and page-type intent. Do not copy logos, trademarked assets, original text, exact screenshot composition, or proprietary product visuals.

## Captured Artifacts

- source.md
- implementation-prompt.md
- screen.json
- tokens/colors.md
- tokens/page-elements.md
- code/css-variables.css
- code/design-tokens.json
- screenshots/README.md
"@

  $source = @"
# Source Metadata

## Links

- Refero view URL: $($Item.referoViewUrl)
- Refero filtered search URL: $($Item.referoSearchUrl)
- Refero API search URL: $($Item.referoApiSearchUrl)
- Entity URL: $($Item.entity.url)
- Primary media URL: $primaryImage
- Thumbnail URL: $($Item.thumbnailUrl)
- Preview URL: $($Item.previewUrl)

## Capture

- Captured by Codex: $(Get-Date -Format "yyyy-MM-dd")
- Discovery mode: bounded public Refero page-type search
- Channel: $($Item.channel)
- Page type ID: $($Item.pageType.id)
- Screen ID: $($Item.id)
- Screen UUID: $($Item.uuid)
- Vault path: $RelativePath
- License status: $($Item.licenseStatus)

## Reference Media

- Media files are not vendored in this public-friendly vault bundle.
- Remote image URLs are preserved in screenshots/README.md and screen.json so AI agents can inspect the original source when permitted.

## Source Signals

- Colors: $colorSummary
- Design patterns: $patterns
- Page elements: $elements
- Fonts: $fonts
"@

  $prompt = @"
# AI Implementation Prompt

Build an original $($Item.pageType.name) UI inspired by this Refero $surface reference for $($Item.entity.name).

Use these signals:

- Channel: $($Item.channel)
- Entity type: $($Item.entity.kind)
- Entity description: $($Item.entity.description)
- Palette: $colorSummary
- Page elements: $elements
- Design patterns: $patterns
- Fonts observed: $fonts

Implementation guidance:

- Create a fresh layout that solves the same page-type job without copying the screenshot.
- Keep the strongest visual priorities from the reference: hierarchy, density, dominant controls, image rhythm, and empty/loading states implied by the page type.
- Use the extracted colors as inspiration, then adapt them into accessible tokens for the target product.
- Replace all brand/product copy, logos, photography, icons, and app-specific data with original material for the new project.
- If building production UI, add responsive states, keyboard focus, accessible labels, validation or empty states where the page type requires them, and server-side authorization for protected product areas.
"@

  $colorMd = [Text.StringBuilder]::new()
  [void]$colorMd.AppendLine("# Color Tokens")
  [void]$colorMd.AppendLine("")
  [void]$colorMd.AppendLine("| Token | Hex | RGB |")
  [void]$colorMd.AppendLine("|---|---|---|")
  foreach ($color in @($Item.colors)) {
    $rgbText = (@($color.rgb) -join ", ")
    [void]$colorMd.AppendLine("| $($color.name) | ``$($color.value)`` | $rgbText |")
  }
  if (@($Item.colors).Count -eq 0) { [void]$colorMd.AppendLine("| - | - | - |") }

  $elementsMd = @"
# Page Elements

## Page Types

$((@($Item.pageTypes) | ForEach-Object { "- $_" }) -join [Environment]::NewLine)

## Design Patterns

$((@($Item.designPatterns) | ForEach-Object { "- $_" }) -join [Environment]::NewLine)

## Elements

$((@($Item.pageElements) | ForEach-Object { "- $_" }) -join [Environment]::NewLine)

## Fonts

$((@($Item.fonts) | ForEach-Object { "- $_" }) -join [Environment]::NewLine)
"@

  $css = [Text.StringBuilder]::new()
  [void]$css.AppendLine(":root {")
  foreach ($color in @($Item.colors)) {
    [void]$css.AppendLine("  --refero-$($Item.pageType.slug)-$($color.name): $($color.value);")
  }
  [void]$css.AppendLine("}")

  $screenShots = [Text.StringBuilder]::new()
  [void]$screenShots.AppendLine("# Screenshot References")
  [void]$screenShots.AppendLine("")
  [void]$screenShots.AppendLine("Media files are not copied into this repository. Use these source links for inspection when the original Refero material is available and permitted.")
  [void]$screenShots.AppendLine("")
  [void]$screenShots.AppendLine("- Thumbnail URL: $($Item.thumbnailUrl)")
  [void]$screenShots.AppendLine("- Preview URL: $($Item.previewUrl)")
  [void]$screenShots.AppendLine("- Video URL: $($Item.videoUrl)")
  [void]$screenShots.AppendLine("- Video preview URL: $($Item.videoPreviewUrl)")
  [void]$screenShots.AppendLine("")
  [void]$screenShots.AppendLine("## Image URLs")
  foreach ($url in @($Item.imageUrls)) { [void]$screenShots.AppendLine("- $url") }

  Write-Text (Join-Path $FolderPath "README.md") $readme
  Write-Text (Join-Path $FolderPath "source.md") $source
  Write-Text (Join-Path $FolderPath "implementation-prompt.md") $prompt
  Write-Text (Join-Path $FolderPath "tokens/colors.md") $colorMd.ToString()
  Write-Text (Join-Path $FolderPath "tokens/page-elements.md") $elementsMd
  Write-Text (Join-Path $FolderPath "code/css-variables.css") $css.ToString()
  Write-Text (Join-Path $FolderPath "screenshots/README.md") $screenShots.ToString()
  Write-Text (Join-Path $FolderPath "screen.json") (($Item | ConvertTo-Json -Depth 24))
  Write-Text (Join-Path $FolderPath "code/design-tokens.json") (([ordered]@{
    pageType = $Item.pageType
    entity = $Item.entity
    colors = $Item.colors
    pageElements = $Item.pageElements
    designPatterns = $Item.designPatterns
    fonts = $Item.fonts
    media = [ordered]@{
      thumbnailUrl = $Item.thumbnailUrl
      previewUrl = $Item.previewUrl
      imageUrls = $Item.imageUrls
      videoUrl = $Item.videoUrl
      videoPreviewUrl = $Item.videoPreviewUrl
    }
  } | ConvertTo-Json -Depth 24))
}

$outputRootPath = Join-Path (Resolve-Path -LiteralPath ".").Path $OutputRoot
Ensure-Directory $outputRootPath

$items = @()
$pageTypeCatalog = @()
$seen = @{}

foreach ($pageType in $pageTypes) {
  $pageTypeStats = [ordered]@{
    id = $pageType.id
    name = $pageType.name
    slug = $pageType.slug
    mode = $pageType.mode
    iosAppMatches = 0
    webMatches = 0
    captured = 0
  }

  foreach ($channel in @("ios-apps", "web")) {
    $prefix = if ($channel -eq "ios-apps") { "refero-apps" } else { "refero-web" }
    $inputPath = Join-Path $InputRoot "$prefix-pt-$($pageType.id).json"
    if (-not (Test-Path -LiteralPath $inputPath -PathType Leaf)) { continue }
    $json = Get-Content -LiteralPath $inputPath -Raw | ConvertFrom-Json
    $records = @($json.records | Where-Object {
      $match = $false
      foreach ($type in @($_.page_types)) { if ([int]$type.id -eq [int]$pageType.id) { $match = $true } }
      return $match
    })
    if ($channel -eq "ios-apps") { $pageTypeStats.iosAppMatches = [int]$json.pagination.count } else { $pageTypeStats.webMatches = [int]$json.pagination.count }

    $selected = $records | Select-Object -First $PerChannelPerType
    foreach ($record in @($selected)) {
      $key = "$channel-$($record.id)"
      if ($seen.ContainsKey($key)) { continue }
      $seen[$key] = $true
      $item = Selected-Record $record $pageType $channel
      $entitySlug = Slugify $item.entity.name
      $folderSlug = "$entitySlug-screen-$($item.id)"
      $relativePath = "screens/refero/$channel/$($pageType.slug)/$folderSlug"
      $folderPath = Join-Path (Resolve-Path -LiteralPath ".").Path $relativePath
      Write-ReferenceFiles $item $folderPath $relativePath
      $item.path = $relativePath
      $item.files = [ordered]@{
        readme = "$relativePath/README.md"
        source = "$relativePath/source.md"
        prompt = "$relativePath/implementation-prompt.md"
        screen = "$relativePath/screen.json"
        colors = "$relativePath/tokens/colors.md"
        pageElements = "$relativePath/tokens/page-elements.md"
        cssVariables = "$relativePath/code/css-variables.css"
        designTokens = "$relativePath/code/design-tokens.json"
        screenshots = "$relativePath/screenshots/README.md"
      }
      $items += $item
      $pageTypeStats.captured++
    }
  }
  $pageTypeCatalog += $pageTypeStats
}

Write-Text (Join-Path $outputRootPath "page-types.json") (($pageTypeCatalog | ConvertTo-Json -Depth 12))

$catalog = [ordered]@{
  name = "AI UI Style Vault - Refero Screen References"
  generatedAt = (Get-Date -Format "yyyy-MM-dd")
  totalScreenReferences = @($items).Count
  sources = @(
    [ordered]@{ name = "Refero iOS Apps"; slug = "refero-ios-apps"; url = "https://refero.design/apps/search"; count = @($items | Where-Object channel -eq "ios-apps").Count; licenseStatus = "inspiration-only-unless-explicitly-licensed" },
    [ordered]@{ name = "Refero Web Screens"; slug = "refero-web-screens"; url = "https://refero.design/search"; count = @($items | Where-Object channel -eq "web").Count; licenseStatus = "inspiration-only-unless-explicitly-licensed" }
  )
  pageTypes = $pageTypeCatalog
  references = $items
}

Write-Text $CatalogJson (($catalog | ConvertTo-Json -Depth 28))

$md = [Text.StringBuilder]::new()
[void]$md.AppendLine("# Screen References")
[void]$md.AppendLine("")
[void]$md.AppendLine("Total screen references: $(@($items).Count)")
[void]$md.AppendLine("")
[void]$md.AppendLine("These are public Refero screen references grouped by page type. Media is linked, not vendored.")
[void]$md.AppendLine("")
[void]$md.AppendLine("## Page Type Coverage")
[void]$md.AppendLine("")
[void]$md.AppendLine("| Page Type | iOS/App Matches | Web Matches | Captured |")
[void]$md.AppendLine("|---|---:|---:|---:|")
foreach ($pt in $pageTypeCatalog) {
  [void]$md.AppendLine("| $(Markdown-Cell $pt.name) | $($pt.iosAppMatches) | $($pt.webMatches) | $($pt.captured) |")
}
[void]$md.AppendLine("")
[void]$md.AppendLine("## References")
[void]$md.AppendLine("")
[void]$md.AppendLine("| Reference | Channel | Page Type | Entity URL | Folder |")
[void]$md.AppendLine("|---|---|---|---|---|")
foreach ($item in $items) {
  $entityUrl = if ($item.entity.url) { "[$(Markdown-Cell $item.entity.name)]($($item.entity.url))" } else { Markdown-Cell $item.entity.name }
  [void]$md.AppendLine("| [$(Markdown-Cell $item.entity.name)]($($item.path)/) | $(Markdown-Cell $item.channel) | $(Markdown-Cell $item.pageType.name) | $entityUrl | ``$($item.path)/`` |")
}
Write-Text $CatalogMarkdown $md.ToString()

Write-Output "SCREEN_REFERENCES=$(@($items).Count)"
Write-Output "WROTE=$CatalogJson"
Write-Output "WROTE=$CatalogMarkdown"
