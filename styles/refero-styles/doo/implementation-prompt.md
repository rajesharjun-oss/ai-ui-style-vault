# AI Implementation Prompt

Build a Doo-inspired interface using this source-derived style bundle.

Reference site: https://getdooapp.com
Theme: light
Category: Productivity
North star: pastel sticky notes drifting on white linen

Use these palette anchors:

- Indigo Pulse `#3b3996` for Supporting palette color for small decorative accents when the core palette needs contrast. Do not promote it to the primary CTA color
- Slate `#6e6d7a` for Hairline borders, dividers, secondary text, list separators - the structural gray that quietly defines the page grid
- Graphite `#383938` for Navigation text, heading text, dark UI elements - the primary readable dark on white
- Ink `#111111` for Headline color, strongest body emphasis, near-black for maximum contrast on light surfaces
- Paper `#ffffff` for Page background, card surfaces, text on dark/indigo fills - the dominant canvas
- Mist `#edeef3` for Elevated panels, subtle background washes, light borders - the cool-tinted off-white that lifts content above the page
- Cloud `#f7f7f7` for Secondary card surfaces, quiet content panels
- Mint Whisper `#c3f5dd` for Task category tag accent (product UI), logo green dot - pastel annotation, not interface chrome
- Lavender Drift `#d1cafa` for Task category tag accent (product UI), logo blue dot - pastel annotation

Use these typography anchors:

- Avenir Next `--font-avenir-next` for Sole typeface across the entire system - nav, body, headings, display. Avenir Next's geometric humanism gives the page a calm, friendly, Apple-adjacent feel. Weight 400 carries everything; weight 600 is reserved for navigation and small emphases. Display headlines at 65px with negative tracking create a compressed, confident presence rather than shouting.

Use these layout rules:

- Base spacing: .
- Density: spacious.
- Page max-width: 1200px.
- Section gap: 100-140px.
- Card padding: 30px.
- Element gap: 20-26px.

Build these component patterns where relevant:

- Primary CTA Button: Single conversion action per screen
- Navigation Bar: Top-level site navigation
- Hero Section: Above-the-fold value proposition
- Product Showcase Frame: Multi-device product display
- Task Card (Product UI): Individual task/reminder item within the app
- Category Color Tag: Task categorization indicator
- Press Logo Strip: Social proof / press mentions
- Feature Section: Product capability showcase with large headline
- Logo Mark: Brand identity anchor
- Section Divider: Visual separation between content blocks

Do:

- Use Indigo Pulse (#3b3996) for exactly one CTA per screen - it is the only saturated fill color on the marketing surface and loses power if overused
- Set all buttons and links to 39px border-radius for the pill shape; set all cards to 30px radius - these two radii are the system's only curves
- Use Avenir Next 400 for all display and body text; reserve weight 600 for nav items and small labels only
- Apply -0.04em letter-spacing to any text 29px and above; use 0.1em tracking on 13px labels for a small-caps eyebrow effect
- Achieve separation with whitespace and Slate (#6e6d7a) hairlines - never with drop shadows
- Keep the marketing surface monochrome; let the product UI's pastel category tags carry all color in screenshots
- Center-align hero and feature headlines; use max-width 1200px container for all content blocks

Avoid:

- Don't introduce additional chromatic UI colors on the marketing page - Indigo Pulse is the only saturated fill permitted
- Don't use drop shadows, gradients, or glow effects - the design is deliberately flat and paper-like
- Don't use any border-radius value other than 30px (cards) or 39px (buttons/links/pills)
- Don't use weight 700 or 800 - Avenir Next caps at 600 in this system, and the whisper-weight 400 headlines are the signature
- Don't add background colors to content sections - the page stays Paper white; use Mist (#edeef3) only for specific elevated panels
- Don't use icons or decorative graphics on the marketing page - product photography and the tri-dot logo are the only visual elements
- Don't use tight column grids; the layout is centered and spacious, not information-dense

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
