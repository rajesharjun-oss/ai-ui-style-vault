# Glein

Source: [Refero Style](https://styles.refero.design/style/2e4ce685-9f49-47a3-9577-bc4f196bd8f7)
Reference site: [https://glein.wien](https://glein.wien)
Captured: 2026-07-31
Refero published: 2026-04-30T03:58:51.184Z
Refero modified: 2026-06-05T08:23:59.787Z
Theme: light
Category: E-commerce

## Style Summary

Explore Glein's light E-commerce design system: Midnight Ink #000000, Bone White #ffffff colors, F-Grotesk, Maison-Neue-Mono typography, and DESIGN.md for...

North star: Atelier lookbook on warm linen - full-bleed photography, hairline rules, one whisper-weight voice.

## What To Borrow

- Midnight Ink `#000000` for Primary text, nav hairline borders, footer dividers, section rules, button text. Dominant structural color - defines the graphic skeleton against the warm canvas
- Bone White `#ffffff` for Page canvas, card surfaces, overlay text on dark imagery, cookie dialog background. The breathing space
- Warm Sand `#ebe6dc` for Secondary surface and section bands - the warm beige that gives the atelier its linen-like tactility. Section dividers, footer wash, category card backgrounds
- Concrete Gray `#8c8c8c` for Muted secondary text, tertiary borders, subdued image overlays. The recede color - present but never competing
- Ash Gray `#b3b3b3` for Subtle dividers, inactive nav borders, low-emphasis rules. The quietest member of the scale

- F-Grotesk `--font-f-grotesk` for Primary grotesque - used for everything from body to display. The entire type system runs at weight 400 only; hierarchy is pure scale.
- Maison-Neue-Mono `--font-maison-neue-mono` for Monospace companion - navigation, category labels, button text, footer meta, promotional strip. The 'labelling' voice that contrasts the editorial grotesque.

## Avoid

- Don't introduce any chromatic color. The system is 0% colorful - adding even one accent breaks the entire monochrome contract.
- Don't use bold, semibold, or light weights. The font files are loaded at 400 only; attempting 500/600/700 will fall back or look wrong.
- Don't add shadows, glows, or blur effects. The surface model is flat - elevation is communicated by warm-band transitions, not z-axis depth.
- Don't round corners. Every radius in the system is 0px. Adding border-radius introduces a 'card' or 'button' feel that contradicts the editorial-paper aesthetic.
- Don't use sans-serif for functional labels. Monospace is reserved for nav, buttons, and meta - mixing it with F-Grotesk here dilutes the atelier voice.
- Don't crowd the 111px display with surrounding UI. Display type needs air - no buttons, links, or images in its immediate margin zone.
- Don't use colored hover states on links. Underline-on-hover in the same color is the only state change the system supports.

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
