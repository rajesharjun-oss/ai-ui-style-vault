# Yellowbird(R)

Source: [Refero Style](https://styles.refero.design/style/22cc86bc-6c5f-4413-a4a2-66b8ddc82ad0)
Reference site: [https://www.yellowbirdfoods.com](https://www.yellowbirdfoods.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:32:59.364Z
Refero modified: 2026-06-05T08:27:23.783Z
Theme: light
Category: E-commerce

## Style Summary

Explore Yellowbird(R)'s light E-commerce design system: Sunglow #ffe845, Sauce Bottle Black #000000 colors, Gooper, ABC Monument Grotesk typography, and...

North star: Retro condiment billboard in midday sun - a single yellow plane under a black sun, every letter drawn with a fat marker.

## What To Borrow

- Sunglow `#ffe845` for Brand canvas - the dominant page background across all sections, hero, footer, and announcement bar; also fills product category tags and sticker burst shapes
- Sauce Bottle Black `#000000` for Primary text, all borders and hairlines, product card strokes, mascot linework, and the filled primary action button background - does the heavy structural and typographic lifting
- Pure White `#ffffff` for Hairline borders, dividers, input outlines, and card edges on light surfaces. Do not promote it to the primary CTA color
- Buttermilk `#fbfaf2` for Alternate card surface for quieter product tiles - an off-white that reads as warm cream against the saturated yellow canvas
- Cool Link Blue `#007aff` for Ghost/outlined secondary action border - a borrowed utility color for low-emphasis links, never used for filled buttons or primary navigation

- Gooper `--font-gooper` for Signature wordmark display - the massive 'Yellowbird' logotype and any oversized display headings; a custom bubbly, ultra-chunky display face that functions as the brand's icon. Tight tracking (-0.028em) keeps the rounded forms from feeling wobbly at 91px
- ABC Monument Grotesk `--font-abc-monument-grotesk` for Primary workhorse - nav links, body copy, product names, section headings, button text, footer, and hero subhead. The single weight (400) carries all roles from 14px caption to 61px hero subhead, unified by negative tracking that tightens as size grows (-0.04em at 14px to -0.011em at 61px)
- Pitch Sans `--font-pitch-sans` for Secondary utility - used for badges, tags, micro-labels, and supporting metadata where a slightly more compact feel is needed. Weight 600 for badge text adds the only weight contrast in the system

## Avoid

- Never introduce a new chromatic color beyond the yellow/black/white/cream/blue set - the system's power is its two-color discipline
- Never add drop shadows, inner glows, or blur effects to cards or buttons - separation comes from solid black strokes, not elevation
- Never use the blue (#007aff) as a filled button background or for navigation; it is a ghost-border utility color only
- Never use a font weight heavier than 400 for Monument Grotesk; the face doesn't ship bold, and faking bold breaks the geometric evenness
- Never place body copy on white over the yellow canvas without a card surface - floating text on white feels broken; always commit to cream or pure white as a card surface
- Never use positive letter-spacing on body or display text - the only positive tracking (0.05em) is reserved for Pitch Sans testimonial attributions
- Never reduce the wordmark below 61px or substitute a standard display face for Gooper; the bubbly custom face is the brand's most recognizable element

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
