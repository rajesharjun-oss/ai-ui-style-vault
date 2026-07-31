# AI Implementation Prompt

Build a Home-inspired interface using this source-derived style bundle.

Reference site: https://www.airtree.vc
Theme: light
Category: Fintech
North star: Sunlit eucalyptus grove on warm parchment - the design rests on a cream page where ink-black type and a single electric yellow accent do all the talking.

Use these palette anchors:

- Parchment Cream `#f7f6e3` for Page canvas, card surfaces, bordered containers - near-gray cream that warms the entire interface and gives the whole site its paper-like calm; Outlined/ghost action borders, pill outlines, and interactive rings that echo the canvas tone - only visible against darker overlays
- Ink Black `#262d29` for Primary text, navigation, body copy, card borders, icon strokes - the only structural color, used for hairline definition and all readable content
- Electric Lemon `#ffff48` for Filled CTA buttons, active states, standout badges - a single saturated yellow that breaks the cream/ink calm to signal action; the ratio against #262d29 is 13.2:1 AAA

Use these typography anchors:

- Prody `--font-prody` for Display headlines - the signature voice. Used at 131px for the hero statement and 42px for secondary display; the heavy serif counters against the flat grotesque body to create editorial tension. Weight stays at 400; size alone carries the authority.
- SuisseIntl `--font-suisseintl` for Body copy, card titles, subheadings, UI labels - the working typeface. Weight 500 for emphasized text, 600 for card titles, 400 default. Sizes step 13 14 16 19 21 33 42 covering caption through heading.
- SuisseIntl Book `--font-suisseintl-book` for Navigation links, form input text, small button labels - a lighter cut of the same family for quieter interactive surfaces

Use these layout rules:

- Base spacing: 4px.
- Density: spacious.
- Page max-width: 1280px.
- Section gap: 75-112px.
- Card padding: 37px.
- Element gap: 9-20px.

Build these component patterns where relevant:

- Hero Statement: Page-opening headline block
- Pill CTA - Filled: Primary action button
- Pill CTA - Ghost: Secondary action button
- Portfolio Card: Image-first content card in a horizontal carousel
- Carousel Arrow Button: Navigation control for card carousels
- Logo Strip: Portfolio company wordmarks
- Testimonial Block: Founder quote with attribution
- Top Navigation: Site-wide primary nav
- Nav Link Item: Individual navigation entry
- Portfolio Program Card: Text-and-button promotional card
- Footer: Site footer with links and legal

Do:

- Use #ffff48 only for filled primary CTAs - it's the system's only saturated color and its power comes from scarcity.
- Set hero headlines in Prody at 131px with line-height 1.15; let the size do the work, never bold the weight.
- Apply 37px border-radius to all content cards; 18px to buttons; 8px to inputs and nav - this three-tier radius is the system.
- Build all text-heavy pages on the #f7f6e3 canvas with #262d29 type; never invert the page background within a light-mode page.
- Use SuisseIntl Book at 13px for nav, links, and input text; reserve SuisseIntl 500/600 for emphasized body and card titles.
- Space sections with 75-112px vertical gaps to let the cream breathe; dense blocks fight the editorial language.
- Render all portfolio company logos in monochrome #262d29 - color logos break the system's two-tone discipline.

Avoid:

- Never introduce a second saturated color; if something needs emphasis, use the yellow or a weight change, not a new hue.
- Never use #ffff48 for body text, icons, or decorative fills - it is a button color only.
- Never set display type under 80px; Prody at 33px or below loses its editorial character and reads as body text.
- Don't add box-shadow to cards or buttons; the system relies on border-radius and background contrast, not elevation.
- Don't place photography on a white background - always carry the #f7f6e3 warmth behind images to maintain the paper feel.
- Don't use gradients on buttons, cards, or page backgrounds; the only gradient in the system is the hero's subtle sky-to-cream wash.
- Don't bold Prody at 131px - its 400 weight is the brand voice; adding weight flattens the contrast with the body grotesque.

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
