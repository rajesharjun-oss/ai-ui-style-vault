# AI Implementation Prompt

Build a A-dam-inspired interface using this source-derived style bundle.

Reference site: https://a-dam.com
Theme: light
Category: E-commerce
North star: morning surf over a curated product shelf - a light, airy canvas where honest basics and ocean-toned photography do the talking.

Use these palette anchors:

- Midcurrent Navy `#000e1f` for Primary text, filled buttons, rating widget, icon strokes - the workhorse dark surface that grounds every interface layer
- Deep Cobalt `#0000c5` for Announcement bar surface and occasional accent punctuation - saturated blue used sparingly to break an otherwise monochrome frame
- Twilight Slate `#1a2635` for Secondary borders and emphasis dividers - a near-gray that steps up from Midcurrent Navy for subtle layering without contrast jumps
- Graphite `#000000` for Icon fills, nav text, and footer ink - pure black reserved for the smallest functional elements where maximum punch is needed
- Paper White `#ffffff` for Card surfaces, product tile backgrounds, nav bar canvas, and inverted text on dark fills
- Morning Mist `#f4f4f4` for Page canvas and elevated card background - the warm off-white that gives the entire site its soft, lived-in brightness
- Cloud Veil `#e6e7e9` for Dominant hairline border for cards, icons, links, and image frames - the quietest structural line in the system
- Soft Stone `#dcdddf` for List dividers, secondary borders, and badge outlines - one step darker than Cloud Veil for hierarchy between hairline and emphasis
- Slate Gray `#666e79` for Muted helper text, secondary copy, and link text in resting state - cool gray that recedes behind primary navy content
- Sunbeam `#fff48d` for Star-rating fills and small highlight washes - the only warm color in the system, kept tiny and functional

Use these typography anchors:

- GT Walsheim Pro `--font-gt-walsheim-pro` for Primary brand typeface across all UI roles. The 900 weight is the signature - it powers the 70px display headlines with architectural density. Geometric humanist forms give the brand a friendly, modern voice; the wide weight range (400 for body, 900 for display) lets a single family carry every level of emphasis.
- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI
- GT-Walsheim-Pro `--font-gt-walsheim-pro` for GT-Walsheim-Pro - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1200px.
- Section gap: 48-80px.
- Card padding: 16px.
- Element gap: 10px.

Build these component patterns where relevant:

- Announcement Bar: Full-width strip pinned above the navigation for promotional or shipping messages
- Top Navigation: Primary site navigation with centered logo
- Hero Banner: Full-bleed lifestyle image with text overlay
- Product Card: Individual product tile in collection grids
- Category Card: Larger featured product card for premium or collection groupings
- Pill Button: Primary call-to-action button
- Ghost Link Button: Secondary or tertiary action with minimal visual weight
- Star Rating Display: Product review rating with numeric score
- Trust Widget: Floating third-party review indicator
- Text Headline Section: Centered editorial section break with supporting copy
- Sustainability Split Section: Asymmetric content block pairing mission text with material photography
- Search Input: Search field in the header or overlay search panel

Do:

- Use GT Walsheim Pro weight 900 at 70px / 1.00 for display headlines - the tight leading makes huge type read as a graphic block
- Set border-radius to 30px on all buttons, inputs, tags, and pill links - the pill shape is the system's tactile signature
- Keep product cards flat: no border, no shadow, no border-radius, just white surface on Morning Mist canvas
- Use Midcurrent Navy (#000e1f) for all primary text and filled buttons - never let body copy drop to Slate Gray when full emphasis is needed
- Reserve Deep Cobalt (#0000c5) for the announcement bar surface and micro-accent moments only - it is an exclamation, not a fill
- Use hairline Cloud Veil (#e6e7e9) borders for card edges, image frames, and list dividers - this is the most-used color in the system
- Use Sunbeam (#fff48d) exclusively for star-rating fills - never as a button background, section fill, or text color

Avoid:

- Don't add drop shadows to product cards, category cards, or buttons - the system is intentionally shadowless
- Don't apply custom letter-spacing to GT Walsheim - its built-in tracking is part of the design; override only if a specific optical correction is needed
- Don't use Deep Cobalt for body text or large fills - it belongs in the 32-40px announcement strip
- Don't introduce rectangular button radii - the 30px pill is the only shape buttons take
- Don't place dark navy on dark navy without sufficient contrast separation - the system relies on light-on-dark and dark-on-light pairing
- Don't use system Arial or sans-serif as substitutes for GT Walsheim in display or heading roles - fall back to Outfit or Inter, which preserve geometric warmth
- Don't fill the page with color - the palette is 95% neutrals; let the one cobalt bar and the tiny sunbeam stars carry all chromatic punctuation

Source prompt cues:

**Quick Color Reference**
- text: #000e1f (Midcurrent Navy)
- background: #f4f4f4 (Morning Mist canvas) / #ffffff (Paper White cards)
- border: #e6e7e9 (Cloud Veil hairline)
- accent: #0000c5 (Deep Cobalt, announcement bar only)
- star highlight: #fff48d (Sunbeam, ratings only)
- primary action: #0000c5 (filled action)

**Example Component Prompts**

1. *Hero banner:* Full-bleed lifestyle photograph (16:9 or wider). Bottom-left overlay: small uppercase label 'SUSTAINABLE BASICS' at 11px GT Walsheim weight 500, white (#ffffff). Below it, headline 'Made for the long run' at 44px weight 700, #ffffff, line-height 1.10. No gradient scrim - text sits directly on the photo.

2. *Product card:* White (#ffffff) surface on #f4f4f4 canvas. No border, no shadow, no border-radius. Product photo centered with 16px padding on all sides. Below image: 'A-dam' in 11px #000000, product name in 15px #000e1f, price in 13px #666e79. Star row: 5 Sunbeam (#fff48d) stars at 12px width with '(4.2)' in 11px #666e79.

3. Create a Primary Action Button: #0000c5 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

4. *Text headline section:* Full-width #f4f4f4 background, vertical padding 64px. Centered headline at 30px weight 700, #000e1f, line-height 1.10. Body copy at 16px #666e79, max-width 640px, centered, line-height 1.40.

5. *Announcement bar:* Full-width #0000c5 strip, height 36px. Centered white text at 12px weight 400. Left/right arrow chevrons in white at the edges.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
