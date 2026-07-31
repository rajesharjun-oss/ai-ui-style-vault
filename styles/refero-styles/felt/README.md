# Felt

Source: [Refero Style](https://styles.refero.design/style/127a4efb-685c-42c3-83eb-72bb410a8429)
Reference site: [https://www.felt.com](https://www.felt.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:28:31.422Z
Refero modified: 2026-06-05T12:09:40.909Z
Theme: dark
Category: SaaS

## Style Summary

Explore Felt's dark SaaS design system: Moss Canvas #314218, Fern #3d521e colors, Arial, GT Alpina Standard typography, and DESIGN.md for AI agents.

North star: topographic atlas at dusk - moss-green pages, serif headlines, one amber needle

## What To Borrow

- Moss Canvas `#314218` for Page background, hero sections, dominant canvas - the deep mossy green that carries the entire site and grounds the editorial atmosphere
- Fern `#3d521e` for Mid-green surface for cards, elevated panels, and the topside of the surface stack
- Lichen `#64754b` for Muted green for secondary surfaces, borders on cards, and subtle dividers against the canvas
- Forest Floor `#212f0c` for Deeper green for nested surface layers and inset product UI backgrounds
- Deep Bog `#18210c` for Darkest green for the deepest surface layer, code blocks, and high-contrast panels
- Amber Compass `#dc8c46` for Primary action - filled CTA buttons, link borders, active link text. The single warm accent that cuts through the green monochrome like a compass needle
- Bone White `#ffffff` for Primary text, heading color, button text on amber fills, and the dominant border for ghost/outlined controls
- Parchment `#eeeeee` for Light surface for embedded product UI, inset map views, and light-mode panel surfaces against the dark canvas
- Charcoal `#333333` for Text and borders inside the light parchment product UI panels - the dark-on-light text color for embedded app surfaces
- Limestone `#d8dcd2` for Soft warm-tinted gray for badge backgrounds, subtle borders, and muted helper text inside light panels
- Ink `#000000` for SVG fills, max-contrast elements, and the map marker pin color

- Arial `--font-arial` for Arial - detected in extracted data but not described by AI
- GT Alpina Standard `--font-gt-alpina-standard` for Display and heading serif - the editorial headline face. Used at large sizes for hero headlines and section titles. The tight negative tracking (-0.033em to -0.040em) and line-height under 1.0 give the serif a compressed, almost carved-into-stone quality that evokes old cartographic title plates. This is the signature type choice: a humanist serif that feels hand-drawn rather than mechanical.
- Atlas Grotesk `--font-atlas-grotesk` for Primary UI and body sans-serif - handles navigation, body text, button labels, badges, and links. The slight positive tracking (0.033em) on body sizes adds legibility on the dark green canvas. The grotesque geometry provides a clean utility counterpoint to the expressive serif headlines.
- Times New Roman `--font-times-new-roman` for Fallback system serif at extreme display sizes. The 101px / 0.88 line-height ratio confirms the compressed display treatment for the largest headlines.

## Avoid

- Don't use Amber Compass (#dc8c46) for body text, backgrounds, or large surface areas - it loses its compass-needle effect when overused
- Don't set serif headlines at line-height above 1.0 - the compressed treatment is essential to the editorial feel
- Don't apply multiple shadow layers - Felt uses elevation through color stepping, not shadow stacks
- Don't use pure black (#000000) as a page background - the mossy green tones are the canvas, not black
- Don't replace GT Alpina Standard with a geometric or grotesque display face - the serif is the brand identity
- Don't use border-radius above 6px on cards, images, or product panels - only buttons get the 20px pill radius
- Don't introduce new accent hues - the entire palette is green monochrome plus one warm amber; any other color breaks the system

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
