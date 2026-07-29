# Daniel Triendl

Source: [Refero Style](https://styles.refero.design/style/14f10100-a102-427a-88d1-7cc80cbb332d) 
Reference site: [https://www.danieltriendl.com](https://www.danieltriendl.com) 
Captured: 2026-07-29 
Refero published: 2026-04-30T01:23:12.280Z 
Refero modified: 2026-06-05T05:44:23.324Z 
Theme: light 
Category: Agency

## Style Summary

Explore Daniel Triendl's light Agency design system: Obsidian #000000, Canvas White #ffffff colors, Times, UniversalSans 425 typography, and DESIGN.md for...

North star: White gallery wall for loud art

## What To Borrow

- Obsidian `#000000` for Primary text, hairline borders, avatar stroke, ghost button outlines - the only ink on the page; borders are the structural device, not shadows
- Canvas White `#ffffff` for Page background, card surface, nav fill - the gallery wall itself
- Plaster Gray `#f2f2f2` for Pill navigation background, subtle surface for tag chips, soft section washes
- Ash Gray `#9b9b9b` for Muted secondary text, caption labels under illustrations, hairline borders on less prominent elements

- Times `--font-times` for Body, captions, labels, links, footer - a deliberate serif choice for UI body copy, the kind of editorial-museum-label voice most portfolios replace with sans-serif
- UniversalSans 425 `--font-universalsans-425` for Headings, emphasized body, link text - a neutral grotesque that steps in when the Times serif is too quiet
- UniversalSans 625 `--font-universalsans-625` for Button text, nav labels, small caps - the only medium weight in the system, used exclusively for clickable elements to give them a slightly firmer voice
- Rza `--font-rza` for Brand wordmark / logo only - a custom display face that gives the header a distinct editorial signature, never used elsewhere

## Avoid

- Do not introduce any chromatic UI color - green, red, blue, or accent hues - the palette is black/white/gray by design
- Do not add box-shadows to illustration cards; the single shadow allowed is the floating pill nav (rgba(0,0,0,0.1) 0px 4px 4px)
- Do not use Times for headings at large sizes; it is a 14px label face, not a display face
- Do not mix Rza into body copy or labels - it lives only in the brand wordmark
- Do not use #9b9b9b for body text on white - it fails contrast (2.8:1); reserve it for meta/tags on black or as a hairline border
- Do not add padding or chrome around illustration images - the image fills its grid cell edge-to-edge
- Do not create filled buttons; every interactive element is ghost/outlined (#000000 border, no fill)

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
