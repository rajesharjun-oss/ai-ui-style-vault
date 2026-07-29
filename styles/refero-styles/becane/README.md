# Becane

Source: [Refero Style](https://styles.refero.design/style/d5017f8f-fa0f-4241-9319-527b0751f66f) 
Reference site: [https://www.becaneparis.com](https://www.becaneparis.com) 
Captured: 2026-07-29 
Refero published: 2026-07-03T15:31:14.865Z 
Refero modified: 2026-07-03T15:37:39.737Z 
Theme: light 
Category: E-commerce

## Style Summary

Explore Becane's light E-commerce design system: Bone White #f6f6f6, Divider Grey #e6e6e6 colors, Eurostile Becane typography, and DESIGN.md for AI agents.

North star: Gallery wall on bone-white plaster

## What To Borrow

- Bone White `#f6f6f6` for Page canvas, large background blocks
- Divider Grey `#e6e6e6` for Hairline borders between nav rows, section dividers
- Off-Black `#0a0a0a` for Headlines, body text, nav labels, button strokes
- Pure White `#ffffff` for Card surfaces, nav bar backgrounds, elevated panels
- Muted Grey `#b2b2b2` for Tertiary helper text, inactive labels
- Signal Red `#ff0000` for Accent panel fills - rotating display block, category highlight surface

- Eurostile Becane `--font-eurostile-becane` for Custom Eurostile variant is the sole typeface across all scales. Used uppercase at 8px with 0.04em tracking for nav, buttons, labels, and micro-copy - the high tracking and small size force labels to read as gallery placards rather than UI. Bold 30px anchors the hero 'COLLECTION' wordmark. Substitutes: Eurostile, 'Helvetica Neue', Arial - the geometric warmth of Eurostile is the closest system match; fallback to Helvetica Neue retains the uppercase utility feel.

## Avoid

- Never add background fills, gradients, or hover-color shifts to buttons - buttons remain ghost
- Never introduce a chromatic CTA button; #ff0000 is a surface accent, not an action
- Never round corners on cards, images, or buttons - sharp 0px edges define the aesthetic
- Never use body copy below 12px or above 30px; the scale is intentionally narrow
- Never add elevation (box-shadow, drop-shadow) - the system is flat and depends on hairline borders for structure
- Never use color to indicate state on links; rely on position, weight, or the Muted Grey #b2b2b2 for de-emphasis
- Never constrain the product row to a centered max-width container - let images breathe edge-to-edge

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
