# Swap

Source: [Refero Style](https://styles.refero.design/style/15d10d6c-1844-46c6-ae69-c99a56e6ad41)
Reference site: [https://www.swap-commerce.com](https://www.swap-commerce.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:19:58.237Z
Refero modified: 2026-06-05T08:40:40.898Z
Theme: light
Category: E-commerce

## Style Summary

Explore Swap's light E-commerce design system: Mint Wash #f2ffe3, Vivid Lime #a3fda7 colors, mainFont, Custom Editorial Serif (swap-serif) typography, and...

North star: Mint editorial greenhouse - pale sage rooms with vivid lime accents and whisper-weight serif type.

## What To Borrow

- Mint Wash `#f2ffe3` for Page canvas, section backgrounds, hero wash - the dominant surface tone
- Forest Depth `#0d5b3b` for Deep green card backgrounds, contrast surfaces, gradient anchor
- Pine Shadow `#083a26` for Darkest green for emphasis cards, gradient endpoints, high-contrast text on light surfaces
- Spring Gradient Start `#82ff87` for Gradient anchor for display type and decorative washes
- Citrus Gradient End `#deff82` for Gradient endpoint for display type - yellow-green warmth in hero text
- Charcoal Ink `#000000` for Primary text, hairline borders, dark action buttons, icon strokes
- Cream Paper `#ffffff` for Card surfaces, button text on dark fills, input backgrounds, elevated overlays
- Stone Charcoal `#2d3637` for Secondary dark surface, icon fills, dark borders, muted dark mode text
- Warm Mist `#e9e7e2` for Alternate section backgrounds, disabled states, cream-toned surfaces
- Silver Border `#cccccc` for Light dividers, inactive borders, subtle separators
- Sage Gray `#838676` for Muted accent card backgrounds, secondary decorative surfaces
- Eucalyptus `#9cb0a8` for Muted sage for outlined secondary action borders, subtle green-tinted UI

- mainFont `--font-mainfont` for mainFont - detected in extracted data but not described by AI
- Custom Editorial Serif (swap-serif) `--font-custom-editorial-serif-swap-serif` for Display and headline serif - used exclusively for hero/headline contexts at 72-120px. Weight 100 for maximum impact headlines, weight 300 for sub-headlines. Negative letter-spacing (-0.017em) tightens the high-contrast strokes for fashion-editorial density. This ultra-thin serif against pale mint is the signature combination - it borrows from luxury print typography (Bodoni/Didone lineage) to make a commerce platform feel like a magazine spread.
- Custom UI Sans (swap-sans) `--font-custom-ui-sans-swap-sans` for Primary interface and body typeface - 16px for body, 15px for compact UI, 18px for lead paragraphs, 24px and 30px for section sub-headings. Weight 400 is default, 500 for emphasis, 700 for labels and small caps eyebrow text. Slight negative tracking (-0.01em) tightens the geometric forms for a precise, modern feel. The sans is functional and quiet - it never competes with the display serif.
- secondaryFont `--font-secondaryfont` for secondaryFont - detected in extracted data but not described by AI

## Avoid

- Never use bold or semibold weights for display headlines - the ultra-thin serif is the brand signature
- Never use sharp or small border-radii on buttons - anything below 100px breaks the pill language
- Never apply the green-to-citrus gradient to body text, UI labels, or anything below 48px
- Never use a dark or charcoal page background - the entire system is built on pale mint and white
- Never use colored body text - all paragraph and UI copy stays in black (#000000) or charcoal (#2d3637)
- Never add heavy drop shadows - the only shadow allowed is the 28px soft black-9% blur on cards
- Never use multiple chromatic accent colors simultaneously - lime is the sole accent; sage gray and forest green appear only in gradients or specific card contexts

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
