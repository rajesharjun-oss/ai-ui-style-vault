# Assembly Coffee London

Source: [Refero Style](https://styles.refero.design/style/8288950a-2731-44fd-85ef-211aecd8091d)
Reference site: [https://assemblycoffee.co.uk](https://assemblycoffee.co.uk)
Captured: 2026-07-30
Refero published: 2026-04-30T00:18:07.021Z
Refero modified: 2026-07-03T15:41:11.464Z
Theme: dark
Category: E-commerce

## Style Summary

Explore Assembly Coffee London's dark E-commerce design system: Obsidian #0e1311, Pure Black #000000 colors, GT America Standard, ID00 Serif typography, and...

North star: Embers in a dark roastery. A near-black canvas with warm, low-lit product photography and italic serif labels - the feeling of a specialty coffee menu printed in a midnight zine.

## What To Borrow

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

- GT America Standard `--font-gt-america-standard` for The UI workhorse: navigation labels, body copy, button text, metadata, footer text, cart count, form fields. Weight 400 for body, 500 for nav items, 600 sparingly for tiny uppercase labels like 'FEATURED'. At 11-14px it carries the entire structural layer.
- ID00 Serif `--font-id00-serif` for The editorial voice: product names, section headings, the 'Shop Now' and 'Limited Time Offer' labels in the hero, the 'Independent specialty coffee roaster...' manifesto copy. Almost always set in italic - this is the signature move. The italic serif against a black canvas is what makes the site read as a curated coffee journal rather than a store.
- Helvetica `--font-helvetica` for Fallback / system substitute for small tertiary text and icons where GT America is not loaded.
- reviewsio-font `--font-reviewsio-font` for reviewsio-font - detected in extracted data but not described by AI

## Avoid

- Do not introduce a filled chromatic CTA button. The system is intentionally CTA-less at the primary level - actions are italic serif links.
- Do not set body copy or navigation in the serif. GT America is for UI; ID00 Serif is for editorial and product naming. Mixing the two roles dilutes both.
- Do not use bright white (#ffffff) as a page background. The system is dark-first; invert only for price chips, modal overlays, and the rare light section.
- Do not apply saturated brand colors to backgrounds, cards, or text. The chromatic palette exists only as small badge fills and hairlines.
- Do not use large drop shadows. The 10px blur at 5% opacity is the ceiling - anything heavier reads as Material/iOS, not editorial gallery.
- Do not set headlines in weight 600 or 700. The serif runs 300-400 italic and the sans runs 400-500. Anything bolder breaks the whisper-quiet tone.
- Do not place product photography on a white or light-gray background. Always shoot against a warm, dark studio tone to maintain the ember-roastery atmosphere.

## Bundle Contents

- [DESIGN.md](DESIGN.md): full source-derived implementation reference.
- [implementation-prompt.md](implementation-prompt.md): ready-to-paste prompt for an AI builder.
- [style.json](style.json): structured style metadata and token summary.
- [tokens/colors.md](tokens/colors.md): palette and surface rules.
- [tokens/typography.md](tokens/typography.md): type scale and font rules.
- [tokens/spacing-shape.md](tokens/spacing-shape.md): spacing and radius rules.
- [tokens/components.md](tokens/components.md): component recipes.
- [tokens/guidelines.md](tokens/guidelines.md): do and do-not guidance.
- [tokens/layout-imagery.md](tokens/layout-imagery.md): layout and imagery direction.
- [code/css-variables.css](code/css-variables.css): CSS variable starter.
- [code/tailwind-v4.css](code/tailwind-v4.css): Tailwind v4 token starter.
- [code/design-tokens.json](code/design-tokens.json): portable token JSON.
- [screenshots/README.md](screenshots/README.md): source media references.
