# TWOTWO

Source: [Refero Style](https://styles.refero.design/style/170a690b-7424-4c2e-9d08-975725cf9261)
Reference site: [https://twotwo-official.com](https://twotwo-official.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:46:49.963Z
Refero modified: 2026-06-05T08:11:33.333Z
Theme: light
Category: E-commerce

## Style Summary

Explore TWOTWO's light E-commerce design system: Voltage Lime #e3fc03, Obsidian #000000 colors, WhyteRegular, Whyte typography, and DESIGN.md for AI agents.

North star: voltage lime on monochrome concrete - a single neon punch inside a black-and-white editorial grid

## What To Borrow

- Voltage Lime `#e3fc03` for Primary CTA fill, active state, accent badges, and decorative highlights - the single chromatic moment in an otherwise monochrome system. Sits at 18.2:1 contrast against black, so it doubles as a high-visibility call-to-action and a hover indicator without needing a second hue
- Obsidian `#000000` for Primary text, hairline borders, icon strokes, image borders, and footer background. Carries 2,045 border usages - this system uses black lines to structure space more than boxes or cards
- Graphite `#323232` for Secondary text and softer borders - slightly lifted from pure black to create a visible hierarchy without introducing color
- Carbon `#1a1a1a` for Icon strokes, link underlines, and low-priority UI marks - the third step of the dark scale, reserved for fine detail that should recede from primary text
- Paper White `#ffffff` for Primary page and card surface - the canvas everything else is drawn onto
- Concrete `#e6e6e6` for Soft section background, alternate surface, and quiet card fill.

- WhyteRegular `--font-whyteregular` for WhyteRegular - detected in extracted data but not described by AI
- Whyte `--font-whyte` for Display and section headings - used at 72px hero scale and 32px section scale. Tight 1.1 leading and a regular (not bold) weight are anti-convention: most sports brands shout with 800-weight display type, but Whyte Regular at 72px carries authority through letterform precision and negative space alone. The headlines never need a second style. Substitute: Inter Tight or Neue Haas Grotesk Display Pro at 400.
- Whyte Book `--font-whyte-book` for Universal workhorse - body copy, subheadings, product captions, navigation, and buttons. One weight, one family, used at seven sizes. The 38px tier handles product card titles; 16px is the default body; 13px is the fine-print and footer size. Line-height tightens from 1.60 at body to 1.30 at 38px. Substitute: Inter or Sohne at 400.
- Whyte Inktrap `--font-whyte-inktrap` for Secondary detail typeface with inktrap terminals - used for fine UI labels, tag monograms, and small monospace-feeling metadata. The inktrap cuts prevent the letterforms from filling in at small sizes, giving tags and micro-copy a distinct technical voice. Substitute: JetBrains Mono or IBM Plex Mono at 400.

## Avoid

- Do not introduce a second chromatic hue - no blues, reds, or greens outside the product photography. The page is monochrome plus lime, full stop.
- Do not use box-shadows or drop-shadows to elevate cards; elevation comes from 1px Obsidian borders on white surfaces, never from blurred shadows.
- Do not use a bold or 600+ weight for headlines - Whyte Regular at 400 with tight tracking is the signature; boldness would break the editorial register.
- Do not round images or cards to anything other than 16px, and do not use 4px or 8px micro-radii - the system lives in two radius steps only.
- Do not place buttons on colored or photographic backgrounds without the Voltage Lime fill - a white or black button would lose the brand's only signal.
- Do not stack the lime accent on lime (lime button on lime highlight) - the accent must sit against Paper White or Obsidian to register.
- Do not use centered text alignment for body copy, product titles, or prices - reserve centering for hero headlines and section headers only.

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
