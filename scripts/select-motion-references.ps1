param(
  [string]$Brief = "",
  [string]$BriefFile = "",
  [string]$ProjectPath = "",
  [string]$MotionCatalogJson = ".\motion\motion-catalog.json",
  [string]$OutputPath = ".\MOTION_SELECTION.generated.md",
  [int]$TopStyles = 8,
  [int]$TopPatterns = 5,
  [switch]$PassThruJson
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$script:RepoRoot = Split-Path -Parent $PSScriptRoot
$script:StopWords = @{}
foreach ($word in @("about","also","and","are","build","can","for","from","have","into","like","make","more","need","needs","site","that","the","this","tool","use","using","with","would","website","your")) { $script:StopWords[$word] = $true }

function Resolve-VaultPath([string]$Path) {
  if ([System.IO.Path]::IsPathRooted($Path)) { return $Path }
  return (Join-Path $script:RepoRoot $Path)
}

function Normalize-Text([string]$Text) {
  if ([string]::IsNullOrWhiteSpace($Text)) { return "" }
  return (($Text.ToLowerInvariant() -replace "[^a-z0-9+#&.]+", " ") -replace "\s+", " ").Trim()
}

function Get-Terms([string]$Text) {
  $normalized = Normalize-Text $Text
  if ([string]::IsNullOrWhiteSpace($normalized)) { return @() }
  return @($normalized -split "\s+" | Where-Object { $_.Length -ge 3 -and -not $script:StopWords.ContainsKey($_) } | Select-Object -Unique)
}

function Convert-ToSearchText($Value) {
  if ($null -eq $Value) { return "" }
  if ($Value -is [string]) { return $Value }
  if ($Value -is [System.Array]) { return (($Value | ForEach-Object { Convert-ToSearchText $_ }) -join " ") }
  if ($Value -is [System.Management.Automation.PSCustomObject]) {
    $values = @($Value.PSObject.Properties | ForEach-Object { $_.Value })
    return (($values | ForEach-Object { Convert-ToSearchText $_ }) -join " ")
  }
  return [string]$Value
}

function Get-ObjectValue($Object, [string]$Name) {
  if ($null -eq $Object) { return $null }
  if ($Object.PSObject.Properties.Name -contains $Name) { return $Object.$Name }
  return $null
}

function Escape-MarkdownCell([string]$Text) {
  if ($null -eq $Text) { return "" }
  return (($Text -replace "\|", "\\|") -replace "`r?`n", " ").Trim()
}

function Short-Text([string]$Text, [int]$Length = 180) {
  if ([string]::IsNullOrWhiteSpace($Text)) { return "Not provided" }
  $oneLine = (($Text -replace "`r?`n", " ") -replace "\s+", " ").Trim()
  if ($oneLine.Length -le $Length) { return $oneLine }
  return ($oneLine.Substring(0, $Length - 3) + "...")
}

function Add-UniqueString([System.Collections.Generic.List[string]]$List, [string]$Value) {
  if (-not [string]::IsNullOrWhiteSpace($Value) -and -not $List.Contains($Value)) { [void]$List.Add($Value) }
}

function Get-ProjectContext([string]$Path) {
  $context = [ordered]@{ Path = $Path; Stack = @(); Text = "" }
  if ([string]::IsNullOrWhiteSpace($Path)) { return [pscustomobject]$context }
  $resolved = if ([System.IO.Path]::IsPathRooted($Path)) { $Path } else { Join-Path (Get-Location) $Path }
  if (-not (Test-Path -LiteralPath $resolved)) { return [pscustomobject]$context }
  $root = (Resolve-Path -LiteralPath $resolved).Path
  $stack = New-Object System.Collections.Generic.List[string]
  $parts = New-Object System.Collections.Generic.List[string]
  foreach ($relative in @("package.json", "README.md", "readme.md", "src/App.tsx", "app/page.tsx", "pages/index.tsx")) {
    $candidate = Join-Path $root $relative
    if (Test-Path -LiteralPath $candidate -PathType Leaf) {
      try {
        $text = Get-Content -LiteralPath $candidate -Raw
        if ($text.Length -gt 12000) { $text = $text.Substring(0, 12000) }
        [void]$parts.Add("FILE: $relative`n$text")
        if ($relative -eq "package.json") {
          $pkg = $text | ConvertFrom-Json
          $depsText = Convert-ToSearchText @((Get-ObjectValue $pkg "dependencies"), (Get-ObjectValue $pkg "devDependencies"), (Get-ObjectValue $pkg "scripts"))
          foreach ($signal in @("react", "next", "vite", "vue", "svelte", "tailwind", "framer-motion", "motion", "gsap", "three", "@react-three/fiber", "lottie", "rive", "animejs")) {
            if ((Normalize-Text $depsText).Contains((Normalize-Text $signal))) { Add-UniqueString $stack $signal }
          }
        }
      } catch {
        [void]$parts.Add("FILE: $relative")
      }
    }
  }
  $context.Stack = @($stack)
  $context.Text = ($parts -join "`n`n")
  return [pscustomobject]$context
}

$briefText = $Brief
if (-not [string]::IsNullOrWhiteSpace($BriefFile)) {
  $briefFilePath = if ([System.IO.Path]::IsPathRooted($BriefFile)) { $BriefFile } else { Join-Path (Get-Location) $BriefFile }
  if (Test-Path -LiteralPath $briefFilePath) { $briefText = (($briefText, (Get-Content -LiteralPath $briefFilePath -Raw)) | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }) -join "`n`n" }
}

