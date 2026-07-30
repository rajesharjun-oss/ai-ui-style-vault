# Spotify

Source: [Refero Style](https://styles.refero.design/style/cc59e195-fed0-4928-96d1-303752786073)
Reference site: [https://www.spotify.com](https://www.spotify.com)
Captured: 2026-07-30
Refero published: 2026-04-29T00:46:03.114Z
Refero modified: 2026-06-05T13:01:18.958Z
Theme: dark
Category: Media

## Style Summary

Explore Spotify's dark Media design system: Void Black #000000, Obsidian #121212 colors, SpotifyMixUI, SpotifyMixUITitle typography, and DESIGN.md for AI...

North star: Darkened record store at midnight - every surface recedes so the album art can glow.

## What To Borrow

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

- SpotifyMixUI `--font-spotifymixui` for Primary UI typeface - handles all body copy, navigation, buttons, metadata, and small headings. Weight 400 carries body and labels, weight 600 appears in tab headers and emphasized metadata, weight 700 anchors section titles. The 4px size range (11-16px) keeps the entire interface at conversational volume, never editorial. Substitute: Inter, IBM Plex Sans, or DM Sans as freely available alternates with similar geometric warmth.
- SpotifyMixUITitle `--font-spotifymixuititle` for Rail and section headings - the 24px bold treatment for 'Trending songs', 'Popular artists', etc. is the only typographic moment that breaks above body size. Substitutes should be a geometric grotesque with a tall x-height and even stroke contrast.

## Avoid

- Do not introduce a new chromatic accent color. The entire system runs on one green (#1ed760) plus the magenta-to-cobalt gradient for premium promotions.
- Do not use sharp corners (<4px radius) on any interactive element. Pills and soft 6px squares are the only acceptable shapes.
- Do not set body text below 11px or above 16px. The 4px size band is deliberate and compact.
- Do not use #1ed760 for hover states on white or dark buttons - green is exclusively a primary action fill, never a state indicator.
- Do not apply the premium magenta-to-cobalt gradient outside of subscription/promotional contexts. It is reserved for upsell moments.
- Do not use white or light backgrounds for any surface. The system is dark-first; even elevated cards stay at #1f1f1f or below.
- Do not add multi-layer shadow stacks, colored glows, or neumorphic effects. The single rgba(0,0,0,0.5) drop shadow is the only elevation treatment.

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
