# Buymeacoffee

Source: [Refero Style](https://styles.refero.design/style/1b2aaf14-43b0-4c23-bd25-1d49924fe85e)  
Reference site: [https://buymeacoffee.com](https://buymeacoffee.com)  
Captured: 2026-07-29  
Refero published: 2026-05-07T22:02:25.025Z  
Refero modified: 2026-06-03T17:11:22.132Z  
Theme: light  
Category: SaaS

## Style Summary

Explore Buymeacoffee's light SaaS design system: Cream Paper #faf8f0, Card White #ffffff colors, ui-sans-serif, Circular Bold typography, and DESIGN.md for...

North star: Cream-paper caf scrapbook with floating polaroid testimonials

## What To Borrow

- Cream Paper `#faf8f0` as Page canvas, section backgrounds the warm off-white ground that softens every interface layer and gives the whole product its caf-on-paper atmosphere
- Card White `#ffffff` as Card surfaces, modal backgrounds, raised panels pure white floats above the cream canvas to create depth through luminance contrast rather than color
- Hairline Gray `#e5e7eb` as Borders, dividers, icon outlines, badge outlines used at 1146+ occurrences as the universal hairline separator across cards, buttons, and inputs
- Ink Black `#000000` as Primary text, filled icon strokes, high-contrast UI elements the dominant text and icon color across the entire product
- Charcoal `#222222` as Body and heading text, filled SVG strokes slightly softer than pure black for sustained reading in longer copy blocks
- Fog Gray `#717171` as Muted helper text, secondary metadata, small caps labels the quietest text voice for timestamps, supporter counts, and contextual hints
- ui-sans-serif ui-sans-serif detected in extracted data but not described by AI `--font-ui-sans-serif` for the source typography voice
- Circular Bold Display and hero headlines Circular Bold at 96px with -0.042em letter-spacing carries the 'Fund your creative work' headline; the extreme size and tight tracking make the wordmark feel monumental. Also used for button labels and emphasized short-form copy. `--font-circular-bold` for the source typography voice
- 4px base spacing with comfortable density
- Source radius system: tags 9999px, cards 24px, modals 32px, buttons 9999px

## Avoid

- Don't use #ffdd00 or #d8573f for body text, links, borders, or decorative fills these are action-only colors
- Don't apply sharp corners (0-4px radius) to cards or buttons the system requires generous rounding (8px minimum, 24px+ preferred for cards)
- Don't use colored shadows or glows all elevation comes from the neutral black-alpha three-layer stack
- Don't introduce new accent colors beyond Marigold, Terracotta, and Blush Border the palette is intentionally two-color (plus warm cream)
- Don't set body text below 14px or above 18px the reading range is narrow by design
- Don't use bold or black weights for long-form body copy Circular Regular or Book at 14-16px is the standard for paragraphs
- Don't fill the cream canvas with pure white sections alternate cream bands with white cards, not cream white cream

## Bundle Contents

- [DESIGN.md](DESIGN.md): implementation notes.
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
