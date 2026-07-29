# Emmalewisham

Source: [Refero Style](https://styles.refero.design/style/1e93f444-0b01-4412-aa2b-877be5ef08d7) 
Reference site: [https://emmalewisham.co.uk](https://emmalewisham.co.uk) 
Captured: 2026-07-29 
Refero published: 2026-04-30T02:18:34.138Z 
Refero modified: 2026-06-05T07:48:47.419Z 
Theme: light 
Category: E-commerce

## Style Summary

Explore Emmalewisham's light E-commerce design system: Iris Violet #49369e, Soft Lavender #a9a7db colors, Martina Plantijn, Regola Pro Book typography, and...

North star: porcelain apothecary at golden hour. Warm linen surfaces cradle jewel-toned glass vessels; the brand violet traces hairlines through the room; serif labels float over clean sans-serif UI like engraved pharmacy signs.

## What To Borrow

- Iris Violet `#49369e` for Outlined action borders, link color, heading accents, navigation emphasis - the singular brand hue, deployed as a fine outline or thin underline rather than a filled mass
- Soft Lavender `#a9a7db` for Muted secondary accent for list borders, decorative link borders, and subtle dividers - the diluted echo of Iris Violet used when the full intensity would overpower
- Iris Focus `#524eb7` for Input focus state text/border - a slightly lifted tonal variant of Iris Violet to signal active text fields
- Blush Petal `#ec9bad` for Atmospheric surface wash and decorative accent - warm pink used for full-bleed product stage backgrounds and occasional badge fills
- Pure White `#ffffff` for Card surfaces, product image cutouts, nav and button borders, inverted text on dark or violet fields
- Stone Linen `#f2f1ef` for Page canvas - the warm off-white that grounds every section, used as the base layer beneath product stages and text blocks
- Warm Ash `#a09c97` for Muted background panels, announcement bar, low-emphasis surfaces
- Charcoal `#333333` for Secondary text and low-emphasis fills - softer than pure black for body copy and metadata
- Graphite `#000000` for Primary text, button outlines, icon strokes - used at hairline weights to stay quiet

- Martina Plantijn `--font-martina-plantijn` for Primary UI and body sans-serif - used for navigation, buttons, body text, product copy, form fields, badges, and micro-labels. The weight 300 thin gives the system its airy, unforced feel; weight 700 is reserved for navigation emphasis and select labels. This is the workhorse - almost everything visible reads in this face.
- Regola Pro Book `--font-regola-pro-book` for Display and editorial serif - used for the brand wordmark and large hero/display copy. Its 80px presence carries the entire brand identity: the 'EMMA LEWISHAM' logotype and product-feature headlines float in Regola Pro Book, creating a distinctive serif-on-sans pairing. The single weight keeps the display quiet and editorial rather than decorative.

## Avoid

- Don't fill buttons with Iris Violet or any other brand color - the action style is always outlined, never filled
- Don't apply box-shadows to cards, buttons, or nav - the system is shadow-free and uses hairline borders for definition
- Don't use bold or heavy weights in the serif (Regola Pro Book is 400 only) - the display must stay quiet
- Don't use Blush Petal (#ec9bad) as a text color or border - it's an atmospheric surface wash only
- Don't crowd the canvas with cards or panels - the layout breathes; let sections flow directly on Stone Linen
- Don't use more than one atmospheric color per section - the hero uses Blush Petal alone, never mixed with lavender or violet washes
- Don't use the 50px nav radius on anything other than the cart badge - it is a single accent, not a system-wide pattern

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
