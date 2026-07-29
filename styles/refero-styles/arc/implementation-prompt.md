# AI Implementation Prompt

Build a Arc-inspired interface using this source-derived style bundle.

Reference site: https://arcboats.com
Theme: light
Category: E-commerce
North star: industrial white gallery above midnight water

Use these palette anchors:

- Bone `#e5e7eb` for Page canvas, card surfaces, hairline dividers between sections, ghost-button borders - the lightest structural gray carries borders, surface, and the dominant background in a near-white mode
- Charcoal `#0a0a0a` for Primary body and heading text, nav links, footer text, filled button text - near-black for maximum legibility without the harshness of pure black
- Paper `#ffffff` for Card surfaces, filled button backgrounds, image overlays, reverse text on dark sections - the brightest structural white
- Obsidian `#000000` for Headings on light canvas where maximum contrast is required, nav background accents - used sparingly only where absolute black is needed
- Deep Current `#031e25` for Dark feature section backgrounds (alternating bands), large image containers - the navy-black that recedes like deep ocean water
- Slate Depth `#1d1d1e` for Secondary dark section background, elevated panels over Deep Current - one step lighter to layer depth within dark bands

Use these typography anchors:

- Soehne `--font-soehne` for All interface type: weight 300 reserved for display headings (48-140px) to create a quiet engineering voice, 400 for body and subheadings, 500 for nav and meta, 600 for button labels. Soehne's geometric neutrality with the extreme -0.043em tracking on display sizes is the signature - it makes headlines feel architectural rather than editorial. Substitute: Inter (closest free analog with matching weights and tracking) or Untitled Sans.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 36-64px.
- Card padding: 20px.
- Element gap: 18-20px.

Build these component patterns where relevant:

- Ghost Navigation Button: Header nav links (SPORT, COAST, COMMERCIAL) and CTAs
- Outlined CTA Button: Primary action on hero (RECREATION, COMMERCIAL) and section CTAs
- Filled Reversed Button: Dark-section actions
- Hero Image Container: Full-bleed opening section with aerial marine photography
- Feature Card: Three-column grid in dark feature section (Advanced Software, Quiet power, etc.)
- Centered Statement Block: Section transition moments (e.g., 'Electric power built for everything the water demands.')
- Hairline Divider: Section separators and grid lines
- Logo Mark: Brand identity in nav
- Overlay Image Frame: In-section photography (product crops, dashboard screenshots)
- Footer Link Row: Footer navigation
- Hamburger Menu Trigger: Mobile or secondary nav
- Meta Label: Pre-headline tags (e.g., 'DESIGNED AND BUILT IN THE USA')

Do:

- Use only Soehne (or Inter substitute) at the weights 300/400/500/600 - never introduce a second typeface family
- Set display headings at 48-140px weight 300 with tracking between -0.021em and -0.043em; the whisper-weight is the signature
- Use 5px radius for all controls (buttons, inputs) and 32px radius for all imagery - never mix or round to 8/12/16px
- Alternate between #e5e7eb / #ffffff light bands and #1d1d1 / #031e25 dark bands for section rhythm - no mid-gray bridges
- Reserve uppercase +0.15em-0.185em tracking for labels, meta, nav, and button text only - never for body or headings
- Let full-bleed aerial marine photography carry the visual weight of hero and feature sections; do not compete with overlaid illustrations or graphics
- Use #e5e7eb hairline 1px borders for all dividers and card edges; avoid colored borders

Avoid:

- Never introduce a chromatic accent color - the system is deliberately monochromatic plus dark teal-navy
- Never use weight 700 or higher - the heaviest weight in the system is 600, and display text stays at 300
- Never add drop shadows, glows, or blur effects to elements beyond the single detected hero shadow
- Never use a border-radius between 6px and 31px - controls stay at 5px, images at 32px, nothing in between
- Never place text directly on a photograph without a darkening overlay or contained card surface
- Never use centered body copy longer than two lines; long-form content goes left-aligned in contained columns
- Never use illustrations, icons-as-decoration, or 3D renders - photography and type are the only visual vocabulary
- Never set body text above 18px or below 14px - the 14-18px range is the readable band

Source prompt cues:

**Quick Color Reference**
- text: #0a0a0a
- background: #ffffff (cards/buttons) / #e5e7eb (canvas) / #031e25 (dark bands)
- border: #e5e7eb (hairline) / #0a0a0a (ghost button)
- accent: none - monochromatic system
- primary action: no distinct CTA color

**3 Example Component Prompts**

1. **Hero section with full-bleed photograph**: Full-viewport dark ocean aerial image as background, object-fit cover. Bottom-left overlay text: 11px Soehne weight 500 uppercase at +0.185em tracking in #ffffff with flag icon, reading 'DESIGNED AND BUILT IN THE USA'. Below it, 48px Soehne weight 300 in #ffffff at -0.021em tracking reading 'Electrifying the marine industry'. Two outlined ghost buttons below, each 5px radius, 1px #ffffff border, 11px Soehne weight 500 uppercase +0.15em, 20px padding, reading 'RECREATION' and 'COMMERCIAL'.

2. **Centered statement block**: Full-width #ffffff band, 64px vertical padding. Centered text, max-width 720px: 32px Soehne weight 300 in #0a0a0a at -0.016em tracking, two lines: 'Electric power built for / everything the water demands.' No other elements - statement alone.

3. **Feature card in dark section**: 32px-radius image filling 100% column width at top (aerial boat shot). Below, 20px padding, #031e25 background extending. Heading: 22px Soehne weight 400 in #ffffff at -0.012em tracking. Body: 16px Soehne weight 400 in #ffffff at default tracking, max 2 lines. No border, no shadow, no card chrome beyond the dark surface.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
