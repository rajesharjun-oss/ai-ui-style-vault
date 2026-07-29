# Sana Agents

Source: [Refero Style](https://styles.refero.design/style/5bfbe8b0-de0e-470f-b130-929f50437160)  
Reference site: [https://sana.ai](https://sana.ai)  
Captured: 2026-07-29  
Refero published: 2026-03-05T20:20:57.000Z  
Refero modified: 2026-06-05T00:57:14.759Z  
Theme: light  
Category: AI

## Style Summary

Explore Sana Agents's light AI design system: Ink Black #0a1217, Paper White #ffffff colors, Sana Serif, Sana Sans typography, and DESIGN.md for AI agents.

North star: Lime spark on editorial white

## What To Borrow

- Ink Black `#0a1217` as Primary text, dark card surfaces, sign-up panel, filled primary buttons on light backgrounds
- Paper White `#ffffff` as Light supporting surface for subtle backgrounds and section separation. Do not promote it to the primary CTA color
- Frost Wash `#e4eff7` as Soft tinted surface for light product cards and secondary panels the only chromatic step between paper white and ink black
- Stone Gray `#85898b` as Muted helper text, footer labels, and desaturated secondary copy
- Obsidian `#000000` as Hairline borders, nav text, and input outlines where the sharpest contrast edge is required
- Electric Lime `#cdfe00` as Green supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Sana Serif Hero display headline only. A weight-400 serif at 72px is the system's signature move: most AI brands shout with bold sans, Sana whispers with editorial type and lets the scale carry authority. The serif counterforms and bracket serifs give the wordmark a literary, humanist quality absent from typical product UI. `--font-sana-serif` for the source typography voice
- Sana Sans All UI, body, navigation, buttons, and subheadings. The 450 weight is a distinctive mid-step between regular and medium used for button labels and nav links instead of jumping to 500, producing quieter emphasis. Tabular numerals (tnum) and lining figures (lnum) are always on, giving all numeric data a consistent grid. `--font-sana-sans` for the source typography voice
- source-defined base spacing with comfortable density
- Source radius system: cards 24px, inputs 24px, buttons 9999px

## Avoid

- Do not use Sana Serif below 56px weight 400 at small sizes loses its authority and reads as thin/generic
- Do not place #cdfe00 on #ffffff or #e4eff7 surfaces the contrast is insufficient and the lime loses its electric quality
- Do not introduce a second accent color the system is monochromatic with exactly one chromatic note, adding more dilutes the poster-like discipline
- Do not apply drop shadows to cards or panels depth comes from the white frost ink surface stack, not elevation
- Do not use sharp corners (0px radius) on any container the 24px radius defines the system's soft, tactile personality
- Do not center-align body text, card content, or navigation links only the hero display headline gets centered treatment
- Do not add gradients, patterns, or background imagery to surfaces the design language is pure flat color blocks

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
