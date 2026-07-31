# RainbowKit

Source: [Refero Style](https://styles.refero.design/style/7421c174-a1b1-4695-a9e7-a82dc6f5ea3b)
Reference site: [https://www.rainbowkit.com](https://www.rainbowkit.com)
Captured: 2026-07-31
Refero published: 2026-04-30T01:48:36.534Z
Refero modified: 2026-06-05T12:16:06.326Z
Theme: dark
Category: Crypto

## Style Summary

Explore RainbowKit's dark Crypto design system: Signal Blue #0e76fd, Aurora Gradient #3898ff colors, SFRounded, SFMono typography, and DESIGN.md for AI agents.

North star: Neon wallet modal floating in a black void - the blue-to-violet aurora glows through the dark.

## What To Borrow

- Signal Blue `#0e76fd` for Primary CTA fill, active states, brand wordmark, link emphasis - the only chromatic blue with enough surface area to carry identity
- Electric Violet `#7a70ff` for Gradient terminus, brand-secondary accent - appears only as the cool half of the aurora
- Deep Iris `#38228f` for Violet wash for highlight backgrounds, decorative bands, and soft emphasis behind content.
- Hyper Pink `#ff5ca0` for Accent spectrum - demonstration option in the wallet-customization showcase, not a UI-state color
- Ember Red `#fa423c` for Accent spectrum - demonstration option in wallet-customization showcase
- Solar Orange `#ff801f` for Accent spectrum - demonstration option in wallet-customization showcase
- Toxic Green `#1db847` for Accent spectrum - demonstration option in wallet-customization showcase
- Void `#000000` for Page canvas, deepest surfaces, inverted button borders - true black anchors the entire system
- Obsidian `#1b1c1e` for Card surfaces, code blocks, modal containers, body text on light - the workhorse elevated surface
- Shadow `#121314` for Shadow tint color (used in box-shadow rgba), near-black with a hint of warmth
- Graphite `#25292e` for Hairline borders, dividers, icon stroke, secondary text on dark - the most-used neutral border in the system
- Slate `#2f3334` for Secondary borders, subtle dividers between sections - sits between Graphite and Pewter
- Carbon `#353a3b` for Tertiary icon fills, disabled-state borders, subtle backgrounds
- Pewter `#646566` for Disabled button background, low-emphasis surfaces - never for text
- Fog `#95979c` for Muted helper text, icon secondary, placeholder text - the only gray that carries readable information
- Snow `#ffffff` for Primary text, inverted button fill, light-surface backgrounds, icon glyphs, hairline highlight borders
- Mist `#f0f1f5` for Light-theme surface fallback, very subtle off-white for section backgrounds on the demo

- SFRounded `--font-sfrounded` for Primary typeface for all UI - rounded geometric sans, chosen because the soft terminals make technical Web3 copy feel approachable rather than intimidating
- SFMono `--font-sfmono` for Code snippets, terminal commands, technical strings - the npm install command in the hero
- system-ui `--font-system-ui` for Fallback body copy when the web font hasn't loaded - barely visible because SFRounded dominates
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI

## Avoid

- Don't use the chromatic accent colors (Hyper Pink, Ember Red, Solar Orange, Toxic Green) as semantic UI states - they are demonstration options, not success/error/warning tokens
- Don't apply shadow to text or the canvas itself - shadows belong to floating cards only, the background is shadowless
- Don't use negative letter-spacing - SFRounded is designed for positive tracking; tightening it fights the rounded letterforms
- Don't introduce a second body font - SFRounded handles everything from 11px captions to 52px displays; a serif or system fallback breaks the cohesion
- Don't place white or light-colored cards on the canvas - every surface must stay in the Obsidian/Graphite range to preserve the void
- Don't use #25292 for text - it's a border color, contrast on it is insufficient for readable copy
- Don't round images of phones or product screenshots with small radii - they should be 24px+ or fully inherit the device frame

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
