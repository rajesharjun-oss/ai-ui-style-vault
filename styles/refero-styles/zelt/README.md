# Zelt

Source: [Refero Style](https://styles.refero.design/style/beba80a3-8f10-48fd-9e6c-a3436112f45b)
Reference site: [https://zelt.app](https://zelt.app)
Captured: 2026-07-31
Refero published: 2026-05-07T02:11:02.088Z
Refero modified: 2026-06-05T10:45:00.449Z
Theme: light
Category: SaaS

## Style Summary

Explore Zelt's light SaaS design system: Ink #121718, Paper #ffffff colors, sans-serif (system) typography, and DESIGN.md for AI agents.

North star: Amber on raw linen - the single honey accent glows against warm cream and near-black ink, as if sunlight fell across a paper spread.

## What To Borrow

- Ink `#121718` for Primary text, icon strokes, hairline borders, default link text - near-black with a barely-warm cast that harmonizes with the cream canvas rather than fighting it
- Paper `#ffffff` for Elevated card surfaces, button text on amber, icon fills - the brightest stop in the stack, used sparingly to lift content above the cream canvas
- Linen `#f6f3ef` for Card backgrounds, soft surface fill, inset panels - the warm off-white that sits one step above the page canvas
- Parchment `#e4e0dd` for Page canvas, outer body background - the warm light gray that gives the entire interface its sunlit quality
- Graphite `#2f2f2f` for Dark surface fill for inverted cards, footer band, contrast blocks - darker than Ink so it reads as a deliberate charcoal panel
- Slate `#444444` for Secondary neutral action background, muted utility surfaces - sits between Ink and the canvas for low-emphasis interactive fills
- Honey `#ffcd6d` for Primary action fill for the demo and get-started buttons, key brand moments - the single saturated color in the system, reserved for decisions that move the user forward
- Apricot `#ffe2aa` for Yellow wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color

- sans-serif (system) `--font-sans-serif-system` for Full type system - weight 500/700 at 76-101px with tracking as tight as -0.043em gives headlines a quiet authority without resorting to a serif; weight 400 at 16-18px handles body; the huge size range (8px 101px) is editorial in proportion, not product-UI proportions

## Avoid

- Don't introduce a second saturated color - the system is monochrome warm with one amber accent, and any second hue breaks the spell.
- Don't apply drop shadows to cards, buttons, or nav - delineation is done with hairline 1px borders and surface fill alone.
- Don't set headlines below weight 500 at display sizes; the tight tracking only reads as confident when paired with sufficient weight.
- Don't round corners below 8px on interactive elements and below 12px on cards/buttons - sharp corners fight the pill-shaped language.
- Don't use blue, purple, or any cool hue for links, icons, or accents; all chromatic energy comes from the warm amber family.
- Don't fill large surfaces with Honey - the accent loses its meaning when it covers anything bigger than a button.
- Don't set body text below 16px or above 18px - the system is editorial in proportion, not dense data-UI proportions.

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
