# AI Implementation Prompt

Build a Flatfile-inspired interface using this source-derived style bundle.

Reference site: https://flatfile.com
Theme: light
Category: Dev Tools
North star: Quiet data journal on warm parchment

Use these palette anchors:

- Midnight Ink `#090b2b` for Primary brand color for headings, logo, emphasized text, nav labels, and icon strokes - a near-black with a faint violet cast that reads as ink rather than pure black against the cream canvas
- Obsidian `#151515` for Dark elevated surface for cards, headers, and contained panels. Do not promote it to the primary CTA color
- Graphite `#1b1b1e` for Primary body and heading text, dark card fills, and icon fills - the workhorse near-black with the faintest cool cast
- Charcoal `#262626` for Secondary dark surfaces and muted borders for inverted panels
- Steel `#808080` for Mid-gray for supporting UI marks, icon fills, and medium borders
- Silver `#aaaaaa` for Lighter mid-gray for tertiary text, placeholder copy, and decorative fills
- Fog `#d7d7d7` for Subtle border tone for ghost controls and quiet dividers
- Mist `#e5e7eb` for The system's structural hairline - dominant border, divider, and table-rule color across every layout context
- Parchment `#e5ebd3` for Warm sage-cream wash used as the hero background and as the secondary button fill - gives the page its printed-paper atmosphere
- Linen `#f8f8f8` for Card and elevated surface background - one step off the page to create depth without shadows
- Paper `#ffffff` for Pure white reserved for inverted buttons, tag chips, and high-contrast list items where Mist would be too muted
- Slate Link `#8c8c8c` for Default link and breadcrumb text color, distinct from body text gray

Use these typography anchors:

- FlatfileDiatypeVariable `--font-flatfilediatypevariable` for FlatfileDiatypeVariable - detected in extracted data but not described by AI
- Flatfile Diatype (Variable) `--font-flatfile-diatype-variable` for Primary UI and body sans - nav links, buttons, body copy, small labels, and card content. The variable axis lets the system shift between neutral body weight and slightly heavier button weight without changing family.
- Flatfile Diatype (Static) `--font-flatfile-diatype-static` for Display and section heading sizes. Uses tighter tracking as size grows - the 60px display sits at -0.0320em, pulling letters into a compact editorial block.
- Source Serif 4 `--font-source-serif-4` for Reserved exclusively for customer-quote hero text in testimonial cards. The serif italic-leaning humanist voice creates a print-publication contrast against the otherwise sans-only system.
- Sharp Grotesk `--font-sharp-grotesk` for Secondary display face for product-feature subheadings where a more condensed, technical voice is needed - used sparingly to break up the Diatype rhythm.
- Booton `--font-booton` for Booton - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 64-88px.
- Card padding: 24-32px.
- Element gap: 16px.

Build these component patterns where relevant:

- Primary CTA Pill (Book a demo): Main conversion action
- Secondary CTA Pill (Check out Obvious): Soft secondary action
- Ghost Nav Link: Top-bar navigation item
- Floating File Card: Hero product showcase card
- Sticky Top Nav Bar: Global navigation
- Testimonial Card: Customer quote block
- Carousel Arrow Button: Testimonial pagination
- Step Tab Bar (Extract / Prepare / Map / Build): Process-step indicator
- Gradient Hero Band: Full-bleed atmospheric divider
- Section Heading Block: Page-section opener
- Link List Item: Footer or nav text link
- File Extension Tag: Format indicator chip

Do:

- Use #151515 filled pills at 99px radius for all primary CTAs - never a rectangular button.
- Set every display heading at 60px in Flatfile Diatype weight 400 with -1.92px tracking; never go bolder than 500 for the display voice.
- Use #e5e7eb for all structural dividers and table rules; it is the system's connective tissue.
- Reserve Source Serif 4 exclusively for the customer-quote hero text inside testimonial cards.
- Layer the canvas as Parchment (#e5ebd3) Paper (#ffffff) Linen (#f8f8f8) for depth instead of adding shadows.
- Use 88px section padding above every new page section to preserve the editorial breathing room.
- Center the page content at max-width 1200px; never edge-to-edge inside content zones.

Avoid:

- Do not introduce a secondary chromatic brand color - Midnight Ink (#090b2b) is the only one.
- Do not use box-shadows to separate cards; shift the surface color one step instead.
- Do not set body text in anything other than Graphite (#1b1b1e) or #090b2b - no chromatic body copy.
- Do not use rectangular (non-pill) buttons; the 99px radius is a signature.
- Do not pair a chromatic icon color with chromatic background - keep the surface white and the icon the only color.
- Do not apply letter-spacing looser than -0.0050em - the system is built on tight, compact tracking at every size.
- Do not use the Parchment (#e5ebd3) wash outside the hero - it is a hero-only atmosphere, not a general surface.

Source prompt cues:

Quick Color Reference:
- text: #1b1b1e
- background: #e5ebd3 (hero) / #ffffff (body)
- border: #e5e7eb
- accent: #090b2b
- primary action: no distinct CTA color

3 Example Component Prompts:

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.


3. Build a testimonial card: Linen (#f8f8f8) background, 12px radius, 1px #e5e7eb border, 32px padding. Top row: author name + role in #1b1b1e 16px on the left, customer logos aligned right. Center: quote text in Source Serif 4 38px weight 400, #1b1b1e, letter-spacing -1.14px, set as italic. Bottom: two metric stats (e.g. '25%') in #1b1b1e 22px with caption labels in #aaaaaa 12px, plus 40px circular arrow buttons with #e5e7eb border on the far right.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
