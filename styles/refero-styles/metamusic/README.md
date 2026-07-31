# MetaMusic

Source: [Refero Style](https://styles.refero.design/style/6ffe7b61-a418-4cbd-9e7a-a5129db6c589)
Reference site: [https://metamusic.ca](https://metamusic.ca)
Captured: 2026-07-31
Refero published: 2026-04-30T03:55:28.647Z
Refero modified: 2026-06-05T10:05:53.747Z
Theme: mixed
Category: SaaS

## Style Summary

Explore MetaMusic's mixed SaaS design system: Brand Blue #0066cc, Deep Indigo #0e2575 colors, Maison Neue, Spoof typography, and DESIGN.md for AI agents.

North star: editorial cream broadsheet with sticker-flat accents - a warm-paper canvas where oversized type and hard-offset shadows replace all decoration.

## What To Borrow

- Brand Blue `#0066cc` for Primary action background, link underlines, heading accents, card fills on light surfaces - the single chromatic voice that powers CTAs, active states, and iconography
- Deep Indigo `#0e2575` for Dark section backgrounds (feature/why panels), hero image frames - the only place a full-bleed surface goes deep and saturated
- Midnight Card `#213680` for Elevated card surface when sitting on Deep Indigo backgrounds - one step lighter than the panel to separate without using shadow
- Charcoal Ink `#101820` for Body text and dark-surface secondary fills - slightly cooler than pure black, anchors reading text without harshness
- Paper Cream `#f4f1ea` for Primary page canvas - the warm base that gives the whole site its editorial, printed feel
- White `#ffffff` for Card surfaces, nav background, button text on blue, input fills - the clean highlight layer above cream
- Lavender Mist `#e6e0f8` for Neutral form states, badge text, and quiet UI feedback where color should stay understated. Do not promote it to the primary CTA color
- Ice Blue `#e9f4ff` for Alternate light surface wash, subtle card background variant - the cool counterpoint to Paper Cream
- Peach Blush `#f7e1d5` for Icon circle backgrounds in audience/feature cards - the only warm accent that breaks the cream-on-cream
- Ash Border `#d6d6d6` for Hairline dividers, subtle borders on neutral surfaces - the quietest structural line

- Maison Neue `--font-maison-neue` for The sole workhorse font across body, nav, headings, buttons, inputs, cards, and footers. Weight 400 carries body and UI labels; 500 steps up to subheadings and nav; 600 owns display sizes (56-120px). The type behaves like a neo-grotesque with humanist warmth - readable at 12px, monumental at 120px. Negative tracking tightens aggressively at display sizes (-0.03em at 120px, -0.02em at 56-80px, -0.01em at 32-40px) so headlines sit visually compact despite their scale.
- Spoof `--font-spoof` for Reserved for a single accent heading or card label at 22px / weight 500. Its ultra-tight 0.90 leading and -0.02em tracking create a display-quality mark at a mid size - used as a typographic exclamation point, never as a workhorse. Free substitute: GT America or a tight condensed sans like Druk Wide.

## Avoid

- Do not use soft, blurred drop shadows - the hard 4px solid offset is the only elevation language in this system
- Do not introduce new chromatic colors; Brand Blue and Deep Indigo are the only saturated voices, and they must not share a surface
- Do not set display type without negative letter-spacing; positive tracking at 56px+ destroys the editorial feel
- Do not use 8px radius on cards or 24px radius on inputs - the three-tier radius system (24px / 9999px / 8px) is strict
- Do not place text directly on Peach Blush or Lavender Mist without checking contrast - both are surface washes, not text backgrounds
- Do not add a second outlined pill button to the same view; the Log-in outline is a one-per-header accent
- Do not center body text longer than a single line; the editorial system relies on left-aligned, ragged-right reading

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
