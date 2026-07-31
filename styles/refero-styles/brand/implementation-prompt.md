# AI Implementation Prompt

Build a Brand-inspired interface using this source-derived style bundle.

Reference site: https://brand.dropbox.com
Theme: light
Category: Design
North star: Chromatic graph paper atlas - a living brand specimen where every color block, headline, and border snaps to an invisible modular grid printed on white.

Use these palette anchors:

- Dropbox Blue `#0061fe` for Primary text, link borders, icon strokes, heading type, outlined action borders - the single most defining chromatic element, used wherever the brand needs to speak
- Dropbox Light `#5f9dff` for Soft surface washes, decorative icon accents, and secondary blue fields - a desaturated companion to Dropbox Blue for large background panels
- Sun Yellow `#fad24b` for Brand palette swatch, large color block panels, decorative fills
- Tangerine `#ff8c19` for Brand palette swatch, full-bleed color block panels, accent fills
- Sky Cyan `#3dd3ee` for Brand palette swatch, full-bleed color block panels, illustration accent
- Lime `#b4dc19` for Brand palette swatch, large color block panels, accent fills
- Coral `#ffafa5` for Brand palette swatch, warm color block panels, accent surfaces
- Lavender `#c8aff0` for Brand palette swatch, soft color block panels, illustration accent
- Magenta `#892055` for Brand palette swatch, deep accent panels, editorial accent
- Slate Navy `#283750` for Brand palette swatch, dark accent panels, editorial contrast
- Ink `#1e1919` for Primary body text, hairline borders, structural dividers, nav type - the near-black workhorse of the grid system
- Paper `#ffffff` for Page canvas, card surfaces, reverse text on color blocks, background beneath the visible grid
- Graphite `#736c64` for Muted secondary text, subtle helper labels, low-emphasis borders

Use these typography anchors:

- Dbsharpgroteskvariable Vf `--font-dbsharpgroteskvariable-vf` for Display and heading type - tight-tracked, geometric grotesque at heavy weights. The 0.80 line-height at 34px is a compression device for editorial taglines where lines almost touch, creating a block-of-text effect. Free substitute: Inter at 700, or Space Grotesk Bold.
- Atlasgrotesk Web `--font-atlasgrotesk-web` for Body copy, navigation labels, link text, button labels, and all utility type. Neutral grotesque at compact sizes - 14px at line-height 1.67 gives breathing room for readable paragraphs while 12px at 1.43 keeps metadata tight. Free substitute: Inter or Atlas Grotesk via Adobe Fonts.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: 64px.
- Card padding: 22-24px.
- Element gap: 16px.

Build these component patterns where relevant:

- Grid Canvas: Structural background
- Color Block Panel: Large chromatic content surface
- Editorial Headline Block: Primary heading display
- Inverted Text Panel: White text on color
- Hairline Divider: Structural separator
- Text Link: Inline navigation
- Outlined Action: Primary call-to-action border
- Nav Label: Navigation text
- Brand Mark: Logo/identity anchor
- Chevron Scroll Indicator: Scroll affordance
- Color Swatch Cell: Brand palette documentation

Do:

- Use #0061fe for all primary headlines, link text, and outlined action borders - it is the voice of the brand
- Apply -0.02em letter-spacing to all display type at 30px and above; the tight tracking is what makes the headings feel custom and editorial
- Snap every element to the visible grid - color blocks, text, and whitespace all respect the modular lattice
- Use 8px border-radius universally for all cards, buttons, and color panels - the only radius in the system
- Use 1px hairline borders in Ink (#1e1919) for all structural dividers and grid cell edges
- Deploy large flat color blocks (full grid cells filled with Sun Yellow, Tangerine, Sky Cyan, etc.) as section furniture - color is both content and layout
- Set body text at 14px with line-height 1.67 for comfortable paragraph density

Avoid:

- Never add drop shadows or box-shadow effects - the grid and flat color provide all visual structure
- Never use border-radius values other than 8px - the system is geometric, not pill-shaped or fully rounded
- Never use filled solid-color CTA buttons - all actions are outlined with a #0061fe border
- Never center body or heading text - all type is left-aligned within its grid cell
- Never use more than 4 brand palette colors on a single section - over-saturation breaks the editorial discipline
- Never add gradients - the palette is entirely flat, saturated, and singular
- Never use colors outside the defined 13-color palette (2 blues, 8 brand swatches, 3 neutrals) for UI elements

Source prompt cues:

**Quick Color Reference:**
- Text: #1e1919 (Ink) for body, #0061fe (Dropbox Blue) for headings and links
- Background: #ffffff (Paper) for canvas, #5f9dff (Dropbox Light) for soft blue surfaces
- Border: #1e1919 (Ink) for hairlines, #0061fe (Dropbox Blue) for outlined actions
- Accent palette: #fad24b Sun Yellow, #ff8c19 Tangerine, #3dd3ee Sky Cyan, #b4dc19 Lime, #ffafa5 Coral, #c8aff0 Lavender, #892055 Magenta, #283750 Slate Navy
- primary action: #0061fe (outlined action border)

**3-5 Example Component Prompts:**

1. **Editorial Headline Block:** Create a left-aligned heading inside a white grid cell. Type at 36px in Dbsharpgroteskvariable Vf weight 700, color #0061fe, letter-spacing -0.72px, line-height 1.20. No background, no border, no decoration - the grid lines frame the type.

2. **Outlined Action Button:** Build a ghost button with transparent background, 1px solid border in #0061fe, text in #0061fe at 14px Atlasgrotesk Web weight 500. 8px border-radius. 12px vertical padding, 16px horizontal padding.

3. **Color Block Panel with Inverted Text:** Create a full grid cell filled with #ff8c19 (Tangerine). 8px border-radius. Inside, set white (#ffffff) body text at 14px Atlasgrotesk Web weight 400, line-height 1.67, left-aligned with 22-24px padding from cell edges.

4. **Brand Swatch Cell:** A rectangular element filled with one of the eight accent colors (e.g., #fad24b Sun Yellow). 8px border-radius. No text, no border, no shadow. Functions as a flat color sample within the grid composition.

5. **Grid Canvas Section:** A full-width section with #ffffff background. Overlay a visible grid of 1px lines in #1e1919 at low opacity (use rgba(30,25,25,0.08)). All content elements - text, color blocks, buttons - snap to this grid. No container boxes; the grid itself defines placement.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
