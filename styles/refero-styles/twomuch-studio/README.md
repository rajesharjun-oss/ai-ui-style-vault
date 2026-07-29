# TWOMUCH.STUDIO

Source: [Refero Style](https://styles.refero.design/style/12b3e1b6-31b9-4843-9b3b-8f39c9dd1474)  
Reference site: [https://twomuch.studio](https://twomuch.studio)  
Captured: 2026-07-29  
Refero published: 2026-04-30T02:36:58.895Z  
Refero modified: 2026-06-05T06:40:13.466Z  
Theme: light  
Category: Agency

## Style Summary

Explore TWOMUCH.STUDIO's light Agency design system: Gallery Plate #e5e7eb, Carbon #000000 colors, ABCMonumentGrotesk typography, and DESIGN.md for AI agents.

North star: floating museum of curiosities

## What To Borrow

- Gallery Plate `#e5e7eb` as Primary canvas and hairline dividers the infinite gray field that hosts floating objects and borders nearly every surface in the system
- Carbon `#000000` as Primary text, icon strokes, and the dark pill in the nav bar the only true black in the system, used for type and high-contrast marks
- Chalk `#f4f4f4` as Elevated surface above the canvas cards, panels, and lighter button fills that need to lift off the gray field
- Paper White `#ffffff` as Inset surfaces and inverse text on dark fills the cleanest white available for maximum contrast pop
- Concrete `#dedede` as Tertiary surface and muted button fill one step darker than Chalk, used where a surface needs weight without drama
- Voltage Lime `#e2ff70` as Primary action fill and highlight accent the only chromatic button/link background in the system, applied to the Menu pill and active link states to switch a control on
- ABCMonumentGrotesk Sole typeface across all UI body, labels, nav, headings, buttons, icons, links. The single medium weight with uniformly negative tracking (~-0.48px) gives every label a compressed, display-poster feel regardless of size. Avoid pairing with a secondary face; the constraint IS the identity. `--font-abcmonumentgrotesk` for the source typography voice
- 4px base spacing with compact density
- Source radius system: tags 9999px, pills 9999px, small 4px, buttons 9999px

## Avoid

- Do not introduce a second typeface, a second weight, or positive letter-spacing the monochrome grotesque is the voice
- Do not add drop shadows, glows, or elevation tiers the system is flat by design
- Do not use a chromatic fill other than Voltage Lime for any button or link Concrete and Chalk are the only neutral fills
- Do not frame imagery in rounded cards or bordered containers let objects touch the canvas directly
- Do not use the Oxide Brown (#68340e) as a UI color it belongs inside imagery and printed artifacts only
- Do not stack more than two surface levels on a single screen (e.g. Chalk card on Gallery Plate is fine; a third nested card is not)
- Do not center-align body copy or use large type sizes the system stays compact and left-aligned, max 22px

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
