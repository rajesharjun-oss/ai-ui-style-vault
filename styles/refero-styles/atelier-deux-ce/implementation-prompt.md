# AI Implementation Prompt

Build a Atelier Deux-Ce-inspired interface using this source-derived style bundle.

Reference site: https://deux-ce.com
Theme: light
Category: Agency
North star: Sunlit editorial gallery

Use these palette anchors:

- Ink Black `#000000` for Body text, headings, nav links, hairline borders, and link underlines - the single type color across the entire system
- Canvas White `#ffffff` for Page background, card surfaces, reverse text on dark photographic regions
- Warm Linen `#eee5da` for Soft section background, the first step off pure white - gives a page the warmth of unbleached paper
- Pale Sage `#d8ddc6` for Tinted section panels, the dominant non-white canvas tone
- Driftwood `#d8d0c5` for Deeper warm section background, used when a panel needs to recede from Pale Sage
- Olive Stone `#afb371` for Saturated warm section background - the deepest neutral step before any chromatic color enters
- Weathered Taupe `#9c978a` for Muted section background, used sparingly as a quieter alternative to Olive Stone
- Soft Pebble `#aaaaa4` for Light warm-gray section background, the coolest of the earth-tone neutrals
- Garden Green `#259558` for Footer background only - the single chromatic accent in the system, used as a deliberate closing beat rather than a brand color spread across the UI

Use these typography anchors:

- Helvetica `--font-helvetica` for Primary UI and editorial type - body copy, navigation, links, project captions, category filters, and all functional text. Weight 400 for body and metadata, weight 600 reserved for the wordmark and the few moments that need emphasis. The system stack ensures identical rendering across platforms without depending on a webfont.
- minion-3 `--font-minion-3` for Editorial accent serif - used for body paragraphs and select headings where a literary, book-page quality is desired. The contrast between this transitional serif and the geometric Helvetica mirrors the brand's positioning: strategy + craft, editorial + commercial.

Use these layout rules:

- Base spacing: 6px.
- Density: comfortable.
- Page max-width: .
- Section gap: 48px.
- Card padding: 0px.
- Element gap: 24px.

Build these component patterns where relevant:

- Split-Screen Hero: Full-bleed opening composition that pairs two photographs meeting at a hard vertical center seam
- Hero Caption Label: Small editorial caption floating over a hero image - project credit, model, location
- Wordmark + Hamburger Navigation: Minimal global navigation - brand wordmark on the left, single hamburger icon on the right
- Editorial Body Text Block: Long-form descriptive paragraph used for the 'What we do' and similar sections
- Category Filter List: Inline multi-row list of project categories with item counts, acting as a navigation index
- Project Card: Image-forward project entry in the 2-column portfolio grid
- Read More Link: Text link ending an editorial paragraph
- Footer Banner: Full-bleed closing band of the page
- Inline Section Label: Small uppercase tag identifying a section ('WHAT WE DO')

Do:

- Let full-bleed photography drive every primary screen - type and chrome are captions, not the subject
- Stack sections using the warm neutral scale (Canvas White Warm Linen Pale Sage Driftwood Olive Stone) to create rhythm without shadows
- Use the two type families in deliberate contrast: Helvetica for functional UI and metadata, minion-3 for editorial body paragraphs and book-page moments
- Apply letter-spacing 0.02em to body and 0.04em to navigation, labels, and uppercase tags across both type families - this slightly positive tracking is the system's quiet signature
- Keep all component radii at 0px - the design is print-flat, not card-lifted
- Reserve Garden Green (#259558) exclusively for the footer - do not introduce it as a button, link, or accent elsewhere
- Set the type scale at 16 / 17 / 20 / 24px only - a compressed scale is a discipline, not a limitation

Avoid:

- Do not add box-shadows, drop shadows, glows, or gradient overlays - hierarchy comes from color and image, never from elevation
- Do not introduce saturated colors beyond the single footer green - the palette is warm earth tones, period
- Do not round corners on cards, buttons, images, or tags - 0px radius is non-negotiable
- Do not use filled buttons, ghost buttons, or pill buttons - the system has no button component, only text links and the footer band
- Do not use icons beyond a single minimal hamburger - the site is image-led, not icon-led
- Do not set type in negative letter-spacing - the positive 0.02-0.04em tracking is a defining choice and must not be tightened
- Do not add decorative borders thicker than 1px hairlines, and never use border colors outside the neutral scale

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
