# FORA

Source: [Refero Style](https://styles.refero.design/style/9929101b-90d4-4306-bc4a-4d8f65b527f5)
Reference site: [https://fora-concept.com](https://fora-concept.com)
Captured: 2026-07-31
Refero published: 2026-03-04T19:23:19.000Z
Refero modified: 2026-06-05T10:31:32.916Z
Theme: light
Category: Agency

## Style Summary

Explore FORA's light Agency design system: Obsidian #000000, Paper #ffffff colors, Theinhardt, Theinhardt Medium typography, and DESIGN.md for AI agents.

North star: Swiss editorial mosaic on white. A grid of monumental color tiles and airy geometric type, where each panel of terracotta or lilac functions as a full-bleed typographic stage.

## What To Borrow

- Obsidian `#000000` for All text, headings, icons, nav links, dividers, and borders. Unsoftened true black anchors every chromatic panel
- Paper `#ffffff` for Page canvas, default card surface, and the negative space that lets chromatic panels breathe. Never tinted
- Terracotta `#a9553c` for Full-bleed section panels and hero zones. Warm oxidized red-brown against pure black and white - evokes raw clay and printed editorial covers
- Lilac Veil `#ddbdea` for Full-bleed section panels, content cards, and soft surface tint. Muted chalky pink that cools the terracotta into a balanced two-color rhythm

- Theinhardt `--font-theinhardt` for Sole typeface across all UI: nav, body, headings, buttons, labels. Positive letter-spacing (0.01em 0.024em) that grows with size is the anti-trend signature - tracking opens up rather than tightens, producing a Swiss neo-grotesque with editorial breathing room. The 700 weight appears only for micro-emphasis (tag labels), keeping the system light and even.
- Theinhardt Medium `--font-theinhardt-medium` for Theinhardt Medium - detected in extracted data but not described by AI

## Avoid

- Don't soften black to near-black or add a tint - #000000 is absolute and the system depends on that contrast.
- Don't introduce a third chromatic color, a gradient, or a neutral mid-gray. The two-color discipline is the brand.
- Don't add shadows, glows, or elevation to cards. The grid is flat - surfaces sit on the page, not above it.
- Don't use negative letter-spacing on any size. The positive tracking is a signature, not a mistake to correct.
- Don't round card or panel corners beyond 0px. The sharp 90 edges are what make it feel like editorial print.
- Don't mix multiple typefaces or weight the headlines at 600-700. Theinhardt 400 everywhere, plus rare 700 for micro-tags.
- Don't create centered, max-width containers. The grid is full-bleed; content fills its tile completely.

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
