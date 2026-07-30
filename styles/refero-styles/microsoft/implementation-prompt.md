# AI Implementation Prompt

Build a Microsoft-inspired interface using this source-derived style bundle.

Reference site: https://www.microsoft.com
Theme: light
Category: Other
North star: Corporate blue retail catalog - think 4-square logo against a white showroom floor with one accent blue guiding every interaction.

Use these palette anchors:

- Microsoft Blue `#0067b8` for Primary action background, link text, navigation accents, icon strokes - the single chromatic authority in the system, used for all filled CTAs and interactive highlights
- Pure White `#ffffff` for Page background, card surfaces, button text on blue, surface elevation
- Mist Gray `#f2f2f2` for Footer background, subtle surface tone, page canvas under cards
- Carbon Black `#000000` for Primary text, card borders, hairline dividers - the dominant typographic and structural color
- Steel Gray `#616161` for Secondary text, navigation text, muted UI elements, footer copy
- Graphite `#262626` for Body text variant, list borders, navigation dividers, secondary headings
- Deep Charcoal `#171717` for Dense text blocks, list separators, button border variant - the darkest neutral after pure black

Use these typography anchors:

- Segoe UI `--font-segoe-ui` for Sole typeface across the entire system - navigation, body, headings, buttons, footer. Weight 400 is the workhorse; weight 600 is reserved for headings and button labels to create section-level contrast without switching families. Segoe UI's humanist proportions and open apertures give the system its calm, enterprise-confident voice - the type does not perform, it informs.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 48px.
- Card padding: 24px.
- Element gap: 8px.

Build these component patterns where relevant:

- Primary Action Button: Filled CTA used for 'Comprar ahora', 'Descargar ahora', 'Unirse ahora', 'Mas informacion'
- Ghost Text Link: Inline links in navigation rows, card text links, footer links
- Product Card: Grid card for Surface, Xbox, accessories, and software promotions
- Hero Card Overlay: White text card layered over a blue photographic hero
- Category Icon Link: Icon + label links for 'Comprar portatiles Surface', 'Comprar consolas y juegos para Xbox', etc.
- Top Navigation Bar: Sticky header with Microsoft logo, product links, and account controls
- Hero Banner: Full-width promotional section with product or lifestyle photography
- Carousel Pagination Dots: Slide indicator for hero carousel
- Feature Band: Full-width promotional section (e.g., Microsoft Edge, AI for Earth)
- Section Heading Group: Text block above a card grid or content row
- 4-Column Card Grid: Product or content grid layout
- Footer: Site-wide footer with links and legal

Do:

- Use #0067b8 as the sole chromatic color for all filled action buttons, link text, and active navigation indicators
- Set button border-radius to 2px - subtle rounding, not pill-shaped
- Apply the card shadow stack (rgba(0,0,0,0.13) 0 3px 7px + rgba(0,0,0,0.11) 0 1px 2px) only to product cards in grids
- Use Segoe UI weight 600 for headings, card titles, and button labels; weight 400 for all body, nav, and link text
- Maintain 8px as the base spacing unit - use 8/16/24/48px steps for padding, margins, and gaps
- Layer white overlay cards (32-48px padding, no border) over full-bleed hero photography for text legibility
- Keep card grids at 4 equal columns with 16-24px gaps inside a max-width 1200px container

Avoid:

- Do not introduce additional brand colors - the system is monochrome plus #0067b8
- Do not use border-radius greater than 2px on buttons, inputs, or cards - keep edges nearly sharp
- Do not apply shadows to navigation bars, buttons, or text blocks - only to product cards
- Do not use Segoe UI weights other than 400 and 600 - no 300 whisper-weights or 700 bold declarations
- Do not create outlined or ghost button variants - all actions are filled blue or simple text links
- Do not add decorative gradients - the system relies on photography and flat surfaces
- Do not use fully saturated icons - category icons should be 1.5-2px stroke outline style in #616161 or #000000

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #ffffff
- border: #000000 (hairline, 1px)
- accent: #0067b8 (links, icons, navigation)
- primary action: #0067b8 (filled action)
- muted surface: #f2f2f2 (footer)

**3-5 Example Component Prompts**

1. Create a Primary Action Button: #0067b8 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. *Create a hero section with overlay card:* Full-bleed blue gradient background (linear from #0050a0 to #003a75). White overlay card on left side: 400px wide, 48px padding, no radius, no border, white background. Headline: Segoe UI 600, 37px, #000000. Body: Segoe UI 400, 15px, #000000. Primary button (#0067b8 background, white text, Segoe UI 600, 15px, 2px radius, 12px 16px padding). Right side: product render or large brand text in white Segoe UI 600, 48px.

3. *Create a category icon-link row:* 5-column row, centered, 24px gap between items. Each item: 24px outlined icon (#616161, 1.5px stroke) stacked above label. Label in Segoe UI 400, 15px, #0067b8. No background, no border. Items are links with underline on hover.

4. *Create a top navigation bar:* White background, 16px vertical padding. Left: Microsoft 4-square logo (16px). Center: nav links in Segoe UI 400, 15px, #616161 with 16px horizontal padding. Right: search icon, cart icon, sign-in button - all #000000, 24px icons. No border-bottom, no shadow.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
