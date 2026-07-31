# AI Implementation Prompt

Build a TWOTWO-inspired interface using this source-derived style bundle.

Reference site: https://twotwo-official.com
Theme: light
Category: E-commerce
North star: voltage lime on monochrome concrete - a single neon punch inside a black-and-white editorial grid

Use these palette anchors:

- Voltage Lime `#e3fc03` for Primary CTA fill, active state, accent badges, and decorative highlights - the single chromatic moment in an otherwise monochrome system. Sits at 18.2:1 contrast against black, so it doubles as a high-visibility call-to-action and a hover indicator without needing a second hue
- Obsidian `#000000` for Primary text, hairline borders, icon strokes, image borders, and footer background. Carries 2,045 border usages - this system uses black lines to structure space more than boxes or cards
- Graphite `#323232` for Secondary text and softer borders - slightly lifted from pure black to create a visible hierarchy without introducing color
- Carbon `#1a1a1a` for Icon strokes, link underlines, and low-priority UI marks - the third step of the dark scale, reserved for fine detail that should recede from primary text
- Paper White `#ffffff` for Primary page and card surface - the canvas everything else is drawn onto
- Concrete `#e6e6e6` for Soft section background, alternate surface, and quiet card fill.

Use these typography anchors:

- WhyteRegular `--font-whyteregular` for WhyteRegular - detected in extracted data but not described by AI
- Whyte `--font-whyte` for Display and section headings - used at 72px hero scale and 32px section scale. Tight 1.1 leading and a regular (not bold) weight are anti-convention: most sports brands shout with 800-weight display type, but Whyte Regular at 72px carries authority through letterform precision and negative space alone. The headlines never need a second style. Substitute: Inter Tight or Neue Haas Grotesk Display Pro at 400.
- Whyte Book `--font-whyte-book` for Universal workhorse - body copy, subheadings, product captions, navigation, and buttons. One weight, one family, used at seven sizes. The 38px tier handles product card titles; 16px is the default body; 13px is the fine-print and footer size. Line-height tightens from 1.60 at body to 1.30 at 38px. Substitute: Inter or Sohne at 400.
- Whyte Inktrap `--font-whyte-inktrap` for Secondary detail typeface with inktrap terminals - used for fine UI labels, tag monograms, and small monospace-feeling metadata. The inktrap cuts prevent the letterforms from filling in at small sizes, giving tags and micro-copy a distinct technical voice. Substitute: JetBrains Mono or IBM Plex Mono at 400.

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: 1280px.
- Section gap: 64px.
- Card padding: 20px.
- Element gap: 16px.

Build these component patterns where relevant:

- Top Navigation Bar: Primary site navigation
- Pill CTA Button: Primary action trigger
- Hero Banner: Full-bleed product showcase
- Product Card: Racket showcase tile
- Section Header: Subsection title block
- Product Variant Tag: Inline product color indicator
- Text Input / Search Field: Query input and form fields
- Footer: Site-wide footer band
- Icon Button: Utility action trigger
- Product Image Frame: Photographic container
- Category Grid: Product listing layout
- Racket Specification Callout: Inline technical note

Do:

- Use Voltage Lime (#e3fc03) only on filled actions, active states, and the 72px hero headline - never as a background wash, never as a decorative gradient.
- Set all button and input radii to 50px (full pill) and all card/image radii to 16px - these two values are the only radii the system permits.
- Use Whyte Book at 400 weight for everything between 13px and 38px; do not introduce a bold weight to create hierarchy - use size and color step instead.
- Compose every page on Paper White (#ffffff) with Concrete (#e6e6e6) as the only permitted mid-gray for section dividers and backdrops.
- Reserve 1px Obsidian (#000000) hairlines for card borders and structural rules - the system uses lines, not shadows, to separate surfaces.
- Set product photographs full-bleed within 16px-radius frames; let the racket colors carry all visual variety inside the grid.
- Use uppercase, tracked navigation links at 13px Whyte Book with ~0.04em letter-spacing for all top-bar and footer text.

Avoid:

- Do not introduce a second chromatic hue - no blues, reds, or greens outside the product photography. The page is monochrome plus lime, full stop.
- Do not use box-shadows or drop-shadows to elevate cards; elevation comes from 1px Obsidian borders on white surfaces, never from blurred shadows.
- Do not use a bold or 600+ weight for headlines - Whyte Regular at 400 with tight tracking is the signature; boldness would break the editorial register.
- Do not round images or cards to anything other than 16px, and do not use 4px or 8px micro-radii - the system lives in two radius steps only.
- Do not place buttons on colored or photographic backgrounds without the Voltage Lime fill - a white or black button would lose the brand's only signal.
- Do not stack the lime accent on lime (lime button on lime highlight) - the accent must sit against Paper White or Obsidian to register.
- Do not use centered text alignment for body copy, product titles, or prices - reserve centering for hero headlines and section headers only.

Source prompt cues:

**Quick Color Reference**
- text: #000000 (Obsidian)
- background: #ffffff (Paper White)
- border: #000000 (Obsidian, 1px hairline)
- accent: #e3fc03 (Voltage Lime)
- secondary text: #323232 (Graphite)
- primary action: #e3fc03 (filled action)

**3-5 Example Component Prompts**

1. **Hero Banner** - Full-bleed 100vw x 560px product image with centered 72px Whyte Regular headline in #e3fc03 (Voltage Lime), letter-spacing -1.44px. Below the headline, a pill CTA: 50px radius, #e3fc03 fill, #000000 text, Whyte Book 16px, padding 16px 32px.

2. **Product Card** - White surface (#ffffff), 1px #000000 border, 16px radius. Product image fills the card top with 16px top-corner radius. Below: 13px Whyte Book product title left-aligned in #000000, 13px price right-aligned, separated by a 1px #000000 hairline. Full-width pill CTA stacked beneath: 50px radius, #e3fc03 fill, #000000 text.

3. **Section Header** - Centered on white, max-width 640px. Title at 38px Whyte Book in #000000, supporting copy at 16px Whyte Book in #323232, line-height 1.6. 40px gap between title and body. No rule, no background.

4. **Top Navigation Bar** - Full-width white bar, 80px tall. Left: 'TWO TWO' wordmark in Whyte Book 16px uppercase. Center-left: five uppercase links at 13px Whyte Book, #000000, letter-spacing 0.04em. Right: three icon buttons (currency, search, cart) as 20px line icons with 1.5px #000000 stroke. No background, no border.

5. **Footer Band** - Full-width #000000 background, 64px vertical padding. Column headers in 16px Whyte Inktrap uppercase #ffffff, link lists in 13px Whyte Book #ffffff. Inverts the page's monochrome system without introducing any new color.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
