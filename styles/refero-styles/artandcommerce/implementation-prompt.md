# AI Implementation Prompt

Build a Artandcommerce-inspired interface using this source-derived style bundle.

Reference site: https://artandcommerce.com
Theme: light
Category: Agency
North star: art book spread on bone paper

Use these palette anchors:

- Ink `#000000` for Primary text, navigation labels, logo, link borders, footer type - the single graphic ink of the system. Every stroke, border, and character mark across the site
- Bone `#e7e7e7` for Page canvas, card surface, elevated surface - the warm near-white that holds all imagery and text
- Charcoal `#121212` for Secondary text and deep surface tone where slightly softer black is needed against bone

Use these typography anchors:

- Adobe Garamond `--font-adobe-garamond` for Editorial display and body serif. The single weight (400) does all the talking - no bold, no italic reliance. Used at 56px for display headlines (artwork titles, hero captions) with tight tracking -0.018em and 1.10 line-height, at 20px for introductory text and at 16px for body. The restraint of a single weight Garamond at display sizes creates an old-master gravitas: authority through historical type, not weight.
- Akzidenz Grotesk `--font-akzidenz-grotesk` for Functional sans-serif for all UI, navigation, labels, and metadata. Rendered almost exclusively in uppercase at 8-10px with aggressive positive tracking (+0.027 to +0.038em) - the effect is that of gallery wall labels, museum credits, and colophon text. Weight 500 highlights active nav, 700 for emphasis labels, 400 default. The grotesk never competes with Garamond for the reader's attention; it serves.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1440px.
- Section gap: 44px.
- Card padding: 16px.
- Element gap: 12px.

Build these component patterns where relevant:

- Site Header / Nav Bar: Minimal top-bar navigation
- Full-Bleed Editorial Image: Hero / feature artwork display
- Image Credit Caption: Attribution line below full-bleed images
- Magazine Cover Card: Featured publication / project cover
- Navigation Link: Header nav item / inline link
- Footer: Site footer with secondary nav and credits
- Artwork Title: Large display heading for project or feature
- Section Label: Uppercase category / context label

Do:

- Use only #000000, #e7e7e7, and #121212 - no other colors, no tints, no accents
- Set display headlines in Adobe Garamond 400 at 56px with letter-spacing -1.0px and line-height 1.10
- Render all UI labels, nav, and metadata in Akzidenz Grotesk uppercase with letter-spacing 0.027-0.038em
- Keep all border-radius at 0px - every card, image, button, and badge is sharp-edged
- Use 12px and 16px as the dominant element gaps; 44px as the standard section gap
- Let images bleed edge-to-edge with no borders, shadows, or rounded corners
- Use a 1px Ink (#000000) border-bottom to denote hover and active states on links and nav

Avoid:

- Do not introduce any color - no brand accent, no CTA fill, no gradient, no status hues
- Do not use Garamond bold or italic; the serif speaks only at weight 400
- Do not apply border-radius to any element; the design is rigorously rectilinear
- Do not add box-shadows or drop-shadows - elevation is expressed through whitespace alone
- Do not mix sentence case into nav and labels; all Grotesk UI is uppercase
- Do not center body text or nav; the layout is flush-left with content anchored to the left edge
- Do not use display sizes below 56px or body sizes above 20px for Garamond - the scale is deliberately compressed

Source prompt cues:

**Quick Color Reference:**
- text: #000000
- background: #e7e7e7
- border: #000000
- accent: none (monochrome only)
- primary action: no distinct CTA color

**Example Component Prompts:**
1. Build a full-bleed hero image section: edge-to-edge image on #e7e7e7 canvas, 0px radius, no shadow, no border. Below the image, a caption row spanning the full width: left-aligned artist credit in Adobe Garamond 400 16px #000000, right-aligned project tag in Akzidenz Grotesk 500 uppercase 10px #000000 letter-spacing 0.033em. 44px vertical gap above the caption.

2. Build a centered magazine cover card: single image centered horizontally on #e7e7e7, no border, no shadow, 0px radius, 44px top and bottom padding. No text overlays on the card itself - the cover is the content.

3. Build a site header nav bar: #e7e7e7 background, full-width, 16px horizontal padding, ~44px tall. Logo 'art+commerce' in Adobe Garamond 400 16px #000000 flush left. Nav items (ARTISTS, IMAGE ARCHIVE, PROD, NEW LIGHT FILMS, EDITIONS, ABOUT, SHOP) in Akzidenz Grotesk 500 uppercase 10px #000000 letter-spacing 0.033em, 16-23px gaps, flush right. 1px #000000 bottom border on hover only.

4. Build a section label: Akzidenz Grotesk 700 uppercase 8px #000000, letter-spacing 0.38em, 12px bottom margin. Reads as a printed colophon stamp.

5. Build a display headline: Adobe Garamond 400 56px #000000, line-height 1.10, letter-spacing -1.0px, flush left. No bold, no italic. Sits on #e7e7e7 with 44px breathing room above and below.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
