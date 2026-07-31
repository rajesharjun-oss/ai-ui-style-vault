# Ordinal

Source: [Refero Style](https://styles.refero.design/style/4657db98-0c6c-4848-91e9-c339f3bb7815)
Reference site: [https://www.meetassembly.com](https://www.meetassembly.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:43:27.975Z
Refero modified: 2026-06-05T09:36:11.450Z
Theme: dark
Category: SaaS

## Style Summary

Explore Ordinal's dark SaaS design system: Void Canvas #151316, Paper #ffffff colors, Inter, Inconsolata (custom-mapped eyebrow face) typography, and...

North star: dark observatory with one mint filament - a near-black room where a single neon green switch glows as the only thing that matters

## What To Borrow

- Void Canvas `#151316` for Page background, hero canvas, footer - near-black with a faint violet undertone that keeps the dark from feeling flat or sterile
- Paper `#ffffff` for Primary text and icon color on dark surfaces; borders on dark UI; inverted text on light feature cards
- Elevated Surface `#444245` for Card and panel surface above the void canvas - subtle lift achieved through one tonal step rather than shadow
- Mist `#8e8e8e` for Muted body text, hairline dividers, inactive icon strokes, and low-emphasis borders on dark backgrounds
- Smoke `#585657` for Mid-weight borders and subtle UI separators - slightly darker than Mist for structural rules
- Ash `#b9b9b9` for Light-mode body borders and secondary text on warm light sections
- Bone `#f4f2ee` for Hairline borders, dividers, input outlines, and card edges on light surfaces.
- Charcoal `#222222` for Primary text on light feature sections and nav borders in light mode
- Mint Filament `#8ef5b5` for The single chromatic accent - filled primary CTAs, eyebrow pill labels, active nav indicator, logo glow, and green-text logo tints. Against #151316 the contrast is 14:1, making it legible as both text and fill

- Inter `--font-inter` for Entire UI - body, nav, headings, buttons, cards. Only two weights used (regular 400, medium 500) which is the core typographic discipline: no bold display weight, no light italic, just calm and confident Inter. The 13px/17px pair forms the dense product text; 40-60px carries the marketing voice. Headlines use -0.03em tracking to pull letters tight against the dark canvas.
- Inconsolata (custom-mapped eyebrow face) `--font-inconsolata-custom-mapped-eyebrow-face` for Eyebrow labels, status pills, and small ALL CAPS markers like 'ASSEMBLY 15 NOW ORDINAL', 'SCHEDULING', 'WATCH A DEMO 4:15'. The monospace character at 13-17px is a deliberate break from Inter's proportions - signals 'metadata / system status / not body content'. 0.01em positive tracking on the eyebrow adds the ALL CAPS breath small caps need.

## Avoid

- Don't introduce a second brand color - the system is monochrome + one mint, nothing else
- Don't use shadows to separate cards from the void - step the surface to #444245 instead
- Don't set headings in bold or semibold; weight 500 is the ceiling
- Don't use decorative gradients on body content - the teal charcoal gradient only appears behind the hero product screenshot
- Don't add rounded corners larger than 18px to cards - the system reads precise, not soft
- Don't use the mint as a background fill for large sections; it loses the 'single switch' effect
- Don't stack the ghost button on ghost button; every secondary action must be ghost, and the tertiary is a text link

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
