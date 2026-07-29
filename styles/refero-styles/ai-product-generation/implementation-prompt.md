# AI Implementation Prompt

Build a AI Product Generation-inspired interface using this source-derived style bundle.

Reference site: https://fourmula.ai
Theme: light
Category: AI
North star: editorial photography studio on white paper - headline display type as cover, orange as the editor's highlight pen

Use these palette anchors:

- Ink Black `#020108` for Primary text, borders, icon strokes - near-black carries all body and heading copy
- Charcoal `#333333` for Dominant border color across the entire interface, card outlines, dividers
- Steel `#5d5c61` for Secondary borders, muted icon fills, tertiary structural lines
- Pewter `#818084` for Muted helper text, secondary link text, subdued metadata
- Ash `#d7d7d6` for Subtle background washes, low-contrast surface differentiation
- Canvas White `#ffffff` for Card surfaces, image backgrounds, inverted text on dark regions
- Paper `#f7f7f7` for Page background - the dominant canvas tone behind all content

Use these typography anchors:

- Arial `--font-arial` for Arial - detected in extracted data but not described by AI
- SF Pro Display `--font-sf-pro-display` for Sole typeface across the system - display headlines reach 100px at weight 400 with -3.1% tracking, subheadings at 53px weight 500 with -2% tracking, body at 15-17px weight 400. The choice to use weight 400-500 even at display sizes (rather than going bold) is signature: the type commands attention through scale and tightness, not weight. Substitute: Inter, or any geometric grotesque with strong x-height and tight default tracking.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1280px.
- Section gap: 80px.
- Card padding: 27px.
- Element gap: 20px.

Build these component patterns where relevant:

- Display Headline: Hero and section titles at editorial scale
- Section Heading: Mid-page section introductions
- Pill Button (Primary Ghost): Call-to-action and navigation links
- Feature Card: Container for product shots and video previews
- Image Tile: Product photography thumbnail in grid
- Section Tag Badge: Small contextual label above sections
- Product Card Header: Label strip on AI-generated output tiles
- Sidebar Nav Item: Left-edge 'What you can do' navigation
- Media Player Strip: Top bar of the app preview window
- Expand/Action Floating Button: Bottom-right interactive control on sections
- Highlighted Inline Word: Editorial emphasis within running text
- Split Section (Text + Visual): Primary content section layout

Do:

- Use #020108 for all primary text and heading copy - never substitute a softer gray for headlines
- Apply the orange inline highlight pattern (one word in #fd7b03 within an otherwise #020108 sentence) for editorial emphasis in headlines and subheadings
- Reach for display sizes of 73-100px at weight 400 - let scale carry authority, not weight
- Use -0.02em to -0.031em letter-spacing on all text 27px and above; keep tracking normal at 15px and below
- Set border-radius to 9999px for all buttons, links, and pill elements - 7px for cards, 20-27px for images
- Keep the page background #f7f7f7 and card surfaces #ffffff or #f7f7f7 - rely on the two-tone surface step, never on shadow
- Use 27px padding inside cards and 20px gaps between elements; 80px between major sections

Avoid:

- Do not introduce a second chromatic accent - the system is monochrome with a single orange highlight, and adding color dilutes the editorial discipline
- Do not use bold or weight 600+ for headlines - weight 400-500 at large sizes is the signature; going heavy breaks the cover-type feel
- Do not apply box-shadows to cards, buttons, or images - the system is entirely flat; elevation must be communicated through tonal surface steps
- Do not use background colors on text spans, underlines, or pills for emphasis - color swap on a word within running text is the only emphasis pattern
- Do not use the gradient system for large hero backgrounds or section fills - gradients are for accent strokes and small decorative elements only
- Do not introduce more than two border-radius values per component type - 9999px is exclusively for buttons, 7px exclusively for cards, 20-27px exclusively for images
- Do not use fully saturated primaries (pure red, pure green, pure blue) anywhere - the palette's chromatic notes all carry warmth or desaturation

Source prompt cues:

**Quick Color Reference**
- text: #020108
- background: #f7f7f7
- surface (card): #ffffff
- border: #333333
- accent (inline highlight): #fd7b03
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

1. *Display headline with inline highlight*: Render at 100px, SF Pro Display weight 400, line-height 0.94, letter-spacing -3.1px, color #020108. One word within the sentence swaps to Ember Orange (#fd7b03). No background, no border, flush-left.

2. *Split section (text left, visual right)*: Two-column grid, 40%/60% split, 40px column gap. Left column: section tag (12px weight 500, #020108, prefixed with glyph), heading (43px weight 500, tracking -0.645px, #020108 with one orange word), body (15px weight 400, #818084). Right column: bordered app-preview window at 7px radius, #020108 media strip on top (with traffic-light dots), image grid below.

3. *Ghost pill button*: 1px border in #333333, border-radius 9999px, padding 12px 20px, background transparent. Text 14px weight 500, #020108. No shadow, no fill on hover.

4. *Product image tile*: Fills its grid cell, border-radius 20px, no border, no shadow. Image extends to edges. No caption or label inside the tile itself.

5. *Section tag badge*: Pure text at 12px weight 500, #020108, prefixed with a small upward-pointing arrow glyph ( ). Zero background, zero border, sits above the section heading with 10px gap.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
