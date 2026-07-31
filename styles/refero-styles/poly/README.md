# Poly

Source: [Refero Style](https://styles.refero.design/style/d8e01e43-d260-4fa3-8f42-ae39e5c6ac84)
Reference site: [https://poly.app](https://poly.app)
Captured: 2026-07-31
Refero published: 2026-04-30T00:14:55.399Z
Refero modified: 2026-06-05T07:32:47.252Z
Theme: light
Category: SaaS

## Style Summary

Explore Poly's light SaaS design system: Ember Gradient #f42919, Porcelain #f4f4f4 colors, Haffer Variable, Bogue typography, and DESIGN.md for AI agents.

North star: Ember on porcelain - one warm gradient ember floating on an otherwise pure white editorial page, surrounded by quiet serif headlines and full-bleed photography.

## What To Borrow

- Ember Gradient `#f4824d` for Brand mark, Poly logo, the sole chromatic accent - warm orange fading to signal red, used only on identity, never on body UI
- Porcelain `#f4f4f4` for Page canvas, card surfaces, inverted text on dark photo backgrounds
- Onyx `#000000` for Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color
- Graphite `#292930` for Secondary text, hairline borders, icon fills, the slight warmth that keeps near-black from feeling clinical
- Ash `#cccccc` for Shadow tone used in the soft-etched link treatment, muted dividers

- Haffer Variable `--font-haffer-variable` for Primary display serif for headlines at 30-53px. Weight 450 is anti-convention - most product sites push display to 600-700, but Haffer at 450 keeps headlines warm and editorial rather than commanding. Activating liga and ss04 unlocks the alternative g and stylised letterforms that give the wordmark its personality.
- Bogue `--font-bogue` for Companion serif at regular weight, used for badge labels and secondary serif moments where Haffer 450 would feel too heavy. Tighter tracking at -0.03em distinguishes it from Haffer.
- Haffer `--font-haffer` for Static fallback for small serif text - 15px badges, 24px sub-serial moments
- Inter `--font-inter` for All UI, body, nav, button labels, helper text. Inter at 400 handles body, 600 carries subheadings and button text. The -0.02em tracking matches the serif family, keeping the type system visually unified.

## Avoid

- Don't introduce any chromatic color outside the Ember Gradient - the palette is monochrome by design
- Don't use drop shadows for card or surface elevation - borders carry separation
- Don't set display type in Inter; display belongs to Haffer at 450, never below 30px
- Don't use border-radius values other than 8px - no pills, no sharp corners, no 12px or 16px variants
- Don't apply the Ember Gradient to buttons, backgrounds, or hover states - it is brand-identity only
- Don't lighten Onyx text below #292930 for body copy - contrast must stay above 9:1 on Porcelain
- Don't break the photo/Porcelain alternation - every content section should sit on Porcelain, never on a tinted background

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
