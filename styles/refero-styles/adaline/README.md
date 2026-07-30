# Adaline

Source: [Refero Style](https://styles.refero.design/style/312423bf-72ea-42fb-b8f5-ab0104e778f3)
Reference site: [https://www.adaline.ai](https://www.adaline.ai)
Captured: 2026-07-30
Refero published: 2026-04-30T00:36:11.612Z
Refero modified: 2026-07-03T10:09:39.356Z
Theme: light
Category: AI

## Style Summary

Explore Adaline's light AI design system: Forest Ink #0a1d08, Olive Press #2b390a colors, akkurat, Newsreader typography, and DESIGN.md for AI agents.

North star: botanist's specimen journal beside a developer's terminal - warm linen pages, sage ink annotations, and tracked mono tags.

## What To Borrow

- Forest Ink `#0a1d08` for Gray text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color
- Olive Press `#2b390a` for Headings at large sizes, high-contrast body text, hover states on filled buttons
- Sage Leaf `#4a6d47` for Decorative icon accent, badge fills, subtle wash backgrounds on spec cards
- Deep Teal `#2b6b5e` for Secondary category fills, alt-card backgrounds, tonal pair with the dominant greens
- Crimson Specimen `#991e4b` for Red text accent for links, tags, and emphasized short phrases. Use as a supporting accent, not as a status color
- Amber Pin `#80581c` for Yellow wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color
- Linen `#f8f9f5` for Page canvas, default surface - warm off-white with a faint green cast
- Bone `#eff2e8` for Card surface, elevated panels, subtle inset containers
- Mist `#e1e6df` for Hairline borders, card outlines, separator strokes
- Slate Hollow `#2a332a` for Inverse surface for footer and dark bands, modal scrims
- Sage Gray `#6b7860` for Secondary body text, supporting copy, icon strokes
- Sage Mist `#a5ac9f` for Muted helper text, disabled labels, low-emphasis metadata
- Eucalyptus `#c9d5c5` for Soft surface tints, category tag backgrounds, hover wash
- Lichen `#c5ccb6` for Outlined-button border color, link underlines, specimen-card borders
- Blush `#e3c9d0` for Decorative alt-card background, tonal contrast specimen
- Sand `#ad9d80` for Decorative card surface, tertiary alt fill
- Sage Foam `#729d92` for Decorative alt-card surface, soft cool counterpoint to the sage family
- Rose Clay `#c27c93` for Decorative alt-card background, warm-tonal specimen
- Surface Glow `#fdfefb` for Surface-highest token, used for elevated card layers above Linen

- akkurat `--font-akkurat` for Workhorse sans for body, nav, headings, buttons, cards across the entire system
- Newsreader `--font-newsreader` for Single display-size serif headline - unexpected literary anchor against the utility sans
- Fragment Mono `--font-fragment-mono` for Field-note tagging: badges, category labels, button text, code-lite metadata, tracked micro-copy
- ui-monospace `--font-ui-monospace` for System mono fallback for the tightest micro-tags (8px, 500 weight, 0.04em tracking)
- GT America Mono `--font-gt-america-mono` for GT America Mono - detected in extracted data but not described by AI
- fragmentMono `--font-fragmentmono` for fragmentMono - detected in extracted data but not described by AI

## Avoid

- Do not pair the serif display font with sans-serif headings - Akkurat at 30-53px owns all non-display headlines.
- Do not introduce bright chromatic CTAs (blue, red, vivid green) - the action palette stays in Forest Ink and Olive Press.
- Do not add drop shadows to cards or modals; rely on borders and surface tints for separation.
- Do not use icons or illustrations to fill empty space - the layout is intentionally sparse and specimen-like.
- Do not mix the Fragment Mono labels into running body copy - keep mono reserved for badges, IDs, and metadata.
- Do not place content into multi-column dashboard grids; sections are wide, centered, and stacked.
- Do not break the 96px vertical rhythm between major sections - Adaline reads as printed pages, not cards.

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
