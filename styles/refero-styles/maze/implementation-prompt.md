# AI Implementation Prompt

Build a Maze-inspired interface using this source-derived style bundle.

Reference site: https://maze.co
Theme: light
Category: SaaS
North star: Editorial research journal - warm bone paper, serif ink, chartreuse highlighter

Use these palette anchors:

- Bone `#f5f4f0` for Page canvas, footer, secondary button fills - warm off-white replaces cold digital white, giving every screen a paper-like base
- Paper `#ffffff` for Card surfaces, elevated panels, input fields - the bright layer above bone
- Ink `#1c1c1c` for Primary text, dark filled buttons, heading color - the default ink, warm near-black rather than #000
- Charcoal `#000000` for Hairline borders, icon strokes, the announcement bar - the thinnest line work
- Fossil `#706f6c` for Secondary text, muted borders, body annotations
- Pebble `#9e9b94` for Input field borders, disabled controls
- Smoke `#3c3c3c` for Body annotations, meta labels
- Sand `#eae6e1` for Active tab background, subtle surface lift, button hover on bone
- Ash `#d2cec6` for Hairline dividers, footer borders, low-contrast separators
- Chartreuse `#dbf570` for Highlight badges, study tags, the globe motif, card accent fills - the only chromatic note in the system, used sparingly to draw the eye to research signals
- Olive `#4b5b0a` for Decorative border accent, chromatic link underline - the only deep color, appears in the olive outline treatments and the heading underline on the hero

Use these typography anchors:

- ui-sans-serif `--font-ui-sans-serif` for ui-sans-serif - detected in extracted data but not described by AI
- Phonic `--font-phonic` for Display, headings, body - the brand's signature humanist serif set aggressively tight at large sizes (-0.09em at 130px down to +0.03em at 12px). Weight 300 dominates for display, 400 for body. The custom typeface carries the editorial voice; weight 300 at 130px is the signature move - most brands use 600-700 here, Maze whispers in a light serif to claim authority through restraint.
- System UI Sans `--font-system-ui-sans` for Secondary UI text, fallback for browser contexts - only used sparingly; Phonic carries the brand

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 8px.

Build these component patterns where relevant:

- Announcement Bar: Top-of-page notification strip
- Top Navigation: Primary site navigation
- Filled Dark Button: Primary action
- Outlined Ghost Button: Secondary action
- Hero Headline Block: Above-the-fold page opening
- Report Preview Card: Featured product surface card
- Unmoderated Study Card: Study result card with rating
- Video Interview Card: Moderated study video tile
- Section Headline Overlay: Mid-page editorial section break
- Tab Navigation: Segment control
- Menu List Panel: Recruitment category list
- Pixel Globe Illustration: Brand motif, section break

Do:

- Use Phonic at weight 300 for every display and headline; weight 400 for body and UI only
- Default to a 12px radius on cards, 8px on buttons, 4px on badges - the radius scale is narrow and intentional
- Use #f5f4f0 (Bone) as the page canvas; reserve #ffffff for cards and inputs that need to lift off the canvas
- Let Chartreuse (#dbf570) appear as small functional punctuation - one badge, one tag, one globe - never as a wide wash of UI color
- Track headlines aggressively tight: -6.3px at 90px, scaling proportionally so letters almost touch at the largest sizes
- Keep buttons quiet: Ink-filled or Ink-outlined, 8px radius, 12px x 20px padding, no shadow, no gradient
- Use Lavender (#b8a3ff) full-bleed for section breaks to create contrast against the bone canvas

Avoid:

- Do not use sans-serif for headlines - Phonic serif at weight 300 IS the brand voice; substituting bold sans-serif destroys the editorial register
- Do not apply heavy box-shadows to cards - the system is intentionally flat, elevation is a hairlines-only discipline
- Do not use Chartreuse as a CTA background - it is a highlight color for tags and motifs, not an action color; Ink stays the action
- Do not set display text at line-height 1.4+ - headlines run tight (1.00-1.10) so the serif rhythm stays architectural
- Do not introduce new chromatic colors beyond the three in the palette (Chartreuse, Olive, Lavender) - every additional hue dilutes the bone-paper system
- Do not use #000000 as body text - Ink (#1c1c1c) is the text color; #000 is reserved for the announcement bar and hairline borders
- Do not center body paragraphs in cards - only section headlines and hero copy may center; study card copy stays left-aligned

Source prompt cues:

QUICK COLOR REFERENCE
- Canvas: #f5f4f0 (Bone)
- Card surface: #ffffff (Paper)
- Primary text: #1c1c1c (Ink)
- Hairline border: #000000 (Charcoal)
- Muted text: #706f6c (Fossil)
- Accent: #dbf570 (Chartreuse)
- primary action: #1c1c1c (filled action)

EXAMPLE COMPONENT PROMPTS
1. Create a Primary Action Button: #1c1c1c background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
2. REPORT PREVIEW CARD - White (#ffffff) surface, 8px radius, no shadow. Header label 'Report Preview' in Phonic 12px / 400 / #706f6c. Chartreuse (#dbf570) image block filling top half with 8px top radius. Body in Phonic 17px / 400 / #1c1c1c with a right-aligned stat column in #706f6c.
3. TAB SEGMENT CONTROL - Three Phonic 46px / 300 labels in #1c1c1c. Active tab on a #eae6e1 pill background with 8px radius and 12px 20px padding. Inactive tabs transparent. 16px gap between tabs.
4. STUDY TAG BADGE - Chartreuse (#dbf570) background, #1c1c1c text, Phonic 12px / 400, 4px radius, 4px 8px padding. Sits at top-left of study cards.
5. PIXEL GLOBE SECTION BREAK - Full-bleed #dbf570 background, centered Phonic 58px / 300 / #1c1c1c headline with letter-spacing -3.48px layered over a 600px dot-matrix globe illustration. Sub-paragraph in Phonic 17px / 400 / #706f6c below the headline.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
