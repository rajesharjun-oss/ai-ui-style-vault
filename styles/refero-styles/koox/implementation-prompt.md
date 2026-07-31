# AI Implementation Prompt

Build a Koox-inspired interface using this source-derived style bundle.

Reference site: https://koox.co.uk
Theme: light
Category: E-commerce
North star: Brutalist cold-press lab - white tile, sticker print, stencil voice.

Use these palette anchors:

- Tile Grout `#d25a24` for Signature brand border and link accent - orange tile-line strokes that frame cards, links, and section edges with the warmth of fired clay against the clinical white canvas
- Cold-Press Green `#113722` for Primary action fill - the dark botanical green of filled CTA buttons, footer band, and category button backgrounds, signaling the product inside without resorting to food-photo greens
- Sticker Crimson `#6b1229` for Hard-offset shadow accent - deep burgundy that throws a zero-blur 5px shadow under stickers and emphasized buttons, turning flat elements into screen-print layers peeled onto the page
- Noir `#000000` for Navigation, body text, and default border color - the unyielding black that carries every paragraph, icon stroke, and card hairline
- Glacial White `#ffffff` for Page canvas, card surface, and reverse text on dark nav and green CTAs - the clinical white tile of the entire system
- Ash `#efefef` for Soft card border and subtle fill - the gray grout between white surfaces, used for hairline dividers and recessed card frames
- Char `#232323` for Heading color and deep-surface accent - nearly-black tone for the heaviest display text and occasional dark bands
- Concrete `#cccccc` for Mid-gray utility border and muted body text - quieter dividers where full black would be too loud
- Fog `#d7d7d7` for Input field border - neutral resting-state outline for form fields
- Slate `#646464` for Input text and icon fill - secondary legibility gray for form labels and small icon detail
- Pewter `#808080` for Decorative low-emphasis border and text - rarely used, appears on tertiary UI marks

Use these typography anchors:

- Helvetica `--font-helvetica` for All UI and editorial text. The choice of system Helvetica is deliberate - it reads as lab-label stencil rather than fashion-serif sophistication. Weight 900 headlines shout at 40-48px in all-caps with positive tracking, weight 400-500 carries body copy at 14-18px. No custom display face: the system itself is the brand.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 40-60px.
- Card padding: 20px.
- Element gap: 20px.

Build these component patterns where relevant:

- Top Navigation Bar: Persistent site navigation
- Hero Image Section: First-screen brand and product statement
- Primary CTA Button (Filled Green): Main conversion action
- Sticker Button (Burgundy Shadow): Emphasized action with screen-print offset
- Ghost / Outline Button: Secondary action
- Marquee Quality Bar: Repetitive brand-attribute ticker
- Category Tile Card: Product category entry point
- Star Rating Display: Social proof inline component
- Bordered Link: Inline text or nav link with frame
- Hairline Divider: Section and grid separator
- Footer Band: Site footer with promotional message
- Form Input: Text input for forms

Do:

- Use Helvetica at weight 900 for all display headlines at 40-48px, all uppercase, with positive letter-spacing between 0.8px and 0.96px
- Frame cards, links, and category tiles with 1-2px #d25a24 (Tile Grout) borders and 5px radius to reinforce the subway-tile language
- Apply the #6b1229 hard-offset shadow (5px 5px 0px 0px, zero blur) only to sticker-style buttons and emphasized links - never use it as a generic elevation
- Keep page canvas at #ffffff and reserve #113722 for filled CTAs and the footer band
- Set card padding to 20px and element gap to 20px for consistent tile rhythm
- Use the marquee bar pattern (uppercase, weight 700, pipe-separated) for repeating brand-attribute claims
- Reference the green #113722 only as a fill on the primary action and footer; do not use it for text or icons

Avoid:

- Do not use negative letter-spacing - the brand's voice depends on positive tracking that gives text room to shout
- Do not apply soft drop shadows, blurs, or multi-layer elevation stacks; elevation is one color and one offset
- Do not introduce additional brand hues beyond Tile Grout orange, Cold-Press green, and Sticker crimson
- Do not use 6px+ border radius or pill-shaped buttons - 5px is the maximum softness in this system
- Do not set body text in anything but weight 400-500 Helvetica; weight 700+ is reserved for display, navigation, and marquee
- Do not place light text on white or dark text on the dark-green band without testing AAA contrast
- Do not use the #6b1229 crimson as a fill - it is a shadow layer, not a brand color

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
