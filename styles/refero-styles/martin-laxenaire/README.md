# Martin Laxenaire

Source: [Refero Style](https://styles.refero.design/style/0e8db8d0-4d8f-48ac-a8e7-aaea9601e3ce)
Reference site: [https://www.martin-laxenaire.fr](https://www.martin-laxenaire.fr)
Captured: 2026-07-31
Refero published: 2026-04-30T03:00:11.860Z
Refero modified: 2026-06-05T10:26:12.942Z
Theme: light
Category: Agency

## Style Summary

Explore Martin Laxenaire's light Agency design system: Ink Black #121212, Paper White #ffffff colors, MonumentExtended UltraBold, MonumentExtended Regular...

North star: kinetic poster crashing through liquid color waves

## What To Borrow

- Ink Black `#121212` for Primary text, all borders, icon strokes, the dominant UI color - every word and divider is this near-black
- Paper White `#ffffff` for Page canvas, surface background, button fills for outlined ghost controls
- Blush Wash `#f9d9f7` for Hero art backdrop, accent surface - the soft pink that hosts the fluid color-shape composition

- MonumentExtended UltraBold `--font-monumentextended-ultrabold` for Display and heading voice - used at extreme sizes (94-419px) with crushed line-height (0.75-0.85) to create block-of-ink typographic moments. This is the site's signature: oversized, nearly touching, black slab letterforms that read as physical print objects, not web text. At smaller sizes (18-21px) it serves nav and icon labels.
- MonumentExtended Regular `--font-monumentextended-regular` for Secondary display weight - used for subheadings and link labels where UltraBold would be excessive. The Regular cut retains the same wide proportions but with thinner strokes, creating a secondary rhythm below the UltraBold roars.
- Swiss `--font-swiss` for Body and utility voice - the invisible workhorse for paragraphs, button labels, footer text, list items. At 31px it steps into subheading territory. Its neutral, humanist sans character prevents the MonumentExtended from exhausting the reader.

## Avoid

- Never use color on functional UI elements - buttons, links, tags, and text are always #121212 on #ffffff
- Never use drop shadows, box-shadows, or any elevation - the design is poster-flat
- Never use border-radius other than 20.93px (for controls) or 0px (for surfaces) - no mixed rounding
- Never set body text larger than 31px or with line-height above 1.20 - the utility voice must stay quiet
- Never use decorative icons or illustrations outside the hero wave composition - the rest of the page is type-only
- Never use #f9d9f7 as a card, section, or component background - it exists solely as the wave-art field
- Never add more than one wave-art composition per page - the collision of monochrome and color is a single-moment effect

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
