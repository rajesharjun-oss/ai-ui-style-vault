# Getburnt

Source: [Refero Style](https://styles.refero.design/style/002cc5a7-0d34-4d8d-afa0-c5fad69477d5) 
Reference site: [https://www.getburnt.ai](https://www.getburnt.ai) 
Captured: 2026-07-29 
Refero published: 2026-05-11T00:39:14.982Z 
Refero modified: 2026-06-03T18:41:18.811Z 
Theme: light 
Category: AI

## Style Summary

Explore Getburnt's light AI design system: Ink #1a1a17, Paper #ffffff colors, Nyght Serif, Switzer typography, and DESIGN.md for AI agents.

North star: editorial monochrome on warm paper - a minimal typeset spread where warm-black ink, a light display serif, and pill-shaped controls turn a B2B tool into something that reads like a quarterly journal.

## What To Borrow

- Ink `#1a1a17` for Primary text, filled buttons, dark surface backgrounds, heading strokes - a warm-tinted near-black that replaces pure #000 throughout the system
- Paper `#ffffff` for Page canvas, card surfaces, light section backgrounds, button borders on dark surfaces
- Ash `#5f5f5d` for Secondary body text, helper text, muted borders, low-emphasis UI metadata

- Nyght Serif `--font-nyght-serif` for Reserved exclusively for display and heading levels (26-72px). Weight 300 is the signature: most systems reach for 600-700 serif, this whisper-weight creates editorial gravitas through restraint. Letter-spacing widens slightly at smaller sizes (0.03em) and tightens at display sizes (0.01em) to preserve optical balance.
- Switzer `--font-switzer` for Workhorse for nav, body, buttons, labels, card metadata, and small headings. Tracking runs consistently at 0.03em - a subtle positive letter-spacing that gives the grotesque a calm, considered cadence. Weight 500 for emphasis, 600 for button text and nav active states.

## Avoid

- Do not introduce blue, green, red, or any saturated brand color - the warmth comes from the near-black, not from accents
- Do not set Nyght Serif in weights other than 300 - adding bold or medium breaks the editorial voice
- Do not use square or 12px+ radii on buttons or tags - the pill shape is load-bearing
- Do not set body or heading text in pure #000000 - always use #1a1a17 for the warm-ink quality
- Do not use heavy drop shadows on cards - the system relies on hairline borders and surface contrast, not elevation
- Do not set line-height above 1.2 on Nyght Serif display sizes - the serif needs to sit tight to read as display, not body
- Do not apply gradients to text, buttons, or text containers - the palette is flat by design

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
