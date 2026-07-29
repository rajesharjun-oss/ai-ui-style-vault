# ARTU

Source: [Refero Style](https://styles.refero.design/style/d1941450-00be-4988-beaa-76bb68ae09ff) 
Reference site: [https://artu.works](https://artu.works) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:55:23.951Z 
Refero modified: 2026-06-03T20:16:00.455Z 
Theme: light 
Category: E-commerce

## Style Summary

Explore ARTU's light E-commerce design system: Canvas White #ffffff, Ink Black #000000 colors, HelveticaNeuePro typography, and DESIGN.md for AI agents.

North star: Gallery wall on white paper. ARTU treats the browser as a museum spread - massive product photography, hairline rules, and a single shock of lime at the bottom edge to close the room.

## What To Borrow

- Canvas White `#ffffff` for Page background, card surface, image plate - the entire site sits on pure white
- Ink Black `#000000` for All text, hairline borders, navigation, link underlines, image frames - the sole structural color
- Terminal Lime `#d7ff66` for Footer band, surface highlight wash, terminal accent - high-chroma green that signals a page boundary the way a colored edge stops a gallery wall
- Signal Red `#ff1313` for Decorative border strokes, icon outlines, hairline rules in editorial layouts - used at sub-readable contrast as graphic punctuation, never as body text

- HelveticaNeuePro `--font-helveticaneuepro` for Universal type family for navigation, body, headings, inputs, and footer - the only weight on the site (400), set in all-caps across the nav and footer, with positive tracking 0.0140em-0.0240em that gives the single weight a mechanical, catalog-like cadence

## Avoid

- Don't introduce a second type weight, a serif, or a display face - 400 Helvetica is the system
- Don't use #ff1313 for body text, headings, or CTAs - its 3.9:1 contrast on white is the point; it belongs only in thin decorative strokes
- Don't add drop shadows, gradients, or glass effects - the site is flat by design
- Don't use rounded corners on any element - not images, not buttons, not tags
- Don't fill the page with the lime green - it only appears as the closing footer band
- Don't add a sticky header, sidebar, or modal - the layout is one continuous gallery scroll
- Don't break the all-caps nav convention with mixed-case menu items or sentence-case headings

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
