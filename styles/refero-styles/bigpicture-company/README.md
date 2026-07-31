# Bigpicture Company

Source: [Refero Style](https://styles.refero.design/style/eafe33bf-6f53-4619-b279-686ad5869799)
Reference site: [https://www.bpco.kr](https://www.bpco.kr)
Captured: 2026-07-31
Refero published: 2026-04-30T01:20:07.374Z
Refero modified: 2026-06-05T10:03:23.070Z
Theme: light
Category: Agency

## Style Summary

Explore 's light Agency design system: Press Ink #121212, Paper White #ffffff colors, Helvetica Neue, PPSupplyMono typography, and DESIGN.md for AI...

North star: Concrete slab typographic manifesto. A black-on-white press kit where oversized Helvetica does the work of photography, and the only texture is a single sheet of crumpled paper under the body type.

## What To Borrow

- Press Ink `#121212` for Primary text, hairlines, section borders, icon strokes, footer text - the singular dark tone that carries 95% of all foreground information
- Paper White `#ffffff` for Page canvas, card surfaces, nav pill background, heading-bordered surfaces
- Newsprint `#f1f1f1` for Subtle surface fills, soft borders, hairline dividers, the tone behind the crumpled-paper texture
- Foil Gray `#e1e1e1` for Light borders, icon stroke accents, secondary dividers
- Mute Gray `#c5c5c5` for Tertiary text, disabled state, low-contrast surface lines

- Helvetica Neue `--font-helvetica-neue` for Universal workhorse - body copy at 17px/1.29, display headlines at 75-274px with -0.04em tracking at the largest sizes, nav labels at 15px
- PPSupplyMono `--font-ppsupplymono` for Meta labels and bracketed captions like [01-N INTRODUCTION] and section tags (ADVERTISEMENTS, CREATIVE/AGENCY, OFFLINE MARKETING) - these are the only typographic accents that break the Helvetica monotony
- PPSupplySans `--font-ppsupplysans` for Secondary nav and footer micro-text where a different sans voice is needed
- Rock Salt `--font-rock-salt` for Rare handwritten signature accent for one or two words per page (e.g. the circled 'pleasure' annotation) - used like a stamp, never for content

## Avoid

- Do not add any color other than the five neutrals (#121212, #ffffff, #f1f1f1, #e1e1e1, #c5c5c5) - zero chroma is the brand
- Do not use box-shadows; depth comes from hairline borders and the paper texture only
- Do not break the all-caps convention on display headlines; mixed case is reserved for the Rock Salt annotation
- Do not use 9999px pill radii on buttons or tags - the largest standard radius is 40px on the nav
- Do not compress line-height below 1.0 on display type, and do not exceed 1.6 on body
- Do not place body copy in a column wider than ~720px - the editorial measure must stay readable
- Do not add hover-lift or transition effects to cards; the aesthetic is static print, not interactive UI

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
