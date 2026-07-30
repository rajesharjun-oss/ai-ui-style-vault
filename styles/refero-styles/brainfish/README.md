# Brainfish

Source: [Refero Style](https://styles.refero.design/style/800734fd-eb95-41f3-b6f4-15fc19e127f0)
Reference site: [https://www.brainfishai.com](https://www.brainfishai.com)
Captured: 2026-07-30
Refero published: 2026-05-07T22:40:32.620Z
Refero modified: 2026-07-03T11:18:40.180Z
Theme: light
Category: AI

## Style Summary

Explore Brainfish's light AI design system: Lime Sprint #a3e635, Paper White #ffffff colors, Geist, Fraunces typography, and DESIGN.md for AI agents.

North star: lime-marker editorial broadsheet - a near-monochrome page where a single vivid green stroke does all the work

## What To Borrow

- Lime Sprint `#a3e635` for Green action color for filled buttons, selected navigation states, and focused conversion moments.
- Paper White `#ffffff` for Primary page canvas and inverse text on dark surfaces
- Cream `#fcfff7` for Warm off-white surface for cards, stat tiles, and footer - a barely-there yellow-green tint that distinguishes a lifted surface from the page without introducing a new color
- Ink `#262626` for Primary text color, default border, icon stroke, and hard shadow color. This is the single dark token that does structural work across text, lines, and elevation
- Black Ink `#000000` for Strongest display text and filled icon glyphs where maximum weight is needed inside a headline or pull-quote
- Depth `#303030` for Dark button and surface background - used for the large primary action blocks in the nav and hero where a heavier fill than ink is needed but true black would be too harsh
- Rule `#e5e5e5` for Hairline borders, card outlines, footer dividers, and the soft separator between sections
- Muted `#525252` for Secondary body text, supporting descriptions, and the slightly softer voice below a heading
- Muted Gray `#737373` for Tertiary helper text, badge labels, copyright fine print, and the most de-emphasized text in the hierarchy
- Mint Edge `#7ee2b8` for Green accent for outlined action borders, linked labels, and lightweight interactive emphasis
- Mint Wash `#dcfff1` for Gray action color for filled buttons, selected navigation states, and focused conversion moments

- Geist `--font-geist` for Primary interface and headline face. Used for navigation, buttons, body copy, and most display text. Weight 600 carries the display sizes (28-56px) with consistently negative letter-spacing; weight 400 carries body and caption. Tight tracking on headings (-0.0200em) compresses the geometric forms into a more editorial density rather than the wide airy SaaS default
- Fraunces `--font-fraunces` for Display serif reserved exclusively for one or two italic emphasis words inside a Geist headline - the word 'every', 'actually', 'B2B complexity'. This single serif italic inside a sans-serif sentence is the site's editorial signature: it signals that the system thinks in terms of typeset prose rather than product copy. Never used for body, buttons, or full headlines
- Phosphor-Fill `--font-phosphor-fill` for Phosphor-Fill - detected in extracted data but not described by AI

## Avoid

- Don't introduce a second chromatic accent beyond lime and mint - the system is monochrome with exactly two purposeful color moments (lime for action, mint for live status)
- Don't use soft blurred drop-shadows - every shadow in the system is a 2px solid offset in #262626 ink, or it doesn't exist
- Don't round buttons to 8px+ - the button radii are 4px or 0px, never pill-shaped on the main UI (pills are reserved for tags and status indicators only)
- Don't use Fraunces for body text, buttons, or full headlines - the serif is only for the italic emphasis word inside a Geist sentence
- Don't use #000000 for borders or large fills - reserve true black for the strongest display text weight, and use #262626 ink for all strokes, borders, and structural dark
- Don't add gradients to body backgrounds or card surfaces - the only gradient in the system is the soft lime radial halo in the hero
- Don't apply uppercase 0.08em tracking to body copy or headings - reserve it for tiny labels, badge chips, and tabular meta data (e.g. 'PERSONALIZING FOR SARAH', 'ROLE:')

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
