# Attio

Source: [Refero Style](https://styles.refero.design/style/08c8700c-f278-42bc-812e-f60dc6ce996e) 
Reference site: [https://attio.com](https://attio.com) 
Captured: 2026-07-29 
Refero published: 2026-02-15T11:19:49.000Z 
Refero modified: 2026-07-03T03:43:47.574Z 
Theme: light 
Category: SaaS

## Style Summary

Explore Attio's light SaaS design system: Page Canvas #ffffff, Ink Black #1c1d1f colors, Inter, InterDisplay typography, and DESIGN.md for AI agents.

North star: Architectural editorial on white marble

## What To Borrow

- Page Canvas `#ffffff` for Primary page background, card surfaces, button backgrounds
- Ink Black `#1c1d1f` for Primary heading and body text, logo mark
- Graphite `#232529` for Dark surface text, dark filled button background
- Obsidian `#101113` for Deepest text and dark surface fills
- Carbon `#2e3238` for Secondary dark text, nav states, button text on light fills
- Slate 500 `#505967` for Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color
- Slate 600 `#6f7988` for Muted body text, secondary descriptions
- Slate 700 `#8f99a8` for Tertiary headings, captions, low-emphasis text
- Fog 400 `#9fa1a7` for Placeholder text, disabled states, subtle icons
- Mist 300 `#b5bdc9` for Muted body text, secondary copy
- Cloud 200 `#cad0d9` for Hairline borders on cards, input borders, dividers
- Cloud 100 `#d3d8df` for Card borders, surface boundaries
- Mist 50 `#e4e7ec` for Primary border color, dividers, subtle backgrounds, button borders
- Haze `#eeeff1` for Subtle background fills, section bands, inset borders
- Paper `#f4f5f6` for Alternate surface background, subtle elevated panels
- Cobalt Core `#266df0` for Primary brand accent - link text, focus rings, active states, highlighted icons, gradient midtone
- Cobalt Bright `#407ff2` for Secondary accent, hover states, decorative strokes in illustrations
- Cobalt Soft `#538bf3` for Violet wash for highlight backgrounds, decorative bands, and soft emphasis behind content.
- Periwinkle `#bad0fa` for Decorative card borders, subtle blue-tinted surface outlines
- Ice Wash `#e4edff` for Soft blue-tinted background, highlight washes, button box-shadow tints
- Onyx Footer `#000000` for Footer background, dark section backgrounds, high-contrast text on light

- Inter `--font-inter` for UI body - used for all body text, buttons, nav, links, card content, footers, icons. Weight 500 is the default for nearly all UI text (buttons, nav, body), giving Attio a slightly heavier, more confident UI voice than typical 400-only systems. Activated 'ss03' alternates give the text a distinctive geometric character.
- InterDisplay `--font-interdisplay` for Marketing headlines and display copy - weight 600 exclusively for large hero and section headings, with tight tracking (-0.015em to -0.02em) and near-1.0 line-heights creating dramatic, compact display blocks. The 56px size with -0.015em tracking is the signature hero voice. Activates 'ss03' and 'calt' for the same alternate character as Inter body.
- TiemposText `--font-tiempostext` for Editorial pull-quote and testimonial headings - a humanist serif that breaks the sans-serif system to create warmth and editorial weight. Used sparingly for quoted customer voices. This serif/sans contrast is the single most distinctive typographic choice in the system.

## Avoid

- Don't use rounded buttons with radius above 12px - the 10px radius is part of the system identity
- Don't introduce secondary accent colors, gradients on buttons, or decorative color - one blue accent is the rule
- Don't use TiemposText for anything other than testimonial pull-quote headings - the serif/sans contrast is earned by rarity
- Don't use Inter weight 400 as a default - weight 500 carries the UI voice
- Don't apply shadows warmer than rgba(28, 40, 64, ...) - the blue-tinted shadow is deliberate, not neutral
- Don't use letter-spacing wider than 0 for body or heading text - the system is consistently tight-tracked
- Don't place the cobalt accent on filled backgrounds in body copy - it belongs to links, icons, and small interactive moments

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
