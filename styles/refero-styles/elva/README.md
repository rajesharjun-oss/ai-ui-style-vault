# Elva

Source: [Refero Style](https://styles.refero.design/style/9568198a-5a51-4cbb-9dc3-b7610757cdd6)
Reference site: [https://helloelva.com](https://helloelva.com)
Captured: 2026-07-31
Refero published: 2026-02-15T14:11:52.000Z
Refero modified: 2026-06-05T08:36:58.558Z
Theme: light
Category: Agency

## Style Summary

Explore Elva's light Agency design system: Warm Obsidian #262523, Bone White #ececec colors, Basis Grotesque, Messina Sans typography, and DESIGN.md for AI...

North star: Monumental type on warm concrete

## What To Borrow

- Warm Obsidian `#262523` for Primary text, logos, pictogram strokes, structural elements - the near-black with a brown undertone is the only ink in the system and gives the minimalism its printed-on-paper warmth
- Bone White `#ececec` for Page canvas and primary surface - the warm slightly-grayed white fills the entire viewport and provides the breathing room around monumental type
- Pale Ash `#cfcdcd` for Secondary surface and hairline borders - one step darker than the canvas, used for subtle dividers and the rare nested surface
- Pure Black `#000000` for Sparing deep contrast for the smallest marks and AAA contrast anchors - never used for body text (that is always Warm Obsidian)

- Basis Grotesque `--font-basis-grotesque` for Primary workhorse typeface - carries the entire system from 10px metadata to 640px hero statements. Weight 400 for body and display, 500 for navigation and small labels, 700 reserved for rare emphasis. The extreme size range is the signature: Basis is asked to perform as both a 10px caption and a building-scale poster without switching families.
- Messina Sans `--font-messina-sans` for Secondary editorial display face - reserved for oversized moments at 240px+ where a slightly more humanist, wider-cut character set can break the Basis rhythm. The 1.0 line-height (versus Basis's 0.82) creates a more relaxed, poster-like cadence when both faces appear together.

## Avoid

- Don't introduce filled buttons, outlined buttons, or any button-shaped affordance - text links with arrows are the only interactive pattern
- Don't add drop shadows, gradients, or any elevation effect - depth is communicated through type size and negative space only
- Don't use #000000 for body or display text - always use #262523 to preserve the warm undertone
- Don't center text or constrain it to a max-width container - content left-aligns to the viewport edge for an editorial spread feel
- Don't use color to create hierarchy - use size and weight only
- Don't set display type with line-height above 1.0 - the 0.80-0.90 compression is what makes the headline a monument
- Don't use icons in the traditional UI sense (nav icons, button icons, status icons) - pictograms belong inline with display text only

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
