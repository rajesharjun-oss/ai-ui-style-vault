# Promly

Source: [Refero Style](https://styles.refero.design/style/9117a4f5-6171-44ad-aa85-a387a5d80620)
Reference site: [https://promlyapp.com](https://promlyapp.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:17:13.134Z
Refero modified: 2026-06-05T09:27:18.788Z
Theme: dark
Category: Other

## Style Summary

Explore Promly's dark Other design system: Void Indigo #040723, Abyss Plum #140f33 colors, Avenir, Poppins typography, and DESIGN.md for AI agents.

North star: Midnight pulse through violet glass - a youth sanctuary lit by neon accents on near-black surfaces, where rounded photo collages float like screensavers behind sharp confident type.

## What To Borrow

- Void Indigo `#040723` for Page background, primary surface - near-black with a violet undertone that makes the whole canvas feel tinted rather than neutral
- Abyss Plum `#140f33` for Elevated card surface, shadow tone - a step lighter than Void Indigo, used to lift cards off the canvas with violet ambient
- Onyx `#000000` for Deep contrast surface for cards, input fills, and the darkest band behind photo content
- Glacier `#e4ebf3` for Off-white section backgrounds, light card surfaces - cool-tinted to harmonize with the violet system
- Paper `#ffffff` for Primary text on dark surfaces, button labels, image overlays - the dominant non-background color in the system
- Smoke `#999999` for Secondary/muted body text, disabled labels
- Ash `#808080` for Tertiary text and subtle borders on light sections
- Graphite `#333333` for Image borders, input strokes, secondary link text on light surfaces
- Charcoal `#222222` for Button borders on light surfaces, heavy text emphasis
- Cinder `#cccccc` for Input field borders, form dividers
- Pulse Blue `#3898ec` for Primary filled action background (CTA buttons, active nav) - the only chromatic fill in the system, acts as the single notification LED against the dark canvas
- Iris `#755eff` for Outlined action border, secondary accent - the violet identity color applied to ghost buttons and decorative strokes
- Lavender Lightning `#aa57ff` for Outlined action border, gradient start - lighter violet for tertiary buttons and gradient origins
- Neon Sprout `#0be014` for Link borders, icon borders, active state highlights - vivid green used sparingly as functional punctuation on links and tags
- Dusk Fade `#47246a` for Gradient mid-stop - deep violet that bridges bright lavender to black in hero gradient washes

- Avenir `--font-avenir` for Primary typeface across all contexts - headings, body, navigation, buttons, cards. Light 300 for large display headings creates a soft documentary feel; bold 700 for buttons and tag labels; regular 400 for body and supporting text.
- Poppins `--font-poppins` for Rare single-use bold label - appears on one decorative badge/button context, providing a geometric contrast to Avenir's humanist curves

## Avoid

- Do not use bold (700) or extra-bold weights for display headings - weight 300 is the system's identity choice; bold headlines break the whisper-tone.
- Do not introduce new colors for action buttons - the system has exactly one filled chromatic action (Pulse Blue) and outlined actions must use Iris, Lavender Lightning, or Neon Sprout.
- Do not apply flat black (#000000) as the page background - Void Indigo (#040723) is the system canvas; pure black is reserved for deepest card surfaces only.
- Do not use sharp corners (0px radius) on any image or card - every visual element must carry at least 8px radius, most 12-20px.
- Do not place green on filled buttons or backgrounds - Neon Sprout (#0be014) is link-border and icon-border only.
- Do not stack shadows or use gray-toned drop shadows - the single violet glow shadow is the only allowed elevation effect.
- Do not alternate text alignment arbitrarily - heroes are consistently left-aligned text with right-side photo collage; do not center-align long-form content.

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
