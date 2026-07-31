# Design Full-Time

Source: [Refero Style](https://styles.refero.design/style/80b2cc74-62c5-4898-bc2b-12aa94ed2943)
Reference site: [https://designfulltime.com](https://designfulltime.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:16:16.400Z
Refero modified: 2026-06-05T11:34:34.235Z
Theme: dark
Category: Other

## Style Summary

Explore Design Full-Time's dark Other design system: Pure Black #000000, Surface Black #111111 colors, Inter typography, and DESIGN.md for AI agents.

North star: black-box cinema with a single warm spotlight

## What To Borrow

- Pure Black `#000000` for Page canvas, dominant background - absorbs everything so content and the warm gradient banner can command attention
- Surface Black `#111111` for Card backgrounds, elevated panels, filled neutral button surface - one step off the canvas creates depth without gray noise
- Lifted Charcoal `#252525` for Mid-elevation surfaces, hover states, and subtle card depth - bridges the page black and border tones
- Border Gray `#343434` for Hairline dividers, card outlines, table rules - defines structural edges in a flat world
- Edge Gray `#4d4d4d` for Heavier borders on outlined buttons and grouped control frames
- Muted Text `#888888` for Secondary body text, metadata, timestamps, supporting copy
- Helper Gray `#a0a0a0` for Body text borders and subtle helper text where full white feels too loud
- Pure White `#ffffff` for Primary headings, nav text, button text, logo fill - the only color allowed to compete with the gradient banner
- Amber Glow `#fa3a19` for Promotional banner start - the cool-yellow origin of the warm spotlight gradient (also gradient)
- Ember Orange `#ff8a00` for Supporting palette color for small decorative accents when the core palette needs contrast. Do not promote it to the primary CTA color
- Crimson Heat `#ff8a00` for Supporting palette color for small decorative accents when the core palette needs contrast. Do not promote it to the primary CTA color

- Inter `--font-inter` for Sole typeface. Inter 700/800 for the wordmark and section headlines (confident, instructor-led); 600 for video titles and nav labels; 400 for body copy and metadata. No display-size font in the system - the brand keeps type compact (capped at 24px) and lets the gradient banner and video thumbnails carry visual weight instead.

## Avoid

- Don't introduce any blue, green, or purple accent - the brand is a two-tone system (monochrome + warm gradient) and extra hues will dilute the spotlight effect.
- Don't apply the warm gradient to body text, icons, or borders - reserve it for the promo banner surface and its CTA button only.
- Don't use shadows or heavy rounded corners (>=12px); the system is intentionally flat with 4-6px radii and hairline borders.
- Don't set headings above 24px; oversized display type breaks the compact, instructor-led feel.
- Don't use #111111 as a button background for primary actions - that role belongs exclusively to the warm gradient CTA.
- Don't introduce a second typeface, custom display face, or serif - Inter alone carries the brand at every weight.
- Don't place the gradient banner inside cards or repeated lists; it must remain a singular full-width conversion event.

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
