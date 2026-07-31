# AI Implementation Prompt

Build a Not Real-inspired interface using this source-derived style bundle.

Reference site: https://notreal.tv
Theme: light
Category: Agency
North star: Editorial gallery spread on greyscale vellum - a high-end catalog where only the artwork is allowed to scream with color.

Use these palette anchors:

- Ink Charcoal `#292a2c` for Primary text, dominant border strokes (635 occurrences as borderColor), nav accents
- Vellum `#f2f2f2` for Page canvas, card surfaces - warm-leaning off-white that gives the page a paper-stock feel rather than digital white
- Full Black `#000000` for Link border underlines, footer text, icon strokes, image overlay text - used as a chromatic anchor only where maximum contrast against Vellum is required

Use these typography anchors:

- ogg `--font-ogg` for Display and project headlines. This is a high-contrast didone-flavored serif used at 55px with aggressive -0.036em tracking - it acts as the gallery label, announcing each case study with typographic weight that the sans-serif never attempts. At smaller sizes (24-26px) the same family handles editorial pull-quotes and the wordmark, where the negative tracking tightens less aggressively (-0.02em). The signature choice: a single weight (400) doing all serif work, relying on the contrast within letterforms rather than weight variation to create hierarchy.
- telegraf `--font-telegraf` for Body copy, navigation, metadata tags, project category labels, and secondary headings. A geometric sans that does all the quiet documentation work. At 55px it can also serve as display type, creating a rare moment where both fonts meet at the same size - typically the serif announces the project name while the sans describes it below. Tracking is positive throughout (0.002em to 0.040em), widening as size decreases - a deliberate inverse relationship that keeps small caps-styled metadata readable and gives the wordmark breathing room.

Use these layout rules:

- Base spacing: 6px.
- Density: compact.
- Page max-width: 1440px.
- Section gap: 120px.
- Card padding: 0px.
- Element gap: 18px.

Build these component patterns where relevant:

- Wordmark / Site Logo: Persistent brand identifier in top-left of every page
- Top Navigation Bar: Primary site navigation, sits flush at the top of every page
- Project Tile (Large Featured): Full-bleed campaign artwork for top case studies in the work grid
- Project Tile (Compact): Smaller secondary case study presentations in the asymmetric grid
- Inline Text Link: Text links within body copy and navigation
- Vertical Running Text: Rotated metadata strip pinned to the right edge of the viewport
- Category Metadata Tag: Small text label indicating project discipline (cgi, art direction, campaign, etc.)
- Project Title with Em-Dash Separator: The signature heading treatment for every case study
- Agency Statement Block: Introductory description text near the top of the Work page
- Asymmetric Image Grid Cell: Individual positioned image within the editorial layout

Do:

- Use only three colors: #292a2c for text, #f2f2f2 for canvas, #000000 for maximum-contrast links and dark surfaces
- Apply ogg for all display text and project titles at 55px with letter-spacing -1.98px; use telegraf at 18-20px for body with 0.38-0.5px tracking
- Render all images as sharp-edged rectangles with 0px border-radius and no drop shadow
- Separate project titles from subtitles with an em-dash (-) in ogg, with the subtitle in italic ogg
- Use ' / ' delimiters between category metadata tags in telegraf 15px
- Position the vertical running text strip absolutely along the right viewport edge on pages that present project work
- Let the canvas breathe: 120px between major sections, no card containers, no elevated panels

Avoid:

- Do not introduce any chromatic color into the UI - saturated color belongs exclusively to client artwork
- Do not apply border-radius to any element, including buttons, cards, tags, or images
- Do not add box-shadow, drop-shadow, or any CSS elevation - the design is intentionally flat
- Do not use centered layouts or constrained max-width wrappers - let content flow to viewport edges
- Do not use bold (600+) or semibold weights - both fonts operate at 400 only
- Do not create a distinct filled CTA button - links are text with 1px black borders, nothing more prominent
- Do not alternate background colors between sections - the entire page shares the single Vellum canvas

Source prompt cues:

**Quick Color Reference**
- text: #292a2c
- background: #f2f2f2
- border: #292a2c
- accent: #000000
- primary action: no distinct CTA color

**Example Component Prompts**

1. *Project tile heading block:* On Vellum (#f2f2f2) canvas. Project title in ogg 26px, weight 400, color #292a2c, letter-spacing -0.52px. Em-dash separator. Subtitle in ogg italic 26px, same color and tracking. Below: category tags in telegraf 15px, #292a2c, separated by ' / '. No background, no border, no padding.

2. *Featured work image:* Full-width image at native aspect ratio on #f2f2f2 canvas. 0px border-radius. No border, no shadow. No overlay text on the image - all text sits below in the heading block.

3. *Navigation bar:* telegraf 18px, weight 400, #292a2c. Four links spaced with wide horizontal distribution, flush right. No background fill, no border, no sticky behavior. Top padding 24px, bottom padding 24px.

4. *Inline link:* telegraf at body size, color #292a2c, with 1px solid #000000 bottom border as underline. No background hover state - border thickens on interaction.

5. *Agency statement paragraph:* telegraf 20px, weight 400, #292a2c, line-height 1.33. The self-identifying phrase 'design-driven' set in ogg serif at the same size. No background panel, no border, no container.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
