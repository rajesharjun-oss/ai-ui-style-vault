# Afterglo

Source: [Refero Style](https://styles.refero.design/style/b13069df-7475-4b51-a734-621e3da75f8b)
Reference site: [https://myafterglo.com](https://myafterglo.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:50:16.808Z
Refero modified: 2026-06-05T07:25:15.695Z
Theme: light
Category: E-commerce

## Style Summary

Explore Afterglo's light E-commerce design system: Ivory Paper #f3f2ec, Sage Mist #e3e4df colors, Aeonik, Cardinal Fruit typography, and DESIGN.md for AI...

North star: Editorial boudoir printed on cream paper - quiet, tactile, typographic.

## What To Borrow

- Ivory Paper `#f3f2ec` for Page canvas, card surfaces, footer wash - the warm off-white that makes every photograph feel printed, not digital
- Sage Mist `#e3e4df` for Hairline borders, input outlines, subtle dividers, secondary card backgrounds - the cool-warm neutral that separates layers without contrast shouting
- Bone Gray `#cbc9bd` for Mid-tone neutrals for input shadows and muted surface fills - the bridge between ivory and ink
- Ink Black `#131313` for Primary text, filled buttons, icon strokes, navigation borders - slightly softer than pure black, reads as printer's ink rather than screen
- Pure Black `#000000` for Highest-contrast borders, pure ink for heaviest typographic moments and fine dividers
- Snow White `#ffffff` for Product card photography backdrop, badge fills - the cleanest white for product isolation
- Ember Coral `#f68e6d` for Footer background, singular warm accent - the one chromatic gesture in the system, used only when the design needs to feel touched, not seen
- Powder Blue `#7faad2` for Blue state accent for badges, validation surfaces, and short status labels. Do not promote it to the primary CTA color

- Aeonik `--font-aeonik` for Workhorse sans for navigation, body, buttons, product cards, and hero overlays. 500 weight for active nav, labels, and emphasis; 400 for body copy. The 132px display size at 0.80 line-height is the signature - oversized headlines that sit tight and confident over photography.
- Cardinal Fruit `--font-cardinal-fruit` for Display serif reserved for editorial moments: the 'FEEL YOUR SELF' statement, category callouts, and the small italic accent '(BEST)'. At 187px with 1.00 line-height it becomes the visual anchor of the page - a magazine-cover gesture that reframes the whole interface as editorial, not transactional.

## Avoid

- Do not use the powder blue (#7faad2) as a CTA or filled action - it is decorative only, reserved for soft badges and washes
- Do not apply drop shadows to cards, buttons, or images - the system stays flat; depth comes from type and photography
- Do not introduce border-radius values other than 5px - the system uses one rounding gesture, repeated exactly
- Do not use pure black (#000000) for large body text - reserve it for fine borders and heaviest display moments; use #131313 for readable text and buttons
- Do not place the Cardinal Fruit serif below 33px - it loses its editorial weight at small sizes; switch to Aeonik for anything under 33px
- Do not use gradients, glows, or color tints on buttons or interactive elements - the system is matte and flat
- Do not center-align body copy or product descriptions - the editorial language reads left-aligned with generous left margin

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
