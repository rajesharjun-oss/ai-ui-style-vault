# AI Implementation Prompt

Build a Framer-inspired interface using this source-derived style bundle.

Reference site: https://www.framer.com
Theme: dark
Category: Design
North star: cinematic black gallery. Pure black canvases cradle white editorial type and one electric blue accent that traces edges rather than filling space.

Use these palette anchors:

- Void `#000000` for Page background, primary canvas - the void that everything else sits on. Also used for filled primary buttons, nav background, card borders, and the vast majority of interface borders
- Carbon `#080808` for Card surface layer, elevated panels, secondary background - barely lifted from the void to suggest depth without leaving the dark family
- Obsidian `#111111` for Higher elevation cards and modal surfaces - the second step up from the page
- Graphite `#171717` for Top-tier surface for popovers, tooltips, and deeply nested panels
- Slate `#242424` for Mid-tone fills, hover states, subtle panel backgrounds
- Fog `#333333` for Button hover, pressed states, and darker UI fills
- Ash `#666666` for Muted text, secondary labels, disabled states, subtle borders
- Smoke `#8c8c8c` for Helper text, tertiary metadata, thin dividers
- Silver `#999999` for Secondary text, body copy at lower emphasis, border dividers
- Bone `#cccccc` for Light borders, subtle dividers on dark surfaces
- Paper `#ffffff` for Primary text, headings, filled button backgrounds, light-on-dark iconography - the dominant foreground against the void
- Deep Harbor `#021f33` for Deep blue-black for box-shadows and subtle tinted surface washes - carries the brand's cool undertone into elevation
- Electric Cyan `#0099ff` for Brand accent: link underlines, active nav state, focus rings, outlined button borders, decorative card borders, and text selection - appears only on edges and micro-states, never as a fill

Use these typography anchors:

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- GT Walsheim `--font-gt-walsheim` for Display and hero headlines. The ultra-condensed geometric character with aggressive negative tracking at 85-110px creates the editorial, almost cinematic weight that defines Framer's voice. At 110px the line-height compresses to 0.85, letting the headline feel like a single block of mass. Substitute: Inter Tight or Mona Sans as a free alternative.
- Inter Variable `--font-inter-variable` for Primary UI and body font. The extensive character variant alternates (cv01-cv11, ss02-ss07) tune individual glyphs - switching between straight and curved tails, alternate g shapes, and stylistic sets depending on context. Body text uses subtle negative tracking (-0.01em to -0.02em); uppercase labels use positive tracking (0.03em). Substitute: Inter (Google Fonts) with matching feature settings.
- Inter `--font-inter` for Secondary text, nav items, links, form labels, and button text. Weights 500-700 for emphasized UI elements. Tracking tightens dramatically at larger sizes (22px at -0.05em). Substitute: Inter from Google Fonts.
- Mona Sans `--font-mona-sans` for Secondary display and text accents. Used at 62px for section headers, with extremely tight tracking (-0.05em) giving it a dense, graphic feel. Substitute: Mona Sans (GitHub).
- Open Runde `--font-open-runde` for Micro-labels and oversized tagline micro-text. Substitute: Inter at 600 weight.
- GT Walsheim Framer Medium `--font-gt-walsheim-framer-medium` for GT Walsheim Framer Medium - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1200px.
- Section gap: 60-80px.
- Card padding: 20-24px.
- Element gap: 10px.

Build these component patterns where relevant:

- Primary Filled Button: Highest-emphasis action (e.g. 'Sign up', 'Start for free')
- Ghost/Outlined Button: Secondary action beside primary (e.g. 'Start with AI')
- Electric Outlined Action: Brand-tinted secondary action or focus/active state
- Hero Display Headline: Page-top headline anchoring the visual identity
- Customer Site Card: Showcase tiles in the logo wall / portfolio grid
- Testimonial Card: Social proof block with quote, attribution, and supporting visual
- Top Navigation Bar: Persistent site navigation
- Announcement Banner: Thin strip above hero linking to reports, events, or promotions
- Logo Grid (Customer Wall): Trust strip showing brands using the product
- Section Heading: Mid-page section titles (e.g. 'Powering ambitious teams worldwide')
- Dark Image Container: Framed media (screenshots, renders, video)
- Subtle Overlay Wash: Decorative gradient overlay for section transitions

Do:

- Set page background to #000000 and let all text be #ffffff by default - the void is the brand
- Use GT Walsheim at 85-110px for hero headlines with letter-spacing -0.05em and line-height 0.85
- Use 100px pill radius for all buttons and tags - never square buttons
- Use 10px as the standard element gap; only reach 20-24px for card padding and 60-80px for section gaps
- Apply Electric Cyan (#0099ff) only to edges: borders, underlines, focus rings, and active states - never as a fill
- Use Inter at 14px weight 400 for body text with letter-spacing -0.01em
- Express elevation through surface color progression (Carbon Obsidian Graphite) rather than heavy shadows

Avoid:

- Don't introduce any background color other than the black-to-charcoal surface stack - no grays, no tinted backgrounds, no warm tones
- Don't use Electric Cyan (#0099ff) as a filled button background - it is an edge accent only
- Don't use box shadows with offset greater than 10px on regular cards - the design is flat-by-default
- Don't set border-radius below 8px on any container - the minimum visual softness is 8px
- Don't use font-weight above 500 for display type - GT Walsheim at 500 is already commanding; going heavier breaks the voice
- Don't add decorative gradients, glows, or colored backgrounds to sections - sections transition through pure black
- Don't use color for body text - keep all text in #ffffff, #999999, or #666666 only

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
