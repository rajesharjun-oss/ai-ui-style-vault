# Atelier Deux-Ce

Source: [Refero Style](https://styles.refero.design/style/d531f0ec-ea94-4a40-b568-3073ff2bd8ed) 
Reference site: [https://deux-ce.com](https://deux-ce.com) 
Captured: 2026-07-29 
Refero published: 2026-05-11T00:08:45.904Z 
Refero modified: 2026-06-03T20:25:01.829Z 
Theme: light 
Category: Agency

## Style Summary

Explore Atelier Deux-Ce's light Agency design system: Ink Black #000000, Canvas White #ffffff colors, Helvetica, minion-3 typography, and DESIGN.md for AI...

North star: Sunlit editorial gallery

## What To Borrow

- Ink Black `#000000` for Body text, headings, nav links, hairline borders, and link underlines - the single type color across the entire system
- Canvas White `#ffffff` for Page background, card surfaces, reverse text on dark photographic regions
- Warm Linen `#eee5da` for Soft section background, the first step off pure white - gives a page the warmth of unbleached paper
- Pale Sage `#d8ddc6` for Tinted section panels, the dominant non-white canvas tone
- Driftwood `#d8d0c5` for Deeper warm section background, used when a panel needs to recede from Pale Sage
- Olive Stone `#afb371` for Saturated warm section background - the deepest neutral step before any chromatic color enters
- Weathered Taupe `#9c978a` for Muted section background, used sparingly as a quieter alternative to Olive Stone
- Soft Pebble `#aaaaa4` for Light warm-gray section background, the coolest of the earth-tone neutrals
- Garden Green `#259558` for Footer background only - the single chromatic accent in the system, used as a deliberate closing beat rather than a brand color spread across the UI

- Helvetica `--font-helvetica` for Primary UI and editorial type - body copy, navigation, links, project captions, category filters, and all functional text. Weight 400 for body and metadata, weight 600 reserved for the wordmark and the few moments that need emphasis. The system stack ensures identical rendering across platforms without depending on a webfont.
- minion-3 `--font-minion-3` for Editorial accent serif - used for body paragraphs and select headings where a literary, book-page quality is desired. The contrast between this transitional serif and the geometric Helvetica mirrors the brand's positioning: strategy + craft, editorial + commercial.

## Avoid

- Do not add box-shadows, drop shadows, glows, or gradient overlays - hierarchy comes from color and image, never from elevation
- Do not introduce saturated colors beyond the single footer green - the palette is warm earth tones, period
- Do not round corners on cards, buttons, images, or tags - 0px radius is non-negotiable
- Do not use filled buttons, ghost buttons, or pill buttons - the system has no button component, only text links and the footer band
- Do not use icons beyond a single minimal hamburger - the site is image-led, not icon-led
- Do not set type in negative letter-spacing - the positive 0.02-0.04em tracking is a defining choice and must not be tightened
- Do not add decorative borders thicker than 1px hairlines, and never use border colors outside the neutral scale

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
