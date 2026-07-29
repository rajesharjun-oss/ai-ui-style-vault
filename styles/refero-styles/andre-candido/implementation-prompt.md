# AI Implementation Prompt

Build a Andre Candido-inspired interface using this source-derived style bundle.

Reference site: https://www.andre-candido.com
Theme: light
Category: Other
North star: Editorial serif on cream paper with one yellow highlighter mark.

Use these palette anchors:

- Ink Black `#111118` for Primary text, nav text, dark footer surface, filled button background, badge fills - near-black with a barely-perceptible cool tint reads as warmer than pure #000 in print contexts
- Paper White `#ffffff` for Page canvas, card surfaces, button text on dark fills, inverted button text - the dominant ground
- Soft Ash `#dddddd` for Muted borders, image placeholder backgrounds, secondary dividers
- Stone Gray `#bdbdbd` for List dividers, body-level borders, tertiary structural lines
- Slate `#7c7c7c` for Helper text, de-emphasized body copy, subtle metadata
- Graphite `#333333` for Link text and link borders in body context - slight lift from pure ink
- True Black `#000000` for Hard border accent in lists and structural dividers where maximum contrast is needed
- Night Forest `#283338` for Navigation-specific borders and text - a cool desaturated charcoal distinct from the warm Ink Black
- Highlighter Yellow `#fef199` for Yellow wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color

Use these typography anchors:

- PP Mori `--font-pp-mori` for Body, nav, UI, and secondary display - the workhorse sans. Weight 200 carries small labels with editorial lightness; 400 is body; 600 is reserved for button text and emphasis. The unusually wide 0.107em letter-spacing on small text (12-15px) gives nav and badges an open, tracked-out feel typical of fashion-editorial UI.
- Editorial New `--font-editorial-new` for Hero and section display headlines only - a thin didone serif at extreme sizes (70-160px) with 1.0 line-height. The whisper-thin weight 200 is the signature: most serif sites use 400-600 for display, this site lets the letterforms almost disappear, making the few words monumental. The contrast between the ultra-thin serif and the heavier PP Mori body creates the magazine-cover tension that defines the brand.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: .
- Section gap: 80-120px.
- Card padding: 24px.
- Element gap: 16-24px.

Build these component patterns where relevant:

- Filled Pill Button (Light): Primary CTA on light backgrounds
- Ghost Pill Button: Secondary action on light backgrounds
- Capsule Link Button: Inline text-link with border treatment
- Work Card: Portfolio project tile in the grid
- About Card (Sidebar): 'Your New Partner' intro block
- Footer CTA Panel: Dark closing section with primary conversion
- Circular Text Badge: Decorative availability indicator (the 'AVAILABLE NOW' element)
- Service/Client Logo Row: Trust strip showing partner brands
- Navigation Bar: Top-level site navigation
- Project Detail Image Card: Large showcase image within portfolio pages
- Headline Display Block: Section-opening serif statement

Do:

- Use Editorial New weight 200 exclusively for display headlines at 48px or larger - never below 48px, never above weight 200
- Keep the page 97% achromatic: Ink Black, Paper White, and grayscale neutrals handle 95% of the visual load
- Apply 0.107em letter-spacing to all PP Mori text at 12-15px - this tracked-out feel is the small-type signature
- Use 24px radius for buttons, 8px for cards, 800px for images - the radius scale is dramatic and must be preserved
- Reserve #fef199 yellow for the dark footer panel only - it is the single chromatic event on the page
- Maintain generous section gaps of 80-120px between major blocks; the airy rhythm is editorial, not compact
- Let display headlines run full-width without max-width constraints; the oversized serif is the layout

Avoid:



Source prompt cues:

primary action: #111118 (filled action)
Create a Primary Action Button: #111118 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