$catalogPath = Resolve-VaultPath $MotionCatalogJson
if (-not (Test-Path -LiteralPath $catalogPath)) { throw "Motion catalog not found: $catalogPath" }
$motionCatalog = Get-Content -LiteralPath $catalogPath -Raw | ConvertFrom-Json
$project = Get-ProjectContext $ProjectPath
$combinedText = (($briefText, $project.Text, ($project.Stack -join " ")) | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }) -join "`n`n"
$combinedNormalized = Normalize-Text $combinedText
$terms = Get-Terms $combinedText

$intentAliases = [ordered]@{
  "quiet-premium" = @("premium", "luxury", "elegant", "refined", "calm", "minimal", "professional")
  "product-story" = @("saas", "product", "workflow", "features", "dashboard", "tool", "platform", "ai", "analytics")
  "cinematic-media" = @("cinematic", "video", "photo", "wedding", "restaurant", "real estate", "showroom", "travel", "hospitality", "portfolio")
  "creative-studio" = @("creative", "studio", "agency", "portfolio", "experimental", "bold", "kinetic")
  "technical-motion" = @("developer", "api", "docs", "terminal", "code", "technical")
  "immersive-3d" = @("3d", "webgl", "three", "spatial", "game", "interactive", "canvas")
  "ambient-symbolic" = @("moon", "eclipse", "night", "space", "astronomy", "astrology", "sleep", "meditation", "wellness", "background", "loading", "loader", "coming soon", "waitlist", "404")
  "stateful-ui" = @("login", "signup", "sign up", "auth", "authentication", "hover menu", "navigation", "navbar", "nav bar", "menu", "microinteraction", "indicator", "carousel", "slider", "timed card", "timed cards", "card", "cards", "sidebar", "side bar", "pill", "delete", "destructive", "button")
}

$detectedIntents = New-Object System.Collections.Generic.List[string]
foreach ($intent in $intentAliases.Keys) {
  foreach ($alias in $intentAliases[$intent]) {
    if ($combinedNormalized.Contains((Normalize-Text $alias))) { Add-UniqueString $detectedIntents $intent; break }
  }
}
if ($detectedIntents.Count -eq 0) { Add-UniqueString $detectedIntents "product-story" }

