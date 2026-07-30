# Waka Waka

Source: [Refero Style](https://styles.refero.design/style/ea55601d-e953-48b3-99db-374b39bf2f56)
Reference site: [https://wakawaka.world](https://wakawaka.world)
Captured: 2026-07-30
Refero published: 2026-04-30T00:35:19.346Z
Refero modified: 2026-06-05T12:42:43.891Z
Theme: light
Category: Design

## Style Summary

Explore Waka Waka's light Design design system: Bone Paper #edeae4, Stone Gray #c9c7c4 colors, Waka Sans typography, and DESIGN.md for AI agents.

North star: museum poster in bone and ink - monumental black grotesk type printed on warm off-white paper, everything else recedes

## What To Borrow

- Bone Paper `#edeae4` for Page background, all canvas surfaces - warm off-white that reads as unbleached paper rather than digital white
- Stone Gray `#c9c7c4` for Secondary surface and muted contextual neutral - appears in contrast pairings as a slightly deeper layer below the canvas
- Ink Black `#28282a` for Primary text, all borders, hairline rules, icon strokes, and the only chromatic anchor in the system - near-black with a hint of warmth so it sits comfortably on the bone background instead of vibrating

- Waka Sans `--font-waka-sans` for Single custom grotesk used for everything from 10px captions to 560px display - tight tracking scales with size (-0.09em at display, -0.02em at body) so the enormous type locks into a dense block while body text stays readable. The 0.80-0.83 line-height at display size is the signature: letterforms stack into an almost solid mass of ink

## Avoid

- Do not introduce any chromatic color, gradient, or accent hue - the system is strictly two-tone
- Do not use filled buttons, colored backgrounds, or background-fill hover states on interactive elements
- Do not apply border-radius greater than 0px to any element
- Do not use box-shadow or any elevation effect - surfaces are flat
- Do not set type below 10px or above 560px - the scale is deliberate and extreme
- Do not use light line-heights (1.5+) on display or heading sizes - 0.80-1.00 is required to maintain density
- Do not separate sections with colored bands or background fills - use whitespace and hairline rules only

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
