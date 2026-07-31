# AI Implementation Prompt

Build a Raad Cycling-inspired interface using this source-derived style bundle.

Reference site: https://www.raad.cc
Theme: light
Category: E-commerce
North star: Ink and ivory gallery runway

Use these palette anchors:

- Ink Black `#000000` for Primary canvas for dark sections, product photography backgrounds, all body text on light surfaces, divider lines, and the dominant border color throughout the system
- Ivory White `#ffffff` for Primary canvas for light sections, text on dark backgrounds, ghost-button fills and borders, the base surface against which all product photography is staged
- Charcoal Edge `#181818` for Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color
- Graphite `#333333` for Secondary border tone for subtle UI structure, divider lines between content blocks, and depth separation on otherwise flat surfaces
- Stone Gray `#666666` for Muted helper text, secondary metadata, and the only step down in the type hierarchy where pure black would feel too heavy - the softest voice in the system

Use these typography anchors:

- Arial `--font-arial` for Fallback system font for micro-text and edge-case rendering - appears so rarely it functions as a safety net rather than a design choice
- Raad Display (custom geometric sans-serif) `--font-raad-display-custom-geometric-sans-serif` for The sole brand typeface used for everything from uppercase product category labels to the massive hero display 'LIQUID LOVE'. The custom face is a clean geometric sans with tall x-height and wide letterforms that hold up at extreme scale. It is used at weight 400 only - no bold, no light variations. The 0.1em positive letter-spacing is applied uniformly across all sizes, creating a slightly aired-out feel even at body text. This single-font, single-weight discipline is the most opinionated choice in the system: Raad removes the typographic hierarchy tools (weight contrast, family contrast) that most sites rely on, forcing scale and letter-spacing to do all the structural work instead.
- wfont_8b8bfe_cd7287b5071a4785a78bba57128a74e2 `--font-wfont8b8bfecd7287b5071a4785a78bba57128a74e2` for wfont_8b8bfe_cd7287b5071a4785a78bba57128a74e2 - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: .
- Section gap: 120px.
- Card padding: 0px.
- Element gap: 20px.

Build these component patterns where relevant:

- Ghost Outline Button: Primary call-to-action across the system
- Minimal Navigation Bar: Top-level site navigation
- Hero Display Banner: Full-viewport editorial header
- Product Category Split Card: Jersey collection entry point (Women's / Men's)
- Editorial Dark Section: Brand story / craft explanation block
- Full-Bleed Product Photograph: Visual showcase of garments and cycling details
- Footer: Site-bottom information block

Do:

- Use only #000000 and #ffffff as the foundation - every section must resolve to one of these two surfaces, creating hard editorial breaks
- Apply 0.1em letter-spacing to every piece of text set in the custom brand face, at every size, without exception
- Render all photography edge-to-edge with zero border-radius, zero padding, zero shadow - let images bleed to the viewport edges
- Use the 100px border-radius exclusively for ghost outline buttons - every interactive element should be a transparent pill with a 1px border
- Set the hero headline at maximum display scale (the 50-54px token, scaled to fill the viewport width) to make typography function as the visual hero instead of imagery
- Maintain 120px vertical padding above and below major sections to create the breathing room of a gallery wall
- Use uppercase for all headings, button labels, and navigation items - sentence case appears nowhere in the system

Avoid:

- Never introduce a chromatic color, gradient, or accent - the system is 0% colorful by design, and any hue would break the gallery aesthetic
- Never use a filled or solid-background button - ghost outlines are the only button pattern permitted
- Never apply box-shadow, drop-shadow, or blur to any element - depth comes from black/white alternation, not elevation
- Never use border-radius on images or cards - the only rounded element is the pill button at 100px
- Never use bold or semibold weights - the custom font exists at weight 400 only, and introducing weight contrast would destroy the system
- Never set body text tighter than 1.4 line-height - the generous leading is what keeps small white-on-black text legible
- Never add decorative UI elements (badges, tags, pills, chips, tooltips) - the system is intentionally stripped to typography, photography, and hairline borders

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
