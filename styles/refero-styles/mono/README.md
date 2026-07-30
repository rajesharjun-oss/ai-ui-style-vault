# mono

Source: [Refero Style](https://styles.refero.design/style/859f6be7-9d2d-4da6-a9b7-baa658172696)
Reference site: [https://mono.frm.fm/en](https://mono.frm.fm/en)
Captured: 2026-07-30
Refero published: 2026-04-30T02:42:12.427Z
Refero modified: 2026-07-03T11:24:50.681Z
Theme: light
Category: Other

## Style Summary

Explore mono's light Other design system: Ink #292929, Paper #ffffff colors, NH, S-Condensed typography, and DESIGN.md for AI agents.

North star: White-walled gallery grid. A page organized like a museum contact sheet - stark white cells, thin black rules, and type that floats without shadow or ornament.

## What To Borrow

- Ink `#292929` for Primary text, heading color, link color, border strokes, surface blocks - the structural dark that replaces shadow everywhere in the system
- Paper `#ffffff` for Page canvas, card surface, input fill, inverse text - the dominant white ground
- Carbon `#000000` for SVG illustration fills and input text - appears in decorative line-art and form value color

- NH `--font-nh` for Primary type family for body copy, hero text, headings, and interactive labels
- S-Condensed `--font-s-condensed` for Utility face for uppercase labels, nav, tags, captions, and condensed body
- EV `--font-ev` for Special display accent
- S-Works `--font-s-works` for Reserved display heading

## Avoid

- Don't add box-shadow, drop-shadow, or any elevation - the system is intentionally flat
- Don't round any corner - cards, buttons, inputs, images all stay 0px
- Don't use bold weights (600+) - the system's voice comes from weight 100/300/400/500
- Don't introduce a brand accent color - the palette is strictly black/white/ink
- Don't use gradients - fills are always flat solids
- Don't use lowercase body text in S-Condensed - that face is always uppercase
- Don't center-align body paragraphs - copy flows left-aligned in editorial register

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
