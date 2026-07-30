# Contractbook

Source: [Refero Style](https://styles.refero.design/style/fbc60c55-da20-4684-a279-0ed86590272e)
Reference site: [https://contractbook.com](https://contractbook.com)
Captured: 2026-07-30
Refero published: 2026-04-30T00:46:08.441Z
Refero modified: 2026-07-03T11:21:58.496Z
Theme: light
Category: SaaS

## Style Summary

Explore Contractbook's light SaaS design system: Ultramarine #1009f6, Gold #ffba09 colors, Abcwhyte, Abcwhyte typography, and DESIGN.md for AI agents.

North star: cream-paper contracts under ultramarine sky

## What To Borrow

- Ultramarine `#1009f6` for Feature card backgrounds, brand-emphasis headlines, footer primary CTA - vivid violet-blue carries the entire brand voice, used as punctuation against the monochromatic cream field
- Gold `#ffba09` for Primary action buttons (Request a demo), accent cards - warm yellow against neutral surfaces creates the only chromatic urgency in an otherwise achromatic system
- Forest `#304801` for Decorative illustration and testimonial card accents - deep dark green used in editorial color blocks
- Tangerine `#ff3b09` for Decorative scribble accents and highlight strokes in illustrations
- Royal `#505cf9` for Soft highlight washes and secondary illustration fills - lighter companion to ultramarine
- Sky `#add3e5` for Pastel card surfaces and muted testimonial accents - near-gray blue used as a quiet cool counterpoint to the warm beige field
- Thistle `#e3c7de` for Pastel illustration fills and testimonial card tints - near-gray mauve
- Mint `#00e9a7` for Decorative green accent for illustration highlights
- Cream `#f0f0ec` for Page background, card surfaces, input fills - warm off-white dominates the entire canvas
- Pearl `#f7f7f3` for Elevated card surfaces, lighter than cream - used for nested content blocks
- White `#ffffff` for Pure white cards and inverted button text
- Smoke `#d4d4d0` for Muted helper text and secondary labels
- Concrete `#eaeae6` for Hairline borders, subtle dividers, disabled states
- Washed Black `#1a1a1a` for Primary text, headings, body copy - slightly softer than pure black for warmer reading
- Ink `#222222` for Secondary text and nav items
- Charcoal `#4d4d4d` for Muted body text, captions, metadata
- Dim `#6d6868` for Tertiary text, timestamps, fine print
- Black `#000000` for Button text on bright fills, strong borders

- Abcwhyte `--font-abcwhyte` for Single sans-serif family used for everything - display headings, body, nav, buttons, inputs, footer. At 48px/700 with tight 1.25 line-height for hero headlines, dropping to 16px/400 with 1.5 line-height for body. The uniformity of one family at all sizes gives the system a document-like coherence rather than a display/body contrast.
- Abcwhyte `--font-abcwhyte` for UI micro-copy - nav labels, tag chips, small captions, footer links

## Avoid

- Do not add box-shadow to any card, button, or panel - elevation comes from color and space, never shadow
- Do not use a serif or display font for headlines - the single-family approach is the signature
- Do not use #1009f6 for body text or borders - reserve ultramarine for card backgrounds and brand emphasis only
- Do not use sharp corners (0-8px radius) on content cards - minimum card radius is 24px
- Do not introduce a second primary action color - gold (#ffba09) is the only filled chromatic button
- Do not use pure black (#000000) for body text - use #1a1a1a for warmer reading
- Do not crowd sections - maintain 120px vertical gaps between major sections

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
