# Aaron Poe

Source: [Refero Style](https://styles.refero.design/style/3240fdc0-ffea-4054-a996-a5f6b942eff0)
Reference site: [https://aaronpoeandco.com](https://aaronpoeandco.com)
Captured: 2026-07-31
Refero published: 2026-05-08T19:19:14.637Z
Refero modified: 2026-06-05T11:10:02.434Z
Theme: light
Category: Agency

## Style Summary

Explore Aaron Poe

North star: Quiet white gallery - coral pink whispers float in vast considered silence, framed only by pill-shaped nav and tightly-tracked type.

## What To Borrow

- Coral Rose `#ea587d` for Accent for heading text, hairline borders, and active-state markers - the single chromatic signal in an otherwise achromatic system
- Pure White `#ffffff` for Page canvas, card surfaces, and inverted backgrounds
- Cloud `#f2f2f2` for Pill nav background, subtle surface elevation, and inset border shadows
- Bone `#d9d8d4` for Warm-toned secondary surface tint for alternating bands
- Char `#282828` for Primary text, body copy, and most interface strokes
- Ink `#121212` for Heavier headings, body text, and prominent borders
- Black `#000000` for Maximum-emphasis text, logo wordmark, and strong border lines
- Fog `#b3b3b3` for Muted helper text and disabled-state strokes
- Mist `#cccccc` for Lowest-emphasis borders and decorative dividers

- -apple-system `--font-apple-system` for System-font fallback for body text and rendering across platforms. Used wherever native OS fonts provide a reliable, performance-optimized default at body size.
- Geist `--font-geist` for Primary display and UI typeface. The 300 weight at micro sizes (8-10px) creates whisper-quiet labels; the negative letter-spacing (-0.056em at 8px, -0.037em at 10px) tightens small type into dense, confident blocks. 400 at 16-18px serves body and subheadings with -0.025em to -0.011em tracking.
- wtqc (custom display) `--font-wtqc-custom-display` for Reserved for prominent display headings (30px, 1.07 line-height, -0.033em tracking) and compact labels (12px, 1.33 line-height). The tight 1.07 line-height on the 30px size gives headings a condensed, editorial feel.
- custom_166638 `--font-custom166638` for custom_166638 - detected in extracted data but not described by AI

## Avoid

- Do not add drop shadows to cards, buttons, or navigation - the system is intentionally flat
- Do not use #ea587d as a button background fill - the accent only appears on headings and borders
- Do not use large border-radii on cards - keep them at 4px; only the pill nav gets 24px
- Do not introduce new chromatic colors - the system is deliberately monochrome with one pink accent
- Do not use positive letter-spacing - all text tracks tight (negative values) to feel compressed and confident
- Do not fill the page with imagery or illustrations - let typography and whitespace carry the composition
- Do not use dark mode as the default theme - white canvas is the signature; dark (#121212) is reserved for inverted sections only

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
