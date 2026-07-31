# BUTT STUDIO

Source: [Refero Style](https://styles.refero.design/style/c6e55968-fa2d-47c9-b833-2c4ad1e74906)
Reference site: [https://www.butt-studio.com](https://www.butt-studio.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:29:10.166Z
Refero modified: 2026-06-05T09:49:05.313Z
Theme: light
Category: Agency

## Style Summary

Explore BUTT STUDIO's light Agency design system: Ink Black #000000, Paper #ffffff colors, helvetica, Caslon typography, and DESIGN.md for AI agents.

North star: gallery wall with one massive serif wordmark

## What To Borrow

- Ink Black `#000000` for Primary text, borders, button outlines, structural strokes - the only color that ever carries information
- Paper `#ffffff` for Card surfaces, thumbnail covers, inverted text on dark blocks
- Carbon `#131313` for Dark project tile backgrounds, near-black surface for video panels
- Bone Gray `#e0e0e0` for Page canvas, neutral button fills - the warm gray the whole composition sits on
- Studio Indigo `#31338e` for Sole chromatic accent - STUDIO pill badge, and any deep brand punctuation. The only saturated color in the system

- helvetica `--font-helvetica` for Every utility, body, list, button, and link on the site. Stays at one weight - no bold, no medium. The decision to use weight 400 Helvetica at 20px for body (not 16px) is deliberate: text is meant to feel like printed matter, not a UI. Tighter letter-spacing on larger sizes (-0.03em) prevents the 40px from feeling airy.
- Caslon `--font-caslon` for The hero wordmark and any serif accent. A single weight of a custom display serif - chosen because its high contrast strokes and ball terminals read as editorial print, not web type. This font IS the brand; everything else is scaffolding.
- Sometimes Times `--font-sometimes-times` for Sometimes Times - detected in extracted data but not described by AI

## Avoid

- Do not introduce any color other than the four neutrals and Studio Indigo - no gradients, no tints, no hover-state color shifts
- Do not use shadows, glows, or elevation - the design is flat like print, with no synthetic depth
- Do not add border-radius to cards, tiles, or thumbnails - they must stay sharp like cut paper
- Do not set body text below 20px or add bold/medium weights to Helvetica - weight 400 is the only weight that exists
- Do not use Caslon for anything below the hero - reserve it for the wordmark and project titles to preserve its weight
- Do not add underlines, color, or icons to links in the client/feature lists - they read as plain text on purpose
- Do not center body text or list items - the ledger columns are left-aligned like a contact page

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
