# Mage

Source: [Refero Style](https://styles.refero.design/style/ba07accb-b2cc-4ad9-a25f-c50b0f90f34e)
Reference site: [https://www.mage.ai](https://www.mage.ai)
Captured: 2026-07-31
Refero published: 2026-04-30T02:40:24.301Z
Refero modified: 2026-06-05T10:20:18.845Z
Theme: light
Category: AI

## Style Summary

Explore Mage's light AI design system: Electric Cobalt #244cff, Lavender Mist #c3aeff colors, sans-serif, Inter typography, and DESIGN.md for AI agents.

North star: data alchemy on parchment. Warm off-white canvas, whisper-weight Inter headlines, one cobalt switch for action, dark-mode product islands floating inside a bright editorial page.

## What To Borrow

- Electric Cobalt `#244cff` for Primary action fill - CTA buttons, active nav state, the single switched-on color in an otherwise muted system
- Lavender Mist `#c3aeff` for Brand illustration accent - decorative fills in the hero artwork and supporting graphics, echoes the cobalt at lower saturation
- Parchment `#f7f7f1` for Page canvas - warm off-white background that gives the whole site its editorial, paper-like quality
- Snow `#ffffff` for Card surfaces, text on dark backgrounds, product thumbnail containers
- Ice Wash `#e8f8ff` for Tinted card surface - subtle blue-white variant for differentiated cards (logo bar, feature callouts)
- Sky Tint `#d6f2ff` for Decorative card wash - pale blue background for illustration overlays and feature card accents
- Lemon Wash `#ffffbd` for Decorative card wash - warm yellow tint for illustration card backgrounds and feature highlights
- Blush `#fcc2cd` for Decorative card wash - soft pink for illustration card backgrounds
- Buttercream `#fced9f` for Decorative card wash - warm cream-yellow for illustration card backgrounds
- Azure `#3388ff` for Illustration accent - mid-blue used in hero artwork and data visualization elements
- Slate Blue `#5487a1` for Illustration accent - muted blue for decorative borders and secondary graphic elements
- Amber `#9e770b` for Illustration accent - warm dark-yellow for decorative graphic elements
- Lilac Pop `#ba9ffc` for Illustration accent - vivid lavender for hero artwork highlights
- Deep Cobalt `#294dba` for Illustration accent - darker blue for hero artwork depth and contrast
- Pure Black `#000000` for Primary text, hairline borders, high-contrast edges
- Graphite `#2b2b2b` for Secondary text, body copy on light surfaces - softer than pure black for reading comfort
- Obsidian `#1d1f21` for High-contrast neutral action fill for primary buttons on light surfaces.
- Ash `#878787` for Muted text - captions, helper text, secondary metadata
- Fog `#b0b0b0` for Borders, dividers, disabled state outlines, muted link text

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- Inter `--font-inter` for Workhorse body and UI text - body copy at 400, buttons/labels at 500-600, bold callouts at 700. The font's open apertures and tall x-height make it readable at 12-16px on the warm canvas
- Inter Variable `--font-inter-variable` for Display and heading sizes - 60px display headlines, 38px section headers, 30px subheadings. Weight stays at 400 even at display size: the headlines whisper rather than shout, authority through scale not weight
- Geist `--font-geist` for Small bold labels - compact uppercase-style tags and category markers at 14px weight 600

## Avoid

- Do not use multiple vivid colors as action buttons - the system has one action color (cobalt) and one dark variant; everything else is text or surface
- Do not set headlines to weight 600 or 700 - the whisper-weight 400 at large size is the signature; bolding breaks the editorial tone
- Do not add drop shadows to cards on the Parchment canvas - the warm tonal contrast between #f7f7f1 and #ffffff is enough separation
- Do not use the illustration palette colors (#fcc2cd, #fced9f, #ba9ffc) as UI chrome - they are reserved for the hero artwork and decorative card washes
- Do not mix Light Slate Blue #5487a1 or Amber #9e770b into text or border roles - they are illustration-only accents
- Do not use sharp corners (0px radius) on cards or images - the 6px minimum radius is a system-wide baseline
- Do not put body text below 14px - the Inter 12px usage is limited to micro-labels and metadata, never running prose

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
