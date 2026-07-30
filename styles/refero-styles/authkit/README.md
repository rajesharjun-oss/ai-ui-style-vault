# Authkit

Source: [Refero Style](https://styles.refero.design/style/e80231a2-e4d6-406a-a2c9-2e6109679690)
Reference site: [https://authkit.com](https://authkit.com)
Captured: 2026-07-30
Refero published: 2026-02-09T15:33:38.000Z
Refero modified: 2026-07-03T09:57:40.499Z
Theme: dark
Category: Dev Tools

## Style Summary

Explore Authkit's dark Dev Tools design system: Midnight Canvas #05060f, Steel Plate #2f343e colors, Untitled Sans, aeonikPro typography, and DESIGN.md for...

North star: Frosted glass cathedral at midnight

## What To Borrow

- Midnight Canvas `#05060f` for Page background, deepest card surface, badge fills - the near-black base everything else floats on
- Steel Plate `#2f343e` for Elevated surface, button fills for ghost/secondary actions, subtle panel backing
- Fog Veil `#9da7ba` for Muted body copy, card text - readable but stepped back from headlines
- Moon Mist `#c7d3ea` for Body text, secondary labels, muted helper copy
- Frost Glow `#d1e4fa` for Primary text fill for body and links, badge text, icon fills - the default luminous foreground
- Ice Highlight `#d8ecf8` for Light text on dark surfaces, inverse labels, and high-contrast captions. Do not promote it to the primary CTA color; Headline gradient - top-to-bottom fade from Ice Highlight to soft blue, used on the AuthKit wordmark and key headings
- Pure White `#ffffff` for Button text, input text, maximum-emphasis foreground
- Void Violet `#663af3` for Primary CTA fill - the only chromatic accent, used exclusively for the Continue/Submit button inside auth forms; vivid violet against near-black creates focused urgency without breaking the monochromatic mood
- Blueprint Blue `#b6d9fc` for Decorative icon accent, soft highlight wash on feature illustrations
- Ember Glow `#e46d4c` for Secondary accent - appears in demo/showcase contexts (logo recoloring swatches) for brand-color customization display
- Signal Blue `#027dea` for Secondary accent - appears in customization swatch grids to demonstrate brand-color options
- Deep Teal `#269684` for Secondary accent - appears in customization swatch grids
- Gridline Blue `#3f4959` for Shadow color for outer card drop-shadows - cool dark blue-grey gives elevation a tinted, on-brand feel rather than neutral black
- Glass Edge `#bad7f7` for Hairline borders on buttons, inputs, and links - inset 1px stroke of frosted blue-white that defines edges without hard lines
- Luminous Fill `#c7d3ea` for Badge fill and soft surface tint - translucent cool white for tag backgrounds and subtle UI washes

- Untitled Sans `--font-untitled-sans` for Body, UI, buttons, inputs, badges, small headings - the working typeface for everything functional
- aeonikPro `--font-aeonikpro` for Display headings only - the wordmark 'AuthKit', section headings, hero copy; weight 500 at 44-48px gives the wordmark a wide, calm presence rather than a bold shout
- dotDigital `--font-dotdigital` for All-caps eyebrow labels ('Introducing', 'Extensible by design', 'Shine bright') - 0.10em tracked monospace-flavored caps act as quiet section markers between the display type and body copy

## Avoid

- Do not introduce additional chromatic accents - the palette is monochromatic with one violet CTA; any extra hue breaks the system.
- Do not use solid colored borders; replace them with 1px inset rgba(186,215,247,0.12) strokes to preserve the glass aesthetic.
- Do not use bold weights (600+) on aeonikPro display headings - the wordmark's authority comes from weight 500 at large size, not volume.
- Do not apply conventional drop-shadows; the system reads elevation through inset glow + dark halo.
- Do not mix radius families on the same component type - every button is pill, every card is 16px, every badge is 6px.
- Do not place white (#ffffff) on background tints brighter than rgba(186,214,247,0.12) - the contrast floor collapses.
- Do not use the Skywash gradient on body text or buttons; reserve it for the display wordmark and the largest headings only.
- Do not introduce light-theme colors into core tokens even though the product supports light mode; the marketing site is dark-first, and light-mode demos are a product feature, not a design-system palette.

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
