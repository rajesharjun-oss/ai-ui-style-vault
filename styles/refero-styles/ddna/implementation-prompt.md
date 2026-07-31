# AI Implementation Prompt

Build a ddna-inspired interface using this source-derived style bundle.

Reference site: https://d-d-n-a.com
Theme: light
Category: E-commerce
North star: warm museum vitrine on raw linen

Use these palette anchors:

- Stone Charcoal `#444242` for Primary text, navigation links, hairline borders, footer anchors - dark warm gray carries the same temperature as the cream surfaces it sits on, never pure black
- Linen Cream `#efe3dc` for Heading text, footer surface, and the lighter plane in the surface stack - sits one step above the canvas
- Warm Sand `#dacabf` for Page canvas - the dominant field every section and hero lives on
- Dust `#938a83` for Secondary borders and dividers when Stone Charcoal would be too heavy
- Mortar `#595552` for Muted body text and subdued borders - the quietest readable neutral

Use these typography anchors:

- Basis `--font-basis` for Body, nav, labels, captions - the only text family used for everything below display. The 0.066-0.099em tracking on 10-14px is the signature: it makes small text feel like a printed catalogue label rather than screen UI.
- Favorit `--font-favorit` for Display and heading - set at a single 30px size, weight 400 only. The narrow, slightly quirky character shapes (open apertures, subtle inktraps) carry all the personality the system allows. No bold weight exists.

Use these layout rules:

- Base spacing: 4px.
- Density: spacious.
- Page max-width: .
- Section gap: 100px.
- Card padding: 135px.
- Element gap: 20-25px.

Build these component patterns where relevant:

- Top Navigation: Site header
- Text Link with Arrow: Primary action affordance
- Product Card: Jewelry item display
- Hero Composition: Above-the-fold brand statement
- Statement Paragraph: Brand body copy
- Section Container: Vertical rhythm unit
- Footer: Site footer
- Image Label: Product caption overlay

Do:

- Set all text at weight 400 - never introduce bold or semibold weights, the system has no hierarchy through weight
- Use 0.066em letter-spacing on 14-15px text and 0.099em on 10px captions to maintain the catalogue-label feel
- Keep the palette to five warm neutrals (#444242, #595552, #938a83, #dacabf, #efe3dc) - no accent colors, no blue links
- Use Favorit at 30px with line-height 2.0 for any heading or statement - one size, one leading, one weight
- Build depth through tonal layering (sand cream charcoal), never through box-shadow
- Pair every affordance with a downward or rightward arrow glyph instead of a button shape
- Use full-bleed product images with 0px radius - let the texture and material do the work

Avoid:

- Do not add drop-shadows, blurs, or any z-axis elevation to cards, buttons, or images
- Do not introduce a brand accent color - the iridescent orbs are content, not tokens
- Do not use bold (600/700) or semibold (500) weights at any level
- Do not use border-radius greater than 0px on any component - sharp edges preserve the printed-catalogue feel
- Do not set body copy below 14px or above 17px; display should stay at 30px
- Do not fill a button background - the system uses text links with arrow glyphs, not filled rectangles
- Do not separate sections with hairline dividers; use 100px of whitespace as the only separator

Source prompt cues:

**Quick Color Reference**
- text: #444242
- background: #dacabf
- surface: #efe3dc
- border: #444242 (primary) / #938a83 (secondary)
- muted text: #595552
- primary action: no distinct CTA color

**Example Component Prompts**

1. *Create a hero section*: Full-viewport Warm Sand (#dacabf) background. Centered statement copy in Favorit 30px, weight 400, line-height 2.0, color #444242, max-width ~600px, 100px bottom padding. Below the copy, a ghost text link: 'Explore Collections ' in Basis 14px, weight 400, letter-spacing 0.066em, color #444242. No background, no border, no shadow.

2. *Create a product card*: Full-bleed image, 0px radius, no border, no shadow. Product name in Basis 10px, weight 400, letter-spacing 0.099em, color #444242, set on a Linen Cream (#efe3dc) chip at top-left with 25px padding. Card sits on Warm Sand (#dacabf) canvas with 25px gap to neighbors.

3. *Create the navigation bar*: Transparent background over Warm Sand (#dacabf) canvas. Logo wordmark (Favorit 30px, weight 400, #444242) at far left. 3-4 nav links at far right in Basis 14px, weight 400, letter-spacing 0.066em, color #444242. 50px horizontal padding, 25px vertical padding. No border, no shadow, no background fill.

4. *Create a footer*: Linen Cream (#efe3dc) background, 50px padding. 2-3 minimal link columns in Basis 10-14px, weight 400, letter-spacing 0.066-0.099em, color #444242. No logo repeat, no social icons, no filled buttons.

5. *Create a section band*: Full-bleed Warm Sand (#dacabf) background, 100px vertical gap to the next section, 50px horizontal padding. Centered heading in Favorit 30px weight 400 line-height 2.0, color #444242. No dividers, no card containers, no shadows.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
