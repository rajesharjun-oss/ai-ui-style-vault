# AI Implementation Prompt

Build a Uniswap Cup-inspired interface using this source-derived style bundle.

Reference site: https://unicup.uniswap.org
Theme: light
Category: Crypto
North star: Esports broadcast on a wireframe court - a pink highlighter tracing through a grid of white boxes and hairline rules.

Use these palette anchors:

- Bracket Pink `#f50db4` for Pink outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color
- Graphite Black `#000000` for Primary text, icon fills, team-name boxes, score text - the typographic and structural anchor
- Page White `#ffffff` for Page canvas, inverted text on dark or pink nodes
- Off-Black `#222222` for Secondary headings and subdued text - softer than pure black for non-critical labels
- Wire Gray `#f2f2f2` for Hairline borders, divider rules, bracket connector lines, card outlines - the structural skeleton of the entire diagram
- Blush Wash `#fef4ff` for Soft pink-tinted surface for highlighted match cards and accent panel backgrounds - pink diluted almost to white

Use these typography anchors:

- ui-sans-serif `--font-ui-sans-serif` for System sans-serif for body text, team names, labels, and UI chrome. Small scale (12-16px) and tight line-heights keep the bracket compact; weight 500-600 for labels, 400 for secondary text. Substitute: Inter, -apple-system, or any geometric sans.
- ui-monospace `--font-ui-monospace` for Monospace for all numerical scores, stage labels (R16, QF, SF), the UNISWAP CUP wordmark, and the central VS separator. Weight 700 at 32px for hero match scores with -0.02em tracking; weight 500 at 12px for stage markers. This monospace handling is signature - numbers and stages read like broadcast graphics, not body text. Substitute: JetBrains Mono, IBM Plex Mono, SF Mono.
- Basel `--font-basel` for Custom brand face used sparingly for select body text passages - a single weight (500) suggests Basel Grotesk or a geometric grotesque chosen for its even, technical character. Substitute: Inter or Sohne at weight 500.

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: .
- Section gap: 24px.
- Card padding: 8px.
- Element gap: 4-8px.

Build these component patterns where relevant:

- Bracket Connector Line: Structural diagram edge
- Winner Node (Pink Filled Box): Highlighted match result box
- Team Identity Box (Black Filled): Team name or avatar container
- Stage Label Tag (R16 / QF / SF): Round-of-tournament marker
- Status Pill (WINNER / Final / Road to final): Match-state annotation
- Central VS Separator: Final-match divider
- Header Nav Tags (GROUP STAGE / LIVESTREAM): Top navigation chips
- Uniswap Cup Wordmark: Page title lockup
- Tournament Bracket Frame: Full-page layout container
- Match Date/Time Label: Scheduling annotation

Do:

- Use #f50db4 exclusively for highlighted/winning states, stage tags, and the final-match callout - never as a decorative background fill on large areas
- Keep all component corners at 0px radius - the design is deliberately square and diagrammatic
- Use monospace (ui-monospace) for all numbers, scores, stage labels, and the wordmark; use system sans-serif for body and team names
- Draw bracket connectors as 1px orthogonal lines in #f2f2f2 with right-angle turns, never curves or diagonals
- Apply -0.02em letter-spacing to all monospace text at 32px and above to tighten the broadcast-graphic feel
- Use #fef4ff as a soft accent surface behind highlighted match cards - it is a diluted pink, not a full brand fill
- Keep the layout full-bleed and symmetrical; the bracket is the page, not a component within the page

Avoid:

- Do not add shadows, gradients, or any elevation effects - the system is intentionally flat and diagrammatic
- Do not introduce border-radius above 0px on any bracket node, tag, or structural element
- Do not use #f50db4 for body text or large background fills - it is a highlighter, not a paint roller
- Do not use a second accent color - the entire chromatic system is one pink; any second hue breaks the broadcast language
- Do not use serif, display, or decorative typefaces - system sans and monospace only
- Do not add card padding beyond 8px or section gaps beyond 24px - the design is compact and diagrammatic, not spacious
- Do not wrap the bracket in a max-width container or centered column - it must span the full viewport to maintain symmetry

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #ffffff
- border: #f2f2f2
- accent: #f50db4 (Bracket Pink)
- highlight surface: #fef4ff
- primary action: no distinct CTA color

**Example Component Prompts**

1. Create a tournament bracket node: 0px radius square, 24x24px, filled #f50db4 with white monospace text at 12px weight 700 (e.g. the score '6'). No shadow, no border.

2. Create a stage label tag: filled #f50db4 rectangle, 0px radius, 8px padding, white monospace text at 12px weight 500 (e.g. 'QF'). No border, no shadow.

3. Create a team identity box: 0px radius square, 32x32px, filled #000000, white icon glyph or monospace letter centered inside. No border, no shadow. Place adjacent to a white box with the score in black 16px weight 600.

4. Create the central VS separator: monospace text 'VS' at 40px weight 700, color #f50db4, centered between two finalist groups. Below it, 'Final' in the same color and font at 32px.

5. Create a bracket connector: a 1px line in #f2f2f2 with orthogonal right-angle turns, no curves, connecting two nodes vertically and horizontally. Change the last segment to #f50db4 to indicate the winning path.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
