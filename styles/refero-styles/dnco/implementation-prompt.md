# AI Implementation Prompt

Build a DNCO-inspired interface using this source-derived style bundle.

Reference site: https://dnco.com
Theme: light
Category: Agency
North star: editorial gallery on white linen.

Use these palette anchors:

- Canvas White `#ffffff` for Page background, primary surface for content blocks, card bases
- Hairline Mist `#e5e7eb` for Hairline borders, dividers, subtle surface wash, filter chip backgrounds, image placeholder fill
- Obsidian `#000000` for Primary text, brand wordmark fill, dark hero background, link text, heading color
- Ash `#a3a3a3` for Muted secondary text, captions, inactive filter labels, helper text

Use these typography anchors:

- Neue Haas Unica Pro `--font-neue-haas-unica-pro` for Sole typeface for all UI - navigation, body, headlines, and brand wordmark. Weight 400 only, no bold or light variants; hierarchy is built purely through size and tracking rather than weight contrast.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1400px.
- Section gap: 64px.
- Card padding: 0px.
- Element gap: 24px.

Build these component patterns where relevant:

- Brand Wordmark Hero: Signature full-bleed opener
- Pill Navigation Bar: Top-level site navigation
- Editorial Headline: Page-level statement copy
- Filter Chip Row: Project categorization controls
- Hairline Divider: Visual section separation
- Project Image Tile: Case study thumbnail in grid
- Filter Label Active Indicator: Active state for filter chips
- Text Link Inline: In-content navigation / project titles
- Case Study Card (Grid Unit): Project entry on Work index
- Footer Text Block: Site-level links and contact

Do:

- Use Neue Haas Unica Pro (or Inter / Neue Haas Grotesk) at weight 400 exclusively - never introduce bold, medium, or light weights
- Set all type with letter-spacing -0.025em; tight tracking is non-negotiable for the editorial feel
- Use only #ffffff, #e5e7eb, #000000, and #a3a3a3 - no chromatic accents anywhere in the UI
- Build hierarchy through size jumps (16 18 22 72), not through weight or color shifts
- Separate sections with 1px #e5e7eb hairlines or generous whitespace, never with fills or shadows
- Make every interactive element a pill (9999px) or a text-only label - no filled buttons, no rounded cards, no bordered inputs
- Let photography carry all color; images bleed into the layout without frames, radii, or overlays

Avoid:

- Do not add a second typeface family - the system is monotypographic by design
- Do not introduce any color other than the four neutrals - no brand red, blue, or accent green
- Do not use box-shadows or elevation on any component - depth comes from whitespace, not blur
- Do not add border-radius to cards or images - only navigation and chips use 9999px
- Do not bold or italicize text to create emphasis - increase size instead
- Do not place content inside bordered containers or filled panels - use whitespace to group
- Do not use background colors for buttons, tags, or interactive states - use text color and the dot indicator

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #ffffff
- border / divider: #e5e7eb
- muted text: #a3a3a3
- dark surface (hero inversion): #000000
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

1. *Brand wordmark hero*: Full-bleed black (#000000) section, edge-to-edge. The text 'DNCO' set in Neue Haas Unica Pro (or Inter) at 72px+, weight 400, color #ffffff, letter-spacing -0.025em, flush-left with no padding offset. No other elements on the screen.

2. *Editorial page headline*: 72px Neue Haas Unica Pro, weight 400, line-height 1.0, tracking -0.025em, color #000000, flush-left at the page edge over a #ffffff background. No max-width constraint.

3. *Pill navigation bar*: Horizontal row of text links at 16px weight 400, color #000000, gap 24px, over a #ffffff background. Active item is marked by a 4px black filled circle positioned 4px below the label - no background fill, no border, no weight change. Top-left wordmark 'DNCO' at 16px weight 400.

4. *Filter label group*: Vertical stack of four text labels (All, Sector, Location, Expertise) at 16px weight 400. Inactive items in #a3a3a3, active item in #000000 with a 4px black dot 4px below the label. No chip background, no border.

5. *Project image grid*: Two or three equal columns of uncropped landscape photography, no borders, no radius, no captions overlaid. Tiles separated only by container padding (24px gap). Missing images render as a solid #e5e7eb fill block at the same aspect ratio.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
