# David Kirschberg

Source: [Refero Style](https://styles.refero.design/style/004f4856-4b01-4c23-a9fb-866303d5013b)
Reference site: [https://kirschberg.co.nz](https://kirschberg.co.nz)
Captured: 2026-07-31
Refero published: 2026-04-30T02:00:06.909Z
Refero modified: 2026-06-05T10:27:56.829Z
Theme: dark
Category: Agency

## Style Summary

Explore David Kirschberg's dark Agency design system: Obsidian #181818, Graphite #262626 colors, Inter, twkLausanne typography, and DESIGN.md for AI agents.

North star: midnight gallery wall - a darkened room where spotlit work is the only color, and the frame around it is intentionally invisible.

## What To Borrow

- Obsidian `#181818` for Page canvas, primary background - the dominant surface that recedes so work thumbnails advance
- Graphite `#262626` for Elevated surface, card thumbnail backgrounds, and content containers that need to sit one level above the page
- Bone `#fafafa` for Primary text, hero headlines, card titles - near-white that reads as soft rather than clinical against the dark canvas
- Ash `#a3a3a3` for Muted secondary text, subtitles, card descriptions - one step quieter than primary text for hierarchy without color

- Inter `--font-inter` for All body text, subtitles, card titles, UI labels, navigation - single weight (400) across every context, relying on size and color contrast rather than weight shifts for hierarchy
- twkLausanne `--font-twklausanne` for Sole display face for the hero headline - a custom typeface with tight tracking and unusually compressed line-height that gives the 32px headline editorial gravitas without bold weight. The -0.04em letter-spacing is aggressive for body size but measured for display, pulling characters close enough to read as a unified mark rather than individual letters

## Avoid

- Never add drop shadows, inner shadows, or box-shadows to any element - depth comes from surface color contrast only
- Never introduce accent colors, brand colors, or saturated hues into the UI chrome - the palette is locked to four neutrals
- Never use font weights other than 400 - hierarchy is built through size and color (Bone vs Ash), not weight
- Never use sharp corners on containers - all surfaces are rounded (16px or 24px)
- Never stack project cards in a multi-row grid - the gallery is a single horizontal scroll row only
- Never add gradients, textures, patterns, or decorative backgrounds to the interface
- Never use letter-spacing wider than -0.009em on body text - the slight tightening is part of the voice

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
