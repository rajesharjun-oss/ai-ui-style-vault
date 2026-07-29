# AI Implementation Prompt

Build a Isla Beauty-inspired interface using this source-derived style bundle.

Reference site: https://isla-beauty.com
Theme: light
Category: E-commerce
North star: Cream apothecary with surgical red accents - think warm parchment walls, amber bottles, and a single red seal on every label.

Use these palette anchors:

- Crimson Seal `#e4263d` for Primary action - filled add-to-cart buttons, CTA borders, section eyebrows, price accents, link underlines, and all brand punctuation against the cream canvas. The red carries the entire chromatic load; it must read as deliberate and small, never as decoration
- Vermillion Mark `#e4002b` for Secondary red accent - link borders, icon strokes, and outline-only controls. Slightly deeper than Crimson Seal; use when a quieter red moment is needed alongside the primary
- Ink Black `#000000` for Primary text, primary borders, navigation rules, body hairlines. The structural anchor of the entire interface
- Soft Coal `#1a1a1a` for Badge borders, heading text, list markers, card text on cream - a near-black used where pure black would feel clinical against the warm canvas
- Slate Drift `#2e2e2e` for Navigation borders, secondary structural lines - sits between Ink Black and the warm cream as a third depth
- Graphite `#3a3a3a` for Body text and borders for muted but still-readable paragraphs
- Pewter `#6f6f6f` for Badge borders, helper text, muted body copy - the first true mid-gray in the scale
- Stone `#8a8580` for Warm-leaning gray for tags, secondary body text, and quiet fills where neutrality needs to harmonize with the cream
- Sand Border `#e4dfd9` for Warm button borders, subtle section dividers - the border color that ties the warm palette together instead of fighting it with cool gray
- Cream Paper `#f8f6f3` for Page canvas, badge fills, soft card surfaces - the dominant background. Slightly warm to harmonize with product photography of amber liquids
- Pure Linen `#ffffff` for Card surfaces, button text on red, elevated product panels - the brightest surface that sits one step above the cream canvas
- Blush Wash `#f5e7df` for Soft accent badge fills, warm callout backgrounds - a desaturated peach that gives badge states a skin-like warmth

Use these typography anchors:

- Soehne Buch `--font-soehne-buch` for Primary body face at comfortable reading sizes (13-16px). Cleaner, more humanist than Nimbus; used for longer paragraphs and form input text.
- Nimbus Sans `--font-nimbus-sans` for Workhorse sans for UI: button labels, body copy, price text, nav links, and all utility surfaces. Carries lnum/tnum features for tabular alignment of prices.
- Soehne Kraftig `--font-soehne-kraftig` for Display and small-bold sans for headlines (60px), navigation, and tracked uppercase labels (11-12px with 0.07-0.10em tracking). The Kraftig cut adds authority without geometric coldness.
- AGaramondPro `--font-agaramondpro` for Editorial serif for major section headlines (54px) and subheadings (17-26px). The Garamond weight gives the brand its apothecary/editorial voice; pairs with italic for emotional accents.
- Garamond Italic `--font-garamond-italic` for Signature italic for emotional phrases, pull quotes, and editorial interjections mid-paragraph. Used sparingly - it is a whisper, not a shout.
- EB Garamond `--font-eb-garamond` for EB Garamond - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 50-64px.
- Card padding: 15-16px.
- Element gap: 10px.

Build these component patterns where relevant:

- Primary Action Button (Add to Cart): Filled CTA for purchase and primary conversion
- Outlined CTA (Shop the Elixir): Secondary hero action with red border
- Ghost Text Link: Inline editorial links and story links
- Product Card: E-commerce product tile with image, name, benefit, price, CTA
- Section Eyebrow Label: Red uppercase tracked label introducing sections
- Editorial Italic Pull-Quote: Garamond italic phrase embedded in or near headlines
- Top Announcement Bar: Free-shipping message strip across the top
- Header Navigation: Primary site navigation with centered logo
- Benefit Pill: Rounded tag listing product function
- Comparison Card: Two-column comparison block (typical vs. Isla system)
- Image Detail Block: Full-bleed or contained macro photography
- Price with Sale: Inline pricing with original and sale value

Do:

- Use #e4263d exclusively as the brand red - never substitute another red, and never tint or lighten it for non-critical contexts.
- Pair Garamond italic #e4263d phrases with sans body copy when you want editorial emphasis.
- Set all uppercase micro-labels (10-12px) at letter-spacing 0.12-0.18em in Nimbus Sans 500.
- Use 3px radius for every rectangular component - cards, buttons, inputs, images. Reserve 999px exclusively for pills/tags.
- Set the page canvas to #f8f6f3 (cream), not #ffffff. White appears only on cards, buttons, and product images.
- Anchor every section with a red eyebrow label (Nimbus 11px uppercase, 0.18em) before the headline.
- Use hairline 1px borders in #000000 or #e4dfd9 - never 2px+ and never with shadows.

Avoid:

- Don't introduce drop shadows, glow effects, or elevation layers - the design is intentionally flat.
- Don't use cool grays (blue-tinted). All neutrals should sit in the warm spectrum (#6f6f6f, #8a8580, #e4dfd9).
- Don't round corners beyond 3px on rectangular components; the system is sharp with intentional restraint.
- Don't mix more than one serif in the same paragraph. Garamond Italic is punctuation, not body type.
- Don't use red as a fill area larger than a button - red is a seal, not a field.
- Don't set body copy below 13px or above 17px. The 13-17px range is the system's comfort zone.
- Don't use #000000 for anything other than primary text and primary borders. For surfaces and secondary text, move to #1a1a1a or #3a3a3a.

Source prompt cues:

**Quick Color Reference**
- text (primary): #000000
- text (muted): #6f6f6f
- background (canvas): #f8f6f3
- border (hairline): #000000 or #e4dfd9
- accent (editorial italic / eyebrow): #e4263d
- primary action: #e4263d (filled action)

**Example Component Prompts**
1. Create a Primary Action Button: #e4263d background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
2. *Product card*: #ffffff card on cream canvas, 15px padding. Square product image (3px radius) at top. Product name in Nimbus Sans 700 at 15px #000. Italic benefit line in Nimbus Sans italic 400 at 13px. Price: $58.00 in #8a8580 strikethrough, $50 in #e4263d bold. Full-width Add to Cart button below: #e4263d fill, white text, 3px radius, 10px 16px padding, Nimbus Sans 500 11px uppercase with 0.10em tracking.
3. *Section eyebrow + heading pair*: Red eyebrow 'THE TYPICAL SHELF' in Nimbus 500 11px uppercase 0.18em tracking #e4263d, 10px below it a Nimbus Sans 700 36px heading in #000. Underneath, body copy in Soehne Buch 400 15px #3a3a3a at 1.4 line-height.
4. *Benefit pill cluster*: 999px radius, 1px #6f6f6f border, transparent fill, Nimbus Sans 500 11px uppercase text #000. Pills in a horizontal row with 8px gap. Used to list product functions (CLEANSE, HYDRATE, BRIGHTEN, REPAIR, EXFOLIATE, PROTECT).
5. *Comparison card*: Two columns on #f8f6f3 background, 3px radius, 15px padding. Left: section eyebrow + '14 bottles. Most half-full.' in Nimbus 36px, with light illustration below. Right: same eyebrow variant + 'Six bottles. Everything covered.' in Nimbus 36px, 6 Isla bottles illustration, benefit pills row at the bottom.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
