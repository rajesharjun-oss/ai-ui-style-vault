# Not Real

Source: [Refero Style](https://styles.refero.design/style/c0a3f588-74b7-4fad-b557-1fc7cd7bd777)
Reference site: [https://notreal.tv](https://notreal.tv)
Captured: 2026-07-31
Refero published: 2026-04-30T02:13:13.078Z
Refero modified: 2026-06-05T11:01:14.652Z
Theme: light
Category: Agency

## Style Summary

Explore Not Real's light Agency design system: Ink Charcoal #292a2c, Vellum #f2f2f2 colors, ogg, telegraf typography, and DESIGN.md for AI agents.

North star: Editorial gallery spread on greyscale vellum - a high-end catalog where only the artwork is allowed to scream with color.

## What To Borrow

- Ink Charcoal `#292a2c` for Primary text, dominant border strokes (635 occurrences as borderColor), nav accents
- Vellum `#f2f2f2` for Page canvas, card surfaces - warm-leaning off-white that gives the page a paper-stock feel rather than digital white
- Full Black `#000000` for Link border underlines, footer text, icon strokes, image overlay text - used as a chromatic anchor only where maximum contrast against Vellum is required

- ogg `--font-ogg` for Display and project headlines. This is a high-contrast didone-flavored serif used at 55px with aggressive -0.036em tracking - it acts as the gallery label, announcing each case study with typographic weight that the sans-serif never attempts. At smaller sizes (24-26px) the same family handles editorial pull-quotes and the wordmark, where the negative tracking tightens less aggressively (-0.02em). The signature choice: a single weight (400) doing all serif work, relying on the contrast within letterforms rather than weight variation to create hierarchy.
- telegraf `--font-telegraf` for Body copy, navigation, metadata tags, project category labels, and secondary headings. A geometric sans that does all the quiet documentation work. At 55px it can also serve as display type, creating a rare moment where both fonts meet at the same size - typically the serif announces the project name while the sans describes it below. Tracking is positive throughout (0.002em to 0.040em), widening as size decreases - a deliberate inverse relationship that keeps small caps-styled metadata readable and gives the wordmark breathing room.

## Avoid

- Do not introduce any chromatic color into the UI - saturated color belongs exclusively to client artwork
- Do not apply border-radius to any element, including buttons, cards, tags, or images
- Do not add box-shadow, drop-shadow, or any CSS elevation - the design is intentionally flat
- Do not use centered layouts or constrained max-width wrappers - let content flow to viewport edges
- Do not use bold (600+) or semibold weights - both fonts operate at 400 only
- Do not create a distinct filled CTA button - links are text with 1px black borders, nothing more prominent
- Do not alternate background colors between sections - the entire page shares the single Vellum canvas

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
