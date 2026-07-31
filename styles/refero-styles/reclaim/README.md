# Reclaim

Source: [Refero Style](https://styles.refero.design/style/71c7b9ad-44cc-483f-9c53-3cf73e0522a4)
Reference site: [https://reclaim.ai](https://reclaim.ai)
Captured: 2026-07-31
Refero published: 2026-01-31T14:54:30.000Z
Refero modified: 2026-06-05T08:48:54.119Z
Theme: light
Category: Productivity

## Style Summary

Explore Reclaim's light Productivity design system: Lavender Canvas #ebefff, White Surface #ffffff colors, Poppins, Inter typography, and DESIGN.md for AI...

North star: lavender productivity workshop with violet ink

## What To Borrow

- Lavender Canvas `#ebefff` for Page background, hero section wash, footer background - the base atmosphere that distinguishes Reclaim from generic white SaaS
- White Surface `#ffffff` for Card surfaces, product mockup containers, button text on dark fills - pure white provides the resting layer above the lavender canvas
- Midnight Ink `#181d25` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color
- Pure Black `#000000` for Dark supporting neutral for text, icons, and strong contrast. Do not promote it to the primary CTA color
- Graphite `#111111` for Body copy and card text on light surfaces - sits just above pure black for slightly softer reading weight
- Slate `#474747` for Muted helper text, secondary descriptions, footer text - the workhorse for non-headline copy
- Charcoal `#2b2b2b` for Subheadings and emphasized body - bridges Midnight Ink headings and Slate body text
- Stone `#333333` for Tertiary text, breadcrumb-style labels
- Mist `#ececec` for Hairline dividers, decorative strokes, subtle separators
- Iris Violet `#5562eb` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Sapphire Violet `#3451e8` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Lavender Mist `#c2caf9` for Soft tints for product card highlights, decorative violet washes, outlined button borders - the muted cousin of Iris Violet
- Periwinkle `#96a0f3` for Disabled or secondary violet state, ghost button text on violet themes
- Indigo Depth `#151f8b` for Dark mode gradient anchor, deep accent for special promotional sections
- Focus Green `#7ac17b` for Green supporting accent for decorative details and low-frequency emphasis
- Mint Whisper `#daf0db` for Light supporting surface for subtle backgrounds and section separation
- Forest Edge `#14532d` for Dark green gradient stop for special promotional banners
- Brick `#5a1a1a` for Red supporting accent for decorative details and low-frequency emphasis. Use as a supporting accent, not as a status color

- Poppins `--font-poppins` for Exclusive brand typeface used for every text element. The 300-weight whisper at 70-90px for hero headlines is the signature move - most productivity apps use bold display weights, but Reclaim's thin Poppins headlines float above the page rather than punch through it. Letter-spacing is consistently tightened at -0.01em across all sizes, giving the rounded Poppins letterforms a slightly more compact, intentional feel rather than the default airy spacing.
- Inter `--font-inter` for Secondary fallback used only in 24 specific UI spots - effectively negligible. Treat as legacy or data-table context, not a design system font.

## Avoid

- Do not use drop shadows on cards - Reclaim uses border-radius and surface contrast instead of elevation
- Do not introduce a new accent color (orange, pink, teal) - the system is two-color: Iris Violet + Focus Green
- Do not use weight 700 or 800 for any text - Poppins tops out at 600 and most display text is 300-400
- Do not use 0px border-radius on any container - minimum 3px, standard 10px for cards
- Do not apply the violet-green gradient to buttons, backgrounds, or full headlines - only individual words in hero text
- Do not use pure white (#ffffff) as the page background - the lavender canvas is the brand base
- Do not use box-shadow for hover or focus states - use color shift to Sapphire Violet (#3451e8) instead

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
