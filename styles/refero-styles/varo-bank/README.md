# Varo Bank

Source: [Refero Style](https://styles.refero.design/style/2c05cf8d-97c5-4f35-96ef-eb53fc03ea81)
Reference site: [https://www.varomoney.com](https://www.varomoney.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:25:47.296Z
Refero modified: 2026-06-05T09:32:57.052Z
Theme: light
Category: Fintech

## Style Summary

Explore Varo Bank's light Fintech design system: Varo Violet #8c58d0, Deep Plum #42185f colors, Neue Haas Grotesk Display, National 2 Compressed typography,...

North star: neon bank statement on a sticky note - bold compressed type punched onto bright colored cardstock, held together by hairline black outlines

## What To Borrow

- Varo Violet `#8c58d0` for Primary action buttons, active nav, brand logo - the single saturated mid-violet that powers all interactive states
- Deep Plum `#42185f` for Dark accent surfaces, bold text on light cards, full-bleed dark band backgrounds - almost-black with violet undertone
- Lilac Mist `#cdb0fa` for Soft violet fill for selected/secondary surface states, tag backgrounds
- Coral Ember `#ed6c52` for Decorative section fills, icon highlights, dotted ticker text - warm chromatic punctuation that breaks up the violet dominance
- Salmon Wash `#f2a295` for Soft warm section background, muted coral - large-area color band that reads warm without screaming
- Butter Cream `#faefdc` for Pale cream surface band - the gentlest warm neutral, used as an alternate section background to white
- Lemon Zest `#fdf0af` for High-saturation yellow accent for card borders, feature callouts, ticker text - never a fill, always an outline or text
- Lime Pulse `#d4e84b` for Vivid lime used in feature card backgrounds and outlined graphic elements - the most attention-grabbing decorative color
- Forest Ink `#183428` for Deep green for dark feature card backgrounds and high-contrast text - rare but anchors green-themed cards
- Mustard Shadow `#4a4216` for Muted olive text and border accent on yellow/cream surfaces - never used as a fill
- Carbon `#000000` for Primary text, hairline borders, icon strokes - the dominant structural color
- Paper White `#ffffff` for Page canvas, card surfaces, button text on colored fills, inverted text on dark bands
- Soft Ash `#1c1c1c` for Near-black secondary text and borders - barely distinguishable from Carbon but used for slightly softer contrast
- Concrete `#939393` for Muted helper text, disabled states, secondary metadata
- Fog `#eff2f5` for Cool light-gray surface, pressed-button background, input field fill on dark sections

- Neue Haas Grotesk Display `--font-neue-haas-grotesk-display` for Body, subheads, small labels, button text, nav, form copy - the workhorse neo-grot at 12-72px. Weight 450 is the signature mid-weight for body copy; 500 for nav and labels; 400 for de-emphasized body. Letter-spacing tightens from 0.0200em at 12px to -0.0200em at 72px. Substitute: Inter, Sohne, or Neue Haas Grotesk Text Pro.
- National 2 Compressed `--font-national-2-compressed` for Display headlines only - used at 56-147px with line-height 0.80-0.95, the ultra-condensed proportions make type behave as a graphic block; weight 450 for default, 700 for maximum-impact stat callouts. Substitute: Oswald (700/600) or Antonio Bold. Letter-spacing: -0.0100em across the scale.
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI
- Times `--font-times` for Times - detected in extracted data but not described by AI
- Metropolis `--font-metropolis` for Metropolis - detected in extracted data but not described by AI

## Avoid

- Never use #8c58d0 as decorative fill or section background - it is reserved exclusively for interactive elements. Colored section bands use cream, salmon, plum, or lime instead.
- Never introduce drop shadows, blur effects, or multi-layer elevation. The system is intentionally flat - if a surface needs separation, add a 1px black border or a color change.
- Never mix line-heights above 1.0 with National 2 Compressed - the compressed letterforms need tight leading to read as a graphic block; open leading destroys the block effect.
- Never place a chromatic button on a chromatic section background of the same hue family - violet buttons only sit on white, cream, or dark plum.
- Never use a serif, monospace, or handwriting face - the two-family system (compressed display + neutral grotesk) is the entire typographic identity.
- Never round corners above 4px or use pill-shaped buttons; 4px is a hard rule across the system.
- Never use #0000ee or any browser-default link color; all link text and underlines are #000000 or section-matched.

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
