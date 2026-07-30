# AI Implementation Prompt

Build a Wemakethings-inspired interface using this source-derived style bundle.

Reference site: https://wemakethings.de
Theme: light
Category: Agency
North star: Brutalist editorial broadsheet - ink-on-white architecture with type as the only building material.

Use these palette anchors:

- Ink Black `#000000` for Primary text, all borders, outline strokes, link underlines, background type fill
- Paper White `#ffffff` for Page canvas, card surface, filled button background

Use these typography anchors:

- Maison Neue `--font-maison-neue` for Primary UI and headline typeface - used for nav links, body copy, button text, and bold all-caps hero statements. The 65px weight 500 is the signature headline voice: tight leading (1.11), all-caps, commanding without decorative weight. Substitute: Inter, Helvetica Neue, Neue Haas Grotesk
- BASEBLOOM `--font-basebloom` for Architectural display layer - rendered as massive outlined characters (864px, line-height 0.83) that sit behind body content as visual scaffolding, never carrying readable information. Substitute: a custom ultra-condensed display face or CSS stroke text
- Unzyale `--font-unzyale` for Rare secondary display use - appears in link context at 58px as a typographic accent. Substitute: a condensed or script contrast face

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: 80-120px.
- Card padding: 20px.
- Element gap: 20px.

Build these component patterns where relevant:

- Top Navigation Bar: Site-wide header
- Logo Mark: Brand identifier
- Hero Headline Statement: Opening page message
- Architectural Background Type: Decorative typographic layer
- Body Paragraph: Informational text
- Inline Section Label: Small typographic tag
- Brand Column Card: Brand listing entry
- Text Link with Arrow: Navigation and CTA link
- Scroll Indicator: Page-scroll affordance
- Section Divider: Inter-section separator

Do:

- Use only #000000 and #ffffff - no chromatic colors anywhere in the UI
- Set all headlines in Maison Neue weight 500, all-caps, 43-65px with tight 1.11 line-height
- Render at least one massive outlined display type element (800px+) as architectural scaffolding behind primary content
- Separate brand listings with 1px black hairline borders, not background fills or shadows
- Use Maison Neue weight 400 at 16px with 1.33 line-height for all body copy
- Append arrow characters to nav links and CTAs - the arrow IS the affordance
- Maintain 80-120px vertical padding between major sections

Avoid:

- Never introduce color, gradients, or tinted backgrounds - the system is strictly monochromatic
- Never use border-radius on buttons, cards, inputs, or tags - all corners are sharp at 0px
- Never add drop shadows or box-shadows - depth comes from typographic layering, not elevation
- Never use photographic imagery or illustration - type is the only visual material
- Never use rounded or soft type - all display text is all-caps with tight leading
- Never center body paragraphs - left-align with a constrained reading column
- Never decorate links with fills, pills, or button chrome - links are bare text with optional underline and arrow

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
