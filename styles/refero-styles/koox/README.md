# Koox

Source: [Refero Style](https://styles.refero.design/style/d1ca41ff-1bcc-4081-b1fd-bdcf380ba749)
Reference site: [https://koox.co.uk](https://koox.co.uk)
Captured: 2026-07-31
Refero published: 2026-04-30T03:03:21.722Z
Refero modified: 2026-06-05T09:15:11.291Z
Theme: light
Category: E-commerce

## Style Summary

Explore Koox's light E-commerce design system: Tile Grout #d25a24, Cold-Press Green #113722 colors, Helvetica typography, and DESIGN.md for AI agents.

North star: Brutalist cold-press lab - white tile, sticker print, stencil voice.

## What To Borrow

- Tile Grout `#d25a24` for Signature brand border and link accent - orange tile-line strokes that frame cards, links, and section edges with the warmth of fired clay against the clinical white canvas
- Cold-Press Green `#113722` for Primary action fill - the dark botanical green of filled CTA buttons, footer band, and category button backgrounds, signaling the product inside without resorting to food-photo greens
- Sticker Crimson `#6b1229` for Hard-offset shadow accent - deep burgundy that throws a zero-blur 5px shadow under stickers and emphasized buttons, turning flat elements into screen-print layers peeled onto the page
- Noir `#000000` for Navigation, body text, and default border color - the unyielding black that carries every paragraph, icon stroke, and card hairline
- Glacial White `#ffffff` for Page canvas, card surface, and reverse text on dark nav and green CTAs - the clinical white tile of the entire system
- Ash `#efefef` for Soft card border and subtle fill - the gray grout between white surfaces, used for hairline dividers and recessed card frames
- Char `#232323` for Heading color and deep-surface accent - nearly-black tone for the heaviest display text and occasional dark bands
- Concrete `#cccccc` for Mid-gray utility border and muted body text - quieter dividers where full black would be too loud
- Fog `#d7d7d7` for Input field border - neutral resting-state outline for form fields
- Slate `#646464` for Input text and icon fill - secondary legibility gray for form labels and small icon detail
- Pewter `#808080` for Decorative low-emphasis border and text - rarely used, appears on tertiary UI marks

- Helvetica `--font-helvetica` for All UI and editorial text. The choice of system Helvetica is deliberate - it reads as lab-label stencil rather than fashion-serif sophistication. Weight 900 headlines shout at 40-48px in all-caps with positive tracking, weight 400-500 carries body copy at 14-18px. No custom display face: the system itself is the brand.

## Avoid

- Do not use negative letter-spacing - the brand's voice depends on positive tracking that gives text room to shout
- Do not apply soft drop shadows, blurs, or multi-layer elevation stacks; elevation is one color and one offset
- Do not introduce additional brand hues beyond Tile Grout orange, Cold-Press green, and Sticker crimson
- Do not use 6px+ border radius or pill-shaped buttons - 5px is the maximum softness in this system
- Do not set body text in anything but weight 400-500 Helvetica; weight 700+ is reserved for display, navigation, and marquee
- Do not place light text on white or dark text on the dark-green band without testing AAA contrast
- Do not use the #6b1229 crimson as a fill - it is a shadow layer, not a brand color

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
