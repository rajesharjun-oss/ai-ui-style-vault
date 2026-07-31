# AI Implementation Prompt

Build a Transform-inspired interface using this source-derived style bundle.

Reference site: https://transformfestival.org
Theme: light
Category: Media
North star: stage poster pinned to warm blush paper

Use these palette anchors:

- Blush Cardstock `#f4ede9` for Page background, nav surface, dominant canvas - the warm paper everything sits on
- Ink Black `#000000` for Primary text, section headings, hairline borders, icon strokes
- Paper White `#ffffff` for Card surface, dark-section text, button labels on chromatic fills
- Ash Gray `#d9d9d9` for Alternate card surface when a quieter neutral block is needed
- Steel Gray `#767676` for Muted input borders, secondary helper strokes
- Festival Violet `#340068` for Full-bleed section bands, secondary filled CTA, footer background - heavy, immersive, sets the serious stage
- Spotlight Magenta `#fb00c2` for Primary filled CTA (DONATE), pull-quote text, heading borders, interactive emphasis - the loudest ink, reserved for moments that demand attention
- Curtain Orange `#ff1e00` for Pull-quote attribution, decorative heading borders - the warm third color that gives the palette a poster-like three-ink depth

Use these typography anchors:

- Walsheim `--font-walsheim` for Single-family type system used for everything from nav to display; the broad weight range (400-900) carries the entire tonal system so color never has to shout alone

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 16px.
- Element gap: 16px.

Build these component patterns where relevant:

- Primary Magenta CTA: Donate and other high-priority filled action buttons
- Secondary Violet CTA: Lower-priority filled action, event recaps, dark-band call-to-action
- Ghost Navigation Link: Primary nav items, inline text links
- Header Bar: Persistent top navigation across all pages
- Hero Stage Panel: Above-the-fold performance introduction
- Pull-Quote Band: Editorial testimonials, press quotes, voice-of-the-festival moments
- Section Heading Block: Introduces news, archive, programme, and content grids
- News Card: Editorial card in content grids (news, opportunities, archive)
- Input Field: Newsletter, search, and form fields
- Outlined Social Icon: Instagram, Facebook, ticket-link icons in header and footer
- Page Footer: Site-wide closing band
- Pill Link Chip: Tag, category, or filterable inline link

Do:

- Use Walsheim 700-900 for all headings and display text - never below 700, the heavy weight is the brand's voice
- Use 50px border-radius only on pill chips and link tags, and 0px on everything else - the radius dichotomy is intentional
- Use -0.02em tracking across every size; do not relax it on display headlines
- Anchor the page on the Blush Cardstock (#f4ede9) canvas; let dark sections earn their place as full-bleed bands
- Reserve Spotlight Magenta (#fb00c2) for primary CTAs and editorial emphasis; never use it as a passive background
- Keep the palette to three chromatic accents plus the cream/black/white neutrals; resist adding more colors
- Use full-bleed photographs as section backgrounds with no gradient overlay or border

Avoid:

- Do not introduce shadows, glows, or blur effects - depth is built through flat color, not elevation
- Do not use thin or light weights (under 700) for headings or display text
- Do not round cards, buttons, or images - only pills get radius
- Do not use Curtain Orange (#ff1e00) for buttons or CTAs - it is a decorative editorial accent only
- Do not place content directly on Spotlight Magenta or Festival Violet without testing contrast; always use Paper White for text on these surfaces
- Do not stack more than two chromatic accents in one component - the palette relies on restraint
- Do not use gradients - no gradient tokens exist and the system is deliberately flat

Source prompt cues:

Quick Color Reference:
- text: #000000
- background: #f4ede9
- border: #000000
- accent: #fb00c2
- primary action: #fb00c2 (filled action)
- dark band: #340068
- editorial accent: #ff1e00

Example Component Prompts:
1. Create a primary donate button: filled Spotlight Magenta (#fb00c2) background, Paper White (#ffffff) label, Walsheim 800 uppercase at 18px, 8px vertical padding, 16px horizontal padding, 0px border-radius.
2. Create a pull-quote band: full-bleed Festival Violet (#340068) background, left-aligned display quote in Spotlight Magenta (#fb00c2) at 56px Walsheim 700 with -1.12px tracking, attribution below in Curtain Orange (#ff1e00) at 24px Walsheim 700, 80px vertical padding.
3. Create a news card: top-anchored full-bleed photograph, 0px border-radius, Paper White (#ffffff) body below, title in Ink Black (#000000) at 22px Walsheim 700 with -0.44px tracking, 16px internal padding.
4. Create a header bar: Blush Cardstock (#f4ede9) background, wordmark 'TRANSFORM' in Walsheim 900 at 24px uppercase in Ink Black, nav links inline in Walsheim 700 at 18px, magenta DONATE button right-aligned, outlined social icons after it.
5. Create a section heading: centered Ink Black (#000000) text in Walsheim 900 at 56px with -1.12px tracking, 80px vertical breathing room above and below, single line, no decoration.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
