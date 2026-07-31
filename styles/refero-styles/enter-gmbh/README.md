# Enter GmbH

Source: [Refero Style](https://styles.refero.design/style/87da9872-f6cc-4354-bf6a-1c02f0394d45)
Reference site: [https://enter-support.de](https://enter-support.de)
Captured: 2026-07-31
Refero published: 2026-04-30T03:45:50.501Z
Refero modified: 2026-06-05T07:29:32.566Z
Theme: mixed
Category: Dev Tools

## Style Summary

Explore Enter GmbH's mixed Dev Tools design system: Signal Orange #ff5000, Seafoam Panel #a5d3d4 colors, Maax Mono, Sofia-Regular typography, and DESIGN.md...

North star: Bauhaus poster workshop, midday sun

## What To Borrow

- Signal Orange `#ff5000` for Full-bleed section surfaces, geometric illustration caps, partner section canvas - carries warmth and authority across an otherwise achromatic text system
- Seafoam Panel `#a5d3d4` for Hero canvas and alternating section ground - a cool counterweight to the warm orange, used as full-bleed background, never as a text highlight
- Cream Stock `#f9f8ea` for Soft band surfaces between content sections - a paper-like off-white warmer than pure #ffffff, signals a transition zone
- Charcoal `#282828` for Filled button background, dark illustration blocks, heading accents - the loaded weight of the palette, softer than pure black
- Ink `#000000` for Primary body and heading text, hairline borders, icon strokes, link underlines - the dominant typographic color
- Pebble `#6a6a6a` for Muted border and separator color for subtle structural lines that shouldn't compete with text
- Paper `#ffffff` for Default page canvas, text on dark filled buttons, surface for content sections between color bands

- Maax Mono `--font-maax-mono` for Primary text and body - monospaced at body size gives the whole site a code-readout, technical-manual cadence. This is the signature choice: a service company writing like a terminal
- Sofia-Regular `--font-sofia-regular` for Display headings - a softer humanist sans used sparingly for larger section titles, providing the only non-monospaced typographic moment in the system
- Helvetica `--font-helvetica` for Micro UI text - marquee strips, tiny labels, and small interface markers; falls back to system monospaced where available

## Avoid

- Do not introduce a sans-serif body font - replacing the mono face destroys the technical-manual personality
- Do not use orange (#ff5000) as a button or link color - it's an architectural surface, not an interactive accent
- Do not add shadows, glows, or elevation effects to cards or buttons - the system is flat and hard-edged
- Do not use teal (#a5d3d4) for text or borders - it only works as a full-bleed surface
- Do not use border-radius values other than 25px on interactive elements - partial rounding breaks the pill vocabulary
- Do not place photography or product screenshots - the site is text-and-illustration only
- Do not add gradient transitions between color bands - every section boundary must be a hard seam

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
