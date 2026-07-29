# Ciridae

Source: [Refero Style](https://styles.refero.design/style/a1b78a21-a304-482b-8ce5-f612d95d44fe)  
Reference site: [https://www.ciridae.com](https://www.ciridae.com)  
Captured: 2026-07-29  
Refero published: 2026-04-13T16:42:41.000Z  
Refero modified: 2026-07-03T03:30:15.537Z  
Theme: dark  
Category: AI

## Style Summary

Explore Ciridae's dark AI design system: Ember Rust #cc6437, Void Black #0b0b0b colors, Pragmatica Cond, Pragmatica typography, and DESIGN.md for AI agents.

North star: void chamber with ember pulse a near-black cathedral where the only warm note is a thin line of ember rust, and every surface is defined by hairline borders rather than shadow.

## What To Borrow

- Ember Rust `#cc6437` as Accent strokes, icon linework, small text highlights the only chromatic color in an otherwise monochrome system, appearing as a hairline pulse rather than a fill
- Void Black `#0b0b0b` as Primary page canvas and section backgrounds; the foundation of the entire system
- Charcoal Surface `#272a2a` as Card and panel backgrounds on dark sections one step lighter than the canvas to create surface separation without shadow
- Bone `#edebe7` as Light section backgrounds and off-white surfaces where the system flips from dark to bright
- Bone Darker `#dfddd9` as Subtle variant of Bone for layered light surfaces and warm-tinted off-white elements
- Pure White `#ffffff` as All body and heading text, ghost button borders, nav elements the dominant foreground color at 19.7:1 contrast on Void Black
- Pragmatica Cond Primary display and UI typeface narrow condensed uppercase at 14px for body, 20px for section labels, 32px for hero wordmark. The extreme narrowness and all-caps setting at 14px body size is the system's most signature choice: body text reads as a whisper of architectural type, not conventional prose. Substitute with Oswald or Barlow Condensed if Pragmatica Cond is unavailable. `--font-pragmatica-cond` for the source typography voice
- Pragmatica Secondary body typeface used for longer-form prose passages (e.g. the 'AI Operating System' card description at 24px, paragraph text at 15px). Slightly wider than Pragmatica Cond for reading comfort in extended blocks, but still 400 weight no bold ever. Substitute with Inter or Shne. `--font-pragmatica` for the source typography voice
- source-defined base spacing with comfortable density
- Source radius system: nav 1440px, cards 10px, badges 1440px, buttons 1440px

## Avoid

- Do not introduce bold or semi-bold weights the entire system operates at weight 400 only
- Do not add drop shadows, glow effects, or any box-shadow values the system is intentionally flat
- Do not use color fills on buttons all interactive controls are ghost/outlined with 1px borders
- Do not use mixed-case text or sentence case in any UI label, heading, or body string
- Do not introduce additional accent colors Ember Rust is the only chromatic note permitted
- Do not use non-pill radii (e.g. 4px, 8px) on buttons, badges, or nav items the 1440px pill is the system's signature shape
- Do not use gradients the system is built on flat color fields and blurred photography, not color transitions

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
