# Dropmark

Source: [Refero Style](https://styles.refero.design/style/5618f26a-4df6-42cb-8081-15e4318b54ff)
Reference site: [https://dropmark.com](https://dropmark.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:59:38.370Z
Refero modified: 2026-06-05T10:09:18.244Z
Theme: light
Category: Productivity

## Style Summary

Explore Dropmark's light Productivity design system: Cyan Signal #00affa, Cream Paper #f7f7f1 colors, DropmarkRealHead, DropmarkRealText typography, and...

North star: Warm paper atelier with cubist murals

## What To Borrow

- Cyan Signal `#00affa` for Blue accent for outlined action borders, linked labels, and lightweight interactive emphasis. Do not promote it to the primary CTA color
- Cream Paper `#f7f7f1` for Page canvas, section backgrounds, soft card surfaces - the warm off-white ground everything sits on
- Pure White `#ffffff` for Inset cards, modal surfaces, inverse button text, nav background
- Stone Gray `#dcdcd4` for Subtle accent surfaces, inset focus rings, warm shadow tints
- Graphite `#404040` for Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color
- Mid Ink `#333333` for Button text and border on dark surfaces, icon stroke
- Charcoal `#111111` for Headline text alternative, deep emphasis borders
- Pewter `#7f7f7f` for Secondary body text, muted helper text, inactive state text
- Ink Black `#000000` for SVG illustration linework, deepest icon fills
- Midnight Violet `#1e2554` for Illustration primary - the dominant dark shape color in cubist murals
- Deep Iris `#2c2a6c` for Illustration mid-tone - secondary dark purple in mural compositions
- Coral Burst `#ff5d43` for Illustration warm accent - orange-red shape fills in murals
- Aqua Glow `#38dede` for Illustration cool accent and icon highlight - teal punctuation in murals
- Vivid Amethyst `#9164fa` for Illustration bright accent - saturated purple shape fills
- Blush `#f8b3b8` for Illustration soft accent - pink shape fills for warmth in murals

- DropmarkRealHead `--font-dropmarkrealhead` for Display and section headings only - used at 60px for hero, 40px for section titles, 24px for sub-section headings. Medium weight is deliberate; avoids the heavy 700 convention to keep headlines calm and editorial rather than assertive.
- DropmarkRealText `--font-dropmarkrealtext` for Body, buttons, nav, list, footer, supporting UI. 400 for body and links, 600 for emphasized sub-labels and button text, 700 reserved for occasional inline emphasis. Functions as the working sans - every non-heading element uses it.

## Avoid

- Do not introduce additional chromatic colors into the UI - the system is intentionally monochrome with one cyan accent
- Do not use drop shadows for elevation; depth comes from surface color and illustration, not shadow
- Do not use border-radius larger than 3px on cards or buttons - the flat editorial geometry is the signature
- Do not bold body text above 600; 700 should appear only for rare inline emphasis
- Do not use #00affa as a text or background tint for non-action elements like tags, badges, or icons
- Do not place the illustration palette colors on text, borders, or background fills - they belong inside mural compositions
- Do not use the cream #f7f7f1 for buttons or CTAs; the canvas color must not compete with actions

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
