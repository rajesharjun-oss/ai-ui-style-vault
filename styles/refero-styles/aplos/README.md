# Aplos

Source: [Refero Style](https://styles.refero.design/style/765e6ba8-af87-4519-afb7-774ceedc463d)
Reference site: [https://aplos.world](https://aplos.world)
Captured: 2026-07-31
Refero published: 2026-04-30T02:49:17.869Z
Refero modified: 2026-06-05T07:42:28.731Z
Theme: light
Category: E-commerce

## Style Summary

Explore Aplos's light E-commerce design system: Bone #f2f1ed, Paper White #ffffff colors, Goudy Old Style, System Sans (UI chrome) typography, and DESIGN.md...

North star: Old-world apothecary at dusk

## What To Borrow

- Bone `#f2f1ed` for Page background, large section canvases - the warm off-white that gives the system its paper-like editorial feel
- Paper White `#ffffff` for Card surfaces, elevated panels, light benefit cards - sits one step above Bone to create lift without shadows
- Cocoa `#3b3429` for Dark accent cards, inverted text blocks - warm near-black that softens pure ink and keeps dark sections feeling organic rather than digital
- Ink `#000000` for Primary text, nav links, logo wordmark, hairline borders, hero backdrop
- Stone `#646464` for Secondary body copy, muted helper text, subdued descriptions
- Ash `#b4aeac` for Subtle link hover shadows, barely-there elevation hints

- Goudy Old Style `--font-goudy-old-style` for Sole typeface for headlines, section titles, product names, card titles, and editorial body - a classical Venetian serif that signals craft and heritage. The narrow weight range (400 only) and tight line-heights (1.05-1.08) let the type sit in dense, menu-like stacks. Letter-spacing of -0.012em tightens optical gaps in display sizes without losing the serif's elegance.
- System Sans (UI chrome) `--font-system-sans-ui-chrome` for Inferred secondary face for navigation, buttons, captions, and dense utility text where serif would be illegible at small sizes. Kept restrained so the serif remains dominant.

## Avoid

- Don't introduce any chromatic color (blue, green, red, etc.) - the system is deliberately 0% colorful and any hue will break the apothecary language.
- Don't use large border-radius (12px+) or pill shapes - the 5px radius is non-negotiable and keeps the system feeling editorial, not app-like.
- Don't use bold weights (600+) for headings - Goudy Old Style 400 only; the whisper-weight serif is the signature.
- Don't add drop shadows, glows, or gradient overlays - elevation comes from tonal contrast between Bone, Paper, and Cocoa, not from blur effects.
- Don't use a sans-serif for product names or section titles - those are exclusively Goudy Old Style domain.
- Don't crowd sections with dense grids - the rhythm depends on 96-120px breathing room between blocks.
- Don't place dark text directly on Cocoa (#3b3429) without testing contrast - use white (#ffffff) text on Cocoa surfaces.

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
