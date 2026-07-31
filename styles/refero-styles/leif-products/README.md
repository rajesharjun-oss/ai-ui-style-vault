# Leif Products

Source: [Refero Style](https://styles.refero.design/style/3f56ea4d-ed9d-4a36-8fb5-a801519ef80b)
Reference site: [https://leifproducts.com](https://leifproducts.com)
Captured: 2026-07-31
Refero published: 2026-04-30T02:18:27.276Z
Refero modified: 2026-06-05T09:04:11.817Z
Theme: light
Category: E-commerce

## Style Summary

Explore Leif Products's light E-commerce design system: Bone #fafaf9, Ink #000000 colors, PP Right Grotesk, Sohne typography, and DESIGN.md for AI agents.

North star: Apothecary on raw linen. A warm, hand-pressed editorial where ink-black type sits on bone-cream paper beside botanical product photography.

## What To Borrow

- Bone `#fafaf9` for Page canvas, primary card surface - the off-white paper tone the entire interface sits on, warm enough to feel linen, not bright enough to feel clinical
- Ink `#000000` for All body type, primary action border, all interactive strokes - the only dark in the system, pure black rather than warm charcoal to create maximum contrast against the cream canvas
- Stone `#e5e2dc` for Card borders, hairline dividers, subtle section breaks - the warm gray-beige that separates elements without drawing attention
- Linen `#edede7` for Hairline borders, dividers, input outlines, and card edges on light surfaces. Do not promote it to the primary CTA color
- Graphite `#595959` for Card secondary text, muted metadata, price-adjacent labels - the mid-gray that recedes behind the primary ink-black headlines
- Silt `#d6d1c7` for Neutral form states, badge text, and quiet UI feedback where color should stay understated. Do not promote it to the primary CTA color
- Blush `#ead1d0` for Decorative accent surface, soft wash behind editorial text blocks, occasional section tints - the dusty rose that nods to botanical petals without becoming saccharine
- Citron `#f3ffa9` for Promotional highlight surface - used sparingly as a wash behind sale tags, value bundle badges, or limited-edition callouts; pale enough to never compete with product photography

- PP Right Grotesk `--font-pp-right-grotesk` for Display headlines and section titles - weight 200 is anti-convention for commerce; the ultra-thin strokes create a calligraphic, editorial whisper that treats product names as poetry rather than slogans. Tight tracking (-0.015em) pulls the delicate strokes into a cohesive block.
- Sohne `--font-shne` for Primary body, UI, navigation, product names, buttons - the workhorse neutral grotesque. Weight 400 for body copy keeps a quiet editorial feel; weight 500 for navigation and product names adds enough presence to guide the eye. Slight positive tracking on uppercase labels opens them up to read as proper editorial tags.
- Sohne Mono `--font-shne-mono` for Micro-labels and scent-family tags - used for 'SMOKY & MEDITATIVE', 'BUTTERY & SOFT', 'VALUE BUNDLE' type annotations. The monospace width and widened tracking (0.05em) give these labels a scientific, museum-catalog quality that contrasts with the organic display type.

## Avoid

- Don't use any chromatic brand color for buttons, links, or CTAs - the system is intentionally achromatic; color appears only in the Blush announcement bar and Citron promotional wash
- Don't add border-radius to buttons, cards, images, or tags - sharp corners are non-negotiable
- Don't use box-shadows or drop-shadows for elevation - depth comes from whitespace and hairline borders only
- Don't use PP Right Grotesk below 26px - the ultra-thin weight becomes illegible at small sizes; switch to Sohne for anything under that threshold
- Don't use pure white (#ffffff) as a background - the slightly warm Bone (#fafaf9) is the canvas, pure white would feel sterile and break the linen paper metaphor
- Don't center-align body copy or long-form descriptions - left-align all paragraphs; centering is reserved for the announcement bar and hero subheadings only
- Don't use bright or saturated colors for icons, hover states, or active states - Ink (#000000) and Graphite (#595959) are the only two interaction colors

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
