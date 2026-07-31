# AI Implementation Prompt

Build a Stryds-inspired interface using this source-derived style bundle.

Reference site: https://stryds.com
Theme: dark
Category: Other
North star: Aurora ringed midnight void

Use these palette anchors:

- Electric Lime `#a6ff00` for Green action color for filled buttons, selected navigation states, and focused conversion moments.
- Deep Violet `#040126` for Outlined action borders, subtle decorative borders - a near-black indigo that adds tonal depth to dark borders without breaking the monochrome canvas
- Obsidian `#101010` for Page canvas, outermost background, shadow tokens - the base void that every surface floats on
- Carbon `#171717` for Card surfaces, elevated content panels - the only step above Obsidian in the surface stack
- Slate `#333333` for Hairline borders, card borders, subtle dividers - the structural border color, used more than any other in the system
- Steel `#3d3d3d` for Strokes, secondary card borders - a half-step lighter than Slate for layering borders on borders
- Fog `#6f6f6f` for Dark borders and separators for elevated surfaces and inverted UI.
- Paper `#fdfdfd` for Primary text, heading borders, illustration highlights - the only text color that reads as active
- Void `#000000` for SVG fills, spectrum ring backing - pure black for graphic elements where absolute darkness is needed

Use these typography anchors:

- SF Pro Display `--font-sf-pro-display` for Display and heading typography - the choice of SF Pro Display signals a premium, iOS-adjacent system voice. Weights 500-600 (never 700+) keep headings from feeling heavy; the brand's authority comes from size, not weight. Display sizes escalate to 184px, creating poster-scale type that dominates every section. Line-height tightens to 0.95 at the largest sizes, making individual letters feel monumental and architectural.
- Arial `--font-arial` for Body, links, card text, button labels - deliberately a system fallback so it stays invisible. While SF Pro Display headlines shout at 184px, Arial whispers at 14px in the background. This split (premium display + neutral body) is a deliberate hierarchy choice: the display type does all the emotional work, the body text just delivers information.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: 80px.
- Card padding: 80px.
- Element gap: 16px.

Build these component patterns where relevant:

- Spectrum Ring Frame: Signature visual frame - the defining element of the brand
- Display Wordmark: Brand name display in hero contexts
- Manifesto Statement: Large editorial statement block
- Primary CTA Button (Filled): Main action button
- Secondary Outlined Button: Secondary action or navigation
- Floating Join Bar: Persistent bottom CTA
- Feature Card: Content block for features, stats, or sections
- User Avatar Badge: Profile indicator floating from the spectrum ring
- Brand Subtitle: Tagline or descriptor below display wordmark
- Hairline Divider: Section separator

Do:

- Use the spectrum ring as the primary visual frame for hero sections and large display statements - it is the brand's signature gesture
- Set display type between 78-184px in SF Pro Display weight 500-600; this is a poster-scale brand, not a SaaS dashboard
- Use #a6ff00 Electric Lime exclusively for CTA fills, active states, and accent dots - it is the only chromatic color and must stay rare
- Set all buttons to 100px border-radius (pill shape) and all cards to 40px border-radius - the system has no sharp corners or small radii
- Keep the canvas at #101010 Obsidian and cards at #171717 Carbon; use 1px #333333 borders, not shadows, to separate surfaces
- Pair display headlines with #fdfdfd active words and #6f6f6f Fog muted words to create emphasis without introducing color
- Maintain 80px section gaps and 80px card padding - the design breathes heavily; dense layouts break the editorial feel

Avoid:

- Do not use box-shadows for elevation - Stryds is flat against the void, separated by borders not depth
- Do not introduce additional accent colors beyond Electric Lime; the monochrome discipline is what makes the lime feel urgent
- Do not set body text below 14px or use font-weight below 400; the brand speaks with confidence, not subtlety
- Do not use sharp corners or radii under 16px; every element is either pill-shaped (100px) or softly rounded (40px)
- Do not center content in narrow columns or constrain to a max-width under 1000px; let display type and the ring fill the viewport
- Do not use color to establish text hierarchy - use size, weight, and the #fdfdfd/#6f6f6f contrast pair instead
- Do not add gradients to UI components, buttons, or cards; gradients are reserved exclusively for the spectrum ring system

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
