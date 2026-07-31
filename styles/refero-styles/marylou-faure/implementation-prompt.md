# AI Implementation Prompt

Build a Marylou Faure-inspired interface using this source-derived style bundle.

Reference site: https://maryloufaure.com
Theme: light
Category: Agency
North star: white gallery wall for fearless color

Use these palette anchors:

- Ink `#000000` for All text, hairline borders, nav dividers, the structural skeleton of the page
- Ash `#737373` for Email link, secondary metadata text
- Paper `#ffffff` for Page background, card surfaces - the unbroken gallery wall
- Crimson Pop `#ff0000` for Red wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Bubblegum `#ffbbff` for Illustration surface - flat shapes and product packaging accents
- Cotton Candy `#f7b2de` for Illustration surface - character skin, hair, soft fills
- Sour Grape `#ffa3fe` for Illustration surface and link hover highlight - bright magenta accent within artwork
- Pool Blue `#72c2f2` for Illustration surface - ice, sky, cooling tones in product photography context
- Ice Blue `#96d6ff` for Illustration surface - soft blue fills, atmospheric tones
- Acid Green `#32c24d` for Illustration accent - rare punctuation green in character and product art

Use these typography anchors:

- Helvetica Now `--font-helvetica-now` for The single typeface for everything: nav links, body, project titles, labels. The 600 weight appears only for project section headers; everything else stays at 400. The uppercase letter-spacing (0.0420em) is reserved for the smallest caption-like text - it reads as a label tag, not body copy
- GTStandard-M `--font-gtstandard-m` for GTStandard-M - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: .
- Section gap: 33px.
- Card padding: 30px.
- Element gap: 15px.

Build these component patterns where relevant:

- Top Navigation Bar: Site-wide navigation
- Bio Block: Introduction section beneath nav
- Client Logo Strip: Social proof band
- Project Section Header: Title for each project gallery
- Project Image Grid: Primary content display for portfolio work
- Hero Project Image: First image in each project section
- Email Link: Contact mechanism
- Page Footer: Minimal site closure

Do:

- Keep the page background #ffffff and all structural text #000000 - the interface is monochrome by design
- Use 1px solid #000000 borders as the primary structural element; they replace shadows, cards, and color fills
- Set border-radius to 0 on all images and project grids; only the cart button uses 8px radius
- Set the project title at 40px weight 600 as the only typographic emphasis on the page
- Let illustration imagery carry all chromatic color - never add a colored UI element that competes with the artwork
- Use letter-spacing 0.0420em on the 12px uppercase labels (nav brand, 'Select Clients', 'Personal work', etc.) to give them label-tag presence
- Maintain generous whitespace: 15px between inline elements, 30px padding inside project sections, 33px between major content blocks

Avoid:

- Do not add shadows, gradients, or colored backgrounds to UI containers - the flat hairline-border aesthetic is the signature
- Do not use any chromatic color as a CTA, button fill, or active state - the reds/pinks/blues belong inside illustrations only
- Do not apply border-radius to images, project cards, or thumbnails - only the 8px cart button breaks from sharp edges
- Do not introduce a second typeface or a decorative display font; Helvetica Now at two weights is the whole system
- Do not add hover overlays, zoom effects, or transition animations to project images - they should present flat and direct
- Do not use colored dividers, tinted section backgrounds, or alternating band colors between projects
- Do not add a hero headline, tagline, or marketing block above the fold - the top nav and bio block are the entire intro

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #ffffff
- border: #000000 (1px)
- secondary text: #737373
- primary action: no distinct CTA color

**Example Component Prompts**

1. *Top Navigation Bar*: Full-width white bar, 1px solid #000000 bottom border. Left: 'Marylou Faure' at 12px Helvetica Now weight 400, color #000000, letter-spacing 0.5px. Right: nav links 'Projects', 'Personal', 'About', 'Shop' inline at 12-16px, weight 400, black, no separators, plus a small bag icon at the far right edge. Total height ~40px. No background fill, no shadow.

2. *Project Section Header*: 'Coca-Cola' at 40px Helvetica Now weight 600, color #000000, line-height 0.80, left-aligned. No subtitle, no metadata, no decorative element. Sits directly above the image grid with 15px gap.

3. *Project Image Grid*: Full-width CSS grid, 2-3 columns depending on viewport, images flush against each other with 0px gap and 1px solid #000000 dividers. Images are sharp-edged (border-radius 0), no captions, no hover overlays. Grid fills the entire viewport width edge-to-edge.

4. *Bio Block*: Two-column flex layout. Left column: bio paragraph at 16px weight 400 #000000, then 'Email' caption at 12px uppercase letter-spacing 0.5px, then email address as plain text link with 1px black underline. Right column: two thumbnail images (~150px wide) labeled above with 'Personal work' and 'Shop prints & figurines' in 12px uppercase style. Columns separated by a 1px vertical black rule.

5. *Client Logo Strip*: Single horizontal row, full-width, all logos rendered in monochrome black on white at uniform ~30px height, evenly spaced. Caption 'Select Clients' in 12px uppercase letter-spacing 0.5px sits above the row, left-aligned. No borders, no background, no padding around individual logos.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
