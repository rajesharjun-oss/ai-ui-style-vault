# AI Implementation Prompt

Build a mono-inspired interface using this source-derived style bundle.

Reference site: https://mono.frm.fm/en
Theme: light
Category: Other
North star: White-walled gallery grid. A page organized like a museum contact sheet - stark white cells, thin black rules, and type that floats without shadow or ornament.

Use these palette anchors:

- Ink `#292929` for Primary text, heading color, link color, border strokes, surface blocks - the structural dark that replaces shadow everywhere in the system
- Paper `#ffffff` for Page canvas, card surface, input fill, inverse text - the dominant white ground
- Carbon `#000000` for SVG illustration fills and input text - appears in decorative line-art and form value color

Use these typography anchors:

- NH `--font-nh` for Primary type family for body copy, hero text, headings, and interactive labels
- S-Condensed `--font-s-condensed` for Utility face for uppercase labels, nav, tags, captions, and condensed body
- EV `--font-ev` for Special display accent
- S-Works `--font-s-works` for Reserved display heading

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: .
- Card padding: 20px.
- Element gap: 8px.

Build these component patterns where relevant:

- Bordered Cell: Fundamental layout unit - replaces cards/sections with hard-edged grid cells
- Outline Button: Primary interactive - text-style outlined action
- Text Link: In-flow navigation and reference link
- Inverse Text Button: Highlighted action - white text on dark surface
- Underline Input: Single-line form field - brutalist minimal
- Display Headline: Hero and section-defining copy
- Uppercase Label: Section/metadata tag (e.g., ABOUT, services)
- Editorial Caption: Rotated/aspirational taglines wrapped around imagery
- Vertical Sidebar Label: Page-edge rotated text - brand/category markers
- Product Hero Image: Full-bleed product photograph as centerpiece
- Footer Bar: Copyright and utility nav row
- Dark Inverse Cell: Occasional dark surface for contrast

Do:

- Use 2px solid #292929 borders as the primary separator and container system instead of shadows or background fills
- Set all border-radius to 0px - no rounded corners anywhere
- Use NH weight 100-300 at 32-43px for headlines with -0.02em letter-spacing
- Set S-Condensed labels at 12-14px uppercase with +0.1em to +0.2em letter-spacing for all nav, tags, and metadata
- Let the grid go edge-to-edge (no max-width container) - sections butt directly against each other via shared borders
- Use 8px as the base spacing unit, stepping in multiples (8, 12, 20, 43, 45)
- Pair white (#ffffff) surfaces with #292929 ink for all text and borders - never introduce accent color

Avoid:

- Don't add box-shadow, drop-shadow, or any elevation - the system is intentionally flat
- Don't round any corner - cards, buttons, inputs, images all stay 0px
- Don't use bold weights (600+) - the system's voice comes from weight 100/300/400/500
- Don't introduce a brand accent color - the palette is strictly black/white/ink
- Don't use gradients - fills are always flat solids
- Don't use lowercase body text in S-Condensed - that face is always uppercase
- Don't center-align body paragraphs - copy flows left-aligned in editorial register

Source prompt cues:

**Quick Color Reference**
- text: #292929
- background: #ffffff
- border: #292929
- inverse surface: #292929
- decorative fill: #000000
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

1. Create a hero headline cell: white (#ffffff) background, 2px solid #292929 border, 0px radius, 43px top/bottom padding. Text inside: 'made for art lovers' in NH weight 300, 43px, #292929, letter-spacing -0.02em, line-height 1.34. No shadow, no rounded corners.

2. Create an outlined navigation button: transparent background, 1px solid #292929 border, 0px radius, padding 0px 20px. Text: 'PRE-ORDER' in S-Condensed weight 500, 12px, uppercase, #292929, letter-spacing +0.1em. The button sits flush on the grid, not floating above it.

3. Create a bordered product showcase cell: white (#ffffff) background, 2px solid #292929 border, 0px radius, full-width inside a grid. Product image renders inside with 0px radius, no border, no shadow - shown raw on the white ground.

4. Create a vertical sidebar label: S-Condensed weight 300, 12px, uppercase, #292929, letter-spacing +0.2em, rotated 90 on the right edge of the page, 20px from the edge. Content: 'Illustration, Creative Coding, Web Experiments'.

5. Create a footer bar: 2px solid #292929 top border, white background, 12px S-Condensed uppercase content with +0.2em tracking, separated by wide horizontal padding. Content: '(C) FRM Inc. 2026 SHOP CONTACT PRESS CORPORATE'.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
