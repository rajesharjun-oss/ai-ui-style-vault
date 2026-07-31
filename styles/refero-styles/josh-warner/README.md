# Josh Warner

Source: [Refero Style](https://styles.refero.design/style/e2e9b80c-b548-4f86-a4d7-7a6b07d1c2e1)
Reference site: [https://www.joshwarner.design](https://www.joshwarner.design)
Captured: 2026-07-31
Refero published: 2026-04-30T02:01:39.912Z
Refero modified: 2026-06-05T10:37:41.687Z
Theme: dark
Category: Design

## Style Summary

Explore Josh Warner's dark Design design system: Void #0f0f0f, Absolute #000000 colors, Inter Display, System sans-serif typography, and DESIGN.md for AI...

North star: black void gallery wall

## What To Borrow

- Void `#0f0f0f` for Page canvas and primary surface - the base layer beneath all artwork, slightly lifted from pure black to prevent OLED banding in the dark void
- Absolute `#000000` for Hairline borders, image containers, icon strokes, footer dividers - pure black acts as the structural ink that defines edges in the absence of visible card surfaces
- Charcoal `#1a1a1a` for Elevated footer surface and deeper UI panels - a single step up from canvas for zone separation without breaking the dark void
- Faint `#080808` for Shadow base for subtle elevation effects - nearly invisible against canvas, used in box-shadow compositions for soft ambient lift
- Bone `#f0f0f0` for Primary text color, nav item fills, filled button background - warm off-white replaces pure white to soften contrast against the black void and reduce eye strain
- Ash `#b8b8b8` for Secondary body text, subdued helper labels, muted metadata - sits one step below Bone for non-emphasized copy without losing legibility on dark surfaces
- Graphite `#696969` for Tertiary text and border accents on headings - used sparingly for fine print and inactive labels that should recede
- Live Wire `#08ff00` for Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content

- Inter Display `--font-inter-display` for Primary typeface across all UI, body, navigation, and headings - used exclusively at weight 400 with no weight variation, creating a flat, even visual texture where size and spacing alone carry hierarchy. Substitute with Inter (free, near-identical metrics).
- System sans-serif `--font-system-sans-serif` for Micro-UI labels (12px) - system stack for the smallest utility text where font loading overhead isn't justified

## Avoid

- Don't introduce any new accent colors beyond Live Wire green - the system is deliberately monochromatic and any additional hue will break the gallery void
- Don't use drop shadows for card or surface elevation - depth must come from the artwork itself or surface tone shifts, not from shadow stacks
- Don't bold headlines or use weight 500+ - the entire type system breathes at weight 400; adding weight disrupts the flat, even texture
- Don't use sharp corners (<12px) on buttons, nav items, or badges - the pill geometry is the system's visual identity
- Don't use pure black (#000000) as a fill background for cards or surfaces - reserve it for hairline borders and edges; use Void (#0f0f0f) for surfaces
- Don't place body text below 14px or above 40px - the type scale is deliberately compressed; deviation breaks the editorial restraint
- Don't add gradients, glows, or color washes to UI elements - the system's visual energy comes from the 3D/photographic content, not from UI decoration

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
