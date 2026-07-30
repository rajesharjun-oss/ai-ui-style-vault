# 099 SUPPLY

Source: [Refero Style](https://styles.refero.design/style/e4a7b5f3-f393-4f6d-b4a5-ecf874024bed)
Reference site: [https://099.supply](https://099.supply)
Captured: 2026-07-30
Refero published: 2026-03-09T13:13:07.000Z
Refero modified: 2026-07-03T11:22:28.077Z
Theme: light
Category: Design

## Style Summary

Explore 099 SUPPLY's light Design design system: Canvas White #ffffff, Ink #101010 colors, Soehne Mono typography, and DESIGN.md for AI agents.

North star: Gallery wall of black-on-white objects

## What To Borrow

- Canvas White `#ffffff` for Page background, card surfaces, button backgrounds, link containers - the gallery wall everything sits on
- Ink `#101010` for Primary headings, body text, and icon fills on light surfaces. Do not promote it to the primary CTA color
- Charcoal `#000000` for Pure-black decorative fills for mockup rendering and high-contrast object silhouettes
- Muted Hard `#222222` for Dark surface tint for elevated dark components and modal/overlay backgrounds; Dark surface fill for elevated panels, toggle/loader component backgrounds
- Muted `#555555` for Secondary body text, supporting copy, muted helper labels
- Muted Soft `#999999` for Section headings, icon fills, badge text, hover border state - the softest readable gray
- Border Soft `#c8c8c8` for Soft hairline borders for less prominent dividers and input outlines
- Border Subtle `#e0e0e0` for Card edges, link borders, subtle dividers between tiles - the dominant hairline color

- Soehne Mono `--font-soehne-mono` for The exclusive typeface - used for every heading, body, badge, link, icon, and label. Weight 400 dominates; weight 500 is reserved for the 26px hero label. All non-body sizes render in uppercase with tracking between 0.02em and 0.18em. The monospaced face reinforces the museum-catalog, specimen-tag atmosphere.

## Avoid

- Never introduce chromatic color - no blues, greens, reds, or any hue. The system is monochrome.
- Never apply box-shadow, drop-shadow, or any elevation effect. Depth comes from hairline borders only.
- Never use a sans-serif or proportional typeface. Mono is non-negotiable.
- Never use background gradients except for the single conic-gradient loader pattern (#101010 #c8c8c8).
- Never set border-radius below 4px on cards or above 9999px on buttons - the radius vocabulary is fixed.
- Never use bold (600+) or light (300-) weights. Stay at 400, with 500 reserved for the 26px section heading.
- Never mix section heading style - always 26px uppercase #999999 with 0.18em tracking, nothing decorative.

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
