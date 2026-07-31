# AI Implementation Prompt

Build a Gamma-inspired interface using this source-derived style bundle.

Reference site: https://www.gamma.io
Theme: light
Category: Crypto
North star: white-walled art gallery. The UI is a silent frame; the artwork is the only thing that should be loud.

Use these palette anchors:

- Ink Black `#0c0c0d` for High-contrast neutral action fill for primary buttons on light surfaces.
- Pure White `#ffffff` for Page canvas, card surfaces, text on dark fills, input backgrounds
- Ash `#e9e9ec` for Hairline borders, subtle dividers, hover surfaces, secondary button outlines
- Smoke `#808080` for Muted body text, metadata (mint counts, prices), inactive icons, placeholder content
- Graphite `#242629` for Icon strokes, secondary button borders, slightly elevated neutral surfaces
- Charcoal `#1d1d1e` for Rare dark surface (e.g. featured card panels) - used sparingly to create a single dark anchor in an otherwise all-white page
- Blush to Violet `#ffffff` for Hero wash gradient - soft pink-to-magenta transition used only as a backdrop to large featured artworks, never as a UI fill

Use these typography anchors:

- Gamma Sans Display `--font-gamma-sans-display` for Single-family system used for everything from micro-labels to the 72px hero display. Weight 300 for oversized hero titles ('LIGHT') creates a near-tracery effect that lets the artwork underneath read through; weight 600 reserved for short labels and the Connect button; weight 400 carries body and metadata. The custom neo-grotesque has a slightly condensed character width and flat apertures that feel more architectural than friendly.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 40-88px.
- Card padding: 20-24px.
- Element gap: 4-8px.

Build these component patterns where relevant:

- Top Navigation Bar: Primary site navigation
- Search Input (Pill): Global collection/artist search
- Connect Button (Filled Pill): Primary action - wallet connection
- Nav Link (Ghost): Section navigation
- Hero Feature Banner: Showcase for the top curated drop
- Collection Card (Grid): Featured drop in 2-column grid
- Numbered Collection List Item: Compact ranked list of drops
- View Drop Button (Outlined Pill): Secondary action on collection cards
- Print Product Card: Section product showcase (Prints / Editions)
- Mints Claimed Progress Bar: Scarcity / progress indicator
- Metadata Label: Caption-level info (price, counts, dates)
- Section Header with Inline Link: Section title bar

Do:

- Use #0c0c0d filled pills with 999px radius for the single primary action per screen; the rest must be ghost or text
- Keep all UI surfaces achromatic - only the artwork or the Blush-to-Violet gradient carries color
- Use 4px radius on artwork images and thumbnails at every size, 8px on text cards, 999px on any interactive element
- Set headlines in Gamma Sans Display weight 300 at 48-72px so the type reads as a watermark, not a wall
- Separate cards with 1px #e9e9ec hairlines or whitespace alone; never use box-shadow for elevation
- Use 14px #808080 weight 400 for all metadata (mint counts, prices, dates) and inline numerics in #0c0c0d weight 600 to lift them
- Maintain ~88px vertical gap between major sections and 40px between sub-blocks to let the artworks breathe

Avoid:

- Do not introduce a chromatic accent color, brand fill, or saturated button - the UI must stay colorless so the artwork remains the only loud element
- Do not round artwork thumbnails beyond 4px; the sharp corner is what makes the image feel like a print pinned to a wall
- Do not use box-shadow, glow, or blur on any component - depth is communicated only by hairline borders and a single dark surface
- Do not place UI text inside a scrim or colored box over artwork; the display type must sit directly on the image
- Do not use the Blush-to-Violet gradient on buttons, navs, or borders - it is reserved for the Prints section backdrop only
- Do not mix more than two type weights on a single screen; the 300/400/600 scale is for hierarchy, not decoration
- Do not center-align body text or metadata; keep descriptions and counts left-aligned with consistent left margin to the thumbnail edge

Source prompt cues:

**Quick Color Reference**
- text: #0c0c0d
- background: #ffffff
- border: #e9e9ec
- muted text: #808080
- accent: no distinct accent - UI is intentionally achromatic
- primary action: #0c0c0d (filled action)

**Example Component Prompts**
1. Build the top nav: white bar, 1px #e9e9ec bottom border, 64px tall. Left: Gamma logo + pill search (999px radius, 1px #e9e9ec border, #ffffff bg, 14px placeholder in #808080). Center: ghost links 'Explore', 'Charts', 'Create', 'Learn' in 14px #0c0c0d. Right: 'Connect' filled pill - #0c0c0d bg, #ffffff text, 999px radius, 14px weight 600, 20px 8px padding.

2. Build a hero feature: full-bleed artwork image (4px radius), overlaid display text 'LIGHT' at 72px Gamma Sans weight 300 in #0c0c0d, sitting directly on the image with no scrim. Below image: title in 20px weight 400, creator description in 16px #808080, mints-claimed progress bar (2px tall, #e9e9ec track, #0c0c0d fill), and a 'View Drop' outlined pill (999px, 1px #0c0c0d border, transparent bg, #0c0c0d text).

3. Build a 2-column collection grid: each card is 4px-radius artwork on top, 20-24px padding below for the meta block (no card background, no border, no shadow). Meta: title 18px weight 400 #0c0c0d, description 14px #808080 truncated to 2 lines, progress bar, and a 'View Drop' ghost pill.

4. Build a numbered list item: horizontal row, ordinal number in 24px weight 300 #808080 on the far left, 72px square thumbnail (4px radius), then title in 18px weight 400 #0c0c0d and a meta line in 14px #808080 ('X minted - 0.00021 BTC'). No card background, no border, just whitespace.

5. Build a section header row: left-aligned title in 24-32px weight 600 with a small leading icon, followed by a 14px #808080 subhead inline, and a right-aligned ghost link ('Explore prints') in 14px weight 400 #0c0c0d. No background, no divider - spacing alone separates sections.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
