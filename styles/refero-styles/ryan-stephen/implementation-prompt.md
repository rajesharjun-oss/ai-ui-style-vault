# AI Implementation Prompt

Build a Ryan Stephen-inspired interface using this source-derived style bundle.

Reference site: https://www.ryanstephen.co
Theme: light
Category: Design
North star: Quiet gallery wall on white plaster - the portfolio is the product, the UI is invisible.

Use these palette anchors:

- Ink Black `#000000` for Primary text, image frame borders, structural lines
- Charcoal `#404040` for Secondary body text, subdued labels
- Warm Ash `#8b8b94` for Muted helper text, link borders, link text, decorative dividers
- Plaster White `#ffffff` for Page canvas, card surfaces, image backgrounds

Use these typography anchors:

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- system-ui `--font-system-ui` for All text uses the OS system font stack. 16px weight 500 carries the bio paragraph and link text; 12px weight 400 covers the small link row (Email - Twitter - LinkedIn) and metadata. The deliberate choice of native system fonts - no custom typeface, no webfont load - keeps the chrome weightless and lets the photographs be the only typographic event on the page.

Use these layout rules:

- Base spacing: 4px.
- Density: spacious.
- Page max-width: 1200px.
- Section gap: 100px.
- Card padding: 40px.
- Element gap: 20px.

Build these component patterns where relevant:

- Bio Block: Left-column introduction paragraph
- Social Link Row: Inline list of outbound links
- Image Gallery Grid: 3-column photo grid showing portfolio work
- Gallery Tile: Single photograph in the grid
- Text Link: Inline navigation to email/social profiles

Do:

- Use 10px border-radius for all images and any card-like surface
- Keep the palette restricted to #000000, #404040, #8b8b94, and #ffffff - no accent colors
- Use system-ui at 16px weight 500 for body and 12px weight 400 for meta/link rows
- Set line-height to 1.20 across all text
- Maintain the 3-column image grid with 15-20px gaps and 100px section breathing room
- Let images sit on the white canvas with no frames, shadows, or backgrounds
- Write links as plain text - no buttons, no underlines, no icons

Avoid:

- Don't introduce a brand color or accent - the absence of color is the brand
- Don't add drop shadows, gradients, or elevation effects to any element
- Don't load a custom webfont - system fonts are the system
- Don't use a border-radius other than 10px on images or cards
- Don't wrap the bio or link row in a card, container, or bordered box
- Don't add icons to social links or nav items
- Don't apply different radii to different elements - one value across the system

Source prompt cues:

Quick Color Reference:
- text: #000000
- muted text: #404040
- link/secondary: #8b8b94
- background: #ffffff
- border: #000000
- primary action: no distinct CTA color

Example Component Prompts:

1. Create a bio block: white (#ffffff) canvas, 16px system-ui weight 500, #000000, line-height 1.20. No border, no background, flush-left at page top. Max-width ~360px.

2. Create a social link row: three bare text links (Email, Twitter, LinkedIn) on one line, separated by ~20px space. 12px system-ui weight 400, #000000, no underline, no icons.

3. Create a 3-column image grid: white background, 15-20px row and column gaps, tiles clipped to 10px border-radius. No borders, no shadows, no captions. Tiles stretch to fill column width.

4. Create a single gallery tile: full-width image inside a 10px-radius container, no padding, no frame, no hover state. Aspect ratio follows the source image.

5. Create a plain text link: 16px system-ui weight 500, #000000, no underline, no background, no border. Distinguishable from body text only by context and convention.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
