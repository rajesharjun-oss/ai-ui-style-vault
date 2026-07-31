# until

Source: [Refero Style](https://styles.refero.design/style/ded6d7c4-2801-45f4-8b8a-089f1b37842d)
Reference site: [https://www.untillabs.com](https://www.untillabs.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:26:24.154Z
Refero modified: 2026-06-05T11:36:55.033Z
Theme: light
Category: AI

## Style Summary

Explore until's light AI design system: Parchment #f7f3ec, Ink #121212 colors, neueHaasDisplay, neueHaasText typography, and DESIGN.md for AI agents.

North star: warm parchment monograph under a single olive tree.

## What To Borrow

- Parchment `#f7f3ec` for Page background, card surfaces, nav container - warm off-white that replaces pure white to soften the entire system
- Ink `#121212` for Primary text, all borders, card outlines, nav links - near-black with a whisper of warmth, drives every structural line on the page
- Black `#000000` for Link borders, footer accents, and icon fills - pure black reserved for high-emphasis micro elements
- Paper `#ffffff` for Button fills, elevated surface accents, footer background - pure white used sparingly for contrast punctuation against the cream canvas
- Mist `#bebebe` for Disabled or secondary body text and subtle dividers - sits below the ink line
- Olive Branch `#6c853b` for Heading color and accent borders - the sole chromatic note, an organic olive green that gives the brand its botanical, anti-corporate feel
- Bone `#121c0f` for Deep text on light backgrounds where extra weight is needed - almost-black with a green undertone matching the olive

- neueHaasDisplay `--font-neuehaasdisplay` for Display and headings - from subhead at 24px to hero at 69px, with tight line-heights (0.90-1.10) and aggressive negative tracking (up to -0.037em) creating a compressed Swiss-editorial feel
- neueHaasText `--font-neuehaastext` for Body copy, nav links, button labels, card text - 14px and 16px with moderate negative tracking (-0.025em at 14px, -0.009em at 16px), reads as a clean grotesque but not clinical
- Geist Mono `--font-geist-mono` for Captions, annotations, code-like labels, scroll prompts - 12-14px with +0.05em tracking on the 12px size, adds a technical/research-lab accent

## Avoid

- Do not use pure black (#000000) for body text - use #121212, which has a slight warmth matching the cream canvas.
- Do not introduce additional chromatic colors; the olive is the only accent and overusing it dilutes the botanical restraint.
- Do not use sharp corners (0-6px radius) on cards, buttons, or images - the rounded language defines the softness.
- Do not place text on tinted overlays over photography; headlines sit directly on images or on the cream canvas.
- Do not set body text below 14px or above 16px; the type scale is deliberately narrow and editorial.
- Do not use filled colored buttons - every CTA is a pill with a 1px #121212 border, either white or ghost.
- Do not use box-shadows heavier than the defined inset/outer combo; the system relies on cream-on-cream layering, not elevation.

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
