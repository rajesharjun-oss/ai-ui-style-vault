# Lovable

Source: [Refero Style](https://styles.refero.design/style/9ff62d34-e48d-4fcb-9fd9-c018e2747542)
Reference site: [https://lovable.dev](https://lovable.dev)
Captured: 2026-07-30
Refero published: 2026-04-30T00:44:25.243Z
Refero modified: 2026-06-05T12:23:55.499Z
Theme: light
Category: AI

## Style Summary

Explore Lovable's light AI design system: Parchment #fcfbf8, Warm Sand #f7f4ed colors, Camera Plain Variable typography, and DESIGN.md for AI agents.

North star: Warm parchment canvas behind a single prismatic horizon

## What To Borrow

- Parchment `#fcfbf8` for Page canvas, primary background, card surfaces when on darker parents
- Warm Sand `#f7f4ed` for Card backgrounds, elevated surface panels, secondary containers
- Linen Border `#eceae4` for All borders - nav dividers, card outlines, input strokes, section separators. Warm beige rather than cool gray gives the entire UI its distinctive non-tech softness
- Stone `#d4d3d0` for Subtle box-shadow tints, disabled borders, secondary dividers
- Dim Gray `#5f5f5d` for Secondary text, placeholder text, muted nav labels, subheadings
- Charcoal `#1c1c1c` for Primary text, nav labels, icon fills, inverse button background. Near-black rather than pure black keeps the warm tone consistent
- Ink `#030303` for Highest-emphasis text (hero headline, button labels in chat input), icon fills
- Indigo Accent `#3451b2` for Reserved accent from CSS tokens (--bg-accent). Inline text links, focus rings, accent highlights when needed

- Camera Plain Variable `--font-camera-plain-variable` for The only typeface on the entire site. A custom variable-weight sans-serif that carries both body text and display headlines. The 480 weight is unusual - heavier than normal but not semi-bold, giving headlines a confident but non-aggressive stance. Ligatures are explicitly disabled ("liga" 0), keeping the letterforms mechanical and preventing decorative swashes.

## Avoid

- Never use cool grays (#e5e7eb, #6b7280) - all neutrals skew warm with a yellow undertone; cool grays would break the parchment atmosphere
- Never apply colored backgrounds to buttons; the primary action is near-black (rgba(0,0,0,0.88)) and secondary is transparent - there is no colored CTA
- Never use drop shadows for elevation except on the chat input card; most cards and surfaces are flat with no shadow at all
- Never use more than one font family - Camera Plain Variable (or its substitute) handles everything from 14px captions to 60px display headlines
- Never use sharp corners (0px radius) on interactive elements; even image thumbnails get 12px radius
- Never use the hero gradient colors on individual UI components like buttons, badges, or icons - the gradient exists only as a full-bleed atmospheric background
- Never add visual weight to feature sections with icons, colored badges, or decorative elements - this system communicates through type weight and scale alone

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
