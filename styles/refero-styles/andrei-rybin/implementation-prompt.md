# AI Implementation Prompt

Build a Andrei Rybin-inspired interface using this source-derived style bundle.

Reference site: https://andreirybin.com
Theme: light
Category: Design
North star: monochrome atelier notebook - a designer's sketchbook where phone screens are pinned like contact sheets on a white wall

Use these palette anchors:

- Paper `#ffffff` for Page background, card surfaces, image holders - the dominant canvas; everything sits on this
- Ink `#000000` for Primary text, link text, icon strokes, thin section dividers - the only mark-making color
- Graphite `#858585` for Secondary text, muted metadata, and softer border lines that recede behind primary ink
- Stone `#8e8e90` for Cool-toned border and divider strokes for borders that need a hairline without competing with Ink

Use these typography anchors:

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- Inter `--font-inter` for Body copy, project captions, and the larger intro paragraphs. Used at a single weight - regularity IS the signature; no bold headlines shout, no light weight whispers.
- system-ui (sans-serif) `--font-system-ui-sans-serif` for Small UI labels, tag text, icon-adjacent microcopy. Appears wherever a single token of body-size type recurs - utility, not statement.
- .SFNSText `--font-sfnstext` for .SFNSText - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1440px.
- Section gap: 120px.
- Card padding: 16px.
- Element gap: 10px.

Build these component patterns where relevant:

- Project Tile Card: Container for a single showcase image (phone mockup) with label and navigation arrow
- Pill Label: Project category tag overlaid on each card
- Arrow Navigation Button: Compact circular control to open a project
- Header Bar: Top-of-page identity, nav, and social link strip
- Intro Block: Two-column intro: contact email on the left, welcome paragraph on the right
- Project Grid: Responsive grid of project tiles filling the rest of the page
- Caption Label: One-line description under each tile describing the project type

Do:

- Keep the entire interface achromatic - Ink on Paper, with Graphite and Stone for soft hierarchy.
- Use 8px radius for project tiles, 16px for icon containers, 40px (or 9999px) for pill labels and circular buttons.
- Set body and caption type at Inter 12px with -0.0170em letter-spacing; reserve 24px Inter for the single intro paragraph.
- Separate header columns with whitespace alone - no vertical rules or dividers between nav items.
- Use 10px element gap inside cards and 120px section gap between page bands.
- Let image weight carry the page; the system should be invisible behind the work.

Avoid:

- Do not introduce any chromatic color - no accent, no brand hue, no semantic state color.
- Do not use multiple font weights - Inter 400 is the only voice; no bold, no light, no italic.
- Do not apply shadows, gradients, or fills to tiles or buttons; borders are the only separator.
- Do not center body text - captions and metadata are left- or context-aligned, not centered except where a tile naturally centers its caption beneath.
- Do not use a border radius below 8px on cards or above 16px on icons - the radii carry the system's softness and must stay consistent.
- Do not add navigation patterns (hamburgers, sidebars, mega-menus); the header is a single text strip.
- Do not break the grid with asymmetric or overlapping tile placements - the grid is the page's structural truth.

Source prompt cues:

Quick Color Reference
- text: #000000 (Ink)
- background: #ffffff (Paper)
- border: #858585 (Graphite) or #8e8e90 (Stone) for soft rules, #000000 (Ink) for structural borders
- muted text: #858585 (Graphite)
- primary action: no distinct CTA color

Example Component Prompts
1. Header strip: white background, full-bleed within 1440px max-width, 16px padding. Four text items in a single row (left/center-left/center-right/right), all Inter 12px weight 400, color #000000, letter-spacing -0.0170em. No dividers between items - whitespace only.
2. Project tile: white background, 8px border-radius, 16px padding. A pill label at top-left: 40px border-radius, 1px solid #000000 border, 6px padding top/bottom and 8px left/right, text Inter 12px #000000. A 32px circular button at top-right: white fill, 1px solid #000000 border, centered right-arrow icon.
3. Intro block: two columns. Left column: Inter 12px #000000 email link. Right column: Inter 24px #858585, line-height 1.23, letter-spacing -0.4px. 40px row gap between rows.
4. Tile caption: Inter 12px #858585, centered, 8px below the tile card.
5. Project grid: 5 equal columns, 16px column gap, each tile showing an image that fills its slot. No borders, no shadows between tiles.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
