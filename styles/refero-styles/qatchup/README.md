# Qatchup

Source: [Refero Style](https://styles.refero.design/style/1b010453-80df-406a-8b1a-72630c4a5165) 
Reference site: [https://www.qatchup.com](https://www.qatchup.com) 
Captured: 2026-07-29 
Refero published: 2026-05-07T22:39:42.507Z 
Refero modified: 2026-06-03T19:25:40.026Z 
Theme: light 
Category: SaaS

## Style Summary

Explore Qatchup's light SaaS design system: Charcoal #080808, Graphite #222222 colors, Aspekta, Fasthand typography, and DESIGN.md for AI agents.

North star: Ink on warm paper, whispered quietly.

## What To Borrow

- Charcoal `#080808` for Primary headings, high-emphasis text - the deepest ink against the warm white canvas, anchoring headlines at maximum contrast
- Graphite `#222222` for Body text, icon strokes, secondary headings - slightly lighter than Charcoal for body density where pure black feels too heavy
- Mid Ink `#292929` for Filled button background, dark UI surfaces, strong border emphasis - the primary action surface; charcoal-darker than body text for weight contrast against pills
- Steel `#696969` for Default border color, card edges, icon strokes at rest - the structural hairline that carries the entire layout; appears in 260 borderColor uses, making it the most-used stroke in the system
- Fog `#999999` for Muted secondary borders, low-emphasis dividers - a lighter hairline for de-emphasized structure
- Ash `#b2b2b2` for Card inner borders, subtle dividers inside containers - softer than Steel for nested elements
- Slate `#8d8d8d` for Disabled or inactive border state, decorative dividers - sits between Steel and Fog for tertiary structural lines
- Mist `#cccccc` for Subtle shadow contribution, light card shadow base - a desaturated mid-gray for soft elevation
- Silk `#e4e4e7` for Image borders, body content dividers, light surface separators - the lightest visible structural line, near-white with just enough definition
- Bone `#fafafa` for Page canvas, card surfaces, link border, light text on dark - the warm white foundation; every other neutral reads against this base
- Cream `#f4f4f5` for Secondary button fill, elevated surface tone, subtle hover state - one step warmer/lighter than Bone for nested surfaces

- Aspekta `--font-aspekta` for All UI text - headlines at 40-56px use weight 400 with aggressive negative tracking (-0.035em to -0.020em) to create a condensed, modern feel; body text at 16-18px uses weight 400 with lighter tracking (-0.011em to -0.010em); weight 500 reserved for button labels and emphasis. The tight letter-spacing at display sizes is signature - it pulls letters together so headlines read as confident blocks rather than airy sentences.
- Fasthand `--font-fasthand` for Handwritten accent for emotional kickers and signatures - the 'Listen!' above the hero headline, the 'Open Letter' section intro. One weight, one size, used at most once per section. This is the human voice in an otherwise architectural system; it appears only where the brand needs warmth over precision.
- Aspekta 500 `--font-aspekta-500` for Aspekta 500 - detected in extracted data but not described by AI

## Avoid

- Don't introduce a chromatic accent color for buttons, links, or text - the system has none
- Don't use square or 4-8px radius on cards - the 32px radius is structural to the brand
- Don't apply the decorative rainbow illustration style to icons, controls, or functional graphics
- Don't use Aspekta weight 500 for body text - reserve it for button labels and single-word emphasis
- Don't add background colors to sections - the system relies on whitespace and the warm-white canvas for separation
- Don't use gradients on UI elements - the system is flat and matte, elevation comes from shadow only
- Don't set letter-spacing to 0 or positive values on display sizes - the tight tracking is signature

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
