# Fidele Editions

Source: [Refero Style](https://styles.refero.design/style/957da5c3-7063-4992-9d25-e255752dc9b3)
Reference site: [https://fidele-editions.com](https://fidele-editions.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:59:02.814Z
Refero modified: 2026-06-05T07:56:11.261Z
Theme: light
Category: E-commerce

## Style Summary

Explore Fidele Editions's light E-commerce design system: Fidele Blue #1664eb, Lighter Press Blue #4f89ec colors, Arial, BaselGrotesk typography, and...

North star: Risograph blue ink on warm cream paper. A single fluorescent blue floods headlines, the announcement bar, and a giant asterisk logo, stamped onto a flat cream stock with zero shadows and near-zero rounding - the page reads as a printed broadsheet, not a SaaS interface.

## What To Borrow

- Fidele Blue `#1664eb` for Headlines, nav links, brand asterisk, announcement bar fill, body borders - the single chromatic ink of the system; whenever color appears, this is it
- Lighter Press Blue `#4f89ec` for Secondary blue used for subtle borders, icon tints, and decorative strokes where Fidele Blue would dominate
- Link Blue `#006ce5` for Deeper blue for inline hyperlinks within running text, slightly darker than the primary to read as a separate interactive state
- Paper White `#f8f7ef` for Page canvas and card surfaces - a warm off-white that gives the entire system its print-stock identity; never use pure #ffffff for page background
- Card Cream `#e2e2df` for Elevated surface for cards, panels, and product tiles - one step warmer/darker than Paper White for layering without shadows
- Pure White `#ffffff` for Hairline borders, dividers, input outlines, and card edges on light surfaces. Do not promote it to the primary CTA color
- Press Black `#121212` for Body text, dark backgrounds, and the rare filled button - near-black rather than pure black, softening contrast on the cream stock

- Arial `--font-arial` for Arial - detected in extracted data but not described by AI
- BaselGrotesk `--font-baselgrotesk` for The sole typeface of the system. Book weight (400) for body and most UI; Regular (400) for lists and some headings; Bold (700) for the rarest emphasis. Display sizes (62px) use line-height 0.92 with -0.049em tracking - characters nearly touch. Small labels (14px) use +0.063em tracking - wide, airy, stamped. The contrast between these two tracking regimes is the type signature.
- OTMagister `--font-otmagister` for Occasional display headlines where a more editorial/serif-leaning voice is wanted. Same 62px display size and tight 0.92 leading as BaselGrotesk display, -0.016em tracking.
- GTStandard-M `--font-gtstandard-m` for GTStandard-M - detected in extracted data but not described by AI
- Assistant `--font-assistant` for Assistant - detected in extracted data but not described by AI

## Avoid

- Don't introduce drop shadows, inner shadows, or glow effects - the system is deliberately flat and reads as paper, not glass.
- Don't use any chromatic color other than Fidele Blue, Lighter Press Blue, and Link Blue - the cream + blue duotone is the entire palette.
- Don't use filled solid-color buttons for primary actions; the system's primary control is the outlined Fidele Blue action.
- Don't set display type with generous line-height (1.2-1.5) - the crushed 0.92 leading is a signature, not a default.
- Don't round cards, images, or tags beyond 4px; anything rounder breaks the print-stock metaphor.
- Don't add gradients, textures, or noise - surfaces are flat solids, period.
- Don't use #ffffff as a page background; it must remain the warm Paper White #f8f7ef to keep the editorial warmth.

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
