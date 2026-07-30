# AI Implementation Prompt

Build a Stellar-inspired interface using this source-derived style bundle.

Reference site: https://www.stellar.work
Theme: dark
Category: Agency
North star: Gallery wall at midnight

Use these palette anchors:

- Void Black `#000000` for Page background, primary canvas - absolute black eliminates surface depth, making images and white type feel like they float
- Obsidian `#171718` for Card surfaces, elevated panels, designer profile containers - one shade above void to separate without illuminating
- Graphite `#2c2c2e` for Borders on inputs, buttons, and nav dividers - the thinnest readable outline on near-black
- Ash `#888888` for Muted body text, secondary labels, inactive borders - the only gray with enough chroma to carry information
- Smoke `#e9e9e9` for Helper text, subtle text accents on dark surfaces
- Bone `#f3f3f3` for Headings, high-emphasis text - slightly off-white to avoid harshness against pure black
- Paper `#ffffff` for Primary headings, logo text, pure-contrast display copy
- Platinum `#dddddd` for Nav text at rest - sits one step below pure white to create a de-emphasized nav hierarchy

Use these typography anchors:

- Neue Montreal `--font-neue-montreal` for Single-family type system. Weight 400 carries the entire display scale up to 104px - the deliberate refusal of a bold weight is the signature. Weight 500 activates only on small uppercase labels and button text. Negative letter-spacing tightens display sizes (-0.02em at 70-104px) while small uppercase eyebrow labels open to +0.035-0.040em. The 104px display at weight 400 is anti-conventional - most systems would set this at 700-800; here it whispers, letting the void around it carry the weight.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 20px.
- Element gap: 20px.

Build these component patterns where relevant:

- Primary CTA Button: Reserve flow entry point and any high-intent action
- Ghost Nav Link: Top-bar navigation at rest
- Display Headline: Hero and section titles
- Designer Profile Card: Portfolio tile in the designer grid
- Sprint Showcase Card: Large horizontal project preview card
- Outlined Input Field: Form fields, email capture
- Eyebrow Label: Small uppercase section markers and tag chips
- Subtext Paragraph: Supporting copy under headlines and in card bodies
- Project Thumbnail Tile: Edge-to-edge image previews in the featured-sprints row
- Inline Ghost Link: Text-level navigation and 'Sprint with me ' inline actions
- Top Navigation Bar: Global site header
- Section Header Block: Reusable section intro

Do:

- Use Sprint Violet (#6a48f2) only for the primary CTA fill, active link state, and focused input border - its scarcity is the design
- Set all display headlines at weight 400, never bold. The 70-104px scale carries authority through size, not stroke weight
- Apply -0.02em letter-spacing at 70px+ display sizes and +0.035-0.040em on small uppercase eyebrows - the contrast between tight display and open labels creates the type system's character
- Use 10px radius on designer cards and 50px pill radius on buttons - these two radii define the geometric language; avoid anything in between
- Layer surfaces at #000000 #171718 #2c2c2 - each step is one shade of difference, creating depth without illumination
- Keep subtext and supporting copy at 18-19px in Ash (#888888) so the display headline remains the loudest element on every screen
- Set page max-width to 1200px and center content - the void extends to the viewport edges but typography stays in a controlled measure

Avoid:

- Do not introduce a second chromatic accent - Sprint Violet is the only color, and adding another dilutes the system
- Do not use bold (weight 600+) on any headline - weight 400 at large sizes is the signature; bold would break the hushed tone
- Do not add box-shadows to cards or buttons - depth comes from the #000000 #171718 surface contrast, not elevation shadows
- Do not use light gray (#f3f3f3, #e9e9e9) as a page background - the entire system depends on pure void black as the canvas
- Do not use 8px or 12px border-radius on cards or buttons - the system only uses 6px (inputs/nav), 10px (cards), and 50px (buttons/links)
- Do not set body text below 15px - the type scale starts at 14px for captions only; 15-16px is the readable minimum
- Do not place white or violet text directly on a #6a48f2 background without testing contrast - use white-on-violet for the CTA text only, never decorative

Source prompt cues:

**Quick Color Reference**
- background: #000000
- text: #ffffff (display), #f3f3f3 (headings), #888888 (body/subtext)
- border: #2c2c2e (outlined controls), #171718 (card edges)
- accent/primary action: #6a48f2 (filled action)
- surface: #171718 (Obsidian - cards and elevated panels)

**3-5 Example Component Prompts**

1. *Hero Section*: Pure black (#000000) background. Display headline 'Your brand or website, delivered at lightspeed.' in Neue Montreal weight 400 at 72px, color #ffffff, letter-spacing -1.44px, line-height 1.1. Subtext paragraph below in #888888 at 19px weight 400, line-height 1.43, max-width 640px. 80px vertical padding above and below the text block.

2. *Primary CTA Button*: Pill shape, 50px border-radius, Sprint Violet (#6a48f2) background fill, no border. Text 'Reserve your sprint' in Neue Montreal 15px weight 500, color #ffffff, padding 10px 24px. No hover shadow - on hover, background brightens 10%.

3. *Designer Profile Card*: 10px border-radius, Obsidian (#171718) surface. 20px padding. Top: full-width portrait photo (no padding around it, image bleeds to card edges). Bottom: designer name in 16px weight 500 #ffffff, role label in 15px weight 400 #888888 directly below. No border, no shadow.

4. *Outlined Input Field*: 1px Graphite (#2c2c2e) border, 6px border-radius, transparent background. Placeholder text in #888888 at 15px weight 400. Vertical padding 20px, horizontal padding 16px. On focus: border color shifts to Sprint Violet (#6a48f2).

5. *Eyebrow Label*: Neue Montreal 14px weight 500, uppercase, letter-spacing +0.5px, color #888888. Used above section headlines or as metadata tags. No background, no border.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
