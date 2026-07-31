# Mr. Pops

Source: [Refero Style](https://styles.refero.design/style/ab7996ed-e0ed-40a0-81a5-d37f19ef35b0)
Reference site: [https://mrpops.ua/en](https://mrpops.ua/en)
Captured: 2026-07-31
Refero published: 2026-04-30T01:23:52.125Z
Refero modified: 2026-06-05T08:18:53.842Z
Theme: light
Category: E-commerce

## Style Summary

Explore Mr. Pops's light E-commerce design system: Cherry Marquee #b00e2f, Cream Bisque #fee5ca colors, Cervo, HelveticaNeueCyr typography, and DESIGN.md...

North star: retro ice cream parlor on cream paper. A bright white shopfront with cherry-red trim, stacked marquee letters, and warm cream cards beneath full-bleed food photography.

## What To Borrow

- Cherry Marquee `#b00e2f` for Brand accent, heading text, link color, icon stroke, outlined button border, footer headline - vivid warm red used as the single chromatic signal across an otherwise cream-and-white interface
- Cream Bisque `#fee5ca` for Secondary surface for cards, callout panels, and the cart/bag detail button - warm near-white that reads as paper, not gray
- Canvas White `#ffffff` for Page background, card surface, input fill, button text on dark
- Ink Black `#000000` for Primary body text, icon fills, heavy borders, SVG fill - the only true dark
- Slate Mid `#aaaaaa` for Muted secondary text, disabled placeholders, low-emphasis dividers

- Cervo `--font-cervo` for Display and headings only. Set extremely tight (line-height 0.75 on the 144px hero, 0.9 on 64-72px) and tracked slightly outward at 0.05em - the condensed letterforms and compressed leading make the headline read as a hand-painted sign rather than a web type block. Weight 400 carries the body, weight 500 amplifies emphasis within the display.
- HelveticaNeueCyr `--font-helveticaneuecyr` for Body, UI, navigation, footer, input, captions. Light 400 weight throughout with generous 1.3-1.4 leading on running text - the whisper-weight keeps chrome from competing with the Cervo display, so the marquee headline always wins the eye.

## Avoid

- Don't fill a button solid Cherry Marquee - the brand signal is the red outline, not a red block.
- Don't apply drop shadows to cards, buttons, or panels - depth comes from cream surfaces, not elevation stacks.
- Don't set Cervo with line-height above 1.0 on display sizes; the compressed leading is the signature.
- Don't introduce gray or cool neutrals - every neutral should be warm (cream, white) or pure black.
- Don't use a second chromatic accent - Cherry Marquee is the only color allowed beyond the cream/black/white system.
- Don't switch the canvas to dark or use a dark-mode pattern - the brand is locked to a sunlit light theme.
- Don't set negative letter-spacing on Cervo - the 0.05em outward tracking is what makes the marquee read as signage.

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
