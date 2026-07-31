# Home

Source: [Refero Style](https://styles.refero.design/style/f9221afc-f5cb-4de8-89cd-40172e765124)
Reference site: [https://www.airtree.vc](https://www.airtree.vc)
Captured: 2026-07-31
Refero published: 2026-05-10T22:32:03.940Z
Refero modified: 2026-06-05T10:50:21.548Z
Theme: light
Category: Fintech

## Style Summary

Explore Home's light Fintech design system: Parchment Cream #f7f6e3, Ink Black #262d29 colors, Prody, SuisseIntl typography, and DESIGN.md for AI agents.

North star: Sunlit eucalyptus grove on warm parchment - the design rests on a cream page where ink-black type and a single electric yellow accent do all the talking.

## What To Borrow

- Parchment Cream `#f7f6e3` for Page canvas, card surfaces, bordered containers - near-gray cream that warms the entire interface and gives the whole site its paper-like calm; Outlined/ghost action borders, pill outlines, and interactive rings that echo the canvas tone - only visible against darker overlays
- Ink Black `#262d29` for Primary text, navigation, body copy, card borders, icon strokes - the only structural color, used for hairline definition and all readable content
- Electric Lemon `#ffff48` for Filled CTA buttons, active states, standout badges - a single saturated yellow that breaks the cream/ink calm to signal action; the ratio against #262d29 is 13.2:1 AAA

- Prody `--font-prody` for Display headlines - the signature voice. Used at 131px for the hero statement and 42px for secondary display; the heavy serif counters against the flat grotesque body to create editorial tension. Weight stays at 400; size alone carries the authority.
- SuisseIntl `--font-suisseintl` for Body copy, card titles, subheadings, UI labels - the working typeface. Weight 500 for emphasized text, 600 for card titles, 400 default. Sizes step 13 14 16 19 21 33 42 covering caption through heading.
- SuisseIntl Book `--font-suisseintl-book` for Navigation links, form input text, small button labels - a lighter cut of the same family for quieter interactive surfaces

## Avoid

- Never introduce a second saturated color; if something needs emphasis, use the yellow or a weight change, not a new hue.
- Never use #ffff48 for body text, icons, or decorative fills - it is a button color only.
- Never set display type under 80px; Prody at 33px or below loses its editorial character and reads as body text.
- Don't add box-shadow to cards or buttons; the system relies on border-radius and background contrast, not elevation.
- Don't place photography on a white background - always carry the #f7f6e3 warmth behind images to maintain the paper feel.
- Don't use gradients on buttons, cards, or page backgrounds; the only gradient in the system is the hero's subtle sky-to-cream wash.
- Don't bold Prody at 131px - its 400 weight is the brand voice; adding weight flattens the contrast with the body grotesque.

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
