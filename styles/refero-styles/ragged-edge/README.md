# Ragged Edge

Source: [Refero Style](https://styles.refero.design/style/fdc0f631-442c-466d-ab79-e1fff2bfdb7d)  
Reference site: [https://raggededge.com](https://raggededge.com)  
Captured: 2026-07-29  
Refero published: 2026-04-30T00:35:49.924Z  
Refero modified: 2026-06-05T09:31:23.055Z  
Theme: light  
Category: Agency

## Style Summary

Explore Ragged Edge's light Agency design system: Obsidian Ink #181f1f, Paper White #ffffff colors, ABCDiatypeExpanded-Bold, Grit-Regular typography, and...

North star: Editorial brutalism on white marble. Imagine Vogue's typographic confidence merged with a Berlin gallery's color restraint all ink and air, with one burst of color used as exclamation, never decoration.

## What To Borrow

- Obsidian Ink `#181f1f` as Primary text, hairline borders, filled action buttons the dominant near-black that carries 90% of the interface
- Paper White `#ffffff` as Canvas background, inverted text on dark blocks, nav/button borders
- Fog `#d1d2d2` as Subtle dividers and secondary borders where Obsidian would be too heavy
- Ash `#a3a5a5` as Muted helper text, inactive button borders, secondary metadata
- Graphite `#374151` as Secondary body text and subtle icon strokes where a lighter black is needed
- True Black `#000000` as Navigation dividers and surface backing for select blocks
- ABCDiatypeExpanded-Bold Display, brand logo, section headings, project titles, and nav labels. The extremely wide expanded letterforms (letter-spacing -0.02em at 7882px) are the signature element uppercase, never set small under 10px, and reserved for moments that demand visual weight. The 7882px sizes fill the full width of the hero canvas. Weight stays at 400 because the expansion provides all the weight needed; going bolder would distort the geometric proportions. `--font-abcdiatypeexpanded-bold` for the source typography voice
- Grit-Regular All body copy, paragraph text, descriptions, and mid-weight headings. A contemporary serif with subtle texture provides editorial gravitas against the expanded display sans. Weight 400 for running text, 500 for emphasized phrases and sub-headings. The 56px size with 1.25 line-height creates dramatic editorial pull-quotes. Pairs with ABCDiatypeExpanded by contrasting serif warmth against geometric coldness. `--font-grit-regular` for the source typography voice
- 4px base spacing with comfortable density
- Source radius system: nav 64px, cards 40px, inputs 54px, buttons 64px

## Avoid

- Do not introduce additional accent colors the system is 98% monochrome; a second chromatic breaks the discipline.
- Do not apply box-shadows anywhere depth comes from surface tone shifts, not elevation.
- Do not use ABCDiatypeExpanded for body copy longer than 45 words; it is a display face, not a running-text face.
- Do not center body text blocks; editorial layouts read left-aligned with generous left margin.
- Do not use border-radius below 40px on any container sharp corners clash with the pill-button system.
- Do not place Iris Voltage on dark backgrounds; it loses its accent role against high-contrast surfaces.
- Do not set the hero gradient above 0deg orientation or stop count; the directional flow is part of the signature.

## Bundle Contents

- [DESIGN.md](DESIGN.md): implementation notes.
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
