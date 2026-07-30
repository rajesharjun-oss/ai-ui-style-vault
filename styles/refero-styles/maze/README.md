# Maze

Source: [Refero Style](https://styles.refero.design/style/966a03d5-13e9-48d8-9b01-28e6ae3f3967)
Reference site: [https://maze.co](https://maze.co)
Captured: 2026-07-30
Refero published: 2026-04-30T00:17:33.174Z
Refero modified: 2026-06-05T12:50:07.578Z
Theme: light
Category: SaaS

## Style Summary

Explore Maze's light SaaS design system: Bone #f5f4f0, Paper #ffffff colors, ui-sans-serif, Phonic typography, and DESIGN.md for AI agents.

North star: Editorial research journal - warm bone paper, serif ink, chartreuse highlighter

## What To Borrow

- Bone `#f5f4f0` for Page canvas, footer, secondary button fills - warm off-white replaces cold digital white, giving every screen a paper-like base
- Paper `#ffffff` for Card surfaces, elevated panels, input fields - the bright layer above bone
- Ink `#1c1c1c` for Primary text, dark filled buttons, heading color - the default ink, warm near-black rather than #000
- Charcoal `#000000` for Hairline borders, icon strokes, the announcement bar - the thinnest line work
- Fossil `#706f6c` for Secondary text, muted borders, body annotations
- Pebble `#9e9b94` for Input field borders, disabled controls
- Smoke `#3c3c3c` for Body annotations, meta labels
- Sand `#eae6e1` for Active tab background, subtle surface lift, button hover on bone
- Ash `#d2cec6` for Hairline dividers, footer borders, low-contrast separators
- Chartreuse `#dbf570` for Highlight badges, study tags, the globe motif, card accent fills - the only chromatic note in the system, used sparingly to draw the eye to research signals
- Olive `#4b5b0a` for Decorative border accent, chromatic link underline - the only deep color, appears in the olive outline treatments and the heading underline on the hero

- ui-sans-serif `--font-ui-sans-serif` for ui-sans-serif - detected in extracted data but not described by AI
- Phonic `--font-phonic` for Display, headings, body - the brand's signature humanist serif set aggressively tight at large sizes (-0.09em at 130px down to +0.03em at 12px). Weight 300 dominates for display, 400 for body. The custom typeface carries the editorial voice; weight 300 at 130px is the signature move - most brands use 600-700 here, Maze whispers in a light serif to claim authority through restraint.
- System UI Sans `--font-system-ui-sans` for Secondary UI text, fallback for browser contexts - only used sparingly; Phonic carries the brand

## Avoid

- Do not use sans-serif for headlines - Phonic serif at weight 300 IS the brand voice; substituting bold sans-serif destroys the editorial register
- Do not apply heavy box-shadows to cards - the system is intentionally flat, elevation is a hairlines-only discipline
- Do not use Chartreuse as a CTA background - it is a highlight color for tags and motifs, not an action color; Ink stays the action
- Do not set display text at line-height 1.4+ - headlines run tight (1.00-1.10) so the serif rhythm stays architectural
- Do not introduce new chromatic colors beyond the three in the palette (Chartreuse, Olive, Lavender) - every additional hue dilutes the bone-paper system
- Do not use #000000 as body text - Ink (#1c1c1c) is the text color; #000 is reserved for the announcement bar and hairline borders
- Do not center body paragraphs in cards - only section headlines and hero copy may center; study card copy stays left-aligned

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
