# Microsoft

Source: [Refero Style](https://styles.refero.design/style/c70a9990-bc4b-4a64-a69b-aeb7b344fb74)
Reference site: [https://www.microsoft.com](https://www.microsoft.com)
Captured: 2026-07-30
Refero published: 2026-04-29T00:44:50.581Z
Refero modified: 2026-06-05T13:02:03.776Z
Theme: light
Category: Other

## Style Summary

Explore Microsoft's light Other design system: Microsoft Blue #0067b8, Pure White #ffffff colors, Segoe UI typography, and DESIGN.md for AI agents.

North star: Corporate blue retail catalog - think 4-square logo against a white showroom floor with one accent blue guiding every interaction.

## What To Borrow

- Microsoft Blue `#0067b8` for Primary action background, link text, navigation accents, icon strokes - the single chromatic authority in the system, used for all filled CTAs and interactive highlights
- Pure White `#ffffff` for Page background, card surfaces, button text on blue, surface elevation
- Mist Gray `#f2f2f2` for Footer background, subtle surface tone, page canvas under cards
- Carbon Black `#000000` for Primary text, card borders, hairline dividers - the dominant typographic and structural color
- Steel Gray `#616161` for Secondary text, navigation text, muted UI elements, footer copy
- Graphite `#262626` for Body text variant, list borders, navigation dividers, secondary headings
- Deep Charcoal `#171717` for Dense text blocks, list separators, button border variant - the darkest neutral after pure black

- Segoe UI `--font-segoe-ui` for Sole typeface across the entire system - navigation, body, headings, buttons, footer. Weight 400 is the workhorse; weight 600 is reserved for headings and button labels to create section-level contrast without switching families. Segoe UI's humanist proportions and open apertures give the system its calm, enterprise-confident voice - the type does not perform, it informs.

## Avoid

- Do not introduce additional brand colors - the system is monochrome plus #0067b8
- Do not use border-radius greater than 2px on buttons, inputs, or cards - keep edges nearly sharp
- Do not apply shadows to navigation bars, buttons, or text blocks - only to product cards
- Do not use Segoe UI weights other than 400 and 600 - no 300 whisper-weights or 700 bold declarations
- Do not create outlined or ghost button variants - all actions are filled blue or simple text links
- Do not add decorative gradients - the system relies on photography and flat surfaces
- Do not use fully saturated icons - category icons should be 1.5-2px stroke outline style in #616161 or #000000

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
