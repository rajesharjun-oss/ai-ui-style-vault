# Artandcommerce

Source: [Refero Style](https://styles.refero.design/style/bc4b420c-be08-4165-95a3-c8338b5a9c3c) 
Reference site: [https://artandcommerce.com](https://artandcommerce.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:55:12.202Z 
Refero modified: 2026-06-03T20:30:10.078Z 
Theme: light 
Category: Agency

## Style Summary

Explore Artandcommerce's light Agency design system: Ink #000000, Bone #e7e7e7 colors, Adobe Garamond, Akzidenz Grotesk typography, and DESIGN.md for AI agents.

North star: art book spread on bone paper

## What To Borrow

- Ink `#000000` for Primary text, navigation labels, logo, link borders, footer type - the single graphic ink of the system. Every stroke, border, and character mark across the site
- Bone `#e7e7e7` for Page canvas, card surface, elevated surface - the warm near-white that holds all imagery and text
- Charcoal `#121212` for Secondary text and deep surface tone where slightly softer black is needed against bone

- Adobe Garamond `--font-adobe-garamond` for Editorial display and body serif. The single weight (400) does all the talking - no bold, no italic reliance. Used at 56px for display headlines (artwork titles, hero captions) with tight tracking -0.018em and 1.10 line-height, at 20px for introductory text and at 16px for body. The restraint of a single weight Garamond at display sizes creates an old-master gravitas: authority through historical type, not weight.
- Akzidenz Grotesk `--font-akzidenz-grotesk` for Functional sans-serif for all UI, navigation, labels, and metadata. Rendered almost exclusively in uppercase at 8-10px with aggressive positive tracking (+0.027 to +0.038em) - the effect is that of gallery wall labels, museum credits, and colophon text. Weight 500 highlights active nav, 700 for emphasis labels, 400 default. The grotesk never competes with Garamond for the reader's attention; it serves.

## Avoid

- Do not introduce any color - no brand accent, no CTA fill, no gradient, no status hues
- Do not use Garamond bold or italic; the serif speaks only at weight 400
- Do not apply border-radius to any element; the design is rigorously rectilinear
- Do not add box-shadows or drop-shadows - elevation is expressed through whitespace alone
- Do not mix sentence case into nav and labels; all Grotesk UI is uppercase
- Do not center body text or nav; the layout is flush-left with content anchored to the left edge
- Do not use display sizes below 56px or body sizes above 20px for Garamond - the scale is deliberately compressed

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
