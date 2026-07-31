# CHELSEA

Source: [Refero Style](https://styles.refero.design/style/905beb8c-9788-4ff4-888b-13370cacd4b0)
Reference site: [https://www.chelsea.com](https://www.chelsea.com)
Captured: 2026-07-31
Refero published: 2026-04-30T01:55:48.319Z
Refero modified: 2026-06-05T10:33:41.321Z
Theme: dark
Category: Agency

## Style Summary

Explore CHELSEA's dark Agency design system: Void Black #000000, Spotlight Blue #4490ff colors, Neue Haas Unica Pro typography, and DESIGN.md for AI agents.

North star: Black-box cinema with a single blue spotlight - the roster plays, the chrome disappears.

## What To Borrow

- Void Black `#000000` for Page canvas, all section backgrounds, negative space - the floor everything sits on
- Spotlight Blue `#4490ff` for Primary action, interactive links, roster name listings, focal dot indicator, highlighted borders - the only chromatic voice in an otherwise monochrome system
- Carbon Slate `#1f2937` for Headings, heavy borders, structural borders on dark surfaces - near-black with a slight cool cast for separation from the pure black canvas
- Bone White `#f4efe9` for Warm off-white for text and subtle borders - softer than pure white, evoking film stock and gallery walls against the black canvas
- Pure White `#ffffff` for Maximum-contrast text and dividers when absolute clarity is needed over photography or dark media
- Ash Gray `#e5e7eb` for Light-mode surfaces, neutral borders on cards or panels, secondary dividers - provides a paper-like counterpoint when a section lifts off the black canvas

- Neue Haas Unica Pro `--font-neue-haas-unica-pro` for All UI and content type - nav labels at 14px, body at 16px, section headings at 32px, display at 48px

## Avoid

- Do not introduce drop shadows, elevation layers, or card containers - the system is flat by design
- Do not add a second accent color or any warm tone; the palette is black + white + one blue
- Do not round images or media frames - they must be sharp rectangles bleeding to the viewport edge
- Do not use #0000ee or browser-default link blue; links must be #4490ff
- Do not add a visible logo block, nav background, or header bar - the nav is text floating on black
- Do not set body type above 1.5 line-height; the credit-roll feel depends on tight leading
- Do not introduce semantic colors (green/yellow/red) for status - the system has no UI states to encode

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
