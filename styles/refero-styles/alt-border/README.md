# Alt-Border

Source: [Refero Style](https://styles.refero.design/style/5fd2cdc0-05ac-4290-b67c-72e7525a532c)
Reference site: [https://www.alt-border.com](https://www.alt-border.com)
Captured: 2026-07-31
Refero published: 2026-04-30T01:51:17.833Z
Refero modified: 2026-06-05T09:28:49.443Z
Theme: light
Category: Agency

## Style Summary

Explore Alt-Border's light Agency design system: Ink #000000, Gallery White #ffffff colors, Neuehaasdisplay, Inferi typography, and DESIGN.md for AI agents.

North star: Monochrome editorial gallery - broadsheet headline on gallery white.

## What To Borrow

- Ink `#000000` for Primary type, body text, hairline rules, link borders, and the structural color of the entire page - used at high frequency for borders and text alike, creating a printed-ink quality against the white canvas
- Gallery White `#ffffff` for Page canvas, card and image backgrounds, the negative space that lets type and photography breathe
- Graphite `#333333` for Secondary text, muted borders, image strokes - a slightly softened black for elements that should not compete with primary ink
- Ash `#808080` for Section divider rules, link borders, faint hairlines where a true black stroke would be too assertive

- Neuehaasdisplay `--font-neuehaasdisplay` for Hero display - used only for the massive opening headline and section-statement lines that fill the viewport. The 0.85 line-height is a deliberate choice: lines nearly touch, producing the compressed broadsheet effect. Substitute: Neue Haas Grotesk Display Pro 35 Thin, or Inter at extreme sizes.
- Inferi `--font-inferi` for Multi-purpose face - medium-weight paragraphs (21px), oversized secondary statements (34px, 120px), and small UI labels (14px). The negative tracking (-0.0270em) tightens the rhythm at every size. Substitute: Sohne, Inter, or Untitled Sans.
- Suisseintl `--font-suisseintl` for Body and supporting copy - quiet, legible, never decorative. Same negative tracking as Inferi keeps the family consistent. Substitute: Suisse Int'l Light, or Inter Light.

## Avoid

- Do not introduce any chromatic color - the palette is achromatic by design, not by omission.
- Do not add drop shadows, blurs, or any elevation - separation comes from rules and whitespace alone.
- Do not round corners on images, buttons, or cards - 0px radius is the system.
- Do not use a CTA button style - there is no primary action color; navigation is text-only with arrow links.
- Do not exceed 0.92 line-height on the 105px display - looser tracking destroys the broadsheet compression.
- Do not set body type below 14px or above 34px - the scale jumps are deliberate: 14, 21, 34, 105.
- Do not add background fills to sections, cards, or navigation - the page is a single white sheet.

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
