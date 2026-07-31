# INVERSA

Source: [Refero Style](https://styles.refero.design/style/8a6dc9c8-7892-4eab-baaa-3c342d5671f2)
Reference site: [https://inversa.com](https://inversa.com)
Captured: 2026-07-31
Refero published: 2026-04-06T19:02:17.000Z
Refero modified: 2026-06-05T09:33:17.290Z
Theme: dark
Category: Other

## Style Summary

Explore INVERSA's dark Other design system: Obsidian Loam #13140e, Bone Vellum #f4f3e8 colors, NB International Pro, JetBrains Mono typography, and...

North star: topographic field terminal at midnight. A dark command surface where massive editorial type and a single neon-lime marker layer over satellite earth photography, every label set in mono as if reading mission coordinates.

## What To Borrow

- Obsidian Loam `#13140e` for Page canvas, hero background, card surfaces - the near-black base with a faint olive cast that keeps the dark from feeling synthetic
- Bone Vellum `#f4f3e8` for Primary text, body copy, headings, icon strokes, border color on dark - warm off-white that reads as paper, not LCD white
- Iron Filings `#404040` for Hairline borders, footer dividers, low-emphasis rules
- Drift Ash `#84837b` for Muted secondary text, placeholder input state, low-contrast labels on light surfaces
- Lime Surveyor `#ebfc72` for Green supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Marsh Olive `#bacd31` for Gradient transition shade for the lime accent - deeper stop used in horizontal lime fades

- NB International Pro `--font-nb-international-pro` for Display and body - the brand's primary voice. Set at 72px for hero statements and 58px for section headers with -0.03em tracking, producing a compressed, editorial presence. Also carries body text at 18px (lh 1.62) and UI labels at 13-14px. Its humanist warmth prevents the dark canvas from feeling cold or corporate.
- JetBrains Mono `--font-jetbrains-mono` for Interface annotations, data labels, button text, tag values, and secondary display moments. The monospaced geometry reads as coordinates, timestamps, and telemetry - reinforcing the field-instrument metaphor. Set in weight 300 for hero-scale data callouts (65px) to keep mono from feeling mechanical at large sizes.

## Avoid

- Do not add box-shadows to any element - the system is deliberately flat; depth comes from color contrast, not elevation.
- Do not introduce a second accent color - the lime is alone by design. Any other chromatic addition dilutes the survey-marker effect.
- Do not set body text below 18px in NB International Pro - the font's humanist proportions require generous size to read correctly.
- Do not use #000000 as the canvas - the olive undertone of #13140 is what makes the dark feel organic rather than digital.
- Do not round corners beyond 3.6px on any component - larger radii would contradict the instrument-panel aesthetic.
- Do not use colored backgrounds for cards or content blocks - content sits directly on the dark canvas with no chrome.
- Do not center body text - editorial alignment is left-aligned throughout, matching the mission-log reading flow.

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
