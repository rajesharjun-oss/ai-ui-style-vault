# A-dam

Source: [Refero Style](https://styles.refero.design/style/0fc184f7-6143-4303-8e3d-0e2f075f76b2)
Reference site: [https://a-dam.com](https://a-dam.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:32:36.032Z
Refero modified: 2026-06-05T12:12:26.802Z
Theme: light
Category: E-commerce

## Style Summary

Explore A-dam's light E-commerce design system: Midcurrent Navy #000e1f, Deep Cobalt #0000c5 colors, GT Walsheim Pro, sans-serif typography, and DESIGN.md...

North star: morning surf over a curated product shelf - a light, airy canvas where honest basics and ocean-toned photography do the talking.

## What To Borrow

- Midcurrent Navy `#000e1f` for Primary text, filled buttons, rating widget, icon strokes - the workhorse dark surface that grounds every interface layer
- Deep Cobalt `#0000c5` for Announcement bar surface and occasional accent punctuation - saturated blue used sparingly to break an otherwise monochrome frame
- Twilight Slate `#1a2635` for Secondary borders and emphasis dividers - a near-gray that steps up from Midcurrent Navy for subtle layering without contrast jumps
- Graphite `#000000` for Icon fills, nav text, and footer ink - pure black reserved for the smallest functional elements where maximum punch is needed
- Paper White `#ffffff` for Card surfaces, product tile backgrounds, nav bar canvas, and inverted text on dark fills
- Morning Mist `#f4f4f4` for Page canvas and elevated card background - the warm off-white that gives the entire site its soft, lived-in brightness
- Cloud Veil `#e6e7e9` for Dominant hairline border for cards, icons, links, and image frames - the quietest structural line in the system
- Soft Stone `#dcdddf` for List dividers, secondary borders, and badge outlines - one step darker than Cloud Veil for hierarchy between hairline and emphasis
- Slate Gray `#666e79` for Muted helper text, secondary copy, and link text in resting state - cool gray that recedes behind primary navy content
- Sunbeam `#fff48d` for Star-rating fills and small highlight washes - the only warm color in the system, kept tiny and functional

- GT Walsheim Pro `--font-gt-walsheim-pro` for Primary brand typeface across all UI roles. The 900 weight is the signature - it powers the 70px display headlines with architectural density. Geometric humanist forms give the brand a friendly, modern voice; the wide weight range (400 for body, 900 for display) lets a single family carry every level of emphasis.
- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI
- GT-Walsheim-Pro `--font-gt-walsheim-pro` for GT-Walsheim-Pro - detected in extracted data but not described by AI

## Avoid

- Don't add drop shadows to product cards, category cards, or buttons - the system is intentionally shadowless
- Don't apply custom letter-spacing to GT Walsheim - its built-in tracking is part of the design; override only if a specific optical correction is needed
- Don't use Deep Cobalt for body text or large fills - it belongs in the 32-40px announcement strip
- Don't introduce rectangular button radii - the 30px pill is the only shape buttons take
- Don't place dark navy on dark navy without sufficient contrast separation - the system relies on light-on-dark and dark-on-light pairing
- Don't use system Arial or sans-serif as substitutes for GT Walsheim in display or heading roles - fall back to Outfit or Inter, which preserve geometric warmth
- Don't fill the page with color - the palette is 95% neutrals; let the one cobalt bar and the tiny sunbeam stars carry all chromatic punctuation

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
