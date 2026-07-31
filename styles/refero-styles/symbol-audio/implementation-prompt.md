# AI Implementation Prompt

Build a Symbol Audio-inspired interface using this source-derived style bundle.

Reference site: https://www.symbolaudio.com
Theme: dark
Category: E-commerce
North star: midcentury listening room after dusk

Use these palette anchors:

- Evergreen Gallery `#1c3c27` for Green accent for outlined action borders, linked labels, and lightweight interactive emphasis. Do not promote it to the primary CTA color
- Frost White `#fffffd` for Product card surfaces, text on dark sections - slightly warm off-white, never pure #fff
- Pewter Mist `#dfe2e5` for Hairline borders, card outlines, divider rules, ghost-button borders on light cards
- Onyx `#000000` for Primary text on light cards, icon strokes, high-contrast detail
- Bone `#fffcda` for Alternate warm cream surface - contrast-pair companion to dark text on light cards
- Ink Shadow `#0e1e14` for Deepest text on evergreen, near-black with green undertone - pairs with frost-white for AAA contrast
- Marquee Cobalt `#447cf0` for Violet outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color
- Ember Lacquer `#c72a00` for Vivid red-orange seen in product photography (lacquered shelf units) - decorative, not functional

Use these typography anchors:

- Chalet-LondonSixty `--font-chalet-londonsixty` for Primary body and UI typeface - all nav links, product names, prices, badge text, footer copy, button labels. A custom rounded serif with distinctive ball terminals; its single weight is used universally
- Chalet-NewYorkSixty `--font-chalet-newyorksixty` for Secondary serif variant for body and link micro-copy - visually similar to LondonSixty but used in narrower contexts (small body, secondary links)
- SupremeLL-Bold `--font-supremell-bold` for Display and heading typeface - exclusively carries section headings ("What's on: Bestsellers..."), the hero wordmark, and large UI moments. A sharp geometric sans that cuts against the serif body type. The massive 80px size with -0.02em tracking is the signature move
- SupremeLL-BoldFlat `--font-supremell-boldflat` for Flat-cut variant of the display sans for inline link emphasis within body copy

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1280px.
- Section gap: 40px.
- Card padding: 20px.
- Element gap: 20px.

Build these component patterns where relevant:

- Top Navigation Bar: Site-wide header
- Announcement Marquee: Repeating bottom ticker
- Hero Display Wordmark: Brand statement above-the-fold
- Product Card: Grid item for catalog
- Product Tag Badge: Status indicator on product cards
- Section Heading: Band title on evergreen
- Ghost Text Link: Inline and standalone navigation
- Outlined Action Button: Primary CTA on light surfaces
- Hero Product Photograph: Full-bleed editorial image

Do:

- Use #1c3c27 as the page canvas for every section band - the entire site lives inside this single color, section transitions are invisible.
- Pair the Chalet serif for all body, nav, prices, and badges with SupremeLL-Bold for every heading - never mix roles.
- Set product card backgrounds to #fffffd (Frost White) with 0px radius and a hairline #dfe2e5 border - the card is a placard, not a tile.
- Use 9999px border-radius for every badge, tag, and pill button - sharp corners everywhere else.
- Anchor display headlines to the left edge and let them run large (52-80px) with -0.02em tracking in SupremeLL-Bold.
- Place the announcement marquee fixed to the bottom viewport edge with the evergreen fill - it never scrolls away.
- Use #000000 text on frost-white cards and #dfe2e5 text on evergreen - maintain the 16:1+ contrast ratio at all times.

Avoid:

- Do not introduce a filled solid-color button - this system only uses outlined/ghost actions on transparent fills.
- Do not use the blue (#447cf0) or red (#c72a00) as functional UI colors - they are decorative photography accents only.
- Do not apply border-radius to product cards or hero images - the system is sharp-edged everywhere except pills and badges.
- Do not set body text in SupremeLL-Bold - the sans is exclusively for display and headings.
- Do not add box-shadow or drop-shadow to cards or images - surfaces are flat, the contrast comes from color, not elevation.
- Do not use pure #ffffff for surfaces or text - the system runs #fffffd (frost) and #dfe2e5 (pewter) for its lightest tones.
- Do not break the marquee pattern - the announcement ticker is always present, always fixed, always evergreen-on-pewter.

Source prompt cues:

**Quick Color Reference**
- text (on light): #000000
- text (on dark): #dfe2e5
- background: #1c3c27 (evergreen canvas)
- card surface: #fffffd (frost white)
- border: #dfe2e5 (hairline pewter)
- accent: #1c3c27 (same as canvas, used for outlined action border on light cards)
- primary action: #1c3c27 (outlined action border)

**3-5 Example Component Prompts**

1. **Product Card**: Frost-white (#fffffd) rectangular surface, 0px border-radius, 1px #dfe2e5 hairline border, 20px padding. Product name in Chalet-LondonSixty 15px #000000. Price line "from $3,650" in same font. No shadow. Top-left pill badge: 9999px radius, transparent fill, 1px #1c3c27 border, label "New Arrival" in Chalet-LondonSixty 11px #1c3c27.

2. **Hero Display Wordmark**: The word "Symbol" in SupremeLL-Bold 80px, color #dfe2e5, letter-spacing -0.02em, set so it bleeds off both the left and right edges of the viewport. No container, sits directly on the evergreen canvas.

3. **Section Heading**: "What's on: Bestsellers..." in SupremeLL-Bold 52px #dfe2e5, letter-spacing -0.02em, left-aligned on the evergreen (#1c3c27) canvas. No underline, no decorative element, trailing ellipsis is part of the signature.

4. **Ghost Outlined Action Button**: Transparent fill, 1px solid #1c3c27 border, 9999px border-radius, 10px vertical padding, 20px horizontal padding. Label "Book an Appointment" in Chalet-LondonSixty 15px #1c3c27. Sits on a frost-white (#fffffd) surface.

5. **Announcement Marquee**: Fixed to viewport bottom, full-width band, background #1c3c27, no vertical padding. Continuously scrolling text in Chalet-LondonSixty 13px #dfe2e5 reading "Our NYC Showroom is now open! Book an Appointment" with "Book an Appointment" rendered as an underlined inline link.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
