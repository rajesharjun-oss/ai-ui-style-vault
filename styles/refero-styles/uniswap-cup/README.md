# Uniswap Cup

Source: [Refero Style](https://styles.refero.design/style/fabb51a0-0f83-4177-b83e-4969705a389c)
Reference site: [https://unicup.uniswap.org](https://unicup.uniswap.org)
Captured: 2026-07-31
Refero published: 2026-04-30T00:30:35.576Z
Refero modified: 2026-06-05T10:00:53.758Z
Theme: light
Category: Crypto

## Style Summary

Explore Uniswap Cup's light Crypto design system: Bracket Pink #f50db4, Graphite Black #000000 colors, ui-sans-serif, ui-monospace typography, and DESIGN.md...

North star: Esports broadcast on a wireframe court - a pink highlighter tracing through a grid of white boxes and hairline rules.

## What To Borrow

- Bracket Pink `#f50db4` for Pink outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color
- Graphite Black `#000000` for Primary text, icon fills, team-name boxes, score text - the typographic and structural anchor
- Page White `#ffffff` for Page canvas, inverted text on dark or pink nodes
- Off-Black `#222222` for Secondary headings and subdued text - softer than pure black for non-critical labels
- Wire Gray `#f2f2f2` for Hairline borders, divider rules, bracket connector lines, card outlines - the structural skeleton of the entire diagram
- Blush Wash `#fef4ff` for Soft pink-tinted surface for highlighted match cards and accent panel backgrounds - pink diluted almost to white

- ui-sans-serif `--font-ui-sans-serif` for System sans-serif for body text, team names, labels, and UI chrome. Small scale (12-16px) and tight line-heights keep the bracket compact; weight 500-600 for labels, 400 for secondary text. Substitute: Inter, -apple-system, or any geometric sans.
- ui-monospace `--font-ui-monospace` for Monospace for all numerical scores, stage labels (R16, QF, SF), the UNISWAP CUP wordmark, and the central VS separator. Weight 700 at 32px for hero match scores with -0.02em tracking; weight 500 at 12px for stage markers. This monospace handling is signature - numbers and stages read like broadcast graphics, not body text. Substitute: JetBrains Mono, IBM Plex Mono, SF Mono.
- Basel `--font-basel` for Custom brand face used sparingly for select body text passages - a single weight (500) suggests Basel Grotesk or a geometric grotesque chosen for its even, technical character. Substitute: Inter or Sohne at weight 500.

## Avoid

- Do not add shadows, gradients, or any elevation effects - the system is intentionally flat and diagrammatic
- Do not introduce border-radius above 0px on any bracket node, tag, or structural element
- Do not use #f50db4 for body text or large background fills - it is a highlighter, not a paint roller
- Do not use a second accent color - the entire chromatic system is one pink; any second hue breaks the broadcast language
- Do not use serif, display, or decorative typefaces - system sans and monospace only
- Do not add card padding beyond 8px or section gaps beyond 24px - the design is compact and diagrammatic, not spacious
- Do not wrap the bracket in a max-width container or centered column - it must span the full viewport to maintain symmetry

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
