# ONE

Source: [Refero Style](https://styles.refero.design/style/71745af1-2e53-4925-992e-82773e55ccd6)
Reference site: [https://one-is.com](https://one-is.com)
Captured: 2026-07-31
Refero published: 2026-04-30T02:32:28.246Z
Refero modified: 2026-06-05T09:25:35.754Z
Theme: light
Category: Agency

## Style Summary

Explore ONE's light Agency design system: Ink #000000, Paper #fbfbfa colors, MagicUiPro typography, and DESIGN.md for AI agents.

North star: art monograph on warm paper

## What To Borrow

- Ink `#000000` for Primary text, hairline borders, video frame outlines, pill button stroke - the only chromatic event in the UI
- Paper `#fbfbfa` for Soft icon strokes, subtle dividers, and low-emphasis decorative details. Do not promote it to the primary CTA color
- Ash `#bec0c5` for Muted text in the cycling manifesto, list dividers, inactive link tone - desaturated gray stays quiet next to ink

- MagicUiPro `--font-magicuipro` for Single-family system: body text and micro-headlines both sit in the 18-24px range at medium weight, with weight 600 reserved for the active manifesto item and button labels. The tight -0.01em tracking and modest size range mean type never breaks 24px - the page treats every word as a label, not a headline.

## Avoid

- Do not introduce accent colors, brand hues, or saturated fills - the palette is strictly ink/paper/ash
- Do not add box-shadows, gradients, or background blurs to any surface
- Do not scale type above 24px or below 18px - both would break the label-scale system
- Do not use weight 400 or 700; the system is bound to 500 and 600 only
- Do not use square or 4px radii on buttons; pill is the only allowed control shape
- Do not add a filled/solid button variant; the Ghost Pill Button is the sole interactive pattern
- Do not add icons, badges, or secondary navigation in the header - the chrome is exactly two elements

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
