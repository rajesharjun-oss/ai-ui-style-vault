# AI Implementation Prompt

Build a Josh Warner-inspired interface using this source-derived style bundle.

Reference site: https://www.joshwarner.design
Theme: dark
Category: Design
North star: black void gallery wall

Use these palette anchors:

- Void `#0f0f0f` for Page canvas and primary surface - the base layer beneath all artwork, slightly lifted from pure black to prevent OLED banding in the dark void
- Absolute `#000000` for Hairline borders, image containers, icon strokes, footer dividers - pure black acts as the structural ink that defines edges in the absence of visible card surfaces
- Charcoal `#1a1a1a` for Elevated footer surface and deeper UI panels - a single step up from canvas for zone separation without breaking the dark void
- Faint `#080808` for Shadow base for subtle elevation effects - nearly invisible against canvas, used in box-shadow compositions for soft ambient lift
- Bone `#f0f0f0` for Primary text color, nav item fills, filled button background - warm off-white replaces pure white to soften contrast against the black void and reduce eye strain
- Ash `#b8b8b8` for Secondary body text, subdued helper labels, muted metadata - sits one step below Bone for non-emphasized copy without losing legibility on dark surfaces
- Graphite `#696969` for Tertiary text and border accents on headings - used sparingly for fine print and inactive labels that should recede
- Live Wire `#08ff00` for Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content

Use these typography anchors:

- Inter Display `--font-inter-display` for Primary typeface across all UI, body, navigation, and headings - used exclusively at weight 400 with no weight variation, creating a flat, even visual texture where size and spacing alone carry hierarchy. Substitute with Inter (free, near-identical metrics).
- System sans-serif `--font-system-sans-serif` for Micro-UI labels (12px) - system stack for the smallest utility text where font loading overhead isn't justified

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1200px.
- Section gap: 60-64px.
- Card padding: 14px.
- Element gap: 10px.

Build these component patterns where relevant:

- Pill Navigation Button: Top-center nav items (Projects, Art, Info) and ghost nav controls
- Filled CTA Button: Primary action - Contact, Hire me
- Status Indicator: Availability signal in footer/hero
- Avatar Badge: Brand identity mark in top-left nav
- Coming Soon Pill: Project status badge on case study previews
- Hero Art Container: Full-bleed 3D render or photographic artwork
- Project Showcase Panel: Individual case study preview (phone mockup in second screenshot)
- Footer Bar: Site footer with bio and CTA
- Tagline Headline: Hero left-aligned copy block
- Subtitle/Body Text: Supporting paragraph text
- Image Thumbnail: Small image containers and inline media

Do:

- Use Bone (#f0f0f0) for all text on the dark void - never use pure white, which clashes with the warm off-white palette
- Apply 100px border-radius to every interactive button, badge, nav item, and avatar - the pill shape is the system's signature geometry
- Keep all type at Inter Display weight 400 - never introduce bold or semibold weights; build hierarchy through size and spacing only
- Use 0.04em letter-spacing on all text - this consistent positive tracking is what makes the whisper-weight type legible and gives the system its measured, deliberate feel
- Reserve Live Wire (#08ff00) exclusively for the availability status dot - it is the only chromatic color and must appear nowhere else
- Set page backgrounds to Void (#0f0f0f), not pure black - the near-black prevents OLED smearing and creates a subtle canvas depth
- Use 4px border-radius for image containers and 100px for all interactive elements - maintain the sharp/round duality

Avoid:

- Don't introduce any new accent colors beyond Live Wire green - the system is deliberately monochromatic and any additional hue will break the gallery void
- Don't use drop shadows for card or surface elevation - depth must come from the artwork itself or surface tone shifts, not from shadow stacks
- Don't bold headlines or use weight 500+ - the entire type system breathes at weight 400; adding weight disrupts the flat, even texture
- Don't use sharp corners (<12px) on buttons, nav items, or badges - the pill geometry is the system's visual identity
- Don't use pure black (#000000) as a fill background for cards or surfaces - reserve it for hairline borders and edges; use Void (#0f0f0f) for surfaces
- Don't place body text below 14px or above 40px - the type scale is deliberately compressed; deviation breaks the editorial restraint
- Don't add gradients, glows, or color washes to UI elements - the system's visual energy comes from the 3D/photographic content, not from UI decoration

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
