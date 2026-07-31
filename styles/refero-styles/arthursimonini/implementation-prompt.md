# AI Implementation Prompt

Build a Arthursimonini-inspired interface using this source-derived style bundle.

Reference site: https://arthursimonini.com
Theme: dark
Category: Media
North star: printed film programme in black ink

Use these palette anchors:

- Obsidian `#000000` for Page canvas, nav background, poster grid ground
- Bone `#ffffff` for All text, hairline section borders, image borders, icon strokes

Use these typography anchors:

- RomieLigatures-Regular `--font-romieligatures-regular` for Display headlines, section titles, marquee text. The signature choice: this didone carries discretionary ligatures (dlig) that fuse letters into ornamental shapes - the oversized wordmarks and repeated marquee bands rely on these ligatures for their distinctive character. Line-height collapses to 0.73 at the 167px size so stacked display lines almost touch, creating a dense editorial block. Reserved exclusively for type-as-art moments; never used for body copy or UI labels.
- LifeLTStd-Roman `--font-lifeltstd-roman` for Navigation links, metadata, body copy, timestamps, section category labels. A single weight at a single size - the system does not modulate emphasis through weight. Tracking is normal. This is the functional typeface that scaffolds the UI while the display face performs. Its quietness is the point: LifeLTStd is a transitional serif that reads cleanly at 18px without competing with the display type.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: .
- Section gap: 40px.
- Card padding: 15px.
- Element gap: 15px.

Build these component patterns where relevant:

- Scrolling Marquee Navigation: Primary navigation
- Site Wordmark: Brand identity header
- Hairline Section Divider: Structural separator
- Playlist Track Row: Music list item
- Film Poster Grid: Image gallery
- Section Category Label: Eyebrow / kicker text
- Timestamp / Duration: Metadata indicator
- Poster Thumbnail: Content card

Do:

- Use only #000000 and #ffffff - every surface, every border, every character is one of these two values.
- Reserve RomieLigatures for display moments only: site wordmark, section titles, marquee bands, and track names at 65px+. Never use it for UI labels or metadata.
- Use LifeLTStd 18px as the single body/nav/label size across the entire site - do not introduce a type scale beyond the four documented roles.
- Separate every content block with a 1px solid white hairline that spans 100% viewport width with no padding gap.
- Set display type at 167px with line-height 0.73 so stacked lines nearly touch - this density is the editorial signature.
- Enable discretionary ligatures ("dlig" on) on all RomieLigatures usage - the fused letterforms are the brand's most recognizable visual element.
- Use 15px padding for all internal spacing within bands and 40px between major content sections.

Avoid:

- Never introduce color - not for hover states, not for active nav, not for error messages, not for decorative accents.
- Never use border-radius - all corners are square (0px). This includes buttons, images, and tags.
- Never apply box-shadow or drop-shadow - elevation is expressed through white hairlines and negative space, not depth.
- Never use bold or semibold weights - both typefaces operate at 400 only. Emphasis comes from size contrast, not weight.
- Never use RomieLigatures for body copy, labels, timestamps, or anything below 65px - the decorative ligatures become illegible at small sizes.
- Never add background fills, gradients, or colored overlays to poster images - keep them raw grayscale with only a white border.
- Never center-align body text or metadata - left-align for content, right-align only for timestamps and durations.

Source prompt cues:

**Quick Color Reference:**
- background: #000000
- text: #ffffff
- border: #ffffff (1px hairline)
- accent: #ffffff (no chromatic accent exists)
- primary action: no distinct CTA color

**Example Component Prompts:**

1. Create a full-bleed site header: black (#000000) background, 0px padding. The wordmark "ARTHUR SIMONINI" set in RomieLigatures at 167px, weight 400, white (#ffffff), line-height 0.73, left-aligned, with discretionary ligatures enabled ("dlig" on, "kern" on). Below the wordmark, a 1px solid white hairline divider spans 100% viewport width.

2. Create a scrolling marquee navigation band: black background, 15px padding top and bottom. Repeated text "B.O. HABILAGES DISQUES PUBS ONERTS INFOS" in RomieLigatures at 18px, white, with the category prefixes (B.O., HABILLAGES, DISQUES) in LifeLTStd 18px preceding each section name. The marquee fills 100% width and scrolls horizontally. No buttons, no borders, no hover states.

3. Create a playlist track row: black background, 40px vertical gap between rows. Track title in RomieLigatures 65px white left-aligned, with a parenthetical subtitle like (BOMBING WAR OST) in LifeLTStd 18px on the same line. Duration timestamp in LifeLTStd 18px right-aligned. No background fill, no row border - rows are separated by spacing alone.

4. Create a film poster grid: 6 equal columns, 0px gap, black page background. Each cell contains a grayscale poster image filling 100% of the cell, wrapped in a 1px solid white border. No captions, no titles, no padding inside the frame. The white borders between adjacent images merge into a continuous grid lattice.

5. Create a section category eyebrow: LifeLTStd 18px, white, uppercase, left-aligned, positioned 15px above a section title. Content is a taxonomy prefix like "B.O." or "HABILLAGES" with intentional periods acting as visual rhythm devices. No bold, no color, no border.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
