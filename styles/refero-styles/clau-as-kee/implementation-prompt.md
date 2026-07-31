# AI Implementation Prompt

Build a clau.as.kee-inspired interface using this source-derived style bundle.

Reference site: https://clauaskee.com
Theme: light
Category: Agency
North star: lavender poster wall, monumental type. A flat periwinkle field with a single black-letter sculpture filling the viewport and a thin line of small nav text floating above it.

Use these palette anchors:

- Periwinkle Field `#8e93ff` for Page canvas, hero background, full-bleed section fills - the single defining brand color, a mid-saturation lavender that swallows the viewport and against which all type is set in black ink
- Carbon Ink `#1a1a1a` for Primary text, display type, hairline borders, dark panels, nav links - near-black rather than pure black, keeps the lavender from vibrating too hard
- Paper White `#ffffff` for Hairline borders, dividers, input outlines, and card edges on light surfaces.
- Signal Green `#47f654` for Green action color for filled buttons, selected navigation states, and focused conversion moments.

Use these typography anchors:

- Beastly clauworks `--font-beastly-clauworks` for Display / wordmark - the proprietary display face, used only at monumental scale (288-504px) for the brand wordmark and hero sculpture. Chunky, almost stencil-cut geometric forms that read as a graphic object rather than readable text. Single weight, no italic. Substitute: a heavy display grotesque like Druk Wide or a custom commission. Do not use at small sizes - this face is architecture, not communication.
- Suisse Intl clauworks `--font-suisse-intl-clauworks` for Headlines, subheads, and long-form body - a custom-cut Suisse International (Swiss grotesque) in a single weight. Used at three distinct scales: 20px for body and nav, 30px for section subheads, 144px for editorial display headings like 'Art direction - Dig...'. The absence of bold/medium weights is the signature: everything is the same quiet weight, hierarchy comes from size alone. Substitute: Suisse Int'l, Inter, or Neue Haas Grotesk.
- Times `--font-times` for Smallest body fallback / metadata - appears as system Times at 16px, likely the serif default for tiny labels and captions. Single weight, system face. Substitute: any system serif.

Use these layout rules:

- Base spacing: .
- Density: spacious.
- Page max-width: .
- Section gap: 130px.
- Card padding: 65px.
- Element gap: 30px.

Build these component patterns where relevant:

- Display Wordmark: Hero brand mark and section-opening sculpture
- Editorial Display Headline: Large in-flow headings on the periwinkle canvas
- Top Navigation: Minimal horizontal nav across the top edge
- Request Badge: Sole chromatic interactive element on the page
- Carbon Panel: Dark inverted section for portfolio content
- Portfolio Spread: Image-and-text content block inside a Carbon Panel
- Image Carousel: Horizontal scroller for project imagery
- Hairline Divider: Section separator
- Body Copy: Long-form paragraph text
- Subheading: Section label and small editorial title

Do:

- Set every page background to Periwinkle Field (#8e93ff) - this is the operating mode of the system
- Use Beastly clauworks at 288px or larger for any display-level headline; do not use it below 200px
- Reach for Suisse Intl clauworks at 20px, 30px, or 144px only - do not interpolate intermediate sizes
- Separate dark content from the lavender canvas with a full-bleed Carbon Ink (#1a1a1a) panel, not a shadow or border
- Let display type run past the viewport edge - cropping is the layout, not a bug
- Place at most one Signal Green (#47f654) badge per page; it is punctuation, not decoration
- Use 130px vertical breathing room between major sections; 30px between typographic elements within a section

Avoid:

- Do not add a fifth color, a tinted neutral, or a soft shadow to soften the lavender - the flatness is the design
- Do not use rounded corners on panels, cards, or images; 0px radius everywhere except the green badge
- Do not introduce a bold or medium weight of Suisse Intl - hierarchy is size-driven only
- Do not use Beastly at small sizes (under 200px) - it loses its character and becomes a bad display grotesque
- Do not center body copy or set it in narrow columns; body text is left-aligned, full-width-feeling, generous
- Do not add a sticky header, breadcrumb, or secondary navigation; the three-link top bar is the entire nav system
- Do not use gradients, blur, glow, or any CSS filter on the lavender background - it must read as a flat printed field

Source prompt cues:

**Quick Color Reference**
- canvas: #8e93ff (Periwinkle Field)
- text: #1a1a1a (Carbon Ink)
- surface: #ffffff (Paper White)
- border: #1a1a1a (Carbon Ink hairline)
- accent: #47f654 (Signal Green)
- primary action: no distinct CTA color

**Example Component Prompts**
1. Build a hero section: full-viewport Periwinkle Field (#8e93ff) background, Beastly clauworks at 504px line-height 1.00 in Carbon Ink (#1a1a1a), single line of display type filling the viewport width, characters may bleed off edges.
2. Build a portfolio dark band: full-bleed Carbon Ink (#1a1a1a) panel, 130px top/bottom padding. Inside, a Paper White (#ffffff) image plate at 0px radius on the left (60% width), and body copy in Suisse Intl clauworks 20px weight 400 line-height 1.50 Carbon Ink on the right.
3. Build an editorial display headline: Periwinkle Field background, Suisse Intl clauworks at 144px weight 400 line-height 1.15 in Carbon Ink, single sentence that may run past the viewport. Below it, a 1px Carbon Ink hairline divider spanning full width.
4. Build a Signal Green request badge: circular shape at 75px radius, Signal Green (#47f654) fill, Carbon Ink text in Suisse Intl clauworks 20px reading 'ON REQUEST', positioned as a floating overlay bottom-left of a portfolio block.
5. Build the top navigation: full-width row, three text links ('About' left, 'Contact' center, 'Playground' right) in Suisse Intl clauworks 20px weight 400 Carbon Ink, no background, no border, 20px top padding.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
