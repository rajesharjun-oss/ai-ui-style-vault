# AI Product Generation

Source: [Refero Style](https://styles.refero.design/style/186775da-7568-49e5-8110-4fd0bbc7bbe3) 
Reference site: [https://fourmula.ai](https://fourmula.ai) 
Captured: 2026-07-29 
Refero published: 2026-04-30T00:15:10.683Z 
Refero modified: 2026-06-05T04:20:48.948Z 
Theme: light 
Category: AI

## Style Summary

Explore AI Product Generation's light AI design system: Ink Black #020108, Charcoal #333333 colors, Arial, SF Pro Display typography, and DESIGN.md for AI...

North star: editorial photography studio on white paper - headline display type as cover, orange as the editor's highlight pen

## What To Borrow

- Ink Black `#020108` for Primary text, borders, icon strokes - near-black carries all body and heading copy
- Charcoal `#333333` for Dominant border color across the entire interface, card outlines, dividers
- Steel `#5d5c61` for Secondary borders, muted icon fills, tertiary structural lines
- Pewter `#818084` for Muted helper text, secondary link text, subdued metadata
- Ash `#d7d7d6` for Subtle background washes, low-contrast surface differentiation
- Canvas White `#ffffff` for Card surfaces, image backgrounds, inverted text on dark regions
- Paper `#f7f7f7` for Page background - the dominant canvas tone behind all content

- Arial `--font-arial` for Arial - detected in extracted data but not described by AI
- SF Pro Display `--font-sf-pro-display` for Sole typeface across the system - display headlines reach 100px at weight 400 with -3.1% tracking, subheadings at 53px weight 500 with -2% tracking, body at 15-17px weight 400. The choice to use weight 400-500 even at display sizes (rather than going bold) is signature: the type commands attention through scale and tightness, not weight. Substitute: Inter, or any geometric grotesque with strong x-height and tight default tracking.

## Avoid

- Do not introduce a second chromatic accent - the system is monochrome with a single orange highlight, and adding color dilutes the editorial discipline
- Do not use bold or weight 600+ for headlines - weight 400-500 at large sizes is the signature; going heavy breaks the cover-type feel
- Do not apply box-shadows to cards, buttons, or images - the system is entirely flat; elevation must be communicated through tonal surface steps
- Do not use background colors on text spans, underlines, or pills for emphasis - color swap on a word within running text is the only emphasis pattern
- Do not use the gradient system for large hero backgrounds or section fills - gradients are for accent strokes and small decorative elements only
- Do not introduce more than two border-radius values per component type - 9999px is exclusively for buttons, 7px exclusively for cards, 20-27px exclusively for images
- Do not use fully saturated primaries (pure red, pure green, pure blue) anywhere - the palette's chromatic notes all carry warmth or desaturation

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