$styleRows = foreach ($ref in @($motionCatalog.styleReferences)) {
  $search = Normalize-Text (Convert-ToSearchText @($ref.name, $ref.slug, $ref.category, $ref.bestFor, $ref.tags, $ref.motionSignals, $ref.usage, $ref.theme))
  $score = [int]$ref.motionScore
  $why = New-Object System.Collections.Generic.List[string]
  if ($score -gt 0) { [void]$why.Add("catalog score $score") }
  $matches = @($terms | Where-Object { $_.Length -gt 3 -and $search.Contains($_) } | Select-Object -Unique -First 8)
  if ($matches.Count -gt 0) { $score += [Math]::Min(25, $matches.Count * 4); [void]$why.Add("term match: " + ($matches -join ", ")) }
  if ($combinedNormalized.Contains("dark") -and $search.Contains("dark")) { $score += 5; [void]$why.Add("theme: dark") }
  if (($combinedNormalized.Contains("light") -or $combinedNormalized.Contains("clean")) -and $search.Contains("light")) { $score += 4; [void]$why.Add("theme: light") }
  if ($combinedNormalized.Contains("landing") -and ($search.Contains("landing") -or $search.Contains("hero") -or $search.Contains("launch"))) { $score += 10; [void]$why.Add("landing fit") }
  if (($combinedNormalized.Contains("video") -or $combinedNormalized.Contains("cinematic")) -and [int]$ref.previewVideoCount -gt 0) { $score += 8; [void]$why.Add("preview video available") }
  if ($why.Count -eq 0) { [void]$why.Add("motion reference") }
  [pscustomobject][ordered]@{
    score = [Math]::Min(100, $score)
    name = [string]$ref.name
    path = [string]$ref.path
    theme = [string]$ref.theme
    signals = @($ref.motionSignals)
    previewVideoCount = [int]$ref.previewVideoCount
    sourceUrl = [string]$ref.sourceUrl
    usage = [string]$ref.usage
    why = (($why | Select-Object -Unique -First 5) -join "; ")
    ref = $ref
  }
}
$selectedStyles = @($styleRows | Sort-Object -Property @{ Expression = "score"; Descending = $true }, @{ Expression = "previewVideoCount"; Descending = $true }, @{ Expression = "name"; Descending = $false } | Select-Object -First $TopStyles)

$patternAliases = @{
  "team-carousel-slider" = @("team carousel", "carousel slider", "profile carousel", "speaker carousel")
  "modern-timed-destination-cards" = @("timed cards", "timed card", "timed hero cards", "destination cards", "travel cards")
  "responsive-hover-sidebar" = @("responsive sidebar", "hover sidebar", "collapsible sidebar", "side bar", "sidebar")
  "glass-theme-pill-nav" = @("glass pill", "pill navigation", "pill nav", "theme pill", "glass nav")
  "animated-delete-button" = @("animated delete", "delete button", "destructive button", "trash button")
}
$patternRows = foreach ($pattern in @($motionCatalog.patterns)) {
  $search = Normalize-Text (Convert-ToSearchText @($pattern.name, $pattern.id, $pattern.bestFor, $pattern.useWhen, $pattern.preferredStack))
  $score = 0
  $matches = @($terms | Where-Object { $_.Length -gt 3 -and $search.Contains($_) } | Select-Object -Unique -First 8)
  if ($matches.Count -gt 0) { $score += [Math]::Min(50, $matches.Count * 8) }
  if ($patternAliases.ContainsKey($pattern.id)) {
    foreach ($alias in $patternAliases[$pattern.id]) {
      if ($combinedNormalized.Contains((Normalize-Text $alias))) { $score += 50; break }
    }
  }
  foreach ($intent in $detectedIntents) {
    if (($intent -eq "cinematic-media" -and $pattern.id -eq "cinematic-media-hero") -or
        ($intent -eq "product-story" -and $pattern.id -in @("scroll-product-story", "product-ui-tour", "animated-data-proof")) -or
        ($intent -eq "creative-studio" -and $pattern.id -in @("kinetic-hero-type", "scroll-product-story")) -or
        ($intent -eq "technical-motion" -and $pattern.id -in @("animated-data-proof", "product-ui-tour", "microinteraction-system")) -or
        ($intent -eq "immersive-3d" -and $pattern.id -eq "threejs-product-stage") -or
        ($intent -eq "quiet-premium" -and $pattern.id -in @("microinteraction-system", "cinematic-media-hero", "ambient-eclipse-moon")) -or
        ($intent -eq "ambient-symbolic" -and $pattern.id -eq "ambient-eclipse-moon") -or
        ($intent -eq "stateful-ui" -and $pattern.id -in @("microinteraction-system", "motion-safe-mega-menu", "code-candy-auth-slanted-overlay", "code-candy-hover-pill-menu", "code-candy-floating-indicator-nav", "code-candy-auth-overlay-slide", "code-candy-hover-expanding-login", "team-carousel-slider", "modern-timed-destination-cards", "responsive-hover-sidebar", "glass-theme-pill-nav", "animated-delete-button"))) { $score += 30 }
  }
  [pscustomobject][ordered]@{ score = [Math]::Min(100, $score); id = [string]$pattern.id; name = [string]$pattern.name; useWhen = [string]$pattern.useWhen; preferredStack = @($pattern.preferredStack); pattern = $pattern }
}
$selectedPatterns = @($patternRows | Sort-Object -Property @{ Expression = "score"; Descending = $true }, @{ Expression = "name"; Descending = $false } | Select-Object -First $TopPatterns)

