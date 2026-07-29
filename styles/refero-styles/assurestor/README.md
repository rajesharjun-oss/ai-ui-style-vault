# Assurestor

Source: [Refero Style](https://styles.refero.design/style/0ed40a3a-2541-4ffa-acdd-f1170858bc5d) 
Reference site: [https://www.assurestor.com](https://www.assurestor.com) 
Captured: 2026-07-29 
Refero published: 2026-05-11T00:08:49.109Z 
Refero modified: 2026-06-03T20:27:34.476Z 
Theme: dark 
Category: SaaS

## Style Summary

Explore Assurestor's dark SaaS design system: Forest Canopy #203400, Vault Floor #1b2d00 colors, Denim Ink, Courier New typography, and DESIGN.md for AI agents.

North star: Electric terminal in a deep forest vault - lime phosphor on midnight olive.

## What To Borrow

- Forest Canopy `#203400` for Primary page background, nav strip, footer canvas - the dominant surface that defines the entire brand atmosphere
- Vault Floor `#1b2d00` for Card surfaces, recessed panels, elevated content blocks within the forest canvas
- Canopy Mid `#335400` for Elevated card variant, highlighted surface tier above the base canvas
- Lime Phosphor `#bdff00` for Primary action buttons, active state indicators, illustrative highlight panels, brand-accent moments - the sole chromatic signal in the system
- Moss Border `#586740` for Hairline dividers, list separators, subtle table borders - barely-there green-on-green rules
- Fern `#73a303` for Secondary accent strokes, table emphasis borders, mid-saturation green used sparingly for variety within lime contexts
- White `#ffffff` for Body text, heading text, icon strokes, ghost button borders, link colors, input fields - the only neutral light tone in the palette

- Denim Ink `--font-denim-ink` for All interface text - from tiny labels to massive display headlines. The custom geometric face is the voice of the brand; weight 400 covers body and body-large, 600 for subheadings and emphasized inline, 700 reserved for the largest display moments. Extreme size jumps (40 64 86 94) create a poster-like hierarchy where the largest text dwarfs everything else on the page.
- Courier New `--font-courier-new` for Tiny monospaced labels (8px) for micro-annotations, likely near icons or status indicators. Ultra-tight tracking (-0.14em) at this size reads as a decorative tech-glitch element rather than readable text.

## Avoid

- Never use #bdff00 as a large background outside of one featured decorative panel per page - rationing lime is what makes it feel like a signal.
- Do not introduce drop shadows for elevation; the system separates layers through color tier shifts, not shadow depth.
- Do not use gray (#808080, #999, etc.) for any UI element - the palette is green-monochrome plus white and lime only.
- Never set body text below 16px except for the 8px Courier New micro-labels - legibility is non-negotiable.
- Do not mix multiple accent greens (#73a303, #586740) into the same component - one accent per surface keeps the hierarchy clean.
- Do not add gradients - the design relies on flat color blocks for its terminal/phosphor aesthetic.
- Do not use heavy font weights below 32px - Denim Ink at weight 700 in body sizes destroys readability; reserve 700 for display moments only.

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
