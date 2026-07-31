# Honk

Source: [Refero Style](https://styles.refero.design/style/ca4708f7-7175-4da2-a47f-ce8f5e601f99)
Reference site: [https://honk.me](https://honk.me)
Captured: 2026-07-31
Refero published: 2026-04-30T02:08:25.009Z
Refero modified: 2026-06-05T07:59:25.038Z
Theme: light
Category: Productivity

## Style Summary

Explore Honk's light Productivity design system: Honk Blue #008fff, Honk Sky #00a0ff colors, Honk Header, Honk Sans typography, and DESIGN.md for AI agents.

North star: Cobalt billboard with a yellow highlighter slash

## What To Borrow

- Honk Blue `#008fff` for Full-viewport page canvas, hero background, all top-level sections - the electric blue IS the brand surface, not a secondary accent
- Honk Sky `#00a0ff` for Secondary blue for gradient bands, large decorative shapes, and depth layers behind the primary canvas
- Signal Yellow `#ffe400` for Accent words inside headlines, heading border underlines, and highlight punctuation - the only chromatic accent on the blue field, used sparingly for emphasis rather than decoration
- Honk White `#ffffff` for Hairline borders, dividers, input outlines, and card edges on light surfaces. Do not promote it to the primary CTA color
- Carbon `#111111` for Primary text on light surfaces, dark borders, near-black detail work - used where text leaves the blue field
- True Black `#000000` for SVG fills, graphic detail, maximum-contrast text where the design needs to drop to absolute black
- Slate `#363636` for Secondary graphic fills, dark illustration detail, softer-than-black accents in SVG work
- Game Green `#3fcc6b` for Phone screen content (in-game UI inside device mockups) - a single-hue secondary color reserved for product-internal screens so the blue/yellow/white trio stays clean on the marketing surface

- Honk Header `--font-honk-header` for Hero and section display headlines - custom heavy display face at a single 52px size, tightly tracked at -0.012em. This is the signature wordmark voice: chunky, loud, slightly condensed, designed to read at billboard scale on the blue field
- Honk Sans `--font-honk-sans` for Body copy, sub-headings, button labels, link text, footer, icons - a neutral grotesk covering the full UI scale from 13px micro-labels to 19px lead paragraphs. Negative tracking across the board (-0.026em at 13px, -0.006em at 19px) tightens the grotesque to feel modern rather than airy

## Avoid

- Don't use white or light-gray page backgrounds for marketing screens - the design system assumes the blue field is always present, so a white page reads as broken.
- Don't use #ffe400 for body text, button backgrounds, or large fill areas - Signal Yellow is a word-level highlight only, not a surface color.
- Don't introduce a third saturated color to the marketing surface (purple, red, orange) - only the blue field, yellow accents, white text, and the green inside device mockups are permitted.
- Don't use heavy drop shadows on cards, buttons, or the phone mockup - elevation comes from color contrast against the blue, not from shadow stacks.
- Don't split the headline across more than 3 lines or highlight more than 2 words with yellow - the system relies on a single punctuation moment, not scattered emphasis.
- Don't use a different font family for sub-headings, buttons, or links - Honk Sans at varied weights covers the entire UI; Honk Header is display-only.
- Don't use the 6px-radius token on cards or large panels, and don't use the 16px-radius token on buttons - keep small-radius on small elements, large-radius on large surfaces.

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
