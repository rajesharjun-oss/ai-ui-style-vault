# Vanmoof

Source: [Refero Style](https://styles.refero.design/style/4887c681-d4e6-41d3-b83c-5650cf925ee9)
Reference site: [https://www.vanmoof.com](https://www.vanmoof.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:40:46.642Z
Refero modified: 2026-06-05T08:54:35.696Z
Theme: mixed
Category: E-commerce

## Style Summary

Explore Vanmoof's mixed E-commerce design system: Carbon #222222, Obsidian #000000 colors, Unica77LLWeb, Unica77Mono typography, and DESIGN.md for AI agents.

North star: cinematic monochrome showroom

## What To Borrow

- Carbon `#222222` for Navigation bar, dark surface panels, primary text on light, logo wordmark fill - the near-black anchor of the system, softer than pure #000 for reduced eye strain on large surfaces
- Obsidian `#000000` for Body text, headline text on light surfaces, footer text - reserved for highest-emphasis type where absolute black is needed for maximum contrast (21:1 on white)
- Graphite `#313131` for Secondary text, link text on light, button labels on light surfaces - the mid-dark step between Carbon and Obsidian for hierarchy without a hue shift
- Frost `#ffffff` for Page canvas for content sections, card surfaces, icon fills on dark hero, button text on dark fills
- Paper `#f7f7f7` for Subtle surface tint alternating with pure white for section banding, elevated card backgrounds when pure white feels too sharp
- Mist `#e5e7eb` for Hairline borders, dividers, nav separator lines, input borders, card outlines - the most-used color in the system by frequency (1231 occurrences), defining structural edges without visual weight
- Ash `#e0e0e0` for Secondary surface fills, muted background panels, subtle hover states - one step deeper than Mist for surfaces that need slightly more presence

- Unica77LLWeb `--font-unica77llweb` for Primary typeface for all UI and editorial text. Weight 400 for body and navigation, weight 600 for subheadings and button labels, weight 700 for product-name hero displays (S6, A5 at 280px) and section headings. The geometric humanist character with its tall x-height carries authority at massive sizes while remaining legible at 12px. The 280px step is the signature - product names function as graphic objects, not text.
- Unica77Mono `--font-unica77mono` for Monospaced companion for technical metadata, spec labels, navigation micro-text, and any data-adjacent content (dimensions, weights, delivery estimates) where tabular alignment matters

## Avoid

- Do not introduce any chromatic color (red, blue, green, purple) to the UI system - the monochromatic discipline IS the brand identity
- Do not use drop shadows, elevation, or blur effects on cards or buttons - flat surfaces only, separated by whitespace and hairlines
- Do not center hero text - always anchor product names left and supporting text right for editorial tension
- Do not set body text below 14px or above 18px; do not set display text below 80px (except the 280px hero step)
- Do not use border-radius values other than 2px (controls), 8px (containers), or 9999px (logo pill) - no 4px, 6px, 12px, 16px, or 24px radii
- Do not add background colors, patterns, or decorative graphics to white content sections - the product and typography carry the visual weight
- Do not use the Gold Award badge color (#FFD700 or similar) as a brand accent - it is a third-party credential, not a design system token

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
