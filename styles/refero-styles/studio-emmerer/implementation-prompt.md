# AI Implementation Prompt

Build a Studio Emmerer-inspired interface using this source-derived style bundle.

Reference site: https://emmerer.com
Theme: light
Category: Agency
North star: Typeset on drafting paper

Use these palette anchors:

- Pure Black `#000000` for Body text, inline links, project titles, table row dividers, the arrow ( ) glyph
- Drafting White `#ffffff` for Page background, surface under all content - no tint, no gradient
- Index Gray `#999999` for Table column headers (PROJECT, TYPE, LOCATION, YEAR), supporting metadata, secondary borders

Use these typography anchors:

- NHaasGrotesk `--font-nhaasgrotesk` for Sole typeface for every UI element - headlines, body, links, table cells, column headers, navigation. Single weight 400 across the entire system, with negative letter-spacing tightening at every size. The Neue Haas Grotesk DNA (geometric neutrality, grotesque proportions) is what carries the architectural-document feel; substitute Helvetica Neue or Inter as a free fallback.

Use these layout rules:

- Base spacing: 6px.
- Density: comfortable.
- Page max-width: .
- Section gap: 32px.
- Card padding: .
- Element gap: 5px.

Build these component patterns where relevant:

- Project Table Row: The primary repeating element on the page - each project is one row in a four-column table.
- Table Column Header: Labels the four columns above the project list.
- Inline Navigation Link: Site-level navigation - about, contact, imprint, read more.
- Arrow Glyph ( ): The only icon in the entire system. Marks navigability.
- Hero Photograph: Large editorial image occupying the right half of the viewport on first load.
- Intro Paragraph: Landing text describing the practice, anchored in the upper-left column.
- News/Featured Project Caption: Metadata strip directly under the hero image.

Do:

- Use NHaasGrotesk weight 400 for every piece of text on the page - no exceptions, no weight variations.
- Set display text to 30px with line-height 0.90 and letter-spacing -0.33px; set body to 16px / 1.16 / -0.13px.
- Use 1px solid #000000 as the only border - for table row dividers, link underlines, and any structural separator.
- Prefix every interactive link with the arrow glyph in the same size and color as the link text.
- Use #999999 for table column headers and supporting metadata only; keep all primary text and links at #000000.
- Let whitespace define hierarchy - use 12px row padding and 32px section gaps rather than cards or fills.
- Keep photography edge-to-edge with no border-radius, no overlay, and no caption box.

Avoid:

- Never introduce a chromatic color - the palette is strictly black, white, and #999999.
- Never use font-weight above 400 - bold or semibold would shatter the single-weight voice of the system.
- Never add box-shadow, drop-shadow, or any z-axis elevation.
- Never apply border-radius - all corners stay at 0px.
- Never wrap content in filled cards, panels, or containers - rows sit directly on the page surface.
- Never introduce an icon set beyond the arrow; no SVGs, no pictograms, no button shapes.
- Never change link color on hover - links stay #000000 with the same underline weight to preserve the printed-page feel.

Source prompt cues:

QUICK COLOR REFERENCE
- text: #000000
- background: #ffffff
- border / divider: #000000
- secondary text (column headers, metadata): #999999
- primary action: no distinct CTA color

EXAMPLE COMPONENT PROMPTS
1. Project table row - White background, 1px solid #000000 bottom border, 12px padding-bottom, 4px padding-left. Project name in 16px NHaasGrotesk weight 400 #000000, left-aligned. Type, Location, Year columns in the same 16px #000000, right-aligned. No fill, no hover state, no border-radius.

2. Inline navigation link - Render the text ' about' where is U+2192 in 16px NHaasGrotesk weight 400 #000000 with a 1px #000000 underline spanning the full text including the arrow. 30px margin-right between adjacent links. No color change on hover.

3. Intro paragraph - 30px NHaasGrotesk weight 400 #000000, line-height 0.90, letter-spacing -0.33px. Wraps at ~45% viewport width. No sub-headline above it, no button beneath - the paragraph itself is the headline.

4. Table column header - 15px NHaasGrotesk weight 400 #999999, uppercase, 12px padding-bottom, 1px solid #000000 bottom border separating header band from data rows. No background fill, no bold weight.

5. Hero photograph - Full-bleed within the right 55% of the viewport, no border, no border-radius, no padding, no overlay text. Architectural documentary photograph at high contrast. An adjacent caption strip below shows 'News 2/19' in 15px #999999 on the left, arrows in 16px #000000 centered, and the project title with ' Open Project' inline link in 16px #000000 on the right.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
