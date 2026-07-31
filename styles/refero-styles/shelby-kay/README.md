# Shelby Kay

Source: [Refero Style](https://styles.refero.design/style/2ab2f666-6da7-4cd8-bc91-52a28bd560ad)
Reference site: [https://shelbykay.dev](https://shelbykay.dev)
Captured: 2026-07-31
Refero published: 2026-04-30T03:53:27.919Z
Refero modified: 2026-06-05T10:59:41.659Z
Theme: light
Category: Agency

## Style Summary

Explore Shelby Kay's light Agency design system: Olive Ink #393c2a, Sage Type #737955 colors, Ranade, Switzer typography, and DESIGN.md for AI agents.

North star: botanical editorial spread on warm linen - two-color ink system on aged paper, with display type that bleeds past the page edge and metadata that whispers from the margins.

## What To Borrow

- Olive Ink `#393c2a` for Primary text, borders, and structural strokes - all type from body to display headings, all card and image borders, all interactive outlines
- Sage Type `#737955` for Display headings and brand voice - used for the monumental SHELBY wordmark, section anchors, and selective heading accents that carry the brand's botanical identity
- Linen `#efe6d9` for Primary canvas and card surfaces - page background, card fills, the base warm tone the entire system sits on
- Sienna `#d6b292` for Orange wash for highlight backgrounds, decorative bands, and soft emphasis behind content.
- Driftwood `#afa199` for Tertiary surface and muted helpers - profile-section backdrop, desaturated metadata, low-emphasis UI text and dividers
- Riverstone `#7b8785` for Cool-toned neutral for subtle contrast shifts - secondary surface, hover or muted state for UI elements needing visual separation from the warm base

- Ranade `--font-ranade` for Display and editorial headlines. Used at extreme scale (83-265px) for the wordmark and section anchors, and at 24px for the CONTACT callout. The geometric, slightly condensed forms give the brand its monumental-but-restrained voice - the type fills the frame without shouting. Substitute: Boldonse or Bold Neue for display, Space Grotesk for smaller uses.
- Switzer `--font-switzer` for Everything else: body copy, nav, labels, metadata, card titles, list items. The compact grotesque reads as editorial running text. Weight 500-600 is the workhorse range; 700 is reserved for section headers and emphasized nav. Substitute: Inter, Untitled Sans, or Suisse Int'l for full weight coverage.

## Avoid

- Don't add drop shadows, glows, or any CSS elevation - the system is deliberately flat and print-like.
- Don't introduce rounded corners (border-radius > 0) on any element - it breaks the editorial metaphor.
- Don't use Sage Type (#737955) for body text - its 3.7:1 contrast on Linen fails readability standards. Reserve it for display headings only.
- Don't create filled button backgrounds in any color - this system has no CTA buttons. Navigation is text-only, contact is a typographic anchor.
- Don't use gradients, brand illustrations, or icon sets - the visual language is photography, type, and tonal layering only.
- Don't use any cool or neutral gray outside the Riverstone (#7b8785) token - all neutrals must stay warm to maintain the botanical atmosphere.
- Don't center body text. Left-align everything except section anchors, which are the only elements that get centered treatment.

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
