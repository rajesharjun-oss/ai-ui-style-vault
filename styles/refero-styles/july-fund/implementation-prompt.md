# AI Implementation Prompt

Build a July Fund-inspired interface using this source-derived style bundle.

Reference site: https://july.fund
Theme: dark
Category: Fintech
North star: dark gallery monograph with chromatic chapter cards

Use these palette anchors:

- Obsidian `#000000` for Page canvas, deepest card base, and the void between sections - the room the cards hang in
- Coffee Bean `#433e3c` for Dominant border color across cards, badges, and dividers - the hairline that frames every chromatic block
- Cream Paper `#f0e7e4` for Light card surface for the hero/about panel and inverted buttons - a warm off-white that reads as printed paper on the dark canvas
- Charcoal `#2b2b2b` for Secondary surface and elevated card base for monochrome content blocks
- Espresso `#221f1e` for Button background for primary text controls on dark surfaces - one shade deeper than the card it sits in
- Stone Gray `#898989` for Muted body copy, list markers, and supporting metadata - the whisper tier below primary text
- Paper White `#ffffff` for Headline color on dark cards, badge text on chromatic fills, and link highlights
- Forest Floor `#113619` for Themed card surface for nature/climate/sustainability chapters - the deepest chromatic field, reads as moss or deep canopy
- Twilight Violet `#322b66` for Themed card surface for space, frontier, and science verticals - saturated enough to dominate a grid cell, dark enough to hold white type
- Olive Depth `#2e2909` for Themed card surface for energy and industry chapters - a near-black ochre that glows against the canvas
- Solar Yellow `#fde440` for High-impact accent card fill for transformation and thesis verticals - the loudest single block in the system, used sparingly to punctuate the grid
- Mint Chip `#56d270` for Small uppercase tag/badge fill for news and announcement labels - the only saturated green used at small scale
- Lavender Mist `#c6bffa` for Soft accent for secondary badges and highlight borders on the violet card family
- Ember Red `#b9534a` for Reserved research and analytical-content badge fill - used almost never; its rarity makes it register as a category marker

Use these typography anchors:

- Portrait `--font-portrait` for Display and heading serif used for the wordmark, section titles, and card headlines. Portrait is a high-contrast didone-style serif; its hairline strokes and sharp serifs give the site its monograph feel. A single weight (400) is used - no bold headlines, authority comes from size and contrast alone.
- Helvetica Neue `--font-helvetica-neue` for Body, UI, badges, buttons, and metadata. Tight 400 for body, 700 for emphasis. The wide letter-spacing at small sizes (0.20-0.25em) is the defining micro-typography move: even 8px labels read as intentional, not afterthoughts.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1280px.
- Section gap: 80px.
- Card padding: 40px.
- Element gap: 20px.

Build these component patterns where relevant:

- Themed Category Card: Primary content unit - each card carries a single saturated background and acts as a chapter in the grid.
- Cream Hero Panel: Light inverted opening section that introduces the fund before the dark grid begins.
- Portfolio Founder Card: Monochrome card introducing an individual team member.
- News Article Card: Editorial post preview with a photographic image, date, excerpt, and read-more control.
- Category Tag Badge: Uppercase label that classifies a card's content vertical.
- Ghost Pill Button: Default text control for navigation, read-more, and secondary actions.
- Filled Pill Button: Rare primary action - used only where a strong CTA is needed.
- Location Card: Compact monochrome card displaying a city and weather metadata.
- Image Tile: Inset photographic or illustrative block within a card.
- Map Tile: Light-surface map preview for location-based content.
- Fund Thesis Statement Block: Long-form text card on a solid chromatic field that explains a fund vertical.
- Footer Link Block: Closing navigation and contact region on the dark canvas.

Do:

- Use Portrait 400 at 30-96px for every heading - never substitute a sans-serif headline.
- Set all uppercase labels (badges, buttons, metadata) at 8-10px with 0.20-0.25em letter-spacing and weight 700.
- Let each card pick exactly one chromatic field (Forest Floor, Twilight Violet, Olive Depth, Solar Yellow, or Charcoal) as its background - no gradients, no images-as-backgrounds inside cards.
- Use 20px radius for cards, 24px for buttons (full pill), 8px for badges, 12px for images.
- Pair Mint Chip (#56d270) badges only with dark or neutral cards; reserve Solar Yellow (#fde440) for the single loudest thesis card in any grid.
- Keep 40px card padding on the dominant axis and 20px on the minor axis; 45px column gap between paired text columns.
- Separate sections with 80px of Obsidian void - never use a divider line between cards, the radius and the gap are the separator.

Avoid:

- Don't add box-shadow, glow, or blur to any element - the system is flat by design.
- Don't use bold weights for Portrait headlines; authority comes from size, not weight.
- Don't mix two chromatic fills inside a single card - pick one field and commit.
- Don't place body copy in a chromatic color other than Stone Gray (#898989), Paper White, or Coffee Bean - no accent text.
- Don't use buttons with square or 8px corners; the 24px pill is non-negotiable.
- Don't set background gradients on text-forward cards - gradients are reserved for the radial accent washes in hero/empty states.
- Don't center body paragraphs or labels; left-align everything except the wordmark.

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
