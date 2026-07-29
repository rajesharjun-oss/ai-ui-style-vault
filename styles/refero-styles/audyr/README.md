# Audyr

Source: [Refero Style](https://styles.refero.design/style/afde66c4-ad74-4d19-94df-0216e945ac5e) 
Reference site: [https://audyr.com](https://audyr.com) 
Captured: 2026-07-29 
Refero published: 2026-05-11T00:38:34.650Z 
Refero modified: 2026-06-03T15:39:37.359Z 
Theme: light 
Category: SaaS

## Style Summary

Explore Audyr's light SaaS design system: Ink #262626, Pure Paper #ffffff colors, Inter typography, and DESIGN.md for AI agents.

North star: Ink on cold-pressed paper. The interface reads as a meticulously typeset monograph - black ink, white stock, hairline rules, and the softest possible shadows to suggest depth.

## What To Borrow

- Ink `#262626` for High-contrast neutral action fill for primary buttons on light surfaces.
- Pure Paper `#ffffff` for Card surfaces, elevated panels, content backgrounds - the base canvas color sits one step brighter than the page
- Soft Mist `#ededed` for Hairline borders, input outlines, dividers, subtle panel fills - the structural glue that separates regions without lines shouting
- Charcoal `#171717` for Secondary dark surface (pricing card, alternate hero), occasional dark fills where deeper weight is needed than Ink
- Ash `#686868` for Secondary body text, nav links, supporting copy - the first step down from primary text
- Slate `#515151` for Tertiary text, icon strokes on light backgrounds, muted metadata
- Muted `#737373` for Helper text, caption-level copy, secondary icon strokes
- Fog `#929292` for Placeholder text, disabled labels, very low-emphasis text
- Chalk `#cbcbcb` for Shadow residue on dark buttons, ultra-low-contrast surface markers
- Mint Whisper `#ecfdf5` for Primary page canvas and white card surfaces. Use as a supporting accent, not as a status color

- Inter `--font-inter` for The sole typeface. Weight 600 reserved for section labels and small UI controls; weight 500 for nav and secondary buttons; weight 400 for body and most copy. The system commits to one family rather than pairing a display serif - a deliberate editorial choice that keeps the visual signal monochrome.

## Avoid

- Don't introduce a brand color accent - the absence of color IS the brand
- Don't use radii outside the 4 / 8 / 14 / 18 / 9999px scale; no 6px or 12px intermediate values
- Don't add drop shadows heavier than the documented card shadow - anything more theatrical breaks the paper-grain feel
- Don't pair Inter with a second typeface for display use - the single-family commitment is structural
- Don't use #ffffff for text on white surfaces, and don't use #ededed for body text - both will fail contrast
- Don't apply gradients - the system is committed to flat, unshaded fills
- Don't use colored status indicators on the marketing site; restrict color to badges and the pricing 'Popular' highlight

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
