# AI Implementation Prompt

Build a Vanmoof-inspired interface using this source-derived style bundle.

Reference site: https://www.vanmoof.com
Theme: mixed
Category: E-commerce
North star: cinematic monochrome showroom

Use these palette anchors:

- Carbon `#222222` for Navigation bar, dark surface panels, primary text on light, logo wordmark fill - the near-black anchor of the system, softer than pure #000 for reduced eye strain on large surfaces
- Obsidian `#000000` for Body text, headline text on light surfaces, footer text - reserved for highest-emphasis type where absolute black is needed for maximum contrast (21:1 on white)
- Graphite `#313131` for Secondary text, link text on light, button labels on light surfaces - the mid-dark step between Carbon and Obsidian for hierarchy without a hue shift
- Frost `#ffffff` for Page canvas for content sections, card surfaces, icon fills on dark hero, button text on dark fills
- Paper `#f7f7f7` for Subtle surface tint alternating with pure white for section banding, elevated card backgrounds when pure white feels too sharp
- Mist `#e5e7eb` for Hairline borders, dividers, nav separator lines, input borders, card outlines - the most-used color in the system by frequency (1231 occurrences), defining structural edges without visual weight
- Ash `#e0e0e0` for Secondary surface fills, muted background panels, subtle hover states - one step deeper than Mist for surfaces that need slightly more presence

Use these typography anchors:

- Unica77LLWeb `--font-unica77llweb` for Primary typeface for all UI and editorial text. Weight 400 for body and navigation, weight 600 for subheadings and button labels, weight 700 for product-name hero displays (S6, A5 at 280px) and section headings. The geometric humanist character with its tall x-height carries authority at massive sizes while remaining legible at 12px. The 280px step is the signature - product names function as graphic objects, not text.
- Unica77Mono `--font-unica77mono` for Monospaced companion for technical metadata, spec labels, navigation micro-text, and any data-adjacent content (dimensions, weights, delivery estimates) where tabular alignment matters

Use these layout rules:

- Base spacing: 8px.
- Density: compact.
- Page max-width: 1440px.
- Section gap: 64px.
- Card padding: 24px.
- Element gap: 8px.

Build these component patterns where relevant:

- Full-Bleed Dark Hero Panel: Cinematic product showcase
- Product Name Display: Hero typographic element
- Ghost CTA Button: Primary call-to-action
- Top Navigation Bar: Primary site navigation
- VANMOOF Logo Pill Badge: Brand mark in navigation
- Country Selector Bar: Localization prompt
- Feature Card Grid Item: App/feature section content card
- App Feature Icon: Visual identifier for feature cards
- Section Header: Editorial section title
- Award Badge (iF Design Gold): Trust/credential marker
- Hero Support Text Block: Hero secondary messaging
- Delivery/Reservation Footer Link: Micro-CTA at hero base

Do:

- Use 280px Unica77LLWeb weight 700 in #ffffff for all hero product names - this is the single most recognizable typographic signature
- Set button and nav radius to 2px; set card and link radius to 8px; use 9999px only for the VANMOOF logo pill - the geometric sharpness is intentional, not lazy default rounding
- Maintain 8px as the base spacing unit; snap all padding, margins, and gaps to multiples of 4px
- Render all icons as 1.5px stroke line-art in #222222 - no filled icons, no multicolor iconography, no emoji-style pictograms
- Use #e5e7eb for all structural dividers and borders; never use a heavier border weight than 1px
- Let product photography provide all color and atmosphere in hero sections - never add background tints, overlays, or gradients to UI chrome
- Alternate between #ffffff and #f7f7f7 for section banding in content areas to create rhythm without borders

Avoid:

- Do not introduce any chromatic color (red, blue, green, purple) to the UI system - the monochromatic discipline IS the brand identity
- Do not use drop shadows, elevation, or blur effects on cards or buttons - flat surfaces only, separated by whitespace and hairlines
- Do not center hero text - always anchor product names left and supporting text right for editorial tension
- Do not set body text below 14px or above 18px; do not set display text below 80px (except the 280px hero step)
- Do not use border-radius values other than 2px (controls), 8px (containers), or 9999px (logo pill) - no 4px, 6px, 12px, 16px, or 24px radii
- Do not add background colors, patterns, or decorative graphics to white content sections - the product and typography carry the visual weight
- Do not use the Gold Award badge color (#FFD700 or similar) as a brand accent - it is a third-party credential, not a design system token

Source prompt cues:

**Quick Color Reference:**
- text: #000000
- background: #ffffff
- surface dark: #222222
- border: #e5e7eb
- secondary text: #313131
- primary action: no distinct CTA color

**Example Component Prompts:**

1. **Full-Bleed Dark Hero Section:** Full-viewport background of #222222 with a product photograph filling the frame. Left-aligned product name at 280px Unica77LLWeb weight 700, color #ffffff, positioned 8% from left, vertically centered. Right-aligned support text at 16px Unica77 weight 400 #ffffff, max-width 280px, positioned 30% from right, with a ghost outline button below (1px #ffffff border, 2px radius, 8px 24px padding, 14px weight 600 label, arrow icon prefix).

2. **Feature Card Grid (4-column):** White #ffffff background, 4 equal columns with 24px gaps. Each card: 32px line-art icon in #222222 at top-left, 18px Unica77 weight 600 heading in #000000 below with 12px gap, 14px Unica77 weight 400 description in #313131 below heading with 8px gap. No card background, no border, no shadow - pure typographic structure on white.

3. **Ghost Outline Button (light variant):** Transparent background, 1px solid border in #222222, 2px border-radius, 8px vertical 24px horizontal padding. Label in Unica77 weight 600 at 14px in #222222, followed by a 12px right-arrow icon ( ) in the same color. No hover fill - border darkens to #000000 on hover.

4. **Top Navigation Bar:** Fixed position, 64px height, background #222222. Flexbox with three zones: left (hamburger icon in #ffffff 20px), center (VANMOOF text in Unica77 weight 700 at 12px tracking +0.1em uppercase, #ffffff, inside a 9999px-radius pill with 1px #ffffff border and 6px 20px padding), right (shopping bag icon in #ffffff 20px). Bottom border: 1px solid #e5e7eb when scrolled.

5. **Editorial Content Section:** Background #ffffff, max-width 1200px centered, 64px vertical padding. Section heading centered in Unica77 weight 600 at 32px #000000, with 16px sub-description in #313131 below at 16px weight 400, 24px gap. Followed by 4-column feature grid with 32px row gap between heading block and grid.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
