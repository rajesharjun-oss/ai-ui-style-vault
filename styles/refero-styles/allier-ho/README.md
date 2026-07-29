# Allier Ho

Source: [Refero Style](https://styles.refero.design/style/a85c74b9-2166-4fa3-be49-a2cc48990c6a) 
Reference site: [https://allierho.com](https://allierho.com) 
Captured: 2026-07-29 
Refero published: 2026-05-10T22:34:21.358Z 
Refero modified: 2026-06-03T21:35:16.292Z 
Theme: light 
Category: Agency

## Style Summary

Explore Allier Ho's light Agency design system: Warm Paper #fcfcfc, Deep Ink #000000 colors, Crimson Pro, Azeret Mono typography, and DESIGN.md for AI agents.

North star: serif whisper on warm paper

## What To Borrow

- Warm Paper `#fcfcfc` for Page canvas, card surfaces, and nav background - the base layer everything sits on
- Deep Ink `#000000` for Primary text, body copy, nav links, and dominant border color - the structural voice
- Press Black `#1c1c1c` for Heading text and heavy borders - slightly softer than pure black for large display sizes
- Charcoal Trace `#262626` for Secondary borders, dividers, and muted text on dark surfaces
- Ash `#a8a8a8` for Helper text, disabled states, and hairline borders on light surfaces
- Dusty Mauve `#6c5f7d` for Accent panel backgrounds, heading color, and chromatic border - a near-gray purple that signals brand moments without shouting
- Pale Sage `#cee6cc` for Secondary heading tint and accent border - a near-gray green that appears as quiet punctuation alongside the mauve

- Crimson Pro `--font-crimson-pro` for Display headlines at 44-50px, weight 300 with negative tracking. The anti-conventionally light serif whispers authority instead of projecting it; most agencies use 600-700 here, this restraint is the signature move.
- Azeret Mono `--font-azeret-mono` for Body copy, labels, and metadata at 12-18px. Monospace for a portfolio is a deliberate editorial choice - it reads as technical, precise, and un-decorative, contrasting the flowing serif headlines.
- System Sans-Serif `--font-system-sans-serif` for Navigation links and micro-labels at 12px. Neutral utility voice that stays out of the way of the serif/mono dialogue.

## Avoid

- Don't use Crimson Pro at weight 400 or heavier - the light weight is non-negotiable
- Don't add drop shadows, inner shadows, or glow effects to cards, buttons, or images - the system is flat
- Don't introduce additional accent colors beyond dusty mauve and pale sage - the palette is deliberately two-note
- Don't round corners on cards, panels, or images - only buttons and tags use radius
- Don't use a sans-serif for body copy - Azeret Mono is the body voice; sans-serif is reserved for nav and labels only
- Don't fill buttons with solid color - the pill outline on transparent background is the only button style
- Don't use system serif or serif substitutes for body - Crimson Pro is display-only

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
