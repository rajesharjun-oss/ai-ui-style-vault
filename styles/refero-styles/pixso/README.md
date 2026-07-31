# Pixso

Source: [Refero Style](https://styles.refero.design/style/155dbf6e-1187-424e-9ce8-59ffecff7e6b)
Reference site: [https://pixso.net](https://pixso.net)
Captured: 2026-07-31
Refero published: 2026-03-29T10:38:19.000Z
Refero modified: 2026-06-05T09:26:24.758Z
Theme: light
Category: Design

## Style Summary

Explore Pixso's light Design design system: Obsidian #000000, Carbon #121212 colors, Figtree typography, and DESIGN.md for AI agents.

North star: pristine designer's canvas flooded with morning light

## What To Borrow

- Obsidian `#000000` for Primary text, heading type, dark icons, and the strongest foreground layer
- Carbon `#121212` for Filled primary buttons, active nav state, dark surface fill
- Graphite `#333333` for Secondary headings, button labels on light surfaces, heavy icon strokes
- Slate `#666666` for Body secondary text, helper copy, muted metadata
- Ash `#808080` for Tertiary text, disabled states, placeholder copy, subtle borders
- Fog `#999999` for Inactive icons, low-emphasis dividers, shadow tinting
- Pebble `#8b8c8f` for Icon strokes on neutral surfaces, muted glyph color
- Smoke `#4d4d4d` for Heavy body text where Obsidian feels too sharp, small caption emphasis
- Charcoal Veil `#3d3d3d` for Navigation bar text and borders - the dark nav strip registers as a separate layer
- Dusk `#292929` for Deep surface fill for elevated dark blocks and image overlays
- Paper `#faf8fd` for Page canvas - barely-there warm/lavender tint that separates the site from pure white
- Bone `#f9f9fa` for Card surfaces, secondary panels, subtle raised containers
- Mist `#eaebee` for Hairline borders, divider rules, button outlines, input borders
- Ice Wash `#cfe7ed` for Pale cool-blue background tint for highlighted cards and feature panels
- Iris Sweep `#ee7cff` for Brand logo gradient midpoint - the wordmark's signature purple-to-blue sweep
- Orchid Edge `#ee7cff` for Brand logo gradient start - warm violet anchor of the wordmark sweep
- Sky Drift `#559cff` for Brand logo gradient end - cool blue terminus of the wordmark sweep

- Figtree `--font-figtree` for Single-family system: 700 carries the hero and section headlines at 48-60px with tight tracking, 600 handles subheadings and prominent labels at 24-34px, 500 covers button labels and emphasized body at 16-18px, 400 runs body and caption copy at 13-16px. The geometric, low-contrast character of Figtree keeps the all-black type from feeling oppressive.

## Avoid

- Don't introduce a chromatic CTA color - the primary action is always Carbon #121212
- Don't use heavy drop shadows or colored shadows; elevation must stay hairline
- Don't set body type below 13px or use Figtree below weight 400
- Don't add gradient backgrounds to UI surfaces; gradients belong to the logo and decorative imagery
- Don't center-align body paragraphs - the system uses left-aligned running text below the hero
- Don't use #0000ee or browser-default link blue for any interactive element
- Don't round buttons to pill (9999px); the system uses 8/12/18px radii only

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
