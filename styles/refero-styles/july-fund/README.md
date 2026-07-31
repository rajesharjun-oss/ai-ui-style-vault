# July Fund

Source: [Refero Style](https://styles.refero.design/style/adc127f5-c6ec-4892-984d-5445c2b6104e)
Reference site: [https://july.fund](https://july.fund)
Captured: 2026-07-31
Refero published: 2026-04-30T01:40:13.405Z
Refero modified: 2026-06-05T08:32:01.972Z
Theme: dark
Category: Fintech

## Style Summary

Explore July Fund's dark Fintech design system: Obsidian #000000, Coffee Bean #433e3c colors, Portrait, Helvetica Neue typography, and DESIGN.md for AI agents.

North star: dark gallery monograph with chromatic chapter cards

## What To Borrow

- Obsidian `#000000` for Page canvas, deepest card base, and the void between sections - the room the cards hang in
- Coffee Bean `#433e3c` for Dominant border color across cards, badges, and dividers - the hairline that frames every chromatic block
- Cream Paper `#f0e7e4` for Light card surface for the hero/about panel and inverted buttons - a warm off-white that reads as printed paper on the dark canvas
- Charcoal `#2b2b2b` for Secondary surface and elevated card base for monochrome content blocks
- Espresso `#221f1e` for Button background for primary text controls on dark surfaces - one shade deeper than the card it sits in
- Stone Gray `#898989` for Muted body copy, list markers, and supporting metadata - the whisper tier below primary text
- Paper White `#ffffff` for Headline color on dark cards, badge text on chromatic fills, and link highlights
- Forest Floor `#113619` for Themed card surface for nature/climate/sustainability chapters - the deepest chromatic field, reads as moss or deep canopy
- Twilight Violet `#322b66` for Themed card surface for space, frontier, and science verticals - saturated enough to dominate a grid cell, dark enough to hold white type
- Olive Depth `#2e2909` for Themed card surface for energy and industry chapters - a near-black ochre that glows against the canvas
- Solar Yellow `#fde440` for High-impact accent card fill for transformation and thesis verticals - the loudest single block in the system, used sparingly to punctuate the grid
- Mint Chip `#56d270` for Small uppercase tag/badge fill for news and announcement labels - the only saturated green used at small scale
- Lavender Mist `#c6bffa` for Soft accent for secondary badges and highlight borders on the violet card family
- Ember Red `#b9534a` for Reserved research and analytical-content badge fill - used almost never; its rarity makes it register as a category marker

- Portrait `--font-portrait` for Display and heading serif used for the wordmark, section titles, and card headlines. Portrait is a high-contrast didone-style serif; its hairline strokes and sharp serifs give the site its monograph feel. A single weight (400) is used - no bold headlines, authority comes from size and contrast alone.
- Helvetica Neue `--font-helvetica-neue` for Body, UI, badges, buttons, and metadata. Tight 400 for body, 700 for emphasis. The wide letter-spacing at small sizes (0.20-0.25em) is the defining micro-typography move: even 8px labels read as intentional, not afterthoughts.

## Avoid

- Don't add box-shadow, glow, or blur to any element - the system is flat by design.
- Don't use bold weights for Portrait headlines; authority comes from size, not weight.
- Don't mix two chromatic fills inside a single card - pick one field and commit.
- Don't place body copy in a chromatic color other than Stone Gray (#898989), Paper White, or Coffee Bean - no accent text.
- Don't use buttons with square or 8px corners; the 24px pill is non-negotiable.
- Don't set background gradients on text-forward cards - gradients are reserved for the radial accent washes in hero/empty states.
- Don't center body paragraphs or labels; left-align everything except the wordmark.

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
