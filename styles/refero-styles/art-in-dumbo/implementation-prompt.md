# AI Implementation Prompt

Build a Art In DUMBO-inspired interface using this source-derived style bundle.

Reference site: https://artindumbo.com
Theme: light
Category: Agency
North star: gallery broadside on raw paper

Use these palette anchors:

- Carbon `#000000` for Primary text, logo cells, hairline dividers between list rows, icon strokes - the only ink in the system
- Paper `#ffffff` for Page canvas, card surfaces, pill-button fills, inverse text on dark cells
- Plaster `#f1f2f2` for Input fields, secondary surfaces, subtle button hovers
- Linen `#e5e3df` for Warm off-white section backgrounds, large quiet surfaces that break the white without going gray
- Ash `#bdbdbd` for Medium-contrast borders, control outlines, and structural separators
- Graphite `#828282` for Button borders and label text for secondary controls
- Smoke `#b3b3b3` for Shadow base tone for the single ambient drop-shadow pattern
- Sage `#71cc98` for Green action color for filled buttons, selected navigation states, and focused conversion moments
- Ember `#ff7f41` for Orange outline accent for tags, dividers, and focused UI edges. Use as a supporting accent, not as a status color

Use these typography anchors:

- Helvetica Neue `--font-helvetica-neue` for Sole typeface across the entire system - display, body, nav, labels. Weight 500 is the only weight used; this medium-only commitment is the signature: not bold, not regular, never thin. Sizes run from 10px captions to 68px display with tight 1.05-1.15 line-heights at the top of the scale and 1.40-1.80 at body sizes.
- Roboto `--font-roboto` for Secondary system fallback for micro-labels and small UI chrome where a different metric helps

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80-120px.
- Card padding: 16-24px.
- Element gap: 12-20px.

Build these component patterns where relevant:

- Logo Wordmark Block: Brand mark in the top-left of every screen
- Sticky Header Bar: Persistent navigation across all pages
- Full-Bleed Hero Photograph: Above-the-fold visual anchor on the landing page
- Display Heading: Section openers and welcome statements
- Body Paragraph: Welcome copy, event descriptions, editorial text
- Email Input Field: Newsletter capture on the welcome block
- Ghost Text Button (Subscribe): Secondary action paired with form fields
- Sage Pill Button (Map & Directory): Primary floating CTA, sticky bottom-right
- Exhibition List Row: Primary content unit on the Exhibitions page
- Urgency Tag (Closing Soon): Status indicator for time-sensitive items
- Status Meta (Open hours): Secondary metadata in list rows
- Sticky Floating Action: Persistent wayfinding CTA

Do:

- Use #000000 for all structural lines, icons, and primary text - it is the only ink the system has
- Reserve #71cc98 Sage exclusively for the Map & Directory pill, heading underline marks, and accent dots
- Set border-radius to 50px on pill buttons and 2px on inputs - never blur the two
- Set type to Helvetica Neue 500 at the scale sizes; do not introduce additional weights
- Separate exhibition list rows with 1px solid #000000 hairlines, never with card backgrounds or zebra striping
- Let hero photography run full-bleed with no overlay text other than the wordmark
- Use #ff7f41 Ember only for urgency status text such as 'Closing Soon' - never as a fill

Avoid:

- Do not add colored panels, gradient fills, or decorative cards behind text
- Do not introduce new typefaces or weight values beyond Helvetica 500 and the Roboto micro-label fallback
- Do not use shadows to separate sections - use 1px black hairlines or a shift to #e5e3df Linen
- Do not round the hero photograph or exhibition thumbnails beyond 4px
- Do not stack more than two type sizes in a single row of the exhibitions list
- Do not place sage green text on the sage pill background - it must remain #000000
- Do not center body paragraphs or exhibition row content; left-align everything

Source prompt cues:

Quick Color Reference:
- text: #000000
- background: #ffffff
- surface-warm: #e5e3df
- surface-input: #f1f2f2
- border: #000000
- accent: #71cc98 (Sage)
- primary action: #71cc98 (filled action)

3 Example Component Prompts:
1. Sage Pill Button: 50px border-radius, #71cc98 fill, 19px Helvetica 500 #000000 label, 20px horizontal padding, 10px vertical padding, a 8px filled sage dot inside the left padding, shadow rgba(0,0,0,0.25) 0 0 10px.
2. Exhibition List Row: four columns - 80px square thumbnail (4px radius), date range in 16px Helvetica 500 #000000, title in 22px Helvetica 500 #000000, gallery name in 19px Helvetica 500 #000000 with 'Open: HH:MM-HH:MM' in 16px #bdbdbd below. Rows separated by 1px solid #000000 hairline, no row background.
3. Display Heading Block: 63px Helvetica 500 #000000, line-height 1.05, with a 3px #71cc98 horizontal rule directly under the heading spanning the full text width. Followed by a 22px Helvetica 500 #000000 body paragraph at line-height 1.27, no max-width clamp.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
