# AI Implementation Prompt

Build a Perplexity AI-inspired interface using this source-derived style bundle.

Reference site: https://www.perplexity.ai
Theme: light
Category: AI
North star: Warm research terminal. A cream-toned search bar floats on aged-paper canvas, surrounded by quiet monochrome controls - the calm of a library reading desk distilled into a single input field.

Use these palette anchors:

- Aged Paper `#faf8f5` for Page canvas and card surfaces - warm off-white replaces sterile pure white, giving the interface a document-like, paper-textured quality
- Ink Black `#000000` for Primary text, icon strokes, and the dominant fill across navigation and body copy
- Charcoal `#27251e` for Primary action button background and high-emphasis text - warm near-black that pairs with the cream canvas for a softer than pure-black contrast
- Ash Gray `#72706b` for Secondary text, muted icons, and inactive nav fills - carries the warm tint of the palette
- Stone `#92918b` for Tertiary/placeholder text and low-emphasis labels
- Pebble `#d1d1cd` for Hairline borders on cards and input containers - warm gray that recedes against the cream canvas
- Deep Teal `#016a71` for Sole chromatic accent - active nav indicator and selected state fill, provides the only color punctuation in the interface

Use these typography anchors:

- pplxSans `--font-pplxsans` for All interface text - the deliberately narrow scale (3 sizes, 2 weights) makes the system feel document-like. Weight 400 handles body, labels, and input text; weight 500 is reserved for active/selected states and emphasis. The custom typeface is geometric and humanist, tighter and more distinctive than a system sans like Inter. Normal letter-spacing throughout.

Use these layout rules:

- Base spacing: 8px.
- Density: compact.
- Page max-width: 640px.
- Section gap: 32px.
- Card padding: 12px.
- Element gap: 8px.

Build these component patterns where relevant:

- Search Input: Central input field - the primary action surface of the product
- Primary Submit Button: Search submission - the only filled dark button in the interface
- Sidebar Nav Item: Left rail navigation links
- Top Nav Link: Horizontal category links in the header
- Mode Toggle Chip: Inline capability selector within the search input
- Status Card: System/connection status notification below the search
- Skeleton Placeholder: Loading state for content cards
- Sign In Button: Authentication entry at sidebar bottom
- Model Selector: Dropdown trigger for AI model selection

Do:

- Use 9999px border-radius for all interactive controls (buttons, nav items, toggle chips, tags)
- Maintain the narrow type scale: 12px caption, 14px body-sm, 16px body - do not introduce sizes outside this set
- Set all card and input backgrounds to #ffffff on the #faf8f5 canvas to create the paper-on-paper layering effect
- Use 1px #d1d1cd borders for all container separation - avoid shadows except the single whisper-soft card shadow
- Use #016a71 teal only for active/selected state indicators - it should appear on fewer than 5% of elements
- Keep the main content column at 640px max-width centered - the search bar is the focal point, not a wide canvas
- Use pplxSans weight 500 exclusively for emphasis and active states; weight 400 for all default and body text

Avoid:

- Do not introduce new colors - the palette is deliberately minimal: cream, black, warm grays, and one teal
- Do not use bold weights (600+) - the system maxes at weight 500
- Do not use 0px or 4px border-radius on interactive elements - always pill (9999px) or 12px minimum
- Do not apply heavy shadows or multiple shadow layers - the design is intentionally flat
- Do not use pure white (#ffffff) as a page background - the warm #faf8f5 canvas is a signature choice
- Do not center-align body text - left-align all labels, descriptions, and input text
- Do not use the teal accent decoratively - it signals a functional state (active, selected, live)

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
