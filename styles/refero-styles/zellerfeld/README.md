# Zellerfeld

Source: [Refero Style](https://styles.refero.design/style/a6efcd16-dcd8-435b-9bd6-8c590589b424)
Reference site: [https://www.zellerfeld.com](https://www.zellerfeld.com)
Captured: 2026-07-30
Refero published: 2026-04-30T00:19:24.463Z
Refero modified: 2026-07-03T15:47:43.879Z
Theme: light
Category: E-commerce

## Style Summary

Explore Zellerfeld's light E-commerce design system: Electric Cobalt #000aff, Pale Iris #e5e7ff colors, Roobert, Space Mono typography, and DESIGN.md for AI...

North star: Sculptor's atelier on white marble - monolithic plinth surfaces, single cobalt spark, lowercase whispers from floor to ceiling.

## What To Borrow

- Electric Cobalt `#000aff` for New In badges, active nav pill, current-slide indicator, claim moments - the only chromatic signal in the system, used sparingly so it reads as activation not decoration
- Pale Iris `#e5e7ff` for New Color badge fill, soft highlight wash, tinted surface for variant callouts - a desaturated ghost of the cobalt that whispers color without breaking the monochrome regime
- Ink Black `#111111` for Primary text, default borders, icon strokes, hairline dividers - the dominant structural color across headings, lists, and links
- Pure White `#ffffff` for Neutral form states, badge text, and quiet UI feedback where color should stay understated. Do not promote it to the primary CTA color
- Plaster `#ecedee` for Secondary surface for product cards, nav bar background, soft elevation tier above the canvas
- Slate `#a1a4aa` for Card border tone, neutral button fill, muted button border - the gray that defines card edges without darkening them
- Fog `#d7d7d7` for Light card border, divider lines, inactive surface tint
- Graphite `#444955` for List and navigation borders, structural dividers between rows and cells
- Ash `#737780` for Secondary text, muted body copy, de-emphasized metadata, link rest state
- Charcoal `#3b3b3b` for Body text alternate, subtle dark surface for inset blocks

- Roobert `--font-roobert` for Primary brand typeface - used for everything from 13px body to 128px hero. The -0.04em tracking is consistent across all sizes, pulling the lowercase wordmark into a tight, sculpted mass. Weights escalate by context: 400 for body and UI, 500 for emphasized labels, 600 for product names, 700 for large display.
- Space Mono `--font-space-mono` for Technical metadata - prices ( 189,00), Top 10 rank numerals, ticker marks, shop name credits. Drops in where the page needs to feel like a spec sheet rather than marketing copy.
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI

## Avoid

- Don't introduce new chromatic colors beyond the single cobalt (#000aff) and its pale variant (#e5e7ff)
- Don't use drop shadows on product cards - the system relies on surface color stepping and 10px radius for separation
- Don't set type larger than 128px (display) or smaller than 12px (Space Mono micro labels)
- Don't use rounded radii other than 10px and 30px - no fully square corners, no fully circular elements
- Don't center body text or metadata; left-align all product information including the 'By {brand}' credit
- Don't apply color to icons - keep all line icons monochrome Ink (#111) at 1.5px stroke
- Don't separate badge variants by shape - all status badges share the 30px pill; differentiate by fill color only

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
