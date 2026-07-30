# Fiasco

Source: [Refero Style](https://styles.refero.design/style/ef73c742-1c3b-48b9-a174-de365ecc4691)
Reference site: [https://fiasco.design](https://fiasco.design)
Captured: 2026-07-30
Refero published: 2026-04-30T00:27:41.225Z
Refero modified: 2026-06-05T12:34:07.619Z
Theme: light
Category: Agency

## Style Summary

Explore Fiasco's light Agency design system: Canvas Cream #f8f9f3, Ink Black #1d1e19 colors, area-normal, HAL Timezone typography, and DESIGN.md for AI agents.

North star: "editorial gallery on cream paper" - warm off-white canvas with confident black type and single-color project cards.

## What To Borrow

- Canvas Cream `#f8f9f3` for Page background, button borders, soft surface
- Ink Black `#1d1e19` for Primary text, nav borders, link borders, all structural outlines
- Stone Mist `#e9eae2` for Nav borders, icon strokes, subtle dividers, secondary borders
- Shadow Stone `#d0d1cc` for Card and hero box-shadow base, low-contrast elevation
- Carbon `#151612` for Footer background, deep surface for dark sections
- Pewter `#686e77` for Input border, muted form fields
- Sulfur Yellow `#fff714` for Featured project card fill, callout blocks - the loudest accent, reserved for hero-grade emphasis
- Carnation Pink `#fbc2d1` for Project card background, soft accent block
- Sky Blue `#84bdff` for Project card background, cool accent block
- Ember Orange `#fd6b01` for Project card background, warm accent block
- Cobalt Violet `#204ce5` for Filled button background - the only chromatic action in the system, used sparingly
- Midnight `#112337` for Input text, deep navy utility for form labels
- Lichen Green `#03ac47` for Project card background, rare accent block

- area-normal `--font-area-normal` for Primary workhorse - body, UI labels, buttons, inputs, project titles. Wide weight range lets it carry both fine 14px body copy and 80px display headlines without leaving the family.
- HAL Timezone `--font-hal-timezone` for Nav labels, small caps treatments, secondary headings. The 100-weight gives nav items a thin, almost editorial feel that contrasts with the bolder body sans.
- Gooper `--font-gooper` for Display and editorial headlines with personality - used for large pull-quotes, italic-feeling treatments, and section titles. The tight 0.8 line-height at 40px gives headlines a compressed, magazine-like density.
- OC Highway `--font-oc-highway` for Micro-labels and tracked-out uppercase tags (e.g. '01:27 UK' timestamp). The +0.10em tracking makes 10px text readable as a label.

## Avoid

- Don't use the chromatic accent palette for buttons, nav, or text - they belong only to project card backgrounds
- Don't mix multiple vivid colors on the same card or section - one color field per surface
- Don't introduce pure black (#000000) as a fill - Ink Black (#1d1e19) is the system black, the tiny warm shift is the difference
- Don't use more than one shadow tier per page level - the heavy shadow is for cards/hero, the faint one for inputs, nothing else
- Don't set body text below 18px - the system is editorial, not data-dense
- Don't use Cobalt Violet (#204ce5) for anything other than a single filled primary action - it's the system's only chromatic action and overuse flattens its meaning
- Don't round inputs at 8px - the 3px input radius creates a deliberate contrast with the pill buttons and is part of the system language

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
