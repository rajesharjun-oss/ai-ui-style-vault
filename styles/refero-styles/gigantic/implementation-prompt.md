# AI Implementation Prompt

Build a Gigantic-inspired interface using this source-derived style bundle.

Reference site: https://giganticcandy.com
Theme: light
Category: E-commerce
North star: punk-rock candy wrapper shouting on cream paper

Use these palette anchors:

- Ink Black `#231f20` for Primary text, filled action buttons, nav, headings, hairline borders, product bar backgrounds
- Cream Paper `#f0ede7` for Primary page canvas, section backgrounds, image backgrounds
- Pure White `#ffffff` for Inverted text on dark surfaces, button text, card/image backgrounds
- Blast Red `#ff634b` for Flavor-coded product accent (Salted Peanut bar), footer band, brand mark, single decorative punctuation across the cream canvas
- True Black `#000000` for Minor icon strokes and print-style detail

Use these typography anchors:

- Neue Haas Grotesk Display `--font-neue-haas-grotesk-display` for Exclusive brand typeface. Weight 700 drives the hero display voice and section openers - set huge, tracked wide, the type IS the graphic. Weights 450/500 handle subheadings, nav, and product labels. Weight 400 at 14-16px with wide tracking (0.0310-0.0500em) runs body and button text. The all-caps + wide-tracking + heavy-weight combination is the signature.
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI
- GTStandard-M `--font-gtstandard-m` for GTStandard-M - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 30px.
- Element gap: 20px.

Build these component patterns where relevant:

- Hero Display Headline: Oversized section opener that dominates the viewport
- Filled Ink Button: Primary action - shop, add to cart, CTAs
- Outline Ink Button: Secondary action and product grid CTAs
- Announcement Bar: Top-of-page promo strip and product ticker
- Minimal Nav Bar: Primary site navigation
- Product Card: Grid item for candy bar SKUs
- Flavor-Coded Product Image: Product bar photography with brand-specific accent
- Dark Feature Section: Product variety showcase and product bar reveal
- Section Header Block: Centered intro text under hero
- Brand Script Logo: Wordmark in nav and on packaging
- Footer Band: Closing brand statement and secondary nav
- Account Icon Group: Utility icons in nav

Do:

- Use Neue Haas Grotesk Display exclusively; weight 700 for display, 500 for UI, 400 for body. No other typefaces.
- Set the canvas to Cream Paper (#f0ede7) by default. Reserve Pure White for product images and inverted text surfaces only.
- Use Ink Black (#231f20) as the primary action color for filled buttons. Make them rectangular with 0px radius, padding 19px x 15px, and 16px uppercase text with 0.0310em tracking.
- Track all text wide: 0.0250em minimum at body sizes, scaling up to 0.0570em at display sizes. Tight tracking breaks the brand voice.
- Reserve Blast Red (#ff634b) for three uses only: flavor-coded product packaging, the footer band, and the brand mark. Never as a button fill or body text accent.
- Make the hero headline oversized and sentence-case, with the final word optionally italicized for a cadence break. The type is the hero - no supporting visual.
- Separate sections with hard color transitions (cream black cream), not with whitespace or dividers. Full-bleed, not padded.

Avoid:

- Do not add shadows, gradients, or any form of elevation. Surfaces stay flat.
- Do not round corners on buttons, cards, images, or tags. 0px radius is the signature.
- Do not use Blast Red as a CTA or button background. Red is decoration; black is action.
- Do not set body text in sentence case at large sizes - body and UI text should be uppercase with wide tracking.
- Do not use multiple accent colors or introduce new hues. The palette is mononeutral + one red.
- Do not add illustrative graphics, lifestyle photography, or decorative backgrounds. The system is type + product photography only.
- Do not use light or thin font weights for display headlines. Weight 700 is the only display weight.

Source prompt cues:

**Quick Color Reference**
- text: #231f20
- background: #f0ede7
- border/divider: #231f20
- accent: #ff634b
- button text: #ffffff
- primary action: #231f20 (filled action)

**3-5 Example Component Prompts**

1. **Hero Headline Block** - Cream Paper (#f0ede7) full-bleed background. Display text 'HAVE A LITTLE THRILL' centered, Neue Haas Grotesk Display weight 700 at ~140px, line-height 1.0, color #231f20, letter-spacing ~0.05em. Three lines stacked, sentence case, final word italicized. No image, no supporting visual - the type fills 70% of the viewport.

2. **Product Grid Card** - White (#ffffff) product image filling the top 70% of the card, no border, no radius. Below the image: product name in Neue Haas Grotesk Display weight 700, 24px, color #231f20, all-caps, letter-spacing 0.0360em. Then an outline button: 1px #231f20 border, 0px radius, 19px horizontal x 15px vertical padding, 16px uppercase text in #231f20 with 0.0310em tracking.

3. **Dark Feature Section** - Ink Black (#231f20) full-bleed background. Display text 'VARIETY' at ~120px weight 700 in #f0ede7, with a halftone-dot texture pattern inside the letterforms. Product bar image (candy bar on dark background with torn-paper edge) overlaps the section's top edge, breaking from the cream section above.

4. **Filled Ink Button** - Background #231f20, text #ffffff, 0px border-radius, padding 19px horizontal x 15px vertical, Neue Haas Grotesk Display weight 500 at 16px, all-caps, letter-spacing 0.0310em. Width auto-fits content. No hover lift, no shadow - only color stays flat.

5. **Footer Band** - Blast Red (#ff634b) full-bleed background, cream text (#f0ede7) for brand statement, centered, 16px Neue Haas Grotesk Display weight 500 all-caps with 0.0310em tracking. White secondary nav links above the red band, separated only by the color change - no divider line.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
