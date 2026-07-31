# Components

### Top Navigation Bar
**Role:** Primary site navigation

Full-width white bar, 64-80px tall, containing the 'TWO TWO' wordmark (left), five uppercase text links at 13px Whyte Book (SHOP, PADEL RACKETS, PADEL BALLS, APPAREL & ACCESSORIES, BEST SELLERS, CONTACT US), and three right-aligned icon actions (CAD currency selector, search magnifier, cart bag) at 20px Obsidian stroke. No background fill, no border-bottom - the bar floats on white. Links are black, uppercase, tracked at ~0.04em.

### Pill CTA Button
**Role:** Primary action trigger

Voltage Lime (#e3fc03) fill, Obsidian (#000000) text, 50px border-radius (full pill), 16px 32px padding, Whyte Book 16px / weight 400 / line-height 1.0. No border, no shadow. Sits centered over hero imagery and stretches full-width on product cards (padding 12px 20px). This is the only interactive surface allowed to carry color.

### Hero Banner
**Role:** Full-bleed product showcase

Edge-to-edge product image filling 100vw x ~560px with a centered overlay headline at 72px Whyte Regular in Voltage Lime, followed by a pill CTA. The lime headline over the muted product photograph creates the brand's signature moment - chromatic type floating on a desaturated canvas. No gradient overlay; the product image's natural tones carry the contrast.

### Product Card
**Role:** Racket showcase tile

White surface, 16px border-radius, 1px Obsidian border, product image fills 100% width with 16px top-corner radius carrying through. Below the image: product title at 13px Whyte Book (left-aligned) and price at 13px right-aligned, separated by a hairline Obsidian rule. Full-width Pill CTA Button stacked beneath. The 1px black border on a white card is the system doing the work that shadows do elsewhere.

### Section Header
**Role:** Subsection title block

Centered text block, max-width ~640px. Primary title at 38px Whyte Book, color Obsidian. Optional supporting copy at 16px Whyte Book, color Graphite, 1.6 line-height. Generous 32-40px gap between title and body. No rule, no background - the centering and whitespace do the separation.

### Product Variant Tag
**Role:** Inline product color indicator

Tiny Voltage Lime square or short label, ~12px, positioned on the product image (top-left corner). Functions as a swatch callout - the lime chip is the same hue as the CTA, reinforcing that the accent is functional, not decorative.

### Text Input / Search Field
**Role:** Query input and form fields

White fill, 1px Obsidian border, 50px border-radius, Whyte Book 16px placeholder in Graphite. 12-16px vertical padding. Focus state thickens border to 2px Obsidian - no color change, no glow. The pill radius is reserved for inputs, buttons, and tags only.

### Footer
**Role:** Site-wide footer band

Full-width Obsidian (#000000) band, white text, uppercase Whyte Inktrap 16px for column headers, Whyte Book 13px for link lists. Padding 48-64px vertical. Inverts the page's white-on-black to black-on-white - the same border and type system, just inverted. No social icons in a different style; everything stays in the monochrome logic.

### Icon Button
**Role:** Utility action trigger

20-24px line icon, 1.5px Obsidian stroke, no fill, no border, no background. Used in nav (search, cart, account) and within cards. Touch target padded to 40px square. No hover state besides color holding - icons are utilitarian, not expressive.

### Product Image Frame
**Role:** Photographic container

Full-bleed product photograph, 16px border-radius, no border, no shadow. Images carry a 1px Obsidian hairline when used in product cards but stand borderless in hero contexts. The product itself is the content - the frame is barely there.

### Category Grid
**Role:** Product listing layout

3-column grid on desktop, 1-column mobile, 16-24px gutters. Cards stretch to equal height; images are aspect-ratio locked (3:4) so all rackets align. No alternating background tints - the grid sits on pure white with hairline grid lines.

### Racket Specification Callout
**Role:** Inline technical note

Centered body text at 16px Whyte Book, Graphite color, max-width 720px, used below section headers to describe product attributes ('Medium balance, 100% carbon and sandy finish - perfect for smooth spins and power in the attacking game without sacrificing too much control.'). Functions as a quiet technical-editorial voice between hero and grid.
