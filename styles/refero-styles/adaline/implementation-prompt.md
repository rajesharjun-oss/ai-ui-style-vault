# AI Implementation Prompt

Build a Adaline-inspired interface using this source-derived style bundle.

Reference site: https://www.adaline.ai
Theme: light
Category: AI
North star: botanist's specimen journal beside a developer's terminal - warm linen pages, sage ink annotations, and tracked mono tags.

Use these palette anchors:

- Forest Ink `#0a1d08` for Gray text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color
- Olive Press `#2b390a` for Headings at large sizes, high-contrast body text, hover states on filled buttons
- Sage Leaf `#4a6d47` for Decorative icon accent, badge fills, subtle wash backgrounds on spec cards
- Deep Teal `#2b6b5e` for Secondary category fills, alt-card backgrounds, tonal pair with the dominant greens
- Crimson Specimen `#991e4b` for Red text accent for links, tags, and emphasized short phrases. Use as a supporting accent, not as a status color
- Amber Pin `#80581c` for Yellow wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color
- Linen `#f8f9f5` for Page canvas, default surface - warm off-white with a faint green cast
- Bone `#eff2e8` for Card surface, elevated panels, subtle inset containers
- Mist `#e1e6df` for Hairline borders, card outlines, separator strokes
- Slate Hollow `#2a332a` for Inverse surface for footer and dark bands, modal scrims
- Sage Gray `#6b7860` for Secondary body text, supporting copy, icon strokes
- Sage Mist `#a5ac9f` for Muted helper text, disabled labels, low-emphasis metadata
- Eucalyptus `#c9d5c5` for Soft surface tints, category tag backgrounds, hover wash
- Lichen `#c5ccb6` for Outlined-button border color, link underlines, specimen-card borders
- Blush `#e3c9d0` for Decorative alt-card background, tonal contrast specimen
- Sand `#ad9d80` for Decorative card surface, tertiary alt fill
- Sage Foam `#729d92` for Decorative alt-card surface, soft cool counterpoint to the sage family
- Rose Clay `#c27c93` for Decorative alt-card background, warm-tonal specimen
- Surface Glow `#fdfefb` for Surface-highest token, used for elevated card layers above Linen

Use these typography anchors:

- akkurat `--font-akkurat` for Workhorse sans for body, nav, headings, buttons, cards across the entire system
- Newsreader `--font-newsreader` for Single display-size serif headline - unexpected literary anchor against the utility sans
- Fragment Mono `--font-fragment-mono` for Field-note tagging: badges, category labels, button text, code-lite metadata, tracked micro-copy
- ui-monospace `--font-ui-monospace` for System mono fallback for the tightest micro-tags (8px, 500 weight, 0.04em tracking)
- GT America Mono `--font-gt-america-mono` for GT America Mono - detected in extracted data but not described by AI
- fragmentMono `--font-fragmentmono` for fragmentMono - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1200px.
- Section gap: 96px.
- Card padding: 20px.
- Element gap: 6px.

Build these component patterns where relevant:

- Primary Pill CTA: Filled dark-pill button for top-level conversion (Get Started, header CTA)
- Outlined Ghost Button: Secondary action - Read Docs, Learn More, lower-emphasis navigation links
- Transparent Nav Pill: Header and section-level inline links (Docs, Pricing, Blog, footer links)
- Category Tag (Field Note): Badge above headlines - 'THE SELF-IMPROVING AGENT', section labels, spec IDs
- Specimen Card: Content container for feature blocks, variant comparisons, test-result panels
- Code Block Panel: Terminal-style trace display, code snippets, trace log views
- Trusted-By Logo Strip: Social proof band of partner/company logos
- Hero Headline (Serif Anchor): Opening headline on the page - 'Never stop learning'
- Section Headline (Akkurat): Mid-page section titles - 'Truly understand your agents', 'Evals that write themselves'
- Nav Header: Top-of-page brand and link bar
- Landscape Plate Divider: Full-bleed photographic breaks between content sections
- Footer Band: Closing conversion and link cluster

Do:

- Use the 108px Newsreader 300 serif for the single opening headline on any page; do not repeat it for subheadings.
- Use Akkurat 400 at 18px for body copy with line-height 1.44 - this is the workhorse rhythm.
- Set filled CTA buttons to Forest Ink (#0a1d08) with Linen text and 20px radius; never use a chromatic green or blue for primary action fills.
- Use Fragment Mono 10-11px with 0.04em tracking for category badges, spec IDs, and field-note labels - always uppercase.
- Separate content sections with full-bleed landscape photography instead of dividers or background-color shifts.
- Stack surfaces via 1px Mist (#e1e6df) borders and tonal fills (Linen Bone Eucalyptus); avoid drop shadows.
- Maintain a 6px element gap and 96px section gap as the spatial rhythm across all pages.

Avoid:

- Do not pair the serif display font with sans-serif headings - Akkurat at 30-53px owns all non-display headlines.
- Do not introduce bright chromatic CTAs (blue, red, vivid green) - the action palette stays in Forest Ink and Olive Press.
- Do not add drop shadows to cards or modals; rely on borders and surface tints for separation.
- Do not use icons or illustrations to fill empty space - the layout is intentionally sparse and specimen-like.
- Do not mix the Fragment Mono labels into running body copy - keep mono reserved for badges, IDs, and metadata.
- Do not place content into multi-column dashboard grids; sections are wide, centered, and stacked.
- Do not break the 96px vertical rhythm between major sections - Adaline reads as printed pages, not cards.

Source prompt cues:

Quick Color Reference
- page background: #f8f9f5 (Linen)
- card surface: #eff2e8 (Bone)
- border / hairline: #e1e6df (Mist)
- primary text: #0a1d08 (Forest Ink)
- muted text: #6b7860 (Sage Gray)
- primary action: #2b390a (filled action)

Example Component Prompts
1. Create a Primary Action Button: #2b390a background, #f8f9f5 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. Specimen card: Bone (#eff2e8) background, 10px radius, 1px Mist (#e1e6df) border, 20px padding. Section headline in Akkurat 400, 30px, Forest Ink, letter-spacing -0.6px. Body in Akkurat 400, 18px, Sage Gray. No drop shadow.

3. Trace/log panel: Linen (#f8f9f5) background, hairline Mist border, Fragment Mono 10px at 0.04em tracking for line content, 1px dividers between rows. Status markers as Crimson (#991e4b) 1px rings.

4. Category badge: transparent fill, Fragment Mono 11px uppercase at 0.04em tracking, Olive Press (#2b390a) text, 4px radius or 9999px pill, trailing arrow glyph in the same color.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
