# AI Implementation Prompt

Build a Martin Laxenaire-inspired interface using this source-derived style bundle.

Reference site: https://www.martin-laxenaire.fr
Theme: light
Category: Agency
North star: kinetic poster crashing through liquid color waves

Use these palette anchors:

- Ink Black `#121212` for Primary text, all borders, icon strokes, the dominant UI color - every word and divider is this near-black
- Paper White `#ffffff` for Page canvas, surface background, button fills for outlined ghost controls
- Blush Wash `#f9d9f7` for Hero art backdrop, accent surface - the soft pink that hosts the fluid color-shape composition

Use these typography anchors:

- MonumentExtended UltraBold `--font-monumentextended-ultrabold` for Display and heading voice - used at extreme sizes (94-419px) with crushed line-height (0.75-0.85) to create block-of-ink typographic moments. This is the site's signature: oversized, nearly touching, black slab letterforms that read as physical print objects, not web text. At smaller sizes (18-21px) it serves nav and icon labels.
- MonumentExtended Regular `--font-monumentextended-regular` for Secondary display weight - used for subheadings and link labels where UltraBold would be excessive. The Regular cut retains the same wide proportions but with thinner strokes, creating a secondary rhythm below the UltraBold roars.
- Swiss `--font-swiss` for Body and utility voice - the invisible workhorse for paragraphs, button labels, footer text, list items. At 31px it steps into subheading territory. Its neutral, humanist sans character prevents the MonumentExtended from exhausting the reader.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 42px.
- Card padding: 21px.
- Element gap: 21px.

Build these component patterns where relevant:

- Pill Button (Outlined): Primary interactive control
- Pill Button (Filled): Secondary or selected control
- Display Headline (Poster Scale): Hero text moments
- Abstract Wave Composition: Hero art and section dividers
- Minimal Top Bar: Site navigation
- Scroll Cue: Invitation to interact
- Section Heading: Content section titles
- Body Text Block: Paragraphs and descriptions
- Link List Item: Navigation within content
- Footer Mark: Closing signature

Do:

- Use MonumentExtended UltraBold at 94px or larger for any headline meant to be a focal point, with line-height 0.75-0.85
- Set all borders to 1px solid #121212 - no colored borders, no thicker hairlines
- Use 20.93px border-radius for all interactive controls (buttons, tags, indicators) - never square corners on controls
- Keep the page background #ffffff everywhere except the hero zone, which uses #f9d9f7 as the wave-art canvas
- Use Swiss at 16-19px for all body, button labels, and utility text with line-height 1.20
- Position wave-art shapes to intersect headline text, using white text outlines to maintain legibility through the color
- Maintain a 42px minimum vertical gap between content sections to preserve gallery-wall breathing room

Avoid:

- Never use color on functional UI elements - buttons, links, tags, and text are always #121212 on #ffffff
- Never use drop shadows, box-shadows, or any elevation - the design is poster-flat
- Never use border-radius other than 20.93px (for controls) or 0px (for surfaces) - no mixed rounding
- Never set body text larger than 31px or with line-height above 1.20 - the utility voice must stay quiet
- Never use decorative icons or illustrations outside the hero wave composition - the rest of the page is type-only
- Never use #f9d9f7 as a card, section, or component background - it exists solely as the wave-art field
- Never add more than one wave-art composition per page - the collision of monochrome and color is a single-moment effect

Source prompt cues:

**Quick Color Reference**
- text: #121212 (Ink Black)
- background: #ffffff (Paper White)
- border: #121212 (Ink Black, 1px hairlines)
- accent: #f9d9f7 (Blush Wash - hero art backdrop only)
- wave art palette: #7c4dff (vivid violet), #b14dff (magenta-purple), #4d6fff (electric blue), #1a8a8a (deep teal), #ff6db5 (hot pink)
- primary action: no distinct CTA color

**Example Component Prompts**

1. Build a display headline section: Paper White (#ffffff) page background. Headline set in MonumentExtended UltraBold at 167px, line-height 0.75, color #121212, with a 2px white stroke outline where text meets the wave art layer. Behind the text, an organic blob composition using #7c4dff, #b14dff, #4d6fff, #1a8a8a, #ff6db5 on a #f9d9f7 backdrop.

2. Build a pill navigation button: 1px solid #121212 border, transparent background, Swiss 16px weight 400 text in #121212, border-radius 20.93px, padding 8px 21px. On hover, invert to filled #121212 with #ffffff text.

3. Build a section heading and body block: heading in MonumentExtended Regular at 31px line-height 0.85 color #121212 with 31px margin-bottom. Body paragraph in Swiss at 19px line-height 1.20 color #121212, max-width 680px, margin-bottom 21px.

4. Build a minimal top bar: transparent background, full-width, 21px top/bottom padding. Left: 'BRAND NAME' in MonumentExtended UltraBold 18px uppercase letter-spacing 0.1em color #121212. Right: a pill indicator showing '0%' in Swiss 16px inside a 1px #121212 border, border-radius 20.93px, padding 4px 8px.

5. Build a wave-art hero background: full-viewport #f9d9f7 canvas with 5-7 organic, overlapping blob shapes positioned radially from center. Shape fills drawn from the wave palette (#7c4dff, #b14dff, #4d6fff, #1a8a8a, #ff6db5). Each blob has soft, hand-drawn curves - no geometric edges, no gradients, flat fills only.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
