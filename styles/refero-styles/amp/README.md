# amp

Source: [Refero Style](https://styles.refero.design/style/261a4ad3-e835-4f7a-beb7-72187f84d462) 
Reference site: [https://ampfit.com](https://ampfit.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T23:15:37.674Z 
Refero modified: 2026-06-03T19:15:38.833Z 
Theme: light 
Category: E-commerce

## Style Summary

Explore amp's light E-commerce design system: Amp Orange #ff6105, Amp Glow #ffa069 colors, PublicaSans typography, and DESIGN.md for AI agents.

North star: warm orange pill on cool white. The design feels like a premium fitness product photographed in a sunlit loft: one object, one accent, one confident typeface doing all the work.

## What To Borrow

- Amp Orange `#ff6105` for Primary action fill, active step badge, accent rule, and brand strokes - the only chromatic color in the interface. Used at high contrast on white surfaces (7.0:1 against #ffffff) and as a warm border tint on cards and inputs
- Amp Glow `#ffa069` for Orange supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Peach Wash `#ffdfcd` for Soft highlight surface for featured cards and step accents. A near-gray peach that stays quiet while adding warmth to a card stack
- Ink `#0a0a0a` for Primary text, logo mark, button text. 19.8:1 against white - the highest-contrast neutral in the stack
- Carbon `#292b2a` for Secondary text and nav links, slightly softer than Ink. Icon strokes also draw from this level
- Slate `#7a7b7b` for Neutral form states, badge text, and quiet UI feedback where color should stay understated.
- Ash `#a2a3a2` for Disabled link text and placeholder-level text - the quietest text tone before disappearing
- Graphite Hairline `#e5e5e5` for The dominant border color across the site - dividers, card borders, button outlines, and structural rules. By far the most-used neutral (1628+ borderColor occurrences)
- Fog `#dfe0df` for Soft border for cards and body blocks where #e5e5e5 reads as too crisp against off-white
- Bone `#e5e7eb` for Neutral button fill (88 occurrences) - the ghost/secondary button background. A light step above canvas
- Canvas White `#ffffff` for Page background, card surfaces, button text on dark and orange fills. The base of the surface stack
- Linen `#f3f4f3` for Off-white alt surface - secondary button fills and surface tints where pure white is too clinical
- Charcoal `#202120` for Dark elevated surface for cards, headers, and contained panels.
- Smoke `#3c3e3d` for Heading underline accent in dark sections, heavier than Carbon

- PublicaSans `--font-publicasans` for The only typeface in the system. Light 300 for display headlines, Regular 400 for body and UI, Medium 500 for buttons and emphasis. Tracking tightens with size: -0.036em at 72-78px, -0.030em at 48px, -0.020em at 32px, -0.010em at 16-18px, near-zero at body. The progressive tightening gives display sizes a magazine-cover feel while body text stays open and readable.

## Avoid

- Don't introduce a second accent color or a secondary brand hue - the system is monochrome + one orange, and any chromatic addition breaks the rationing.
- Don't use weight 600 or 700 in PublicaSans; the system tops out at 500. Heavier weights are not part of the type scale.
- Don't apply shadows to cards, images, or non-primary buttons. Flat-with-hairline-border is the default; elevation is a privilege, not a default.
- Don't use the 50px radius on anything except the primary CTA and inputs. 24px is the cap for secondary buttons, 5px for cards.
- Don't set display text in all-caps or with positive letter-spacing. Tracking only tightens as size grows; never loosens.
- Don't fill large areas with #ff6105. The orange is a punctuation mark - let it punctuate, not paint.
- Don't mix rounded and square corner systems on the same page. Pick from the 5 / 8 / 24 / 32 / 50 ladder and stay on it.

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
