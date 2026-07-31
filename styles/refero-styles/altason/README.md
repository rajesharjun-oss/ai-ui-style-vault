# Altason

Source: [Refero Style](https://styles.refero.design/style/e99ae628-89df-4de9-ab80-9885b1be4dc0)
Reference site: [https://atlason.com](https://atlason.com)
Captured: 2026-07-31
Refero published: 2026-04-30T01:31:53.571Z
Refero modified: 2026-06-05T11:31:07.050Z
Theme: light
Category: Agency

## Style Summary

Explore Altason's light Agency design system: Ink Black #000000, Paper White #ffffff colors, Haas Grotesk DS Pro, Haas Grotesk TX Pro typography, and...

North star: architectural monochrome broadsheet

## What To Borrow

- Ink Black `#000000` for Primary text, hairline borders, structural rules, image borders, heading fills - the dominant ink that draws the entire page
- Paper White `#ffffff` for Page canvas, card surfaces, reverse text on dark blocks - the surface that lets the black type speak
- Charcoal Plate `#212121` for Dark surface blocks and image backgrounds where white reverse type sits - a softer alternative to pure black for large dark areas
- Silver Hairline `#b0b0b0` for Subtle dividers and muted secondary links - a quiet mid-gray that recedes behind the black ink without disappearing

- Haas Grotesk DS Pro `--font-haas-grotesk-ds-pro` for Display and section wordmarks - used at 48-288px with extremely tight leading (0.77-0.80) so multi-line display type nearly touches. The DS variant's compressed proportions are what let 288px headlines fit within a single viewport without breaking rhythm. Substitute: Neue Haas Grotesk Display, or Akzidenz-Grotesk Pro Medium
- Haas Grotesk TX Pro `--font-haas-grotesk-tx-pro` for Body copy, captions, image labels, navigation links, UI text. Weight 400 for body, weight 500 for navigation labels and emphasis. The 36px size at line-height 0.90 creates a tight subheading that bridges body and display scales. Substitute: Neue Haas Grotesk Text, or Inter

## Avoid

- Never introduce chromatic colors - the palette is strictly black, white, and gray
- Never add box-shadow, drop-shadow, or any elevation effect - the page is flat
- Never use border-radius greater than 0px on any element
- Never use weight 700+ for headings - medium (500) is the heaviest weight in the system
- Never set display type with line-height above 0.85 - the tight leading is what makes oversized type feel structural
- Never use colored hover or active states on links - navigation is purely typographic and static
- Never center text within columns - all text aligns left within its column

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
