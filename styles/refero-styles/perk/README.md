# Perk

Source: [Refero Style](https://styles.refero.design/style/75c06591-34d2-493a-bd49-70551b5e4a53)
Reference site: [https://travelperk.com](https://travelperk.com)
Captured: 2026-07-30
Refero published: 2026-04-05T18:07:33.000Z
Refero modified: 2026-07-03T11:10:44.012Z
Theme: light
Category: SaaS

## Style Summary

Explore Perk's light SaaS design system: Electric Lime #beff50, Off-Black Ink #14140f colors, OTSono typography, and DESIGN.md for AI agents.

North star: electric lime on warm parchment paper

## What To Borrow

- Electric Lime `#beff50` for Primary action background, hero surface fills, accent panels - the singular chromatic charge against an otherwise achromatic system, creating brand presence through contrast not decoration
- Off-Black Ink `#14140f` for Body text, headings, icon fills, link borders, button text - warm-tinted near-black that feels less clinical than pure black against parchment
- Off-White Canvas `#f5f5eb` for Card surfaces, secondary page background - warm parchment replacing cold white as the resting surface for the lime accent
- Pure White `#ffffff` for Highest surface level, card fills, input fields - used where clean white needs to lift above the parchment
- Ash `#d2d2c8` for Borders, dividers, subtle structural lines, inactive backgrounds - the warm gray that separates surfaces without harshness
- Graphite `#6e6e64` for Muted body text, secondary copy, card text - warm gray for de-emphasized information
- Deep Charcoal `#30302a` for Dark card surfaces, inverted blocks - for rare moments when the page flips to a dark island
- Stone `#919183` for Faint borders, decorative strokes - only visible at fine stroke widths
- Smoke `#b9b9b7` for Placeholder backgrounds, subtle wash zones

- OTSono `--font-otsono` for Single-family system covering everything from 90px display headlines (weight 500, line-height 0.89, tracking -0.03em) through 16px body (weight 400, line-height 1.5) to 10px micro-labels. Weight 500 is the emphasis voice used on headings, labels, and CTAs; weight 400 handles body, icons, and supporting text. The 0.1em tracking on small caps is reserved for eyebrow labels and category tags.

## Avoid

- Do not add box-shadows to cards - the system relies on tonal contrast, not elevation
- Do not use #000000 for body text - #14140f is warmer and more on-brand
- Do not introduce blue, red, or any secondary accent color - the lime is the only chromatic voice
- Do not mix border-radius values within the same component type (all buttons are 28px, all pills are 9999px)
- Do not use system fonts as fallback for display sizes - OTSono at 60px+ with -0.03em tracking is signature
- Do not place lime buttons on white surfaces without sufficient padding - the contrast is loud, give it room
- Do not use 600 or 700 weights - the system operates on 400 and 500 only
- Do not add gradients - the lime is already saturated; gradients would muddy it

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
