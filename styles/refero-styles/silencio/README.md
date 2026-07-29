# Silencio

Source: [Refero Style](https://styles.refero.design/style/e67ac20e-6497-4756-b7e2-17859a794fb6)  
Reference site: [https://silencio.es](https://silencio.es)  
Captured: 2026-07-29  
Refero published: 2026-02-27T09:21:05.000Z  
Refero modified: 2026-06-05T02:59:30.989Z  
Theme: light  
Category: Design

## Style Summary

Explore Silencio's light Design design system: Ink Black #000000, Paper Warm Gray #dbdad9 colors, HaasR, HaasT typography, and DESIGN.md for AI agents.

North star: white room with floating artifacts. A warm-paper gallery vitrine where every element earns its space against negative volume, and silence is a deliberate design material.

## What To Borrow

- Ink Black `#000000` as Primary text, iconography, hairline rules, table borders the only high-contrast element on the page
- Paper Warm Gray `#dbdad9` as Card surfaces, soft fills, the single chromatic departure from pure white, gentle gradient origin
- Graphite Border `#808080` as Subtle table dividers and secondary rule lines used when #000000 would feel too heavy
- Bleach White `#ffffff` as Supporting palette color for small decorative accents when the core palette needs contrast.
- HaasR Workhorse grotesque for body, subheadings, and mid-size headings. Weight 100 is used for restraint in body contexts; 700 sparingly for emphasis. The single most-used face carries the page. `--font-haasr` for the source typography voice
- HaasT Display-only face at 141px with tightened leading (0.90). Used for hero statements and singular set-pieces the only moment typography shouts, and it shouts at full volume against pure white. `--font-haast` for the source typography voice
- 4px base spacing with comfortable density
- Source radius system: tags 9999px, cards 7.2px, buttons 129.6px, surfaces 43.2px

## Avoid

- Never introduce a chromatic color the palette ends at #000000, #dbdad9, #808080, and #ffffff
- Never use drop shadows for elevation; the gradient #dbdad9 #ffffff is the only depth the system allows
- Never set type above 141px or below 9px the 132px range is the entire expressive spectrum
- Never use #0000ee or any default browser link color links are #000000, no exception
- Never fill a button with color; the pill is always transparent with a 1px #000000 border
- Never center body text in paragraphs; only display statements and labels earn centered alignment
- Never use shadows, blurs, or glows on photographs or product imagery

## Bundle Contents

- [DESIGN.md](DESIGN.md): implementation notes.
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
