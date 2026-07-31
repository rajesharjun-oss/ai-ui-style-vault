# Cards Against Humanity

Source: [Refero Style](https://styles.refero.design/style/51b5d80e-d898-4d70-bd16-9e50406e014c)
Reference site: [https://www.cardsagainsthumanity.com](https://www.cardsagainsthumanity.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:34:26.528Z
Refero modified: 2026-06-05T09:24:15.072Z
Theme: dark
Category: Media

## Style Summary

Explore Cards Against Humanity's dark Media design system: Game Night Black #000000, Card White #ffffff colors, Helvetica Neue LT, Helvetica Neue...

North star: Scattered playing cards on a velvet game table - the design language is the game itself, not a wrapper around it.

## What To Borrow

- Game Night Black `#000000` for Page background, card shadows, button borders, heading text on light surfaces
- Card White `#ffffff` for Card surfaces, body text on dark, button borders, input fills
- Signal Red `#fe2f2f` for Primary accent border on cards and badges - the brand's loudest punctuation, used as outline not fill
- Royal Violet `#7333f1` for Primary accent border on cards and badges - deep saturated purple carrying the brand's irreverent energy
- Antique Gold `#d7b73b` for Primary accent border on cards and badges - warm yellow-gold that rounds out the three-color system
- Lemon Card `#fffe5b` for Card face fill for highlighted playing cards in the scattered background
- Lavender Card `#ede5ff` for Card face fill for pastel playing cards, soft purple surface
- Cobalt Card `#1b5bff` for Card face fill for blue playing cards, saturated blue accent surface
- Sky Card `#a0e9ff` for Card face fill for light blue playing cards
- Bubblegum Card `#ffa0f0` for Card face fill for pink playing cards
- Mint Card `#b4ff91` for Card face fill for green playing cards
- Tangerine Card `#ff9559` for Card face fill for orange playing cards

- Helvetica Neue LT `--font-helvetica-neue-lt` for The site's sole typeface. Weight 800 dominates everything from body up through 80px display - this anti-hierarchy choice makes the brand feel like it's shouting a punchline rather than presenting information. Tight leading at display sizes (0.98-1.07) creates an impactful block, generous leading on body (2.0-2.86) lets the heavy weight breathe. No letter-spacing tricks; the geometry of Helvetica at 800 weight does all the work.
- Helvetica Neue `--font-helvetica-neue` for Helvetica Neue - detected in extracted data but not described by AI

## Avoid

- Don't use weight 400 for anything above 16px - the site's voice is uniformly heavy
- Don't apply drop shadows for elevation - the 2px inset border system is the only depth treatment
- Don't fill large areas with chromatic color - accent colors are outlines, not backgrounds
- Don't use border-radius below 13px on cards or below 32px on buttons - the geometry must read as physical cards
- Don't add gradient fills - the palette is strictly flat, the only complexity comes from scattered card composition
- Don't use letter-spacing tricks - the raw Helvetica geometry at weight 800 is the entire typographic system
- Don't introduce blues, greens, or pinks as UI chrome - those colors exist only as card face fills in decorative scatter

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
