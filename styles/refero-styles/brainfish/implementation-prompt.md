# AI Implementation Prompt

Build a Brainfish-inspired interface using this source-derived style bundle.

Reference site: https://www.brainfishai.com
Theme: light
Category: AI
North star: lime-marker editorial broadsheet - a near-monochrome page where a single vivid green stroke does all the work

Use these palette anchors:

- Lime Sprint `#a3e635` for Green action color for filled buttons, selected navigation states, and focused conversion moments.
- Paper White `#ffffff` for Primary page canvas and inverse text on dark surfaces
- Cream `#fcfff7` for Warm off-white surface for cards, stat tiles, and footer - a barely-there yellow-green tint that distinguishes a lifted surface from the page without introducing a new color
- Ink `#262626` for Primary text color, default border, icon stroke, and hard shadow color. This is the single dark token that does structural work across text, lines, and elevation
- Black Ink `#000000` for Strongest display text and filled icon glyphs where maximum weight is needed inside a headline or pull-quote
- Depth `#303030` for Dark button and surface background - used for the large primary action blocks in the nav and hero where a heavier fill than ink is needed but true black would be too harsh
- Rule `#e5e5e5` for Hairline borders, card outlines, footer dividers, and the soft separator between sections
- Muted `#525252` for Secondary body text, supporting descriptions, and the slightly softer voice below a heading
- Muted Gray `#737373` for Tertiary helper text, badge labels, copyright fine print, and the most de-emphasized text in the hierarchy
- Mint Edge `#7ee2b8` for Green accent for outlined action borders, linked labels, and lightweight interactive emphasis
- Mint Wash `#dcfff1` for Gray action color for filled buttons, selected navigation states, and focused conversion moments

Use these typography anchors:

- Geist `--font-geist` for Primary interface and headline face. Used for navigation, buttons, body copy, and most display text. Weight 600 carries the display sizes (28-56px) with consistently negative letter-spacing; weight 400 carries body and caption. Tight tracking on headings (-0.0200em) compresses the geometric forms into a more editorial density rather than the wide airy SaaS default
- Fraunces `--font-fraunces` for Display serif reserved exclusively for one or two italic emphasis words inside a Geist headline - the word 'every', 'actually', 'B2B complexity'. This single serif italic inside a sans-serif sentence is the site's editorial signature: it signals that the system thinks in terms of typeset prose rather than product copy. Never used for body, buttons, or full headlines
- Phosphor-Fill `--font-phosphor-fill` for Phosphor-Fill - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 8px.

Build these component patterns where relevant:

- Lime Primary Button: Primary call-to-action - the only filled chromatic button in the system
- Dark Block Button: Large primary action block for nav and hero CTAs
- Outlined Secondary Button: Secondary action paired with a lime primary - used for 'Join webinar' and similar
- Ghost Text Link: Inline text link and nav anchor
- Cream Stat Card: Numeric proof tile in the 4-column results band
- Status Pill Badge: Live status indicator - 'All platforms & systems operational'
- Pill Tag: Category label and personalization chip (e.g. 'ROLE: Product Manager', 'PLAN: Pro Annual')
- Top Navigation Bar: Primary site navigation
- Hero Split Section: Above-the-fold introduction
- Customer Logo Strip: Social proof row directly below the hero CTAs
- Testimonial Quote Section: Long-form customer pull-quote
- Feature Mockup Card: Product UI showcase used in feature sections

Do:

- Use #a3e635 lime exclusively for primary CTAs, the 'Book a demo' button, and hero gradient halos - never as a text color, icon fill, or decorative background
- Pair every Geist weight 600 headline with exactly one or two Fraunces italic emphasis words - the italic word should be a contrasting idea or qualifying word (every, actually, B2B complexity, this week)
- Apply 2px 2px 0 0 #262626 hard offset shadows to interactive elements on hover/active - never use blur-based drop shadows
- Set button border-radius to 4px (small inline buttons) or 0px (large block buttons) - the system deliberately rejects pill-shaped buttons on the main UI
- Use #fcfff7 cream as the only card/band surface above #ffffff white - this warm off-white is what distinguishes a lifted area from the page without introducing a new color family
- Set headings at 56px (display) or 48px (heading-lg) with negative letter-spacing between -0.28px and -0.96px - never default to loose tracking on display sizes
- Use the topographic contour-line illustration as a continuous background watermark across entire sections, not as a single hero image

Avoid:

- Don't introduce a second chromatic accent beyond lime and mint - the system is monochrome with exactly two purposeful color moments (lime for action, mint for live status)
- Don't use soft blurred drop-shadows - every shadow in the system is a 2px solid offset in #262626 ink, or it doesn't exist
- Don't round buttons to 8px+ - the button radii are 4px or 0px, never pill-shaped on the main UI (pills are reserved for tags and status indicators only)
- Don't use Fraunces for body text, buttons, or full headlines - the serif is only for the italic emphasis word inside a Geist sentence
- Don't use #000000 for borders or large fills - reserve true black for the strongest display text weight, and use #262626 ink for all strokes, borders, and structural dark
- Don't add gradients to body backgrounds or card surfaces - the only gradient in the system is the soft lime radial halo in the hero
- Don't apply uppercase 0.08em tracking to body copy or headings - reserve it for tiny labels, badge chips, and tabular meta data (e.g. 'PERSONALIZING FOR SARAH', 'ROLE:')

Source prompt cues:

**Quick Color Reference**
- text: #262626 (Ink)
- background: #ffffff (Paper White)
- surface / card: #fcfff7 (Cream)
- border: #e5e5e5 (Rule) | 1px solid #262626 for structural borders
- accent: #a3e635 (Lime Sprint)
- primary action: #a3e635 (filled action)

**Example Component Prompts**

1. Create a Primary Action Button: #a3e635 background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. *Build a stat tile row.* Cream (#fcfff7) full-width background band with four stat cards arranged in a grid, each 24px padding, #fcfff7 surface, 8px radius, 1px solid #e5e5e5 border, no shadow. Number at 48px Geist weight 600 in #262626. Description at 18px Geist weight 400 in #525252. Source attribution at 14px Geist weight 400 in #737373. 80px section gap above and below the band.

3. *Build a status pill badge.* Background #dcfff1, 1px solid #7ee2b8 border, 9999px border-radius, 6px vertical / 12px horizontal padding. Text at 14px Geist weight 500 in #262626, paired with a 6px mint (#7ee2b8) dot to the left. Use this pattern only for live system status indicators - never for generic tags or labels.


5. *Build a testimonial pull-quote section.* Full-width cream (#fcfff7) background. Large quote at 36px Geist weight 600 in #262626 occupying the left two-thirds, with one or two emphasis words in Fraunces italic weight 500. Right column: 48px circular portrait image and a 16px Geist weight 500 name in #262626 with a 14px Geist weight 400 role line in #737373. No card container - the cream band is the surface. 80px section gap above and below.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
