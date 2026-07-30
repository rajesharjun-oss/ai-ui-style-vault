# AI Implementation Prompt

Build a Flutterwave Design-inspired interface using this source-derived style bundle.

Reference site: https://www.flutterwave.design
Theme: light
Category: Design
North star: warm editorial magazine on cream paper

Use these palette anchors:

- Cream Paper `#fff9f1` for Primary page canvas, card surfaces, nav background - the warm ground tone every screen sits on
- Ink Black `#171717` for Primary text, body copy, icon strokes, hairline borders - the dominant ink across the system
- Steel Gray `#b5b5b5` for Muted card backgrounds, disabled surfaces, secondary fills
- Graphite `#8b8b8b` for Tertiary surface, subtle background blocks, inactive dividers
- True Black `#000000` for Hard borders on icons, nav emphasis, button outlines where maximum contrast is needed
- Midnight Indigo `#12122c` for Display headings, link text, heading borders - deep violet-black replacing pure black for warmth and brand character
- Golden Amber `#f5a623` for Primary action fill, logo heart mark, highlighter accents - the single warm punctuation color in an otherwise cool monochrome system
- Peach Blush `#fcd2ba` for Accent section band backgrounds (Vibes, features) - warm wash that breaks cream monotony without introducing a new hue

Use these typography anchors:

- Millik `--font-millik` for Display and heading font - used only for the hero headline and section titles. Heavy weight (700-800) with -0.025em tracking at 60px creates a poster-like authority. Custom serif-adjacent display cut gives the site its editorial magazine voice; substitute with Recoleta or Tiempos Headline if Millik is unavailable.
- Moderat `--font-moderat` for Primary UI and body font - covers everything from 12px captions to 22px subheads. Geometrical sans with uniformly tight -0.036em tracking that keeps even small text compact and editorial. 400 for body, 500 for nav/links, 600 for labels, 700 for emphasis. Substitute with Inter or General Sans for closest match.
- Flutterwave `--font-flutterwave` for Reserved for the Flutterwave wordmark and icon glyphs - not a general-purpose text face. Limited to brand marks and the small heart logo.

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1200px.
- Section gap: 60px.
- Card padding: 20px.
- Element gap: 10px.

Build these component patterns where relevant:

- Top Navigation Bar: Site-wide header
- Display Hero Headline: Primary page-level headline
- Hero Body Text: Intro paragraph below hero headline
- Story Carousel Card: Horizontal scrolling story preview
- Story Grid Card: 3-column editorial story card
- Category Tag: Small uppercase label above story titles
- Author Byline: Credit line below story title
- Section Header: Section title with optional action link
- Peach Section Band: Full-bleed warm content section
- Theme Toggle: Light/dark mode switcher in nav
- Golden Amber CTA Button: Primary action button
- Ghost Link Button: Secondary text-based action

Do:

- Use #fff9f1 (Cream Paper) as the default canvas for every page - never switch to pure white.
- Set display headlines in Millik 60px weight 700 with -1.5px letter-spacing and Midnight Indigo (#12122c) color.
- Apply 5px border-radius to all cards, buttons, inputs, and tags - consistency is the point.
- Reserve Golden Amber (#f5a623) for the primary CTA fill and the heart logo only - it is accent punctuation, not a surface color.
- Use the Peach Blush (#fcd2ba) band to separate major content sections from the cream default.
- Set all text to Ink Black (#171717) for body and Midnight Indigo (#12122c) for headings - do not mix pure black into the heading hierarchy.
- Keep all tracking negative - Moderat at -0.036em, Millik at -0.025em - to preserve the compact editorial density.

Avoid:

- Do not introduce drop shadows, glows, or blurs to cards or buttons - elevation comes from color contrast alone.
- Do not use Golden Amber for backgrounds, panels, or large fills - it loses its punch as a accent if it covers more than button-sized areas.
- Do not use pure white (#ffffff) as a surface - cream (#fff9f1) is the canvas, white breaks the warm system.
- Do not set headings in pure black (#000000) - Midnight Indigo (#12122c) is the heading color, it carries the brand character.
- Do not use border-radius values other than 5px - no pills, no 0px sharp corners, no 8-12px rounded cards.
- Do not add gradients, patterns, or decorative backgrounds to UI chrome - illustrations on cards are where visual interest lives.
- Do not set body text above 20px in Moderat - for larger sizes, switch to Millik to maintain the type hierarchy.

Source prompt cues:

**Quick Color Reference**
- text: #171717 (Ink Black)
- heading: #12122c (Midnight Indigo)
- background: #fff9f1 (Cream Paper)
- border: #171717 (Ink Black hairline)
- accent: #f5a623 (Golden Amber - CTA fill, logo)
- section band: #fcd2ba (Peach Blush)
- primary action: #f5a623 (filled action)

**Example Component Prompts**

1. *Create a hero headline block:* Cream Paper background (#fff9f1). Centered Millik 60px weight 700, color Midnight Indigo (#12122c), letter-spacing -1.5px, line-height 1.2. Below it, a body paragraph in Moderat 18px weight 400, Ink Black (#171717), max-width 600px, centered. 80px top padding, 60px bottom padding.

2. *Create a story grid card:* 5px border-radius, no border, no shadow. Full-bleed illustration fills the top half. Below: 20px padding containing a category tag (Moderat 12px weight 600, uppercase, Ink Black), then a title (Moderat 20px weight 600, Ink Black, 2 lines), then a date meta line (Moderat 12px weight 400, uppercase, #8b8b8b). Card sits directly on cream canvas.

3. *Create the top navigation:* Full-width bar on #fff9f1 with a 1px #171717 bottom border. Left: heart icon (#f5a623 fill, 16px) + 'Design' wordmark (Moderat 16px weight 500, Ink Black). Center: nav links (Moderat 14px weight 400, Ink Black) with 30px horizontal gap. Right: theme toggle (two 16px circles, one filled #171717, one outlined 1px #171717). 20px vertical padding.

4. Create a Primary Action Button: #f5a623 background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

5. *Create a Peach Blush section band:* Full-width background #fcd2ba, 60px vertical padding, centered content. Heading in Millik 32px weight 700, Midnight Indigo. Body in Moderat 16px weight 400, Ink Black, max-width 700px.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