$resourceRows = foreach ($resource in @($motionCatalog.implementationResources)) {
  $search = Normalize-Text (Convert-ToSearchText @($resource.name, $resource.type, $resource.bestFor, $resource.notes))
  $score = 0
  $why = New-Object System.Collections.Generic.List[string]
  foreach ($stackItem in @($project.Stack)) {
    if ($search.Contains((Normalize-Text $stackItem))) { $score += 25; [void]$why.Add("already in stack: $stackItem") }
  }
  if (($project.Stack -contains "react" -or $project.Stack -contains "next" -or $project.Stack -contains "vite") -and $resource.name -eq "Motion for React") { $score += 35; [void]$why.Add("React UI motion") }
  if (($combinedNormalized.Contains("scroll") -or $combinedNormalized.Contains("cinematic") -or $combinedNormalized.Contains("timeline")) -and $resource.name -eq "GSAP") { $score += 35; [void]$why.Add("advanced choreography") }
  if (($combinedNormalized.Contains("lottie") -or $combinedNormalized.Contains("illustration") -or $combinedNormalized.Contains("empty state")) -and $resource.name -like "LottieFiles*") { $score += 35; [void]$why.Add("vector animation") }
  if (($combinedNormalized.Contains("rive") -or $combinedNormalized.Contains("interactive") -or $combinedNormalized.Contains("state machine")) -and $resource.name -like "Rive*") { $score += 35; [void]$why.Add("interactive animation") }
  if (($combinedNormalized.Contains("3d") -or $combinedNormalized.Contains("webgl") -or $combinedNormalized.Contains("three")) -and $resource.name -eq "Three.js") { $score += 40; [void]$why.Add("3D/WebGL") }
  if ($resource.name -eq "CSS animations") { $score += 20; [void]$why.Add("baseline motion") }
  if ($why.Count -eq 0) { [void]$why.Add("optional") }
  [pscustomobject][ordered]@{ score = [Math]::Min(100, $score); name = [string]$resource.name; url = [string]$resource.url; bestFor = @($resource.bestFor); why = (($why | Select-Object -Unique) -join "; "); resource = $resource }
}
$selectedResources = @($resourceRows | Where-Object { $_.score -gt 0 } | Sort-Object -Property @{ Expression = "score"; Descending = $true }, @{ Expression = "name"; Descending = $false } | Select-Object -First 4)

$resolvedOutput = $OutputPath
if (-not [System.IO.Path]::IsPathRooted($resolvedOutput)) { $resolvedOutput = Join-Path (Get-Location) $OutputPath }
$outputParent = Split-Path -Parent $resolvedOutput
if ($outputParent -and -not (Test-Path -LiteralPath $outputParent)) { New-Item -ItemType Directory -Path $outputParent -Force | Out-Null }

$readFiles = New-Object System.Collections.Generic.List[string]
Add-UniqueString $readFiles "motion/LANDING_PAGE_MOTION_GUIDE.md"
Add-UniqueString $readFiles "motion/MOTION_REFERENCES.md"
Add-UniqueString $readFiles "motion/motion-catalog.json"
foreach ($row in $selectedStyles) {
  foreach ($file in @($row.ref.requiredReadFiles)) { Add-UniqueString $readFiles ([string]$file) }
}
foreach ($row in $selectedPatterns) {
  $pattern = $row.pattern
  foreach ($file in @((Get-ObjectValue $pattern "localPath"), (Get-ObjectValue $pattern "verificationNotes"))) {
    if (-not [string]::IsNullOrWhiteSpace([string]$file)) { Add-UniqueString $readFiles ([string]$file) }
  }
}

