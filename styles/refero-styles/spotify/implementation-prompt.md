# AI Implementation Prompt

Build a Spotify-inspired interface using this source-derived style bundle.

Reference site: https://www.spotify.com
Theme: dark
Category: Media
North star: Darkened record store at midnight - every surface recedes so the album art can glow.

Use these palette anchors:

- Void Black `#000000` for Primary canvas, page background - deepest layer of the dark surface stack
- Obsidian `#121212` for Card surfaces, raised panels, modal backgrounds - one step up from the canvas
- Graphite `#1f1f1f` for Elevated controls, hover surfaces, filled button backgrounds - the interactive surface tier
- Ash Gray `#333333` for Input borders, subtle dividers, inactive control outlines
- Steel Mist `#767676` for Muted text, secondary nav, disabled labels - text that fades into the background
- Cloud Gray `#b3b3b3` for Secondary body text, metadata, timestamps - readable but never competing with content
- Pure White `#ffffff` for Primary text, headings, light icon fills, pill button fills - the highest-contrast element on the dark canvas
- Spotify Green `#1ed760` for Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Premium Magenta `#af2896` for Gradient anchor for premium promotional banners, subscription upsell surfaces
- Premium Cobalt `#509bf5` for Gradient terminus for premium promotional banners, feature callouts on subscription screens
- Amber Glow `#a16b1b` for Decorative warmth - album artwork occasionally carries this tonal range

Use these typography anchors:

- SpotifyMixUI `--font-spotifymixui` for Primary UI typeface - handles all body copy, navigation, buttons, metadata, and small headings. Weight 400 carries body and labels, weight 600 appears in tab headers and emphasized metadata, weight 700 anchors section titles. The 4px size range (11-16px) keeps the entire interface at conversational volume, never editorial. Substitute: Inter, IBM Plex Sans, or DM Sans as freely available alternates with similar geometric warmth.
- SpotifyMixUITitle `--font-spotifymixuititle` for Rail and section headings - the 24px bold treatment for 'Trending songs', 'Popular artists', etc. is the only typographic moment that breaks above body size. Substitutes should be a geometric grotesque with a tall x-height and even stroke contrast.

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: .
- Section gap: 32px.
- Card padding: 12px.
- Element gap: 12px.

Build these component patterns where relevant:

- Pill Button - Green Primary: High-emphasis action button
- Pill Button - White Secondary: Medium-emphasis action
- Pill Button - Ghost Outline: Low-emphasis action
- Album Card: Content tile for albums, singles, playlists
- Artist Card: Circular artist portrait with name
- Sidebar Library Panel: Left-rail persistent navigation container
- Playlist Prompt Card: Onboarding call-out inside the library
- Top Navigation Bar: Global header
- Search Field: Global search input
- Content Rail Header: Section title bar
- Horizontal Content Rail: Scrollable card row
- Premium Banner: Full-width subscription promotion

Do:

- Use 9999px border-radius for every button, tag, and search field - the pill shape is non-negotiable for Spotify's identity.
- Apply 6px radius to all square content cards (albums, playlists) and 9999px for circular artist portraits - never mix radii within the same card type.
- Reserve #1ed760 for the single most important action per screen - log in, play, confirm. Never use it for secondary links, metadata, or decorative elements.
- Keep all text between 11px and 24px. The system is compact; no body copy should exceed 16px, and only section headings reach 24px.
- Use #000000 for the page canvas, #121212 for content cards, and #1f1f1f for interactive controls - maintain this three-tier surface hierarchy on every screen.
- Apply the 0px 8px 24px rgba(0,0,0,0.5) shadow only to content cards lifted off the canvas, never to navigation, buttons, or inputs.
- Let album artwork and artist photography supply all chromatic color in the interface. The chrome itself should remain monochrome with #ffffff and #b3b3b3 as the only text colors.

Avoid:

- Do not introduce a new chromatic accent color. The entire system runs on one green (#1ed760) plus the magenta-to-cobalt gradient for premium promotions.
- Do not use sharp corners (<4px radius) on any interactive element. Pills and soft 6px squares are the only acceptable shapes.
- Do not set body text below 11px or above 16px. The 4px size band is deliberate and compact.
- Do not use #1ed760 for hover states on white or dark buttons - green is exclusively a primary action fill, never a state indicator.
- Do not apply the premium magenta-to-cobalt gradient outside of subscription/promotional contexts. It is reserved for upsell moments.
- Do not use white or light backgrounds for any surface. The system is dark-first; even elevated cards stay at #1f1f1f or below.
- Do not add multi-layer shadow stacks, colored glows, or neumorphic effects. The single rgba(0,0,0,0.5) drop shadow is the only elevation treatment.

Source prompt cues:

Quick Color Reference:
- canvas: #000000
- surface: #121212
- elevated: #1f1f1f
- border: #ffffff (at low opacity, ~5-10%)
- text primary: #ffffff
- text secondary: #b3b3b3
- primary action: #1f1f1f (filled action)
- premium gradient: linear-gradient(90deg, #af2896, #509bf5)

Example Component Prompts:

1. Album Card: 180px square with #121212 background, 6px border radius, 0px 8px 24px rgba(0,0,0,0.5) shadow. Square album artwork fills the card with no internal padding. Below the image: song title in #ffffff at 16px SpotifyMixUI weight 400, artist name in #b3b3b3 at 14px. 12px padding around the text block.

2. Create a Primary Action Button: #1f1f1f background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

3. Artist Portrait Card: 180px diameter circle (9999px radius) with 1:1 artist image, no background, no shadow, no border. Below: artist name in #ffffff at 16px, 'Artist' label in #b3b3b3 at 14px.

4. Search Field: #1f1f1f background, 9999px radius (pill), placeholder in #ffffff at 40% opacity at 14px, left-aligned search icon in #b3b3b3. Expands width on focus. No border.

5. Premium Banner: Full-width strip, linear-gradient(90deg, #af2896, #509bf5) background. Left: 'Preview of Spotify' in #ffffff at 14px weight 700, subtitle in #ffffff at 60% opacity at 12px. Right: white pill button at 9999px radius, #000000 text at 14px weight 700, 12px 32px padding.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
