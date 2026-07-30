# Wemakethings

Source: [Refero Style](https://styles.refero.design/style/15d57573-513b-49aa-91c7-1b7f87bb1a55)
Reference site: [https://wemakethings.de](https://wemakethings.de)
Captured: 2026-07-30
Refero published: 2026-04-30T03:36:05.380Z
Refero modified: 2026-06-05T12:21:28.706Z
Theme: light
Category: Agency

## Style Summary

Explore Wemakethings's light Agency design system: Ink Black #000000, Paper White #ffffff colors, Maison Neue, BASEBLOOM typography, and DESIGN.md for AI...

North star: Brutalist editorial broadsheet - ink-on-white architecture with type as the only building material.

## What To Borrow

- Ink Black `#000000` for Primary text, all borders, outline strokes, link underlines, background type fill
- Paper White `#ffffff` for Page canvas, card surface, filled button background

- Maison Neue `--font-maison-neue` for Primary UI and headline typeface - used for nav links, body copy, button text, and bold all-caps hero statements. The 65px weight 500 is the signature headline voice: tight leading (1.11), all-caps, commanding without decorative weight. Substitute: Inter, Helvetica Neue, Neue Haas Grotesk
- BASEBLOOM `--font-basebloom` for Architectural display layer - rendered as massive outlined characters (864px, line-height 0.83) that sit behind body content as visual scaffolding, never carrying readable information. Substitute: a custom ultra-condensed display face or CSS stroke text
- Unzyale `--font-unzyale` for Rare secondary display use - appears in link context at 58px as a typographic accent. Substitute: a condensed or script contrast face

## Avoid

- Never introduce color, gradients, or tinted backgrounds - the system is strictly monochromatic
- Never use border-radius on buttons, cards, inputs, or tags - all corners are sharp at 0px
- Never add drop shadows or box-shadows - depth comes from typographic layering, not elevation
- Never use photographic imagery or illustration - type is the only visual material
- Never use rounded or soft type - all display text is all-caps with tight leading
- Never center body paragraphs - left-align with a constrained reading column
- Never decorate links with fills, pills, or button chrome - links are bare text with optional underline and arrow

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
