# Splice

Source: [Refero Style](https://styles.refero.design/style/1f69df96-675d-4ee0-aa85-e085d9d39981) 
Reference site: [https://splice.com](https://splice.com) 
Captured: 2026-07-29 
Refero published: 2026-02-24T14:22:25.000Z 
Refero modified: 2026-06-05T08:39:05.264Z 
Theme: dark 
Category: Media

## Style Summary

Explore Splice's dark Media design system: Signal Blue #528fff, Button Blue #1253ff colors, InterVariable (custom), SoehneBreit (custom) typography, and...

North star: midnight recording studio - a dark, weightless space where the only thing that ever gets loud is the music.

## What To Borrow

- Signal Blue `#528fff` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Button Blue `#1253ff` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Voltage Yellow `#f1f607` for Rare text accent - highlight punctuation, featured labels, emphasis. Used sparingly, only when a word needs to flash against the dark canvas. Never on backgrounds
- Carbon `#121214` for Primary page canvas, card surfaces, input fields, footer. The dominant working surface at 425 occurrences across every context
- Obsidian `#000000` for Deepest dark - image containers, nav surface, full-bleed backgrounds. Creates the bottom of the surface stack
- Platinum `#ffffff` for Primary text, inverted button text, icon fills. The only true white in the system; appears 1506 times across every text context
- Graphite `#232426` for Dominant canvas background, secondary button surface. Sits one step lighter than Carbon, used when a surface needs to feel like a different plane without using shadow
- Fog `#a6a8ad` for Muted text, nav items, secondary labels, inactive links. The first step down from white in the type hierarchy
- Ash `#c8c9cc` for Button borders, icon strokes, hairline dividers, ghost control outlines. The border that doesn't feel like a border
- Slate `#63656d` for Borders, dividers, inactive controls. Darker than Ash for when a divider needs to recede further
- Iron `#45464d` for Elevated surfaces, button borders, nav separators. The highest dark in the stack - used for the 1px inset stroke that replaces shadows

- InterVariable (custom) `--font-intervariable-custom` for Workhorse for all UI text - body, nav, buttons, inputs, cards, footer. The variable axis allows weight shifts (400 500 600 700) within a single family. Universal -0.015em tracking creates a compact, efficient reading rhythm across every size.
- SoehneBreit (custom) `--font-soehnebreit-custom` for Editorial display headlines. The wider, geometric cut of SoehneBreit at weight 400 creates a distinctive voice - headlines don't shout, they announce with quiet authority. The 0.071em tracking (applied at 14px) appears on uppercase eyebrow labels, creating the system's only wide-tracked text. Weight 400 only - bold is never used.
- Soehne (custom) `--font-soehne-custom` for Subheadings - bridges the gap between SoehneBreit display and Inter body. Used at 20px for secondary headings that need editorial weight without display scale.

## Avoid

- Never use #f1f607 Voltage Yellow on backgrounds - it is text-only punctuation
- Don't add drop shadows to cards or panels - the system is intentionally flat
- Never set SoehneBreit to bold weight - it only exists at 400 in this system
- Don't introduce new accent colors - the palette is grayscale plus two signals (blue, yellow-green)
- Avoid pure white backgrounds - the canvas is always Carbon #121214 or Graphite #232426
- Don't center-align body text - left-align for editorial reading rhythm
- Never use more than one chromatic color per component - the system rations color

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
