# AI Implementation Prompt

Build a Ragged Edge-inspired interface using this source-derived style bundle.

Reference site: https://raggededge.com
Theme: light
Category: Agency
North star: Editorial brutalism on white marble. Imagine Vogue's typographic confidence merged with a Berlin gallery's color restraint all ink and air, with one burst of color used as exclamation, never decoration.

Use these palette anchors:

- Obsidian Ink `#181f1f` for Primary text, hairline borders, filled action buttons the dominant near-black that carries 90% of the interface
- Paper White `#ffffff` for Canvas background, inverted text on dark blocks, nav/button borders
- Fog `#d1d2d2` for Subtle dividers and secondary borders where Obsidian would be too heavy
- Ash `#a3a5a5` for Muted helper text, inactive button borders, secondary metadata
- Graphite `#374151` for Secondary body text and subtle icon strokes where a lighter black is needed
- True Black `#000000` for Navigation dividers and surface backing for select blocks
- Mint Wash `#eaf7f3` for Soft tinted surface for nav backgrounds and breathing sections barely-there green to warm the white canvas
- Deep Teal `#1f3233` for Dark surface blocks for case study framing and image-overlay panels

Use these typography anchors:

- ABCDiatypeExpanded-Bold Display, brand logo, section headings, project titles, and nav labels. The extremely wide expanded letterforms (letter-spacing -0.02em at 7882px) are the signature element uppercase, never set small under 10px, and reserved for moments that demand visual weight. The 7882px sizes fill the full width of the hero canvas. Weight stays at 400 because the expansion provides all the weight needed; going bolder would distort the geometric proportions. `--font-abcdiatypeexpanded-bold`
- Grit-Regular All body copy, paragraph text, descriptions, and mid-weight headings. A contemporary serif with subtle texture provides editorial gravitas against the expanded display sans. Weight 400 for running text, 500 for emphasized phrases and sub-headings. The 56px size with 1.25 line-height creates dramatic editorial pull-quotes. Pairs with ABCDiatypeExpanded by contrasting serif warmth against geometric coldness. `--font-grit-regular`

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Respect the extracted card, section, and element spacing.
- Preserve the source radius system.

Build these component patterns where relevant:

- Hero Gradient Banner: Full-viewport opening visual
- Pill Navigation Button: Primary nav and utility navigation
- Outlined Accent Button: Secondary call-to-action with chromatic distinction
- Editorial Headline: Section-opening statement
- Case Study Split Block: Project showcase with text-left, image-right layout
- Vertical Project Mark: Overlaid image identity
- Image-Block Panel: Full-bleed case study visual
- Section Divider: Thin horizontal break between content bands

Do:

- Use ABCDiatypeExpanded-Bold only at 10px or above; below that the expanded forms become illegible.
- Pair Grit-Regular body text with ABCDiatypeExpanded-Bold headings never two serifs or two expanded sans in the same block.
- Reserve the 180px section gap for major content divisions; use 80px for within-section breaks.
- Apply the 64px radius to all nav and button surfaces; 4054px for body content blocks.
- Use Iris Voltage (#516fea) only as a 1.5px border on outlined buttons never as a fill, never on text.
- Let the hero gradient be the only colorful surface on any given page; all subsequent sections stay on white or mint.
- Set hero display text at 7882px with -0.02em tracking to achieve the edge-to-edge brand mark effect.

Avoid:

- Do not introduce additional accent colors the system is 98% monochrome; a second chromatic breaks the discipline.
- Do not apply box-shadows anywhere depth comes from surface tone shifts, not elevation.
- Do not use ABCDiatypeExpanded for body copy longer than 45 words; it is a display face, not a running-text face.
- Do not center body text blocks; editorial layouts read left-aligned with generous left margin.
- Do not use border-radius below 40px on any container sharp corners clash with the pill-button system.
- Do not place Iris Voltage on dark backgrounds; it loses its accent role against high-contrast surfaces.
- Do not set the hero gradient above 0deg orientation or stop count; the directional flow is part of the signature.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
