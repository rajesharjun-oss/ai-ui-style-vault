# A24

Source: [Refero Style](https://styles.refero.design/style/6afa22a6-bec8-47c3-b5ee-5d11d64902cb)
Reference site: [https://a24films.com](https://a24films.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:40:24.980Z
Refero modified: 2026-06-05T08:44:00.618Z
Theme: mixed
Category: Media

## Style Summary

Explore A24's mixed Media design system: Obsidian #000000, Paper White #ffffff colors, NB International Web, NB International Mono Web typography, and...

North star: opening title sequence on pure black

## What To Borrow

- Obsidian `#000000` for Section backgrounds for dark bands, primary body text on light surfaces, hairline borders and dividers throughout - the structural backbone of every page
- Paper White `#ffffff` for Light section backgrounds, card surfaces, product image containers, modal/overlay panels, primary text on dark backgrounds
- Ash Gray `#eeeeee` for Subtle surface variant for product showcase panels and soft background shifts on light sections
- Smoke `#888888` for Muted secondary text, subdued nav labels, low-emphasis borders - sits just above AA contrast for accessibility
- Bone `#cacaca` for Light hairline borders on white surfaces, minimal separator lines, very low-emphasis UI strokes

- NB International Web `--font-nb-international-web` for Primary typeface for all UI - navigation, body copy, headings, and display film titles. Weight 400 carries body and most UI; weight 500 for emphasis. The 74px display size with tight tracking (-0.04em) and 0.92 line-height lets film titles stack in dense, almost poster-like blocks. The humanist proportions and slight warmth make it readable at 11px yet commanding at 74px - the same family spans the entire voice.
- NB International Mono Web `--font-nb-international-mono-web` for Monospaced companion for technical labels, year markers beside film titles, and code-like annotations. Used sparingly as a typographic accent that signals data/specification context.

## Avoid

- Do not introduce any color, gradient, or chromatic accent - the palette is strictly achromatic
- Do not use border-radius on any element, including images and product cards
- Do not apply box-shadow, drop-shadow, or any elevation effect - depth comes from value contrast alone
- Do not center-align body copy or film titles - everything reads left-aligned
- Do not use font-weight above 500 - NB International's range is restrained on purpose
- Do not add decorative elements, dividers, or ornamental graphics between content blocks
- Do not use a second typeface family beyond NB International Mono - the mono variant is the only permitted departure

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
