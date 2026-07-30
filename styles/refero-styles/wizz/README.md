# Wizz

Source: [Refero Style](https://styles.refero.design/style/408d0b89-be7d-4a09-bc29-8a8ce13d0a7b)
Reference site: [https://wizzapp.com](https://wizzapp.com)
Captured: 2026-07-30
Refero published: 2026-04-30T00:41:01.440Z
Refero modified: 2026-06-05T12:40:32.028Z
Theme: light
Category: Other

## Style Summary

Explore Wizz's light Other design system: Volt Pink #ff3d9e, Obsidian #000000 colors, sans-serif, PolySans Bulky typography, and DESIGN.md for AI agents.

North star: Neon pink highlighter on a black-and-white editorial - like a single fluorescent mark on a fashion magazine spread.

## What To Borrow

- Volt Pink `#ff3d9e` for Primary action buttons, section labels, active states, cookie accept - the sole chromatic brand color, carrying 100% of the accent weight in the interface
- Obsidian `#000000` for Page text, floating navigation bar, bold display headlines, cookie banner surface, icon fills
- Paper White `#ffffff` for Page canvas, section backgrounds, text on dark surfaces, card surfaces in light sections
- Ash `#dadada` for Hairline borders, card inset rings, subtle dividers, secondary text on light backgrounds
- Charcoal `#444444` for Input borders, secondary surface fills, muted UI elements
- Onyx `#292929` for Secondary button backgrounds, elevated surface tone
- Mist `#eeeeee` for Input field backgrounds, subtle fill surfaces

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- PolySans Bulky `--font-polysans-bulky` for Hero display headlines - the signature compressed ultra-bold weight; tight line-height (1.0) lets the letters stack like a logo mark rather than reading as paragraphs
- PolySans Median `--font-polysans-median` for Primary workhorse - nav links, section headings, the 86px display for page-openers, all-caps micro-labels with 0.05em tracking. The compressed line-heights (0.85-1.0) at large sizes are what give Wizz its editorial-magazine density
- PolySans Neutral `--font-polysans-neutral` for Body copy, paragraph text, descriptive content - generous line-height (1.5) creates reading rhythm distinct from the tight display set
- PolySans Slim `--font-polysans-slim` for Light-weight utility text, subtle links, fine-print detail - provides typographic contrast against heavier Median weights in the same layout
- Inter `--font-inter` for Inter - detected in extracted data but not described by AI

## Avoid

- Never introduce a second accent color. The entire brand identity depends on pink being the only chromatic signal in a black-and-white field.
- Never use decorative gradients on UI elements. The hero gradient is the only allowed multi-color surface - everything else is flat solid fills.
- Never use drop shadows heavier than the two defined values. The system is intentionally flat; heavy elevation breaks the editorial feel.
- Don't use system sans-serif for headings. PolySans Median and Bulky are the identity - fall back to Inter or Manrope only if the custom fonts are unavailable.
- Never place body copy below 14px. The compact density is created through tight spacing, not through microscopic type.
- Don't use sharp corners (<5px radius) on any interactive element. Every button, input, card, and nav must have at least 12px or fully pill-shaped radius.
- Never use the pink accent on body text longer than a few words. Pink is for labels, buttons, and emphasis - not for paragraphs or descriptions.

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
