# Co Projects

Source: [Refero Style](https://styles.refero.design/style/5c9743ad-fe33-4d21-9185-db012f6f96c7)
Reference site: [https://co-projects.xyz](https://co-projects.xyz)
Captured: 2026-07-31
Refero published: 2026-02-05T10:48:04.000Z
Refero modified: 2026-06-05T09:07:12.737Z
Theme: light
Category: Agency

## Style Summary

Explore Co Projects's light Agency design system: Paper White #ffffff, Graphite Ink #000000 colors, Alpha, Takt typography, and DESIGN.md for AI agents.

North star: black geometric sculpture on white void. Massive circular forms carved from a pure white gallery wall, where the only type is whisper-weight 400 and the only accent is the void between things.

## What To Borrow

- Paper White `#ffffff` for Page canvas, background of all surfaces, inner counter of the ring forms - the negative space that gives the black marks their mass
- Graphite Ink `#000000` for Primary mark fill, text, and the large circular ring forms. The sole chromatic-payload element in the system
- Fog Hairline `#e5e7eb` for Hairline borders, structural dividers, and subtle separator rules at 1px. The only gray in the palette and it never fills - it only divides

- Alpha `--font-alpha` for Primary face for nav, body, and display. Used at 16px for navigation labels and links (lineHeight 1.50), 29px for mid-scale headings, and 60px for the display headline (lineHeight 1.00 - headline sits tight on its baseline). The signature move is running 60px display text at weight 400, which reads as architectural line-drawing rather than shouted headline
- Takt `--font-takt` for Secondary face for body copy and 36px subheadings. Tight lineHeight (1.10-1.11) at all sizes gives it a compact, editorial-block feel - runs in long stacked paragraphs where Alpha would feel too austere. Weight 400 is the ONLY weight in the entire system

## Avoid

- Never add a shadow, blur, or elevation effect - the system is completely flat and any depth cue breaks the figure/ground purity
- Never introduce a color outside the three achromatic tokens - no accent hues, no tinted grays, no hover-state colors beyond opacity shifts
- Never use a font weight other than 400 - no 500, 600, 700, or 800 under any circumstance
- Never apply border-radius to buttons, cards, tags, or inputs - rectangular means sharp corners, always
- Never constrain the hero composition to a max-width container - let the geometric forms run full-bleed and crop at viewport edges
- Never add icons, illustrations, photography, or decorative graphics - the circle/ring IS the imagery
- Never use letter-spacing adjustment - all type sits at default tracking, the custom typefaces are already tuned

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
