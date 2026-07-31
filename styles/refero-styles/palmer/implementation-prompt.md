# AI Implementation Prompt

Build a Palmer-inspired interface using this source-derived style bundle.

Reference site: https://www.palmer-dinnerware.com
Theme: light
Category: E-commerce
North star: Ceramic gallery in soft daylight - the interface is the wall, the objects are the art.

Use these palette anchors:

- Gallery Cream `#f5f6ee` for Page canvas and base surface - a warm off-white that flatters glazed ceramics more than pure white would
- Ink `#222222` for Primary text, hairline borders, card outlines, icon strokes - the entire structural skeleton runs through this one near-black
- Bone `#ffffff` for Product image backgrounds, occasional inverse surface when a card needs to sit forward of the cream canvas
- Fog `#a1a19c` for Muted secondary borders and low-priority text - used when Ink would be too heavy for a structural divider
- Lampblack `#000000` for Reserved for the rare filled element (active nav background, weight anchors) - used sparingly so Ink remains the default voice

Use these typography anchors:

- TWK Lausanne `--font-twk-lausanne` for Sole typeface - handles everything from micro-labels to 120px editorial display. Weight 300 carries display and large headings (whisper-thin Swiss grotesque that lets the ceramics dominate), weight 400-500 for body and UI, weight 600-700 reserved for active states and filter labels. The tight letter-spacing (-0.04em at display, -0.02em at body) is signature: characters nestle together, giving even 11px labels a compressed, considered feel rather than airy defaults.

Use these layout rules:

- Base spacing: 6px.
- Density: comfortable.
- Page max-width: .
- Section gap: 80px.
- Card padding: 16px.
- Element gap: 12px.

Build these component patterns where relevant:

- Experience View Toggle: Primary mode switcher floating top-center
- Scattered Product Tile: Individual ceramic piece in the main editorial canvas
- Bottom Control Bar: Fixed footer with menu and filter toggles
- Navigation Link: Text link in top-left brand mark and ancillary nav
- Zoom Control: Circular zoom in/out buttons
- Filter Chip: Category or attribute filter in menu mode
- Card Surface: Product card used in grid/list views (non-scattered mode)
- Input Field: Text input for search or filter

Do:

- Use #f5f6ee for every page background - never pure white, it flatters the ceramics and signals the editorial tone
- Set all borders to 1px solid #222222 - hairlines are the only structural separator in the system
- Reach 120px for editorial display headlines in weight 300 with -0.04em tracking - the extreme scale is part of the brand voice
- Use 100px border-radius only for pills (toggles, filter chips, zoom buttons) and 9px for cards, 3px for everything else
- Set type at weight 300-400 for display and large headings; reserve 600-700 for active/selected states only
- Keep interactive elements at the viewport edges (top-center toggle, bottom-center control bar) so the center stays open for product imagery
- Use letter-spacing -0.02em on all body sizes (11-16px) and tighten further as type scales up

Avoid:

- Don't introduce any chromatic accent color - the ceramics supply all the color, the UI stays grayscale
- Don't add drop shadows to cards, buttons, or nav - borders alone define depth
- Don't use corner radius above 100px or below 3px - the three tiers (3px, 9px, 100px) are the complete system
- Don't set type at weight 600+ in display sizes - it would overwhelm the whisper-thin signature of the 120px tier
- Don't use pure black (#000000) for text - Ink (#222222) is the text color; black is reserved for filled active states
- Don't add background color to the main canvas behind product photography - flat cream is non-negotiable
- Don't use letter-spacing 0 or positive values - all text tracks negative

Source prompt cues:

**Quick Color Reference**
- text: #222222
- background: #f5f6ee
- border: #222222 (1px)
- muted: #a1a19c
- active fill: #000000
- primary action: no distinct CTA color

**Example Component Prompts**

1. **Create a scattered product hero:** Full-bleed #f5f6ee canvas. Place 8-10 circular ceramic plate images at irregular positions across the viewport (no grid, no alignment). Each image ~120-200px wide, no border, no background, slight drop shadow baked into the photo only. No headline, no subtext - the products are the entire viewport.

2. **Create the experience view toggle:** Top-center of viewport, pill shape (100px radius), 1px solid #222222 border, no fill. Inside: small dot-grid icon (3x3 dots, #222222) + 'experience view' label at 12px TWK Lausanne weight 400, #222222, letter-spacing -0.02em. Horizontal padding 15px, vertical 7px.

3. **Create the bottom control bar:** Fixed to viewport bottom-center. Two adjacent ghost buttons with 3px radius, 1px #222222 border, cream fill. Left: hamburger icon (3 horizontal lines, #222222) + 'menu' label at 12px weight 500. Right: list icon (3 dots with lines) + 'filter' label at 12px weight 500. Gap between them: 4px.

4. **Create a product card (grid mode):** 9px corner radius, 1px solid #222222 border, #f5f6ee fill, 16px padding. Product image fills width, edge-to-edge inside the radius. Below image: product name at 14px weight 400, #222222, letter-spacing -0.02em. Price at 12px weight 400, #a1a19c. No shadow.

5. **Create a zoom control:** Bottom-right of viewport. Two stacked circular buttons, 24px diameter, 100px radius, 1px #222222 border, #f5f6ee fill. Top circle: '+' glyph at 12px #222222. Bottom circle: '-' glyph at 12px #222222. 4px vertical gap between them.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
