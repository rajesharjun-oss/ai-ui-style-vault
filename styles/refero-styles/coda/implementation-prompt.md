# AI Implementation Prompt

Build a Coda-inspired interface using this source-derived style bundle.

Reference site: https://coda.io
Theme: light
Category: Productivity
North star: Cream-paper workspace - warm editor's desk where bold black type and a single orange accent do all the work.

Use these palette anchors:

- Ink Black `#212121` for Primary text, heading fills, primary borders, and the structural ink color across all UI surfaces
- Pure White `#ffffff` for Default page canvas, card surfaces, button text on dark fills, and outlined-button fills
- Carbon `#000000` for Filled primary action background, hard offset shadow color, and high-contrast icon fills
- Cream Paper `#fff6ec` for Warm hero band, footer surface, and the signature alternate canvas that gives Coda its editorial mood
- Ash Border `#e0e0e0` for Hairline borders, card edges, and subtle dividers separating surfaces from canvas
- Graphite `#666666` for Secondary body text, muted helper text, and low-emphasis metadata
- Smoke `#8e8e8e` for Tertiary text, placeholder text, disabled labels, and nav item resting state
- Slate Button `#444444` for Secondary button borders and mid-weight icon strokes
- Ember Orange `#ee5a29` for Sole chromatic accent - heading highlights, section eyebrow text, decorative underlines, and brand-mark punctuation. The single warm note against an otherwise black-and-cream system

Use these typography anchors:

- Calibre-R `--font-calibre-r` for Display and section headlines. Custom geometric 700-weight face with extremely tight tracking that compresses letterforms into dense blocks of ink. The heavy + tight combination is Coda's signature - headlines feel carved rather than written. Substitute: Manrope 800 or DM Sans 800 with -0.03em tracking.
- Inter `--font-inter` for All UI text: body copy, nav links, buttons, labels, captions. Inter carries the entire functional layer; its near-default weights and tracking let the Calibre headlines lead.
- Tiempos-Headline `--font-tiempos-headline` for Occasional editorial subheading in a light serif weight - the soft counterpoint to Calibre's blocky display. Used sparingly for emphasis rather than hierarchy.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 96px.
- Card padding: 24px.
- Element gap: 8px.

Build these component patterns where relevant:

- Top Navigation Bar: Primary site header
- Filled Primary Button: Main conversion action
- Outlined Button: Secondary action
- Ghost Link Button: Tertiary text action
- Hero Section: Above-the-fold brand statement
- Product Mockup Frame: Browser-chrome product screenshot container
- Hard Shadow Block: Editorial feature card with retro offset
- Status Badge: Inline status indicator in product tables
- Social Proof Logo Bar: Customer trust strip
- Section Eyebrow: Small label above a heading
- Document Card: Content tile in galleries and resource grids
- Footer: Site bottom anchor

Do:

- Use Calibre-R (or Manrope 800 substitute) at 52-72px with -0.035em to -0.045em tracking for all display headlines.
- Anchor the primary CTA on a solid #000000 fill with white Inter 600 text, 8px radius, and a 1.5px inset #212121 shadow.
- Open the page with a full-bleed #fff6ec hero band when the goal is brand introduction or top-of-funnel conversion.
- Show product through browser-chrome mockups that overlap section boundaries, anchored by the soft two-layer rgba(0,0,0,0.06) shadow stack.
- Reserve #ee5a29 for single-word emphasis, eyebrows, or small icon accents - never fills or large surfaces.
- Use 8px radius as the universal default for cards, buttons, and images; reach for 12px only on large CTAs.
- Let Inter at 400/600 carry every functional label; never let body weight climb above 700.

Avoid:

- Don't introduce a second chromatic accent - the system is monochrome plus a single ember orange.
- Don't use soft blurred drop-shadows on content cards; elevation is either the hard 8px/8px black offset or the two-layer rgba stack, nothing in between.
- Don't set body or subheading text in Calibre-R - it belongs only at 38px and above, 700 weight only.
- Don't apply rounded pill (9999px) radii to primary buttons; 8px is the system default.
- Don't place white cards directly on the cream band without a visible border or shadow - the value difference is too subtle.
- Don't use light grays (#8e8e8, #aeaeae) for primary text; reserve them for placeholder and disabled states only.
- Don't break the 4px spacing grid - all padding, gaps, and margins should snap to 4 / 8 / 12 / 16 / 20 / 24 / 32.

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
