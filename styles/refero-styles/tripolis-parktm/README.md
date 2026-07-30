# Tripolis-ParkTM

Source: [Refero Style](https://styles.refero.design/style/bce52fd3-ac16-4e67-a45f-78bfc2350aad)
Reference site: [https://www.tripolis-park.com](https://www.tripolis-park.com)
Captured: 2026-07-30
Refero published: 2026-04-30T02:46:01.954Z
Refero modified: 2026-06-05T12:54:09.326Z
Theme: light
Category: Other

## Style Summary

Explore Tripolis-ParkTM's light Other design system: Aurora Lilac #b9a3e8, Deep Iris #7c4fb8 colors, Matter, Matter typography, and DESIGN.md for AI agents.

North star: luminous violet portal - soft lavender light bleeding through frosted glass edges, achromatic content floating above.

## What To Borrow

- Aurora Lilac `#c5b0ec` for Hero gradient start, atmospheric section backgrounds - the soft entry tone of the brand's signature violet wash
- Deep Iris `#7c4fb8` for Hero gradient deep stop, section transition anchors - the rich violet terminus that gives the gradient its weight
- Midnight Ink `#000000` for Primary text, heading strokes, hairline borders, icon fills, link color
- Carbon Mist `#2d2d2d` for Secondary text, subdued headings - softer than pure black for less critical copy
- Frost White `#ffffff` for Page canvas, card surfaces, text on dark/gradient backgrounds, ghost button fill
- Ash Veil `#b5b5b5` for Muted helper text, disabled states, tertiary metadata
- Smoke Line `#cccccc` for Hairline dividers, subtle structural lines, secondary borders
- Pale Mist `#e2e2e2` for Light borders, input field outlines, card edge definition
- Concrete Gray `#808080` for Surface variation, muted backgrounds, placeholder fills

- Matter `--font-matter` for Primary workhorse sans - body copy at 14px and 18px, subheadings at 27px. The humanist proportions and subtle warmth make long-form reading comfortable. Tabular numerals ('tnum') are enabled site-wide, signaling precision and data-readiness across all sizes.
- Matter `--font-matter` for Medium-weight emphasis - used for key headings and callouts at 27px and 47px with -0.025em tracking. The medium weight (not bold) keeps the voice measured and confident rather than aggressive.
- Matter `--font-matter` for SemiBold display weight - reserved for the most prominent headings at 47px with -0.024em tracking. The jump from Medium to SemiBold at the same size is rare and intentional: it creates a deliberate weight tier for hero-level statements.
- IvarHeadline `--font-ivarheadline` for Serif display face for editorial-style headings at 47px. The contrast with Matter's sans body creates a typographic duet - serif headlines anchor emotion and permanence, sans body delivers clarity. Tracking at -0.015em to -0.01em keeps the serif tight and contemporary rather than traditional.

## Avoid

- Don't introduce additional colors to the palette - the system is achromatic + violet gradient. No green, blue, red, or warm accents outside the gradient.
- Don't use border-radius greater than 0px on any component - no rounded buttons, no pill tags, no curved cards. The sharp geometry is intentional.
- Don't set headings at weights above 600 (SemiBold) - the system relies on the Medium-to-SemiBold tier, not heavy/black weights.
- Don't apply drop shadows or elevation effects - the design uses flat surfaces with hairline borders for separation, never shadows.
- Don't use the gradient on small UI elements (buttons, badges, icons) - it belongs only on large atmospheric surfaces.
- Don't set body text below 14px or above 18px - the 14-18px range is the only readable zone for this system.
- Don't mix serif and sans within the same heading - choose IvarHeadline OR Matter for any single headline, not both.

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
