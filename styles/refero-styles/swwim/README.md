# Swwim

Source: [Refero Style](https://styles.refero.design/style/5cb1fbe8-b539-4482-b645-74a745332965)
Reference site: [https://www.weswwim.com](https://www.weswwim.com)
Captured: 2026-07-31
Refero published: 2026-04-30T02:23:51.496Z
Refero modified: 2026-06-05T10:54:53.463Z
Theme: light
Category: Agency

## Style Summary

Explore Swwim's light Agency design system: Cobalt Current #1658b3, Deep Channel #0d3c88 colors, Baton Turbo, Greycliff typography, and DESIGN.md for AI agents.

North star: Cobalt wave with floating luxury objects.

## What To Borrow

- Cobalt Current `#1658b3` for Hero background, primary surface flood, outlined-link borders - the single color that defines every full-bleed section
- Deep Channel `#0d3c88` for Darker blue for gradient depth in decorative graphics, icon accents, footer bands
- Electric Ripple `#015fee` for Violet wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Abyssal Ink `#01295f` for Darkest blue used inside SVG decoration and deep gradient stops - never as text or button
- White Canvas `#ffffff` for Page background, body text on blue, primary pill button fill - the neutral that carries white sections and inverts on blue
- Cloud Border `#e5e7eb` for Hairline dividers, card borders, separator rules across all white surfaces - the structural neutral of the system
- Carbon `#000000` for Body text on white, icon fills in black-mode illustrations
- Nude Clay `#eee1d9` for Warm flesh-tone accent inside decorative illustration fills and strokes - the only chromatic neutral, used to humanize blue compositions

- Baton Turbo `--font-baton-turbo` for Display and oversized headlines only - the 151px hero weight is the signature choice, a single weight (400) stretched across 14px to 151px to create the full editorial scale
- Greycliff `--font-greycliff` for Body, UI labels, nav, buttons, badges, footer - the working typeface at three weights, with 500/700 reserved for small headings and nav emphasis

## Avoid

- Do not use Baton Turbo for body copy, nav labels, buttons, or anything below 20px - it loses its editorial voice at small sizes
- Do not introduce drop shadows, glows, or multi-layer elevation stacks - the system is intentionally flat
- Do not add chromatic colors outside the blue family plus the single #eee1d9 flesh tone accent
- Do not center the hero composition in a clean symmetrical layout - the scattered overlapping product crops are the signature
- Do not round card corners or input fields; the only radius in the system is the 9999px pill
- Do not use 151px type outside the hero; the display scale steps sharply down to 48px
- Do not break the blue monochrome with a contrasting CTA color - the white pill on blue IS the action pattern

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
