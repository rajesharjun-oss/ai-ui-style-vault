# Laura Monin

Source: [Refero Style](https://styles.refero.design/style/2b9e90ad-51d9-4f29-8f7e-a343dc741eab)
Reference site: [https://lauramonin.com](https://lauramonin.com)
Captured: 2026-07-31
Refero published: 2026-04-30T01:56:30.973Z
Refero modified: 2026-06-05T08:18:20.090Z
Theme: light
Category: Agency

## Style Summary

Explore Laura Monin's light Agency design system: Paper White #ffffff, Ink Black #000000 colors, title, neue-haas-grotesk-display typography, and DESIGN.md...

North star: editorial gallery wall, white marble, ink stamp

## What To Borrow

- Paper White `#ffffff` for Page canvas, card surfaces, image borders, nav backgrounds - the only surface tone in the system
- Ink Black `#000000` for Primary text, all border outlines on images and nav, list markers - the sole chromatic anchor

- title `--font-title` for Display serif used exclusively for the brand title and hero headlines. The custom serif - with its high contrast strokes and slightly condensed forms - carries all brand identity. Letter-spacing of -0.018em tightens the large caps just enough to feel deliberate without becoming stiff. A close substitute would be a transitional or didone-style serif like 'GT Sectra Display' or free options 'Playfair Display' / 'DM Serif Display'
- neue-haas-grotesk-display `--font-neue-haas-grotesk-display` for All UI, navigation, captions, metadata, and body-adjacent text. Geometric grotesque at a single weight (400) - the system deliberately avoids bold/light contrast, using size and placement to create hierarchy instead. Use 'Inter' or 'Neue Haas Grotesk' itself (free via Adobe) as substitutes

## Avoid

- Do not add drop shadows, glows, or any box-shadow to any element - the design is intentionally flat
- Do not use rounded corners (border-radius > 0) on any image, card, or button
- Do not introduce accent colors, gradients, or background fills - the system is strictly black on white
- Do not use bold or semibold weights for UI text - weight 400 at all sizes is the rule
- Do not align images to a uniform grid with equal gutters - the asymmetric scatter is the layout identity
- Do not add hover animations, transitions, or micro-interactions to navigation or links
- Do not use sans-serif or grotesque fonts for headlines or display text - the serif carries all brand weight

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
