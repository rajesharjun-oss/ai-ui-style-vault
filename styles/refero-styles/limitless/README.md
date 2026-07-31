# Limitless

Source: [Refero Style](https://styles.refero.design/style/626ae2de-c402-4805-b859-2c6adca41022)
Reference site: [https://limitless.ai](https://limitless.ai)
Captured: 2026-07-31
Refero published: 2026-01-14T13:08:23.000Z
Refero modified: 2026-06-05T08:58:24.158Z
Theme: light
Category: AI

## Style Summary

Explore Limitless's light AI design system: Plaster #f2f3f5, Mist #e5e7eb colors, Greycliff typography, and DESIGN.md for AI agents.

North star: monochrome editorial on plaster white. A single weight-contrast typeface, no accent color, and one violet spark - the system achieves identity through restraint, not decoration.

## What To Borrow

- Plaster `#f2f3f5` for Page background, full-bleed canvas
- Mist `#e5e7eb` for Card surfaces, placeholder image wells, subtle inset zones
- Chalk `#ffffff` for Elevated card surfaces when differentiation from Plaster is needed
- Hairline `#d1d5db` for Stronger dividers, disabled icon strokes, secondary borders
- Inkstone `#0f172a` for Primary heading text, high-emphasis body copy, nav logo wordmark
- Slate `#334155` for Secondary headings, medium-emphasis text, icon strokes
- Graphite `#475569` for Body text, nav links, button labels - the everyday workhorse neutral
- Pewter `#64748b` for Muted helper text, secondary links, metadata
- Fog `#939eae` for Disabled state text, tertiary captions, low-emphasis labels
- Obsidian `#000000` for Maximum-contrast text where #0f172a still feels too soft (rare)
- Spark Violet `#6d4aff` for Wordmark icon and the sole chromatic accent in the entire system - used at the smallest possible size to mark the brand without coloring the interface

- Greycliff `--font-greycliff` for Single-family system. Weight 300 carries display (60px) and large headings (36px) for a quiet, editorial whisper. Weight 400-500 handles body (16-18px) and UI labels. Weight 600-700 reserved for emphasis and the wordmark. Because there is no secondary face, the system creates rhythm purely through weight and size contrast inside one typeface.

## Avoid

- Do not introduce a second typeface - the system is single-family by design
- Do not use weight 700 on headings; weight 300 is the display treatment and weight 500-600 is the UI treatment
- Do not use a chromatic color as a button background, link color, or badge fill - the interface is intentionally colorless
- Do not add borders to cards that sit on #f2f3f5; let the white-on-plaster contrast do the work
- Do not center display headings - they are always left-aligned with the content column
- Do not use sharp corners (0-4px radius) on any surface - the system reads rounded or pill, never squared
- Do not stack multiple shadow layers or add glow effects - one shadow, used once, is the rule

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
