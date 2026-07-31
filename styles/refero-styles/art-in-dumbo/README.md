# Art In DUMBO

Source: [Refero Style](https://styles.refero.design/style/5d79f0c2-526e-4c37-b780-08404f60839b)
Reference site: [https://artindumbo.com](https://artindumbo.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:44:59.120Z
Refero modified: 2026-06-05T11:17:35.754Z
Theme: light
Category: Agency

## Style Summary

Explore Art In DUMBO's light Agency design system: Carbon #000000, Paper #ffffff colors, Helvetica Neue, Roboto typography, and DESIGN.md for AI agents.

North star: gallery broadside on raw paper

## What To Borrow

- Carbon `#000000` for Primary text, logo cells, hairline dividers between list rows, icon strokes - the only ink in the system
- Paper `#ffffff` for Page canvas, card surfaces, pill-button fills, inverse text on dark cells
- Plaster `#f1f2f2` for Input fields, secondary surfaces, subtle button hovers
- Linen `#e5e3df` for Warm off-white section backgrounds, large quiet surfaces that break the white without going gray
- Ash `#bdbdbd` for Medium-contrast borders, control outlines, and structural separators
- Graphite `#828282` for Button borders and label text for secondary controls
- Smoke `#b3b3b3` for Shadow base tone for the single ambient drop-shadow pattern
- Sage `#71cc98` for Green action color for filled buttons, selected navigation states, and focused conversion moments
- Ember `#ff7f41` for Orange outline accent for tags, dividers, and focused UI edges. Use as a supporting accent, not as a status color

- Helvetica Neue `--font-helvetica-neue` for Sole typeface across the entire system - display, body, nav, labels. Weight 500 is the only weight used; this medium-only commitment is the signature: not bold, not regular, never thin. Sizes run from 10px captions to 68px display with tight 1.05-1.15 line-heights at the top of the scale and 1.40-1.80 at body sizes.
- Roboto `--font-roboto` for Secondary system fallback for micro-labels and small UI chrome where a different metric helps

## Avoid

- Do not add colored panels, gradient fills, or decorative cards behind text
- Do not introduce new typefaces or weight values beyond Helvetica 500 and the Roboto micro-label fallback
- Do not use shadows to separate sections - use 1px black hairlines or a shift to #e5e3df Linen
- Do not round the hero photograph or exhibition thumbnails beyond 4px
- Do not stack more than two type sizes in a single row of the exhibitions list
- Do not place sage green text on the sage pill background - it must remain #000000
- Do not center body paragraphs or exhibition row content; left-align everything

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
