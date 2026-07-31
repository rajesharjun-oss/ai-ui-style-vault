# AI Implementation Prompt

Build a Erno Forsstrom-inspired interface using this source-derived style bundle.

Reference site: https://erno.works
Theme: light
Category: Agency
North star: editorial gallery on warm paper

Use these palette anchors:

- Ink `#202020` for Body text, headings, project titles, hairline borders, and the bottom edge of links - a soft near-black that reads as flat black at body sizes but never goes dead 000
- Bone `#dfdcdc` for Page canvas and the implicit surface for every project card - a warm off-white with just enough gray to feel like paper, not a screen
- Ash `#cdcecf` for Hairline divider tone that sits one step darker than the canvas to register as a visible rule without becoming a hard line

Use these typography anchors:

- NB Akademie Pro `--font-nb-akademie-pro` for The only font in the system, used at a single weight across every role. 58px at 0.93 line-height carries the hero - lines overlap slightly, creating editorial density. 43px at 1.10 serves medium section heads. 21px at 1.33 is the body, nav, labels, and project metadata - a single typographic voice at conversational size. The 'tnum' feature is active sitewide, forcing tabular figures in any year label or date.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1280px.
- Section gap: 80px.
- Card padding: 0px.
- Element gap: 18px.

Build these component patterns where relevant:

- Tri-Column Header: Persistent site navigation
- Hero Headline Block: Opening statement on the home page
- Section Heading Label: Introduces a content band (e.g. 'Featured', '2018-2020')
- Project Card (Featured): Hero project entry in the featured band
- Project Card (Grid): Standard two-up project entry
- Hairline Divider: Marks the end of a content section
- Period Label: Date range heading for a chronological grouping (e.g. '2018-2020')
- Inline Text Link: Navigation between pages (Works, About, project titles)

Do:

- Use NB Akademie Pro (or Inter as substitute) at weight 400 for every text element - never introduce a second weight or a second family
- Set the hero headline at 58px with line-height 0.93 and letter-spacing -2.9px so lines physically overlap
- Keep the canvas at #dfdcdc and ink at #202020 - the warm off-white is a brand choice, not a fallback
- Let project images sit edge-to-edge with the content column: zero radius, zero border, zero shadow
- Separate sections with a 1px hairline in #cdcecf rather than background-color changes or extra whitespace bands
- Use the 21px body size for nav, labels, titles, and metadata - hierarchy is built from size jumps (21 43 58), not from weight or color
- Activate tabular numerals ("tnum") site-wide so year labels and dates align on the decimal

Avoid:

- Don't add a CTA button, a colored accent, or a filled background - this system has no primary action surface
- Don't round image corners, add drop shadows, or apply any elevation to project cards
- Don't introduce a second typeface, a serif companion, or a different weight of NB Akademie Pro
- Don't use white (#ffffff) as the canvas - #dfdcdc is the signature warm paper tone
- Don't break the three-size type scale (21 / 43 / 58) with intermediate steps; the gap between sizes is the hierarchy
- Don't underline links by default - use the bottom border in #202020 only on hover/active to signal interaction
- Don't add gradients, colored badges, tags, or status pills - the system is strictly two-color

Source prompt cues:

**Quick Color Reference**
- text: #202020
- background: #dfdcdc
- border: #cdcecf (hairline), #202020 (link active state)
- accent: none
- primary action: no distinct CTA color

**Example Component Prompts**

1. *Hero headline paragraph*: Bone (#dfdcdc) canvas. Text at 58px NB Akademie Pro weight 400, color #202020, line-height 0.93, letter-spacing -2.9px. Left-aligned, occupying roughly 70% of the 1280px content width. No accompanying image, no button, no border.

2. *Project card (two-up grid)*: Image filling half the content width, zero border-radius, zero shadow, sitting directly on the #dfdcdc canvas with 18px column gap to the next card. Below the image: title in 21px NB Akademie Pro #202020, then 8px gap, then one-line label in 21px #202020.

3. *Tri-column header*: Single row with three inline groups at 21px NB Akademie Pro weight 400, color #202020, line-height 1.33, letter-spacing -0.32px. Left group: name. Center group: discipline label. Right group: two text links (Works, About). No background, no border, no logo.

4. *Section divider*: 1px horizontal line in #cdcecf spanning the full content width, with 42px space above and 31px space below. No label, no icon, no ornament.

5. *Period label*: Set in 58px NB Akademie Pro #202020, line-height 0.93, letter-spacing -2.9px - the same display treatment as the hero, but acting as a section heading (e.g. '2018-2020'). Left-aligned to the content edge. Use a real en-dash, not a hyphen.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
