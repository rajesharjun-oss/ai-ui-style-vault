# Base44

Source: [Refero Style](https://styles.refero.design/style/e869e214-f672-4ac3-bfc2-bd25de7b003b)
Reference site: [https://base44.com](https://base44.com)
Captured: 2026-07-30
Refero published: 2026-03-16T14:12:04.000Z
Refero modified: 2026-07-03T10:50:53.599Z
Theme: light
Category: AI

## Style Summary

Explore Base44's light AI design system: Canvas Bone #faf9f7, Card White #ffffff colors, WixMadeforText, WixMisoRegular typography, and DESIGN.md for AI agents.

North star: sunlit notepad with a lime highlighter

## What To Borrow

- Canvas Bone `#faf9f7` for Page background, section bands, large surface fills - the warm off-white that defines the entire atmosphere
- Card White `#ffffff` for Card surfaces, elevated panels, input backgrounds, footer - pure white sitting on the bone canvas
- Ink Black `#0f0f0f` for Primary text, filled action buttons, icon strokes, nav color - the dominant near-black that carries all type and the filled dark CTA
- Graphite `#232529` for Secondary text, button text, nav strokes - slightly softer than Ink Black for de-emphasized copy
- Hairline `#d1d1d1` for Default 1px borders on cards, inputs, dividers - the thinnest structural line
- Soft Border `#e6e6e6` for Secondary borders, subtle surface backgrounds - softer than Hairline for nested edges
- Muted Ink `#a0a0a0` for Tertiary text, disabled states, muted icon strokes
- Lime Wash `#ebffb1` for Primary CTA fill (Start Building button) - a pale lime that glows against the bone canvas like a fresh highlighter mark
- Lime Edge `#ade900` for Green accent for outlined action borders, linked labels, and lightweight interactive emphasis. Do not promote it to the primary CTA color
- Ember Orange `#ff631f` for Logo color, decorative fill accents, secondary action - vivid orange used sparingly to anchor brand identity

- WixMadeforText `--font-wixmadefortext` for Primary UI sans - body text, buttons, nav, inputs, badges, all chrome. The geometric forms and slightly expanded tracking on small sizes (0.025em at 12px, 0.18em uppercase) give it a friendly, slightly humanist feel that keeps 16px body text comfortable to scan
- WixMisoRegular `--font-wixmisoregular` for Display headline face - used at 48-56px with tight tracking (-0.02em) and very tight line-height (1.05). The single weight at 400 creates a calm, confident headline that doesn't shout - authority through spaciousness. Body sizes (20-24px) share the same character, keeping the type system coherent across scales
- WixMisoLight `--font-wixmisolight` for Secondary display - lighter weight version for subheadings (25px) and lead body text (17px), creating tonal contrast against the Regular headlines. Same family guarantees harmony while the weight difference adds hierarchy without size jumps

## Avoid

- Don't add drop shadows to cards - the system uses background contrast (white on bone) for hierarchy, not elevation. Reserve the single shadow for the hero prompt card only
- Don't use #ff631f orange on text or large fills - it's reserved for the logo, decorative accents, and the submit circle inside the input
- Don't set headline weight above 400 - the system uses weight and tracking for hierarchy, not boldness. Heavier weights would break the calm, spacious feel
- Don't use saturated blue for links or actions - the system has no traditional 'info blue'; interactive elements are either lime, black, or ghost
- Don't create dark sections - the page is entirely light-mode. Use the sunset gradient band for atmospheric breaks, never a full dark background
- Don't use borders heavier than 1px - the hairline aesthetic is the entire structural language. Thicker borders feel heavy and corporate
- Don't use corner radii below 8px on any surface - the system rounds generously (8px cards, 30px hero card, 9999px pills). Sharp corners clash with the warm, friendly tone

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
