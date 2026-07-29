# Andrei Rybin

Source: [Refero Style](https://styles.refero.design/style/519ca09b-9a85-4eec-8630-0d7aae5ac2da) 
Reference site: [https://andreirybin.com](https://andreirybin.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:16:10.663Z 
Refero modified: 2026-06-03T21:51:21.076Z 
Theme: light 
Category: Design

## Style Summary

Explore Andrei Rybin's light Design design system: Paper #ffffff, Ink #000000 colors, sans-serif, Inter typography, and DESIGN.md for AI agents.

North star: monochrome atelier notebook - a designer's sketchbook where phone screens are pinned like contact sheets on a white wall

## What To Borrow

- Paper `#ffffff` for Page background, card surfaces, image holders - the dominant canvas; everything sits on this
- Ink `#000000` for Primary text, link text, icon strokes, thin section dividers - the only mark-making color
- Graphite `#858585` for Secondary text, muted metadata, and softer border lines that recede behind primary ink
- Stone `#8e8e90` for Cool-toned border and divider strokes for borders that need a hairline without competing with Ink

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- Inter `--font-inter` for Body copy, project captions, and the larger intro paragraphs. Used at a single weight - regularity IS the signature; no bold headlines shout, no light weight whispers.
- system-ui (sans-serif) `--font-system-ui-sans-serif` for Small UI labels, tag text, icon-adjacent microcopy. Appears wherever a single token of body-size type recurs - utility, not statement.
- .SFNSText `--font-sfnstext` for .SFNSText - detected in extracted data but not described by AI

## Avoid

- Do not introduce any chromatic color - no accent, no brand hue, no semantic state color.
- Do not use multiple font weights - Inter 400 is the only voice; no bold, no light, no italic.
- Do not apply shadows, gradients, or fills to tiles or buttons; borders are the only separator.
- Do not center body text - captions and metadata are left- or context-aligned, not centered except where a tile naturally centers its caption beneath.
- Do not use a border radius below 8px on cards or above 16px on icons - the radii carry the system's softness and must stay consistent.
- Do not add navigation patterns (hamburgers, sidebars, mega-menus); the header is a single text strip.
- Do not break the grid with asymmetric or overlapping tile placements - the grid is the page's structural truth.

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
