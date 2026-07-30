# Titan

Source: [Refero Style](https://styles.refero.design/style/964b9215-396b-492c-abec-7bd778d7b1c9)
Reference site: [https://www.titan.com](https://www.titan.com)
Captured: 2026-07-30
Refero published: 2026-04-30T00:20:19.588Z
Refero modified: 2026-07-03T10:48:26.652Z
Theme: light
Category: Fintech

## Style Summary

Explore Titan's light Fintech design system: Ink #111111, Pure White #ffffff colors, Geist, Geist Mono typography, and DESIGN.md for AI agents.

North star: warm-toned monochrome archive

## What To Borrow

- Ink `#111111` for Primary text, filled button background, icon strokes - near-black ink that carries the entire brand identity. The slight softness vs pure #000 keeps it from feeling sterile
- Pure White `#ffffff` for Page canvas, card surfaces, button text - the dominant light field the entire interface sits on
- Mist Border `#e9eaeb` for Primary hairline borders, nav pill background, structural dividers - cool gray that defines edges and containers without competing with content
- Cream Surface `#f3efeb` for Warm card and section surfaces - the warm signature tone that gives the system its editorial, paper-like quality against the cool white canvas
- Tan Divider `#d8d3cc` for Secondary borders on warm surfaces, subtle background washes - extends the cream warmth into the border layer
- Warm Subtle `#615e5b` for Muted helper text, secondary copy - warm gray that recedes on cream surfaces while staying readable on white
- Mid Gray `#888888` for Tertiary text and disabled states - only when even Warm Subtle is too prominent
- Pure Black `#000000` for Rare SVG fills and graphic accents - used sparingly where absolute black is required
- Obsidian `#1e1e1d` for Footer background, dark section inversions - the only dark surface in the system, creating a terminal moment at page bottom

- Geist `--font-geist` for Primary interface and headline typeface - used at weight 500 (not 700) for all headings, a deliberate restraint that gives headlines editorial weight without shouting. Variable substitute: Inter.
- Geist Mono `--font-geist-mono` for Numerical stats, metadata, small labels - reserved for figures like $1.2B, 10,000+, 2017 where monospaced digits create an editorial financial-journalism quality. Variable substitute: JetBrains Mono.

## Avoid

- Do not use weight 600 or 700 for headings - weight 500 at large sizes with tight tracking is the system's voice
- Do not add box-shadow, gradients, or any form of elevation - depth comes from surface color contrast only
- Do not introduce blue, green, or any chromatic accent - the 0% colorfulness is intentional
- Do not use sharp corners (0-8px radius) on buttons or cards - the pill (160px) and large-rounded (32px) geometry is mandatory
- Do not center body text - left-align all paragraphs, descriptions, and feature lists
- Do not use pure #000000 for body text or button backgrounds - use #111111 for a softer near-black
- Do not place dark cards on light backgrounds outside the footer - the Obsidian #1e1e1d inversion is reserved for terminal page sections only

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
