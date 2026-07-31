# AI Implementation Prompt

Build a Specht Studio-inspired interface using this source-derived style bundle.

Reference site: https://stephaniespecht.com
Theme: light
Category: Design
North star: Gallery wall of restrained curiosity. The studio's own chrome is a white plane and black type; the visual fireworks live entirely inside the project tiles.

Use these palette anchors:

- Gallery White `#ffffff` for Page canvas, project tile background where artwork doesn't fill the frame
- Fog Gray `#b0b0b0` for Secondary surface, subtle dividers, muted metadata text
- Graphite `#666666` for Link borders, secondary text, caption metadata, inactive nav
- Gallery Black `#000000` for Primary text, active nav, all structural borders, the single ink that holds the system together

Use these typography anchors:

- Helvetica Neue `--font-helvetica-neue` for Sole typeface across every context - nav, body, headings, links, footer. The deliberate choice of a single weight at 400 across all roles removes typographic hierarchy and forces the grid and the imagery to do the ranking. No display cuts, no bold emphasis, no italics - restraint as a point of view.

Use these layout rules:

- Base spacing: 6px.
- Density: comfortable.
- Page max-width: 1400px.
- Section gap: 67-122px.
- Card padding: 0px.
- Element gap: 2-10px.

Build these component patterns where relevant:

- Navigation Bar: Site-wide top navigation
- Project Tile: Portfolio thumbnail in the grid
- Grid Container: Holds the portfolio tiles in masonry arrangement
- Text Link: Inline and standalone links in body copy
- Section Header: Optional heading text for sections like 'Artwork', 'Young Innovators'
- Brand Lockup: Studio identity in the top-left corner
- Footer: Site footer with secondary links and metadata

Do:

- Use only Helvetica Neue at weight 400 - no bold, no light, no italic beyond the brand subtitle. Typographic uniformity is the system.
- Set body text at 15-16px and headings at 25px max. Anything larger than 25px breaks the gallery-wall scale where the imagery dominates.
- Build with the white canvas as the default surface. Gallery Black (#000000) is the only structural ink; Graphite (#666666) handles secondary text and link borders.
- Let project tiles butt directly against each other with 2-10px gaps. The tight masonry grid is the primary organizational device - wide gutters would dissolve the visual density.
- Treat every page as a catalog. Text should annotate and index the work; it should never compete with the imagery for attention.
- Keep all borders hairline (1-2px) in Gallery Black. Borders replace shadows, fills, and rounding as the structural language.
- When a page needs section labels, use 25px black type directly on the white plane - never a colored chip, pill, or badge.

Avoid:

- Do not introduce a brand color. Any chromatic accent would shift the system from 'gallery wall' to 'product page' and destroy the curatorial neutrality.
- Do not add rounded corners to tiles, buttons, or containers. The system is orthogonal - sharp 0px radii everywhere.
- Do not use shadows, blurs, or elevation. Depth must come from image content and grid density, not from CSS box-shadow.
- Do not use multiple typefaces or weights. A second weight or family immediately introduces hierarchy that the system deliberately suppresses.
- Do not add a CTA button. There is no primary action in this system - if a page needs a link, use a Graphite-underlined text link.
- Do not center the content on the page. The grid is left-aligned, slightly off-center, which creates the editorial-publication feel.
- Do not use gradients, fills, or tinted backgrounds. Every surface is pure white or pure black, never a shade between.

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #ffffff
- border: #000000
- accent: #666666
- primary action: no distinct CTA color

**3-5 Example Component Prompts**
1. Build a portfolio grid: white #ffffff background, 3-column masonry layout at 1400px max-width, tiles are edge-to-edge images with 0px border-radius and 8px gap between cells. No shadows, no borders on tiles.
2. Build a top nav bar: white background, 1px solid #000000 bottom border, 24px padding. Left: 'Specht Studio' in 16px Helvetica Neue weight 400 #000000 with 'structure, intuition, experiment' in #666666 directly below. Right: nav links 'Work', 'Art / Research', 'Archive', 'About', 'Shop' at 15px weight 400 #000000, 30px margin-right between items, active item gets a 2px solid #000000 underline.
3. Build a text link: 15px Helvetica Neue weight 400, color #666666, 1px solid #666666 underline. No hover state change.
4. Build a section header: 'Artwork' in 25px Helvetica Neue weight 400 #000000, line-height 1.2, 24px margin-bottom. Sits directly on the white canvas with no background or border.
5. Build a project tile: a single image filling the entire tile area, 0px padding, 0px border-radius, no overlay text, no border, no shadow. The tile is raw content.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
