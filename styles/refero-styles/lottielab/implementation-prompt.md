# AI Implementation Prompt

Build a Lottielab-inspired interface using this source-derived style bundle.

Reference site: https://www.lottielab.com
Theme: light
Category: Design
North star: Animation studio on bright paper

Use these palette anchors:

- Electric Violet `#7270ff` for Primary CTA buttons, active nav items, accent keywords in headlines, focus rings - the only chromatic element allowed to break the monochrome canvas, making every action feel switched on
- Signal Blue `#1560fb` for Secondary accent for interactive highlights, selected states in tool surfaces, and inline brand emphasis where a cooler note is needed
- Deep Indigo `#2f2b4a` for Primary text and headings - a near-black with a violet undertone that warms the monochrome palette and distinguishes the brand from flat-charcoal SaaS defaults
- Midnight Ink `#1c1a2c` for Heaviest text weight, section titles, and surface-dark contexts - a deeper step than Deep Indigo for maximum contrast moments
- Slate `#4b5563` for Secondary body text, descriptions, metadata - sits between Deep Indigo and Silver for layered reading hierarchy
- Silver `#9ca3af` for Muted helper text, placeholder copy, disabled labels, and icon secondary tones
- Fog `#d9dbda` for Icon strokes at rest, subtle surface borders, low-emphasis dividers
- Mist `#e5e7eb` for Primary hairline borders across cards, inputs, dividers, and component edges - the dominant structural neutral
- Paper `#ffffff` for Card surfaces, elevated panels, button text on violet fills, inverted icon strokes
- Bone `#f9fafb` for Alternate surface for nested panels, input fills, quiet sections within white pages
- Pebble `#f3f4f6` for Page canvas, section bands between white blocks, product mockup backgrounds, footer wash
- Sunset Gradient `#facc15` for Decorative gradient endpoint for marketing visuals and showcase cards
- Bloom Gradient `#ec4899` for Decorative gradient endpoint for showcase cards and hero illustration accents

Use these typography anchors:

- Plus Jakarta Sans `--font-plus-jakarta-sans` for Sole typeface across the product. Geometric humanist sans with subtly squared terminals - contemporary but not cold. Weight 700 carries display and headings for confident vertical presence; weight 500 serves UI controls and labels; weight 400 handles body and descriptions. The slight openness in counters at small sizes keeps labels legible on dense tool surfaces.
- Google Sans Code `--font-google-sans-code` for Google Sans Code - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 24px.

Build these component patterns where relevant:

- Primary CTA Button: Single decisive conversion action on every page
- Outlined Nav Button: Secondary action in the header
- Ghost Text Link: Inline navigation and tertiary actions
- Product Mockup Frame: Browser-style container around the editor preview
- Animation Preview Card: Showcase tile in the product gallery
- Timeline Track Row: Animation keyframe row inside the editor
- Trust Logo Strip: Social proof bar below the hero
- Section Heading Block: Centered text intro before content sections
- Input Field: Text entry in forms and editor
- Nav Bar: Top-level site navigation
- Brand Logo Mark: Lottielab identity
- Gradient Showcase Card: Decorative card in feature sections

Do:

- Use #7270ff as the only chromatic fill on the page - every other surface stays in the neutral scale from #f3f4f6 to #2f2b4a.
- Set display text at 60px and headings at 48px with letter-spacing -1.5px and -1.2px respectively to match the contemporary tight-tracking rhythm.
- Apply 8px radius to all cards and panels, 12px to buttons, 9999px to tags and icon containers - the three-tier system is non-negotiable.
- Use Mist (#e5e7eb) 1px borders instead of shadows to separate layers; elevation comes from background stepping, not blur.
- Highlight one keyword per headline in Electric Violet (#7270ff) - the rest of the sentence stays Deep Indigo to create a single beat of color.
- Pair Plus Jakarta Sans weight 700 with 1.00-1.11 line-height for headlines; reserve weight 500 for UI labels and weight 400 for body copy.
- Alternate between #ffffff and #f3f4f6 section bands to create rhythm without using color or shadows.

Avoid:

- Don't introduce additional brand hues - the palette is intentionally violet-only; resist adding teals, greens, or pinks to core UI.
- Don't use shadows, glows, or blur effects for elevation; rely on surface color stepping and 1px hairline borders instead.
- Don't set body text below 14px or use weights under 400 - the type system is calibrated for comfortable reading at 16px+.
- Don't apply gradient fills to buttons, inputs, or navigation - gradients are reserved for showcase and marketing visuals only.
- Don't use pure #000000 for text on light backgrounds; use Deep Indigo (#2f2b4a) to preserve the warm violet undertone of the brand.
- Don't break the 8px spacing grid - all padding, gaps, and margins should land on multiples of 8 (with 4px and 2px allowed only for micro-adjustments inside components).
- Don't stack multiple violet elements on a single screen - one chromatic moment per viewport keeps the accent meaningful.

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
