# Acceptandproceed

Source: [Refero Style](https://styles.refero.design/style/f63b4703-db8b-4bc9-8d8f-17262b12d4b3)
Reference site: [https://www.acceptandproceed.com](https://www.acceptandproceed.com)
Captured: 2026-07-31
Refero published: 2026-04-30T02:41:30.031Z
Refero modified: 2026-06-05T10:02:22.728Z
Theme: light
Category: Agency

## Style Summary

Explore Acceptandproceed's light Agency design system: Ink #000000, Paper Warm #f9f7f3 colors, Messina Sans, Letterformvariations 04 Dmgx typography, and...

North star: editorial broadsheet on warm paper

## What To Borrow

- Ink `#000000` for Primary text, hairline borders, icon strokes, badge outlines, card outlines - the only structural line color in the system
- Paper Warm `#f9f7f3` for Page canvas, card surfaces, body backgrounds - the warm cream base layer for all content
- Bone `#ecebe7` for Raised surfaces, pill button fills, input fills, link backgrounds - one step warmer/darker than the canvas for tactile depth without shadows
- White `#ffffff` for Headline color on dark hero overlays, card highlight wash, inverted surface accents
- Graphite `#8c8c8c` for Secondary borders, muted metadata text, badge secondary text and borders - the warm mid-gray step in the neutral scale
- Ash `#a2a1a1` for Tertiary badge borders and subtle dividers - the lightest structural gray for the quietest separators
- Charcoal `#333333` for Input text and form field copy - softer than pure black for longer reading inside form contexts

- Messina Sans `--font-messina-sans` for The only workhorse typeface - used for everything from micro-labels (8px) to display headlines (72px). Weight 400 is the sole weight; hierarchy is created entirely by size and line-height, never by weight contrast. This produces a quiet, editorial voice where the type whispers at every level rather than shouting with bold.
- Letterformvariations 04 Dmgx `--font-letterformvariations-04-dmgx` for Decorative display face used very sparingly for typographic moments - an experimental or contrast voice to break the Messina Sans monotony, reserved for editorial flourishes only

## Avoid

- Don't introduce bold, semibold, or any non-400 weight. The single-weight system is the entire typographic voice; a bold headline would break the editorial whisper.
- Don't add any color - no blue links, no red errors, no green success states. Every state change uses #000000 #8c8c8c opacity shifts, or #f9f7f3 #ecebe7 surface steps.
- Don't apply drop shadows or box-shadows to any element. Depth is communicated by surface color and hairlines only.
- Don't use a border-radius outside the four-tier system: 3.4px (badges), 8px (cards/images), 20px (secondary buttons), 100px (pills/inputs). No 4px, no 12px, no 16px.
- Don't use uppercase tracking or letter-spacing increases for labels. The -0.01em tightening is consistent across the type scale - never widen it.
- Don't add icons, illustrations, or decorative graphics. Photography is the only imagery; everything else is type and hairline structure.
- Don't use colored hover states. Hover changes on links and buttons should toggle between #000000 and #8c8c8c text/border, or swap #ecebe7 #f9f7f3 surface inversion.

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
