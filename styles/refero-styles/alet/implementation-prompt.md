# AI Implementation Prompt

Build a alet-inspired interface using this source-derived style bundle.

Reference site: https://aletagency.com
Theme: light
Category: Agency
North star: Vintage editorial contact sheet on warm taupe paper.

Use these palette anchors:

- Taupe Paper `#ada59b` for Full-page canvas, the single dominant surface - every section and component sits on this warm gray, never on white or near-black. The warm undertone (vs cool slate) is what makes the whole site feel like printed stock rather than a digital UI
- Ink Black `#000000` for Primary text, all borders, all hairlines, all SVG strokes. Used at full opacity - no softened text grays, no 80% black. The crispness against warm taupe creates the magazine-printed feel
- Charcoal `#252525` for Navigation text and the nav underline borders. Slightly softer than pure ink for the persistent top-of-page chrome so the nav recedes behind the work
- Graphite `#101010` for Secondary text and supporting borders where Charcoal reads too soft but pure Ink is too loud. The single mid-step between nav and body
- Stone `#454545` for Occasional inset surface for body-level containers - the only tonal step above the canvas, used sparingly for any small frame or block that needs to separate from the page without introducing color
- Press Black `#060506` for Fine SVG illustration stroke - near-identical to Ink Black but kept distinct in the source. Use for line-art icons and decorative vector marks

Use these typography anchors:

- WorkSans `--font-worksans` for All UI chrome: navigation, category labels, body copy, metadata, toggle text. Deliberately tiny - 11-13px forces an editorial intimacy and keeps the page from feeling like a product interface. Set in Work Sans Regular at default tracking; the small size is what makes it feel like print captions rather than web UI.
- SilkSerif `--font-silkserif` for The ALET wordmark and any other serif display moment. Light weight at 23px with tight leading (0.94) and extremely wide letter-spacing - the letters almost float apart. The serif is the only non-sans on the site, which is what makes the brand mark readable as a masthead rather than a wordmark.

Use these layout rules:

- Base spacing: 6px.
- Density: comfortable.
- Page max-width: .
- Section gap: 101-180px.
- Card padding: 0px.
- Element gap: 11-23px.

Build these component patterns where relevant:

- Editorial Image Tile: The work - photography placed on the taupe canvas in an asymmetric scattered grid
- Floating Category Label: Anchors the image grid - names the discipline (GRAPHIC DESIGN, SOCIAL MEDIA, ART DIRECTION, etc.)
- Corner Nav Link: Primary navigation - top-left and top-right clusters
- ALET Wordmark: Centered masthead in the top bar - the only serif on the site
- Layout Toggle: Switches the image grid between LINEAR and RANDOM arrangement
- Studio Statement: Centered editorial blurb below the image field
- Hairline Divider: Section separation
- Pill Container: Rare surface for a small inline element (e.g. the toggle track)

Do:

- Use #ada59b as the page canvas for every section, every page, every state - the taupe paper is the brand
- Set all UI text at 11-13px in Work Sans Regular; never scale up to 14-16px for a 'primary' label
- Set the ALET wordmark in Silk Serif Light at 23px with letter-spacing opened to ~0.5em
- Use #000000 for all text, borders, and SVG strokes at full opacity - no softened blacks
- Place photographs at 0px radius, no border, no shadow - let the image edges meet the canvas directly
- Use 9999px radius only for the layout-toggle pill; 10.8px only for tiny inset frames; everything else stays sharp
- Keep section gaps in the 101-209px range - the page breathes like a printed spread, not a dashboard

Avoid:

- Do not introduce any chromatic color - no accent, no CTA fill, no status greens/reds/blues
- Do not use white, off-white, or near-black as a section background - the taupe canvas is the only surface
- Do not add box-shadows, elevation, or gradient fills to any component
- Do not use a sans-serif for the wordmark or any display moment - Silk Serif is the only serif and the only size above 13px
- Do not round image corners or wrap photographs in cards with fills or borders
- Do not center body text in narrow columns - the studio statement is the only centered block, and it spans a wide measure
- Do not use large display weights (600-700) - the system runs entirely on Regular and Light

Source prompt cues:

Quick Color Reference:
 text: #000000
 background: #ada59b
 border: #000000
 accent: none - there is no accent color in this system
 primary action: no distinct CTA color

Example Component Prompts:

1. Create a top navigation bar on a #ada59b full-bleed canvas. Left cluster: 'OUR WORK' at 11px Work Sans Regular, #252525, uppercase, letter-spacing normal. Center: the word 'ALET' set in Silk Serif Light, 23px, #000000, line-height 0.94, letter-spacing roughly 0.5em so the letters are widely separated. Right cluster: 'ABOUT PROCESS CONTACT' at 11px Work Sans, #252525, with 36px gaps between links. No background fill, no border on the bar itself - it floats directly on the taupe canvas.

2. Create an editorial image grid section on #ada59b. Place 6-8 photographs at varying aspect ratios (roughly 1:1, 4:5, 3:2) with marginLeft and marginTop offsets between 101px and 209px so the grid reads scattered and asymmetric, not column-aligned. Each image is 0px border-radius, no border, no shadow. Surround the grid with floating category labels in 11px Work Sans, #000000, uppercase, positioned at irregular coordinates: 'GRAPHIC DESIGN' top-left, 'SOCIAL MEDIA' top-center, 'ART DIRECTION' top-right, 'COPYWRITING' bottom-left, 'PHOTOGRAPHY & FILM' bottom-center, 'CREATIVE CONSULTANCY' bottom-right.

3. Create a layout toggle component on the #ada59b canvas: the word 'LINEAR' on the left, 'RANDOM' on the right, both at 11px Work Sans uppercase #000000, flanking a 9999px-radius pill track (roughly 28px wide x 14px tall) drawn with a 1px #000000 stroke, transparent fill. A small circular thumb (~10.8px diameter) sits inside the track, also 1px #000000 stroke, no fill.

4. Create a studio statement block centered below the image grid. Single paragraph, 13px Work Sans Regular, #000000, line-height 1.5, centered, sitting directly on the #ada59b canvas with roughly 180px of padding above. No container, no border, no background.

5. Create a small pill tag component for inline use: 1px #000000 stroke, 9999px radius, transparent fill on #ada59b, 11px Work Sans Regular #000000 text inside, 5px vertical and 11px horizontal padding. No fill states - the pill remains outline-only at rest and on hover.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
