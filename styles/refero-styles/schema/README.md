# Schema

Source: [Refero Style](https://styles.refero.design/style/2b07d62c-d706-4c9d-a3fb-9c163da09f03)
Reference site: [https://schema.figma.com](https://schema.figma.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:12:34.842Z
Refero modified: 2026-06-05T12:10:34.402Z
Theme: mixed
Category: Design

## Style Summary

Explore Schema's mixed Design design system: Obsidian #000000, Ink #0f0f0f colors, Source Sans Pro, Figma Sans Display typography, and DESIGN.md for AI agents.

North star: Ink-black keynote stage with confetti-bright murals

## What To Borrow

- Obsidian `#000000` for Hero canvas, heavy structural borders, icon strokes - sets the high-contrast keynote-stage mood for the opening fold
- Ink `#0f0f0f` for Body and heading text on light surfaces, dark section borders
- Paper `#ffffff` for Page background, speaker card surfaces, light-section text on dark hero
- Ash `#e2e2e2` for Hairline borders, subtle icon fills, structural dividers between UI regions
- Mint Wash `#c7f8fb` for Teal wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Emerald Band `#24cb71` for Full-bleed accent section background - a bright green horizontal band that closes the hero composition

- Source Sans Pro `--font-source-sans-pro` for Source Sans Pro - detected in extracted data but not described by AI
- Figma Sans Display `--font-figma-sans-display` for Headlines and display copy - used at 56-86px for hero ('Schema by Figma', 'Meet our speakers!') with tight leading (0.90-1.10) and -0.02em tracking that makes type feel carved from a block. Weight 400 carries the design; 700 is reserved for emphasis.
- Figma Sans Text `--font-figma-sans-text` for Body, nav, button labels, supporting text. The companion text face at modest sizes (13-18px) with weight 400 as default and 600 for buttons/labels. -0.02em at 13px prevents the small type from feeling loose; 0.03em at 18px gives labels air.
- Figma Mono `--font-figma-mono` for Code or metadata snippets - used sparingly at 16px with 0.03em tracking for an architectural, monospaced accent in a world of proportional text
- Figma VF-normal-700-75 `--font-figma-vf-normal-700-75` for Figma VF-normal-700-75 - detected in extracted data but not described by AI
- Figma VF-normal-400-100 `--font-figma-vf-normal-400-100` for Figma VF-normal-400-100 - detected in extracted data but not described by AI

## Avoid

- Don't add border-radius to any element - sharp corners define the system's poster-like character
- Don't use shadows, glows, or blur effects - flat is the only elevation language here
- Don't introduce a chromatic CTA color - the system is intentionally monochrome, actions are outlined or text-only
- Don't set body text below 16px; captions can go to 13px but never smaller
- Don't let display headlines exceed 0.90-1.00 line-height - tight leading is what makes them feel architectural
- Don't color-fill buttons with brand hues; outlined Paper-on-Obsidian is the only button pattern in the system
- Don't separate light sections with gray bands - use either full-bleed color or seamless Paper-to-Paper flow

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
