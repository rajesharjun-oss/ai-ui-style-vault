# Vucko

Source: [Refero Style](https://styles.refero.design/style/cc5b19fd-12cf-4b30-801c-8a0363646e48)
Reference site: [https://vucko.co](https://vucko.co)
Captured: 2026-07-31
Refero published: 2026-04-30T00:34:40.876Z
Refero modified: 2026-06-05T12:02:08.192Z
Theme: light
Category: Agency

## Style Summary

Explore Vucko's light Agency design system: Ink #000000, Paper #ffffff colors, Suisse Int'l typography, and DESIGN.md for AI agents.

North star: oversized type on white gallery floor - a type-specimen book where the wordmark is the room.

## What To Borrow

- Ink `#000000` for Primary text, all borders, dark surface blocks, and the hero wordmark - the structural backbone of every screen
- Paper `#ffffff` for Hairline borders, dividers, input outlines, and card edges on light surfaces. Do not promote it to the primary CTA color
- Faint Ash `#eeeeee` for Subtle surface tint for secondary cards or de-emphasized blocks, barely distinguishable from Paper
- Steel `#888a8b` for Muted secondary text and ghost-list items in service lists - the only non-black text color, used to create tonal hierarchy without introducing hue
- Charcoal `#222222` for Alternate dark surface for nav or panel backgrounds - a softer dark than Ink when full black is too severe

- Suisse Int'l `--font-suisse-intl` for Sole typeface across the entire system. Weight 700 carries all display and heading roles up to 211px for the hero wordmark; weight 400 handles body and link text. The 211px weight-700 wordmark with -0.057em tracking is the signature - it turns the brand name into a room-scale installation. Weight 500 appears in nav and transitional text. The aggressive negative tracking on display sizes (-0.057em at 211px, -0.020em at 55px) tightens the Swiss grotesque geometry into a denser, more monolithic block - the type is meant to read as architecture, not as text.

## Avoid

- Never add colored CTA buttons - this system uses underlined text links and neutral pill elements only
- Never use drop shadows, glow effects, or any form of CSS elevation - depth comes from whitespace and contrast alone
- Never center body text - all running text should be left-aligned
- Never use borders thicker than 1px
- Never introduce chromatic colors into the UI chrome - color belongs exclusively inside project showcase content
- Never use display sizes (55px+) for body copy or secondary content - reserve them for headlines and service titles only
- Never break the whitespace rhythm - maintain 58px minimum between major sections and let the type do the work

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
