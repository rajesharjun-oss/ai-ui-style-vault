# Chronicle

Source: [Refero Style](https://styles.refero.design/style/1c60b014-473b-443b-b0f5-220612feebb7) 
Reference site: [https://chroniclehq.com](https://chroniclehq.com) 
Captured: 2026-07-29 
Refero published: 2026-02-05T09:57:52.000Z 
Refero modified: 2026-05-11T16:25:39.831Z 
Theme: light 
Category: SaaS

## Style Summary

Explore Chronicle's light SaaS design system: Pitch Black #050505, Midnight #000000 colors, Diatype typography, and DESIGN.md for AI agents.

North star: Typographer's proof sheet - a composited page where precision of letterform carries the entire visual weight, color is an intrusion, and the grid is the design.

## What To Borrow

- Pitch Black `#050505` for Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color
- Midnight `#000000` for Filled action button backgrounds (Try Chronicle, Talk to sales, Try for free); icon fills; strongest contrast anchor
- Charcoal `#151515` for Navigation link text and active nav states
- Obsidian `#292929` for Footer fine print and copyright text
- Graphite `#6b6b6b` for Body text, UI borders, ghost button borders and text - the workhorse mid-tone
- Pewter `#7e7e7e` for Secondary body copy and captions
- Ash `#929292` for Disabled or inactive button text and borders
- Silver `#b3b3b3` for Subtle background dividers and muted separators
- Fog `#e2e2e2` for Card borders, image borders, input borders - the hairline rule color
- Limestone `#f3f3f3` for Alternating section backgrounds, testimonial section canvas, muted surface fills
- Cloud `#ffffff` for Primary page canvas, card surfaces, link text on filled black buttons

- Diatype `--font-diatype` for Single typeface for the entire system - headings, body, nav, buttons. Weight 400 for body and secondary text; weight 500 for prominent headings and CTAs. Negative tracking of -0.03em at display sizes creates mechanical compression uncommon in SaaS type - the letterforms feel pressed into the page rather than set on it. No serif, no decorative fallback: if Diatype is absent, the design loses its primary identity marker.

## Avoid

- Never introduce a brand color (blue, purple, green) into navigation, buttons, section backgrounds, or typography - the UI is intentionally achromatic
- Never round buttons or inputs beyond 4px - pill-shaped buttons would break the editorial typographic register
- Never use font weights above 500 - Diatype at 400/500 is the full weight range; heavier weights crush the mechanical letterform quality
- Never stack more than two type sizes within a single content block without re-establishing hierarchy through #6b6b6b muted color rather than additional size steps
- Never apply more than one shadow elevation level - the system uses a single subtle card shadow; adding layered shadows introduces unwanted depth
- Never center-align body paragraphs or subheadings - all text below headline level is left-aligned
- Never use #b3b3b3 or #929292 as text colors for meaningful content - these tones exist only for disabled states and decorative separators

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
