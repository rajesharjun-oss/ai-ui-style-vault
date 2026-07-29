# Outsource Consultants

Source: [Refero Style](https://styles.refero.design/style/16be276a-d8ce-484e-8f7a-cbbb09f717f7) 
Reference site: [https://oci.madebybuzzworthy.com](https://oci.madebybuzzworthy.com) 
Captured: 2026-07-29 
Refero published: 2026-03-24T12:09:56.000Z 
Refero modified: 2026-06-05T03:59:47.501Z 
Theme: light 
Category: Agency

## Style Summary

Explore Outsource Consultants's light Agency design system: Indigo Strike #1925aa, Bone #e8e6e0 colors, GT America Mono, PP Neue Montreal typography, and...

North star: Architectural broadsheet on bone paper. A monograph aesthetic where one violent indigo section interrupts an otherwise warm, typographically maximalist grid.

## What To Borrow

- Indigo Strike `#1925aa` for Brand mark, full-bleed section backgrounds, large headlines, icon strokes, nav borders - the singular chromatic voice of the system, used as a sudden tonal shift rather than a decorative accent
- Bone `#e8e6e0` for Page canvas and card surface - a warm off-white that reads as paper rather than screen, providing the neutral ground against which indigo gains force
- Ink `#000000` for Body copy, small labels, standard text - used for dense information layers that must stay recessive against the bone canvas
- Paper `#ffffff` for Light supporting surface for subtle backgrounds and section separation. Do not promote it to the primary CTA color
- Deep Indigo `#0d1355` for Logo and brand-mark fill - a near-black violet that grounds the wordmark against the brighter Indigo Strike used in UI contexts

- GT America Mono `--font-gt-america-mono` for Micro-metadata and technical labels - nav identifiers, menu button text, accordion descriptions, footer tags. The mono face signals 'technical / regulatory / specification' and is kept under 14px so it reads as annotation rather than content. Negative tracking at 10px tightens the monospace grid; the slight positive tracking at 14px opens it for legibility. This pairing of editorial sans + technical mono is the system's core typographic gesture.
- PP Neue Montreal `--font-pp-neue-montreal` for Display and editorial type - carries the massive hero headline at 160px (line-height 0.94, so letters nearly touch), subheadings at 36-46px, and body at 18px. The grotesque geometry and tight line-height at scale create a poster-like voice; the same family steps down to 12-16px for nav links and service titles. Using one sans family from 12px to 160px (an extreme ratio) is a signature choice - it means hierarchy is built by size alone, not by weight or family switching.
- ui-sans-serif `--font-ui-sans-serif` for ui-sans-serif - detected in extracted data but not described by AI

## Avoid

- Do not introduce shadows, glows, blurs, or any form of drop elevation - the system is deliberately flat.
- Do not use indigo as a button background fill - the Menu button is white with an indigo icon square; indigo is a surface, not an action color.
- Do not add a second accent color - the system is bone + ink + a single indigo; any new chromatic role will dilute the editorial tension.
- Do not use PP Neue Montreal below 12px - the grotesque loses character at small sizes; switch to GT America Mono for anything sub-14px.
- Do not center headlines or wrap them - display type stays flush-left and bleeds toward the page edge.
- Do not use cards with backgrounds, padding, or radius - content sits directly on the bone canvas divided only by hairlines.
- Do not use a system font fallback for hero type - if PP Neue Montreal is unavailable, substitute with a grotesque (Inter or Sohne), not a humanist sans.

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
