# Shupatto

Source: [Refero Style](https://styles.refero.design/style/17824ea8-ac7d-42ca-97e2-9bf92ebea7e1)
Reference site: [https://www.shupatto.com/en](https://www.shupatto.com/en)
Captured: 2026-07-31
Refero published: 2026-04-30T00:14:54.023Z
Refero modified: 2026-06-05T09:07:11.320Z
Theme: light
Category: E-commerce

## Style Summary

Explore Shupatto's light E-commerce design system: Graphite #2d2d2d, Ink #000000 colors, GillSansNova-Book, GillSansNova-SemiBold typography, and DESIGN.md...

North star: Museum vitrine on white marble

## What To Borrow

- Graphite `#2d2d2d` for Primary text, hairline borders, structural lines - the dominant neutral carrying all interface weight
- Ink `#000000` for Strongest text and most emphatic borders, logo dots, footer marks
- Paper `#ffffff` for Page canvas, card surfaces, nav backgrounds - the unbroken white field everything floats on
- Fog `#878887` for Muted helper text, secondary borders, dimmed metadata
- Periwinkle `#738ae5` for Sole chromatic accent - selected nav state, badge fills, a rare pressure point in an otherwise colorless system

- GillSansNova-Book `--font-gillsansnova-book` for Primary typeface for body, headings, nav, links, and icon-adjacent text - carries the entire English typographic system at a medium weight with wide tracking
- GillSansNova-SemiBold `--font-gillsansnova-semibold` for Emphasis and key headings - the bolder weight creates hierarchy without size inflation; the 8px variant carries micro-labels and badge text
- (Yu Gothic) `--font-yu-gothic` for Japanese text rendering - sits at the same metric scale as the English system, ensuring bilingual visual parity
- CezannePro-DB `--font-cezannepro-db` for Micro-decorative and brand-specific marks - a secondary display face for labels that need a different visual texture from the main Gill system
- GillSansNova-Medium `--font-gillsansnova-medium` for GillSansNova-Medium - detected in extracted data but not described by AI

## Avoid

- Do not introduce shadows, gradients, or any form of elevation - the design system is flat by philosophy
- Do not add bright or saturated colors beyond #738ae5; even secondary accents should stay neutral
- Do not use border-radius above 3px; avoid pill shapes and large rounded corners
- Do not set type in mixed case or normal letter-spacing; everything reads as editorial display via tracking
- Do not fill cards or sections with tinted backgrounds; rely on hairline borders to create structure on the white canvas
- Do not use large display type below 28px or above 32px - the scale is deliberately compressed and quiet
- Do not add icons with weight above 1px stroke; icons are absent or drawn as the thinnest possible lines

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
