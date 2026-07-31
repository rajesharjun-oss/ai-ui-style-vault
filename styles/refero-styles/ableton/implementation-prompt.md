# AI Implementation Prompt

Build a Ableton-inspired interface using this source-derived style bundle.

Reference site: https://ableton.com
Theme: light
Category: Productivity
North star: Editorial workshop on stark white. White paper, black Futura, one blue pen mark for interactivity, photography clipped flush to the edges like magazine spreads.

Use these palette anchors:

- Ink `#000000` for Primary text, nav labels, logo, icon strokes, and every text-level heading - sets the full information hierarchy
- Paper `#ffffff` for Page canvas, card surface, and hero overlay text - the default background for almost every screen
- Fog `#eeeeee` for Subtle form inputs, tag surfaces, and quiet secondary panel backgrounds - barely-there neutral
- Signal Blue `#0000ff` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Coral `#ff8389` for Category tag fills (Downloads, News) - flat rectangular badges that classify content without padding the layout
- Teal `#00d2be` for Category tag fills (Tutorials, Videos) - flat rectangular badges paired with coral to split content taxonomy visually

Use these typography anchors:

- futura-pt `--font-futura-pt` for The single typeface powering everything from body copy to 90px display headlines. Futura PT's geometric precision mirrors Ableton's grid-based music software - the type and the product share a visual logic. Weight 700 carries headlines, 400 carries body. No serif, no monospace secondary face - the system stays mono-typographic.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 0px.
- Element gap: 10px.

Build these component patterns where relevant:

- Top Navigation Bar: Primary site navigation
- Full-Bleed Hero with Photo Scrim: Above-the-fold announcement
- Section Header with Filter Bar: Content section introduction
- Content Card (Grid Item): Blog post or video entry in 3-column grid
- Category Tag: Content classification badge
- Inline Text Link: Default clickable text
- Overlay Text Link (on dark scrim): Link variant on photographic backgrounds
- Filter Link (Section): Content category filter
- Image Thumbnail (Tutorial Card): Visual entry into video content
- Logo Glyph: Brand mark in navigation
- Horizontal Section Divider: Implicit separation between content zones

Do:

- Use Futura PT for all text - never introduce a secondary typeface
- Set every border-radius to 0px - the system is sharp, angular, and grid-faithful
- Use #0000ff exclusively for link text, active nav, and interactive text - no other blue
- Reach for coral #ff8389 and teal #00d2be only as category tag fills, never as backgrounds or text colors
- Let the page be flat: no shadows, no borders, no fills on cards - let whitespace and type do the work
- Use 90px weight 400 white for hero overlay text, not weight 700 - the light weight on bold imagery is the signature
- Set body line-height to 1.50 and display line-height to 1.00 - the contrast between breathing body and tight display is intentional

Avoid:

- Do not add box-shadows or elevation to any component - the system is deliberately flat
- Do not round corners on cards, tags, buttons, or inputs - keep 0px everywhere
- Do not use coral or teal for buttons, CTAs, or interactive text - they are taxonomy-only
- Do not call #0000ff a 'CTA color' - it is a link color used for interactive text, not filled buttons
- Do not introduce gradient backgrounds - the system is solid color and photography only
- Do not add icons, illustrations, or decorative graphics - photography and type carry the visual load
- Do not set body text below 14px or use a weight other than 400 for body copy

Source prompt cues:

Quick Color Reference:
- text: #000000
- background: #ffffff
- border: none (0px everywhere)
- link/interactive text: #0000ff
- tag fill A: #ff8389 (coral)
- tag fill B: #00d2be (teal)
- primary action: no distinct CTA color

Example Component Prompts:

1. Create a full-bleed hero: a photograph (musician at studio desk) fills the entire viewport width, with a dark semi-transparent scrim overlay. Headline at 90px futura-pt weight 400 white, line-height 1.00, positioned at left ~8% from edge, sits on the scrim. A white inline link 'Learn more >' at 14px weight 400 sits directly below the headline, 0px border-radius, no background, no underline.

2. Create a content section: white #ffffff background, max-width 1200px centered, 80px vertical padding above and below. Section heading at 30px futura-pt weight 400 #000000, left-aligned. To the right on the same baseline, filter links at 14px #0000ff separated by 16px gaps.

3. Create a 3-column card grid: three cards per row, 20px horizontal gap, 40px vertical gap. Each card has 0px border-radius, 0px border, no shadow, no background fill. Top of card: full-width 16:10 photograph (contained, sharp edges). Below: a flat tag rectangle (0px radius, #ff8389 or #00d2be fill, 2px 8px padding, #000000 text at 12px). Below tag: title at 20px weight 400 #000000.

4. Create a top navigation bar: white background, 48px height, full width. Left: Ableton glyph icon (vertical black bars) at 24px height. Beside it: product names (Live, Push, Move, Note, Link, Shop, Packs, Help, More +) in 14px futura-pt weight 400 #000000, 20px gap between items. Right-aligned: 'Try Live 12 for free' in 14px #0000ff, then 16px gap, then 'Log in or register' in 14px #0000ff. No borders, no fills, no hover backgrounds.

5. Create a category tag: 0px border-radius rectangle, 2px vertical padding, 8px horizontal padding, fill #ff8389 (or #00d2be for the second category), text at 12px futura-pt weight 400 #000000. No border, no shadow, no hover state.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
