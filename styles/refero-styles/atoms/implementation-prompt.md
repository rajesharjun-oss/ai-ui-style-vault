# AI Implementation Prompt

Build a Atoms-inspired interface using this source-derived style bundle.

Reference site: https://atoms.co
Theme: dark
Category: AI
North star: obsidian monolith in candlelight - a near-black canvas where a single warm champagne accent cuts like a blade through the darkness

Use these palette anchors:

- Champagne Gold `#c8ad86` for Accent headings, category tags, decorative borders - the only chromatic color in the system, used sparingly to mark emphasis and brand-bearing elements
- Candlelight Cream `#fff7dd` for Primary text, hairline borders, icon strokes - warm off-white reads softer than pure white against the black canvas
- Obsidian Black `#000000` for Page canvas, card surfaces, image backgrounds - absolute black dominates the visual field
- Ember Ash `#66635f` for Muted surface variation, secondary backgrounds, low-emphasis fills

Use these typography anchors:

- Switzer `--font-switzer` for Primary typeface for all headings, body, and navigation - a geometric sans with unusually tight tracking on display sizes (-0.042em at 44px) that creates a precision-engineered feel. Weight 400 for body, 500 for labels and tags. The negative letter-spacing on the 44px headline tightens the word shapes into compact, machined forms.
- system-ui sans-serif `--font-system-ui-sans-serif` for Fallback / system rendering for micro-UI and link text

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 32px.
- Element gap: 8-16px.

Build these component patterns where relevant:

- Hero Logo Mosaic: Full-bleed brand mark
- Hero Headline: Primary statement type
- Ghost Text Link: Navigation cue to secondary content
- Top Navigation Bar: Global site navigation
- Company Card: Portfolio/company grid item
- Category Tag Pill: Industry/sector label
- Company Logo Tile: Brand mark display within card
- Card Footer Link Row: External resource links
- Section Header: Content section title
- Arrow Glyph: Directional/link indicator

Do:

- Use #fff7dd for all primary text and hairline borders on black surfaces
- Reserve #c8ad86 exclusively for category tags, accent headings, and decorative borders - never as a full-surface fill
- Apply Switzer with tight negative letter-spacing on all display sizes: -1.85px at 44px, -0.13px at 16px
- Set border-radius to 4px on cards and buttons, 100px on tags and pills only
- Separate cards and sections with 1px hairline borders, never with shadows or background fills
- Keep vertical rhythm tight: 8-16px between related elements, 80px between major sections
- Render all icons and arrows in #fff7dd or #c8ad86 - never introduce additional colors

Avoid:

- Do not use shadows, glows, or blur effects for elevation - define surfaces with borders only
- Do not introduce saturated colors beyond the champagne accent - no blues, greens, or reds
- Do not use pure white (#ffffff) for text - #fff7dd is warmer and on-brand
- Do not add background fills to cards or sections - they sit directly on the black canvas
- Do not use large border-radius values on cards (no 12px, 16px, 24px) - stay at 4px max for rectangles
- Do not apply letter-spacing to body text - keep tracking tight only on 16px+ sizes
- Do not animate color, position, or scale on load - the system is static and placed, not kinetic

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
