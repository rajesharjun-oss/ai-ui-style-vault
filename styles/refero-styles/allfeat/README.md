# Allfeat

Source: [Refero Style](https://styles.refero.design/style/2f9bf724-3829-4c62-bcc8-391b32925d1b) 
Reference site: [https://allfeat.org](https://allfeat.org) 
Captured: 2026-07-29 
Refero published: 2026-05-10T22:34:07.514Z 
Refero modified: 2026-06-03T21:51:30.357Z 
Theme: dark 
Category: Crypto

## Style Summary

Explore Allfeat's dark Crypto design system: Charcoal Stage #151515, Warm Cream #fffbeb colors, TASA Orbiter typography, and DESIGN.md for AI agents.

North star: Backstage monitor at midnight - one teal stage light cutting through warm cream type on charcoal glass.

## What To Borrow

- Charcoal Stage `#151515` for Page canvas, primary surface, all dark backgrounds - the base layer every other color sits on
- Warm Cream `#fffbeb` for Primary text, nav links, heading copy, hairline borders on dark surfaces - never pure white, always slightly buttered
- Card Edge `#383835` for Inset 1px card borders, card ambient shadow, subtle separator lines on elevated surfaces
- Mute Cream `#b8b8b8` for Secondary body text, subdued descriptions, muted helper copy
- Ash Gray `#a6a6a6` for Subdued heading text, list separators, inactive link borders
- Bronze Veil `#504f4a` for Badge borders, card hairline accents, low-emphasis outline treatments
- Signal Teal `#00b18c` for Teal action color for filled buttons, selected navigation states, and focused conversion moments.
- Ember Coral `#ff4a5f` for Red action color for filled buttons, selected navigation states, and focused conversion moments

- TASA Orbiter `--font-tasa-orbiter` for Single typeface across the entire system. Weight 600 for hero and section headlines, weight 500 for subheadings and emphasized body runs, weight 400 for body and metadata. The tight -0.02em tracking on display sizes (54-56px) collapses the headline into a confident slab; the 0.02em loosening on badge/eyebrow text (13-14px) makes labels feel like printed marks.

## Avoid

- Don't introduce a new accent color - teal and coral are the only chromatic voices in the system
- Don't use 8px or 16px radius on cards or images; the system is strictly 12px for containers and 900px for interactive elements
- Don't use pure white (#ffffff) for text - always #fffbeb, the warm cream tint is part of the brand
- Don't apply drop shadows anywhere - the entire elevation system is inset-only
- Don't break the single-typeface rule by introducing a second font; TASA Orbiter at 400/500/600 covers every need
- Don't set headlines in light or thin weights - 600 is the floor for display sizes, mixing in 400-500 only as muted secondary clauses
- Don't fill buttons with #ff4a5f coral - coral is atmospheric, not actionable; only #00b18c signals an action

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
