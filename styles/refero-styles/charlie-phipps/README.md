# Charlie Phipps

Source: [Refero Style](https://styles.refero.design/style/7f6799d9-0733-4523-9a94-036b9ad3bf28)
Reference site: [https://phippscharlie.com](https://phippscharlie.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:30:41.117Z
Refero modified: 2026-06-05T08:16:31.400Z
Theme: mixed
Category: Design

## Style Summary

Explore Charlie Phipps's mixed Design design system: Canvas Black #101011, Paper White #ffffff colors, Helvetica Neue, Times typography, and DESIGN.md for...

North star: oversized editorial gallery wall - a single massive Helvetica headline and one full-bleed photograph, nothing else

## What To Borrow

- Canvas Black `#101011` for Base page canvas beneath full-bleed photography and dark bands; primary text on light surfaces; link underlines in dark contexts
- Paper White `#ffffff` for Primary text color on dark/photographic backgrounds; content section background; dominant border color (hairline rules and dividers across the layout)
- Ink Black `#000000` for Heading and body text on light surfaces; second structural border color - used wherever a slightly harder edge than #101011 is needed
- Fog Gray `#ededed` for Subtle surface tint separating content blocks from white paper; soft borders on body text and cards where a pure white hairline would disappear
- Smoke Gray `#bab7b2` for Muted heading accent - used for secondary headings and borders where the hierarchy needs to recede below the primary type
- Ash Gray `#888888` for Body text metadata, link underlines in light contexts, and mid-weight borders - the workhorse neutral for anything that should be seen but not foregrounded
- Charcoal `#262627` for Deepest secondary border and muted text on light sections - just one step lighter than canvas black, used to keep dark elements feeling part of the same family
- Void `#080809` for Near-pure black for the darkest link borders and emphasis text - visually indistinguishable from #000000 but kept distinct in the scale for deepest emphasis

- Helvetica Neue `--font-helvetica-neue` for The entire typographic system. Weight 400 at 162px is the signature move - most portfolios would use 700-900 for a hero this large; Phipps uses regular, letting the sheer size and aggressive negative tracking carry authority instead of stroke weight. LineHeight of 0.90 on the display size means the two-line hero actually visually interlocks. All other text (body, labels, navigation, links) is the same family at the same weight - there is no secondary typeface voice.
- Times `--font-times` for Used only as 13px image captions or photo metadata - the serif appears as a deliberate editorial counterpoint to the Helvetica system, breaking the all-grotesque monotony at micro scale

## Avoid

- Do not introduce any chromatic color - no brand reds, no accent blues, no button fills; the photograph is the only color source
- Do not add border-radius to any element - keep all corners at 0px; rounded corners would break the printed-poster logic
- Do not use box-shadows, drop-shadows, or any elevation effects - the design is flat against the photographic plane by intent
- Do not swap the display weight to 700 or 800 in any context - if a heading needs more weight, increase size instead; 400 at scale is the only authority the system allows
- Do not wrap text content in cards, panels, or bordered containers - sections are separated by whitespace alone, never by chrome
- Do not use icons for social links, email, or navigation - text plus the external arrow is the entire icon vocabulary
- Do not use uppercase tracking-wide labels for body copy - only the small section identifiers (EXPLORE, LATEST WORKS) use the stacked-label pattern

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
