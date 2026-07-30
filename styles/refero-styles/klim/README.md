# Klim

Source: [Refero Style](https://styles.refero.design/style/0dad8530-9422-4d9e-8622-1f50ee4bc702)
Reference site: [https://klim.co.nz](https://klim.co.nz)
Captured: 2026-07-30
Refero published: 2026-04-30T03:34:36.029Z
Refero modified: 2026-06-05T12:45:54.537Z
Theme: mixed
Category: Design

## Style Summary

Explore Klim's mixed Design design system: Studio Charcoal #101c19, Gallery Black #000000 colors, SOEHNE, Sohne typography, and DESIGN.md for AI agents.

North star: typographic gallery in a black box - a curator's vitrina where each specimen hangs in its own dark band

## What To Borrow

- Studio Charcoal `#101c19` for Page canvas, primary background - a near-black with a green undertone that reads as neutral but feels warmer than pure black
- Gallery Black `#000000` for Feature bands, specimen backgrounds, header bar - pure black for maximum type contrast
- Charcoal Surface `#1c1c1c` for Elevated surface, input fields, secondary panel backgrounds - one step lighter than the canvas
- Slate Mist `#3c585f` for Muted accent band, tertiary surface - desaturated blue-gray used as an alternate section background
- Graphite `#555555` for Mid-tone borders, muted body text on light sections, card outlines
- Steel `#646464` for Secondary borders, subdued link text on dark backgrounds
- Fog `#7f7f7f` for Tertiary borders, inactive UI elements, secondary text
- Ash `#939393` for Medium-contrast borders, control outlines, and structural separators. Do not promote it to the primary CTA color
- Marble `#f9f9f9` for Light-mode page canvas, pale gray that photographs cleanly for specimen presentations
- Bone `#ffffff` for Primary text on dark backgrounds, type specimen letterforms, button labels, high-contrast surfaces
- Flare Orange `#d33c03` for Label tags, collection names, editorial annotations - a saturated vermilion that reads as the foundry's signature mark on light backgrounds
- Signal Red `#e90702` for Hot accent on dark surfaces, inline highlights, the reddest red in the palette for maximum voltage
- Electric Blue `#24a7f2` for Interactive highlights, active states, link emphasis - a bright cyan-blue that pops against black
- Mint Pulse `#93ffe6` for Decorative text accent, special-occasion highlights - a pale mint used sparingly for emphasis
- Canary `#ffff79` for Rare chromatic accent, used for the highest-attention text moment on dark backgrounds
- Blush `#ffe6d9` for Soft warm accent, subtle text tint - a cream-pink that warms dark sections without competing with type

- SOEHNE `--font-soehne` for SOEHNE - detected in extracted data but not described by AI
- Sohne `--font-shne` for Primary UI typeface - used for navigation, body text, buttons, form labels, and all functional interface text. Tight line-heights (0.98-1.20) at display sizes; generous (1.50) for body. Two weights only: regular for content, bold for emphasis. Tabular numerals via tnum for price alignment; ordinals via ordn.
- Sohne Ikon `--font-shne-ikon` for Iconographic variant of Sohne for interface glyphs, special characters, and numeric UI elements. Same voice as Sohne but with alternate character forms via calt and tabular figures via tnum.
- SOEHNE_IKON `--font-soehneikon` for SOEHNE_IKON - detected in extracted data but not described by AI

## Avoid

- Do not introduce drop shadows, gradients, or glow effects - the system is flat and shadowless
- Do not use border-radius greater than 2px - the design is intentionally near-sharp
- Do not use color on large background fills - chromatic colors are reserved for tiny label tags and text accents
- Do not set body or display type in colors other than Bone (#ffffff on dark) or Graphite (#555555 on light) - chromatic type is for special emphasis only
- Do not add visible section dividers or whitespace gaps larger than ~69px between bands - the background color shift IS the divider
- Do not use system fonts for UI text - Sohne is the voice of the interface
- Do not place more than one chromatic color in a single component - each color punch gets its own moment

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
