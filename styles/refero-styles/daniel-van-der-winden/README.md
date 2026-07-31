# Daniel van der Winden

Source: [Refero Style](https://styles.refero.design/style/e8eda526-d686-4e45-a60d-61b6503a8eda)
Reference site: [https://www.daniel.pizza](https://www.daniel.pizza)
Captured: 2026-07-31
Refero published: 2026-04-30T02:05:33.966Z
Refero modified: 2026-06-05T07:33:33.320Z
Theme: light
Category: Agency

## Style Summary

Explore Daniel van der Winden's light Agency design system: Vellum #e5e7eb, Ink Black #111827 colors, Degular, Blanco typography, and DESIGN.md for AI agents.

North star: Printed monograph on vellum

## What To Borrow

- Vellum `#e5e7eb` for Page canvas, hairline dividers, link underlines, card-edge borders - the warm-gray field that holds all content
- Ink Black `#111827` for Primary text, nav links, body copy - the default reading color
- Graphite `#374151` for Secondary body text, list items, supporting copy - one step lighter than primary ink
- Charcoal `#2a2a28` for Headings and editorial emphasis - slightly warm dark for serif display
- Stone `#717272` for Tertiary text, icon fills, meta labels
- Pebble `#909191` for Muted body text, image captions, fine print
- Ash `#c4c6c8` for Rarely-used border, subtle structural separator
- Slate `#7b7c7c` for Subdued heading variant, de-emphasized titles
- Pressed Ink `#222222` for Primary action button fill - the only dark surface on the canvas, creating the only moment of visual weight
- Midnight `#1a202c` for Secondary dark surface, alternate button fill

- Degular `--font-degular` for UI and body sans - navigation, buttons, body copy, metadata, links, tags, resume dates. Carries all functional text. Weights step from 400 body to 700 for emphasis in headings and dates.
- Blanco `--font-blanco` for Editorial serif - hero headline, resume role titles, section headings, and any text that should read as 'published' rather than 'navigational'. Single weight 400, letting size and the serif's own authority carry hierarchy.

## Avoid

- Do not introduce chromatic color - the 3% colorfulness is deliberate, not a limitation to fix.
- Do not add shadows, gradients, or glow effects; elevation is achieved through fill contrast only.
- Do not use Blanco for body text or nav; it is a display face, not a reading face.
- Do not create card containers with backgrounds or borders for content blocks - content sits directly on the vellum.
- Do not use 9999px pill radius; this system's 3px radius is a quiet, bookish choice.
- Do not bold body text for emphasis; use size, color, or the Blanco/Degular font swap instead.
- Do not center-align body paragraphs; left-align at a fixed reading width to preserve the editorial column.

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
