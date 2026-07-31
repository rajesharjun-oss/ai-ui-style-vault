# AI Implementation Prompt

Build a OFFFICE :-inspired interface using this source-derived style bundle.

Reference site: https://offficestud.io
Theme: dark
Category: Design
North star: noir gallery swallowed by monolithic type

Use these palette anchors:

- Onyx `#0e0e00` for Full-bleed page background, navigation surface, product staging void - the entire canvas is one continuous dark field
- Paper White `#fefefe` for Display headlines, body text, navigation labels, archive list entries, locale switcher - the sole ink color across all UI layers
- Faint White `#2a2a2a` for Supporting palette color for small decorative accents when the core palette needs contrast. Do not promote it to the primary CTA color

Use these typography anchors:

- ak `--font-ak` for Primary workhorse - nav, body, display headlines, archive list, labels, links. The extreme range from 12px to 216px in a single family, with weights 400 for quiet copy and 700 only for emphasis, defines the system's voice. Tight 0.80 line-height at 216px creates stacked text-blocks that read as architectural walls rather than sentences.
- gs `--font-gs` for Editorial serif accent - used exclusively in the project archive list for project titles. At 72px it provides a high-contrast counterpoint to ak's geometric sans; at 12px it renders archive metadata with classical warmth. The two-font system is deliberately minimal: one sans does everything, one serif appears only where editorial gravitas is needed.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: .
- Section gap: 96-128px.
- Card padding: 0px.
- Element gap: 8px.

Build these component patterns where relevant:

- Top Navigation Bar: Minimal two-anchor header - brand mark left, contact CTA right
- Display Headline Block: Hero-scale typographic wall that defines the first viewport
- Product Sculpture (3D Hero Object): Centered product showcase - the only non-text element on the canvas
- Description Caption: Small editorial body text adjacent to the product showcase
- Locale Switcher: Three-letter language selector
- Archive Project Entry: Single row in the project archive list
- Archive List (Full): Vertically stacked project archive - the index page in list form
- Section Label (Inline): Minimal in-content metadata markers

Do:

- Use ak weight 400 for all body and display text; reserve ak weight 700 only for the 'GET IN TOUCH' nav CTA and emphasis that must break through at small sizes
- Let display headlines overflow viewport edges - 216px ak at 0.80 line-height is meant to be cropped by the frame
- Use Onyx (#0e0e0e) as a single continuous background across all pages; never introduce a lighter surface or card fill
- Use gs serif 72px exclusively for archive project titles - this is the only place the serif appears
- Space archive list entries at exactly 32px vertical gap to create rhythmic stacking
- Position 3D product renders centered in the viewport with no shadow, platform, or environmental context
- Set all small metadata (nav, labels, captions) in ak 12px with 1.50+ line-height for gallery-wall-label tone

Avoid:

- Do not introduce any accent color, brand color, or chromatic hue - the system is 100% achromatic by design
- Do not add borders, dividers, or background fills to separate sections - use space and type scale instead
- Do not use border-radius on any element - all corners are sharp (0px)
- Do not use shadows, glows, or blur effects for elevation - the design is flat by philosophy
- Do not use the serif (gs) for body copy, navigation, or anything outside the archive project titles
- Do not add gradients, textures, or background patterns to the Onyx canvas
- Do not constrain display headlines with max-width or text-overflow:hidden styling - overflow is the point

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
