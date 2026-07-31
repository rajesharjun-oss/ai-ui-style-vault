# NEVERHACK

Source: [Refero Style](https://styles.refero.design/style/05a82625-786e-4343-a554-3ba8f4de23d7)
Reference site: [https://neverhack.com/en](https://neverhack.com/en)
Captured: 2026-07-31
Refero published: 2026-05-10T22:02:52.534Z
Refero modified: 2026-06-05T08:41:30.590Z
Theme: light
Category: SaaS

## Style Summary

Explore NEVERHACK's light SaaS design system: Sovereign Ink #0a0f1f, Signal White #ffffff colors, Roobert typography, and DESIGN.md for AI agents.

North star: encrypted command terminal on cold marble

## What To Borrow

- Sovereign Ink `#0a0f1f` for Primary text, headlines, nav, core UI - near-black with a barely-perceptible blue cast that separates it from pure black and lets violet accents feel native
- Signal White `#ffffff` for Card surfaces, elevated panels, button text on dark fills
- Mist Surface `#f6f7fc` for Page canvas, soft card backgrounds, subtle wash sections
- Cool Hairline `#e5e7eb` for Borders, dividers, input outlines, structural separators - the single neutral that holds the whole UI together
- Shadow Lichen `#d8d7e2` for Card inset shadow tint, quiet elevation layer
- Carbon Gray `#4e4e4e` for Secondary text, supporting copy, muted labels
- Ash Gray `#999999` for Button shadow tint, disabled affordances, tertiary text
- Violet Wash `#afa9fd` for Tinted backgrounds for AI-adjacent surfaces, soft highlight washes, capability tags
- Cyber Cyan `#28d3fe` for Blue wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Crimson Glow `#f4baba` for Red supporting accent for decorative details and low-frequency emphasis. Use as a supporting accent, not as a status color
- Info Blue `#2563eb` for Informational badges, neutral data callouts, non-critical status indicators

- Roobert `--font-roobert` for Single-family system. Roobert's geometric-humanist forms handle the full scale from 11px micro-labels to 72px display headlines. The custom face's slightly condensed proportions and subtle stroke contrast make headlines feel like terminal readouts rather than marketing copy. Weight 400 carries most UI; weight 500 is reserved for nav items, button labels, and emphasis. Letter-spacing tightens aggressively as size grows: -0.03em at 72px down to neutral at body sizes; micro-labels and ALL-CAPS badges open up to +0.08-0.12em for legibility

## Avoid

- Don't use Alert Crimson for non-critical actions, marketing copy, or decorative emphasis - it loses meaning through overuse
- Don't pair Sovereign Violet with Alert Crimson in the same component - the two chromatic accents must stay in separate semantic lanes
- Don't add shadows to text, icons, or small UI elements - elevation belongs only on cards, chat surfaces, and the primary CTA
- Don't use 72px or 52px display sizes for sub-headings or section intros - those are hero-only; step down to 32-40px for section openers
- Don't introduce new chromatic colors beyond the defined palette - the 5% colorfulness is the brand contract
- Don't use pure black (#000000) for body text - Sovereign Ink (#0a0f1f) is the only acceptable text color; black is reserved for nav border accents and button micro-details
- Don't apply soft radius (6-14px) to buttons or interactive controls - only cards, inputs, and nested elements use measured radii

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
