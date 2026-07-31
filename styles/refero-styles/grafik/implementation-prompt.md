# AI Implementation Prompt

Build a Grafik-inspired interface using this source-derived style bundle.

Reference site: https://grafik.co.nz
Theme: light
Category: Agency
North star: Editorial gallery on warm paper. A design annual laid out as a full-bleed screen - typographic grid lines, monochrome photography, and nothing between the work and the page.

Use these palette anchors:

- Bone `#f0eeeb` for Page background and primary canvas - a warm off-white that reads as paper rather than screen, the defining surface of the entire system
- Ink `#000000` for Primary text, body copy, navigation, project metadata, 1px grid lines, image borders, and dark image treatments - the only non-canvas color
- Paper `#ffffff` for Card surfaces, image backgrounds, and reverse-text blocks - white inserts on the warm canvas to isolate portfolio pieces

Use these typography anchors:

- Grotesk `--font-grotesk` for Sole typeface across all UI - navigation, project metadata, and headlines. Used exclusively at weight 400 (no bold, no light), which is anti-convention for an agency portfolio; the regular weight whispers where competitors shout. Negative tracking tightens headlines at -0.02em while body sits at -0.005em, giving every line a printed-page density. The dlig feature enables discretionary ligatures for editorial flourish.

Use these layout rules:

- Base spacing: 8px.
- Density: compact.
- Page max-width: .
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 12px.

Build these component patterns where relevant:

- Hairline Grid Divider: Structural separator between portfolio columns and rows
- Navigation Bar: Site-wide top navigation
- Portfolio Grid Cell: Single project tile within the 3-column portfolio grid
- Project Metadata Block: Caption beneath each portfolio item
- Full-Bleed Image: Oversized project image spanning full viewport width
- Tablet/Device Frame: Portfolio project shown in context (tablet or browser frame)
- Footer: Site footer with contact and legal

Do:

- Use only Grotesk at weight 400 - never introduce bold, semibold, or light variants. The single-weight discipline is the signature.
- Set backgrounds to #f0eeeb for the page canvas and #ffffff for card/image inserts. The warm bone is non-negotiable; pure white as canvas breaks the paper metaphor.
- Separate all portfolio elements with 1px solid #000000 hairlines. Use borders to create the grid, never padding gaps or box-shadows.
- Set border-radius to 0px on every element. No rounded corners on images, cards, buttons, or containers - the design is architecturally sharp.
- Type at three sizes only: 20px for body and metadata, 38px and 40px for headings. The sparse scale forces hierarchy through content, not through type variety.
- Apply negative letter-spacing: -0.02em at 38px, -0.01em at 40px, -0.005em at 20px. This tracking is what makes Grotesk feel like editorial print rather than screen type.
- Keep the interface fully monochromatic. Any color should live inside portfolio content (photography, project artifacts), never in the UI chrome.

Avoid:

- Do not introduce a second typeface. Grotesk carries the entire system - adding a serif or display face fragments the editorial cohesion.
- Do not add box-shadows or any form of elevation. The design uses surface contrast and hairline borders, not depth.
- Do not use rounded corners on any element. Every edge is sharp - cards, images, buttons, tags.
- Do not use bright or saturated colors in the UI. The green and brown tones in screenshots are project content, not system tokens.
- Do not set the page background to pure #ffffff. The warm #f0eeeb canvas is the paper-like foundation - white-as-canvas looks clinical and breaks the design annual metaphor.
- Do not add decorative gradients, patterns, or background textures. The design is flat, monochromatic, and print-faithful.
- Do not use bold or semibold weights. The entire system runs on Grotesk 400 - adding weight breaks the measured, restrained voice.

Source prompt cues:

Quick Color Reference:
- text: #000000
- background: #f0eeeb (canvas) / #ffffff (card)
- border: #000000
- accent: no distinct accent color - system is fully monochromatic
- primary action: no distinct CTA color

Example Component Prompts:

1. Portfolio grid cell: 1px solid #000000 border, 0px radius, background #ffffff or #000000 depending on image. Image fills the cell edge-to-edge with no padding. Three of these cells sit side by side in a 3-column row, separated by 1px #000000 hairlines.

2. Navigation bar: full-width horizontal bar on #f0eeeb background. Left-aligned text 'Grafik, About, Contact.' in Grotesk 400, 20px, #000000, letter-spacing -0.1px. Right-aligned 'Hi' in the same style. No background fill, no border, no logo.

3. Project metadata caption: three lines of Grotesk 400 at 20px, #000000, line-height 1.0. Line 1 is a project number, line 2 is project name and year, line 3 is service categories. Left-aligned, sits on the #f0eeeb canvas ~80px below the image grid.

4. Full-bleed project image: a single image spanning 100vw with 1px solid #000000 border, 0px radius. No overlaid text, no padding, no caption inside the image area. Functions as a full-width section break.

5. Device-framed project: a website or app screenshot displayed inside a rectangular frame with 1px solid #000000 border and #000000 background fill, showing the work in context. No shadow, no radius, no padding between frame and content.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
