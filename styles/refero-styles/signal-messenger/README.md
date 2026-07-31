# Signal Messenger

Source: [Refero Style](https://styles.refero.design/style/41c479a9-7b41-445b-9ea7-c7a6331828f0)
Reference site: [https://signal.org](https://signal.org)
Captured: 2026-07-31
Refero published: 2026-02-27T11:31:08.000Z
Refero modified: 2026-06-05T07:59:46.810Z
Theme: light
Category: Other

## Style Summary

Explore Signal Messenger's light Other design system: Signal Blue #2c6bed, Deep Signal #2942ff colors, Inter, system-ui typography, and DESIGN.md for AI agents.

North star: Frosted privacy glass. A nearly white room washed in pale blue light, with one vivid blue line marking every door you can open.

## What To Borrow

- Signal Blue `#2c6bed` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Deep Signal `#2942ff` for Navigation links and brand mark anchors - slightly cooler and more electric than Signal Blue, reserved for chrome-level interaction
- Signal Sky `#9dbbf8` for Hero section wash, large decorative panels - soft periwinkle that bathes the page in brand color without overwhelming
- Signal Mist `#a5cad5` for Secondary feature panel backgrounds - desaturated teal that recedes behind content, used to break the page rhythm without adding chroma
- Ink `#1b1b1b` for Primary body and heading text - soft black at AAA contrast on every surface, the dominant typographic color
- Slate `#404654` for Secondary body text, subdued paragraphs - cool gray with a faint violet cast that echoes the brand blue
- Twilight `#3c3744` for Footer background - muted purple-black that grounds the page in a warm dark wash without pure black harshness
- Fog `#e9e9e9` for Hairline borders, dividers, footer text - the structural neutral that separates content bands
- Paper `#f6f6f6` for Page canvas - off-white that warms the stark white without going cream
- White `#ffffff` for Light supporting surface for subtle backgrounds and section separation. Do not promote it to the primary CTA color

- Inter `--font-inter` for Sole typeface across the entire site. Weight 800 headlines are anti-soft - paired with tight 1.07-1.14 line-heights they create near-solid blocks of type that anchor the page. Weight 600 handles buttons and subheadings with a confident mid-weight. Weight 400 body at 1.50 line-height provides generous reading rhythm. The extreme contrast between 800 display and 400 body is the typographic signature.
- system-ui `--font-system-ui` for system-ui - detected in extracted data but not described by AI

## Avoid

- Don't use filled blue buttons on white backgrounds - outlined buttons are the primary CTA pattern and should not be overridden
- Don't add gradients, drop shadows beyond the defined elevation token, or decorative borders - the design relies on flat color bands for structure
- Don't use colors outside the defined palette - no additional chroma, no warm accents, no status colors beyond the blue family
- Don't set headline line-height above 1.20 - loose leading destroys the dense, confident type character
- Don't use pill-shaped buttons (9999px radius) - the 8px radius is a deliberate choice that distinguishes Signal from typical consumer apps
- Don't add photography, abstract graphics, or illustration styles other than the halftone dot technique - the visual personality is singular
- Don't use Inter at weights other than 400, 600, or 800 - 500 and 700 are absent from the type system for a reason; the three-weight gap is the scale

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
