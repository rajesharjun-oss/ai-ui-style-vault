# Slite

Source: [Refero Style](https://styles.refero.design/style/607c2098-bbbb-40bb-b23e-adf2b72c63dd)
Reference site: [https://slite.com](https://slite.com)
Captured: 2026-07-30
Refero published: 2026-03-27T15:07:05.000Z
Refero modified: 2026-07-03T11:25:51.679Z
Theme: light
Category: SaaS

## Style Summary

Explore Slite's light SaaS design system: Parchment Cream #fdf9f4, Star White #ffffff colors, Garnett, UniversalSans typography, and DESIGN.md for AI agents.

North star: Warm parchment notebook with terracotta pen - every surface is cream paper, every accent a single ember-orange stroke.

## What To Borrow

- Parchment Cream `#fdf9f4` for Page canvas and primary card surface - the warm off-white that defines Slite's identity. Never use cold white #ffffff at the page level
- Star White `#ffffff` for Elevated surfaces - product mockup cards, tooltips, white-product interiors stacked on top of the cream canvas
- Dust Sand `#f9efe4` for Secondary surface and tag/chip background - a half-step darker than the canvas. Tag pills, secondary buttons, and warm-emphasis callouts
- Moon Silver `#ecedef` for Hairline borders, dividers, and 2px outlined button borders - the only border tone used at full opacity
- Shade Ink `#2d2f34` for Primary heading and body text - slightly warm near-black. The headline color
- Shade Charcoal `#3f434a` for Secondary body text, navigation labels, and subdued headings. Do not promote it to the primary CTA color
- Shade Slate `#5e646e` for Tertiary body text, captions, helper copy - the quietest readable gray
- Shade Fog `#9da3af` for Disabled states, placeholder text, and the lightest non-white neutral - used sparingly on the page
- Shade Dusk `#6a707c` for Small print and fine print text - pricing footnotes, micro-copy beneath headings
- Border Mist `#d9dde6` for Card borders and stroke at low contrast - slightly bluer than Moon Silver, used when a card edge needs to be felt but not seen
- Ember Orange `#f67748` for Primary action - filled CTA buttons, selected card border accent, featured testimonial card background, and the scribble-annotation color. The single saturated brand color, used sparingly so it always feels like a deliberate highlight
- Neptune Blue `#74a6f1` for Secondary action accent - used on at most one button per page (e.g. alternating testimonial CTA) and link-text accents. Never the primary CTA
- Verification Green `#479a53` for Green text accent for links, tags, and emphasized short phrases. Use as a supporting accent, not as a status color
- Verified Mint `#bbf7d0` for Green decorative accent for icons, marks, and small graphic details. Use as a supporting accent, not as a status color
- Tag Violet `#4b51c3` for Violet text accent for links, tags, and emphasized short phrases. Use as a supporting accent, not as a status color
- Illustration Violet `#6b70d6` for Decorative illustration fill - light-violet shapes in product mockups, paired with Tag Violet as a tonal pair

- Garnett `--font-garnett` for Display and editorial headings. Used at 64px (display), 36px (h1), 28px (h2), 24px (large body), 12px (small links). The serif-like Garnett paired with a humanist sans is Slite's signature typographic contrast - it makes the page feel like a designed document rather than a dashboard.
- UniversalSans `--font-universalsans` for Body text, UI controls, navigation, buttons, and supporting headlines. Carries almost all of the page's content. The 50px / weight 400 / line-height 1.5 hero variant is a deliberate departure from typical 700-weight display sizes - it lets the Garnett headline above do the work, while UniversalSans handles the breathing paragraph copy beneath.

## Avoid

- Do not introduce a second saturated color as a brand accent - #f67748 must remain the only chromatic surface color
- Do not use 700-weight UniversalSans at display sizes - 50px hero text is always weight 400
- Do not stack more than one shadow elevation on a single element; the three-layer shadow is the maximum
- Do not use pure black #000000 for body text - always #2d2f34 (Shade Ink) or #3f434a (Shade Charcoal)
- Do not use #ecedef or #d9dde6 as background fills - these are border tones only
- Do not break the pill/tag radius system with square chips or rounded-but-not-pill buttons
- Do not place #f67748 fills on large backgrounds (more than 20% of a section) - it dilutes the CTA signal

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
