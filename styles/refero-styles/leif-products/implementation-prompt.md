# AI Implementation Prompt

Build a Leif Products-inspired interface using this source-derived style bundle.

Reference site: https://leifproducts.com
Theme: light
Category: E-commerce
North star: Apothecary on raw linen. A warm, hand-pressed editorial where ink-black type sits on bone-cream paper beside botanical product photography.

Use these palette anchors:

- Bone `#fafaf9` for Page canvas, primary card surface - the off-white paper tone the entire interface sits on, warm enough to feel linen, not bright enough to feel clinical
- Ink `#000000` for All body type, primary action border, all interactive strokes - the only dark in the system, pure black rather than warm charcoal to create maximum contrast against the cream canvas
- Stone `#e5e2dc` for Card borders, hairline dividers, subtle section breaks - the warm gray-beige that separates elements without drawing attention
- Linen `#edede7` for Hairline borders, dividers, input outlines, and card edges on light surfaces. Do not promote it to the primary CTA color
- Graphite `#595959` for Card secondary text, muted metadata, price-adjacent labels - the mid-gray that recedes behind the primary ink-black headlines
- Silt `#d6d1c7` for Neutral form states, badge text, and quiet UI feedback where color should stay understated. Do not promote it to the primary CTA color
- Blush `#ead1d0` for Decorative accent surface, soft wash behind editorial text blocks, occasional section tints - the dusty rose that nods to botanical petals without becoming saccharine
- Citron `#f3ffa9` for Promotional highlight surface - used sparingly as a wash behind sale tags, value bundle badges, or limited-edition callouts; pale enough to never compete with product photography

Use these typography anchors:

- PP Right Grotesk `--font-pp-right-grotesk` for Display headlines and section titles - weight 200 is anti-convention for commerce; the ultra-thin strokes create a calligraphic, editorial whisper that treats product names as poetry rather than slogans. Tight tracking (-0.015em) pulls the delicate strokes into a cohesive block.
- Sohne `--font-shne` for Primary body, UI, navigation, product names, buttons - the workhorse neutral grotesque. Weight 400 for body copy keeps a quiet editorial feel; weight 500 for navigation and product names adds enough presence to guide the eye. Slight positive tracking on uppercase labels opens them up to read as proper editorial tags.
- Sohne Mono `--font-shne-mono` for Micro-labels and scent-family tags - used for 'SMOKY & MEDITATIVE', 'BUTTERY & SOFT', 'VALUE BUNDLE' type annotations. The monospace width and widened tracking (0.05em) give these labels a scientific, museum-catalog quality that contrasts with the organic display type.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1440px.
- Section gap: 64px.
- Card padding: 12px.
- Element gap: 8-12px.

Build these component patterns where relevant:

- Outlined Action Button: Primary interactive trigger (e.g. 'EXPLORE COLLECTION')
- Ghost Link Button: Secondary text-based actions and navigation links
- Product Card: Grid cell for product listings in collections
- Value Bundle Badge: Promotional label overlaid on product cards
- Hero Editorial Split: Full-viewport homepage hero
- Scent Family Filter: Left-sidebar category navigation on collection pages
- Category Feature Card: Right-side featured display on the 'Meet the family' page
- Announcement Bar: Top-of-page promotional strip
- Primary Navigation: Top bar with logo and menu items
- Product Card Hover State: Interactive feedback for product grid items
- Footer: Bottom-of-page navigation and legal content

Do:

- Use PP Right Grotesk weight 200 for all display headlines at 34px and above - the ultra-thin stroke is the signature, never substitute with weight 400 or 500
- Apply Sohne Mono 11-12px with 0.05em tracking for all small uppercase labels (scent families, badges, metadata) - this creates the museum-tag rhythm
- Keep all corners at 0px radius - every component should have sharp rectangular edges to maintain the editorial print feel
- Use #fafaf9 (Bone) as the exclusive page background - never pure white, never gray
- Let product photography carry the color - the interface palette stays warm-neutral so botanicals and amber bottles become the only chromatic elements
- Use 1px borders in #e5e2dc (Stone) or #000000 (Ink) for all separation - no shadows, no fills, no background tints to create depth
- Set display headlines to line-height 1.0 with tight negative tracking (-0.015em) so the thin strokes lock into a cohesive editorial block

