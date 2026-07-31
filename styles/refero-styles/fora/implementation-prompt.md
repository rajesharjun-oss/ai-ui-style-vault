# AI Implementation Prompt

Build a FORA-inspired interface using this source-derived style bundle.

Reference site: https://fora-concept.com
Theme: light
Category: Agency
North star: Swiss editorial mosaic on white. A grid of monumental color tiles and airy geometric type, where each panel of terracotta or lilac functions as a full-bleed typographic stage.

Use these palette anchors:

- Obsidian `#000000` for All text, headings, icons, nav links, dividers, and borders. Unsoftened true black anchors every chromatic panel
- Paper `#ffffff` for Page canvas, default card surface, and the negative space that lets chromatic panels breathe. Never tinted
- Terracotta `#a9553c` for Full-bleed section panels and hero zones. Warm oxidized red-brown against pure black and white - evokes raw clay and printed editorial covers
- Lilac Veil `#ddbdea` for Full-bleed section panels, content cards, and soft surface tint. Muted chalky pink that cools the terracotta into a balanced two-color rhythm

Use these typography anchors:

- Theinhardt `--font-theinhardt` for Sole typeface across all UI: nav, body, headings, buttons, labels. Positive letter-spacing (0.01em 0.024em) that grows with size is the anti-trend signature - tracking opens up rather than tightens, producing a Swiss neo-grotesque with editorial breathing room. The 700 weight appears only for micro-emphasis (tag labels), keeping the system light and even.
- Theinhardt Medium `--font-theinhardt-medium` for Theinhardt Medium - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 6px.
- Density: spacious.
- Page max-width: .
- Section gap: .
- Card padding: 25px.
- Element gap: 20px.

Build these component patterns where relevant:

- Full-Bleed Color Panel: Section container that claims a grid cell
- Panel Link with Arrow: Inline text link inside a colored panel
- Pill Tag: Category label overlay
- Team Portrait Cell: Photo showcase in grid
- Newsfeed Card: Social content card
- Ghost Button: Secondary action inside colored panels
- Primary Text Button: The only true button - minimal
- Footer Navigation Bar: Site-wide bottom nav
- Grid Tile Divider: Structural separator between panels
- Display Headline: Hero and panel headlines
- Location Marker: Geographic descriptor in hero panel

Do:

- Use Terracotta (#a9553c) and Lilac Veil (#ddbdea) only as full-bleed panel fills - never as button backgrounds, never as text colors, never as borders.
- Let letter-spacing grow with size: 0.01em at 15px, 0.024em at 35px. Never set negative tracking on headlines.
- Keep all type at weight 400 except the rare 700 micro-label. Weight contrast is a resource - spend it sparingly.
- Build the page as a strict grid of edge-to-edge tiles. White canvas between tiles is the gutter - no margins, no shadows, no hairlines.
- Use 0px border-radius on all panels and cards. Reserve 5px for buttons and 9999px only for pill tags.
- Pad panel interiors with 25px on all sides. Headlines sit 25px from the panel edge - flush, never floating.
- Pair every colored panel with a single short text element (headline + optional inline arrow link). Never stack multiple components inside a panel.

Avoid:

- Don't soften black to near-black or add a tint - #000000 is absolute and the system depends on that contrast.
- Don't introduce a third chromatic color, a gradient, or a neutral mid-gray. The two-color discipline is the brand.
- Don't add shadows, glows, or elevation to cards. The grid is flat - surfaces sit on the page, not above it.
- Don't use negative letter-spacing on any size. The positive tracking is a signature, not a mistake to correct.
- Don't round card or panel corners beyond 0px. The sharp 90 edges are what make it feel like editorial print.
- Don't mix multiple typefaces or weight the headlines at 600-700. Theinhardt 400 everywhere, plus rare 700 for micro-tags.
- Don't create centered, max-width containers. The grid is full-bleed; content fills its tile completely.

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #ffffff
- border: #000000
- accent: #ddbdea (Lilac Veil)
- brand panel: #a9553c (Terracotta)
- primary action: no distinct CTA color

**3-5 Example Component Prompts**
1. Build a full-bleed terracotta panel: background #a9553c, padding 25px, no radius, no border, no shadow. Inside, place a 35px Theinhardt 400 headline in #000000 with letter-spacing 0.024em, followed 20px below by a 15px ghost text link reading 'Erfahren Sie mehr '.
2. Build a newsfeed card: background #ddbdea, padding 25px, 0px radius. Left-aligned 80x80px square thumbnail (no radius), 20px gap, then a 18px body line in #000000, letter-spacing 0.016em, followed by a 15px underlined text link 'Mehr lesen'.
3. Build a pill tag overlay: 9999px radius, white #ffffff background, 5px vertical padding, 10px horizontal padding, 15px Theinhardt 400 in #000000 with letter-spacing 0.024em. Position absolute top-left of a grid cell with 10px margin.
4. Build a footer nav bar: full-width #ffffff background, 0px radius, single row of inline links in 15px Theinhardt 400 #000000 separated by 40px gap. Items: About, Team, Work, Contact. No dividers, no background bar.
5. Build a display headline block: 35px Theinhardt 400 in #000000, line-height 1.17, letter-spacing 0.024em. Text wraps naturally to fill 2-3 lines. No background, no border, no decoration - pure typographic statement on the white canvas.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
