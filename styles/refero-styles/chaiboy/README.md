# CHAIBOY

Source: [Refero Style](https://styles.refero.design/style/442dfaf8-c0c6-467b-a8d4-54e953c049f3)
Reference site: [https://wearechaiboy.com](https://wearechaiboy.com)
Captured: 2026-07-31
Refero published: 2026-04-30T02:50:24.215Z
Refero modified: 2026-06-05T11:54:52.070Z
Theme: dark
Category: E-commerce

## Style Summary

Explore CHAIBOY's dark E-commerce design system: Void #000000, Carbon #131313 colors, Neue Haas Grotesk TP 55 Roman typography, and DESIGN.md for AI agents.

North star: black gallery wall with a single illuminated photograph.

## What To Borrow

- Void `#000000` for Page canvas, hero background, footer background - the absolute ground everything else sits on or within
- Carbon `#131313` for Subtle surface variation from the page canvas - used as a near-identical lifted surface where one is needed without breaking the monochrome spell
- Ash `#afafaf` for Secondary text, muted labels, inactive input borders - a half-step between white and black for elements that must recede
- Bone `#ffffff` for Primary text, hairline rules, link and button borders, image borders - the only forward-facing tone, used with restraint as both type and geometry

- Neue Haas Grotesk TP 55 Roman `--font-neue-haas-grotesk-tp-55-roman` for Sole typeface for all interface text - navigation, body, headlines, buttons, footer. The exclusive use of weight 400 is a deliberate anti-hierarchy choice; scale and spacing do the work that weight normally would. The OpenType 'case' feature is enabled site-wide, giving all-caps small text properly designed uppercase parentheses, hyphens, and numerals instead of lowercase glyphs scaled up.

## Avoid

- Do not introduce any chromatic color - no brand accent, no semantic red/green/blue, no hover tint. The system is monochromatic by conviction.
- Do not use font-weight above 400, and do not add italic. Weight contrast is not available as a hierarchy tool.
- Do not use box-shadow, gradients, or glow effects. Surfaces are flat black; depth comes from hairline borders and photography only.
- Do not use border-radius larger than 4px. Pills, fully rounded shapes, and large curves are outside this system.
- Do not use backgrounds or fills on nav links, buttons in the main flow, or cart. The bordered chip is the only filled/bordered interactive shape, and it belongs only in the announcement bar.
- Do not underline links or change their color on hover. Text links are distinguished by position, context, and cursor only.
- Do not set type below 11px or use centered body copy. Small text is always uppercase, tight-leading, left-aligned in rows.

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
