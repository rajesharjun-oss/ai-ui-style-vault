# AI Implementation Prompt

Build a Maelan Le Meur-inspired interface using this source-derived style bundle.

Reference site: https://maelanlemeur.com
Theme: mixed
Category: Agency
North star: Museum wall, warm parchment and tobacco - a portfolio printed on bone-colored paper with ink-black display type and deep umber chapter breaks.

Use these palette anchors:

- Parchment `#eee9cc` for Primary canvas and card surface - the warm bone tone that carries all body content, tables, and quiet sections
- Aged Linen `#cecab1` for Secondary surface and muted text - slightly deeper parchment for sub-surfaces, helper text, and table headers
- Tobacco Brown `#674825` for Chapter-break sections and featured band backgrounds - rich warm umber that anchors the page's heaviest typographic moments
- Midnight Espresso `#1e1915` for Full-bleed dark sections and navigation background - the near-black that creates the page's dramatic section breaks
- Ink Black `#111111` for Primary text and hairline rules - the deepest tone for body copy, headings, table content, and footer dividers

Use these typography anchors:

- PP Neue Montreal `--font-pp-neue-montreal` for The sole typeface across the entire system - used at every size from 15px captions to 317px display words. Weight stays at 400 throughout, so hierarchy is built purely through scale, whitespace, and the choice of dark or light ground. This single-weight restraint is the signature: no bold, no italic, no medium - just one calm voice that gets larger or smaller depending on how much the page wants to say. Substitute with Inter or Sohne for similar geometric neutrality.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: .
- Card padding: 40px.
- Element gap: 20px.

Build these component patterns where relevant:

- Full-Bleed Dark Section: Chapter-break bands that segment the portfolio
- Display Heading Block: Hero and section statement typography
- Top Navigation Bar: Persistent site navigation
- Text Navigation Link: All interactive navigation throughout the site
- Section Label Heading: Category headers within the portfolio grid
- Quote / Manifesto Block: Large typographic statement sections
- Project Table: Portfolio listing of works
- Table Row: Individual project entry
- Featured Band Header: Page title section with warm color background
- Footer: Site footer

Do:

- Use PP Neue Montreal 400 at every size - never introduce bold, medium, or italic weights; the single-weight restraint is the signature
- Set all large display text (58px+) with line-height 0.95 to create the tight, architectural rhythm
- Apply 210px vertical padding to full-bleed section bands to create the gallery-wall breathing room
- Use #1e1915 and #674825 as full-bleed chapter breaks - never as card or component backgrounds
- Let display type bleed off the right viewport edge without a max-width container
- Build all navigation as typographic text links at 15-16px uppercase - no buttons, no pills, no fills
- Separate table rows with 1px #111111 hairlines - never use row backgrounds or zebra striping

Avoid:

- Do not introduce accent colors, gradients, or chromatic highlights - the warm earth palette is the entire system
- Do not add shadows, elevations, or depth effects to any component - the design is intentionally flat
- Do not use rounded corners on cards, inputs, or containers - the only radius is 40px, reserved for link hit areas
- Do not set a max-width on hero or display sections - the type is meant to crop at the viewport edge
- Do not use color to indicate interactive states - links remain typographically identical across hover, active, and visited
- Do not add icons, badges, or decorative graphics inside text blocks - the typographic hierarchy carries all meaning
- Do not use line-height above 1.20 for any heading or display size - tight leading is essential to the editorial feel

Source prompt cues:

**Quick Color Reference**
- text: #111111
- background: #eee9cc
- border: #111111
- accent: #674825 (Tobacco Brown)
- dark section: #1e1915 (Midnight Espresso)
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

1. **Full-bleed dark section**: Background #1e1915, full viewport width, 210px padding-top and padding-bottom. Section label in PP Neue Montreal 400 at 58px, color #eee9cc, left-aligned with 40px padding-left. Text reads 'Design de marque'.

2. **Display heading block**: PP Neue Montreal 400 at 225px, line-height 0.95, color #111111 on #eee9cc background. Text: 'Je construis des images aux formes simples et harmonieuses.' The text should fill the full viewport width without a max-width container, bleeding off the right edge.

3. **Project table**: Three columns (PROJET, DESCRIPTION, DATE) on #eee9cc background. Header row in 15px PP Neue Montreal 400, uppercase, color #111111, with 20px vertical padding. Body rows at 16px PP Neue Montreal 400, separated by 1px #111111 hairlines. No row backgrounds, no hover states.

4. **Top navigation bar**: Full-width #1e1915 bar, 15-16px PP Neue Montreal 400. Brand name 'Maelan' left-aligned in #eee9cc. Three nav items (VOUS, REALISATIONS, ECRIVEZ-MOI) right-aligned, uppercase, color #eee9cc. No borders, no background fills on links, no underline.

5. **Featured band header**: Full-width #674825 (Tobacco Brown) section with display text 'Realisations' at 225px PP Neue Montreal 400, color #eee9cc, line-height 0.95. Text left-aligned, bleeding to the right viewport edge. 210px vertical padding.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
