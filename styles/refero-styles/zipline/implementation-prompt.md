# AI Implementation Prompt

Build a Zipline-inspired interface using this source-derived style bundle.

Reference site: https://www.zipline.com
Theme: light
Category: Other
North star: open meadow in morning light

Use these palette anchors:

- Meadow Cream `#f7f4e8` for Page canvas, card surfaces, body text inverse, button borders - the warm off-white that gives the whole system its outdoor, paper-like character instead of clinical SaaS white
- Hillside Ink `#000000` for Primary headings, body copy, icon strokes, filled action buttons, hairline borders - maximum-contrast black that lets the cream breathe and makes fkScreamer headlines land
- Stone Border `#c6c3ba` for Muted dividers, secondary surfaces, low-contrast borders - warm gray that sits a step behind Meadow Cream and prevents the canvas from looking flat
- Drone Violet `#643aed` for Card and feature-block backgrounds, accent surfaces - the single chromatic note in an otherwise achromatic system; vivid against the cream so attention-grabbing blocks pop without breaking the editorial mood

Use these typography anchors:

- fkGroteskNeue `--font-fkgroteskneue` for Body copy, navigation, buttons, captions, and any text smaller than the display headlines - the workhorse grotesque that handles all functional UI at 14-22px. The consistent -0.01em tracking keeps it tight even at small sizes.
- fkScreamer `--font-fkscreamer` for Signature display face - used only for oversized editorial statements (40-150px). This is the voice of the brand: ultra-heavy, aggressively condensed, line-height 0.85 so the letters nearly touch. The restraint of using one weight at one role makes the moments it appears feel like magazine pull-quotes, not just headings.
- fkDisplay `--font-fkdisplay` for Mid-weight display variant for sub-statements that need fkScreamer's character at a smaller scale - bridges the gap between the massive editorial type and fkGroteskNeue body

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: 60-128px.
- Card padding: 24px.
- Element gap: 24px.

Build these component patterns where relevant:

- Pill Action Button (Filled Black): Primary conversion action
- Ghost Outline Button: Secondary action or navigation CTA
- Editorial Display Statement: Hero or section-level headline
- Violet Feature Card: Highlighted content block
- Outlined Cream Card: Standard content card on cream canvas
- Full-Bleed Photo Hero: Hero section background
- Top Navigation Bar: Global header
- Inline Thumbnail Token: Embedded visual within display text

Do:

- Use fkScreamer 700 at 90-150px for editorial headlines; line-height 0.85 is non-negotiable - it's what makes the type feel stamped rather than set
- Keep the canvas at Meadow Cream (#f7f4e8) on every body section; reserve stark white for moments you specifically want to feel clinical
- Default all buttons, cards, and images to 20px radius - this single value unifies the system and is the most repeated shape token
- Pair fkGroteskNeue body at 16px/1.4 with fkScreamer displays; never use fkScreamer for anything under 40px
- Reach for Drone Violet (#643aed) only as a card or feature-block surface, never as a text color or border - its job is to make a block pop, not to tint typography
- Use 1px Hillside Ink borders in place of shadows for elevation; the system is flat-by-default and the border carries the separation
- Bleed photography full-bleed in heroes and section dividers; avoid contained rounded image cards at large scale

Avoid:

- Don't use fkScreamer for body copy, navigation, captions, or anything under 40px - the weight and line-height collapse at small sizes
- Don't introduce additional chromatic accent colors; the entire system's restraint depends on having exactly one violet
- Don't add box-shadows to cards or buttons - use 1px borders or the violet surface for separation instead
- Don't use pure white (#ffffff) as a background; Meadow Cream is the canvas and stark white breaks the warm editorial tone
- Don't set body type at anything other than fkGroteskNeue 16px/1.4 as the default - resist the urge to mix in a serif or secondary sans
- Don't apply radii smaller than 20px to interactive elements; buttons, cards, and images all share the same generous rounding
- Don't use letter-spacing on fkScreamer - it ships with normal tracking and the tight glyph spacing is part of its impact

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
