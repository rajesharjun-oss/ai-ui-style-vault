param(
    [string]$Brief = "",
    [string]$BriefFile = "",
    [string]$ProjectPath = "",
    [string]$CatalogJson = ".\catalog.json",
    [string]$ScreenCatalogJson = ".\screen-catalog.json",
    [string]$AgentIndexJson = ".\agent-index.json",
    [string]$OutputPath = ".\VAULT_SELECTION.generated.md",
    [int]$TopStyles = 5,
    [int]$SupportingStyles = 2,
    [int]$ScreensPerPageType = 2,
    [switch]$PassThruJson
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$script:RepoRoot = Split-Path -Parent $PSScriptRoot
$script:StopWords = @{}
foreach ($word in @(
    "about", "after", "again", "also", "and", "are", "build", "can", "for", "from", "have", "into", "like", "make", "more", "need", "needs", "site", "that", "the", "their", "them", "this", "tool", "using", "with", "would", "website", "where", "when", "your"
)) {
    $script:StopWords[$word] = $true
}

function Resolve-VaultPath {
    param([string]$Path)
    if ([string]::IsNullOrWhiteSpace($Path)) { return $null }
    if ([System.IO.Path]::IsPathRooted($Path)) { return $Path }
    return (Join-Path $script:RepoRoot $Path)
}

function Read-JsonFile {
    param([string]$Path)
    $resolved = Resolve-VaultPath $Path
    if (-not (Test-Path -LiteralPath $resolved)) {
        throw "Required JSON file not found: $resolved"
    }
    return Get-Content -LiteralPath $resolved -Raw | ConvertFrom-Json
}

function Get-ObjectValue {
    param($Object, [string]$Name)
    if ($null -eq $Object) { return $null }
    if ($Object.PSObject.Properties.Name -contains $Name) { return $Object.$Name }
    return $null
}

function Normalize-Text {
    param([string]$Text)
    if ([string]::IsNullOrWhiteSpace($Text)) { return "" }
    return (($Text.ToLowerInvariant() -replace "[^a-z0-9+#&.]+", " ") -replace "\s+", " ").Trim()
}

function Get-Terms {
    param([string]$Text)
    $normalized = Normalize-Text $Text
    if ([string]::IsNullOrWhiteSpace($normalized)) { return @() }
    return @($normalized -split "\s+" | Where-Object { $_.Length -ge 3 -and -not $script:StopWords.ContainsKey($_) } | Select-Object -Unique)
}

function Convert-ToSearchText {
    param($Value)
    if ($null -eq $Value) { return "" }
    if ($Value -is [string]) { return $Value }
    if ($Value -is [System.Array]) {
        return (($Value | ForEach-Object { Convert-ToSearchText $_ }) -join " ")
    }
    if ($Value -is [System.Management.Automation.PSCustomObject]) {
        $propertyValues = @($Value.PSObject.Properties | ForEach-Object { $_.Value })
        return (($propertyValues | ForEach-Object { Convert-ToSearchText $_ }) -join " ")
    }
    return [string]$Value
}

function Test-ContainsAlias {
    param([string]$Haystack, [string[]]$Aliases)
    $text = Normalize-Text $Haystack
    foreach ($alias in $Aliases) {
        $needle = Normalize-Text $alias
        if ($needle -and $text.Contains($needle)) { return $true }
    }
    return $false
}

function Get-MatchedAliases {
    param([string]$Haystack, [string[]]$Aliases, [int]$Limit = 8)
    $text = Normalize-Text $Haystack
    $matches = New-Object System.Collections.Generic.List[string]
    foreach ($alias in $Aliases) {
        $needle = Normalize-Text $alias
        if ($needle -and $text.Contains($needle) -and -not $matches.Contains($alias)) {
            [void]$matches.Add($alias)
            if ($matches.Count -ge $Limit) { break }
        }
    }
    return @($matches)
}

function Add-UniqueString {
    param([System.Collections.Generic.List[string]]$List, [string]$Value)
    if (-not [string]::IsNullOrWhiteSpace($Value) -and -not $List.Contains($Value)) {
        [void]$List.Add($Value)
    }
}

function Get-ProjectContext {
    param([string]$Path)
    $context = [ordered]@{
        Path = $Path
        Files = @()
        Stack = @()
        Text = ""
    }
    if ([string]::IsNullOrWhiteSpace($Path)) { return [pscustomobject]$context }

    $resolved = $Path
    if (-not [System.IO.Path]::IsPathRooted($resolved)) {
        $resolved = Join-Path (Get-Location) $Path
    }
    if (-not (Test-Path -LiteralPath $resolved)) { return [pscustomobject]$context }

    $root = (Resolve-Path -LiteralPath $resolved).Path
    $contentParts = New-Object System.Collections.Generic.List[string]
    $files = New-Object System.Collections.Generic.List[string]
    $stack = New-Object System.Collections.Generic.List[string]

    $candidateFiles = @(
        "package.json", "README.md", "readme.md", "app.json", "components.json",
        "tailwind.config.ts", "tailwind.config.js", "vite.config.ts", "vite.config.js",
        "next.config.ts", "next.config.js", "src/App.tsx", "src/App.jsx", "src/main.tsx",
        "app/page.tsx", "pages/index.tsx"
    )

    foreach ($relative in $candidateFiles) {
        $candidate = Join-Path $root $relative
        if (Test-Path -LiteralPath $candidate -PathType Leaf) {
            [void]$files.Add($relative)
            try {
                $text = Get-Content -LiteralPath $candidate -Raw
                if ($text.Length -gt 12000) { $text = $text.Substring(0, 12000) }
                [void]$contentParts.Add("FILE: $relative`n$text")
                if ($relative -eq "package.json") {
                    $pkg = $text | ConvertFrom-Json
                    $depsText = Convert-ToSearchText @((Get-ObjectValue $pkg "dependencies"), (Get-ObjectValue $pkg "devDependencies"), (Get-ObjectValue $pkg "scripts"))
                    foreach ($signal in @("react", "next", "vite", "vue", "svelte", "tailwind", "shadcn", "typescript", "framer-motion", "lucide", "three")) {
                        if ((Normalize-Text $depsText).Contains((Normalize-Text $signal))) { Add-UniqueString $stack $signal }
                    }
                }
            } catch {
                [void]$contentParts.Add("FILE: $relative")
            }
        }
    }

    $context.Files = @($files)
    $context.Stack = @($stack)
    $context.Text = ($contentParts -join "`n`n")
    return [pscustomobject]$context
}

function Get-StyleSearchText {
    param($Style)
    $parts = @(
        (Get-ObjectValue $Style "name"),
        (Get-ObjectValue $Style "slug"),
        (Get-ObjectValue $Style "category"),
        (Get-ObjectValue $Style "bestFor"),
        (Get-ObjectValue $Style "tags"),
        (Get-ObjectValue $Style "theme"),
        (Get-ObjectValue $Style "northStar"),
        (Get-ObjectValue $Style "summary"),
        (Get-ObjectValue $Style "fonts"),
        (Get-ObjectValue $Style "primaryColors")
    )
    return Normalize-Text (($parts | ForEach-Object { Convert-ToSearchText $_ }) -join " ")
}

function Get-ScreenSearchText {
    param($Screen)
    $parts = @(
        (Get-ObjectValue $Screen "channel"),
        (Get-ObjectValue $Screen "pageType"),
        (Get-ObjectValue $Screen "pageTypes"),
        (Get-ObjectValue $Screen "entity"),
        (Get-ObjectValue $Screen "designPatterns"),
        (Get-ObjectValue $Screen "pageElements"),
        (Get-ObjectValue $Screen "colors")
    )
    return Normalize-Text (($parts | ForEach-Object { Convert-ToSearchText $_ }) -join " ")
}

function Escape-MarkdownCell {
    param([string]$Text)
    if ($null -eq $Text) { return "" }
    return (($Text -replace "\|", "\\|") -replace "`r?`n", " ").Trim()
}

function Short-Text {
    param([string]$Text, [int]$Length = 160)
    if ([string]::IsNullOrWhiteSpace($Text)) { return "Not provided" }
    $oneLine = (($Text -replace "`r?`n", " ") -replace "\s+", " ").Trim()
    if ($oneLine.Length -le $Length) { return $oneLine }
    return ($oneLine.Substring(0, $Length - 3) + "...")
}

$domainAliases = [ordered]@{
    "ai-workspace" = @("ai", "assistant", "agent", "llm", "chatbot", "automation", "workspace", "prompt")
    "developer-tool" = @("developer", "api", "sdk", "code", "docs", "webhook", "integration", "terminal", "git")
    "saas-dashboard" = @("saas", "dashboard", "admin", "crm", "operations", "portal", "analytics", "b2b", "reporting")
    "finance" = @("finance", "fintech", "bank", "crypto", "trading", "payment", "invoice", "accounting", "wallet")
    "commerce" = @("commerce", "ecommerce", "shop", "store", "catalog", "checkout", "product", "retail", "marketplace")
    "health-wellness" = @("health", "wellness", "care", "patient", "clinic", "fitness", "meditation", "therapy")
    "education" = @("education", "learning", "course", "school", "student", "lesson", "training")
    "creative-studio" = @("portfolio", "agency", "studio", "creative", "case study", "media", "brand")
    "local-service" = @("restaurant", "salon", "clinic", "showroom", "hotel", "real estate", "service", "appointment", "booking")
}

$pageAliases = [ordered]@{
    "product-page-landing" = @("landing", "homepage", "home page", "marketing", "hero", "product page", "website", "conversion")
    "dashboard" = @("dashboard", "admin", "analytics", "metrics", "overview", "reports", "stats", "console")
    "login" = @("login", "log in", "sign in", "signup", "sign up", "auth", "authentication", "onboarding")
    "product-details" = @("product details", "details", "item page", "specification", "pricing detail", "comparison")
    "catalog-page" = @("catalog", "listing", "browse", "search results", "directory", "collection")
    "profile-account" = @("profile", "account", "settings", "billing", "preferences", "user page")
    "paywall-subscription" = @("pricing", "paywall", "subscription", "plans", "membership")
    "blog" = @("blog", "article", "news", "journal", "content", "editorial")
    "about" = @("about", "story", "company", "mission", "team")
    "contacts" = @("contact", "contacts", "support", "sales", "visit", "location")
    "developers-page" = @("developers", "docs", "documentation", "api docs", "sdk")
    "integration-page" = @("integration", "integrations", "connectors", "apps", "plugins")
    "careers" = @("career", "careers", "jobs", "hiring")
    "media-kit" = @("media kit", "press", "brand kit")
    "404-page" = @("404", "not found", "error page")
}

$toneAliases = [ordered]@{
    "premium" = @("premium", "luxury", "elegant", "refined", "polished", "high end")
    "minimal" = @("minimal", "clean", "simple", "quiet", "calm")
    "playful" = @("playful", "fun", "friendly", "colorful", "warm")
    "technical" = @("technical", "developer", "precise", "terminal", "docs")
    "editorial" = @("editorial", "magazine", "story", "article", "serif")
    "cinematic" = @("cinematic", "immersive", "visual", "motion", "video")
    "utilitarian" = @("utilitarian", "dense", "table", "operational", "admin")
    "high-contrast" = @("high contrast", "black", "white", "monochrome", "bold")
}

$briefText = $Brief
if (-not [string]::IsNullOrWhiteSpace($BriefFile)) {
    $briefFilePath = $BriefFile
    if (-not [System.IO.Path]::IsPathRooted($briefFilePath)) { $briefFilePath = Join-Path (Get-Location) $briefFilePath }
    if (Test-Path -LiteralPath $briefFilePath) {
        $briefText = (($briefText, (Get-Content -LiteralPath $briefFilePath -Raw)) | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }) -join "`n`n"
    }
}

