# Studio Thomas

Source: [Refero Style](https://styles.refero.design/style/f2b24dce-5b1f-47c2-8ef6-bbbd08b68826)
Reference site: [https://studiothomas.co.uk](https://studiothomas.co.uk)
Captured: 2026-07-31
Refero published: 2026-04-30T02:34:34.600Z
Refero modified: 2026-06-05T11:53:33.648Z
Theme: mixed
Category: Agency

## Style Summary

Explore Studio Thomas's mixed Agency design system: Signal Orange #ff4f00, Ink Black #000000 colors, Moderat typography, and DESIGN.md for AI agents.

North star: Alarm-orange broadcast panel on raw linen

## What To Borrow

- Signal Orange `#ff4f00` for Hero blocks, brand statement panels, full-bleed feature sections - the single chromatic commitment, used in large committed areas rather than small accents
- Ink Black `#000000` for Primary text, logo, hairline borders, dark UI elements, and display type on light surfaces
- Paper White `#ffffff` for Display headings overlaid on photography and colored panels, input fields, light surface level, inverse text on dark hero blocks
- Raw Linen `#ebe9e3` for Page canvas, footer background, secondary surface - warm off-white that softens the contrast between stark white and pure black
- Faint Stone `#767676` for Input field borders, low-emphasis form chrome - the only mid-tone in the system

- Moderat `--font-moderat` for Sole typeface - geometric sans-serif used at weight 300 for display and project names (120px) and weight 400 for body copy (16px). The light weight at display scale is a deliberate anti-shout: headlines whisper authority rather than declaring it, letting the orange blocks and editorial photography carry visual volume instead.

## Avoid

- Do not introduce a secondary accent color. The system is monochromatic-plus-orange - adding blue, green, or any other hue dilutes the commitment.
- Do not use border-radius on any element. The system is edgeless - buttons, cards, inputs, and tags are all sharp-cornered (0px radius).
- Do not use bold or black weights (600-900). Moderat is loaded at 300 and 400 only; using heavier weights breaks the restrained voice.
- Do not add drop shadows, glows, or elevation effects. Surfaces are flat - separation comes from color blocks and full-bleed edges, not depth.
- Do not create a filled CTA button. The system has no ACTION_BACKGROUND evidence - interactions are text links and border-bordered text, not filled buttons.
- Do not wrap project photography in cards with borders, backgrounds, or padding. The image IS the container.
- Do not use gradients. The system is entirely flat color - no detected gradient usage anywhere.

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
