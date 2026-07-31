# AI Implementation Prompt

Build a Bigpicture Company-inspired interface using this source-derived style bundle.

Reference site: https://www.bpco.kr
Theme: light
Category: Agency
North star: Concrete slab typographic manifesto. A black-on-white press kit where oversized Helvetica does the work of photography, and the only texture is a single sheet of crumpled paper under the body type.

Use these palette anchors:

- Press Ink `#121212` for Primary text, hairlines, section borders, icon strokes, footer text - the singular dark tone that carries 95% of all foreground information
- Paper White `#ffffff` for Page canvas, card surfaces, nav pill background, heading-bordered surfaces
- Newsprint `#f1f1f1` for Subtle surface fills, soft borders, hairline dividers, the tone behind the crumpled-paper texture
- Foil Gray `#e1e1e1` for Light borders, icon stroke accents, secondary dividers
- Mute Gray `#c5c5c5` for Tertiary text, disabled state, low-contrast surface lines

Use these typography anchors:

- Helvetica Neue `--font-helvetica-neue` for Universal workhorse - body copy at 17px/1.29, display headlines at 75-274px with -0.04em tracking at the largest sizes, nav labels at 15px
- PPSupplyMono `--font-ppsupplymono` for Meta labels and bracketed captions like [01-N INTRODUCTION] and section tags (ADVERTISEMENTS, CREATIVE/AGENCY, OFFLINE MARKETING) - these are the only typographic accents that break the Helvetica monotony
- PPSupplySans `--font-ppsupplysans` for Secondary nav and footer micro-text where a different sans voice is needed
- Rock Salt `--font-rock-salt` for Rare handwritten signature accent for one or two words per page (e.g. the circled 'pleasure' annotation) - used like a stamp, never for content

Use these layout rules:

- Base spacing: .
- Density: spacious.
- Page max-width: 1440px.
- Section gap: 72px.
- Card padding: 40px.
- Element gap: 50px.

Build these component patterns where relevant:

- Navigation Pill: Sticky top-center nav container
- Logo Wordmark: Top-left brand identifier
- Display Headline: Hero-scale typographic block
- Section Heading: Mid-page editorial headline
- Monospace Meta Tag: Caption-style label
- Body Manifesto Block: Centered editorial paragraph
- Sparkle Divider: Section separator
- Rounded Image Block: Full-bleed hero photography
- Address Block: Contact / location caption
- Handwritten Annotation: Editorial stamp
- Footer Strip: Bottom-of-page meta
- Nav Indicator Globe: Inline iconographic accent

Do:

- Set display headlines at 75-274px in Helvetica Neue 700 with -0.04em tracking - type size is the primary visual mass, not imagery
- Use #121212 as the only foreground color; never introduce chromatic accents
- Apply the 288px border-radius to all full-bleed images to soften architectural/outdoor photography
- Wrap meta labels in square brackets using PPSupplyMono 16px: [SECTION NAME]
- Use 40px radius for the navigation pill and 28px for individual nav items inside it
- Maintain 72px between major sections and 50px between content blocks within a section
- Place the four-pointed sparkle icon in a horizontal row of 4-5 as the standard section divider

Avoid:

- Do not add any color other than the five neutrals (#121212, #ffffff, #f1f1f1, #e1e1e1, #c5c5c5) - zero chroma is the brand
- Do not use box-shadows; depth comes from hairline borders and the paper texture only
- Do not break the all-caps convention on display headlines; mixed case is reserved for the Rock Salt annotation
- Do not use 9999px pill radii on buttons or tags - the largest standard radius is 40px on the nav
- Do not compress line-height below 1.0 on display type, and do not exceed 1.6 on body
- Do not place body copy in a column wider than ~720px - the editorial measure must stay readable
- Do not add hover-lift or transition effects to cards; the aesthetic is static print, not interactive UI

Source prompt cues:

**Quick Color Reference**
- text: #121212
- background: #ffffff
- surface/soft: #f1f1f1
- border: #e1e1e1
- muted: #c5c5c5
- primary action: no distinct CTA color

**Example Component Prompts**

1. *Navigation Pill*: Centered floating container, 40px outer radius, 28px item radius, 1px solid #121212 border, white #ffffff background, 20px horizontal padding, 10px vertical padding. Three text items in Helvetica Neue 15px/500 #121212: HOME (active, with a subtle inset fill), PROJECTS, CONTACT.

2. *Display Headline*: Full-width block, text 'PEOPLE BRAND' in Helvetica Neue 700 at 274px, line-height 1.0, letter-spacing -10.96px, color #121212, on #ffffff background. Two lines, each filling the viewport width.

3. *Monospace Meta Tag*: Single line '[01-N INTRODUCTION]' in PPSupplyMono 16px/400, uppercase, letter-spacing normal, color #121212, centered above a section.

4. *Full-Bleed Image Block*: Photographic image (architectural/outdoor ad) at 100% viewport width, 288px border-radius on all corners, no caption, no border. Place a three-line address caption in Helvetica Neue 17px/1.2 #121212 over the image, top-right area, no background plate.

5. *Sparkle Divider Row*: Five four-pointed sparkle icons in #121212, 20px each, arranged horizontally with 72px gaps, centered on the page. Acts as a section break between major content blocks.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
