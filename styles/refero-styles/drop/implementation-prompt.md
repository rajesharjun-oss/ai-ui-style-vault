# AI Implementation Prompt

Build a Drop-inspired interface using this source-derived style bundle.

Reference site: https://www.usedrop.io
Theme: light
Category: SaaS
North star: lavender editorial spread in bold serif. Lavender dusk washing over stark white pages, anchored by a confident slab-serif voice that commands the page like a broadsheet headline.

Use these palette anchors:

- Obsidian `#101010` for Neutral form states, badge text, and quiet UI feedback where color should stay understated. Do not promote it to the primary CTA color
- Pure White `#ffffff` for Page canvas, card surfaces, text on dark fills - the default surface that 60%+ of the page lives on
- Carbon `#1a1a1a` for Dark card surfaces for product mockups and the dark editorial band, barely distinguishable from Obsidian to create depth without color
- Mint Cream `#e5ede4` for Light pastel surface tint, used sparingly for soft card backgrounds that need warmth without chromatic commitment
- Sage Mist `#c7d8c5` for Near-gray green surface wash, appears as a muted canvas tint on light sections and soft card backgrounds
- Ash Gray `#9b9b9b` for Muted helper text, secondary borders, inactive UI elements - handles every de-emphasized text or border role
- Lavender Mist `#b8afda` for Dominant chromatic accent, large section backgrounds, circle diagram fills, decorative borders - carries the brand's pastel identity and appears more than any other chromatic color
- Ember Orange `#eb652b` for Orange wash for highlight backgrounds, decorative bands, and soft emphasis behind content.
- Electric Yellow `#f6f361` for Secondary accent for borders, highlights, and decorative geometric elements - neon-charged against black to create energy

Use these typography anchors:

- ABC Normal `--font-abc-normal` for Workhorse sans for body, nav, buttons, badges, and even large display sizes. The 300 weight is the signature - lightweight and editorial rather than the 600+ bold most SaaS sites use for headlines, giving Drop a quiet authority. Letter-spacing tightens aggressively at larger sizes (from -0.005em at 16px to -0.041em at 177px).
- Ivar Display `--font-ivar-display` for Reserved exclusively for the largest display headings - the 'OLD WORLD' / 'NEW WORLD' editorial moments. A serif with 0.78 line-height and -0.043em tracking at 169px creates slab-like density that reads as printed editorial rather than web type. Weight stays at 400 even at poster scale, trusting the size and serif personality to carry authority.

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: 1200px.
- Section gap: 80-120px.
- Card padding: 14-16px.
- Element gap: 5-8px.

Build these component patterns where relevant:

- Primary Pill Button: Filled action button for demos and key conversions
- Ghost Pill Button: Secondary action with no fill
- Text Link with Underline: Inline and footer navigation links
- Navigation Bar: Top-level site navigation
- Hero Split Card - Black: Left-side product showcase card in the hero
- Hero Split Card - Lavender: Right-side product showcase card in the hero
- Brand Logo Strip: Social proof footer of the hero
- Editorial Display Section - Dark: Full-bleed dark band for the 'Old World' narrative
- Editorial Display Section - Light: Full-bleed light band for the 'New World' narrative
- Circle Comparison Diagram: Data visualization showing audience/engagement/customer scale
- Revenue Callout: Large monetary figure tied to the narrative
- Section Pill Badge: Inline label or tag for categorizing content

Do:

- Use Ivar Display only at 60px or larger - below that, it loses its editorial power and competes with the sans-serif body
- Use 1440px radius for every button, badge, and tag - the full pill is the most consistent shape in the system
- Reach for Lavender Mist (#b8afda) as the default chromatic surface before any other color - it carries brand identity more than orange or yellow
- Set display headlines to line-height 0.78-0.90 to let the serif slabs sit close together like editorial body type
- Use weight 300 or 400 in ABC Normal for body and even sub-headings - reserve 500 for tags, labels, and nav only
- Place Ember Orange only on revenue figures, the 'new world' headline split, and single-word accents - one orange moment per section maximum
- Keep card padding tight (14-16px) and let the large border-radius and background color do the visual work - no shadows needed

Avoid:

- Never use Ivar Display for body text, nav links, or anything below 60px - the serif personality overwhelms at small sizes
- Do not introduce a second chromatic accent color beyond the existing three (lavender, orange, yellow) - the palette is deliberately small
- Do not use box-shadows for elevation - Drop separates surfaces with hard color contrast (white vs black vs lavender), not depth
- Do not set display headlines to line-height above 1.0 - the tight leading is what makes the type feel printed rather than web-rendered
- Do not use sharp corners (0px radius) on any interactive element - even small UI should use at least 4-8px radius
- Do not place orange and yellow adjacent to each other - they vibrate against each other; let white or black separate them
- Do not center-align body text - left-align everything except display headlines and revenue figures

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
