# Components

### Filled Primary Button
**Role:** The single chromatic CTA on any page - signals the most important action

Pill-shaped (border-radius: 980px), background #0071e3, text #ffffff at 14px/400, padding 11px 21px. Sits on the light canvas as the only non-monochrome element in the action set. Used for 'Mas informacion' across product sections.

### Outlined Secondary Button
**Role:** Companion action to the filled primary, typically 'Comprar' or 'Comprar un iPhone'

Pill-shaped (border-radius: 980px), transparent background, 1px border in #0066cc, text #0066cc at 14px/400, padding 11px 21px. Always appears to the right of the filled primary button. Pairs the two pills side by side with an 8px gap.

### Ghost Outline Button (Dark Surface)
**Role:** Outlined action variant used on dark hero bands like Apple TV+ carousel

Pill-shaped (border-radius: 980px), transparent background, 1px border in #2997ff, text #2997ff at 14px/400, padding 8px 15px (slightly tighter than the light-surface outlined variant).

### Text Link
**Role:** Inline links in body copy, footer terms, and the global message bar

No border-radius, no background, color #0066cc, text-decoration-underline on hover. The link 'Comprar >' in the financing banner is the canonical example - it sits inline with body text, underlined or with a chevron suffix.

### Global Nav Bar
**Role:** Persistent top navigation across all pages

Height 44px, full viewport width, background #ffffff with backdrop-filter saturate(1.8) blur(20px). Left: Apple logo glyph. Center: 9 nav items (Tienda, Mac, iPad, iPhone, Watch, AirPods, TV y Casa, Entretenimiento, Accesorios, Soporte) at 12px/400, color #1d1d1f with #474747 hover. Right: search icon and bag icon, both 44px tap targets.

### Global Message Bar
**Role:** Promotional ribbon below the nav - financing offers, launch announcements

Background #ffffff, 12px/400 body text, centered, includes an inline blue text link. No border, no padding above or below beyond the nav's own spacing.

### Product Hero Section
**Role:** The dominant unit of the page - one product per full-width section

Full-bleed width, background switches between #f5f5f7 (neutral) and soft gradient washes (e.g. pale blue for iPad Air, near-white for MacBook Air). Centered content stack: product name at 56px/600 in #1d1d1f, subhead at 21px/400 in #1d1d1f, button pair centered below, then a large product render image (MacBook open, iPhone lineup) at full width. Section height typically 600-700px.

### Button Pair (CTA Cluster)
**Role:** The action duo under every product headline

Two pill buttons centered horizontally with 8px gap. Left: filled #0071e3 with 'Mas informacion'. Right: outlined #0066cc with 'Comprar' or 'Comprar un iPhone'. The pair is the only place on the page where blue appears as a color - everything else is monochrome.

### Entertainment Carousel
**Role:** Full-bleed horizontal scroll for Apple TV+ content

Background dark or photographic, large card tiles (roughly 280px wide, 420px tall) with rounded corners ~12px. Each card has a 'Ver ahora' white pill button overlaid in the bottom-left corner. Dot pagination (8 dots) below the carousel indicates position.

### Product Lineup Display
**Role:** Showcase of product variants (iPhone 17 colors, MacBook angles)

Full-width product photography with no card or border - the products float on the section background. Multiple product angles or colorways arranged in a row, shot on pure #f5f5f7 or #aad0f6 backgrounds with soft drop shadows in the photography itself.

### iPad Air Wordmark
**Role:** Product name with mixed-weight treatment

The word 'iPad' at 40px/600 in #1d1d1f followed by 'air' in a lighter italic-leaning weight (visually distinct script treatment) at the same size, in #1d1d1f. The weight contrast within a single wordmark is the signature treatment for Air-tier products.

### Footer Link List
**Role:** Dense grid of navigational and legal links at the page bottom

Background #f5f5f7, two-column layout with column headings at 12px/600 in #1d1d1f and link items at 12px/400 in #515154. Columns separated by ~10px row gap. No dividers between items, no card containers.

### Legal / Terms Block
**Role:** Fine-print legal text at the very bottom of the page

Full width within the footer band, 12px/400 in #707070, line-height 1.33. Dense paragraph blocks with inline blue links to 'Consulta las condiciones'.
