# Drop

Source: [Refero Style](https://styles.refero.design/style/36d939b8-e3b5-45c7-8d81-f7c4d7c8fdaa)
Reference site: [https://www.usedrop.io](https://www.usedrop.io)
Captured: 2026-07-31
Refero published: 2026-04-30T03:17:53.629Z
Refero modified: 2026-06-05T09:14:49.382Z
Theme: light
Category: SaaS

## Style Summary

Explore Drop's light SaaS design system: Obsidian #101010, Pure White #ffffff colors, ABC Normal, Ivar Display typography, and DESIGN.md for AI agents.

North star: lavender editorial spread in bold serif. Lavender dusk washing over stark white pages, anchored by a confident slab-serif voice that commands the page like a broadsheet headline.

## What To Borrow

- Obsidian `#101010` for Neutral form states, badge text, and quiet UI feedback where color should stay understated. Do not promote it to the primary CTA color
- Pure White `#ffffff` for Page canvas, card surfaces, text on dark fills - the default surface that 60%+ of the page lives on
- Carbon `#1a1a1a` for Dark card surfaces for product mockups and the dark editorial band, barely distinguishable from Obsidian to create depth without color
- Mint Cream `#e5ede4` for Light pastel surface tint, used sparingly for soft card backgrounds that need warmth without chromatic commitment
- Sage Mist `#c7d8c5` for Near-gray green surface wash, appears as a muted canvas tint on light sections and soft card backgrounds
- Ash Gray `#9b9b9b` for Muted helper text, secondary borders, inactive UI elements - handles every de-emphasized text or border role
- Lavender Mist `#b8afda` for Dominant chromatic accent, large section backgrounds, circle diagram fills, decorative borders - carries the brand's pastel identity and appears more than any other chromatic color
- Ember Orange `#eb652b` for Orange wash for highlight backgrounds, decorative bands, and soft emphasis behind content.
- Electric Yellow `#f6f361` for Secondary accent for borders, highlights, and decorative geometric elements - neon-charged against black to create energy

- ABC Normal `--font-abc-normal` for Workhorse sans for body, nav, buttons, badges, and even large display sizes. The 300 weight is the signature - lightweight and editorial rather than the 600+ bold most SaaS sites use for headlines, giving Drop a quiet authority. Letter-spacing tightens aggressively at larger sizes (from -0.005em at 16px to -0.041em at 177px).
- Ivar Display `--font-ivar-display` for Reserved exclusively for the largest display headings - the 'OLD WORLD' / 'NEW WORLD' editorial moments. A serif with 0.78 line-height and -0.043em tracking at 169px creates slab-like density that reads as printed editorial rather than web type. Weight stays at 400 even at poster scale, trusting the size and serif personality to carry authority.

## Avoid

- Never use Ivar Display for body text, nav links, or anything below 60px - the serif personality overwhelms at small sizes
- Do not introduce a second chromatic accent color beyond the existing three (lavender, orange, yellow) - the palette is deliberately small
- Do not use box-shadows for elevation - Drop separates surfaces with hard color contrast (white vs black vs lavender), not depth
- Do not set display headlines to line-height above 1.0 - the tight leading is what makes the type feel printed rather than web-rendered
- Do not use sharp corners (0px radius) on any interactive element - even small UI should use at least 4-8px radius
- Do not place orange and yellow adjacent to each other - they vibrate against each other; let white or black separate them
- Do not center-align body text - left-align everything except display headlines and revenue figures

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
