# Drepute

Source: [Refero Style](https://styles.refero.design/style/523d3e7b-b0a2-4979-a626-00f1487b6e4d)
Reference site: [https://drepute.xyz](https://drepute.xyz)
Captured: 2026-07-31
Refero published: 2026-04-30T01:57:17.023Z
Refero modified: 2026-06-05T09:52:49.352Z
Theme: dark
Category: Other

## Style Summary

Explore Drepute's dark Other design system: Pure White #ffffff, Deep Ink #000000 colors, Source Sans Pro, Playfair Display typography, and DESIGN.md for AI...

North star: midnight observatory over still water - a single sentence floats beneath a field of stars

## What To Borrow

- Pure White `#ffffff` for Primary text on dark hero, input fills, light surfaces
- Deep Ink `#000000` for Dominant text and border color across body, nav, and dividers
- Obsidian `#161616` for Dark canvas and hero surface - the page's atmospheric base
- Ash Gray `#bfbfbf` for Subtle input borders, ghost box-shadows, disabled hairlines
- Fog `#a9a9a9` for Secondary body text, muted borders, low-emphasis dividers
- Steel `#7f8080` for Navigation and link borders, tertiary text on light surfaces
- Slate Blue `#8995a9` for Outlined ghost-button border - the only chromatic interactive treatment
- Lagoon Teal `#00a4a6` for Sole accent - link border, indicating the single interactive edge in the system

- Source Sans Pro `--font-source-sans-pro` for Workhorse sans for body, buttons, nav, inputs, and all UI microcopy; weight 700 reserved for emphasis
- Playfair Display `--font-playfair-display` for Display serif for hero headlines ('Launching Soon') - the single expressive type voice; weight 400 italic-leaning elegance rather than bold
- Montserrat `--font-montserrat` for Wordmark only - 'DREPUTE' set wide at 0.154em to function as a typographic constellation above the hero
- GD Sherpa `--font-gd-sherpa` for Custom brand secondary; deployed alongside Source Sans Pro for select links and image overlays
- Times `--font-times` for Times - detected in extracted data but not described by AI

## Avoid

- Do not add shadows, gradients, or glows to any component - the system is flat and photographic.
- Do not introduce pills, circles, or any radius above 4px.
- Do not use color fills on buttons - all actions are ghost/outlined with border-only treatment.
- Do not use Playfair Display below 44px - it is a display face, not a body face.
- Do not place body text directly over the hero photograph without a #161616 backing layer - contrast must remain AAA.
- Do not add more than one chromatic accent - the teal is singular; adding another color breaks the cinematic restraint.
- Do not use bold (600+) on the wordmark - weight 700 is the ceiling, and it only applies to Montserrat.

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
