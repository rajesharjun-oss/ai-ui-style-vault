# AI Implementation Prompt

Build a Peggy-inspired interface using this source-derived style bundle.

Reference site: https://peggy.com/royalties
Theme: light
Category: E-commerce
North star: monochrome art gallery on a winter morning - the only color comes from the work on the walls

Use these palette anchors:

- Gallery White `#ffffff` for Card surfaces, input fields, button text on dark fills, nav surface over dark strips
- Canvas Mist `#f4f4f4` for Page background; also functions as the universal hairline border (borderColor 572 occurrences across every context) - the system draws structure with the canvas color itself
- Ink Black `#000000` for Primary text, logo, nav labels, body copy - the strongest type color, never used as a surface
- Charcoal `#141414` for High-contrast neutral action fill for primary buttons on light surfaces.
- Fog `#e2e8f0` for Muted accents, icon fills at rest, secondary surface tint, subtle dividers where Canvas Mist is too light
- Graphite `#666666` for Secondary/muted text - helper copy, metadata in transaction cards, footer body, link at rest

Use these typography anchors:

- Reckless `--font-reckless` for All display and heading copy. Weight 300 at the largest sizes (48-60px) is the signature move - most gallery/marketplace sites use 600-700 serif weights; the light cut reads as editorial restraint rather than shouting authority. Weight 400 takes over for 20-36px subheadings. Line-height collapses from 1.40 at 20px to 1.00 at 60px, letting large display text sit tight like a magazine cover.
- Inter `--font-inter` for All UI chrome: nav labels, button text, body paragraphs, helper copy, card metadata. Inter is deliberately invisible here - it serves Reckless by getting out of the way. Weight 500 appears in nav and active states; 400 is the body default. Line-height opens up to 1.50 at 16px for paragraph readability.
- Monument Grotesk `--font-monument-grotesk` for Footer column labels ('Product', 'Partners', 'Company', 'Support', 'Get the App') and the copyright line. Acts as a structural label typeface - small caps category architecture under a serif body. Strictly 12px, weight 400, used at 11 occurrences, signaling intentional scarcity.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 128px.
- Card padding: 16px.
- Element gap: 16px.

Build these component patterns where relevant:

- Top Navigation Bar: Primary site chrome
- Download App Notification Strip: Dismissible app-promo bar
- Primary Filled CTA Button: Main conversion action (e.g. 'Join Peggy')
- Ghost Text Link: Secondary inline action (e.g. 'Learn more')
- Split Hero Section: Above-the-fold brand statement
- Section Header (Editorial): Introduces an explanatory section
- Royalty Transaction Card: Data row showing a resale payout
- Trust Badge Cell: Reassurance row item (6 across)
- Gallery CTA Panel: Conversion block for gallery partners
- Footer Column: Site map link group
- Footer Copyright Bar: Legal/social strip
- Hero Photograph (Pill-Masked): Artwork/contextual imagery

Do:

- Use Reckless at weight 300 for any display-size heading (48px and above); the light cut is the brand's typographic signature - using 600+ breaks the editorial tone
- Set the CTA background to #141414 with #ffffff text, 0px border-radius, Inter 14px weight 500; this is the only filled button style in the system
- Mask all artwork and lifestyle photography to 9999px border-radius - the pill silhouette is how Peggy signals 'this is art' without color or framing
- Use #f4f4f4 for both the page background AND 1px hairline borders; the canvas color doing double duty as the divider keeps the palette at six colors total
- Reserve Inter for everything below 20px; Reckless handles 20px and up; Monument Grotesk stays at 12px for footer category labels only
- Maintain the monochrome constraint - do not introduce chromatic brand colors, gradients, or colored status pills; trust the artwork to provide color
- Use 128px vertical breathing room between major sections; the page earns its gallery feel through space, not decoration

Avoid:

- Do not add rounded corners (4px, 8px, 12px) to cards, buttons, or inputs - the system is deliberately sharp-edged, reserving curvature for pill-masked photography only
- Do not use colored badges, tags, or status pills (no green for success, no red for error) - the palette is grayscale only; communicate status through text or icon shape
- Do not use Reckless at weight 400 for display-size text; the serif loses its whisper quality and reads as ordinary at 60px
- Do not apply drop shadows, colored glows, or colored borders to elevate cards - elevation is expressed through surface color contrast (#f4f4f4 canvas vs #ffffff card), never through shadow
- Do not place CTAs anywhere except inside the top nav and as the primary action of a section; ghost links handle all secondary actions
- Do not use Monument Grotesk for body copy or headings - it is a 12px label-only typeface; using it elsewhere breaks the typographic hierarchy
- Do not introduce illustrations, icons with chromatic fills, or decorative gradients; the brushstroke curve is the only ornamental element and it should not be replicated

Source prompt cues:

**Quick Color Reference**
- canvas/background: #f4f4f4
- card surface: #ffffff
- primary text: #000000
- muted text: #666666
- border/hairline: #f4f4f4
No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.
- primary action: no distinct CTA color

**Example Component Prompts**

1. *Hero section*: #f4f4f4 background, no border. Left half: display headline 'Artists deserve compensation on every sale of their work' in Reckless 60px weight 300, #000000, line-height 1.00. 24px below: sub-copy in Inter 16px weight 400, #000000, max 2 lines. Right half: full-bleed photograph of a framed artwork in an interior, masked to 9999px border-radius, no caption or border. 128px vertical padding, max-width 1200px centered.

2. *Royalty transaction card row*: four stacked cards on #f4f4f4 canvas. Each card: #ffffff background, 1px #f4f4f4 border, 0px radius, 16px padding. Internal layout: 24px square artwork thumbnail + title in Inter 14px weight 500 (#000000) + 'Sold on {date}' in Inter 12px #666666 on the left; dollar amount in Inter 14px weight 500 (#000000) + 'Royalties Paid' in Inter 12px #666666 on the right. 8px gap between cards.


4. *Trust badge row*: single horizontal row of 6 cells on #f4f4f4 canvas, separated by 1px #f4f4f4 vertical dividers. Each cell: 24px solid #000000 icon centered (lock, shipping box, shield-check, museum frame, dollar bill, person silhouette) above label in Inter 14px weight 500 #000000. No background, no border, no padding on the cell itself.

5. *Footer column*: on #f4f4f4 canvas with a 1px #f4f4f4 top border. Column heading in Monument Grotesk 12px weight 400 #000000. Below: list of links in Inter 14px weight 400 #666666 with 8px row gap. 5 columns total, equal width, 48px horizontal padding.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
