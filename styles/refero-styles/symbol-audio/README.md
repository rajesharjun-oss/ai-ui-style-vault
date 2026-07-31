# Symbol Audio

Source: [Refero Style](https://styles.refero.design/style/3b742f76-25ad-446c-a942-09b09b93f6a3)
Reference site: [https://www.symbolaudio.com](https://www.symbolaudio.com)
Captured: 2026-07-31
Refero published: 2026-04-30T01:30:04.547Z
Refero modified: 2026-06-05T11:35:07.878Z
Theme: dark
Category: E-commerce

## Style Summary

Explore Symbol Audio's dark E-commerce design system: Evergreen Gallery #1c3c27, Frost White #fffffd colors, Chalet-LondonSixty, Chalet-NewYorkSixty...

North star: midcentury listening room after dusk

## What To Borrow

- Evergreen Gallery `#1c3c27` for Green accent for outlined action borders, linked labels, and lightweight interactive emphasis. Do not promote it to the primary CTA color
- Frost White `#fffffd` for Product card surfaces, text on dark sections - slightly warm off-white, never pure #fff
- Pewter Mist `#dfe2e5` for Hairline borders, card outlines, divider rules, ghost-button borders on light cards
- Onyx `#000000` for Primary text on light cards, icon strokes, high-contrast detail
- Bone `#fffcda` for Alternate warm cream surface - contrast-pair companion to dark text on light cards
- Ink Shadow `#0e1e14` for Deepest text on evergreen, near-black with green undertone - pairs with frost-white for AAA contrast
- Marquee Cobalt `#447cf0` for Violet outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color
- Ember Lacquer `#c72a00` for Vivid red-orange seen in product photography (lacquered shelf units) - decorative, not functional

- Chalet-LondonSixty `--font-chalet-londonsixty` for Primary body and UI typeface - all nav links, product names, prices, badge text, footer copy, button labels. A custom rounded serif with distinctive ball terminals; its single weight is used universally
- Chalet-NewYorkSixty `--font-chalet-newyorksixty` for Secondary serif variant for body and link micro-copy - visually similar to LondonSixty but used in narrower contexts (small body, secondary links)
- SupremeLL-Bold `--font-supremell-bold` for Display and heading typeface - exclusively carries section headings ("What's on: Bestsellers..."), the hero wordmark, and large UI moments. A sharp geometric sans that cuts against the serif body type. The massive 80px size with -0.02em tracking is the signature move
- SupremeLL-BoldFlat `--font-supremell-boldflat` for Flat-cut variant of the display sans for inline link emphasis within body copy

## Avoid

- Do not introduce a filled solid-color button - this system only uses outlined/ghost actions on transparent fills.
- Do not use the blue (#447cf0) or red (#c72a00) as functional UI colors - they are decorative photography accents only.
- Do not apply border-radius to product cards or hero images - the system is sharp-edged everywhere except pills and badges.
- Do not set body text in SupremeLL-Bold - the sans is exclusively for display and headings.
- Do not add box-shadow or drop-shadow to cards or images - surfaces are flat, the contrast comes from color, not elevation.
- Do not use pure #ffffff for surfaces or text - the system runs #fffffd (frost) and #dfe2e5 (pewter) for its lightest tones.
- Do not break the marquee pattern - the announcement ticker is always present, always fixed, always evergreen-on-pewter.

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
