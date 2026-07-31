# ARTWORLD

Source: [Refero Style](https://styles.refero.design/style/bab94db1-25ec-459d-8c81-5905a0324b65)
Reference site: [https://artworld.agency](https://artworld.agency)
Captured: 2026-07-31
Refero published: 2026-04-30T02:50:15.516Z
Refero modified: 2026-06-05T09:59:25.222Z
Theme: light
Category: Agency

## Style Summary

Explore ARTWORLD's light Agency design system: Ink Black #000000, Paper White #ffffff colors, Graphik Light, Cardinal Fruit (and Italic / Classic Italic...

North star: fashion masthead on white linen

## What To Borrow

- Ink Black `#000000` for All text, the ARTWORLD wordmark, hairline structural borders, link strokes - the only mark-making color in the entire system
- Paper White `#ffffff` for Page canvas, negative space between type, reverse text on the wordmark bar

- Graphik Light `--font-graphik-light` for The invisible support system - body text, captions, metadata, role tags, the legend, the info link. Weight 300 is deliberately thin: it recedes so the Cardinal Fruit can dominate. This is the typographic equivalent of using whisper voice in a conversation where someone else is speaking. The consistent -0.065em letter-spacing tightens the already-light forms, giving the sans-serif an editorial density that prevents it from feeling like default UI text.
- Cardinal Fruit (and Italic / Classic Italic variants) `--font-cardinal-fruit-and-italic-classic-italic-variants` for The editorial display voice - used for talent names, artist credits, and any moment of typographic expression. The italic variant carries the romantic, fashion-magazine feeling while the upright version provides structural headlines. Custom serif with high contrast strokes, used at extreme sizes (65-75px) to dominate the page. The whisper weight (300) on such a large serif is anti-convention: most editorial serifs use 400-700 here, but the light cuts create airier letterforms that feel more printed than digital.
- Cardinal Fruit Italic `--font-cardinal-fruit-italic` for Cardinal Fruit Italic - detected in extracted data but not described by AI
- Cardinal Classic Italic `--font-cardinal-classic-italic` for Cardinal Classic Italic - detected in extracted data but not described by AI

## Avoid

- Do not add any color beyond black and white. No accent colors, no state colors, no hover tints. Monochrome is the brand.
- Do not use rounded corners. Every edge is sharp, every surface is flat. The system has no curves.
- Do not add shadows, gradients, or elevation effects. The design is completely flat - depth comes from type size contrast, not from visual effects.
- Do not use bold or semibold weights for body or display type. The system lives at 300. Heavier weights break the whisper voice.
- Do not use system sans-serifs (Arial, Helvetica, Roboto) as substitutes for Graphik Light. The lightness and tight tracking of Graphik are what make it disappear correctly.
- Do not center-align body text or grid items. The ragged left edge is a design feature, not a limitation.
- Do not add icons, illustrations, photography, or decorative graphics. This is a typography-only system. The wordmark is the only visual element that isn't running text.

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
