# DNCO

Source: [Refero Style](https://styles.refero.design/style/c072c00a-ee7f-4160-bd06-645cca12f7a8)
Reference site: [https://dnco.com](https://dnco.com)
Captured: 2026-07-31
Refero published: 2026-04-30T01:36:06.076Z
Refero modified: 2026-06-05T11:26:28.349Z
Theme: light
Category: Agency

## Style Summary

Explore DNCO's light Agency design system: Canvas White #ffffff, Hairline Mist #e5e7eb colors, Neue Haas Unica Pro typography, and DESIGN.md for AI agents.

North star: editorial gallery on white linen.

## What To Borrow

- Canvas White `#ffffff` for Page background, primary surface for content blocks, card bases
- Hairline Mist `#e5e7eb` for Hairline borders, dividers, subtle surface wash, filter chip backgrounds, image placeholder fill
- Obsidian `#000000` for Primary text, brand wordmark fill, dark hero background, link text, heading color
- Ash `#a3a3a3` for Muted secondary text, captions, inactive filter labels, helper text

- Neue Haas Unica Pro `--font-neue-haas-unica-pro` for Sole typeface for all UI - navigation, body, headlines, and brand wordmark. Weight 400 only, no bold or light variants; hierarchy is built purely through size and tracking rather than weight contrast.

## Avoid

- Do not add a second typeface family - the system is monotypographic by design
- Do not introduce any color other than the four neutrals - no brand red, blue, or accent green
- Do not use box-shadows or elevation on any component - depth comes from whitespace, not blur
- Do not add border-radius to cards or images - only navigation and chips use 9999px
- Do not bold or italicize text to create emphasis - increase size instead
- Do not place content inside bordered containers or filled panels - use whitespace to group
- Do not use background colors for buttons, tags, or interactive states - use text color and the dot indicator

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
