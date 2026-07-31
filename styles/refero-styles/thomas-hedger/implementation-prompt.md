# AI Implementation Prompt

Build a Thomas Hedger-inspired interface using this source-derived style bundle.

Reference site: https://thomashedger.co.uk
Theme: light
Category: Design
North star: Silent frame, loud prints

Use these palette anchors:

- Canvas White `#ffffff` for Page background, card surface, text on dark tiles
- Ink Black `#000000` for Primary text, card and image borders, grid hairlines, nav accents
- Carbon Plum `#29242b` for Heading text - a warm near-black that softens against pure Ink Black for editorial moments
- Ash `#e5e5e5` for Subtle divider and muted border tone for low-emphasis separations

Use these typography anchors:

- Diatype `--font-diatype` for Body and small UI text at 19px; copyright/caption at 9px. Diatype is a contemporary neo-grotesque with humanist proportions - paired with the bold Variable cut, it creates a tight, modern-editorial feel without a serif in sight. The 9px caption is intentionally tiny, like a museum wall label.
- Diatype Variable `--font-diatype-variable` for Primary navigation and section headings at 26px. The 500 weight is the default nav voice; 700 is reserved for emphasis and the designer's name. The 26px cap-height next to 19px body text creates a deliberate 7px gap that reads as confident hierarchy without loud type.
- Times `--font-times` for Occasional fallback or inherited editorial copy; not a primary voice. Appears at 13px as a quiet secondary tier.

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: .
- Section gap: .
- Card padding: 3px.
- Element gap: 19px.

Build these component patterns where relevant:

- Top Navigation Bar: Sticky primary header spanning full viewport width
- Portfolio Grid Tile: Single project image cell in the 3-column mosaic
- 3-Column Mosaic Grid: Page-level layout for the portfolio body
- Social Icon Link: Utility icon in the top-right of the nav
- Footer: Minimal page-end credit line
- Nav Text Link: Uppercase navigation label

Do:

- Use the full 3-column edge-to-edge mosaic for all portfolio work - pageMaxWidth is null, the grid bleeds to the viewport.
- Set every corner radius to 0px - no rounded surfaces anywhere in the UI.
- Use Diatype Variable at 26px 500/700 for all navigation and section headings; reserve 700 for the designer's name and active emphasis.
- Use Diatype 400 at 19px for body and 9px for copyright/footer - the 9px caption is a signature scale choice.
- Keep internal tile padding at 3px and inter-tile gaps at 0-3px for a print-flat-file feel.
- Let project images supply all color - never introduce accent or brand color into chrome elements.
- Pair Carbon Plum (#29242b) with Ink Black (#000000) only when you need editorial warmth in headings; otherwise stay in pure Ink Black.

Avoid:

- Do not add shadows, gradients, or border-radius to any component - the design is intentionally flat.
- Do not introduce accent, brand, or semantic colors (no success green, no error red) - the palette is a closed two-tone system.
- Do not use a serif or display font for navigation - Diatype Variable is the only allowed heading voice.
- Do not add hover backgrounds, underlines, or animation to nav links - text alone is the interactive surface.
- Do not wrap the grid in a centered max-width container - the mosaic must reach the viewport edges.
- Do not use type sizes outside the 9/13/19/26 scale - interpolation breaks the editorial rhythm.
- Do not add card surfaces, elevated panels, or modal containers - if it needs a container, the project image should fill it directly.

Source prompt cues:

Quick Color Reference:
- background: #ffffff
- text: #000000
- heading: #29242b
- border: #000000
- muted border: #e5e5e5
- primary action: no distinct CTA color

Example Component Prompts:
1. Build a sticky top navigation: white background, 26px Diatype Variable 500 in #000000. Left: 'THOMAS HEDGER' at weight 700. Center: 'CONTACT' at weight 500. Right: three 26px black SVG icons (Behance, Instagram, cart) flush to the right edge. Zero padding inside the bar, 3px vertical breathing room.
2. Build a 3-column full-bleed mosaic grid: three equal-width columns, no max-width, no inter-column gap. Each cell is a project image at 1px solid #000000 border with 3px internal padding and 0px border-radius. Images can be any aspect ratio - masonry, not uniform grid.
3. Build a footer line: centered single row at 9px Diatype 400 in #000000. Left half: '(C)Thomas Hedger 2026'. Right half: 'Thanks for looking '. No divider above, no background fill, sits directly on canvas white.
4. Build a project tile: full-bleed image, 1px #000000 border, 3px padding, 0px radius. The image is the content - no title, no caption, no overlay.
5. Build an editorial section heading: 'SELECTED WORK' in Diatype Variable 700 at 26px, #29242b, uppercase, left-aligned, 19px top margin above the heading, 0px below it - the grid starts immediately.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
