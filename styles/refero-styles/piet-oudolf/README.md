# Piet Oudolf

Source: [Refero Style](https://styles.refero.design/style/3cc1d30c-3b08-48af-bbf0-df195d77835f)
Reference site: [https://oudolf.com](https://oudolf.com)
Captured: 2026-07-30
Refero published: 2026-04-30T02:45:27.355Z
Refero modified: 2026-06-05T12:34:07.761Z
Theme: light
Category: Agency

## Style Summary

Explore Piet Oudolf's light Agency design system: Field White #ffffff, Charcoal Black #000000 colors, Maison Neue Book, UniversLTStd-Light typography, and...

North star: Botanical index on white paper.

## What To Borrow

- Field White `#ffffff` for Page canvas, text on dark inverted sections, and link underline anchor for body copy
- Charcoal Black `#000000` for SVG icon fills and absolute typographic black where maximum contrast is needed (headings against light imagery)
- Lead Gray `#808080` for Primary type, all link and border lines, and the connective tissue of the system - every hairline rule, navigation separator, and body character sits here
- Ash Gray `#b3b3b3` for Navigation labels, muted metadata, footer text, and the secondary tonal floor that recedes behind lead-gray working type
- Smoke `#999999` for Subtle border accent used sparingly to separate tertiary structural elements

- Maison Neue Book `--font-maison-neue-book` for Signature display face for project titles and section headings - 60px at weight 300 is the defining choice, letting each garden name whisper across the page rather than announce
- UniversLTStd-Light `--font-universltstd-light` for Workhorse sans for navigation, country-code labels, body, footer, and all meta information - 12px handles the tiny geo tags above project names, 15px carries paragraph body at generous 1.87 leading for editorial breathing room

## Avoid

- Never introduce a brand color, accent, or fill of any kind - the monochromatic palette is the identity
- Never set a project title below 48px or above 64px - the 60px headline scale is a fixed point of the system
- Never add shadows, gradients, glows, or any form of z-axis depth to cards, buttons, or containers
- Never round corners - all radii are 0px; the system is deliberately rectilinear like a printed page
- Never bold body or heading type - weight 300 is the ceiling for display, weight 400 for everything else
- Never place more than 6px between an inline link and its sibling, or more than 3px between text and its underline
- Never use a filled button, pill, or chip - interaction is expressed only through typographic underlines

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
