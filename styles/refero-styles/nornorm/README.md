# Nornorm

Source: [Refero Style](https://styles.refero.design/style/0769ff4c-f719-4865-98df-de2f44c694a6) 
Reference site: [https://nornorm.com](https://nornorm.com) 
Captured: 2026-07-29 
Refero published: 2026-04-30T03:26:03.895Z 
Refero modified: 2026-06-05T12:46:55.464Z 
Theme: light 
Category: Other

## Style Summary

Explore Nornorm's light Other design system: Canvas White #ffffff, Bone #f1efe9 colors, Lunar typography, and DESIGN.md for AI agents.

North star: Scandinavian showroom, cobalt punctuation - a white-walled furniture gallery where one deep blue stroke cuts through warm bone and ink.

## What To Borrow

- Canvas White `#ffffff` for Page background, card surfaces, button text on cobalt, nav background, image backgrounds
- Bone `#f1efe9` for Warm off-white surface for section bands, feature card panels, and soft contrast zones against pure white
- Ash `#ececec` for Subtle elevated surface and neutral button fill for low-emphasis controls
- Stone `#6a6a6a` for Secondary body text, helper copy, nav muted labels, and dividers - the warm mid-gray that gives body text hierarchy without competing with the brand accent
- Graphite `#333333` for Hairline borders and structural dividers
- Ink `#1f1d1e` for Slightly warm near-black for body and heading text - a softer alternative to pure black that matches the warm bone surface
- Obsidian `#000000` for Primary text, nav text, strong borders, and the ghost button outline - the typographic workhorse
- Cobalt Ink `#1e37a0` for Violet outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color

- Lunar `--font-lunar` for Single-family geometric sans used for everything from 14px nav labels to 112px hero display. The tight universal tracking of -0.03em is the signature - it tightens every size equally, so body text feels editorial and display text feels architectural rather than decorative. Weight 500 carries body emphasis, weight 700 is reserved for numbered list items and UI labels.

## Avoid

- Do not introduce a second chromatic color - the system's authority comes from a single accent against monochrome
- Do not use shadows, glows, or any box-shadow on cards, buttons, or modals - the system is deliberately flat
- Do not use a filled neutral button (gray, black, or bone) as a primary action - the only filled button is Cobalt Ink on white
- Do not break the -0.03em letter-spacing at any size, including body copy and captions - looser tracking reads as a different typeface
- Do not add borders to feature cards, image containers, or section bands - the warm white-to-bone contrast carries separation
- Do not use gradients on backgrounds, buttons, or text - the palette has no gradient tokens and adding one would break the Scandinavian restraint
- Do not round the corners of large photographs, hero images, or gallery images - editorial content stays sharp-edged to contrast with the pill-shaped UI controls

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
