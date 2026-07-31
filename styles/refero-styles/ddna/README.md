# ddna

Source: [Refero Style](https://styles.refero.design/style/0e8e546b-004c-46b6-a960-5dd88968ae07)
Reference site: [https://d-d-n-a.com](https://d-d-n-a.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:26:23.826Z
Refero modified: 2026-06-05T08:54:35.702Z
Theme: light
Category: E-commerce

## Style Summary

Explore ddna's light E-commerce design system: Stone Charcoal #444242, Linen Cream #efe3dc colors, Basis, Favorit typography, and DESIGN.md for AI agents.

North star: warm museum vitrine on raw linen

## What To Borrow

- Stone Charcoal `#444242` for Primary text, navigation links, hairline borders, footer anchors - dark warm gray carries the same temperature as the cream surfaces it sits on, never pure black
- Linen Cream `#efe3dc` for Heading text, footer surface, and the lighter plane in the surface stack - sits one step above the canvas
- Warm Sand `#dacabf` for Page canvas - the dominant field every section and hero lives on
- Dust `#938a83` for Secondary borders and dividers when Stone Charcoal would be too heavy
- Mortar `#595552` for Muted body text and subdued borders - the quietest readable neutral

- Basis `--font-basis` for Body, nav, labels, captions - the only text family used for everything below display. The 0.066-0.099em tracking on 10-14px is the signature: it makes small text feel like a printed catalogue label rather than screen UI.
- Favorit `--font-favorit` for Display and heading - set at a single 30px size, weight 400 only. The narrow, slightly quirky character shapes (open apertures, subtle inktraps) carry all the personality the system allows. No bold weight exists.

## Avoid

- Do not add drop-shadows, blurs, or any z-axis elevation to cards, buttons, or images
- Do not introduce a brand accent color - the iridescent orbs are content, not tokens
- Do not use bold (600/700) or semibold (500) weights at any level
- Do not use border-radius greater than 0px on any component - sharp edges preserve the printed-catalogue feel
- Do not set body copy below 14px or above 17px; display should stay at 30px
- Do not fill a button background - the system uses text links with arrow glyphs, not filled rectangles
- Do not separate sections with hairline dividers; use 100px of whitespace as the only separator

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
