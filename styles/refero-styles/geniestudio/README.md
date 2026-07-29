# Geniestudio

Source: [Refero Style](https://styles.refero.design/style/2ffd50d4-93b7-4acf-9bc2-e86e61b63f27) 
Reference site: [https://geniestudio.app](https://geniestudio.app) 
Captured: 2026-07-29 
Refero published: 2026-05-07T22:40:42.087Z 
Refero modified: 2026-07-03T10:33:19.010Z 
Theme: light 
Category: AI

## Style Summary

Explore Geniestudio's light AI design system: Sky Tint #ebf5ff, Paper White #ffffff colors, Aeonik, Geist typography, and DESIGN.md for AI agents.

North star: soft daylight notebook - the kind with generous margins and a single bold pen stroke

## What To Borrow

- Sky Tint `#ebf5ff` for Page canvas and soft background washes - the defining ambient color that sets the daylight atmosphere
- Paper White `#ffffff` for Pure card surfaces, button text, and icon fills on dark controls
- Bone White `#fafdff` for Primary card surface and elevated panel backgrounds - a barely-blue white that feels paper-like
- Mist Gray `#f6f7f8` for Subtle secondary surfaces and section dividers
- Ink `#0a0d12` for All heading text, primary display type, and deep emphasis copy
- Charcoal `#181d27` for Filled button backgrounds and the dense visual anchor against the airy canvas
- Graphite `#535862` for Secondary body text and supporting copy
- Fog `#93979f` for Muted helper text, FAQ answers, and low-emphasis body
- Slate Shadow `#3b3d41` for Dark shadow tone behind buttons and elevated controls
- Sky Blue `#0099ff` for Inline highlight text and emphasis spans within body copy
- Lavender Wash `#f1e6ff` for Pastel card surface for feature tiles and category blocks
- Mint Wash `#d3f6e3` for Pastel card surface for feature tiles and category blocks
- Powder Blue `#cce7ff` for Gray wash for highlight backgrounds, decorative bands, and soft emphasis behind content

- Aeonik `--font-aeonik` for Display and heading face for all editorial moments - 148px hero headlines, 72px section openers, 48px card titles, 32px subheadings. Fixed at weight 500; the brand never goes bolder. Tracking pulls tight at -0.02em which gives the geometric forms a sculpted, almost engraved quality at large sizes. Substitute: 'Sohne', 'Inter', or 'General Sans'.
- Geist `--font-geist` for UI and body face for everything below the headline tier - body copy, buttons, labels, captions, card descriptions, nav links. Weight 500 is the workhorse; 600 only for tiny 10px micro-labels. The 18px / 20px sizes with -0.01em tracking carry the interface's conversational voice. Substitute: 'Geist', 'Inter', or 'Sohne'.

## Avoid

- Do not use bold weights (600+) for display headlines - Aeonik 500 is the ceiling
- Do not use 90 sharp corners on cards or buttons - minimum 16px, default 32px, pill 9999px
- Do not place saturated blue (#0069e0) as a button fill - it is an outline/accent color, not a CTA color
- Do not add box-shadows to content cards - depth comes from the canvas/surface color shift, not elevation
- Do not use body-weight black (#000000) for text - use #0a0d12, which has a hint of blue that ties to the canvas
- Do not mix more than two pastel washes in a single section - the pastel palette is for tile variety, not visual noise
- Do not set display type below 48px or use display sizes for body content - the scale has a hard floor for editorial moments

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