Avoid:

- Don't use any chromatic brand color for buttons, links, or CTAs - the system is intentionally achromatic; color appears only in the Blush announcement bar and Citron promotional wash
- Don't add border-radius to buttons, cards, images, or tags - sharp corners are non-negotiable
- Don't use box-shadows or drop-shadows for elevation - depth comes from whitespace and hairline borders only
- Don't use PP Right Grotesk below 26px - the ultra-thin weight becomes illegible at small sizes; switch to Sohne for anything under that threshold
- Don't use pure white (#ffffff) as a background - the slightly warm Bone (#fafaf9) is the canvas, pure white would feel sterile and break the linen paper metaphor
- Don't center-align body copy or long-form descriptions - left-align all paragraphs; centering is reserved for the announcement bar and hero subheadings only
- Don't use bright or saturated colors for icons, hover states, or active states - Ink (#000000) and Graphite (#595959) are the only two interaction colors

Source prompt cues:

**Quick Color Reference**
- text: #000000 (Ink)
- background: #fafaf9 (Bone)
- border: #e5e2dc (Stone) for subtle, #000000 (Ink) for interactive
- accent surface: #ead1d0 (Blush) for announcement bars, #f3ffa9 (Citron) for promotional badges
- primary action: no distinct CTA color

**Example Component Prompts**

1. **Hero Editorial Split**: Full-viewport 50/50 layout. Left half: full-bleed product photo. Right half: Bone (#fafaf9) background. Headline 'Scents of affection' in PP Right Grotesk 52px weight 200, color Ink (#000000), letter-spacing -0.78px, line-height 1.0. Subtext in Sohne 15px weight 400, line-height 1.38. Outlined button below: 1px Ink border, Bone fill, text 'EXPLORE COLLECTION' in Sohne 12px weight 500 uppercase with 0.02em tracking, padding 12px 24px, 0px radius.

2. **Product Grid Card**: Bone (#fafaf9) background, no border, 0px radius. Square product image fills the card. Below: product name in Sohne 16px weight 400 left-aligned, price in Sohne 16px weight 400 right-aligned. Bottom row: scent label in Sohne Mono 11px uppercase, 0.05em tracking, e.g. 'SMOKY & MEDITATIVE'. Optional Citron (#f3ffa9) badge top-left with text 'VALUE BUNDLE' in Sohne Mono 11px uppercase on Ink.

3. **Scent Family Filter Row**: Full-width row, 1px Stone (#e5e2dc) border-bottom. Small square thumbnail (~60px) on left, scent name in Sohne Mono 11px uppercase centered in the row, radio indicator on right (filled Ink dot if active, empty circle if not). Zero vertical padding beyond image height.

4. **Announcement Bar**: Full-bleed Blush (#ead1d0) background, 40px height. Centered text 'FREE STD SHIPPING AU WIDE ON ORDERS $50+' in Sohne Mono 12px uppercase, 0.05em tracking, Ink color. Close x icon at right in Ink.

5. **Category Feature Display**: Two-column asymmetric layout - left 50% is a large square botanical/product photograph, right 50% is Bone (#fafaf9) with text stacked vertically. Headline 'Kakadu Plum' in PP Right Grotesk 34px weight 200, Ink. Subtitle 'BUTTERY & SOFT' in Sohne Mono 11px uppercase below headline. Description paragraph in Sohne 15px weight 400. Ghost link 'SHOP KAKADU PLUM' in Sohne 13px weight 500, Ink, 1px Ink border-bottom, at bottom.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
