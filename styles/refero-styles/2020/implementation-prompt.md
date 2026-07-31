# AI Implementation Prompt

Build a 2020-inspired interface using this source-derived style bundle.

Reference site: https://albumcolors.com
Theme: light
Category: Media
North star: Solid color poster wall. A single saturated color fills the viewport like painted drywall, and massive black type sits on top as if stenciled.

Use these palette anchors:

- Signal Orange `#e4822e` for Primary canvas - the full-viewport page background that changes on refresh; this is the design system
- Olive Ink `#4f503e` for Primary text, headline color, and the only outlined action accent (outlined-button borders, link underlines) - warm dark green-brown that pairs with the orange field without competing chroma
- Oxblood `#b13225` for Alternating surface variation - one of the page colors the background can take on refresh
- Burnt Sienna `#c97f40` for Alternating surface variation - secondary warm shade the canvas can adopt
- Near Black `#081618` for Alternating surface variation - deep cool surface the canvas can adopt, creates the darkest mode of the page
- Pearl `#feccc0` for Soft warm highlight - one of the lighter surface variations the canvas can adopt
- Sage Mist `#99aa91` for Soft cool surface variation - one of the muted color states the canvas cycles through
- Carbon `#000000` for Album cover backgrounds, deep text on light surface states
- Ink `#161616` for Album cover backgrounds and heavy dark surface tone
- Charcoal `#111111` for Album cover and card backgrounds within the grid
- Ash `#8d8d8d` for Mid-neutral for muted helper text and secondary surface states
- Paper `#ffffff` for Album cover backgrounds, text on dark surface states

Use these typography anchors:

- Helvetica LT Pro `--font-helvetica-lt-pro` for The sole typeface across all text - display, heading, body, button, link. A single weight (400 regular) is used at every scale, which is the most distinctive typographic choice on the site. The whisper-regular giant-size headlines are anti-convention; most poster/editorial sites use 700-900 for display type, and using the book weight at 137px makes the headline feel stamped rather than shouted - authority through stillness.
- Helvetica `--font-helvetica` for Helvetica - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: .
- Section gap: 20px.
- Card padding: 0px.
- Element gap: 20px.

Build these component patterns where relevant:

- Display Headline Block: The page-defining typographic element - site title rendered as a monolithic shape
- Section Subtitle: Short descriptive line that sits directly under the display headline
- Album Cover Tile: Unframed square image in the content grid
- Refresh Record Button: The only interactive control - a small circular record/disc icon that triggers a full page color change
- Rotated Side Label: Vertical instructional text - tells the user the page mechanic
- Outlined Action Border: Chromatic border treatment for interactive elements (links, tags, light buttons)
- Body Caption: Small helper text used in metadata, tags, or footnotes
- Subheading Link: In-text or tag-style link element

Do:

- Set display headlines at 137px / line-height 0.79 / letter-spacing -0.05em in Helvetica LT Pro 400 - never bump the weight, the book weight is the signature
- Use Olive Ink (#4f503e) for all text and borders regardless of canvas color - the text must always be the same dark warm tone so the changing background feels like a single identity expressing different moods
- Let the page canvas fill 100% of the viewport edge-to-edge with no container, no max-width, no margin - full-bleed is non-negotiable
- Use 20px as the only spacing unit - vertical rhythm between the headline, subtitle, and grid is always 20px
- Keep all radii at 0px - album tiles, buttons, and tags are sharp-cornered; the colored field provides all the softness the page needs
- Treat the canvas color as the primary navigation: the user changes the page by changing the background, not by clicking links
- Set every text element in a single weight (400) - do not introduce bold, medium, or light variants

Avoid:

- Do not use filled buttons - a solid fill would compete with the canvas color; all actions are outlined borders or pure icons
- Do not add card frames, drop shadows, or elevation to album tiles - they sit directly on the canvas with no chrome
- Do not introduce a second typeface - the entire site is set in one family at one weight
- Do not center body text - copy aligns left, full-bleed, and wraps naturally
- Do not use a max-width container - the layout is always edge-to-edge
- Do not pair Olive Ink (#4f503e) text with a colored background outside the established palette (oxblood, sienna, near-black, sage, pearl) - the six surface colors are the only valid canvases
- Do not add line-height above 1.0 for any size above 21px - the tight leading (0.79-0.80) on display text is what makes the headlines feel like solid shapes

Source prompt cues:

**Quick Color Reference**
- text: #4f503e (Olive Ink)
- background: #e4822e (Signal Orange) - changes on refresh
- border: #4f503e (Olive Ink, 1px)
- accent: #b13225 (Oxblood) / #c97f40 (Burnt Sienna) / #081618 (Near Black) - alternative canvas states
- surface: #ffffff (Paper) for light album tiles, #000000 (Carbon) for dark album tiles
- primary action: no distinct CTA color

**Example Component Prompts**
1. Build the page hero: full-bleed Signal Orange (#e4822e) background, no padding, no container. Display headline 'ALBUM COLORS OF THE YEAR 2020' in Helvetica LT Pro 400 at 137px, line-height 0.79, letter-spacing -0.05em, color Olive Ink (#4f503e). Text fills width edge-to-edge, wrapping naturally. A 21px Olive Ink subtitle sits 20px below.
2. Build a single album tile: 1:1 aspect ratio, 0px border-radius, no border, no shadow, no padding. Sits directly on the canvas with 20px gap to neighbors. Image fills the tile.
3. Build the refresh button: top-right corner, 20px from edges, Olive Ink (#4f503e) disc icon on the orange canvas. No border, no background, icon only.
4. Build the rotated side label: positioned flush to the right viewport edge, text rotated 90 reading bottom-to-top, Helvetica LT Pro 400 at 16px, line-height 1.6, letter-spacing -0.05em, color Olive Ink (#4f503e).
5. Build the album grid: uniform columns of square tiles, 20px gap, no outer padding, tiles bleed to the viewport edges. Mix of Paper (#ffffff) and Carbon (#000000) backgrounds depending on cover content.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