$catalog = Read-JsonFile $CatalogJson
$screenCatalog = Read-JsonFile $ScreenCatalogJson
$agentIndex = Read-JsonFile $AgentIndexJson
$project = Get-ProjectContext $ProjectPath
$combinedText = (($briefText, $project.Text, ($project.Stack -join " ")) | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }) -join "`n`n"
$combinedNormalized = Normalize-Text $combinedText
$briefTerms = Get-Terms $combinedText

$styles = @()
if ($catalog.PSObject.Properties.Name -contains "styles") { $styles = @($catalog.styles) }
elseif ($catalog.PSObject.Properties.Name -contains "items") { $styles = @($catalog.items) }
if ($styles.Count -eq 0) { throw "No styles found in $CatalogJson" }

$screens = @()
foreach ($propertyName in @("references", "screenReferences", "screens", "items")) {
    if ($screenCatalog.PSObject.Properties.Name -contains $propertyName) {
        $screens = @($screenCatalog.$propertyName)
        break
    }
}

$detectedDomains = New-Object System.Collections.Generic.List[string]
foreach ($key in $domainAliases.Keys) {
    if (Test-ContainsAlias $combinedText $domainAliases[$key]) { Add-UniqueString $detectedDomains $key }
}

$detectedTones = New-Object System.Collections.Generic.List[string]
foreach ($key in $toneAliases.Keys) {
    if (Test-ContainsAlias $combinedText $toneAliases[$key]) { Add-UniqueString $detectedTones $key }
}

