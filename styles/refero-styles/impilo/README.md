# Impilo

Source: [Refero Style](https://styles.refero.design/style/b44b0bb2-4ba3-4599-9706-3c3e0c8c2522)  
Reference site: [https://impilo.health](https://impilo.health)  
Captured: 2026-07-29  
Refero published: 2026-05-07T22:01:52.513Z  
Refero modified: 2026-06-03T19:11:00.884Z  
Theme: dark  
Category: Other

## Style Summary

Explore Impilo's dark Other design system: Deep Iris #16165c, Iris Shadow #232269 colors, Gilroy typography, and DESIGN.md for AI agents.

North star: Midnight clinical observatory a violet command console where health data glows in cyan.

## What To Borrow

- Deep Iris `#16165c` as Page canvas, hero background, primary surface the brand-defining midnight violet that sets the entire dark mode identity
- Iris Shadow `#232269` as Elevated card surfaces on dark canvas, secondary card backgrounds one step lighter than canvas for depth without breaking the violet atmosphere
- Iris Glow `#403cd5` as Mid-tone accent surface, footer background, highlighted metric blocks mid-violet for tertiary elevation and accent fills
- Iris Pulse `#5350cc` as Violet action color for filled buttons, selected navigation states, and focused conversion moments.
- Iris Border `#4846c6` as Card border outlines, subtle surface edges on dark mode keeps card perimeters defined without breaking the violet mood
- Iris Veil `#524fe1` as Body and card border accent, secondary surface outline lighter violet for hairline separators on dark surfaces
- Gilroy Sole typeface across the entire system weight 500 for body, links, buttons, cards; weight 600 for all headings and display. Gilroy's geometric humanism gives medical data a friendly, non-clinical warmth `--font-gilroy` for the source typography voice
- 4px base spacing with comfortable density
- Source radius system: tags 9999px, cards 24px, icons 7px, inputs 16px

## Avoid

- Never use a neutral gray (e.g., #1a1a1a, #2a2a2a) as a background all dark surfaces must stay in the violet family
- Do not mix weight 400 or 700 into the type system Gilroy speaks only in 500 and 600
- Never apply Clinical Cyan (#00b1ff) as a large solid fill on buttons or hero blocks it is a data/link color, not a surface color
- Do not use Mint Vital (#00ffaa) for error states or warnings its meaning is locked to positive health signals
- Avoid sharp corners (0-4px radius) on any container minimum 7px for icons, 16px for inputs, 24px for cards
- Do not introduce a second typeface Gilroy at weights 500/600 covers every typographic need
- Never use white (#ffffff) as a card background on the dark canvas the light inversion section is the only place Cloud White surfaces belong
- Do not use gradient transitions between dark and light sections the hard cut is a signature choice

## Bundle Contents

- [DESIGN.md](DESIGN.md): implementation notes.
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
