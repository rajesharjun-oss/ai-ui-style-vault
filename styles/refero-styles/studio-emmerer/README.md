# Studio Emmerer

Source: [Refero Style](https://styles.refero.design/style/670869ea-9576-4f9d-af3a-038910f8b9b8)
Reference site: [https://emmerer.com](https://emmerer.com)
Captured: 2026-07-31
Refero published: 2026-04-30T01:38:27.267Z
Refero modified: 2026-06-05T10:30:36.515Z
Theme: light
Category: Agency

## Style Summary

Explore Studio Emmerer's light Agency design system: Pure Black #000000, Drafting White #ffffff colors, NHaasGrotesk typography, and DESIGN.md for AI agents.

North star: Typeset on drafting paper

## What To Borrow

- Pure Black `#000000` for Body text, inline links, project titles, table row dividers, the arrow ( ) glyph
- Drafting White `#ffffff` for Page background, surface under all content - no tint, no gradient
- Index Gray `#999999` for Table column headers (PROJECT, TYPE, LOCATION, YEAR), supporting metadata, secondary borders

- NHaasGrotesk `--font-nhaasgrotesk` for Sole typeface for every UI element - headlines, body, links, table cells, column headers, navigation. Single weight 400 across the entire system, with negative letter-spacing tightening at every size. The Neue Haas Grotesk DNA (geometric neutrality, grotesque proportions) is what carries the architectural-document feel; substitute Helvetica Neue or Inter as a free fallback.

## Avoid

- Never introduce a chromatic color - the palette is strictly black, white, and #999999.
- Never use font-weight above 400 - bold or semibold would shatter the single-weight voice of the system.
- Never add box-shadow, drop-shadow, or any z-axis elevation.
- Never apply border-radius - all corners stay at 0px.
- Never wrap content in filled cards, panels, or containers - rows sit directly on the page surface.
- Never introduce an icon set beyond the arrow; no SVGs, no pictograms, no button shapes.
- Never change link color on hover - links stay #000000 with the same underline weight to preserve the printed-page feel.

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
