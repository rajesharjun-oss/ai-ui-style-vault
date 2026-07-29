# AI Implementation Prompt

Build a Daniel Triendl-inspired interface using this source-derived style bundle.

Reference site: https://www.danieltriendl.com
Theme: light
Category: Agency
North star: White gallery wall for loud art

Use these palette anchors:

- Obsidian `#000000` for Primary text, hairline borders, avatar stroke, ghost button outlines - the only ink on the page; borders are the structural device, not shadows
- Canvas White `#ffffff` for Page background, card surface, nav fill - the gallery wall itself
- Plaster Gray `#f2f2f2` for Pill navigation background, subtle surface for tag chips, soft section washes
- Ash Gray `#9b9b9b` for Muted secondary text, caption labels under illustrations, hairline borders on less prominent elements

Use these typography anchors:

- Times `--font-times` for Body, captions, labels, links, footer - a deliberate serif choice for UI body copy, the kind of editorial-museum-label voice most portfolios replace with sans-serif
- UniversalSans 425 `--font-universalsans-425` for Headings, emphasized body, link text - a neutral grotesque that steps in when the Times serif is too quiet
- UniversalSans 625 `--font-universalsans-625` for Button text, nav labels, small caps - the only medium weight in the system, used exclusively for clickable elements to give them a slightly firmer voice
- Rza `--font-rza` for Brand wordmark / logo only - a custom display face that gives the header a distinct editorial signature, never used elsewhere

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1440px.
- Section gap: 48-64px.
- Card padding: 20px.
- Element gap: 6-8px.

Build these component patterns where relevant:

- Illustration Thumbnail Card: Primary content unit - each piece of portfolio work
- Ghost Header Button: Top-right navigation (Explore, Index)
- Floating Pill Navigation: Sticky bottom-center nav (Work, About, Contact)
- Avatar + Brand Mark: Top-left site identity
- Hash Tag Label: Metadata under each illustration (medium, style)
- About Block: Self-description in a featured grid cell
- Newsletter / Stay-up-to-date Block: Audience engagement cell in the grid
- Image Border / Frame: Hairline border around images in lists and cards

Do:

- Keep the canvas pure white (#ffffff) - the illustrations provide all color, the UI must not compete
- Use Times 14px for body, captions, and labels; switch to UniversalSans 425 only for headings or emphasized runs
- Frame every image with a 1px #000000 hairline - the black border IS the visual device, not shadows
- Round interactive elements (buttons, pills) to 48px for full pill shape; round image cards to 10px
- Use #f2f2f2 exclusively for the floating pill nav and soft tag chips - never for page sections
- Set body and caption text at exactly 14px / 1.2 line-height / -0.14px letter-spacing - the compactness is deliberate
- Let the Rza wordmark appear exactly once, in the header - it is the only display moment in the system

Avoid:

- Do not introduce any chromatic UI color - green, red, blue, or accent hues - the palette is black/white/gray by design
- Do not add box-shadows to illustration cards; the single shadow allowed is the floating pill nav (rgba(0,0,0,0.1) 0px 4px 4px)
- Do not use Times for headings at large sizes; it is a 14px label face, not a display face
- Do not mix Rza into body copy or labels - it lives only in the brand wordmark
- Do not use #9b9b9b for body text on white - it fails contrast (2.8:1); reserve it for meta/tags on black or as a hairline border
- Do not add padding or chrome around illustration images - the image fills its grid cell edge-to-edge
- Do not create filled buttons; every interactive element is ghost/outlined (#000000 border, no fill)

Source prompt cues:

Quick Color Reference:
- text: #000000
- background: #ffffff
- surface (pills/tags): #f2f2f2
- muted text / hairline border: #9b9b9b
- border (primary structural): #000000
- primary action: no distinct CTA color

Example Component Prompts:
1. Illustration Thumbnail Card: edge-to-edge image with 1px #000000 border and 10px radius. Title below in Times 14px #000000, line-height 1.2, letter-spacing -0.14px. Tag row beneath in Times 14px #9b9b9b, tags separated by single spaces, each prefixed '#'. No card padding, no shadow, no background fill.
2. Ghost Header Button: 1px #000000 border, 48px full-pill radius, 10px vertical / 20px horizontal padding. Label in UniversalSans 625 at 14px #000000, letter-spacing -0.14px. Optional small icon to the left. No fill, no shadow.
3. Floating Pill Navigation: single pill container with 48px radius, #f2f2f2 fill, 8px vertical padding, containing three labels (Work / About / Contact) in UniversalSans 625 at 14px #000000 separated by 16px. Subtle drop shadow rgba(0,0,0,0.1) 0px 4px 4px. Fixed to bottom-center of viewport.
4. Avatar + Wordmark Header: 24px circular avatar followed by 'Daniel Triendl' in Rza 24px / line-height 1.17 / letter-spacing -0.144px, color #000000. Left-aligned, single line.
5. About Text Block: white card, no border, no shadow. 'About' label in Times 14px #000000 on top. Body copy in Times 14px #000000, 1.2 line-height. 'Find out more' link in UniversalSans 425 at 14px #9b9b9b below.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
