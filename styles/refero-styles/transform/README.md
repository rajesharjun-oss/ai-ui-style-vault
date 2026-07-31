# Transform

Source: [Refero Style](https://styles.refero.design/style/91939ad3-9e22-4256-a396-a1716a064ac4)
Reference site: [https://transformfestival.org](https://transformfestival.org)
Captured: 2026-07-31
Refero published: 2026-04-30T02:41:43.996Z
Refero modified: 2026-06-05T09:15:31.316Z
Theme: light
Category: Media

## Style Summary

Explore Transform's light Media design system: Blush Cardstock #f4ede9, Ink Black #000000 colors, Walsheim typography, and DESIGN.md for AI agents.

North star: stage poster pinned to warm blush paper

## What To Borrow

- Blush Cardstock `#f4ede9` for Page background, nav surface, dominant canvas - the warm paper everything sits on
- Ink Black `#000000` for Primary text, section headings, hairline borders, icon strokes
- Paper White `#ffffff` for Card surface, dark-section text, button labels on chromatic fills
- Ash Gray `#d9d9d9` for Alternate card surface when a quieter neutral block is needed
- Steel Gray `#767676` for Muted input borders, secondary helper strokes
- Festival Violet `#340068` for Full-bleed section bands, secondary filled CTA, footer background - heavy, immersive, sets the serious stage
- Spotlight Magenta `#fb00c2` for Primary filled CTA (DONATE), pull-quote text, heading borders, interactive emphasis - the loudest ink, reserved for moments that demand attention
- Curtain Orange `#ff1e00` for Pull-quote attribution, decorative heading borders - the warm third color that gives the palette a poster-like three-ink depth

- Walsheim `--font-walsheim` for Single-family type system used for everything from nav to display; the broad weight range (400-900) carries the entire tonal system so color never has to shout alone

## Avoid

- Do not introduce shadows, glows, or blur effects - depth is built through flat color, not elevation
- Do not use thin or light weights (under 700) for headings or display text
- Do not round cards, buttons, or images - only pills get radius
- Do not use Curtain Orange (#ff1e00) for buttons or CTAs - it is a decorative editorial accent only
- Do not place content directly on Spotlight Magenta or Festival Violet without testing contrast; always use Paper White for text on these surfaces
- Do not stack more than two chromatic accents in one component - the palette relies on restraint
- Do not use gradients - no gradient tokens exist and the system is deliberately flat

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
