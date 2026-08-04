param(
  [string]$CatalogJson = ".\catalog.json",
  [string]$StylesRoot = ".\styles\refero-styles",
  [string]$OutputRoot = ".\motion",
  [int]$MarkdownLimit = 120
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

function Resolve-RepoPath([string]$Path) {
  if ([System.IO.Path]::IsPathRooted($Path)) { return $Path }
  return (Join-Path (Get-Location) $Path)
}

function Get-ObjectValue($Object, [string]$Name) {
  if ($null -eq $Object) { return $null }
  if ($Object.PSObject.Properties.Name -contains $Name) { return $Object.$Name }
  return $null
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

function Normalize-Text([string]$Text) {
  if ([string]::IsNullOrWhiteSpace($Text)) { return "" }
  return (($Text.ToLowerInvariant() -replace "[^a-z0-9+#&.]+", " ") -replace "\s+", " ").Trim()
}

function Escape-MarkdownCell([string]$Text) {
  if ($null -eq $Text) { return "" }
  return (($Text -replace "\|", "\\|") -replace "`r?`n", " ").Trim()
}

function Get-UniqueMatches([string]$Text, [string[]]$Needles) {
  $normalized = Normalize-Text $Text
  $out = New-Object System.Collections.Generic.List[string]
  foreach ($needle in $Needles) {
    $n = Normalize-Text $needle
    if ($n -and $normalized.Contains($n) -and -not $out.Contains($needle)) { [void]$out.Add($needle) }
  }
  return @($out)
}

function Get-VideoUrls([string]$Text) {
  if ([string]::IsNullOrWhiteSpace($Text)) { return @() }
  $matches = [regex]::Matches($Text, 'https?://[^\s\)\]"''<>]+\.(?:mp4|webm|mov)(?:\?[^\s\)\]"''<>]+)?', 'IgnoreCase')
  return @($matches | ForEach-Object { $_.Value.TrimEnd('.', ',', ';') } | Select-Object -Unique)
}

$catalogPath = Resolve-RepoPath $CatalogJson
$stylesPath = Resolve-RepoPath $StylesRoot
$outputPath = Resolve-RepoPath $OutputRoot
if (-not (Test-Path -LiteralPath $catalogPath)) { throw "Missing catalog: $catalogPath" }
if (-not (Test-Path -LiteralPath $stylesPath)) { throw "Missing styles root: $stylesPath" }
if (-not (Test-Path -LiteralPath $outputPath)) { New-Item -ItemType Directory -Path $outputPath -Force | Out-Null }

$catalog = Get-Content -LiteralPath $catalogPath -Raw | ConvertFrom-Json
$styles = @($catalog.styles)

$motionKeywords = @(
  "motion", "animation", "animated", "kinetic", "cinematic", "interactive", "lottie", "lottiefiles", "lottielab", "gsap", "jitter", "rive", "three", "webgl", "3d", "canvas", "scroll", "parallax", "transition", "microinteraction", "video", "film", "showcase", "immersive", "playful", "hero", "landing", "launch", "product story", "sequence", "timeline"
)

$strongNames = @(
  "GSAP", "Jitter", "LottieFiles", "Lottielab", "Active Theory", "Unicorn Studio", "Apple Watch Ultra 3", "Frame.io", "Ferrari", "SpaceX", "Framer", "North Kingdom", "OHZI Interactive Studio / Dive into digital magic.", "Vivid+Co", "Watch new Originals", "Amaterasu", "Air", "Vanmoof", "Superhuman", "Superpower", "AREA 17", "EPIC agency", "Karl"
)

$styleRefs = New-Object System.Collections.Generic.List[object]
foreach ($style in $styles) {
  $path = [string](Get-ObjectValue $style "path")
  $absolute = if ($path) { Join-Path (Get-Location) $path } else { $null }
  $sourceText = ""
  $sourcePath = if ($absolute) { Join-Path $absolute "source.md" } else { $null }
  $screensPath = if ($absolute) { Join-Path $absolute "screenshots/README.md" } else { $null }
  if ($sourcePath -and (Test-Path -LiteralPath $sourcePath)) { $sourceText += Get-Content -LiteralPath $sourcePath -Raw }
  if ($screensPath -and (Test-Path -LiteralPath $screensPath)) { $sourceText += "`n" + (Get-Content -LiteralPath $screensPath -Raw) }

  $metadataText = Convert-ToSearchText @(
    (Get-ObjectValue $style "name"),
    (Get-ObjectValue $style "slug"),
    (Get-ObjectValue $style "category"),
    (Get-ObjectValue $style "bestFor"),
    (Get-ObjectValue $style "tags"),
    (Get-ObjectValue $style "theme"),
    (Get-ObjectValue $style "northStar"),
    (Get-ObjectValue $style "summary"),
    (Get-ObjectValue $style "mood")
  )
  $combined = "$metadataText`n$sourceText"
  $signals = @(Get-UniqueMatches $combined $motionKeywords)
  $videos = @(Get-VideoUrls $sourceText)
  $name = [string](Get-ObjectValue $style "name")
  $isStrong = $strongNames -contains $name
  if ($signals.Count -eq 0 -and $videos.Count -eq 0 -and -not $isStrong) { continue }

  $score = 0
  $score += [Math]::Min(45, $signals.Count * 5)
  $score += [Math]::Min(20, $videos.Count * 4)
  if ($isStrong) { $score += 28 }
  if ((Normalize-Text $metadataText).Contains("motion")) { $score += 20 }
  if ((Normalize-Text $metadataText).Contains("landing")) { $score += 8 }
  if ((Normalize-Text $metadataText).Contains("cinematic")) { $score += 10 }
  if ((Normalize-Text $metadataText).Contains("developer")) { $score += 5 }
  $score = [Math]::Min(100, $score)

  $usage = "Motion inspiration"
  if ($signals -contains "gsap") { $usage = "Advanced scroll and timeline animation reference" }
  elseif ($signals -contains "lottie" -or $signals -contains "lottiefiles" -or $signals -contains "lottielab") { $usage = "Vector animation and motion-system reference" }
  elseif ($signals -contains "3d" -or $signals -contains "webgl" -or $signals -contains "three") { $usage = "3D or WebGL landing-page reference" }
  elseif ($signals -contains "cinematic" -or $signals -contains "video") { $usage = "Cinematic landing-page and media-led reference" }
  elseif ($signals -contains "interactive") { $usage = "Interactive website reference" }
  elseif ($videos.Count -gt 0) { $usage = "Remote preview video available for motion study" }

  [void]$styleRefs.Add([pscustomobject][ordered]@{
    name = $name
    slug = [string](Get-ObjectValue $style "slug")
    path = $path
    sourceUrl = [string](Get-ObjectValue $style "sourceUrl")
    referenceUrl = [string](Get-ObjectValue $style "referenceSite")
    theme = [string](Get-ObjectValue $style "theme")
    category = [string](Get-ObjectValue $style "category")
    bestFor = Get-ObjectValue $style "bestFor"
    tags = Get-ObjectValue $style "tags"
    motionScore = [int]$score
    motionSignals = @($signals)
    previewVideoCount = $videos.Count
    previewVideoUrls = @($videos | Select-Object -First 4)
    usage = $usage
    licenseStatus = "inspiration-only-unless-explicitly-licensed"
    requiredReadFiles = @(
      "$path/README.md",
      "$path/DESIGN.md",
      "$path/implementation-prompt.md",
      "$path/tokens/components.md",
      "$path/tokens/guidelines.md",
      "$path/code/design-tokens.json",
      "$path/source.md"
    )
  })
}

$styleRefs = @($styleRefs | Sort-Object -Property @{Expression = "motionScore"; Descending = $true}, @{Expression = "previewVideoCount"; Descending = $true}, @{Expression = "name"; Descending = $false})
$highSignal = @($styleRefs | Where-Object { $_.motionScore -ge 35 })
$withVideo = @($styleRefs | Where-Object { $_.previewVideoCount -gt 0 })

$patterns = @(
  [pscustomobject][ordered]@{ id = "kinetic-hero-type"; name = "Kinetic Hero Type"; bestFor = @("AI launches", "developer tools", "creative studios", "premium landing pages"); useWhen = "The first screen needs a memorable message without relying on many product screenshots."; preferredStack = @("CSS", "Motion for React", "GSAP"); implementationNotes = @("Animate opacity, y, scale, and clip-path only after text is readable.", "Keep the final text state static and accessible.", "Use one primary kinetic idea, not several competing text effects."); reducedMotion = "Respect prefers-reduced-motion by showing the final static state, disabling autoplay or scroll-driven choreography, and preserving readable content without animation."; avoid = @("Animating every word forever", "letter spacing jitter", "low contrast over video") },
  [pscustomobject][ordered]@{ id = "scroll-product-story"; name = "Scroll Product Story"; bestFor = @("SaaS", "AI tools", "fintech", "hardware", "showrooms"); useWhen = "A landing page must explain a workflow step by step."; preferredStack = @("GSAP ScrollTrigger", "Motion for React", "CSS sticky sections"); implementationNotes = @("Pin only one major section at a time.", "Pair each scroll beat with a clear content change.", "Provide reduced-motion fallback as stacked static sections."); reducedMotion = "Respect prefers-reduced-motion by showing the final static state, disabling autoplay or scroll-driven choreography, and preserving readable content without animation."; avoid = @("Hijacking scroll", "nested pinned sections", "hiding core copy inside animation") },
  [pscustomobject][ordered]@{ id = "cinematic-media-hero"; name = "Cinematic Media Hero"; bestFor = @("hospitality", "weddings", "real estate", "restaurants", "luxury services", "product launches"); useWhen = "The brand has strong photos or videos and needs atmosphere quickly."; preferredStack = @("CSS", "HTML video", "Motion for React"); implementationNotes = @("Use one full-bleed stage with stable dimensions.", "Add pause controls when autoplay is used.", "Preload cautiously and keep overlay contrast high."); reducedMotion = "Respect prefers-reduced-motion by showing the final static state, disabling autoplay or scroll-driven choreography, and preserving readable content without animation."; avoid = @("Huge uncompressed video", "text moving over busy footage", "autoplay without reduced-motion handling") },
  [pscustomobject][ordered]@{ id = "product-ui-tour"; name = "Animated Product UI Tour"; bestFor = @("web tools", "dashboards", "AI assistants", "productivity apps"); useWhen = "Visitors need to understand product states or workflow outputs."; preferredStack = @("Motion for React", "CSS", "GSAP timeline"); implementationNotes = @("Animate real UI components, not screenshots when possible.", "Use short timeline loops with pause on hover/focus.", "Keep state labels visible for screen readers."); reducedMotion = "Respect prefers-reduced-motion by showing the final static state, disabling autoplay or scroll-driven choreography, and preserving readable content without animation."; avoid = @("Fake unreadable UI", "rapid looping dashboards", "layout shift between states") },
  [pscustomobject][ordered]@{ id = "lottie-illustration-system"; name = "Lottie Illustration System"; bestFor = @("onboarding", "feature cards", "empty states", "friendly SaaS", "consumer apps"); useWhen = "Vector illustrations need lightweight repeated motion."; preferredStack = @("LottieFiles", "dotLottie", "React Lottie player"); implementationNotes = @("Use owned or licensed animation JSON/dotlottie files.", "Keep loops short and optional.", "Pair each animation with text labels and static fallbacks."); reducedMotion = "Respect prefers-reduced-motion by showing the final static state, disabling autoplay or scroll-driven choreography, and preserving readable content without animation."; avoid = @("Unlicensed marketplace files", "too many loops on one viewport", "motion-only meaning") },
  [pscustomobject][ordered]@{ id = "rive-interactive-control"; name = "Rive Interactive Control"; bestFor = @("configurators", "games", "education", "interactive explainers", "playful tools"); useWhen = "The motion should respond to user input, state machines, or controls."; preferredStack = @("Rive Web Runtime", "React", "Canvas"); implementationNotes = @("Map states to real product states.", "Keep interaction labels visible outside the canvas.", "Expose accessible controls that mirror canvas behavior."); reducedMotion = "Respect prefers-reduced-motion by showing the final static state, disabling autoplay or scroll-driven choreography, and preserving readable content without animation."; avoid = @("Canvas-only navigation", "unlabeled interactions", "large runtimes for tiny decorative motion") },
  [pscustomobject][ordered]@{ id = "threejs-product-stage"; name = "Three.js Product Stage"; bestFor = @("3D products", "spatial portfolios", "hardware", "games", "immersive launches"); useWhen = "A product or environment benefits from real 3D inspection."; preferredStack = @("Three.js", "React Three Fiber", "WebGL"); implementationNotes = @("Make the 3D scene full-bleed or central, not a tiny decorative card.", "Check canvas pixels and mobile framing.", "Use progressive loading and static fallback poster."); reducedMotion = "Respect prefers-reduced-motion by showing the final static state, disabling autoplay or scroll-driven choreography, and preserving readable content without animation."; avoid = @("Blank canvases", "GPU-heavy hero on low-end devices", "unlabeled 3D controls") },
  [pscustomobject][ordered]@{ id = "microinteraction-system"; name = "Microinteraction System"; bestFor = @("forms", "checkout", "dashboards", "admin tools", "SaaS apps"); useWhen = "The product needs polish without theatrical motion."; preferredStack = @("CSS transitions", "Motion for React", "component library states"); implementationNotes = @("Standardize durations, easings, hover, focus, active, disabled, loading, success, and error states.", "Make important state changes visible but quick.", "Prefer transform and opacity."); reducedMotion = "Respect prefers-reduced-motion by showing the final static state, disabling autoplay or scroll-driven choreography, and preserving readable content without animation."; avoid = @("Animating layout-heavy properties", "different easings everywhere", "motion that delays tasks") },
  [pscustomobject][ordered]@{ id = "motion-safe-mega-menu"; name = "Motion-Safe Mega Menu"; bestFor = @("retail", "showrooms", "marketplaces", "service websites"); useWhen = "Dropdown navigation needs depth without covering content awkwardly."; preferredStack = @("CSS", "Motion for React" ); implementationNotes = @("Fade/slide the panel within 150 to 220ms.", "Keep keyboard focus order predictable.", "Use static accordion fallback on mobile."); reducedMotion = "Respect prefers-reduced-motion by showing the final static state, disabling autoplay or scroll-driven choreography, and preserving readable content without animation."; avoid = @("Bouncy menus", "menus that trap focus unintentionally", "hover-only access") },
  [pscustomobject][ordered]@{ id = "animated-data-proof"; name = "Animated Data Proof"; bestFor = @("analytics", "finance", "AI tools", "B2B SaaS"); useWhen = "Numbers, charts, or proof points need life without becoming dashboards."; preferredStack = @("CSS", "Motion for React", "SVG animation", "Canvas when needed"); implementationNotes = @("Animate chart reveal once on entry.", "Keep final values readable and truthful.", "Do not fake metrics that look like claims."); reducedMotion = "Respect prefers-reduced-motion by showing the final static state, disabling autoplay or scroll-driven choreography, and preserving readable content without animation."; avoid = @("Constantly moving charts", "unlabeled axes", "misleading number counters") }
)

$resources = @(
  [pscustomobject][ordered]@{ name = "CSS animations"; url = "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations/Using_CSS_animations"; type = "native-web"; bestFor = @("simple transitions", "microinteractions", "low-dependency landing pages"); notes = "Use CSS for simple keyframes and transitions where JavaScript is unnecessary." },
  [pscustomobject][ordered]@{ name = "Motion for React"; url = "https://motion.dev/docs/react-quick-start"; type = "react-library"; bestFor = @("React UI transitions", "layout animation", "presence", "component-level motion"); notes = "Use for React and Next.js interface motion before reaching for heavier timeline tooling." },
  [pscustomobject][ordered]@{ name = "GSAP"; url = "https://gsap.com/docs/v3/"; type = "animation-platform"; bestFor = @("advanced timelines", "scroll scenes", "creative coding", "landing-page choreography"); notes = "Use when animation sequencing and scroll control are central to the experience." },
  [pscustomobject][ordered]@{ name = "LottieFiles dotLottie React"; url = "https://docs.lottiefiles.com/en/runtimes/distributions/react"; type = "vector-animation-runtime"; bestFor = @("owned vector animations", "feature illustrations", "empty states", "onboarding"); notes = "Use only with owned, user-provided, generated, or clearly licensed animation assets." },
  [pscustomobject][ordered]@{ name = "Rive Web Runtime"; url = "https://rive.app/docs/runtimes/web/web-js"; type = "interactive-animation-runtime"; bestFor = @("state-machine animation", "interactive explainers", "playful controls"); notes = "Use when the animation must respond to product state or user input." },
  [pscustomobject][ordered]@{ name = "Three.js"; url = "https://threejs.org/docs/"; type = "3d-webgl"; bestFor = @("3D product stages", "immersive backgrounds", "spatial UI", "games"); notes = "Use for true 3D or WebGL scenes, then verify canvas rendering across viewport sizes." },
  [pscustomobject][ordered]@{ name = "Anime.js"; url = "https://animejs.com/documentation/"; type = "javascript-animation-engine"; bestFor = @("small JS timelines", "SVG motion", "non-React projects", "lightweight choreography"); notes = "Use for smaller animation timelines where GSAP would be more than the project needs." }
)

$catalogObject = [pscustomobject][ordered]@{
  name = "AI UI Style Vault Motion Catalog"
  generatedAt = (Get-Date -Format "yyyy-MM-dd")
  purpose = "Machine-readable motion reference entry point for professional landing pages and motion graphics websites."
  policy = [pscustomobject][ordered]@{
    mediaStorage = "remote-links-only"
    licenseStatus = "inspiration-only-unless-explicitly-licensed"
    reducedMotionRequired = $true
    copiedAssetsAllowed = $false
  }
  totals = [pscustomobject][ordered]@{
    styleReferences = $styleRefs.Count
    highSignalStyleReferences = $highSignal.Count
    styleReferencesWithPreviewVideo = $withVideo.Count
    motionPatterns = $patterns.Count
    implementationResources = $resources.Count
  }
  motionSignals = $motionKeywords
  styleReferences = @($styleRefs)
  patterns = @($patterns)
  implementationResources = @($resources)
}

$catalogOut = Join-Path $outputPath "motion-catalog.json"
$markdownOut = Join-Path $outputPath "MOTION_REFERENCES.md"
$catalogObject | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $catalogOut -Encoding utf8

$md = New-Object System.Text.StringBuilder
[void]$md.AppendLine("# Motion References")
[void]$md.AppendLine("")
[void]$md.AppendLine("Generated from local vault metadata and remote media links. Media is referenced only; no videos are vendored.")
[void]$md.AppendLine("")
[void]$md.AppendLine("## Totals")
[void]$md.AppendLine("")
[void]$md.AppendLine("- Style references: $($styleRefs.Count)")
[void]$md.AppendLine("- High-signal motion references: $($highSignal.Count)")
[void]$md.AppendLine("- Style references with preview video links: $($withVideo.Count)")
[void]$md.AppendLine("- Motion patterns: $($patterns.Count)")
[void]$md.AppendLine("- Implementation resources: $($resources.Count)")
[void]$md.AppendLine("")
[void]$md.AppendLine("## Best Starting Points")
[void]$md.AppendLine("")
[void]$md.AppendLine("| Score | Name | Theme | Signals | Videos | Path |")
[void]$md.AppendLine("|---:|---|---|---|---:|---|")
foreach ($ref in @($styleRefs | Select-Object -First $MarkdownLimit)) {
  [void]$md.AppendLine(("| {0} | {1} | {2} | {3} | {4} | ``{5}`` |" -f $ref.motionScore, (Escape-MarkdownCell $ref.name), (Escape-MarkdownCell $ref.theme), (Escape-MarkdownCell (($ref.motionSignals | Select-Object -First 6) -join ', ')), $ref.previewVideoCount, $ref.path))
}
[void]$md.AppendLine("")
[void]$md.AppendLine("## Motion Patterns")
[void]$md.AppendLine("")
foreach ($pattern in $patterns) {
  [void]$md.AppendLine("### $($pattern.name)")
  [void]$md.AppendLine("")
  [void]$md.AppendLine(("- ID: ``{0}``" -f $pattern.id))
  [void]$md.AppendLine("- Best for: $($pattern.bestFor -join ', ')")
  [void]$md.AppendLine("- Use when: $($pattern.useWhen)")
  [void]$md.AppendLine("- Preferred stack: $($pattern.preferredStack -join ', ')")
  [void]$md.AppendLine("- Reduced motion: $($pattern.reducedMotion)")
  [void]$md.AppendLine("- Avoid: $($pattern.avoid -join '; ')")
  [void]$md.AppendLine("")
}
[void]$md.AppendLine("## Implementation Resources")
[void]$md.AppendLine("")
[void]$md.AppendLine("| Resource | Best For | URL |")
[void]$md.AppendLine("|---|---|---|")
foreach ($resource in $resources) {
  [void]$md.AppendLine(("| {0} | {1} | {2} |" -f (Escape-MarkdownCell $resource.name), (Escape-MarkdownCell ($resource.bestFor -join ', ')), $resource.url))
}
[void]$md.AppendLine("")
[void]$md.AppendLine("## Usage Rule")
[void]$md.AppendLine("")
[void]$md.AppendLine("Use these references for motion direction, timing, choreography, and interaction behavior. Do not copy protected videos, exact compositions, logos, product footage, or proprietary brand motion.")
Set-Content -LiteralPath $markdownOut -Value $md.ToString() -Encoding utf8

Write-Output "MOTION_REFERENCES=$($styleRefs.Count)"
Write-Output "HIGH_SIGNAL=$($highSignal.Count)"
Write-Output "WITH_PREVIEW_VIDEO=$($withVideo.Count)"
Write-Output "PATTERNS=$($patterns.Count)"
Write-Output "WROTE=$catalogOut"
Write-Output "WROTE=$markdownOut"