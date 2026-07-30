# AI Implementation Prompt

Build a Zellerfeld-inspired interface using this source-derived style bundle.

Reference site: https://www.zellerfeld.com
Theme: light
Category: E-commerce
North star: Sculptor's atelier on white marble - monolithic plinth surfaces, single cobalt spark, lowercase whispers from floor to ceiling.

Use these palette anchors:

- Electric Cobalt `#000aff` for New In badges, active nav pill, current-slide indicator, claim moments - the only chromatic signal in the system, used sparingly so it reads as activation not decoration
- Pale Iris `#e5e7ff` for New Color badge fill, soft highlight wash, tinted surface for variant callouts - a desaturated ghost of the cobalt that whispers color without breaking the monochrome regime
- Ink Black `#111111` for Primary text, default borders, icon strokes, hairline dividers - the dominant structural color across headings, lists, and links
- Pure White `#ffffff` for Neutral form states, badge text, and quiet UI feedback where color should stay understated. Do not promote it to the primary CTA color
- Plaster `#ecedee` for Secondary surface for product cards, nav bar background, soft elevation tier above the canvas
- Slate `#a1a4aa` for Card border tone, neutral button fill, muted button border - the gray that defines card edges without darkening them
- Fog `#d7d7d7` for Light card border, divider lines, inactive surface tint
- Graphite `#444955` for List and navigation borders, structural dividers between rows and cells
- Ash `#737780` for Secondary text, muted body copy, de-emphasized metadata, link rest state
- Charcoal `#3b3b3b` for Body text alternate, subtle dark surface for inset blocks

Use these typography anchors:

- Roobert `--font-roobert` for Primary brand typeface - used for everything from 13px body to 128px hero. The -0.04em tracking is consistent across all sizes, pulling the lowercase wordmark into a tight, sculpted mass. Weights escalate by context: 400 for body and UI, 500 for emphasized labels, 600 for product names, 700 for large display.
- Space Mono `--font-space-mono` for Technical metadata - prices ( 189,00), Top 10 rank numerals, ticker marks, shop name credits. Drops in where the page needs to feel like a spec sheet rather than marketing copy.
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1440px.
- Section gap: 80px.
- Card padding: 20px.
- Element gap: 16px.

Build these component patterns where relevant:

- Announcement Bar: Top-of-page promotional strip
- Main Navigation: Primary site navigation
- Hero with Background Imagery: Above-the-fold product feature
- Floating Product Info Card: In-hero product buy card
- Ranked Product Card (Top 10): Numbered editorial product list item
- Standard Product Card (New Releases): Grid product display card
- New In Badge: Status indicator for fresh products
- Sold Out Badge: Inventory status indicator
- New Color Badge: Variant announcement
- See All Button: Section-end navigation
- Featured In Media Bar: Press credentials strip
- Section Header with Carousel Arrows: List section title

Do:

- Use Roobert at -0.04em tracking for all UI text; never let letter-spacing drift to 0 or positive values
- Reserve #000aff exclusively for New In badges, the active Shop pill, and current-state indicators - no more than 3% of any screen should carry this color
- Apply 10px border-radius to all cards, buttons, inputs, and images; 30px only for pill-shaped badges
- Use Space Mono for prices, rank numerals, and 'By {brand}' credit lines - never for headlines or body
- Set product card surfaces to #ecedee (Plaster), not #ffffff, to create a gentle tier above the white canvas
- Anchor product card metadata (brand mark, name, price) to a 16-20px padding from the card edge with a consistent 40x40 brand thumbnail
- Keep the hero image full-bleed and let overlays sit on the bottom third - the shoe should be the visual subject, the UI floats on top

Avoid:

- Don't introduce new chromatic colors beyond the single cobalt (#000aff) and its pale variant (#e5e7ff)
- Don't use drop shadows on product cards - the system relies on surface color stepping and 10px radius for separation
- Don't set type larger than 128px (display) or smaller than 12px (Space Mono micro labels)
- Don't use rounded radii other than 10px and 30px - no fully square corners, no fully circular elements
- Don't center body text or metadata; left-align all product information including the 'By {brand}' credit
- Don't apply color to icons - keep all line icons monochrome Ink (#111) at 1.5px stroke
- Don't separate badge variants by shape - all status badges share the 30px pill; differentiate by fill color only

Source prompt cues:

**Quick Color Reference**
- Primary text: #111111 (Ink Black)
- Page background: #ffffff (Pure White)
- Card surface: #ecedee (Plaster)
- Border: #ecedee (subtle) / #a1a4aa (defined) / #444955 (structural)
- Brand accent (badges, active state, claim moments): #000aff (Electric Cobalt)
- primary action: #000aff (filled action)

**Example Component Prompts**

1. Build a 'New Releases' product card: Plaster (#ecedee) background, 10px radius, no border, 20px padding. Top-left has a 'New In' badge - Electric Cobalt (#000aff) fill, white text in Roobert 600 12px, 30px pill radius, 4px 8px padding, positioned 12px from the card edge. Center the product image at 60% of card height. Below the image at 16px gap, place a 40x40 white brand logo thumbnail (4px radius, 1px #ecedee border). Underneath: product name in Roobert 600 16px Ink (#111111), 'By {brand}' in Space Mono 12px Ash (#737780), price in Space Mono 400 12px Ink (#111111).

2. Build a full-bleed product hero: Background fills 100vw at 80vh minimum - a photographic image of shoes on a natural surface. Bottom-left overlay stack: 'New In' badge (Electric Cobalt #000aff, 30px pill, 12px from edge), then a display headline 'studio runner' in Roobert 700 at 128px white with -5px letter-spacing, lowercase, 20px line-height. Below: 15px subhead in white at 80% opacity, Roobert 400. Right side floats a 280px-wide white product info card with 14.4px radius, 20px padding, containing a 60x60 thumbnail, product name, 'By studio' credit, and a black 'Shop studio runner' button (10px radius, 8px 20px padding, #111 background, white text).

3. Build the 'Featured In' press bar: Full-bleed Ink (#111111) background, 100px height, centered. Above the bar (separated by 24px): 'Featured in' label in Space Mono 12px Ash (#737780). Inside the bar, distribute 5 press wordmarks (COMPLEX, POPULAR MECHANICS, VOGUE, WIRED) horizontally with even spacing, all white at 60% opacity, 32-48px cap height, Roobert 700.

4. Create a Primary Action Button: #000aff background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

5. Build the 'See All' call-to-action button below a product grid: Full content-column width (not full-bleed), white (#ffffff) surface, Ink (#111111) text 'See All' in Roobert 500 16px, 10px radius, 12px 24px padding, 1px #ecedee border, centered. Subtle 0 1px 2px shadow for tap affordance. Place 32px below the grid it summarizes.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