$neededPages = New-Object System.Collections.Generic.List[string]
foreach ($key in $pageAliases.Keys) {
    if (Test-ContainsAlias $combinedText $pageAliases[$key]) { Add-UniqueString $neededPages $key }
}

$archetypes = @()
if ($agentIndex.PSObject.Properties.Name -contains "productArchetypes") { $archetypes = @($agentIndex.productArchetypes) }
$matchedArchetypes = New-Object System.Collections.Generic.List[object]
foreach ($archetype in $archetypes) {
    $signals = @((Get-ObjectValue $archetype "name"), (Get-ObjectValue $archetype "selectionTags"), (Get-ObjectValue $archetype "styleHints"))
    if (Test-ContainsAlias $combinedText @($signals | ForEach-Object { Convert-ToSearchText $_ })) {
        [void]$matchedArchetypes.Add($archetype)
        foreach ($page in @((Get-ObjectValue $archetype "screenPageTypes"))) { Add-UniqueString $neededPages ([string]$page) }
    }
}

if ($neededPages.Count -eq 0) {
    foreach ($page in @("product-page-landing", "dashboard", "login", "contacts")) { Add-UniqueString $neededPages $page }
}
if ($combinedNormalized.Contains("website") -or $combinedNormalized.Contains("business")) {
    Add-UniqueString $neededPages "product-page-landing"
    Add-UniqueString $neededPages "about"
    Add-UniqueString $neededPages "contacts"
}

