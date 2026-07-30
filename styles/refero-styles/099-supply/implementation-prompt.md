# AI Implementation Prompt

Build a 099 SUPPLY-inspired interface using this source-derived style bundle.

Reference site: https://099.supply
Theme: light
Category: Design
North star: Gallery wall of black-on-white objects

Use these palette anchors:

- Canvas White `#ffffff` for Page background, card surfaces, button backgrounds, link containers - the gallery wall everything sits on
- Ink `#101010` for Primary headings, body text, and icon fills on light surfaces. Do not promote it to the primary CTA color
- Charcoal `#000000` for Pure-black decorative fills for mockup rendering and high-contrast object silhouettes
- Muted Hard `#222222` for Dark surface tint for elevated dark components and modal/overlay backgrounds; Dark surface fill for elevated panels, toggle/loader component backgrounds
- Muted `#555555` for Secondary body text, supporting copy, muted helper labels
- Muted Soft `#999999` for Section headings, icon fills, badge text, hover border state - the softest readable gray
- Border Soft `#c8c8c8` for Soft hairline borders for less prominent dividers and input outlines
- Border Subtle `#e0e0e0` for Card edges, link borders, subtle dividers between tiles - the dominant hairline color

Use these typography anchors:

- Soehne Mono `--font-soehne-mono` for The exclusive typeface - used for every heading, body, badge, link, icon, and label. Weight 400 dominates; weight 500 is reserved for the 26px hero label. All non-body sizes render in uppercase with tracking between 0.02em and 0.18em. The monospaced face reinforces the museum-catalog, specimen-tag atmosphere.

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: .
- Section gap: 80px.
- Card padding: .
- Element gap: 12px.

Build these component patterns where relevant:

- Mockup Tile Card: Primary unit - displays a 3D mockup asset with catalog-style metadata strip
- Framer Component Tile Card: Second tile variant for interactive component previews
- Section Heading: Section label above each grid block
- Primary Button: Filled dark button for 'Buy' and conversion actions
- Ghost Button: Secondary outlined button paired with primary
- Metadata Label: Catalog-style tag below each tile
- Modal Panel: Overlay for copy/info interactions
- Theme Toggle: Interactive component demo - pill switch
- Loader Ring: Circular progress component demo
- Browser Frame: Windowed screenshot frame component
- Compare Slider: Before/after image comparison component
- Table Component: Structured data table demo

Do:

- Use only Soehne Mono (or JetBrains Mono substitute) for every piece of text - no second typeface.
- Set every label, badge, and metadata strip in uppercase with tracking between 0.02em and 0.18em.
- Render all buttons at 9999px radius and all cards/tiles at 8px radius - the contrast is the system.
- Use 1px solid borders in #e0e0e0 for default state, #999999 for hover, and #101010 for strong emphasis.
- Keep all mockup assets on pure white backgrounds centered within their tiles - the object IS the content.
- Maintain the catalog metadata pattern: asset ID left ('M 005'), asset name right ('IPHONE'), separated by a horizontal divider.
- Use #101010 as the sole fill for dark elements - buttons, strokes, silhouettes, checkmark icons, loader arcs.

Avoid:

- Never introduce chromatic color - no blues, greens, reds, or any hue. The system is monochrome.
- Never apply box-shadow, drop-shadow, or any elevation effect. Depth comes from hairline borders only.
- Never use a sans-serif or proportional typeface. Mono is non-negotiable.
- Never use background gradients except for the single conic-gradient loader pattern (#101010 #c8c8c8).
- Never set border-radius below 4px on cards or above 9999px on buttons - the radius vocabulary is fixed.
- Never use bold (600+) or light (300-) weights. Stay at 400, with 500 reserved for the 26px section heading.
- Never mix section heading style - always 26px uppercase #999999 with 0.18em tracking, nothing decorative.

Source prompt cues:

**Quick Color Reference**
- canvas/background: #ffffff
- primary text: #101010
- muted text: #555555
- border default: #e0e0e0
- border hover: #999999
- primary action: no distinct CTA color

**Example Component Prompts**
1. Create a mockup tile card: white background, 1px solid #e0e0e0 border, 8px radius. Center a black iPhone silhouette in the top 75% of the tile. Add a 1px #e0e0e0 horizontal divider below the asset. Footer strip: 10px top/bottom padding, 12px left/right padding. Left label 'M 005' in Soehne Mono 11px #555. Right label 'IPHONE' in Soehne Mono 12px uppercase 0.08em tracking #555.

2. Create a section heading: Soehne Mono 26px weight 500, uppercase, #999999, letter-spacing 0.18em (4.68px). Text '3D MOCKUPS'. No underline, left-aligned with 40px top margin and 12px bottom margin.

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

4. Create a loader ring: two concentric SVG arcs. Background arc: stroke #e0e0e0, 4px weight, full 360 . Progress arc: stroke #101010, 4px weight, 270 sweep starting from top. No fill, centered in a 120px container.

5. Create a theme toggle: pill shape at 999px radius, 40px tall, 72px wide, 1px #e0e0e0 border. Inner thumb: 16px circle, positioned 4px from left edge, white fill with 1px #999999 border. On/active state: thumb at right, #101010 fill.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
