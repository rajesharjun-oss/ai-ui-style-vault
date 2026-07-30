# AI Implementation Prompt

Build a Assembly Coffee London-inspired interface using this source-derived style bundle.

Reference site: https://assemblycoffee.co.uk
Theme: dark
Category: E-commerce
North star: Embers in a dark roastery. A near-black canvas with warm, low-lit product photography and italic serif labels - the feeling of a specialty coffee menu printed in a midnight zine.

Use these palette anchors:

- Obsidian `#0e1311` for Primary canvas - page backgrounds, hero sections, card surfaces. The near-black with a faint green undertone makes white type glow without feeling sterile
- Pure Black `#000000` for Deepest surface, borders, and type. Used for maximum-contrast outlines, product box photography backgrounds, and the darkest UI strokes
- Ash Charcoal `#1a1a1a` for Secondary surface and border tone - slightly lifted from black for subtle layering on nav, dividers, and outlined button edges
- Graphite `#333333` for Mid-neutral for secondary text, input borders, and card outlines where pure black is too heavy
- Stone Gray `#808080` for Image placeholder and muted background tone - holds space where product photography is loading or absent
- Silver `#b3b3b3` for De-emphasized borders and helper text on light surfaces
- Bone `#ffffff` for Primary text on dark canvases, price-chip fills, inverted button surfaces. The brightest accent in an otherwise low-key palette
- Linen `#f6f7f2` for Warm off-white surface for inverted sections, price pill backgrounds, and soft button fills. Sits between bone and the khaki family
- Sand Khaki `#dfdbca` for Hairline borders, dividers, input outlines, and card edges on light surfaces.
- Lichen Green `#cadcac` for Green state accent for badges, validation surfaces, and short status labels.
- Citron `#faf080` for Yellow state accent for badges, validation surfaces, and short status labels.
- Antique Gold `#cfa53b` for Accent stroke and border for promotional or limited-availability badges. Reads as aged brass - never neon
- Olive Bark `#4d4a31` for Dark olive link/announcement background - the deep green-brown of the top bar, grounded and earthy

Use these typography anchors:

- GT America Standard `--font-gt-america-standard` for The UI workhorse: navigation labels, body copy, button text, metadata, footer text, cart count, form fields. Weight 400 for body, 500 for nav items, 600 sparingly for tiny uppercase labels like 'FEATURED'. At 11-14px it carries the entire structural layer.
- ID00 Serif `--font-id00-serif` for The editorial voice: product names, section headings, the 'Shop Now' and 'Limited Time Offer' labels in the hero, the 'Independent specialty coffee roaster...' manifesto copy. Almost always set in italic - this is the signature move. The italic serif against a black canvas is what makes the site read as a curated coffee journal rather than a store.
- Helvetica `--font-helvetica` for Fallback / system substitute for small tertiary text and icons where GT America is not loaded.
- reviewsio-font `--font-reviewsio-font` for reviewsio-font - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1400px.
- Section gap: 80px.
- Card padding: 20px.
- Element gap: 16px.

Build these component patterns where relevant:

- Announcement Bar: Top-of-page utility strip
- Primary Header / Nav: Site-wide navigation
- Editorial Hero - Featured Column: Left-side hero index
- Product Hero - Studio Photograph: Right-side hero visual
- Editorial Manifesto Block: Brand statement section
- Product Card (Dark): Catalog product tile
- Price Pill: Inline price chip
- Editorial Tag Badge: Category / status label
- Outlined Text Button: Primary navigation action
- Search Icon Button: Header utility
- Cart Indicator: Header utility
- Pairing Banner (Red Box): Co-branded event block

Do:

- Set headlines and product names in ID00 Serif italic - the italic serif is the brand's voice. Setting them in roman or in the sans destroys the editorial feel.
- Keep the canvas near-black (#0e1311 or #000000) and let bone (#ffffff) type carry the hierarchy. Reach for colored surfaces only for inverted sections or badge fills.
- Use 4px radii on cards, buttons, inputs, and badges. The 60px radius is reserved exclusively for the cream price pill - do not apply it to other components.
- Place product photography on warm, low-lit studio backdrops (ember red, dark amber, charcoal). Avoid white or bright backgrounds - they break the dark-gallery mood.
- Use badge colors (citron #faf080, lichen #cadcac, antique gold #cfa53b) sparingly and only for editorial tags, not for actions or alerts.
- Make CTAs typographic links in ID00 Serif italic, not filled buttons. A 4px-radius ghost button is acceptable only for secondary utility actions like the cart selector.
- Separate layers with 1px hairlines in #1a1a1a or #dfdbca, not with shadows. The system runs on border contrast, not elevation.

Avoid:

- Do not introduce a filled chromatic CTA button. The system is intentionally CTA-less at the primary level - actions are italic serif links.
- Do not set body copy or navigation in the serif. GT America is for UI; ID00 Serif is for editorial and product naming. Mixing the two roles dilutes both.
- Do not use bright white (#ffffff) as a page background. The system is dark-first; invert only for price chips, modal overlays, and the rare light section.
- Do not apply saturated brand colors to backgrounds, cards, or text. The chromatic palette exists only as small badge fills and hairlines.
- Do not use large drop shadows. The 10px blur at 5% opacity is the ceiling - anything heavier reads as Material/iOS, not editorial gallery.
- Do not set headlines in weight 600 or 700. The serif runs 300-400 italic and the sans runs 400-500. Anything bolder breaks the whisper-quiet tone.
- Do not place product photography on a white or light-gray background. Always shoot against a warm, dark studio tone to maintain the ember-roastery atmosphere.

Source prompt cues:

**Quick Color Reference**
- text (on dark): #ffffff
- text (secondary/muted): #b3b3b3
- Create a Primary Action Button: #000000 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
- surface (warm border / hairline): #dfdbca
- accent (editorial badge - new release): #faf080
- primary action: #000000 (filled action)

**3-5 Example Component Prompts**

1. *Editorial Hero Index Entry*: A vertical stack entry on #0e1311 canvas. Product name in ID00 Serif italic 21px, #ffffff. Sublabel 'Shop Now' or 'Limited Time Offer' in ID00 Serif italic 16px, #b3b3b3. Vertical spacing 48px between entries. No border, no background, no button - pure typographic link.

2. *Product Card (Dark)*: Square card on #0e1311 background, 4px radius, 1px border in #1a1a1a. Upper 65%: product photograph on a warm ember-red studio backdrop with soft shadow. Lower 35%: product name in ID00 Serif italic 24px #ffffff, tasting notes in GT America 14px #b3b3b3, price pill at bottom-left.

3. *Price Pill*: Inline pill, 60px radius, #f6f7f2 background, padding 6px 16px. Text 'From - 29.95' in GT America 13px weight 500, #0e1311. No border, no shadow.

4. *Editorial Tag Badge*: Small pill, 4px radius, #faf080 background, padding 4px 8px. Text 'New Release' in GT America 11px weight 500 uppercase, #0e1311. No border.

5. *Manifesto Block*: Full-width #0e1311 section, 80px vertical padding above and below. Centered or left-aligned text in ID00 Serif italic 36px, #ffffff, line-height 1.2, weight 300. No buttons, no links, no images - the prose is the section.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
