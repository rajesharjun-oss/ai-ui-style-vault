# Thomas Hedger

Source: [Refero Style](https://styles.refero.design/style/9fe18d8b-58b7-404d-bcc6-9e8a73b8862c)
Reference site: [https://thomashedger.co.uk](https://thomashedger.co.uk)
Captured: 2026-07-31
Refero published: 2026-04-30T03:29:16.353Z
Refero modified: 2026-06-05T11:53:58.594Z
Theme: light
Category: Design

## Style Summary

Explore Thomas Hedger's light Design design system: Canvas White #ffffff, Ink Black #000000 colors, Diatype, Diatype Variable typography, and DESIGN.md for...

North star: Silent frame, loud prints

## What To Borrow

- Canvas White `#ffffff` for Page background, card surface, text on dark tiles
- Ink Black `#000000` for Primary text, card and image borders, grid hairlines, nav accents
- Carbon Plum `#29242b` for Heading text - a warm near-black that softens against pure Ink Black for editorial moments
- Ash `#e5e5e5` for Subtle divider and muted border tone for low-emphasis separations

- Diatype `--font-diatype` for Body and small UI text at 19px; copyright/caption at 9px. Diatype is a contemporary neo-grotesque with humanist proportions - paired with the bold Variable cut, it creates a tight, modern-editorial feel without a serif in sight. The 9px caption is intentionally tiny, like a museum wall label.
- Diatype Variable `--font-diatype-variable` for Primary navigation and section headings at 26px. The 500 weight is the default nav voice; 700 is reserved for emphasis and the designer's name. The 26px cap-height next to 19px body text creates a deliberate 7px gap that reads as confident hierarchy without loud type.
- Times `--font-times` for Occasional fallback or inherited editorial copy; not a primary voice. Appears at 13px as a quiet secondary tier.

## Avoid

- Do not add shadows, gradients, or border-radius to any component - the design is intentionally flat.
- Do not introduce accent, brand, or semantic colors (no success green, no error red) - the palette is a closed two-tone system.
- Do not use a serif or display font for navigation - Diatype Variable is the only allowed heading voice.
- Do not add hover backgrounds, underlines, or animation to nav links - text alone is the interactive surface.
- Do not wrap the grid in a centered max-width container - the mosaic must reach the viewport edges.
- Do not use type sizes outside the 9/13/19/26 scale - interpolation breaks the editorial rhythm.
- Do not add card surfaces, elevated panels, or modal containers - if it needs a container, the project image should fill it directly.

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
