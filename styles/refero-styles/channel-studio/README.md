# Channel Studio

Source: [Refero Style](https://styles.refero.design/style/4c19bf7b-d5e8-4e2a-b3e3-69a9bde19b7a)
Reference site: [https://channel.studio](https://channel.studio)
Captured: 2026-07-31
Refero published: 2026-04-30T01:41:27.816Z
Refero modified: 2026-06-05T07:36:44.270Z
Theme: dark
Category: Agency

## Style Summary

Explore Channel Studio's dark Agency design system: Bone Gray #cacaca, Carbon Black #0a0a0a colors, Lausanne typography, and DESIGN.md for AI agents.

North star: Studio darkroom with a single coral flare

## What To Borrow

- Bone Gray `#cacaca` for Primary text on dark surfaces, hairline borders on images and links, divider strokes - a desaturated near-white that reads softer than pure #fff against black
- Carbon Black `#0a0a0a` for Page background, section canvas, project card surface - the entire design lives here
- Iron Gray `#727272` for Muted secondary text, low-emphasis borders, caption-level metadata
- Coral Flare `#ff7777` for Accent for project titles, signature heading borders, and occasional decorative strokes - the only chromatic element in the system, used sparingly for editorial emphasis

- Lausanne `--font-lausanne` for Sole typeface across all roles - navigation, body, subheadings, and display headlines. Weight stays at 400 throughout; visual hierarchy is built entirely through size and tracking, not weight. Display at 75px uses line-height 0.90-0.95, creating a compressed poetry-staircase effect unique to this system.

## Avoid

- Never use shadows, gradients, or any elevation effects - the design is deliberately flat
- Never add border-radius to cards, buttons, images, or any element - 0px everywhere
- Never use color other than #ff7777 for accents - no blues, greens, or other hues; the system is monochromatic plus one coral
- Never set body or heading text in pure #fff - always use #cacaca for the softened-light quality
- Never use multiple font weights - the system is weight 400 only across all roles
- Never use centered text alignment for body content - everything is left-aligned with the viewport edge
- Never add background colors to cards, buttons, or interactive elements - they sit directly on the black canvas

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
