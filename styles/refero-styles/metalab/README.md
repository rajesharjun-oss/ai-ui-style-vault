# Metalab

Source: [Refero Style](https://styles.refero.design/style/da087e69-8832-418a-aa1b-42e1acabb39e)
Reference site: [https://metalab.com](https://metalab.com)
Captured: 2026-07-31
Refero published: 2026-03-01T09:00:16.000Z
Refero modified: 2026-06-05T09:11:09.014Z
Theme: dark
Category: Agency

## Style Summary

Explore Metalab's dark Agency design system: Void #000000, Bone #ffffff colors, Basis Grotesque Pro, PP Eiko typography, and DESIGN.md for AI agents.

North star: black editorial spread - a serif headline breathing in void, annotated by a whisper-quiet grotesque

## What To Borrow

- Void `#000000` for Page canvas, primary surface, heading text on light zones - the dominant black that absorbs all surrounding elements
- Bone `#ffffff` for Inverse text on dark surfaces, hairline borders on dark zones, contrast punctuation against the black canvas
- Charcoal `#252525` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color

- Basis Grotesque Pro `--font-basis-grotesque-pro` for All functional copy: body text, metadata annotations, labels, nav, buttons, lists. The 350 weight (light) handles editorial captioning at 12px - the small annotations like 'EST 2006', 'BC, CA', '12:32 EDT' - while 400 handles body and interactive text at 16px. Slight -0.01em tracking tightens the grotesque into a precise, measured voice. This font does the quiet work; the serif does the talking.
- PP Eiko `--font-pp-eiko` for Display headings only - the 88px ultra-light serif is the signature element. Weight 240 (near-hairline) is a dramatic anti-convention choice: most agencies use 400-500 serifs for authority; Metalab's whisper-weight communicates confidence through restraint, not volume. Tight 0.80 line-height and -0.02em tracking let letters nearly touch, creating a sculptural block of text.
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI

## Avoid

- Do not introduce any chromatic color - no blues, reds, greens, or brand accents. The system is achromatic by conviction
- Do not use PP Eiko at sizes below 40px - the weight 240 becomes too thin to render reliably at small sizes
- Do not add drop shadows to any element - depth in this system comes from surface value contrast (#000000 #252525), not elevation effects
- Do not use weight 600+ for any text - the entire system operates in the 240-400 range; heavier weights break the whisper-quiet tone
- Do not add gradients, glows, or any color effects - the flat achromatic palette is the brand identity
- Do not use system serif defaults (Times, Georgia) as substitutes for PP Eiko without matching the ultra-light weight - a regular-weight serif will read as conservative, not editorial
- Do not fill buttons with #ffffff on the dark canvas - it would create the only bright shape on the page and dominate the hierarchy. Use #252525 or transparent

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
