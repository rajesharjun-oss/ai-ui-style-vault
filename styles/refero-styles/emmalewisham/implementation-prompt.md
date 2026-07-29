# AI Implementation Prompt

Build a Emmalewisham-inspired interface using this source-derived style bundle.

Reference site: https://emmalewisham.co.uk
Theme: light
Category: E-commerce
North star: porcelain apothecary at golden hour. Warm linen surfaces cradle jewel-toned glass vessels; the brand violet traces hairlines through the room; serif labels float over clean sans-serif UI like engraved pharmacy signs.

Use these palette anchors:

- Iris Violet `#49369e` for Outlined action borders, link color, heading accents, navigation emphasis - the singular brand hue, deployed as a fine outline or thin underline rather than a filled mass
- Soft Lavender `#a9a7db` for Muted secondary accent for list borders, decorative link borders, and subtle dividers - the diluted echo of Iris Violet used when the full intensity would overpower
- Iris Focus `#524eb7` for Input focus state text/border - a slightly lifted tonal variant of Iris Violet to signal active text fields
- Blush Petal `#ec9bad` for Atmospheric surface wash and decorative accent - warm pink used for full-bleed product stage backgrounds and occasional badge fills
- Pure White `#ffffff` for Card surfaces, product image cutouts, nav and button borders, inverted text on dark or violet fields
- Stone Linen `#f2f1ef` for Page canvas - the warm off-white that grounds every section, used as the base layer beneath product stages and text blocks
- Warm Ash `#a09c97` for Muted background panels, announcement bar, low-emphasis surfaces
- Charcoal `#333333` for Secondary text and low-emphasis fills - softer than pure black for body copy and metadata
- Graphite `#000000` for Primary text, button outlines, icon strokes - used at hairline weights to stay quiet

Use these typography anchors:

- Martina Plantijn `--font-martina-plantijn` for Primary UI and body sans-serif - used for navigation, buttons, body text, product copy, form fields, badges, and micro-labels. The weight 300 thin gives the system its airy, unforced feel; weight 700 is reserved for navigation emphasis and select labels. This is the workhorse - almost everything visible reads in this face.
- Regola Pro Book `--font-regola-pro-book` for Display and editorial serif - used for the brand wordmark and large hero/display copy. Its 80px presence carries the entire brand identity: the 'EMMA LEWISHAM' logotype and product-feature headlines float in Regola Pro Book, creating a distinctive serif-on-sans pairing. The single weight keeps the display quiet and editorial rather than decorative.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1440px.
- Section gap: 48-80px.
- Card padding: 20-30px.
- Element gap: 12px.

Build these component patterns where relevant:

- Brand Wordmark: Primary brand identity lockup
- Outlined Action Button: Primary interactive element
- Ghost Text Link: Secondary navigation and inline links
- Announcement Bar: Top-of-page utility message
- Top Navigation: Primary site navigation
- Full-Bleed Product Stage: Hero and product showcase sections
- Product Card: Grid item for product listings
- Badge: Small status indicators and cart count
- Text Input: Form fields for email, search, checkout
- Body Copy Block: Editorial text sections
- Section Heading: Major section titles
- Footer Link List: Footer navigation columns

Do:

- Use Iris Violet (#49369e) exclusively for outlined action borders and link text - never fill a button or surface with it
- Set the brand wordmark and all display headings in Regola Pro Book at 400 weight, never bold it
- Keep all borders at 1px hairline weight; the system rejects thick borders and shadows
- Use Stone Linen (#f2f1ef) as the default canvas beneath all content; let Blush Petal (#ec9bad) and other atmospheric colors serve as full-bleed product stages, not inline backgrounds
- Use 30px radius on cards and 3px on buttons - the wide card / tight button ratio is the system's signature geometry
- Let product photography occupy the full viewport in hero sections with zero padding around the object
- Pair the sans-serif Martina Plantijn (UI) with the serif Regola Pro Book (display) - never use the serif for body copy or the sans for the wordmark

Avoid:

- Don't fill buttons with Iris Violet or any other brand color - the action style is always outlined, never filled
- Don't apply box-shadows to cards, buttons, or nav - the system is shadow-free and uses hairline borders for definition
- Don't use bold or heavy weights in the serif (Regola Pro Book is 400 only) - the display must stay quiet
- Don't use Blush Petal (#ec9bad) as a text color or border - it's an atmospheric surface wash only
- Don't crowd the canvas with cards or panels - the layout breathes; let sections flow directly on Stone Linen
- Don't use more than one atmospheric color per section - the hero uses Blush Petal alone, never mixed with lavender or violet washes
- Don't use the 50px nav radius on anything other than the cart badge - it is a single accent, not a system-wide pattern

Source prompt cues:

**Quick Color Reference**
- text: #000000 (primary), #333333 (secondary)
- background: #f2f1ef (canvas), #ffffff (card)
- border: #a9a7db (soft), #49369e (emphasis)
- accent: #ec9bad (atmospheric)
- primary action: #49369e (outlined action border)

**Example Component Prompts**
1. Build a hero stage: full-bleed Blush Petal (#ec9bad) background, a centered product bottle image at 60% viewport height, 'Shop now' ghost link in bottom-left as Martina Plantijn 14px Iris Violet text with 12px padding.
2. Build a product card: 30px radius, 20px padding, Pure White (#ffffff) surface, 1px Soft Lavender (#a9a7db) hairline border, product image filling the top 70%, product name in Martina Plantijn 20px Graphite, price in 14px Charcoal below.
3. Build the header nav: transparent background, no border, centered 'EMMA LEWISHAM' wordmark in Regola Pro Book 20px Graphite, left-aligned Shop/Routines/Gifts links and right-aligned utility icons all in Martina Plantijn 13px Graphite, 12px horizontal spacing.
4. Build an outlined action button: transparent fill, 1px Iris Violet (#49369e) border, 3px corner radius, 12px vertical x 5px horizontal padding, 'Add to bag' in Martina Plantijn 14px weight 400 Iris Violet.
5. Build a section heading: 'Our Routines' set in Regola Pro Book 30px weight 400 Graphite, 1.25 line height, 48px top margin from previous section, left-aligned on Stone Linen canvas.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
