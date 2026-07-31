# AI Implementation Prompt

Build a Sandland Sleep-inspired interface using this source-derived style bundle.

Reference site: https://sandlandsleep.com
Theme: light
Category: E-commerce
North star: warm cream sleep journal with deep navy nights

Use these palette anchors:

- Midnight Navy `#1a365d` for Hero gradient base, dark data cards, icon strokes - the cool nocturnal counterpoint to the warm cream canvas, signals science and trust at the deepest end of the palette
- Sunlit Yellow `#fae467` for Primary CTA fill, bestseller badges, data-highlight accents - the only vivid chromatic in the system, warm and optimistic like morning light, used sparingly so every action glows
- Linen Cream `#f2ede8` for Page canvas, default section background - the dominant warm neutral that sets the entire sleep-warmth tone of the site
- Paper White `#ffffff` for Card surfaces, product photography backgrounds, nav backgrounds - pure white creates lift against the cream canvas
- Soft Vellum `#faf8f6` for Secondary card surfaces, subtle elevation layer - warmer than pure white, used when cards need to nest within cream sections without disappearing
- Graphite `#3d3d3d` for Body text, subtle border accents - softer than pure black for extended reading
- Smoke `#666666` for Secondary text, list borders, muted link underlines - the mid-gray that carries all supporting copy
- Slate `#726f6d` for Input borders, disabled button text and borders - the warm-leaning gray for form and inactive states
- Charcoal `#191923` for Deep surface fill for dark accent cards, alternative button backgrounds - nearly black with a slight cool cast, sits between midnight navy and true black
- Frost `#e6e6e6` for Hairline dividers, image borders, section separators - neutral-cool gray for structural lines
- Ink Black `#000000` for Primary text, dominant heading color, primary borders - the typographic anchor across all surfaces

Use these typography anchors:

- Sandland-550 `--font-sandland-550` for Custom sans-serif used across every UI surface - body, headings, buttons, nav, cards. Weight 400 dominates body and most headings, weight 500/600 reserved for emphasis. The tight negative tracking on display sizes (-0.03em at 48-72px) gives headlines a composed, compact feel; positive tracking on small uppercase labels (0.036-0.045em at 10-13px) provides the airy editorial rhythm seen in nav links, badge text, and section eyebrows.
- Inter `--font-inter` for Inter - detected in extracted data but not described by AI
- GTStandard-M `--font-gtstandard-m` for GTStandard-M - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 64px.
- Card padding: 20px.
- Element gap: 12-16px.

Build these component patterns where relevant:

- Primary CTA Button: Main conversion action (Shop Now, Add to Cart)
- Ghost Nav Pill Button: Secondary navigation action (Take the Sleep Quiz)
- Nav Link: Top-level navigation items (Shop All, Stay Asleep, Deep Sleep, FAQ)
- Product Card: Product showcase in the Science-Backed Solutions grid
- Bestseller Badge: Product ranking indicator on product cards
- Testimonial Card: Customer review with avatar, rating, quote, and product reference
- Dark Data Card: Oura Ring sleep score results - the dramatic counterpoint to the warm sections
- Circular Progress Gauge: Sleep score visualization in the dark data card
- Star Rating: 5-star review display in testimonial cards
- Carousel Navigation Arrow: Left/right navigation for testimonial and product carousels
- Section Heading Block: Section titles (Science-Backed Solutions for Better Rest)
- Input Field: Form inputs (email, search)

Do:

- Use Sunlit Yellow (#fae467) as the fill for exactly one element per viewport: the primary action or the single data highlight
- Set border-radius to 20px for buttons and nav pills, 10px for cards and badges, 4px for inputs - three radius values, no others
- Keep the cream canvas (#f2ede8) unbroken across full page-width sections; never tile it within cards or components
- Apply -0.03em letter-spacing at 48px and above; apply 0.036-0.045em tracking at 10-13px uppercase labels; leave body text at default tracking
- Use Midnight Navy (#1a365d) as a section-level surface, not as a text color or border - it should feel like turning off the lights
- Limit shadows to 10% black opacity with 12-20px blur; never use sharp or saturated shadows
- Place the brand wordmark centered in the top nav with nav links left-aligned and action pill right-aligned

Avoid:

- Do not introduce a second chromatic accent color - yellow is the only highlighter in the system
- Do not use sharp corners (0-2px radius) on any container, card, or interactive element
- Do not use saturated shadows, glow effects, or multi-layer shadow stacks
- Do not place colored product top bands outside the product card - the pink/orange lives on the product mockup only
- Do not use Midnight Navy as a body text color; reserve it for surface fills and large display contexts
- Do not use pure black (#000000) as a background fill; use Charcoal (#191923) for dark surfaces
- Do not apply letter-spacing tighter than -0.03em or looser than 0.045em - the tracking scale is narrow and intentional

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
