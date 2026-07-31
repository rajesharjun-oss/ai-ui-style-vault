# AI Implementation Prompt

Build a Mother Design-inspired interface using this source-derived style bundle.

Reference site: https://www.motherdesign.com
Theme: light
Category: Agency
North star: broadsheet manifesto in black ink

Use these palette anchors:

- Newsprint `#f4f4f4` for Soft section background, alternate surface, and quiet card fill.
- Bone White `#ffffff` for Navigation background, card surfaces, button fills, inverted text - pushes forward off the gray canvas
- Press Black `#000000` for Neutral form states, badge text, and quiet UI feedback where color should stay understated.
- Foil Gray `#808080` for Secondary text, subdued link borders, metadata - sits behind Press Black as quiet annotation
- Ink Green `#306f09` for Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content

Use these typography anchors:

- Basis `--font-basis` for Primary typeface across all UI. Weight 400 for body, links, and most running text; weight 600 used sparingly for the small uppercase-ish labels and the navigation tabs. The 226px size at 1.0 line-height is the signature - display type behaves like a poster headline, not a web heading. Negative tracking tightens as size grows: -0.04em at display, -0.02em at mid, -0.01em at body.
- Basis Mono `--font-basis-mono` for Used for technical labels, metadata, timestamps, and small annotations. The +0.06em letter-spacing gives it the feel of a printed caption set in a typewriter face - a deliberate counterpoint to Basis's tight grotesque.
- Times `--font-times` for System serif used as a rare editorial accent - appears in icon and small body contexts where a note of 'newspaper' or 'footnotes' is wanted. Its presence is felt more than seen; the choice signals print lineage rather than decoration.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: 160-200px.
- Card padding: 0px.
- Element gap: 20px.

Build these component patterns where relevant:

- Navigation Tab: Top-level page links (Work, Information, News, Contact)
- Brand Mark Cell: Logo container at the far left of the nav row
- News Marquee Bar: Headline/news ticker running across the top right
- Theme Toggle Cluster: Icon-only controls in the top-right corner
- Portfolio Thumbnail: Project preview tiles in the work grid
- Project Caption Block: Title + role text below the work grid
- Manifesto Block: Large editorial paragraph introducing the studio's voice
- Section Display Header: Monumental section titles (Rigor, Rebellion, Depth, Care)
- Grid Section Frame: Container for 2-up section displays and content
- Service List Item: Vertical list of capabilities (Brand Strategy, Naming, etc.)
- Inline Link: Hyperlinks within manifesto and body copy
- Section Label: Small all-caps-style label above content blocks (e.g. 'How we do it', 'What we do')

Do:

- Set display type at 226px with -0.04em letter-spacing and line-height 1.0 - the extreme scale is the signature, not an exception.
- Use only the five colors: #f4f4f4 canvas, #ffffff surface, #000000 text and rules, #808080 secondary, #306f09 as the only chromatic note.
- Structure all layout with 1px Press Black rules - vertical, horizontal, and as borders on interactive cells. Never use shadows or fills to separate regions.
- Use Basis Mono with +0.06em tracking for metadata, labels, and the news ticker. Reserve Basis for everything else; bring in Times only for the occasional editorial annotation.
- Keep card and thumbnail padding at 0px. Let raw images sit edge-to-edge in their grid cells with no chrome, border, or radius.
- Anchor the nav with a 1px-bordered segmented control: brand mark cell + tab group on the left, theme toggle cluster on the right. Bone White fill, no radius.
- Treat whitespace as a structural element - large vertical gaps (160-200px) between the portfolio grid and the next section are part of the system, not negative space to be filled.

Avoid:

- Do not introduce additional colors. Any new hue, even a desaturated one, will dilute the broadsheet identity. The green is a printer's mark, not a palette swatch.
- Do not add box-shadows, blurs, or any form of elevation. The system has no z-axis - depth is typographic.
- Do not round corners. Every border, button, and cell stays at 0px radius. Curvature would betray the printed-page metaphor.
- Do not cap display type at conventional web sizes (48-72px). The 226px / 110px scale is the point - shrinking it to 'feel more modern' removes the signature.
- Do not use weight 700 or 800. Basis 600 is the heaviest weight in the system; 400 does the work at display sizes because the size itself provides weight.
- Do not add icons inside buttons or cards. Icons live only in the theme toggle cluster and the brand mark cell.
- Do not center body copy or set paragraphs to a narrow max-width. The manifesto reads full-bleed; column width is controlled by the grid, not by a content container.

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #f4f4f4
- surface: #ffffff
- border: #000000 (1px)
- secondary text: #808080
- accent: #306f09
- primary action: no distinct CTA color

**Example Component Prompts**
1. *Section display header*: Render 'Rigor' at 226px Basis weight 400, color #000000, letter-spacing -0.04em, line-height 1.0, centered in a grid cell framed by 1px #000000 rules on all sides with ~120px internal padding.
2. *Navigation tab*: Basis 14px weight 600, text 'Work', color #000000, background #ffffff, 1px #000000 border, 16px horizontal padding, 2px vertical padding, 0px radius. Place in a row of similar tabs edge-to-edge.
3. *Service list item*: Basis 60px weight 400, text 'Brand Strategy', color #000000, letter-spacing -0.02em, line-height 1.0, left-aligned, stacked vertically with 8px row gap, no bullet, no border.
4. *Portfolio thumbnail*: Full-bleed image filling a 5-column grid cell, 0px border, 0px radius, 0px padding, no caption inside the cell.
5. *Section label*: Basis Mono 14px weight 400, text 'What we do', color #000000, letter-spacing 0.06em, line-height 1.2, positioned at the top-left of a content area.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
