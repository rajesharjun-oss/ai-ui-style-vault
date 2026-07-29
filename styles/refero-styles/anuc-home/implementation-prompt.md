# AI Implementation Prompt

Build a Anuc Home-inspired interface using this source-derived style bundle.

Reference site: https://www.anuchome.com
Theme: light
Category: Agency
North star: editorial gallery in warm white - a quiet, magazine-like space where oversized serif headlines and monumental rounded geometric letterforms frame intimate interior photography

Use these palette anchors:

- Ink `#1a1a1e` for Primary text, all borders, logo forms, icon strokes - the structural near-black that defines every contour across the system
- Canvas `#f3f3f2` for Page background - warm off-white that gives the entire system its gallery-wall warmth rather than clinical white
- Paper `#ffffff` for Card surfaces, article blocks, elevated panels - pure white sits on top of Canvas to create subtle layering without shadows
- Ash `#d1d1d2` for Hairline borders, divider lines, subtle structural rules - the thinnest visible grid
- Stone `#c1c2bd` for Secondary borders, muted fills, icon strokes at lower emphasis
- Linen `#e7e6e4` for Muted surface for category tags, soft chips, low-emphasis backgrounds - warm-tinted neutral that steps between Paper and Canvas
- Graphite `#4d4942` for Muted body text, secondary copy - warm dark gray for hierarchy below Ink
- Mist `#8d8d8f` for Tertiary text, timestamps, metadata - the lightest readable gray
- Bronze `#9a682c` for Sparingly used warm accent - appears as small punctuation dots or category indicators, never as fills; adds a whisper of warmth to the achromatic system
- Slate `#4a626f` for Secondary accent - cool counterpoint to Bronze, used in equally restrained dot/tag contexts to create subtle color rhythm

Use these typography anchors:

- Instrument Sans `--font-instrument-sans` for All UI, navigation, body copy, button labels, and small headlines. Weight 500 carries nav and button emphasis; weight 400 is the default reading voice. Free substitute: Inter, DM Sans.
- Instrument Serif `--font-instrument-serif` for All display and editorial headlines - the 52px and 74px sizes carry the brand's magazine-portfolio voice. The contrast between this high-contrast serif and the neutral sans is the system's signature typographic gesture. Free substitute: Playfair Display, Cormorant Garamond.

Use these layout rules:

- Base spacing: 8px.
- Density: compact.
- Page max-width: 1440px.
- Section gap: 96px.
- Card padding: 24px.
- Element gap: 8px.

Build these component patterns where relevant:

- ANUC Wordmark: Primary brand identity - monumental geometric letterforms
- Top Navigation: Minimal site navigation
- Hero Image Grid: Full-viewport visual statement for the landing
- Editorial Section Heading: Large display text for section openers
- Article Card: Content preview block in articles section
- Category Tag: Small label chip for content categorization
- CTA Button - Outlined Ghost: Primary action button (e.g., 'AGENDAR CONSULTA')
- Two-Column Editorial Section: Content layout pattern for text+image or label+content
- Hairline Divider: Structural separation between sections and grid cells
- Section Label: Small uppercase section identifier (e.g., 'SERVICIOS', 'ARTICULOS')

Do:

- Use Instrument Serif 400 at 52-74px for all display headlines - the high-contrast serif at oversized scale is the brand's signature typographic moment
- Set all radii to 0px for buttons, cards, and tags - the system is architectural, not soft; sharpness communicates precision
- Maintain the warm off-white Canvas (#f3f3f2) as the dominant background; never use pure clinical white for full-page backgrounds
- Use Ink (#1a1a1e) for all text and borders; let color do no work - the system is deliberately achromatic
- Separate image grid cells with 1-2px hairline borders in Ink to create the gallery-grid structure
- Precede every display headline with a small uppercase Instrument Sans 500 label (15px) to create the editorial section-opening rhythm
- Apply 96px minimum vertical spacing between major sections to maintain the gallery-walk pacing

Avoid:

- Do not introduce shadows, glows, or blur effects - the system communicates elevation through background color steps (Canvas Paper Linen), never through box-shadow
- Do not use border-radius greater than 0px on any UI element - rounded buttons or cards would break the architectural language; the only rounded forms are the monumental logo shapes
- Do not add chromatic fills to buttons, backgrounds, or large UI surfaces - Bronze and Slate are reserved for dot punctuation only
- Do not use Instrument Sans for display headlines - the serif/sans contrast is the system's signature; flattening both to sans destroys the editorial voice
- Do not place body copy at sizes below 15px - the system is generous with reading size, not compact
- Do not stack dense information without the 96px section gap - the gallery-walk rhythm requires breathing room between content blocks
- Do not use decorative gradients, textures, or background imagery behind text - every text surface must sit on a flat, untextured neutral

Source prompt cues:

QUICK COLOR REFERENCE:
- text: #1a1a1e
- background: #f3f3f2
- surface/card: #ffffff
- border: #d1d1d2
- accent dot: #9a682c
- primary action: no distinct CTA color

EXAMPLE COMPONENT PROMPTS:

1. Create an editorial section opener: Canvas (#f3f3f2) background, full-width with max-width 1200px centered. Small uppercase label 'SERVICIOS' in Instrument Sans 500, 15px, #1a1a1e, positioned top-left. Display headline below in Instrument Serif 400, 52px, #1a1a1e, line-height 1.05, left-aligned.

2. Create an article card: #ffffff background, 0px radius, 24px padding, no border, no shadow. Date '16.07.2025' in Instrument Sans 400, 15px, #8d8d8f at top. Title in Instrument Serif 400, 32px, #1a1a1e below. Category tag at bottom: small dot (-) in #9a682c followed by uppercase Instrument Sans 500, 15px, #1a1a1e text 'DISENO OFICINAS'.

3. Create a ghost action button: transparent background, 1px solid #1a1a1e border, 0px radius, 12px 24px padding. Label 'AGENDAR CONSULTA' in Instrument Sans 500, 15px, uppercase, #1a1a1e, letter-spacing 0.5px, followed by a small right-arrow icon ( ) in #1a1a1e.

4. Create a hero image grid: 4-5 equal columns, full viewport width, each cell containing an interior photograph. Cells separated by 1px solid #1a1a1e borders. No captions, no overlays, images fill cells edge-to-edge with 0px radius.

5. Create a section divider: a single 1px solid #d1d1d2 horizontal line spanning the full content width, with 96px vertical space above and below it.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
