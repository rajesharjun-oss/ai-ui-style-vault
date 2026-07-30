# Fey

Source: [Refero Style](https://styles.refero.design/style/733e6475-892a-4138-8835-bf40344df317)
Reference site: [https://feyapp.com](https://feyapp.com)
Captured: 2026-07-30
Refero published: 2026-01-31T13:04:03.000Z
Refero modified: 2026-07-03T11:04:52.763Z
Theme: light
Category: Fintech

## Style Summary

Explore Fey's light Fintech design system: Warm Paper #fafafa, Graphite #595959 colors, -apple-system, Wealthsimple Sans Display typography, and DESIGN.md...

North star: a printed broadsheet on warm paper - type and silence, nothing else.

## What To Borrow

- Warm Paper `#fafafa` for Page background - the only surface; everything floats on this warm off-white
- Graphite `#595959` for Body text, nav labels, footer copy - medium-dark gray keeps long-form reading comfortable without high-contrast harshness
- Ink `#1c1c1c` for Secondary body text, navigation labels, and subdued headings.

- -apple-system `--font-apple-system` for Body and navigation. At 21px / 600 / line-height 1.55 with -0.01em tracking, the system stack carries the entire page - the signature is the size and rhythm, not a custom face. 13px / 400 nav labels use the same -0.002em micro-tracking. A 16px / 400 utility size appears for small captions.
- Wealthsimple Sans Display `--font-wealthsimple-sans-display` for Reserved for the "Wealthsimple" link - a single display-grade cut at 21px / 700 / -0.01em. It signals partnership without changing the page's monochrome restraint.

## Avoid

- Do not introduce accent colors, buttons, or CTAs - this page is a declaration, not an action.
- Do not add headings (h1/h2/h3) - the 21px body carries the hierarchy through weight and color alone.
- Do not use shadows, borders, or background fills on text containers.
- Do not break the 520px column with sidebars, images, or multi-column layouts.
- Do not use a display or serif font for body copy - the system stack at 21px / 600 is the intended voice.
- Do not add hover states beyond color/weight transitions on links; no transform, scale, or shadow effects.

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
