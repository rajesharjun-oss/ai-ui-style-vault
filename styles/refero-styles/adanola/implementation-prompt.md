# AI Implementation Prompt

Build a Adanola-inspired interface using this source-derived style bundle.

Reference site: https://adanola.com
Theme: light
Category: E-commerce
North star: Editorial lookbook on white paper. A fashion editorial spread where typography and photography breathe across clean white surfaces, with black ink for type and a whisper-thin custom sans-serif (Favorit) carrying the entire brand voice.

Use these palette anchors:

- Carbon Ink `#000000` for Primary text, filled action buttons, icon strokes, hairlines - the dominant ink across the entire interface
- Paper White `#ffffff` for Page canvas, card surfaces, text on dark fills, image backgrounds
- Soft Mist `#e5e7eb` for Subtle surface alternation, disabled states, skeleton backgrounds, light dividers
- Warm Fog `#f0efe7` for Off-white surface variant for subtle banding between product rows and editorial sections
- Blush Sand `#f5ebd5` for Warm cream surface for editorial highlight sections and seasonal accents
- Smoke Charcoal `#333333` for Secondary text, input borders, subdued UI chrome
- Onyx `#1d1d1d` for Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color
- Stone Gray `#cccccc` for Placeholder backgrounds, image placeholder fills, neutral swatch defaults
- Slate `#2f3440` for Cool charcoal for product photography backgrounds and muted editorial surfaces
- Olive Drab `#636355` for Warm muted surface for product photography contexts
- Maroon Clay `#523037` for Warm muted surface for product photography contexts
- Deep Iris `#222845` for Cool muted surface for product photography contexts
- Pewter `#677284` for Cool gray for product photography contexts
- Driftwood `#dfccbe` for Warm beige for product photography contexts
- Pale Tide `#badce4` for Cool pastel surface for editorial accent sections

Use these typography anchors:

- Favorit `--font-favorit` for Brand and UI typeface - used across all navigation, headings, body, buttons, inputs, and product cards. Custom monoline sans-serif with tight tracking (0.025em). Substitutes: Inter, Sohne, or Neue Haas Grotesk. The whisper-weight 400 at 30px for hero headlines is a signature choice - most fashion sites use display serifs or bold weights, but Adanola's regular-weight headlines in a clean sans feel like editorial captions rather than advertising slogans.
- Nunito Sans `--font-nunito-sans` for Secondary fallback for form inputs and minor chrome elements
- Arial `--font-arial` for System fallback for legacy email and content blocks
- swym-font `--font-swym-font` for swym-font - detected in extracted data but not described by AI
- Source Sans Pro `--font-source-sans-pro` for Source Sans Pro - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: 1440px.
- Section gap: 64px.
- Card padding: 16px.
- Element gap: 8px.

Build these component patterns where relevant:

- Ghost CTA Button: Primary hero and section action (e.g. 'SHOP ACTIVE')
- Filled Quick Add Button: Compact product-card action for adding to bag
- Product Card: Grid item in product listing sections
- Top Navigation Bar: Site-wide navigation header
- Announcement Bar: Top-of-page promotional strip
- Category Tab Filter: Horizontal category switcher above product grids
- Wishlist Heart Icon: Save-to-favorites trigger on product cards
- Color Swatch Row: Product colorway selector on cards
- Search Input: Site search and product filtering
- Chat Widget: Live chat and support trigger
- Hero Image Section: Full-bleed editorial photography
- Product Grid: Main product listing layout

Do:

- Use Favorit at all UI touchpoints - navigation, buttons, product names, headings - with 0.025em letter-spacing as the brand's defining typographic fingerprint
- Set primary actions as ghost/outlined buttons (1px #000000 border, transparent fill) - filled black is reserved for compact secondary actions like Quick Add
- Keep all border-radius values at 0px for product cards, images, and tags; use 4px only for buttons and inputs - the crisp rectangular geometry is core to the editorial lookbook feel
- Let product photography provide all color on listing and editorial pages - the UI chrome should stay near-monochrome (white surfaces, black text, #e5e7eb alternation) so garment hues read as the only chromatic accents
- Use compact 4px-based spacing (4/8/16/24px) for UI elements, then break to generous 64px+ section gaps to create the calm editorial rhythm between product grids
- Anchor the product card layout to a 4-column desktop grid with images that fill card width edge-to-edge - no card containers, no shadows, no borders around product images
- Apply the black announcement bar (#000000 bg, white 9px Favorit text) as a persistent strip above the nav for promotions and shipping messages

Avoid:

- Do not introduce drop shadows or box-shadow elevation on any component - the design system is deliberately flat and relies on whitespace and hairlines for separation
- Do not use saturated brand colors for buttons, links, or interactive states - keep the action palette strictly black/white/outline
- Do not round product card images or product card containers - the sharp rectangular edges are signature to the lookbook treatment
- Do not use display serifs, script fonts, or decorative typefaces for headings - the whisper-weight regular Favorit at 30px is the hero voice
- Do not add gradient backgrounds, colored section bands, or decorative patterns to page sections - alternation should be subtle (#e5e7eb, #f0efe7, #f5ebd5) at most
- Do not add icon containers, badges, or pill shapes around UI elements - tags and labels should be plain text with optional hairline underlines
- Do not use large border-radius values (8px+) on any element - the entire system is anchored to 0px and 4px radii only

Source prompt cues:

Quick Color Reference:
- text: #000000
- background: #ffffff
- surface alternate: #e5e7eb
- border: #000000
- accent surface: #f5ebd5
- primary action: #000000 (filled action)

Example Component Prompts:
1. Create a hero section: full-bleed lifestyle photograph (no border-radius, no overlay), white text headline 'The Ultimate staples' centered in Favorit 30px weight 400 with 0.75px letter-spacing. Below the headline, a ghost CTA button: transparent fill, 1px solid #000000 border, 4px border-radius, 'SHOP ACTIVE' in Favorit 12px weight 500 #000000, 6px 24px padding.

2. Create a product grid section: 4-column grid on #ffffff background, 16px column gap, 64px row gap. Section heading 'New & Trending' in Favorit 20px weight 700 #000000 at top-left. Each card has a full-width product image (no rounding, no border), 4 color swatch squares (12x12px) below, product name in Favorit 12px weight 400 #000000, price beneath in same style, and a filled black 'Quick Add' button at bottom-right (12px text, 4px radius, 4px 10px padding).

3. Create the top navigation: white background with 1px #000000 bottom border. Black announcement bar above: #000000 fill, white Favorit 9px weight 400 centered text 'FREE Standard Delivery on orders over 125'. Nav row: left-aligned category links (SHOP, ACTIVE, SWEATS, SPRING SUMMER) in Favorit 12px weight 500 #000000, center-aligned wordmark 'ADANOLA' in Favorit 30px weight 700, right-aligned icon cluster (heart, search, person, bag) as 16px outlined icons in #000000.

4. Create a category tab filter: horizontal row of text tabs in Favorit 12px weight 500. Active tab 'HOODIES' has #000000 background with white text and 0px border-radius. Inactive tabs 'SHORTS', 'T-SHIRTS' are #000000 text on white. 6px gap between tabs. No underlines or chevrons.

5. Create a Primary Action Button: #000000 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
