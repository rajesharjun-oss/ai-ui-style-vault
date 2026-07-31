# Josephmark

Source: [Refero Style](https://styles.refero.design/style/58c0af12-8706-428f-8282-482d57d7b90e)
Reference site: [https://josephmark.studio](https://josephmark.studio)
Captured: 2026-07-31
Refero published: 2026-04-30T02:03:46.899Z
Refero modified: 2026-06-05T11:55:34.730Z
Theme: dark
Category: Agency

## Style Summary

Explore Josephmark's dark Agency design system: Carbon Black #000000, Pure White #ffffff colors, Scto Grotesk A typography, and DESIGN.md for AI agents.

North star: Midnight editorial gallery. Monochrome walls, warm spotlights, oversized grotesque typography floating in negative space.

## What To Borrow

- Carbon Black `#000000` for Primary dark canvas - hero backgrounds, full-bleed section stages, base for the editorial atmosphere
- Pure White `#ffffff` for Inverse text on dark canvases, form field backgrounds, button text on filled dark elements
- Stone Taupe `#a9a498` for The system's sole warm chromatic note - muted link states, secondary surface tints, paper-like card backgrounds that soften the black-to-gray transitions
- Bone Cream `#f4f5ef` for Warm off-white surface - secondary card and panel backgrounds, breaks the clinical feel of pure white and echoes the studio's paper-based brand collateral
- Mist Gray `#e5e7eb` for Hairline borders, dividers, list separators, subtle structural lines - the 999-occurrence border color that defines spatial relationships without visual weight
- Graphite `#666666` for Mid-tone text - secondary headings, supporting copy, metadata that needs presence without competing with primary type
- Forest Ink `#4e5449` for Body text on light surfaces - a desaturated dark olive that reads warmer than pure black, the only hue-leaning neutral in the system

- Scto Grotesk A `--font-scto-grotesk-a` for The sole typeface - a custom neo-grotesque used for everything from 70px display headlines down to 12px captions. Weight 300 carries display and large headings (a deliberate anti-convention choice - most agency sites use bold for impact; Josephmark whispers with light). Weight 400 for body, 500 reserved for emphasis and interactive elements. The consistent aggressive negative tracking (-0.019em to -0.035em) tightens the grotesque's natural apertures, creating a compressed, editorial density even at body sizes.

## Avoid

- Do not introduce color beyond the single warm taupe (#a9a498) - the system's power comes from its 1% colorfulness
- Do not add shadows, glows, or any drop effects - this system is rigorously flat
- Do not use rounded corners on cards, images, or containers - only buttons are rounded (to 9999px)
- Do not center text - everything is left-aligned, following editorial column logic
- Do not use bold weights (600+) for emphasis - the scale goes 300 400 500, and contrast comes from size and color, not weight
- Do not add icon systems or decorative graphics - typography and photography are the only visual elements
- Do not use #ffffff as a section background - it appears only as surface within forms and as text color on dark

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
