# AI Implementation Prompt

Build a Elva-inspired interface using this source-derived style bundle.

Reference site: https://helloelva.com
Theme: light
Category: Agency
North star: Monumental type on warm concrete

Use these palette anchors:

- Warm Obsidian `#262523` for Primary text, logos, pictogram strokes, structural elements - the near-black with a brown undertone is the only ink in the system and gives the minimalism its printed-on-paper warmth
- Bone White `#ececec` for Page canvas and primary surface - the warm slightly-grayed white fills the entire viewport and provides the breathing room around monumental type
- Pale Ash `#cfcdcd` for Secondary surface and hairline borders - one step darker than the canvas, used for subtle dividers and the rare nested surface
- Pure Black `#000000` for Sparing deep contrast for the smallest marks and AAA contrast anchors - never used for body text (that is always Warm Obsidian)

Use these typography anchors:

- Basis Grotesque `--font-basis-grotesque` for Primary workhorse typeface - carries the entire system from 10px metadata to 640px hero statements. Weight 400 for body and display, 500 for navigation and small labels, 700 reserved for rare emphasis. The extreme size range is the signature: Basis is asked to perform as both a 10px caption and a building-scale poster without switching families.
- Messina Sans `--font-messina-sans` for Secondary editorial display face - reserved for oversized moments at 240px+ where a slightly more humanist, wider-cut character set can break the Basis rhythm. The 1.0 line-height (versus Basis's 0.82) creates a more relaxed, poster-like cadence when both faces appear together.

Use these layout rules:

- Base spacing: 8px.
- Density: spacious.
- Page max-width: .
- Section gap: 80px.
- Card padding: 40px.
- Element gap: 16px.

Build these component patterns where relevant:

- Brand Wordmark: Site identity lockup
- Top Navigation: Primary site navigation
- Contact Email Link: Primary contact affordance
- Display Hero Headline: Monumental typographic statement
- Pictogram Glyph: Typographic flourish replacing a letter
- Section Label Pill: Small marker for content sections
- Inline Newsletter Notice: Compact contextual update with link
- Text Link with Arrow: Primary interactive element (replaces buttons)
- Body Paragraph: Long-form text content

Do:

- Use Basis at 120px+ for every display moment, with line-height 0.90 and letter-spacing -0.06em - the compressed stacking is the signature
- Keep the canvas at #ececec and all ink at #262523 - chromatic color breaks the printed-on-paper warmth
- Maintain section gaps of at least 80px; use 160px+ for the gap above the hero headline
- Replace individual letters in display text with pictogram glyphs (heart, asterisk, peace sign, victory hand) at matching cap-height
- Set body text at 15px with 2.0 line-height - the airy leading is editorial, not utilitarian
- Use 70px border-radius only for pill-shaped tags and section labels; use 10px for any nested surface
- Make every interactive element a text link followed by a arrow - never a filled or outlined button

Avoid:

- Don't introduce filled buttons, outlined buttons, or any button-shaped affordance - text links with arrows are the only interactive pattern
- Don't add drop shadows, gradients, or any elevation effect - depth is communicated through type size and negative space only
- Don't use #000000 for body or display text - always use #262523 to preserve the warm undertone
- Don't center text or constrain it to a max-width container - content left-aligns to the viewport edge for an editorial spread feel
- Don't use color to create hierarchy - use size and weight only
- Don't set display type with line-height above 1.0 - the 0.80-0.90 compression is what makes the headline a monument
- Don't use icons in the traditional UI sense (nav icons, button icons, status icons) - pictograms belong inline with display text only

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
