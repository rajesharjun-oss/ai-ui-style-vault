# Gamma

Source: [Refero Style](https://styles.refero.design/style/4782832c-1c23-4fe3-997c-2a08d7b6c5d1)
Reference site: [https://www.gamma.io](https://www.gamma.io)
Captured: 2026-07-31
Refero published: 2026-04-30T00:58:01.165Z
Refero modified: 2026-06-05T08:13:45.311Z
Theme: light
Category: Crypto

## Style Summary

Explore Gamma's light Crypto design system: Ink Black #0c0c0d, Pure White #ffffff colors, Gamma Sans Display typography, and DESIGN.md for AI agents.

North star: white-walled art gallery. The UI is a silent frame; the artwork is the only thing that should be loud.

## What To Borrow

- Ink Black `#0c0c0d` for High-contrast neutral action fill for primary buttons on light surfaces.
- Pure White `#ffffff` for Page canvas, card surfaces, text on dark fills, input backgrounds
- Ash `#e9e9ec` for Hairline borders, subtle dividers, hover surfaces, secondary button outlines
- Smoke `#808080` for Muted body text, metadata (mint counts, prices), inactive icons, placeholder content
- Graphite `#242629` for Icon strokes, secondary button borders, slightly elevated neutral surfaces
- Charcoal `#1d1d1e` for Rare dark surface (e.g. featured card panels) - used sparingly to create a single dark anchor in an otherwise all-white page
- Blush to Violet `#ffffff` for Hero wash gradient - soft pink-to-magenta transition used only as a backdrop to large featured artworks, never as a UI fill

- Gamma Sans Display `--font-gamma-sans-display` for Single-family system used for everything from micro-labels to the 72px hero display. Weight 300 for oversized hero titles ('LIGHT') creates a near-tracery effect that lets the artwork underneath read through; weight 600 reserved for short labels and the Connect button; weight 400 carries body and metadata. The custom neo-grotesque has a slightly condensed character width and flat apertures that feel more architectural than friendly.

## Avoid

- Do not introduce a chromatic accent color, brand fill, or saturated button - the UI must stay colorless so the artwork remains the only loud element
- Do not round artwork thumbnails beyond 4px; the sharp corner is what makes the image feel like a print pinned to a wall
- Do not use box-shadow, glow, or blur on any component - depth is communicated only by hairline borders and a single dark surface
- Do not place UI text inside a scrim or colored box over artwork; the display type must sit directly on the image
- Do not use the Blush-to-Violet gradient on buttons, navs, or borders - it is reserved for the Prints section backdrop only
- Do not mix more than two type weights on a single screen; the 300/400/600 scale is for hierarchy, not decoration
- Do not center-align body text or metadata; keep descriptions and counts left-aligned with consistent left margin to the thumbnail edge

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
