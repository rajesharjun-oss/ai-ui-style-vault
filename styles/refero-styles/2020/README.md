# 2020

Source: [Refero Style](https://styles.refero.design/style/ac660bff-3b21-4753-a80f-3692da6e735e)
Reference site: [https://albumcolors.com](https://albumcolors.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:21:29.129Z
Refero modified: 2026-06-05T12:08:47.955Z
Theme: light
Category: Media

## Style Summary

Explore 2020's light Media design system: Signal Orange #e4822e, Olive Ink #4f503e colors, Helvetica LT Pro, Helvetica typography, and DESIGN.md for AI agents.

North star: Solid color poster wall. A single saturated color fills the viewport like painted drywall, and massive black type sits on top as if stenciled.

## What To Borrow

- Signal Orange `#e4822e` for Primary canvas - the full-viewport page background that changes on refresh; this is the design system
- Olive Ink `#4f503e` for Primary text, headline color, and the only outlined action accent (outlined-button borders, link underlines) - warm dark green-brown that pairs with the orange field without competing chroma
- Oxblood `#b13225` for Alternating surface variation - one of the page colors the background can take on refresh
- Burnt Sienna `#c97f40` for Alternating surface variation - secondary warm shade the canvas can adopt
- Near Black `#081618` for Alternating surface variation - deep cool surface the canvas can adopt, creates the darkest mode of the page
- Pearl `#feccc0` for Soft warm highlight - one of the lighter surface variations the canvas can adopt
- Sage Mist `#99aa91` for Soft cool surface variation - one of the muted color states the canvas cycles through
- Carbon `#000000` for Album cover backgrounds, deep text on light surface states
- Ink `#161616` for Album cover backgrounds and heavy dark surface tone
- Charcoal `#111111` for Album cover and card backgrounds within the grid
- Ash `#8d8d8d` for Mid-neutral for muted helper text and secondary surface states
- Paper `#ffffff` for Album cover backgrounds, text on dark surface states

- Helvetica LT Pro `--font-helvetica-lt-pro` for The sole typeface across all text - display, heading, body, button, link. A single weight (400 regular) is used at every scale, which is the most distinctive typographic choice on the site. The whisper-regular giant-size headlines are anti-convention; most poster/editorial sites use 700-900 for display type, and using the book weight at 137px makes the headline feel stamped rather than shouted - authority through stillness.
- Helvetica `--font-helvetica` for Helvetica - detected in extracted data but not described by AI

## Avoid

- Do not use filled buttons - a solid fill would compete with the canvas color; all actions are outlined borders or pure icons
- Do not add card frames, drop shadows, or elevation to album tiles - they sit directly on the canvas with no chrome
- Do not introduce a second typeface - the entire site is set in one family at one weight
- Do not center body text - copy aligns left, full-bleed, and wraps naturally
- Do not use a max-width container - the layout is always edge-to-edge
- Do not pair Olive Ink (#4f503e) text with a colored background outside the established palette (oxblood, sienna, near-black, sage, pearl) - the six surface colors are the only valid canvases
- Do not add line-height above 1.0 for any size above 21px - the tight leading (0.79-0.80) on display text is what makes the headlines feel like solid shapes

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
