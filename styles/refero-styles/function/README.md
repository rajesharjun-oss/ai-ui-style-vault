# Function

Source: [Refero Style](https://styles.refero.design/style/21b71be3-78a0-4681-a5b9-64cc4b40eb67) 
Reference site: [https://www.functionhealth.com](https://www.functionhealth.com) 
Captured: 2026-07-29 
Refero published: 2026-04-30T00:12:10.227Z 
Refero modified: 2026-06-05T01:03:10.354Z 
Theme: light 
Category: Other

## Style Summary

Explore Function's light Other design system: Terracotta Seal #b05a36, Parchment #fef9ef colors, Financier Display, Ftbase typography, and DESIGN.md for AI...

North star: warm apothecary journal on parchment

## What To Borrow

- Parchment `#fef9ef` for Page canvas and primary surface - never use pure white; this warm off-white is the system's base tone
- Aged Paper `#f5eee1` for Card and panel surfaces, subtle wash backgrounds - one step deeper than the canvas to create soft elevation without shadows
- Warm Taupe `#d1c9bf` for Hairline borders, divider lines, card outlines - replaces cold gray with a tone that belongs to the cream family
- Ink `#2a2b2f` for Primary text, heading fills, strong borders - near-black with a barely-warm cast to harmonize with parchment rather than fight it
- Charcoal `#333333` for Secondary text, body copy, default icon fills, structural borders - slightly softer than Ink for reading-length passages
- Graphite `#515151` for Muted helper text, captions, secondary metadata - never below 14px without sufficient weight to maintain AAA contrast on parchment
- Ash `#808988` for Input borders, disabled state outlines, placeholder text - the only cool-leaning neutral, used only on form elements
- Pure Black `#000000` for SVG fill default, logo mark - reserve for vector illustration, never use as text or background

- Financier Display `--font-financier-display` for Display and editorial headlines - weight 400 for roman, weight 300 for italic accent words within the same headline (e.g. 'Testing is easy' pairs roman with italic). The mix of roman + italic serif in one line is the system's most distinctive typographic move. Substitute: GT Super, Domaine Display, Tiempos Headline
- Ftbase `--font-ftbase` for Body, navigation, buttons, UI labels, and all interface text. Weight 300 is used for hero subhead and large descriptive passages; weight 400 for body; weight 600 for button labels and strong UI; weight 700 reserved for emphasis. The consistent -0.023em tracking pulls the type into a tight, confident block that contrasts the generous serif spacing. Substitute: Inter, Sohne, or Untitled Sans
- Fragment mono `--font-fragment-mono` for Tiny all-caps labels in badge and eyebrow contexts - monospace gives a clinical, data-precise feel for markers like 'HSA/FSA Eligible'. Use sparingly; Ftbase caps at 600+ serve most label needs

## Avoid

- Never use pure white (#ffffff) as a background - it kills the parchment warmth that defines the brand
- Don't set body text in anything other than Ftbase; the serif is for editorial headlines only
- Don't use small sharp drop shadows; elevation must come from color stepping or the two approved shadow recipes
- Don't apply the terracotta to large background areas, decorative blocks, or text over 24px - it overwhelms when undiluted
- Avoid rectangular buttons or square card corners; the rounded shape family (40px / 24px / 9999px) is non-negotiable
- Don't introduce a second accent color - the system is monochromatic warm with one rust accent, and a second hue breaks the apothecary mood
- Don't use the -0.023em tracking on the serif Financier Display - it belongs only to Ftbase

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
