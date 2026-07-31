# Zipline

Source: [Refero Style](https://styles.refero.design/style/4a248569-2b5a-4416-bb2a-c78890218b9f)
Reference site: [https://www.zipline.com](https://www.zipline.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:39:56.920Z
Refero modified: 2026-06-05T07:39:05.947Z
Theme: light
Category: Other

## Style Summary

Explore Zipline's light Other design system: Meadow Cream #f7f4e8, Hillside Ink #000000 colors, fkGroteskNeue, fkScreamer typography, and DESIGN.md for AI...

North star: open meadow in morning light

## What To Borrow

- Meadow Cream `#f7f4e8` for Page canvas, card surfaces, body text inverse, button borders - the warm off-white that gives the whole system its outdoor, paper-like character instead of clinical SaaS white
- Hillside Ink `#000000` for Primary headings, body copy, icon strokes, filled action buttons, hairline borders - maximum-contrast black that lets the cream breathe and makes fkScreamer headlines land
- Stone Border `#c6c3ba` for Muted dividers, secondary surfaces, low-contrast borders - warm gray that sits a step behind Meadow Cream and prevents the canvas from looking flat
- Drone Violet `#643aed` for Card and feature-block backgrounds, accent surfaces - the single chromatic note in an otherwise achromatic system; vivid against the cream so attention-grabbing blocks pop without breaking the editorial mood

- fkGroteskNeue `--font-fkgroteskneue` for Body copy, navigation, buttons, captions, and any text smaller than the display headlines - the workhorse grotesque that handles all functional UI at 14-22px. The consistent -0.01em tracking keeps it tight even at small sizes.
- fkScreamer `--font-fkscreamer` for Signature display face - used only for oversized editorial statements (40-150px). This is the voice of the brand: ultra-heavy, aggressively condensed, line-height 0.85 so the letters nearly touch. The restraint of using one weight at one role makes the moments it appears feel like magazine pull-quotes, not just headings.
- fkDisplay `--font-fkdisplay` for Mid-weight display variant for sub-statements that need fkScreamer's character at a smaller scale - bridges the gap between the massive editorial type and fkGroteskNeue body

## Avoid

- Don't use fkScreamer for body copy, navigation, captions, or anything under 40px - the weight and line-height collapse at small sizes
- Don't introduce additional chromatic accent colors; the entire system's restraint depends on having exactly one violet
- Don't add box-shadows to cards or buttons - use 1px borders or the violet surface for separation instead
- Don't use pure white (#ffffff) as a background; Meadow Cream is the canvas and stark white breaks the warm editorial tone
- Don't set body type at anything other than fkGroteskNeue 16px/1.4 as the default - resist the urge to mix in a serif or secondary sans
- Don't apply radii smaller than 20px to interactive elements; buttons, cards, and images all share the same generous rounding
- Don't use letter-spacing on fkScreamer - it ships with normal tracking and the tight glyph spacing is part of its impact

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
