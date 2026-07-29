# Coda

Source: [Refero Style](https://styles.refero.design/style/0f0d4cb7-5109-4e81-8c8d-f6bd0441b27c) 
Reference site: [https://coda.io](https://coda.io) 
Captured: 2026-07-29 
Refero published: 2026-04-30T00:54:47.571Z 
Refero modified: 2026-06-05T07:32:20.599Z 
Theme: light 
Category: Productivity

## Style Summary

Explore Coda's light Productivity design system: Ink Black #212121, Pure White #ffffff colors, Calibre-R, Inter typography, and DESIGN.md for AI agents.

North star: Cream-paper workspace - warm editor's desk where bold black type and a single orange accent do all the work.

## What To Borrow

- Ink Black `#212121` for Primary text, heading fills, primary borders, and the structural ink color across all UI surfaces
- Pure White `#ffffff` for Default page canvas, card surfaces, button text on dark fills, and outlined-button fills
- Carbon `#000000` for Filled primary action background, hard offset shadow color, and high-contrast icon fills
- Cream Paper `#fff6ec` for Warm hero band, footer surface, and the signature alternate canvas that gives Coda its editorial mood
- Ash Border `#e0e0e0` for Hairline borders, card edges, and subtle dividers separating surfaces from canvas
- Graphite `#666666` for Secondary body text, muted helper text, and low-emphasis metadata
- Smoke `#8e8e8e` for Tertiary text, placeholder text, disabled labels, and nav item resting state
- Slate Button `#444444` for Secondary button borders and mid-weight icon strokes
- Ember Orange `#ee5a29` for Sole chromatic accent - heading highlights, section eyebrow text, decorative underlines, and brand-mark punctuation. The single warm note against an otherwise black-and-cream system

- Calibre-R `--font-calibre-r` for Display and section headlines. Custom geometric 700-weight face with extremely tight tracking that compresses letterforms into dense blocks of ink. The heavy + tight combination is Coda's signature - headlines feel carved rather than written. Substitute: Manrope 800 or DM Sans 800 with -0.03em tracking.
- Inter `--font-inter` for All UI text: body copy, nav links, buttons, labels, captions. Inter carries the entire functional layer; its near-default weights and tracking let the Calibre headlines lead.
- Tiempos-Headline `--font-tiempos-headline` for Occasional editorial subheading in a light serif weight - the soft counterpoint to Calibre's blocky display. Used sparingly for emphasis rather than hierarchy.

## Avoid

- Don't introduce a second chromatic accent - the system is monochrome plus a single ember orange.
- Don't use soft blurred drop-shadows on content cards; elevation is either the hard 8px/8px black offset or the two-layer rgba stack, nothing in between.
- Don't set body or subheading text in Calibre-R - it belongs only at 38px and above, 700 weight only.
- Don't apply rounded pill (9999px) radii to primary buttons; 8px is the system default.
- Don't place white cards directly on the cream band without a visible border or shadow - the value difference is too subtle.
- Don't use light grays (#8e8e8, #aeaeae) for primary text; reserve them for placeholder and disabled states only.
- Don't break the 4px spacing grid - all padding, gaps, and margins should snap to 4 / 8 / 12 / 16 / 20 / 24 / 32.

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
