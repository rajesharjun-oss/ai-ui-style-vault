# AI Implementation Prompt

Build a Afterglo-inspired interface using this source-derived style bundle.

Reference site: https://myafterglo.com
Theme: light
Category: E-commerce
North star: Editorial boudoir printed on cream paper - quiet, tactile, typographic.

Use these palette anchors:

- Ivory Paper `#f3f2ec` for Page canvas, card surfaces, footer wash - the warm off-white that makes every photograph feel printed, not digital
- Sage Mist `#e3e4df` for Hairline borders, input outlines, subtle dividers, secondary card backgrounds - the cool-warm neutral that separates layers without contrast shouting
- Bone Gray `#cbc9bd` for Mid-tone neutrals for input shadows and muted surface fills - the bridge between ivory and ink
- Ink Black `#131313` for Primary text, filled buttons, icon strokes, navigation borders - slightly softer than pure black, reads as printer's ink rather than screen
- Pure Black `#000000` for Highest-contrast borders, pure ink for heaviest typographic moments and fine dividers
- Snow White `#ffffff` for Product card photography backdrop, badge fills - the cleanest white for product isolation
- Ember Coral `#f68e6d` for Footer background, singular warm accent - the one chromatic gesture in the system, used only when the design needs to feel touched, not seen
- Powder Blue `#7faad2` for Blue state accent for badges, validation surfaces, and short status labels. Do not promote it to the primary CTA color

Use these typography anchors:

- Aeonik `--font-aeonik` for Workhorse sans for navigation, body, buttons, product cards, and hero overlays. 500 weight for active nav, labels, and emphasis; 400 for body copy. The 132px display size at 0.80 line-height is the signature - oversized headlines that sit tight and confident over photography.
- Cardinal Fruit `--font-cardinal-fruit` for Display serif reserved for editorial moments: the 'FEEL YOUR SELF' statement, category callouts, and the small italic accent '(BEST)'. At 187px with 1.00 line-height it becomes the visual anchor of the page - a magazine-cover gesture that reframes the whole interface as editorial, not transactional.

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: 1440px.
- Section gap: 25-33px.
- Card padding: 17px.
- Element gap: 8-17px.

Build these component patterns where relevant:

- Primary Navigation Bar: Top-level site navigation
- Product Card: Product grid item in featured/listing sections
- Out of Stock Badge: Availability indicator on product cards
- Info Badge: Decorative or informational tagging
- Hero Photography Panel: Full-bleed opening section
- Filled Primary Button: Primary call-to-action (e.g. 'Start Exploring', 'About Us')
- Ghost Text Button: Secondary inline action or link styled as button
- Editorial Display Heading: Section or page statement
- Featured Section Header: Section title for product grids
- Image Collage Panel: Editorial about/mission section visual
- Category Carousel Arrow: Horizontal navigation for product carousels
- Input Field: Form input (search, email, etc.)

Do:

- Use Cardinal Fruit serif at 54px+ for editorial display moments and reserve it for those moments - one per section maximum
- Set Aeonik display sizes at tight line-heights: 0.80 for 132px headlines, 1.00 for 50-54px section titles, 1.20 for 22px body
- Apply the 5px radius universally to cards, buttons, badges, and inputs - it is the system's only rounding gesture
- Use the ivory canvas (#f3f2ec) as the default background for every page; let #ffffff appear only inside product photography frames
- Pair Aeonik weight 500 for navigation labels, buttons, and the brand mark; weight 400 for body copy and descriptions
- Let the footer be the only surface that uses #f68e6d - do not introduce the coral accent on buttons, badges, or links
- Build product cards as flat compositions: image on white, text below in ink, no hover elevation, no shadows, no borders around the card itself

Avoid:

- Do not use the powder blue (#7faad2) as a CTA or filled action - it is decorative only, reserved for soft badges and washes
- Do not apply drop shadows to cards, buttons, or images - the system stays flat; depth comes from type and photography
- Do not introduce border-radius values other than 5px - the system uses one rounding gesture, repeated exactly
- Do not use pure black (#000000) for large body text - reserve it for fine borders and heaviest display moments; use #131313 for readable text and buttons
- Do not place the Cardinal Fruit serif below 33px - it loses its editorial weight at small sizes; switch to Aeonik for anything under 33px
- Do not use gradients, glows, or color tints on buttons or interactive elements - the system is matte and flat
- Do not center-align body copy or product descriptions - the editorial language reads left-aligned with generous left margin

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
