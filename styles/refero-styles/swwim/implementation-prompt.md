# AI Implementation Prompt

Build a Swwim-inspired interface using this source-derived style bundle.

Reference site: https://www.weswwim.com
Theme: light
Category: Agency
North star: Cobalt wave with floating luxury objects.

Use these palette anchors:

- Cobalt Current `#1658b3` for Hero background, primary surface flood, outlined-link borders - the single color that defines every full-bleed section
- Deep Channel `#0d3c88` for Darker blue for gradient depth in decorative graphics, icon accents, footer bands
- Electric Ripple `#015fee` for Violet wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Abyssal Ink `#01295f` for Darkest blue used inside SVG decoration and deep gradient stops - never as text or button
- White Canvas `#ffffff` for Page background, body text on blue, primary pill button fill - the neutral that carries white sections and inverts on blue
- Cloud Border `#e5e7eb` for Hairline dividers, card borders, separator rules across all white surfaces - the structural neutral of the system
- Carbon `#000000` for Body text on white, icon fills in black-mode illustrations
- Nude Clay `#eee1d9` for Warm flesh-tone accent inside decorative illustration fills and strokes - the only chromatic neutral, used to humanize blue compositions

Use these typography anchors:

- Baton Turbo `--font-baton-turbo` for Display and oversized headlines only - the 151px hero weight is the signature choice, a single weight (400) stretched across 14px to 151px to create the full editorial scale
- Greycliff `--font-greycliff` for Body, UI labels, nav, buttons, badges, footer - the working typeface at three weights, with 500/700 reserved for small headings and nav emphasis

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1440px.
- Section gap: 64px.
- Card padding: 24px.
- Element gap: 8-16px.

Build these component patterns where relevant:

- White Pill CTA: Primary action button
- Ghost Nav Button: Secondary header action
- Header Logo Lockup: Brand mark in navigation
- Hero Headline: Primary page statement
- Hero Body Caption: Supporting hero copy
- Dive In Link: Anchor for scroll
- Service Marquee: Horizontal service ticker
- Product Float Image: Decorative product crop
- White Surface Card: Content container on white
- Icon: UI iconography

Do:

- Use Baton Turbo only for display and oversized headlines - 29px and up; never set it below 20px
- Set the hero headline at 151px on the cobalt background, line-height 1.0, all-caps, with at least one product image overlapping the letterforms
- Use 9999px radius for every button, tag, and pill control - there are no rounded-corner cards or inputs in this system
- Keep surfaces flat: 1px #e5e7eb hairline borders separate content, never drop shadows
- Let #1658b3 carry full-bleed sections as the dominant surface; reserve white for content pages and #0d3c88 for footer/gradient depth
- Use Greycliff 500 for interactive labels and small headings, 400 for body, 700 sparingly for emphasis
- Place a 1px white vertical divider between the wordmark and the descriptor in the header lockup

Avoid:

- Do not use Baton Turbo for body copy, nav labels, buttons, or anything below 20px - it loses its editorial voice at small sizes
- Do not introduce drop shadows, glows, or multi-layer elevation stacks - the system is intentionally flat
- Do not add chromatic colors outside the blue family plus the single #eee1d9 flesh tone accent
- Do not center the hero composition in a clean symmetrical layout - the scattered overlapping product crops are the signature
- Do not round card corners or input fields; the only radius in the system is the 9999px pill
- Do not use 151px type outside the hero; the display scale steps sharply down to 48px
- Do not break the blue monochrome with a contrasting CTA color - the white pill on blue IS the action pattern

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
