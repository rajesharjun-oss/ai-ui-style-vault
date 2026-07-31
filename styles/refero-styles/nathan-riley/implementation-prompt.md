# AI Implementation Prompt

Build a Nathan Riley-inspired interface using this source-derived style bundle.

Reference site: https://www.nrly.co
Theme: light
Category: Design
North star: Gallery wall in a black void. A monochrome portfolio where the grid of atmospheric renders is the only color, and a single oversized serif name card anchors the center like a magazine cover floating over the work.

Use these palette anchors:

- Pure Black `#000000` for Text, image grid gutter borders, hairline dividers, nav chip outlines - the structural ink that defines the grid structure and typography
- Paper White `#ffffff` for Page canvas, nav chip backgrounds, card surface - the gallery wall behind everything
- Warm Charcoal `#393939` for Central name card surface, secondary text, soft borders - the mid-tone that makes the pale-rose card read as a distinct layer without breaking the monochrome
- Blush Card `#e8c4c0` for Background of the central name card - the only chromatic accent, a dusty rose that warms the otherwise pure black-and-white system

Use these typography anchors:

- font1 `--font-font1` for font1 - detected in extracted data but not described by AI
- Custom Display Serif `--font-custom-display-serif` for Hero name display and small print. The 238px size with line-height 0.80 and -0.04em tracking creates a tightly cropped masthead that feels printed, not rendered. Weight 300 at display size is the signature - it whispers rather than shouts, giving the name editorial weight through restraint rather than boldness. The italic treatment in the screenshot adds a calligraphic warmth that contrasts the rigid grid around it.
- Custom Body Serif `--font-custom-body-serif` for Body copy, bio description, nav chip text, and link labels. Tight line-height 1.10 at small sizes creates a dense, catalog-like feel. The -0.025em tracking tightens the letterforms for compact, refined small text that reads as label or caption rather than prose.
- font2 `--font-font2` for font2 - detected in extracted data but not described by AI
- ui-sans-serif `--font-ui-sans-serif` for ui-sans-serif - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: .
- Section gap: .
- Card padding: 38px.
- Element gap: 6px.

Build these component patterns where relevant:

- Image Grid Tile: Primary content unit - each cell of the mosaic
- Central Name Card: The artist's identity card anchored over the grid
- Pill Navigation Chip: Social/contact link in the bottom bar
- Profile Link: Secondary text link inside the name card
- Masonry Grid Container: Page-level layout structure
- Image Gutter Divider: Hairline separation between grid cells
- Bio Description Block: Text body inside the central name card

Do:

- Use only the three neutral values plus the single dusty-rose card color - never introduce a new hue, the system is intentionally monochrome
- Set display name text at 238px with line-height 0.80 and -0.04em letter-spacing to reproduce the editorial masthead effect
- Use 9999px radius exclusively for nav pill chips - all other elements stay at 0px radius
- Keep all image tiles edge-to-edge with no padding, no rounded corners, and no shadows - the grid is the layout, not a container
- Anchor the central name card with #e8c4c0 background and 38px padding on all sides as the single non-monochrome surface
- Use custom serif at weight 300-400 for all display text - never substitute a sans-serif headline, the serif is the brand
- Maintain 6px gap between nav chips and 2px between image grid cells to keep spacing tight and structural

Avoid:

- Do not add any new color - no blues, greens, or warm tones beyond the single blush card background
- Do not use border-radius on cards, images, or content containers - only pill nav chips get radius
- Do not apply shadows or elevation effects to any component - the system is flat, relying on color contrast and grid structure for depth
- Do not add gradients of any kind - the palette is solid only
- Do not use sans-serif for headlines or display text - the custom serif at extreme sizes is the signature element
- Do not constrain the image grid with a max-width container - the grid must be full-bleed edge-to-edge
- Do not add header navigation, footers, or sidebar chrome - the floating name card and bottom pill row are the entire navigation system

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #ffffff
- border/gutter: #000000
- accent surface (name card): #e8c4c0
- secondary text: #393939
- primary action: no distinct CTA color

**Example Component Prompts**

1. *Create a full-bleed image mosaic page*: white (#ffffff) canvas. CSS grid filling 100vw x 100vh with 6-8 columns of image tiles, each tile flush edge-to-edge with 2px black (#000000) gaps. No padding, no margins, no border-radius on any tile. Images fill their grid cells completely with object-fit cover.

2. *Create the central floating name card*: 38px padding on all sides, background #e8c4c0 (dusty rose), no border, no shadow, no radius. Name text at 238px custom serif weight 300, italic, #000000, line-height 0.80, letter-spacing -0.04em. Bio paragraph below at 14px custom serif weight 400, #393939, line-height 1.10, -0.025em tracking. Small 'PROFILE >' link at 12px below bio.

3. *Create the bottom nav row*: horizontal flex row with 6px gap between items. Each chip is a pill (9999px border-radius), white (#ffffff) background, no border, 16px horizontal padding, 2px vertical padding. Text inside is 12-14px custom serif weight 400, uppercase, #000000, letter-spacing -0.025em. Chips contain: EMAIL, TW, IG, NFTS.

4. *Create a gallery grid image tile*: one cell of the mosaic, filling its grid area completely. The image is a 3D-rendered atmospheric scene (soft light, surreal natural/architectural composition). No border-radius, no padding, no overlay text, no shadow. The tile's edge is defined only by the 2px black gap to neighboring tiles.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
