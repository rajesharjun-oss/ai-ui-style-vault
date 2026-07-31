# Podcorn

Source: [Refero Style](https://styles.refero.design/style/8d4b0738-c302-45c6-98c9-b3cd36e04613)
Reference site: [https://podcorn.com](https://podcorn.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:37:04.738Z
Refero modified: 2026-06-05T09:17:58.418Z
Theme: light
Category: Media

## Style Summary

Explore Podcorn's light Media design system: Blush Cream #fff4f2, Pure White #ffffff colors, Gilroy, Georgia typography, and DESIGN.md for AI agents.

North star: Indie magazine spread on warm blush paper. A cream canvas carrying deep-indigo editorial typography, hand-drawn illustrations framed in hairline rectangles, and a single coral button as the only warm mark on the page.

## What To Borrow

- Blush Cream `#fff4f2` for Page canvas - warm off-white that sets the editorial tone and makes the deep-indigo text read like printed ink on heavy paper
- Pure White `#ffffff` for Card surfaces, nav background, button fills on light backgrounds - stacked above the cream canvas to create depth without shadow
- Ink Violet `#090335` for Primary text, headings, filled CTA buttons, nav links, hairline borders - the single dominant color of the entire interface; near-black with a violet undertone gives headings personality without abandoning readability
- Coral Flame `#fc736c` for Red wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Peach Whisper `#ffb0a1` for Orange decorative accent for icons, marks, and small graphic details. Do not promote it to the primary CTA color
- Deep Navy `#132645` for Illustration detail fill (SVG artwork) - cooler sibling of Ink Violet used inside drawings to add tonal range to the editorial illustrations
- Graphite `#434352` for Secondary nav text and nav borders - a softer alternative to Ink Violet for tertiary labels and dividers
- Silver Mist `#8993a2` for Muted nav borders and inactive control outlines
- Hairline `#d8d8d8` for Hairline link underlines and subtle dividers
- Zinc Mute `#71717d` for Helper text and tertiary metadata

- Gilroy `--font-gilroy` for Primary interface typeface - body text, navigation, buttons, card labels, footer. Geometric sans with tight tracking gives UI elements a confident, contemporary voice.
- Georgia `--font-georgia` for Headline and hero typeface - a classical serif reserved for editorial moments. The serif/sans pairing is the site's most distinctive typographic decision: Georgia carries warmth and craft, Gilroy carries clarity and UI density. Mixing these creates an indie-magazine feel that distinguishes Podcorn from generic SaaS layouts.

## Avoid

- Never use drop shadows, blurs, or glow effects - depth comes from surface color shifts only
- Never use the Coral accent on text, borders, or icon fills - it is a button-only color
- Never apply Georgia to body text, nav, or buttons - reserve it for headings and hero copy only
- Never round illustration frames - the 0px rectangular border is essential to the editorial frame metaphor
- Never use pure black #000000 for primary text - Ink Violet #090335 is the text standard
- Never place photography or product screenshots inside the cream sections - illustrations only
- Never use emoji, gradient fills, or neon accents - the palette is deliberately limited to cream, white, ink-violet, and coral

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