$styleScores = foreach ($style in $styles) {
    $search = Get-StyleSearchText $style
    $score = 0
    $why = New-Object System.Collections.Generic.List[string]

    $directMatches = @($briefTerms | Where-Object { $_.Length -gt 3 -and $search.Contains($_) } | Select-Object -Unique -First 8)
    if ($directMatches.Count -gt 0) {
        $points = [Math]::Min(24, $directMatches.Count * 3)
        $score += $points
        [void]$why.Add("term match: " + ($directMatches -join ", "))
    }

    foreach ($domain in $detectedDomains) {
        $aliases = @($domainAliases[$domain]) + @($domain)
        if (Test-ContainsAlias $search $aliases) {
            $score += 9
            [void]$why.Add("domain: $domain")
        }
    }

    foreach ($tone in $detectedTones) {
        $aliases = @($toneAliases[$tone]) + @($tone)
        if (Test-ContainsAlias $search $aliases) {
            $score += 7
            [void]$why.Add("tone: $tone")
        }
    }

    foreach ($archetype in $matchedArchetypes) {
        $styleHints = @((Get-ObjectValue $archetype "styleHints") | ForEach-Object { Convert-ToSearchText $_ })
        $selectionTags = @((Get-ObjectValue $archetype "selectionTags") | ForEach-Object { Convert-ToSearchText $_ })
        if (Test-ContainsAlias $search $styleHints) {
            $score += 16
            [void]$why.Add("archetype hint: " + (Get-ObjectValue $archetype "name"))
        } elseif (Test-ContainsAlias $search $selectionTags) {
            $score += 8
            [void]$why.Add("archetype tag: " + (Get-ObjectValue $archetype "name"))
        }
    }

    $files = Get-ObjectValue $style "files"
    if ($null -ne $files) {
        foreach ($fileSignal in @("design", "prompt", "cssVariables", "designTokens", "tailwind")) {
            if ($files.PSObject.Properties.Name -contains $fileSignal -and -not [string]::IsNullOrWhiteSpace([string]$files.$fileSignal)) { $score += 2 }
        }
        if (($project.Stack -contains "tailwind") -and ($files.PSObject.Properties.Name -contains "tailwind")) { $score += 4; [void]$why.Add("stack: Tailwind tokens") }
        if (($project.Stack -contains "react") -or ($project.Stack -contains "next") -or ($project.Stack -contains "vite")) { $score += 2 }
    }

    $theme = [string](Get-ObjectValue $style "theme")
    if ($combinedNormalized.Contains("dark") -and (Normalize-Text $theme).Contains("dark")) { $score += 5; [void]$why.Add("theme: dark") }
    if (($combinedNormalized.Contains("light") -or $combinedNormalized.Contains("clean")) -and (Normalize-Text $theme).Contains("light")) { $score += 3; [void]$why.Add("theme: light") }
    if (($combinedNormalized.Contains("premium") -or $combinedNormalized.Contains("luxury")) -and (Test-ContainsAlias $search @("premium", "luxury", "elegant", "refined", "apple"))) { $score += 5 }

    $score = [Math]::Min(100, [Math]::Max(0, $score))
    if ($why.Count -eq 0) { [void]$why.Add("general style-system availability") }

    [pscustomobject]@{
        Score = [int]$score
        Name = [string](Get-ObjectValue $style "name")
        Slug = [string](Get-ObjectValue $style "slug")
        Theme = [string](Get-ObjectValue $style "theme")
        Category = [string](Get-ObjectValue $style "category")
        Path = [string](Get-ObjectValue $style "path")
        SourceUrl = [string](Get-ObjectValue $style "sourceUrl")
        Why = (($why | Select-Object -Unique -First 5) -join "; ")
        Style = $style
    }
}

