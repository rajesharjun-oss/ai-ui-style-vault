# Perplexity AI

Source: [Refero Style](https://styles.refero.design/style/e9fff87a-63ce-4c19-840f-98233db62f58)
Reference site: [https://www.perplexity.ai](https://www.perplexity.ai)
Captured: 2026-07-30
Refero published: 2026-04-29T00:14:05.186Z
Refero modified: 2026-06-05T12:44:28.031Z
Theme: light
Category: AI

## Style Summary

Explore Perplexity AI's light AI design system: Aged Paper #faf8f5, Ink Black #000000 colors, pplxSans typography, and DESIGN.md for AI agents.

North star: Warm research terminal. A cream-toned search bar floats on aged-paper canvas, surrounded by quiet monochrome controls - the calm of a library reading desk distilled into a single input field.

## What To Borrow

- Aged Paper `#faf8f5` for Page canvas and card surfaces - warm off-white replaces sterile pure white, giving the interface a document-like, paper-textured quality
- Ink Black `#000000` for Primary text, icon strokes, and the dominant fill across navigation and body copy
- Charcoal `#27251e` for Primary action button background and high-emphasis text - warm near-black that pairs with the cream canvas for a softer than pure-black contrast
- Ash Gray `#72706b` for Secondary text, muted icons, and inactive nav fills - carries the warm tint of the palette
- Stone `#92918b` for Tertiary/placeholder text and low-emphasis labels
- Pebble `#d1d1cd` for Hairline borders on cards and input containers - warm gray that recedes against the cream canvas
- Deep Teal `#016a71` for Sole chromatic accent - active nav indicator and selected state fill, provides the only color punctuation in the interface

- pplxSans `--font-pplxsans` for All interface text - the deliberately narrow scale (3 sizes, 2 weights) makes the system feel document-like. Weight 400 handles body, labels, and input text; weight 500 is reserved for active/selected states and emphasis. The custom typeface is geometric and humanist, tighter and more distinctive than a system sans like Inter. Normal letter-spacing throughout.

## Avoid

- Do not introduce new colors - the palette is deliberately minimal: cream, black, warm grays, and one teal
- Do not use bold weights (600+) - the system maxes at weight 500
- Do not use 0px or 4px border-radius on interactive elements - always pill (9999px) or 12px minimum
- Do not apply heavy shadows or multiple shadow layers - the design is intentionally flat
- Do not use pure white (#ffffff) as a page background - the warm #faf8f5 canvas is a signature choice
- Do not center-align body text - left-align all labels, descriptions, and input text
- Do not use the teal accent decoratively - it signals a functional state (active, selected, live)

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
