# AI Implementation Prompt

Build a Klim-inspired interface using this source-derived style bundle.

Reference site: https://klim.co.nz
Theme: mixed
Category: Design
North star: typographic gallery in a black box - a curator's vitrina where each specimen hangs in its own dark band

Use these palette anchors:

- Studio Charcoal `#101c19` for Page canvas, primary background - a near-black with a green undertone that reads as neutral but feels warmer than pure black
- Gallery Black `#000000` for Feature bands, specimen backgrounds, header bar - pure black for maximum type contrast
- Charcoal Surface `#1c1c1c` for Elevated surface, input fields, secondary panel backgrounds - one step lighter than the canvas
- Slate Mist `#3c585f` for Muted accent band, tertiary surface - desaturated blue-gray used as an alternate section background
- Graphite `#555555` for Mid-tone borders, muted body text on light sections, card outlines
- Steel `#646464` for Secondary borders, subdued link text on dark backgrounds
- Fog `#7f7f7f` for Tertiary borders, inactive UI elements, secondary text
- Ash `#939393` for Medium-contrast borders, control outlines, and structural separators. Do not promote it to the primary CTA color
- Marble `#f9f9f9` for Light-mode page canvas, pale gray that photographs cleanly for specimen presentations
- Bone `#ffffff` for Primary text on dark backgrounds, type specimen letterforms, button labels, high-contrast surfaces
- Flare Orange `#d33c03` for Label tags, collection names, editorial annotations - a saturated vermilion that reads as the foundry's signature mark on light backgrounds
- Signal Red `#e90702` for Hot accent on dark surfaces, inline highlights, the reddest red in the palette for maximum voltage
- Electric Blue `#24a7f2` for Interactive highlights, active states, link emphasis - a bright cyan-blue that pops against black
- Mint Pulse `#93ffe6` for Decorative text accent, special-occasion highlights - a pale mint used sparingly for emphasis
- Canary `#ffff79` for Rare chromatic accent, used for the highest-attention text moment on dark backgrounds
- Blush `#ffe6d9` for Soft warm accent, subtle text tint - a cream-pink that warms dark sections without competing with type

Use these typography anchors:

- SOEHNE `--font-soehne` for SOEHNE - detected in extracted data but not described by AI
- Sohne `--font-shne` for Primary UI typeface - used for navigation, body text, buttons, form labels, and all functional interface text. Tight line-heights (0.98-1.20) at display sizes; generous (1.50) for body. Two weights only: regular for content, bold for emphasis. Tabular numerals via tnum for price alignment; ordinals via ordn.
- Sohne Ikon `--font-shne-ikon` for Iconographic variant of Sohne for interface glyphs, special characters, and numeric UI elements. Same voice as Sohne but with alternate character forms via calt and tabular figures via tnum.
- SOEHNE_IKON `--font-soehneikon` for SOEHNE_IKON - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1440px.
- Section gap: 69px.
- Card padding: 20px.
- Element gap: 10px.

Build these component patterns where relevant:

- Top Bar: Primary site navigation
- Label Tag: Collection or edition annotation
- Typeface Specimen Band: Full-width type showcase row in the font catalogue
- Specimen Variant Row: Individual sub-style entry within a typeface band
- Buy Link: Purchase action for a typeface variant
- Image Specimen: Full-bleed type-in-context or object photography
- Hamburger Menu Trigger: Mobile and desktop menu toggle
- Input Field: Form input for search or filter
- Text Link: Inline hyperlink within body or navigation content
- Section Divider: Horizontal rule between specimen bands
- Collection Annotation: Editorial label overlaid on specimen imagery

Do:

- Set all primary UI text in Sohne 16px/400 with Sohne 700 for emphasis only
- Use Flare Orange (#d33c03) for label tags, collection names, and editorial annotations - this is the foundry's signature mark
- Alternate specimen band backgrounds between #000000, #1c1c1c, #3c585f, and #f9f9f9 to create rhythm without dividers
- Use 2px border-radius on all interactive elements (buttons, tags, inputs) - this near-sharp corner is the system's geometric signature
- Set type specimens in the typeface they represent at 36px+ - the font IS the content
- Enable tnum and ordn font features on all Sohne usage for consistent number and ordinal rendering
- Maintain tight spacing: 8px component padding, 10px element gaps, 20px horizontal page padding

Avoid:

- Do not introduce drop shadows, gradients, or glow effects - the system is flat and shadowless
- Do not use border-radius greater than 2px - the design is intentionally near-sharp
- Do not use color on large background fills - chromatic colors are reserved for tiny label tags and text accents
- Do not set body or display type in colors other than Bone (#ffffff on dark) or Graphite (#555555 on light) - chromatic type is for special emphasis only
- Do not add visible section dividers or whitespace gaps larger than ~69px between bands - the background color shift IS the divider
- Do not use system fonts for UI text - Sohne is the voice of the interface
- Do not place more than one chromatic color in a single component - each color punch gets its own moment

Source prompt cues:

**Quick Color Reference**
- text (on dark): #ffffff
- text (on light): #555555
- background (dark mode): #101c19
- background (light mode): #f9f9f9
- border / outline: #939393
- accent / label tag: #d33c03
- primary action: no distinct CTA color

**Example Component Prompts**

1. **Label Tag**: Flare Orange (#d33c03) background, white Sohne 16px/400 text, 2px border-radius, 8px horizontal padding, 4px vertical padding. Place bottom-left of an image.

2. **Specimen Band (dark)**: Full-width, Gallery Black (#000000) background, 20px horizontal padding, 20px vertical padding. Left: family name in the typeface itself, 36px, Bone (#ffffff). Center: variant list in Sohne 16px, Bone. Right: 'Buy' text in Sohne 16px, Fog (#7f7f7f).

3. **Specimen Band (light)**: Full-width, Marble (#f9f9f9) background. Left: family name in the typeface itself, 36px, Graphite (#555555). Center: variants in Sohne 16px, Graphite. Right: 'Buy' in Sohne 16px, Graphite.

4. **Top Bar**: Full-width, Gallery Black (#000000), 8px vertical padding, 20px horizontal. Left: 'Klim Type Foundry' in Sohne 16px/400 white, then 'Fonts' in Sohne 16px/400 Flare Orange. Right: hamburger in white.

5. **Inline Link on Dark**: Sohne 16px/400, Electric Blue (#24a7f2), no underline, no background. Used for interactive text within specimen descriptions.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