$rankedStyles = @($styleScores | Sort-Object -Property @{ Expression = "Score"; Descending = $true }, @{ Expression = "Name"; Descending = $false })
$primaryStyle = $rankedStyles | Select-Object -First 1
$supportingStyleRows = @($rankedStyles | Select-Object -Skip 1 -First $SupportingStyles)

$screenScores = foreach ($screen in $screens) {
    $search = Get-ScreenSearchText $screen
    $pageType = Get-ObjectValue $screen "pageType"
    $pageSlug = ""
    $pageName = ""
    if ($null -ne $pageType) {
        $pageSlug = [string](Get-ObjectValue $pageType "slug")
        $pageName = [string](Get-ObjectValue $pageType "name")
    }
    if ([string]::IsNullOrWhiteSpace($pageSlug)) { $pageSlug = Normalize-Text ([string](Get-ObjectValue $screen "pageTypes")) -replace "\s+", "-" }
    if ([string]::IsNullOrWhiteSpace($pageName)) { $pageName = [string](Get-ObjectValue $screen "pageTypes") }

    $score = 0
    $why = New-Object System.Collections.Generic.List[string]
    if ($neededPages.Contains($pageSlug)) { $score += 60; [void]$why.Add("needed page: $pageSlug") }
    elseif (Test-ContainsAlias $combinedText (@($pageAliases[$pageSlug]) + @($pageName))) { $score += 35; [void]$why.Add("page term match") }

    $directMatches = @($briefTerms | Where-Object { $_.Length -gt 3 -and $search.Contains($_) } | Select-Object -Unique -First 5)
    if ($directMatches.Count -gt 0) { $score += [Math]::Min(15, $directMatches.Count * 3); [void]$why.Add("term match: " + ($directMatches -join ", ")) }

    $channel = [string](Get-ObjectValue $screen "channel")
    if (($project.Stack -contains "react" -or $project.Stack -contains "next" -or $project.Stack -contains "vite" -or $combinedNormalized.Contains("web")) -and $channel -eq "web") { $score += 8; [void]$why.Add("channel: web") }
    if (($combinedNormalized.Contains("ios") -or $combinedNormalized.Contains("mobile") -or $combinedNormalized.Contains("app")) -and $channel -eq "ios-apps") { $score += 8; [void]$why.Add("channel: iOS") }

    foreach ($tone in $detectedTones) {
        if (Test-ContainsAlias $search (@($toneAliases[$tone]) + @($tone))) { $score += 3 }
    }

    $entity = Get-ObjectValue $screen "entity"
    $entityName = [string](Get-ObjectValue $entity "name")
    if ([string]::IsNullOrWhiteSpace($entityName)) { $entityName = "Unknown" }

    $score = [Math]::Min(100, [Math]::Max(0, $score))
    if ($why.Count -eq 0) { [void]$why.Add("page reference availability") }

    [pscustomobject]@{
        Score = [int]$score
        PageTypeSlug = $pageSlug
        PageTypeName = $pageName
        Channel = $channel
        EntityName = $entityName
        Path = [string](Get-ObjectValue $screen "path")
        ReferoViewUrl = [string](Get-ObjectValue $screen "referoViewUrl")
        Why = (($why | Select-Object -Unique -First 4) -join "; ")
        Screen = $screen
    }
}

