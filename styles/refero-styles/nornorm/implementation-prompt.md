# AI Implementation Prompt

Build a Nornorm-inspired interface using this source-derived style bundle.

Reference site: https://nornorm.com
Theme: light
Category: Other
North star: Scandinavian showroom, cobalt punctuation - a white-walled furniture gallery where one deep blue stroke cuts through warm bone and ink.

Use these palette anchors:

- Canvas White `#ffffff` for Page background, card surfaces, button text on cobalt, nav background, image backgrounds
- Bone `#f1efe9` for Warm off-white surface for section bands, feature card panels, and soft contrast zones against pure white
- Ash `#ececec` for Subtle elevated surface and neutral button fill for low-emphasis controls
- Stone `#6a6a6a` for Secondary body text, helper copy, nav muted labels, and dividers - the warm mid-gray that gives body text hierarchy without competing with the brand accent
- Graphite `#333333` for Hairline borders and structural dividers
- Ink `#1f1d1e` for Slightly warm near-black for body and heading text - a softer alternative to pure black that matches the warm bone surface
- Obsidian `#000000` for Primary text, nav text, strong borders, and the ghost button outline - the typographic workhorse
- Cobalt Ink `#1e37a0` for Violet outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color

Use these typography anchors:

- Lunar `--font-lunar` for Single-family geometric sans used for everything from 14px nav labels to 112px hero display. The tight universal tracking of -0.03em is the signature - it tightens every size equally, so body text feels editorial and display text feels architectural rather than decorative. Weight 500 carries body emphasis, weight 700 is reserved for numbered list items and UI labels.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1280px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 16px.

Build these component patterns where relevant:

- Primary CTA Button: Filled action button for the main conversion on each page
- Ghost Button: Secondary action that pairs with a primary CTA
- Nav Link: Top navigation menu items with optional dropdown caret
- Logo Wordmark: Brand identifier in the top-left of every page
- Language Switcher: Globe icon + region label in the top-right nav
- Hero Overlay: Full-bleed photographic hero with centered text block
- Client Logo Strip: Social proof band directly under the hero
- Feature Card: 4-column grid item in the 'Why Subscribe' section
- Section Header: Centered title block for content sections
- Image Gallery Carousel: Full-bleed horizontal photo strip showing client office spaces
- Gallery CTA Link: Text link to enter a full gallery view
- Carousel Nav Button: Circular prev/next controls for image carousels

Do:

- Use Lunar at every size with -0.03em letter-spacing - the universal tracking is the brand's typographic signature, not optional
- Use Cobalt Ink (#1e37a0) only for the logo wordmark, primary filled CTA buttons, and active states - never as a background fill, icon color, or decorative accent
- Pair every Primary CTA with a Ghost Button beside it: the two-button pattern is the system's standard conversion unit
- Use 9999px radius on all buttons, tags, and pill controls - there is no rounded-corner alternative in the system
- Use 8px radius for image-less cards and content containers; leave photographic content with sharp 0px edges so the images read as full-bleed editorial
- Build section backgrounds from Canvas White (#ffffff) and Bone (#f1efe9) only - never introduce a new tint
- Use 16px or 24px as the gap between text and its adjacent control; 48px between stacked text blocks; 80px between sections

Avoid:

- Do not introduce a second chromatic color - the system's authority comes from a single accent against monochrome
- Do not use shadows, glows, or any box-shadow on cards, buttons, or modals - the system is deliberately flat
- Do not use a filled neutral button (gray, black, or bone) as a primary action - the only filled button is Cobalt Ink on white
- Do not break the -0.03em letter-spacing at any size, including body copy and captions - looser tracking reads as a different typeface
- Do not add borders to feature cards, image containers, or section bands - the warm white-to-bone contrast carries separation
- Do not use gradients on backgrounds, buttons, or text - the palette has no gradient tokens and adding one would break the Scandinavian restraint
- Do not round the corners of large photographs, hero images, or gallery images - editorial content stays sharp-edged to contrast with the pill-shaped UI controls

Source prompt cues:

**Quick Color Reference**
- text: #000000 (primary) / #6a6a6a (secondary) / #ffffff (on dark or cobalt)
- background: #ffffff (canvas) / #f1efe9 (bone section)
- border: #000000 (structural) / #e5e5e5 (hairline on white controls)
- accent: #1e37a0 Cobalt Ink (logo, active state, link emphasis only)
- primary action: no distinct CTA color

**Example Component Prompts**
No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.
2. Build a 4-column feature grid on a white #ffffff canvas. Each card: square image at top with 0px border-radius, then Lunar 20px weight 700 '01.' through '04.' in #000000, then heading at Lunar 20px weight 500 #000000, then body copy Lunar 16px weight 400 #6a6a6a. 24px gap between image and text, 32px column gap.
3. Build a centered section header: Lunar 48px weight 400 #000000 heading with -1.44px letter-spacing, optional Lunar 20px weight 400 #6a6a6a subhead directly below with 8px gap. 64px bottom margin to the content. No decorative element.
5. Build a client logo strip: white background, single row of 8 grayscale logos at uniform 24px height, evenly distributed across the full 1280px content width, 60% opacity to read as secondary social proof.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
