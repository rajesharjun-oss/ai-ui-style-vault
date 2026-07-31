# Specht Studio

Source: [Refero Style](https://styles.refero.design/style/dd646da4-36f5-42b1-83dd-6a1c90cf8983)
Reference site: [https://stephaniespecht.com](https://stephaniespecht.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:13:27.224Z
Refero modified: 2026-06-05T11:00:40.682Z
Theme: light
Category: Design

## Style Summary

Explore Specht Studio's light Design design system: Gallery White #ffffff, Fog Gray #b0b0b0 colors, Helvetica Neue typography, and DESIGN.md for AI agents.

North star: Gallery wall of restrained curiosity. The studio's own chrome is a white plane and black type; the visual fireworks live entirely inside the project tiles.

## What To Borrow

- Gallery White `#ffffff` for Page canvas, project tile background where artwork doesn't fill the frame
- Fog Gray `#b0b0b0` for Secondary surface, subtle dividers, muted metadata text
- Graphite `#666666` for Link borders, secondary text, caption metadata, inactive nav
- Gallery Black `#000000` for Primary text, active nav, all structural borders, the single ink that holds the system together

- Helvetica Neue `--font-helvetica-neue` for Sole typeface across every context - nav, body, headings, links, footer. The deliberate choice of a single weight at 400 across all roles removes typographic hierarchy and forces the grid and the imagery to do the ranking. No display cuts, no bold emphasis, no italics - restraint as a point of view.

## Avoid

- Do not introduce a brand color. Any chromatic accent would shift the system from 'gallery wall' to 'product page' and destroy the curatorial neutrality.
- Do not add rounded corners to tiles, buttons, or containers. The system is orthogonal - sharp 0px radii everywhere.
- Do not use shadows, blurs, or elevation. Depth must come from image content and grid density, not from CSS box-shadow.
- Do not use multiple typefaces or weights. A second weight or family immediately introduces hierarchy that the system deliberately suppresses.
- Do not add a CTA button. There is no primary action in this system - if a page needs a link, use a Graphite-underlined text link.
- Do not center the content on the page. The grid is left-aligned, slightly off-center, which creates the editorial-publication feel.
- Do not use gradients, fills, or tinted backgrounds. Every surface is pure white or pure black, never a shade between.

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
