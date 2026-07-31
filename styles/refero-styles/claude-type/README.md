# Claude Type

Source: [Refero Style](https://styles.refero.design/style/134cfb76-12e0-4e2e-9995-5a1617190c56)
Reference site: [https://claudetype.com](https://claudetype.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:12:15.644Z
Refero modified: 2026-06-05T11:05:17.716Z
Theme: light
Category: Design

## Style Summary

Explore Claude Type's light Design design system: Parchment Cream #fcfbf7, Pure Linen #ffffff colors, MagicUIPro typography, and DESIGN.md for AI agents.

North star: curated gallery on warm parchment

## What To Borrow

- Parchment Cream `#fcfbf7` for Primary page canvas and hero section background - warm off-white that flatters display serifs the way museum walls flatter paintings
- Pure Linen `#ffffff` for Card surfaces, button fills, icon strokes - the cleanest white sits one step above the cream canvas to separate cards from page
- Warm Linen `#e7e4e0` for Secondary surface and frosted nav background - a muted stone tone that softens the nav bar against the cream canvas
- Ink Black `#0d0d0f` for Primary text and button borders - near-black with a cool undertone, used for all body copy and the outlined button strokes
- Espresso `#2b1b1b` for Secondary text and hairline borders - a warm dark brown that acts as the dominant border color across cards, nav, and dividers
- Carbon `#000000` for SVG fills, logo marks, and icon strokes - pure black for the highest-contrast graphic elements
- Bitter Brown `#100401` for Dark showcase card background - nearly black with warm brown undertone, used for display type specimen cards to make white serifs glow
- Acid Lime `#99ff66` for Accent badge fill for metadata tags - the only chromatic color in the UI, used sparingly to mark type specs, style counts, and new releases

- MagicUIPro `--font-magicuipro` for Sole UI typeface - all navigation, body copy, buttons, labels, and section headings use this family at 11-18px; the custom font includes discretionary ligatures ("dlig") that add character to small text

## Avoid

- Do not add drop shadows, glows, or blur effects to cards or buttons - the system is shadow-free by design
- Do not introduce additional accent colors beyond #99ff66; the 3% colorfulness is intentional
- Do not use border-radius values below 10px for cards or 100px for interactive elements - the pill/arch vocabulary is binary
- Do not set body text above 18px or use MagicUIPro for display headlines; display serifs are product content, not UI
- Do not use pure white (#ffffff) as a page background - always use #fcfbf7 cream as the canvas
- Do not apply bold (600+) or semibold weights to MagicUIPro; the family exists at 400 only and any synthetic bolding breaks the system
- Do not center-align body paragraphs or create dense text blocks; the layout is gallery-sparse with generous line-height (1.6-2.0)

## Bundle Contents

- [DESIGN.md](DESIGN.md): full source-derived implementation reference.
- [implementation-prompt.md](implementation-prompt.md): ready-to-paste prompt for an AI builder.
- [style.json](style.json): structured style metadata and token summary.
- [tokens/colors.md](tokens/colors.md): palette and surface rules.
- [tokens/typography.md](tokens/typography.md): type scale and font rules.
- [tokens/spacing-shape.md](tokens/spacing-shape.md): spacing and radius rules.
- [tokens/components.md](tokens/components.md): component recipes.
- [tokens/guidelines.md](tokens/guidelines.md): do and do-not guidance.
- [tokens/layout-imagery.md](tokens/layout-imagery.md): layout and imagery direction.
- [code/css-variables.css](code/css-variables.css): CSS variable starter.
- [code/tailwind-v4.css](code/tailwind-v4.css): Tailwind v4 token starter.
- [code/design-tokens.json](code/design-tokens.json): portable token JSON.
- [screenshots/README.md](screenshots/README.md): source media references.
