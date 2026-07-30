# Apple (Espana)

Source: [Refero Style](https://styles.refero.design/style/a48ef430-8c6a-42d8-8c53-ab7bb43cf33b)
Reference site: [https://www.apple.com/ipad-air](https://www.apple.com/ipad-air)
Captured: 2026-07-30
Refero published: 2026-04-01T18:00:11.000Z
Refero modified: 2026-07-03T11:06:39.174Z
Theme: light
Category: E-commerce

## Style Summary

Explore Apple (Espana)'s light E-commerce design system: Pure White #ffffff, Fog Mist #f3f6f6 colors, SF Pro Text, SF Pro Display typography, and DESIGN.md...

North star: white gallery vitrine

## What To Borrow

- Pure White `#ffffff` for Page canvas, card surfaces, nav background, icon fills
- Fog Mist `#f3f6f6` for Footer surface, secondary card tint, alternating section backgrounds
- Paper Gray `#fafafc` for Opened nav menu surface - barely-distinguished from white canvas
- Silver Smoke `#e8e8ed` for Tertiary surface, subtle dividers, chip backgrounds
- Ash Border `#dedfe2` for Hairline separators, disabled button backgrounds
- Graphite `#6e6e73` for Secondary body text, captions, helper labels
- Charcoal `#444545` for Nav text, secondary nav and link text
- Steel `#313131` for Nav icon fills, button text on light surfaces, dark surface tint
- Near Black `#1d1d1f` for Headlines, primary body text, all editorial copy - the dominant ink
- True Black `#000000` for Icon fills, input underline, maximum-emphasis headings
- Apple Blue `#0071e3` for Primary action fill - the only chromatic button color, also nav hover and focus ring
- Link Blue `#0066cc` for Inline text link color, secondary link accent
- Ember `#b64400` for Orange state accent for badges, validation surfaces, and short status labels.

- SF Pro Text `--font-sf-pro-text` for Body, navigation, micro-copy, and smaller headings. 17px/400 for primary body (line-height 1.47), 14px/600 for eyebrow labels and small link lists, 12px/400 for legal and fine print, 44px/400 for nav bar text, 34px/600 for card sub-headings.
- SF Pro Display `--font-sf-pro-display` for Display and editorial headlines - 80px hero, 56px section opener, 48px feature, 28px sub-feature, 21px large body. Negative letter-spacing tightens as size increases (-0.015em at 80px down to 0.011em at 21px). The only family used at sizes 40px.
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI

## Avoid

- Do not use any chromatic color other than #0071e3 for buttons - no orange, green, or red CTAs.
- Do not add borders or drop-shadows to cards; separation must come from surface tint or whitespace alone.
- Do not use sans-serif weights below 400 or decorative typefaces; the system is two families (SF Pro Display, SF Pro Text) only.
- Do not place two filled buttons in the same row - pair a single filled button with a text-link or an outlined pill.
- Do not use letter-spacing wider than 0.011em on any size; the system is always tight or normal tracking.
- Do not introduce background colors other than #ffffff, #fafafc, #f3f6f6, and #e8e8ed for surfaces.
- Do not use radius values other than 12px (small), 28px (card), 32px (nav pill), or 980px+ (full pill) - no 4px or 8px rounded corners.

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
