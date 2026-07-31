# AI Implementation Prompt

Build a INVERSA-inspired interface using this source-derived style bundle.

Reference site: https://inversa.com
Theme: dark
Category: Other
North star: topographic field terminal at midnight. A dark command surface where massive editorial type and a single neon-lime marker layer over satellite earth photography, every label set in mono as if reading mission coordinates.

Use these palette anchors:

- Obsidian Loam `#13140e` for Page canvas, hero background, card surfaces - the near-black base with a faint olive cast that keeps the dark from feeling synthetic
- Bone Vellum `#f4f3e8` for Primary text, body copy, headings, icon strokes, border color on dark - warm off-white that reads as paper, not LCD white
- Iron Filings `#404040` for Hairline borders, footer dividers, low-emphasis rules
- Drift Ash `#84837b` for Muted secondary text, placeholder input state, low-contrast labels on light surfaces
- Lime Surveyor `#ebfc72` for Green supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Marsh Olive `#bacd31` for Gradient transition shade for the lime accent - deeper stop used in horizontal lime fades

Use these typography anchors:

- NB International Pro `--font-nb-international-pro` for Display and body - the brand's primary voice. Set at 72px for hero statements and 58px for section headers with -0.03em tracking, producing a compressed, editorial presence. Also carries body text at 18px (lh 1.62) and UI labels at 13-14px. Its humanist warmth prevents the dark canvas from feeling cold or corporate.
- JetBrains Mono `--font-jetbrains-mono` for Interface annotations, data labels, button text, tag values, and secondary display moments. The monospaced geometry reads as coordinates, timestamps, and telemetry - reinforcing the field-instrument metaphor. Set in weight 300 for hero-scale data callouts (65px) to keep mono from feeling mechanical at large sizes.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 86-104px.
- Card padding: 14-18px.
- Element gap: 18px.

Build these component patterns where relevant:

- Hero Headline: Primary page-level statement, 58-72px
- Lime Action Button: Primary call-to-action, high-emphasis interactive
- Ghost Text Button: Secondary action, low-emphasis interactive
- Data Tag: Coordinate, label, or classification marker
- Top Navigation Bar: Site-wide header
- Full-Bleed Image Band: Atmospheric section separator or context image
- Text Block (Dark Surface): Contained editorial content on canvas
- Footer: Site footer
- Input Field: Text input

Do:

- Set hero headlines at 58-72px NB International Pro weight 400 with line-height 0.90 and letter-spacing -0.03em - the tight leading stacks lines into a single mass.
- Use #ebfc72 as the sole chromatic accent for any element that needs to be noticed: buttons, active states, data tags, and icon highlights.
- Apply -0.03em letter-spacing to all NB International Pro text regardless of size - the tracking is part of the brand voice, not a display-only treatment.
- Let imagery bleed to all four edges at 100vw with zero radius, zero border, and zero overlay - the photo is the surface.
- Set all UI labels, button text, and metadata in JetBrains Mono - the mono voice distinguishes interface from editorial copy.
- Use 3.6px border-radius consistently for buttons, tags, and inputs - do not introduce larger radii for 'softness'.
- Space sections at 86-104px and separate them with whitespace, not dividers or background color shifts.

Avoid:

- Do not add box-shadows to any element - the system is deliberately flat; depth comes from color contrast, not elevation.
- Do not introduce a second accent color - the lime is alone by design. Any other chromatic addition dilutes the survey-marker effect.
- Do not set body text below 18px in NB International Pro - the font's humanist proportions require generous size to read correctly.
- Do not use #000000 as the canvas - the olive undertone of #13140 is what makes the dark feel organic rather than digital.
- Do not round corners beyond 3.6px on any component - larger radii would contradict the instrument-panel aesthetic.
- Do not use colored backgrounds for cards or content blocks - content sits directly on the dark canvas with no chrome.
- Do not center body text - editorial alignment is left-aligned throughout, matching the mission-log reading flow.

Source prompt cues:

**Quick Color Reference**
- background: #13140e
- text: #f4f3e8
- border: #404040
- accent: #ebfc72
- muted text: #84837b
- primary action: no distinct CTA color

**Example Component Prompts**

1. Build a hero section: full-bleed background (any photo or solid #13140e), max-width 1200px content container, headline NB International Pro 72px weight 400 color #f4f3e8 line-height 0.90 letter-spacing -2.16px left-aligned at bottom-left. Include a lime-filled action button (#ebfc72 bg, #13140e text, JetBrains Mono 14px, 3.6px radius, 14px 18px padding).

2. Create a data tag: #ebfc72 background, #13140e text, JetBrains Mono 13px weight 400, padding 5px 7px, 3.6px radius, uppercase content.

3. Build a content section on dark canvas: #13140e background, no card chrome, heading in NB International Pro 58px #f4f3e8, body in NB International Pro 18px #f4f3e8 line-height 1.62, section gap 86-104px above and below.

4. Create a top navigation bar: transparent background, brand 'INVERSA' left in NB International Pro 14px #f4f3e8, 'Menu' label right in JetBrains Mono 13px #f4f3e8 with a 4px #f4f3e8 dot indicator beside it.

5. Build a footer: full-width #13140e band with 1px #404040 top border, 2-3 column link grid in JetBrains Mono 13px #f4f3e8, 86px top padding.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
