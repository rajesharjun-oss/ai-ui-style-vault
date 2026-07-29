# AI Implementation Prompt

Build a ORYZO AI-inspired interface using this source-derived style bundle.

Reference site: https://oryzo.ai
Theme: dark
Category: Design
North star: Darkroom product editorial. A lone object floating in warm darkness, cream typography the only decoration.

Use these palette anchors:

- Warm Cream `#ffedd7` for Light text on dark surfaces, inverse labels, and high-contrast captions.
- Walnut Shadow `#100904` for Page canvas and deepest background - warm near-black, not pure black. The void behind every product reveal
- Bark Brown `#382416` for Elevated surface and filled button background - the one chromatic step above the canvas, used for the single solid CTA
- Cork Border `#40372e` for Hairline dividers, dashed section separators, subtle container borders - warmer than the canvas by one step
- Driftwood `#6c5f51` for Mid-tone warm gray for secondary dividers and muted structural elements - the bridge between Bark and Cream
- Ember Accent `#dc5000` for Orange text accent for links, tags, and emphasized short phrases.
- Pure Black `#000000` for SVG icon fills and decorative vector elements only - never used as a background or text color

Use these typography anchors:

- halyard-display-variable `--font-halyard-display-variable` for The only typeface. Weight 500 at 51px drives display headlines with extreme uppercase confidence; the same family at weight 400 / 29px becomes the system's sole mixed-case body voice. Letter-spacing stays normal - the geometric forms do the work without tightening. Substitute: 'Inter', 'Sohne', or 'Neue Haas Grotesk' for close structural match.
- Arial `--font-arial` for System fallback for micro-legal labels (8px uppercase credits like "* ADOBE ILLUSTRATOR"). Not a design choice - a necessity for system-rendered disclaimers.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: .
- Section gap: .
- Card padding: 24px.
- Element gap: 18px.

Build these component patterns where relevant:

- Pill Button (Filled): Primary solid CTA - used once on the page for the Lusion studio link
- Outlined Ghost Button: Secondary action or decorative button - cream border on transparent fill
- Underline Text Link: Inline links and navigation items - borderless, relying on underline
- Input Field (Underline Only): Minimal form input - bottom border only, no full outline
- Fixed Top Navigation: Persistent site navigation - minimal, 4 items, uppercase micro-type
- Vertical Sidebar Label: Edge branding - vertical text running down the right margin
- Logo Wordmark: Brand identifier - the only graphical mark
- Hero Overlay Info Card: Semi-transparent attribution card in the hero
- Product Reveal Section: Full-viewport void-mode section - centered 3D render with flanking text
- Section Divider (Dashed Hairline): Visual separator between content blocks
- Video Thumbnail Card: Embedded video preview with play indicator
- Legal/Disclaimer Text: System-rendered micro-copy in Arial 8px

Do:

- Set all UI text in #ffedd7 (Warm Cream) - never use pure #fff; the warm tint is the system's signature.
- Use #dc5000 (Ember) only for credit lines, the "Built by" label, and the Lusion studio link - a single accent earns its rarity through restraint.
- Set type in uppercase weight 500 across the entire interface; use weight 400 / mixed case only for the 29px body copy that explains the product.
- Use 36px border-radius for the one filled CTA and 22.5px for outlined ghost buttons; 12px for cards; 0px for inputs and inline links - these four values are the entire radius vocabulary.
- Set section gaps at 100vh - each section gets its own full viewport, never compress product reveals into bands.
- Use 1px dashed lines in #40372 for section dividers; avoid solid dividers and avoid any divider thicker than 2px.
- Center the 3D product render in every void-mode section with text flanking symmetrically left and right at 18px gutters.

Avoid:

- Never use pure #fff for text or #000 for backgrounds - the warm cream and walnut shadow are the system; purity reads as wrong here.
- Never apply #dc5000 to buttons, CTAs, or interactive surfaces - the orange is editorial credit only.
- Never use lowercase or sentence-case for headings, nav, or labels; the only mixed-case text is the 29px body description.
- Never add drop shadows to cards, buttons, or sections - depth comes from the two-step surface stack (#100904 #382416), not from blur.
- Never use border-radius below 12px on containers - the geometry is deliberately chunky, not sharp.
- Never use more than one filled button per section; restraint is the design language.
- Never center-align body copy - headings and body text are always left-aligned, even when flanking a centered image.

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
