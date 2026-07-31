# AI Implementation Prompt

Build a Pangram Pangram Foundry-inspired interface using this source-derived style bundle.

Reference site: https://pangrampangram.com
Theme: light
Category: Design
North star: Museum vitrine on white marble. A gallery-style type foundry where the canvas is bare stone, the lighting is flat daylight, and the only vivid color is a single orange-red label used by a curator to flag what is new.

Use these palette anchors:

- Ember Orange `#ff2f00` for Orange action color for filled buttons, selected navigation states, and focused conversion moments.
- Marble White `#fafafa` for Page canvas, card surfaces, input fields, default panel backgrounds. The dominant surface tone, barely off-white for warmth
- Stone Gray `#ededed` for Secondary surface for filled buttons, muted card backgrounds, image placeholder fills. One step deeper than Marble White to create gentle separation without contrast
- Graphite `#666666` for Secondary text, link color, subdued metadata, helper text. Reads as muted black - never used for primary text or headings
- Ink Black `#000000` for Primary text, all headings, hairline borders (cards, lists, badges, inputs), icons, navigation. The structural backbone - 1px borders everywhere define the system
- Signal Yellow `#ffb700` for Yellow state accent for badges, validation surfaces, and short status labels.
- Ice Blue `#bfe0ff` for Blue state accent for badges, validation surfaces, and short status labels.

Use these typography anchors:

- Neue Montreal `--font-neue-montreal` for The workhorse and display face. Weight 400 for body, weight 530 for subheads and medium emphasis, weight 600 for headings and display overlays. Used at 145px for hero type, 48px for section headlines, 18-20px for body, 14px for navigation, 12px for badges. The type IS the product - this single family carries the entire brand voice.
- Neue Montreal Semibold `--font-neue-montreal-semibold` for Heavy display variant used for the largest typographic moments in specimen cards. Tighter, more compressed than standard weight 600.
- Neue York `--font-neue-york` for Companion serif/contrast face shown in specimen contexts. The 700 weight provides a sharp counterpoint to the geometric Montreal.
- Frama Semibold `--font-frama-semibold` for Specimen showcase weight - displayed at exact 103px in the grid to demonstrate each family's character at scale.
- Kyoto Semibold `--font-kyoto-semibold` for Specimen showcase - fixed 103px display size in the font grid.
- Neue Gstaad Bold `--font-neue-gstaad-bold` for Specimen showcase - fixed 103px display size in the font grid.
- Palma Fizzy Heavy `--font-palma-fizzy-heavy` for Specimen showcase - fixed 103px display size in the font grid.
- Mori Bold `--font-mori-bold` for Specimen showcase - fixed 103px display size in the font grid.
- Museum Light `--font-museum-light` for Specimen showcase - the 300 weight in the grid is deliberately whisper-light, making weight 300 headlines read as anti-convention: authority through restraint rather than volume.
- Neue Corp Semibold `--font-neue-corp-semibold` for Specimen showcase - fixed 103px display size in the font grid.
- Watch Medium `--font-watch-medium` for Specimen showcase - fixed 103px display size in the font grid.
- Monument Narrow Medium `--font-monument-narrow-medium` for Specimen showcase - fixed 103px display size in the font grid.
- Model Plastic Regular `--font-model-plastic-regular` for Specimen showcase - fixed 103px display size in the font grid.
- neue-gstaad-normal-bold `--font-neue-gstaad-normal-bold` for neue-gstaad-normal-bold - detected in extracted data but not described by AI
- neue-corp-normal-semibold `--font-neue-corp-normal-semibold` for neue-corp-normal-semibold - detected in extracted data but not described by AI
- neue-york-normal-normal-bold `--font-neue-york-normal-normal-bold` for neue-york-normal-normal-bold - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 92px.
- Card padding: 26px.
- Element gap: 8px.

Build these component patterns where relevant:

