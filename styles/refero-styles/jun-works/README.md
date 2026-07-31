# jun.works

Source: [Refero Style](https://styles.refero.design/style/02ba867b-49e3-4ab4-ad23-c30baf345078)
Reference site: [https://jun.works](https://jun.works)
Captured: 2026-07-31
Refero published: 2026-04-30T03:13:34.771Z
Refero modified: 2026-06-05T11:18:13.344Z
Theme: light
Category: Design

## Style Summary

Explore jun.works's light Design design system: Press Black #000000, Bone White #ffffff colors, Standard, Times typography, and DESIGN.md for AI agents.

North star: printed editorial zine with sticker labels - black ink on bright white, nothing else

## What To Borrow

- Press Black `#000000` for Body text, all borders, pill outlines, button strokes - the sole ink color, used at full opacity for every foreground element
- Bone White `#ffffff` for Page canvas, card surfaces, pill fills - the only surface color, creating maximum contrast against Press Black
- Smoke Gray `#cccccc` for Hairline dividers, muted outlines, secondary borders where a softer separation is needed

- Standard `--font-standard` for Display and heading type only - a custom geometric sans used at two large sizes with extreme negative tracking (-0.045em to -0.054em). Also sets link and button text. The single weight (400) and tight tracking create a compressed, poster-like presence that dominates the page. No bold variant exists; hierarchy is achieved through size and tracking alone.
- Times `--font-times` for Body and micro-copy type - the system serif at 13px, used in editorial contexts (footnotes, annotations, fine print). The serif/sans collision with Standard is deliberate: the sans shouts, the serif footnotes.

## Avoid

- Never add color - no accent, no semantic green/red/yellow, no brand color
- Never use box-shadow or elevation - depth comes from border definition, not shadow
- Never use border-radius below 129.6px on any element
- Never bold the display type - Standard ships in one weight (400) and that restraint is the system
- Never use a sans-serif for body text - the serif/sans split is structural, not optional
- Never center-align headings or body paragraphs
- Never add imagery, photography, or illustration - the page is pure typography and label geometry

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
