# AI Implementation Prompt

Build a Haus Otto-inspired interface using this source-derived style bundle.

Reference site: https://hausotto.com
Theme: light
Category: Agency
North star: Monumental wordmark on white void

Use these palette anchors:

- Obsidian `#000000` for Primary text, wordmark fills, link text, all heading color - the only non-white pigment in the interface
- Paper `#ffffff` for Page canvas, card surfaces, inverse text on dark moments
- Terracotta `#af7653` for Sole chromatic accent - warm earthen tone for hover states, active indicators, or single-element highlights against the monochrome field

Use these typography anchors:

- Monument `--font-monument` for Sole typeface across the entire system. Regular variant at 13-23px for nav links, metadata, body micro-copy. Medium variant at 216px for the hero wordmark - the only element that earns the 216px scale, with -0.033em tracking to tighten the ultra-condensed letterforms into a continuous bar of black

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: .
- Section gap: 30px.
- Card padding: 12-20px.
- Element gap: 4px.

Build these component patterns where relevant:

- Display Wordmark: Hero brand identifier - the signature element
- Navigation Link: Top-level nav items (e.g. 'Info')
- Top-Left Brand Mark: Persistent brand identifier in nav
- Page Dot Indicators: Section navigation (right edge, top)
- Cookie Consent Bar: Legal/UX footer notice
- Page Section Spacer: Vertical rhythm device between content blocks
- Tertiary Body Text: Supplementary information, metadata, descriptions

Do:

- Set hero type at exactly 216px Monument Medium with letter-spacing -0.033em - this scale is non-negotiable, it IS the brand
- Use zero border-radius on every interactive element: buttons, tags, inputs, cards - sharp corners only
- Keep the color palette to Obsidian (#000000) and Paper (#ffffff) as the default; reserve Terracotta (#af7653) for single-element accent moments only
- Set base spacing to a 4px grid with 30px section gaps - the design is compact in its tokens but vast in its whitespace
- Let the wordmark fill the full viewport width - no max-width container should clip the display type
- Use 13px Monument Regular for all navigation and metadata at line-height 1.77-2.00 for breathing room at small sizes
- Treat the white canvas as an active design element - never fill backgrounds with color or imagery behind text

Avoid:

- Never introduce a second typeface family - Monument is the sole voice
- Never apply border-radius to buttons, cards, or tags - every corner is sharp
- Never use shadows, gradients, or glow effects - the design is flat and chromatically minimal
- Never add borders, dividers, or rules between sections - whitespace is the only separator
- Never reduce the 216px display below 120px - the wordmark's authority depends on its scale
- Never use more than one accent color per screen - Terracotta appears as punctuation, not decoration
- Never fill the page with imagery, illustrations, or product photography - text on void is the entire visual system

Source prompt cues:

**Quick Color Reference**
- text/wordmark: #000000 (Obsidian)
- background: #ffffff (Paper)
- border: none (use whitespace, not lines)
- accent: #af7653 (Terracotta - single-element highlights only)
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

1. **Hero Display Wordmark**: Full-viewport Paper (#ffffff) background. Single text element at 216px, Monument Medium weight 400, color Obsidian (#000000), letter-spacing -0.033em, line-height 1.0. Text fills 100% of viewport width edge-to-edge. No subtitle, no tagline.

2. **Navigation Bar**: Top edge of viewport, 4px vertical padding. Left: 'Haus Otto' at 13px Monument Regular Obsidian. Center-left: nav link 'Info' at 13px Monument Regular Obsidian with 20px right margin. Right: two 8px circular dots stacked vertically - top dot Obsidian (active), bottom dot Terracotta #af7653 (inactive). No background, no border.

3. **Body Text Block**: Paper background. 20px Monument Regular Obsidian, line-height 1.23. No max-width constraint. 30px top margin from preceding element. Single paragraph only - no bullet points, no subheadings.

4. **Bottom Consent Bar**: Full-width fixed bar at viewport bottom, Paper background, 30px top/bottom padding. Left: 13px Monument Regular Obsidian consent text. Right group: 'Yes' button (Obsidian fill, Paper text, 4px 8px padding, 0px radius), 'No' text link (Obsidian, no background), 'More' text link (Obsidian, no background), separated by 20px right margins.

5. **Section Divider (Invisible)**: No visible element. Simply 30px of vertical whitespace between the bottom of one content block and the top of the next. The absence of a line IS the divider.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
