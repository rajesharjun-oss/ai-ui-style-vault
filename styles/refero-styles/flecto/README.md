# Flecto

Source: [Refero Style](https://styles.refero.design/style/fdc72952-9b36-443a-9e0c-20b366aee29f)
Reference site: [https://flecto.io](https://flecto.io)
Captured: 2026-07-31
Refero published: 2026-04-30T01:37:21.721Z
Refero modified: 2026-06-05T11:28:55.253Z
Theme: mixed
Category: SaaS

## Style Summary

Explore Flecto's mixed SaaS design system: Forest Ink #004737, Mint Pulse #56f09f colors, Aeonik, roobert typography, and DESIGN.md for AI agents.

North star: Botanical greenhouse glasshouse. A warm cream-walled conservatory where deep teal planters hold bright mint seedlings - flat, rounded, alive with green, zero shadows.

## What To Borrow

- Forest Ink `#004737` for Dominant brand surface - hero panels, section backgrounds, thick structural borders, nav header, footer blocks. Deep teal absorbs the page and makes cream text glow
- Mint Pulse `#56f09f` for Green outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color
- Mint Mist `#d4ffe8` for Green accent for outlined action borders, linked labels, and lightweight interactive emphasis. Do not promote it to the primary CTA color
- Cream Canvas `#fffbec` for Page background - warm off-white replaces pure white. Border-color on teal sections, card fills on light areas, heading text on dark surfaces
- Deep Loam `#032019` for Text color on cream surfaces, subtle dark borders. Near-black with a green undertone that harmonizes with the Forest Ink brand color
- Sage Whisper `#99b5af` for Muted body text and secondary borders - desaturated green-gray that recedes on cream while staying tonally consistent with the brand palette
- Stone Mist `#ccdad7` for Hairline dividers, icon borders, subtle background tints on cards within light sections
- Bone `#faf2d5` for Soft warm card background - slightly warmer and more saturated than cream canvas, used to lift specific content blocks without breaking the tonal family
- Charcoal `#222222` for Body text and standard button borders in neutral contexts. Used when chromatic text is not appropriate
- Iris Spark `#8f37ff` for Violet outline accent for tags, dividers, and focused UI edges.

- Aeonik `--font-aeonik` for Universal typeface - headings, body, UI labels, buttons. Single weight 400 across the entire system; contrast is achieved through size and negative letter-spacing, not weight. This is the signature choice: a monoweight geometric sans where display headlines at 56-74px tighten to -0.043em while body text at 14-16px sits at normal or slightly positive tracking. Tabular numerals ('tnum') are enabled for all instances.
- roobert `--font-roobert` for Secondary body face - used for longer descriptive copy, list items, and hero subtext. Warmer and more humanist than Aeonik, providing tonal variety in long-form text while staying in the same single-weight, geometric family.
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI

## Avoid

- Don't introduce additional font weights - the monoweight system is the signature
- Don't use Mint Pulse (#56f09f) as a large surface area - it loses punch; keep it to button-sized and icon-sized moments
- Don't add drop shadows beyond rgba(0,0,0,0.04) 0px 3px 2px 0px - the flatness is intentional
- Don't use pure #ffffff as the page background - the cream warmth is load-bearing for the botanical feel
- Don't apply gradients - the system is strictly flat color blocks
- Don't use #8f37ff (Iris Spark) as a functional color - it is decorative only and should appear rarely
- Don't center-align body copy or lists - only headlines; body text stays left-aligned for reading rhythm

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
