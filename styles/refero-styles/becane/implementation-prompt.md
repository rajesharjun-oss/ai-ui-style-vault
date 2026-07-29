# AI Implementation Prompt

Build a Becane-inspired interface using this source-derived style bundle.

Reference site: https://www.becaneparis.com
Theme: light
Category: E-commerce
North star: Gallery wall on bone-white plaster

Use these palette anchors:

- Bone White `#f6f6f6` for Page canvas, large background blocks
- Divider Grey `#e6e6e6` for Hairline borders between nav rows, section dividers
- Off-Black `#0a0a0a` for Headlines, body text, nav labels, button strokes
- Pure White `#ffffff` for Card surfaces, nav bar backgrounds, elevated panels
- Muted Grey `#b2b2b2` for Tertiary helper text, inactive labels
- Signal Red `#ff0000` for Accent panel fills - rotating display block, category highlight surface

Use these typography anchors:

- Eurostile Becane `--font-eurostile-becane` for Custom Eurostile variant is the sole typeface across all scales. Used uppercase at 8px with 0.04em tracking for nav, buttons, labels, and micro-copy - the high tracking and small size force labels to read as gallery placards rather than UI. Bold 30px anchors the hero 'COLLECTION' wordmark. Substitutes: Eurostile, 'Helvetica Neue', Arial - the geometric warmth of Eurostile is the closest system match; fallback to Helvetica Neue retains the uppercase utility feel.

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1440px.
- Section gap: 100px.
- Card padding: 10px.
- Element gap: 8-10px.

Build these component patterns where relevant:

- Ghost Nav Button: Top-left brand cluster (ALL / STORIES / BECANE)
- Ghost Cart Button: Top-right cart trigger
- Hero Wordmark: Section title - 'COLLECTION'
- Meta Label Row: Section counter - 'COLLECTION 01 / 01'
- Product Count Strip: Footer summary - '14 PRODUCTS - DISCOVER'
- Hairline Divider: Vertical rhythm between nav clusters
- Red Accent Panel: Rotating chromatic display block (signal surface)
- Product Silhouette Tile: Editorial product row - 12 figures across viewport
- Footer Link Cluster: Bottom-right policy + contact links

Do:

- Use Eurostile Becane at 8px with 0.04em tracking as the universal label size for nav, buttons, counts, and footer links
- Keep all borders at 0.5px solid #e6e6e6 - never use box-shadow, never use 1px+ strokes
- Set border-radius to 0px on every interactive element; the only rounding token is the site's own --inner-border-radius for inner cutouts, not visible UI
- Reserve #ff0000 for a single accent surface per viewport; let the rest of the page stay achromatic
- Let product photography carry layout rhythm - space tiles evenly across the full viewport rather than constraining to a fixed grid column
- Set line-height to 1.0 for the 30px wordmark and 1.1-1.2 for 8px labels - tight tracking amplifies the gallery-placard feel
- Anchor a meta-strip (count + secondary affordance) to the bottom of the viewport on category pages

Avoid:

- Never add background fills, gradients, or hover-color shifts to buttons - buttons remain ghost
- Never introduce a chromatic CTA button; #ff0000 is a surface accent, not an action
- Never round corners on cards, images, or buttons - sharp 0px edges define the aesthetic
- Never use body copy below 12px or above 30px; the scale is intentionally narrow
- Never add elevation (box-shadow, drop-shadow) - the system is flat and depends on hairline borders for structure
- Never use color to indicate state on links; rely on position, weight, or the Muted Grey #b2b2b2 for de-emphasis
- Never constrain the product row to a centered max-width container - let images breathe edge-to-edge

Source prompt cues:

Quick Color Reference
- text: #0a0a0a
- background: #f6f6f6
- surface (elevated panel/nav): #ffffff
- border: #e6e6e6
- muted text: #b2b2b2
- accent surface: #ff0000
- primary action: no distinct CTA color

Example Component Prompts
1. Build a sticky top header: background #ffffff, 86px tall, 0px radius, 0.5px solid #e6e6e6 bottom border. Left cluster - brand 'BECANE' at 8px Eurostile Becane weight 700 uppercase, tracking 0.04em, color #0a0a0a. Right cluster - 'CART 00' at 8px weight 400 same styling. No button backgrounds, no padding beyond 10px vertical.
2. Build a hero wordmark block: left-aligned on #f6f6f6 canvas. Meta line 'COLLECTION 01 / 01' at 8px uppercase #0a0a0a tracking 0.04em. Below it, 'COLLECTION' at 30px Eurostile Becane weight 700 uppercase, line-height 1.0, tracking 0.04em, color #0a0a0a. No underlines, no accent bars.
3. Build a product row: full viewport width, #f6f6f6 background, 12 evenly-spaced product photographs at equal column width, 0px radius, no borders, no card containers. Row gap 0; rely on natural image whitespace.
4. Build a footer meta-strip: pinned bottom, background #f6f6f6. Left - '14 PRODUCTS' at 8px uppercase #0a0a0a tracking 0.04em. Right - 'DISCOVER' at 8px uppercase #b2b2b2 tracking 0.04em. No button chrome, no separator glyph.
5. Build a nav link group: horizontal row on #ffffff, separated by 0.5px solid #e6e6e6 hairlines. Links at 8px uppercase #0a0a0a tracking 0.04em, 10px horizontal padding, 0px radius, transparent backgrounds. Hover: color shift to #666 only - no background change.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
