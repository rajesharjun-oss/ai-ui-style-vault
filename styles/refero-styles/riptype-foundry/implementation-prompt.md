# AI Implementation Prompt

Build a Riptype Foundry-inspired interface using this source-derived style bundle.

Reference site: https://www.riptype.xyz
Theme: dark
Category: Other
North star: ink on black paper - the type is the only bright thing in the room

Use these palette anchors:

- Workshop Black `#121212` for Page background, primary canvas - the dark surface the type sits on
- Platen Gray `#292929` for Raised surface for buttons, hover fills, interactive plate
- Bone `#d0d0d0` for Default body text, link strokes, hairline rules, icon outlines
- Ash `#a0a0a0` for Secondary text, metadata, subdued borders and captions
- Paper White `#ffffff` for Headings, display type, high-contrast text, image borders
- Acid Flash `#d9ff00` for Green outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color

Use these typography anchors:

- Office `--font-office` for Sole typeface - used for navigation, body, buttons, specimens, and display. The foundry sells custom type so the UI type IS the product showcase. Weights 400 (regular) for UI and body, 700 (bold) for the large display announcement and emphasis.

Use these layout rules:

- Base spacing: 6px.
- Density: compact.
- Page max-width: .
- Section gap: 84px.
- Card padding: 13px.
- Element gap: 6px.

Build these component patterns where relevant:

- Sidebar Nav Link: Primary navigation entry
- Acid Download Pill: Primary CTA - the single most important action on the site
- Platen Button: Secondary action, secondary CTA
- Font Specimen Row: Core content unit - the product itself
- Annotation Block: Descriptive copy paired with specimens
- Custom Type Image Card: Showcase of a commissioned type project
- Release Announcement Panel: Featured product launch banner
- Decorative Star Mark: Ornamental accent on nav and section headers
- Cart Badge: Persistent shopping indicator
- Section Header: Major content section title

Do:

- Use #d9ff00 exclusively for the Download Pill CTA and decorative star marks - the acid green's power comes from scarcity
- Pair all body text (#d0d0d0) with the Workshop Black (#121212) canvas - contrast ratio 12.2:1 exceeds AAA
- Set type specimens at 43px+ with 0.083em letter-spacing to give the display characters room to demonstrate their own proportions
- Use 6px as the default element gap; 7px rowGap is the specimen-book rhythm
- Communicate elevation through surface tone (#121212 #292929) and 1px #d0d0d0 hairlines, never through shadows
- Keep radius at 0px for cards and images - the only rounded elements are the 144px pill CTA and the 4px standard button
- Default to Office 400 for all UI; reach for Office 700 only for display specimens and emphasis moments

Avoid:

- Do not introduce additional chromatic colors - the red announcement panel and acid green are the only breaks from monochrome
- Do not add drop shadows to any component - the system is intentionally flat and print-referenced
- Do not use rounded corners on cards or images beyond what the data specifies (0px)
- Do not substitute a different display font for specimens - the typeforms on this site ARE the product catalog
- Do not soften the dark canvas with gradients or tints - #121212 is absolute and edge-to-edge
- Do not apply the acid green to body text, icons, or large areas - it loses signal value at any surface area larger than the pill button
- Do not add decorative dividers, background tints, or section backgrounds - content is separated by whitespace and hairlines only

Source prompt cues:

**Quick Color Reference**
- text (body): #d0d0d0
- text (heading): #ffffff
- background: #121212
- border/hairline: #d0d0d0
- accent: #d9ff00 (decoration + outlined action border)
- primary action: no distinct CTA color

**Example Component Prompts**
1. Build a navigation link: transparent background, no border, text in Office 400 at 16px color #d0d0d0, 6px top margin, preceded by a small icon mark. Separated from the next link by a 1px #d0d0d0 hairline.
2. Build a font specimen row: 43px display text in Office 400 with 0.083em letter-spacing, color #d0d0d0, line-height 1.0, with the font name label in 16px #ffffff above it. Dotted #a0a0a0 underline at 7px row gap to the next specimen.
3. Build an acid download pill: 144px border-radius, transparent background, 1px solid #d9ff00 border, text in Office 400 at 12px with 0.083em letter-spacing, color #d9ff00, 8px vertical / 13px horizontal padding, with a small download icon glyph before the label.
4. Build a custom type image card: full-bleed square image, 1px #d0d0d0 border, 0px radius, no padding, optional 12px #a0a0a0 caption below in Office 400.
5. Build a release announcement panel: full-width block, solid red (#d8261b) background with a grain/noise texture overlay, centered white display text at 43px in Office 700 with 0.083em letter-spacing, line-height 1.0.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