$selectedScreens = New-Object System.Collections.Generic.List[object]
foreach ($page in $neededPages) {
    $matches = @($screenScores | Where-Object { $_.PageTypeSlug -eq $page } | Sort-Object -Property @{ Expression = "Score"; Descending = $true }, @{ Expression = "EntityName"; Descending = $false } | Select-Object -First $ScreensPerPageType)
    foreach ($match in $matches) { [void]$selectedScreens.Add($match) }
}

$readFiles = New-Object System.Collections.Generic.List[string]
$primaryFiles = Get-ObjectValue $primaryStyle.Style "files"
foreach ($fileProp in @("readme", "design", "prompt", "cssVariables", "designTokens", "tailwind")) {
    if ($null -ne $primaryFiles -and $primaryFiles.PSObject.Properties.Name -contains $fileProp) { Add-UniqueString $readFiles ([string]$primaryFiles.$fileProp) }
}
foreach ($screenRow in $selectedScreens) {
    $files = Get-ObjectValue $screenRow.Screen "files"
    foreach ($fileProp in @("readme", "prompt", "screen", "colors", "pageElements", "cssVariables", "designTokens")) {
        if ($null -ne $files -and $files.PSObject.Properties.Name -contains $fileProp) { Add-UniqueString $readFiles ([string]$files.$fileProp) }
    }
}

$resolvedOutput = $OutputPath
if (-not [System.IO.Path]::IsPathRooted($resolvedOutput)) { $resolvedOutput = Join-Path (Get-Location) $OutputPath }
$outputParent = Split-Path -Parent $resolvedOutput
if (-not [string]::IsNullOrWhiteSpace($outputParent) -and -not (Test-Path -LiteralPath $outputParent)) {
    New-Item -ItemType Directory -Path $outputParent | Out-Null
}