- Hero Font Showcase Card: Full-bleed feature card for a typeface release
- Status Badge - New: Highlight tag for newly released fonts
- Status Badge - Update: Highlight tag for recently updated fonts
- Status Badge - Early Access: Highlight tag for preview/beta releases
- Primary Filled Button: Main call-to-action (Explore font, Try for Free)
- Ghost Outlined Button: Secondary action paired with primary button
- Font Specimen Card (Grid View): Card showing one typeface in the font catalog grid
- Navigation Bar: Top site navigation
- Section Divider: Visual separator between content sections
- Input Field: Text input for search or forms
- View Toggle (Card View / List View): Switch between display modes in the font grid
- Footer Link Group: Footer navigation cluster

Do:

- Use only #ff2f00 as the chromatic accent - it must remain rare enough to register as editorial highlight, not decoration
- Set all borders to 1px solid #000000 for cards, lists, badges, and inputs - the hairline black is the structural skeleton
- Use 20px border-radius for cards, buttons, and inputs; reserve 999px exclusively for badge pills
- Set hero type to Neue Montreal at 121-145px weight 600 with line-height 1.00 - the type should fill the card vertically
- Use status badges (#ff2f00 New, #ffb700 Update, #bfe0ff Early Access) as the only chromatic elements in any view
- Set card padding to 26px and card gaps to 15-23px to maintain the comfortable editorial density
- Let full-bleed photography carry the hero sections - never apply colored backgrounds to hero cards

Avoid:

- Do not use #ff2f00 for body text, headings, or large surfaces - its role is badge/punctuation only
- Do not apply box-shadow or heavy elevation - the system relies on 1px borders and whitespace, not depth
- Do not use radius values other than 20px (cards/buttons/inputs) and 999px (badges) - the rounded softness is signature
- Do not use colors other than the defined palette - no decorative blues, greens, or purples for UI chrome
- Do not use multiple type families in the same view - Neue Montreal carries everything except specimen showcases
- Do not set line-height above 1.30 for any size - the tight leading is essential to the editorial feel
- Do not center body text or metadata - only headlines and hero type use center alignment

Source prompt cues:

Quick Color Reference:
- text: #000000
- background: #fafafa
- border: #000000 (1px hairline)
- secondary surface: #ededed
- muted text: #666666
- accent: #ff2f00 (badges, icons, highlights only)
- primary action: #ff2f00 (filled action)

Example Component Prompts:

1. Create a hero font showcase card: full-bleed background image filling a 20px-radius card. Centered title in Neue Montreal 121px weight 600, color #ffffff, line-height 1.00. Subtitle below in Neue Montreal 18px weight 400, #ffffff. A #ff2f00 status pill badge (999px radius, white text, 12px) floats above the title. A white filled pill button ('Explore font') and a white ghost outlined button ('Try for Free') sit side by side at the bottom center - both 20px radius, padding 8px 23px, 14px weight 500.

2. Create a font specimen grid card: #fafafa background, 1px #000000 border, 20px radius, 26px padding. Font name at top-left in Neue Montreal 18px weight 530, #000000. Metadata below in Neue Montreal 14px weight 400, #666666. A #ff2f00 'New' pill badge (999px radius, 12px weight 500, white text) positioned top-right. A massive 'Aa' at ~103px in the showcased font, bottom-aligned, #000000. Cards arrange in a 4-column grid with 20px gaps.

3. Create a status badge: pill shape (999px radius), 4px 12px padding, Neue Montreal 12px weight 500. Three variants: #ff2f00 bg + white text (New), #ffb700 bg + black text (Update), #bfe0ff bg + black text (Early Access).

4. Create the top navigation bar: full-width, transparent background, ~60px height. 'Pangram Pangram Foundry' logo at far left in Neue Montreal 14px weight 530. Five nav links center-aligned in Neue Montreal 14px weight 400, #000000, with 23px gap between items. Search icon, cart icon, and hamburger menu icon right-aligned, all 1px stroke black.

5. Create a filled action button: 20px border-radius, #fafafa background, 1px #000000 border, Neue Montreal 14px weight 500, #000000 text, padding 8px 23px. Inline display, no shadow. This is the 'Explore font' button - the system's only filled button variant.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
