# Rains INT

Source: [Refero Style](https://styles.refero.design/style/38c8a8c9-4d2e-462a-bff0-80c9d9619ef2)
Reference site: [https://www.rains.com](https://www.rains.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:29:15.946Z
Refero modified: 2026-06-05T11:32:25.956Z
Theme: light
Category: E-commerce

## Style Summary

Explore Rains INT's light E-commerce design system: Fog #efefef, Ink #10100f colors, EuropaGroNr2SH, EuropaGroNr2SB typography, and DESIGN.md for AI agents.

North star: Nordic rain catalog on fog-gray paper.

## What To Borrow

- Fog `#efefef` for Page canvas, card surfaces, divider hairlines - the warm light gray that IS the page background
- Ink `#10100f` for Primary text, nav links, body copy, icon strokes - near-black with a barely-warm bias (never pure #000)
- Paper `#ffffff` for Card surfaces over the gray canvas, text on dark buttons, product image backgrounds
- Charcoal `#26292a` for Filled button background, active states, inverted UI surfaces - warm-tinted dark, never pure black
- Graphite `#40403f` for Secondary button fill, subtle dark UI accents
- Ash `#b3b3b2` for Muted helper text, tertiary metadata, inactive nav items
- Black `#000000` for Pure black for SVG icon fills and the occasional hard edge - functional, not brand
- Butter Cream `#fffb85` for Hero display text accent - the single chromatic voice on the page, used only on oversized seasonal headlines over photography

- EuropaGroNr2SH `--font-europagronr2sh` for Headings, display statements, nav items, body emphasis - the hero font. Used at 232-245px with weight 400 and line-height 0.90 for the signature oversized editorial type. The ultra-tight leading locks massive letters into a single visual band. Subheads drop to 32-48px at weight 600-700.
- EuropaGroNr2SB `--font-europagronr2sb` for Small UI text, nav labels, button copy, captions, footer micro-copy. The functional sans - quiet, compact, only at 12-14px. The deliberate size gap between this and EuropaGroNr2SH creates a clear voice split: small = system, large = editorial.

## Avoid

- Do not introduce saturated accent colors (reds, blues, greens) into the UI - the 1% colorfulness is deliberate
- Do not apply box-shadows, drop-shadows, or gradient fills to any component - the system is completely flat
- Do not use sharp or moderately rounded corners on buttons or interactive elements - only 9999px or 0px exist
- Do not use pure #000000 for text - use #10100f; the near-black warmth is a design choice, not a compromise
- Do not place body text directly over product photography without sufficient contrast or a dark scrim
- Do not break the two-font split: EuropaGroNr2SB for 12-14px system text, EuropaGroNr2SH for 16px and above - mixing sizes across fonts fragments the voice
- Do not add decorative borders, dividers, or background tints to card components - the photograph and gray canvas define all visual structure

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
