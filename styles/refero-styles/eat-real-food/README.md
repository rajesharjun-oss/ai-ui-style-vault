# Eat Real Food

Source: [Refero Style](https://styles.refero.design/style/3d32f841-490d-4e5f-aba0-43c9d0c13130)
Reference site: [https://realfood.gov](https://realfood.gov)
Captured: 2026-07-30
Refero published: 2026-04-30T00:17:40.047Z
Refero modified: 2026-06-05T12:33:31.642Z
Theme: light
Category: Other

## Style Summary

Explore Eat Real Food's light Other design system: Press Ink #110000, Aged Parchment #fdfbee colors, Die Grotesk D, Die Grotesk B typography, and DESIGN.md...

North star: government health brief on cream parchment

## What To Borrow

- Press Ink `#110000` for Primary text, dark hero surfaces, filled pill buttons, navigation dots - near-black with a warm undertone replaces the cold #000000 to keep the palette feeling printed rather than digital
- Aged Parchment `#fdfbee` for Page canvas, body text on dark surfaces, filled button backgrounds - the warm off-white that gives the entire site its paper-like quality
- Newsprint White `#ffffff` for Card surfaces, elevated panels, button text on dark fills
- Wheat Field `#f3f0d6` for Accent surface, secondary button fill, soft highlight wash - a desaturated straw tone that sits between parchment and olive
- Fog `#e5e5e5` for Hairline borders, dividers, card edges - the structural neutral that defines component boundaries at 1px weight
- Dusty Brick `#8d7d7d` for Muted secondary text, small labels - warm gray-brown that recedes without going cold
- Ash `#bebcb3` for Subtle image borders, soft shadow base - warm gray for non-critical structural lines
- Stone `#d2d0c6` for Card shadow base tone, subtle elevation warmth
- Alert Red `#d50000` for Data emphasis blocks, statistics backgrounds, alarm callouts - the only chromatic color in the system, reserved for moments when numbers must cut through the editorial calm

- Die Grotesk D `--font-die-grotesk-d` for Display and heading - weight 700 only, the single heaviest voice in the system. Used at enormous sizes (96-170px) with extremely tight line-heights (0.84-0.96) that make headlines stack into solid editorial blocks. This is the voice that shouts.
- Die Grotesk B `--font-die-grotesk-b` for Mid-scale headings and emphasized body - the bridge between display and text. Slight negative tracking (-0.019em) tightens medium sizes without making them feel clinical.
- Die Grotesk A `--font-die-grotesk-a` for Body text, navigation, buttons, links, lists, cards - the workhorse. Negative tracking (-0.02em to -0.03em) at body sizes keeps the grotesque feeling sharp. Weight 600 is available for inline emphasis.
- Geist Mono `--font-geist-mono` for Monospaced labels, section markers, micro-copy - the only monospace voice. Wide tracking (+0.06em) gives it a typewriter/telegraph quality that signals 'official data' or 'system label'.

## Avoid

- Don't introduce additional chromatic colors - the palette is Press Ink, parchment neutrals, and one Alarm Red
- Don't use #000000 for body text or backgrounds - always use the warmer #110000
- Don't apply Alert Red (#d50000) to buttons, links, or navigation - it is for data blocks only
- Don't use sharp corners (0-4px radius) on buttons or cards - the system is defined by its pill and rounded softness
- Don't set display headlines at standard line-height (1.2+) - tight stacking (0.84-0.96) is the signature
- Don't use heavy drop shadows on dark sections - the near-black surfaces should feel flat and printed, not elevated
- Don't use photography for decorative atmosphere - imagery should be content-bearing (data, video, diagrams) or absent

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
