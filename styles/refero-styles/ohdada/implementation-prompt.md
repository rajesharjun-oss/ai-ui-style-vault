# AI Implementation Prompt

Build a OhDada-inspired interface using this source-derived style bundle.

Reference site: https://ohdada.de
Theme: light
Category: E-commerce
North star: Editorial gallery wall

Use these palette anchors:

- Chalk Cream `#e6e0d9` for Primary page canvas and secondary section background; the warm off-white that makes brown type and sculpture photography feel curated rather than clinical
- Lavender Stone `#b7b3be` for Alternate section background and hero canvas; introduces a cool, chalky counterpoint to the warm cream without breaking the achromatic discipline
- Saddle Brown `#5d3a19` for All headings, body copy, link text, and hairline borders - the only chromatic voice in the system, used as a drawn-with-ink accent against the pale neutrals; Outlined and ghost interactive borders; links and navigation controls carry a 1px brown stroke rather than a filled background, keeping the surface quiet
- Ink Black `#000000` for Decorative SVG fills only; never used for UI text or surface elements

Use these typography anchors:

- GrandSlang-Roman `--font-grandslang-roman` for Brand mark and large display headings only - used at 58px+ for the wordmark and section titles. Weight 100 is the entire signature: hairline serif strokes that read as drawn rather than typeset. Substitute: Cormorant Garamond Ultralight or Italiana, which approximate the extreme thinness and high-contrast serif construction.
- Neue Haas Grotesk Display `--font-neue-haas-grotesk-display` for All body copy, navigation, secondary headings, and product labels. Weights 400 for body, 500 for emphasis. The neo-grotesque geometry acts as a neutral ground for the expressive display serif - a deliberate Swiss-type baseline that lets GrandSlang perform. Substitute: Inter, Neue Haas Unica, or Helvetica Neue.

Use these layout rules:

- Base spacing: 6px.
- Density: compact.
- Page max-width: .
- Section gap: 115px.
- Card padding: 40px.
- Element gap: 10px.

Build these component patterns where relevant:

- Hero Wordmark: Brand identity display
- Hero Subtitle: Tagline beneath wordmark
- Section Title (Display): Major section heading
- Product Card - Editorial: Product entry in catalog
- Outlined Link: Navigation and inline links
- Section Divider: Implicit section break
- Product Photography Frame: Sculpture product imagery
- Navigation Bar: Top-level site navigation

Do:

- Use only GrandSlang-Roman weight 100 for the wordmark and display headings - never set it bold or above 72px
- Alternate Chalk Cream (#e6e0d9) and Lavender Stone (#b7b3be) as full-bleed section backgrounds to create rhythm without introducing new colors
- Apply 115px top/bottom padding to all major sections to maintain gallery-wall breathing room
- Set all body and navigation text in Neue Haas Grotesk weight 400-500, Saddle Brown (#5d3a19), 16-17px
- Mark links and interactive elements with a 1px Saddle Brown bottom border rather than a filled background
- Use 0px border-radius on all components - cards, buttons, images, and product frames are sharp-edged
- Let product photography be the only source of additional color (blues, whites from the sculptures); the UI itself stays three-tone

Avoid:

- Do not introduce gradients, drop shadows, or elevation effects - the system is flat by design
- Do not use rounded corners on any element; 0px radius is structural to the editorial feel
- Do not add a fourth color to the palette - Saddle Brown, Chalk Cream, and Lavender Stone are the complete chromatic vocabulary
- Do not set GrandSlang-Roman below 58px or in any weight other than 100; it loses its character at small sizes
- Do not use filled button backgrounds for primary actions; use the outlined-link treatment with a brown border instead
- Do not center body text - the layout is left-aligned throughout, even in the hero
- Do not add hover animations, color transitions, or motion; the interface reads as a printed catalog

Source prompt cues:

Quick Color Reference:
- text: #5d3a19 (Saddle Brown)
- background: #e6e0d9 (Chalk Cream)
- border: #5d3a19 (Saddle Brown, 1px hairline)
- accent surface: #b7b3be (Lavender Stone)
- primary action: #5d3a19 (outlined action border)

Example Component Prompts:

1. Create a hero wordmark block: full-bleed Lavender Stone (#b7b3be) background, 115px top padding. Headline 'Oh DaDa' set in GrandSlang-Roman weight 100, 72px, color #5d3a19, line-height 1.0, left-aligned with ~10% left margin. Below at 40px gap, a three-line subtitle in Neue Haas Grotesk weight 400, 16px, color #e6e0d9, line-height 1.18.

2. Create a section title: Chalk Cream (#e6e0d9) background. Heading 'Products' in Neue Haas Grotesk weight 500, 58px, color #5d3a19, line-height 1.0, 115px top padding, left-aligned.

3. Create a product card: Chalk Cream (#e6e0d9) background, two-column split. Right column (65% width) is an edge-to-edge product photograph with 0px radius. Left column (35% width) contains the product name 'Kaskasi' set in Neue Haas Grotesk italic weight 400, 17px, color #5d3a19, aligned to the bottom of the column.

4. Create an outlined navigation link: Neue Haas Grotesk weight 400, 16px, color #5d3a19, 1px solid #5d3a19 bottom border, 10px right margin, no background fill, no padding.

5. Create a section transition: switch from Chalk Cream (#e6e0d9) to Lavender Stone (#b7b3be) as the background, 115px vertical padding, no visible border or shadow between sections.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