$md = New-Object System.Text.StringBuilder
[void]$md.AppendLine("# Motion Selection")
[void]$md.AppendLine("")
[void]$md.AppendLine("Generated by `scripts/select-motion-references.ps1` on $(Get-Date -Format yyyy-MM-dd).")
[void]$md.AppendLine("")
[void]$md.AppendLine("## Target")
[void]$md.AppendLine("")
[void]$md.AppendLine("- Brief: $(Short-Text $briefText 240)")
[void]$md.AppendLine("- Target repo or output path: $(if ([string]::IsNullOrWhiteSpace($ProjectPath)) { 'Not provided' } else { $ProjectPath })")
[void]$md.AppendLine("- Detected stack: $(if ($project.Stack.Count -gt 0) { $project.Stack -join ', ' } else { 'Not detected' })")
[void]$md.AppendLine("- Motion intent: $($detectedIntents -join ', ')")
[void]$md.AppendLine("")
[void]$md.AppendLine("## Selected Motion Style References")
[void]$md.AppendLine("")
[void]$md.AppendLine("| Score | Name | Signals | Videos | Path | Why |")
[void]$md.AppendLine("|---:|---|---|---:|---|---|")
foreach ($row in $selectedStyles) {
  [void]$md.AppendLine(("| {0} | {1} | {2} | {3} | ``{4}`` | {5} |" -f $row.score, (Escape-MarkdownCell $row.name), (Escape-MarkdownCell (($row.signals | Select-Object -First 6) -join ', ')), $row.previewVideoCount, $row.path, (Escape-MarkdownCell $row.why)))
}
[void]$md.AppendLine("")
[void]$md.AppendLine("## Selected Motion Patterns")
[void]$md.AppendLine("")
foreach ($row in $selectedPatterns) {
  [void]$md.AppendLine("### $($row.name)")
  [void]$md.AppendLine("")
  [void]$md.AppendLine(("- ID: ``{0}``" -f $row.id))
  [void]$md.AppendLine("- Score: $($row.score)/100")
  [void]$md.AppendLine("- Use when: $($row.useWhen)")
  [void]$md.AppendLine("- Preferred stack: $($row.preferredStack -join ', ')")
  [void]$md.AppendLine("")
}
[void]$md.AppendLine("## Recommended Implementation Resources")
[void]$md.AppendLine("")
foreach ($row in $selectedResources) {
  [void]$md.AppendLine("- $($row.name): $($row.url) - $($row.why)")
}
[void]$md.AppendLine("")
[void]$md.AppendLine("## Implementation Plan")
[void]$md.AppendLine("")
[void]$md.AppendLine("- Define motion tokens before animating individual components.")
[void]$md.AppendLine("- Use one primary motion model and no more than 2 to 5 major motion patterns.")
[void]$md.AppendLine("- Build original animation from target content and owned/licensed assets only.")
[void]$md.AppendLine("- Keep final content readable and available without animation.")
[void]$md.AppendLine("- Add reduced-motion behavior for every autoplay, scroll, canvas, video, or looping animation.")
[void]$md.AppendLine("- Verify mobile performance, keyboard access, layout stability, and text overlap.")
[void]$md.AppendLine("")
[void]$md.AppendLine("## Read Before Implementation")
[void]$md.AppendLine("")
foreach ($file in $readFiles) { [void]$md.AppendLine(("- ``{0}``" -f $file)) }

[System.IO.File]::WriteAllText($resolvedOutput, $md.ToString(), [System.Text.UTF8Encoding]::new($false))

$result = [ordered]@{
  motionIntent = @($detectedIntents)
  styles = @($selectedStyles | ForEach-Object { [ordered]@{ name = $_.name; score = $_.score; path = $_.path; videos = $_.previewVideoCount; why = $_.why } })
  patterns = @($selectedPatterns | ForEach-Object { [ordered]@{ id = $_.id; name = $_.name; score = $_.score } })
  resources = @($selectedResources | ForEach-Object { [ordered]@{ name = $_.name; url = $_.url; why = $_.why } })
  outputPath = $resolvedOutput
}

Write-Output "MOTION_INTENT=$($detectedIntents -join ',')"
Write-Output "STYLE_REFERENCES=$($selectedStyles.Count)"
Write-Output "PATTERNS=$($selectedPatterns.Count)"
Write-Output "RESOURCES=$($selectedResources.Count)"
Write-Output "OUTPUT=$resolvedOutput"
if ($PassThruJson) { $result | ConvertTo-Json -Depth 8 }
