# Grafik

Source: [Refero Style](https://styles.refero.design/style/0226e028-3cd3-440d-b469-ca459267161d)
Reference site: [https://grafik.co.nz](https://grafik.co.nz)
Captured: 2026-07-31
Refero published: 2026-04-30T01:50:01.460Z
Refero modified: 2026-06-05T07:35:42.413Z
Theme: light
Category: Agency

## Style Summary

Explore Grafik's light Agency design system: Bone #f0eeeb, Ink #000000 colors, Grotesk typography, and DESIGN.md for AI agents.

North star: Editorial gallery on warm paper. A design annual laid out as a full-bleed screen - typographic grid lines, monochrome photography, and nothing between the work and the page.

## What To Borrow

- Bone `#f0eeeb` for Page background and primary canvas - a warm off-white that reads as paper rather than screen, the defining surface of the entire system
- Ink `#000000` for Primary text, body copy, navigation, project metadata, 1px grid lines, image borders, and dark image treatments - the only non-canvas color
- Paper `#ffffff` for Card surfaces, image backgrounds, and reverse-text blocks - white inserts on the warm canvas to isolate portfolio pieces

- Grotesk `--font-grotesk` for Sole typeface across all UI - navigation, project metadata, and headlines. Used exclusively at weight 400 (no bold, no light), which is anti-convention for an agency portfolio; the regular weight whispers where competitors shout. Negative tracking tightens headlines at -0.02em while body sits at -0.005em, giving every line a printed-page density. The dlig feature enables discretionary ligatures for editorial flourish.

## Avoid

- Do not introduce a second typeface. Grotesk carries the entire system - adding a serif or display face fragments the editorial cohesion.
- Do not add box-shadows or any form of elevation. The design uses surface contrast and hairline borders, not depth.
- Do not use rounded corners on any element. Every edge is sharp - cards, images, buttons, tags.
- Do not use bright or saturated colors in the UI. The green and brown tones in screenshots are project content, not system tokens.
- Do not set the page background to pure #ffffff. The warm #f0eeeb canvas is the paper-like foundation - white-as-canvas looks clinical and breaks the design annual metaphor.
- Do not add decorative gradients, patterns, or background textures. The design is flat, monochromatic, and print-faithful.
- Do not use bold or semibold weights. The entire system runs on Grotesk 400 - adding weight breaks the measured, restrained voice.

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