$md = New-Object System.Text.StringBuilder
[void]$md.AppendLine("# Vault Selection")
[void]$md.AppendLine("")
[void]$md.AppendLine("Generated by ``scripts/select-vault-style.ps1`` on $(Get-Date -Format yyyy-MM-dd).")
[void]$md.AppendLine("")
[void]$md.AppendLine("## Target")
[void]$md.AppendLine("")
[void]$md.AppendLine("- Product or business: $(Short-Text $briefText 220)")
[void]$md.AppendLine("- Target repo or output path: $(if ([string]::IsNullOrWhiteSpace($ProjectPath)) { 'Not provided' } else { $ProjectPath })")
[void]$md.AppendLine("- Detected stack: $(if ($project.Stack.Count -gt 0) { $project.Stack -join ', ' } else { 'Not detected' })")
[void]$md.AppendLine("- Detected domains: $(if ($detectedDomains.Count -gt 0) { $detectedDomains -join ', ' } else { 'general' })")
[void]$md.AppendLine("- Needed page types: $($neededPages -join ', ')")
[void]$md.AppendLine("")
[void]$md.AppendLine("## Selected Vault References")
[void]$md.AppendLine("")
[void]$md.AppendLine("Primary style bundle:")
[void]$md.AppendLine("")
[void]$md.AppendLine("- Name: $($primaryStyle.Name)")
[void]$md.AppendLine(("- Path: ``{0}``" -f $primaryStyle.Path))
[void]$md.AppendLine("- Score: $($primaryStyle.Score)/100")
[void]$md.AppendLine("- Why it fits: $($primaryStyle.Why)")
if (-not [string]::IsNullOrWhiteSpace($primaryStyle.SourceUrl)) { [void]$md.AppendLine("- Source: $($primaryStyle.SourceUrl)") }
[void]$md.AppendLine("")
[void]$md.AppendLine("Supporting style references:")
[void]$md.AppendLine("")
if ($supportingStyleRows.Count -eq 0) {
    [void]$md.AppendLine("- None selected.")
} else {
    foreach ($row in $supportingStyleRows) {
        [void]$md.AppendLine(("- ``{0}`` - {1}, score {2}/100. {3}" -f $row.Path, $row.Name, $row.Score, $row.Why))
    }
}
[void]$md.AppendLine("")
[void]$md.AppendLine("Page-specific screen references:")
[void]$md.AppendLine("")
if ($selectedScreens.Count -eq 0) {
    [void]$md.AppendLine("- None selected. Use style bundle page guidance only.")
} else {
    foreach ($row in $selectedScreens) {
        [void]$md.AppendLine(("- {0} / {1}: ``{2}`` - {3}, score {4}/100. {5}" -f $row.PageTypeName, $row.Channel, $row.Path, $row.EntityName, $row.Score, $row.Why))
    }
}
[void]$md.AppendLine("")
[void]$md.AppendLine("## Candidate Score Table")
[void]$md.AppendLine("")
[void]$md.AppendLine("| Score | Style | Theme | Category | Path | Why |")
[void]$md.AppendLine("|---:|---|---|---|---|---|")
foreach ($row in @($rankedStyles | Select-Object -First $TopStyles)) {
    [void]$md.AppendLine(("| {0} | {1} | {2} | {3} | ``{4}`` | {5} |" -f $row.Score, (Escape-MarkdownCell $row.Name), (Escape-MarkdownCell $row.Theme), (Escape-MarkdownCell $row.Category), $row.Path, (Escape-MarkdownCell $row.Why)))
}
[void]$md.AppendLine("")
[void]$md.AppendLine("## Read Before Implementation")
[void]$md.AppendLine("")
foreach ($file in $readFiles) { [void]$md.AppendLine(("- ``{0}``" -f $file)) }
[void]$md.AppendLine("")
[void]$md.AppendLine("## Adaptation Plan")
[void]$md.AppendLine("")
[void]$md.AppendLine("- Color and theme: start from the primary style tokens, then adjust contrast and brand accents for the target product.")
[void]$md.AppendLine("- Typography: keep the selected style's type hierarchy unless the target repo already has a stricter font system.")
[void]$md.AppendLine("- Spacing and layout: use the selected style rhythm, but fit real content and responsive breakpoints from the target repo.")
[void]$md.AppendLine("- Components: map buttons, cards, forms, tables, nav, menus, and states into the target component system.")
[void]$md.AppendLine("- Page structure: use selected screen references for information architecture, not as copied layouts.")
[void]$md.AppendLine("- Interaction states: include loading, empty, error, success, disabled, hover, focus, active, and mobile states.")
[void]$md.AppendLine("")
[void]$md.AppendLine("## Copy And Asset Policy")
[void]$md.AppendLine("")
[void]$md.AppendLine("- Use vault references as inspiration and implementation guidance only.")
[void]$md.AppendLine("- Do not copy protected logos, screenshots, product photos, exact marketing copy, or proprietary page layouts.")
[void]$md.AppendLine("- Use user-provided assets, owned assets, generated assets, or clearly licensed media.")
[void]$md.AppendLine("- Keep external source URLs in research notes instead of vendoring screenshots or brand assets.")
[void]$md.AppendLine("")
[void]$md.AppendLine("## QA Plan")
[void]$md.AppendLine("")
[void]$md.AppendLine("- Run available lint, typecheck, test, and build commands.")
[void]$md.AppendLine("- Check desktop, mobile, and wide layouts for text overflow, edge padding, sticky headers, and form alignment.")
[void]$md.AppendLine("- Run ``scripts/validate-generated-site.ps1`` when the output is a rendered website or web app.")
[void]$md.AppendLine("- Audit copied assets and placeholder text before handoff.")

[System.IO.File]::WriteAllText($resolvedOutput, $md.ToString(), [System.Text.UTF8Encoding]::new($false))

$result = [ordered]@{
    primaryStyle = [ordered]@{ name = $primaryStyle.Name; score = $primaryStyle.Score; path = $primaryStyle.Path; why = $primaryStyle.Why }
    supportingStyles = @($supportingStyleRows | ForEach-Object { [ordered]@{ name = $_.Name; score = $_.Score; path = $_.Path; why = $_.Why } })
    neededPageTypes = @($neededPages)
    screenReferences = @($selectedScreens | ForEach-Object { [ordered]@{ pageType = $_.PageTypeSlug; channel = $_.Channel; entity = $_.EntityName; score = $_.Score; path = $_.Path; why = $_.Why } })
    outputPath = $resolvedOutput
}

Write-Output "PRIMARY_STYLE=$($primaryStyle.Name)"
Write-Output "PRIMARY_SCORE=$($primaryStyle.Score)"
Write-Output "PRIMARY_PATH=$($primaryStyle.Path)"
Write-Output "SCREEN_REFERENCES=$($selectedScreens.Count)"
Write-Output "OUTPUT=$resolvedOutput"

if ($PassThruJson) {
    $result | ConvertTo-Json -Depth 8
}
