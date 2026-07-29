# AI Implementation Prompt

Build a Getburnt-inspired interface using this source-derived style bundle.

Reference site: https://www.getburnt.ai
Theme: light
Category: AI
North star: editorial monochrome on warm paper - a minimal typeset spread where warm-black ink, a light display serif, and pill-shaped controls turn a B2B tool into something that reads like a quarterly journal.

Use these palette anchors:

- Ink `#1a1a17` for Primary text, filled buttons, dark surface backgrounds, heading strokes - a warm-tinted near-black that replaces pure #000 throughout the system
- Paper `#ffffff` for Page canvas, card surfaces, light section backgrounds, button borders on dark surfaces
- Ash `#5f5f5d` for Secondary body text, helper text, muted borders, low-emphasis UI metadata

Use these typography anchors:

- Nyght Serif `--font-nyght-serif` for Reserved exclusively for display and heading levels (26-72px). Weight 300 is the signature: most systems reach for 600-700 serif, this whisper-weight creates editorial gravitas through restraint. Letter-spacing widens slightly at smaller sizes (0.03em) and tightens at display sizes (0.01em) to preserve optical balance.
- Switzer `--font-switzer` for Workhorse for nav, body, buttons, labels, card metadata, and small headings. Tracking runs consistently at 0.03em - a subtle positive letter-spacing that gives the grotesque a calm, considered cadence. Weight 500 for emphasis, 600 for button text and nav active states.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 64px.
- Card padding: 24px.
- Element gap: 8px.

Build these component patterns where relevant:

- Pill Primary Button: Filled action button for top-level CTAs
- Pill Ghost Button: Outlined or text-only action for secondary actions
- Pill Nav Link: Navigation items in header
- Editorial Display Heading: Section and hero headlines
- Product Mockup Card: Embedded product UI screenshots within feature sections
- Workflow Card: Three-column feature card on light section
- Stat Tile: Metric callouts in the trust strip below hero
- Feature Row: Two-column text + visual feature layout
- Chat Input Bar: AI assistant prompt inside product mockup
- Task List Item: Individual row inside the product mockup task list
- Status Pill Badge: Order/inventory status indicators inside mockups
- Icon Bullet: Small leading icon for feature list items

Do:

- Use Nyght Serif weight 300 for all heading and display text - never set a heading in Switzer
- Keep the entire interface within the #1a1a17 / #ffffff / #5f5f5d triad; resist introducing chromatic accents
- Set all buttons, nav active states, and tags to 1440px border-radius for the pill signature
- Maintain 0.03em letter-spacing on all Switzer text to preserve the editorial cadence
- Use 6px radius for cards, mockup containers, and any rectangular UI surface
- Place product mockups on #1a1a17 dark panels to create a museum-vitrine effect against the white page
- Anchor every section with 48-64px vertical gap to keep the editorial pacing

Avoid:

- Do not introduce blue, green, red, or any saturated brand color - the warmth comes from the near-black, not from accents
- Do not set Nyght Serif in weights other than 300 - adding bold or medium breaks the editorial voice
- Do not use square or 12px+ radii on buttons or tags - the pill shape is load-bearing
- Do not set body or heading text in pure #000000 - always use #1a1a17 for the warm-ink quality
- Do not use heavy drop shadows on cards - the system relies on hairline borders and surface contrast, not elevation
- Do not set line-height above 1.2 on Nyght Serif display sizes - the serif needs to sit tight to read as display, not body
- Do not apply gradients to text, buttons, or text containers - the palette is flat by design

Source prompt cues:

Quick Color Reference:
- text: #1a1a17
- background: #ffffff
- border: #5f5f5d (hairline) or #1a1a17 (emphasized)
- accent: no distinct accent - the system is monochromatic
- primary action: #1a1a17 (filled action)
- inverted surface: #1a1a17

Example Component Prompts:
1. Build a hero section: white background, max-width 1200px centered. Left half holds a Nyght Serif weight 300 headline at 72px, color #1a1a17, letter-spacing 0.01em, line-height 1.0. Below it a Switzer 16px weight 400 subtext in #5f5f5d, then a pill button - #1a1a17 background, #ffffff text, 1440px radius, 28px horizontal padding, Switzer 15px weight 500. Right half is a full-bleed photograph with no border-radius.
2. Build a workflow card: white surface, 6px radius, 24px padding, 1px border #5f5f5d. Top section is a product mockup on a #1a1a17 dark panel. Below the mockup, a Switzer 14px weight 500 eyebrow label in #1a1a17 with 0.06em tracking, then a Nyght Serif 26px weight 300 heading in #1a1a17, then a Switzer 16px weight 400 body paragraph in #5f5f5d.
3. Build a stat strip: three equal columns separated by 1px #5f5f5d vertical dividers, no top/bottom borders. Each column has a 16px monochrome icon in #1a1a17, then Switzer 16px weight 400 text in #1a1a17, 8px row gap between icon and text.
4. Build a feature row: two-column layout, 48px column gap. Left column has a Switzer 14px weight 500 eyebrow in #1a1a17, then a Nyght Serif 48px weight 300 heading, then three feature bullets each with a 16px icon, Switzer 20px weight 500 label, and Ash body text. Right column is a #1a1a17 dark panel, 6px radius, containing a white product mockup card with 24px padding.
5. Build a pill nav bar: white background, 64px height, flex row. Left: logo text in Switzer 16px weight 600 #1a1a17. Center: four Switzer 15px weight 400 nav links in #1a1a17, 34px gap. Right: a pill ghost button - transparent background, 1px border #1a1a17, 1440px radius, Switzer 15px weight 500 text #1a1a17, 16px 24px padding.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
