# Woven

Source: [Refero Style](https://styles.refero.design/style/76483bd1-37d3-4fb9-889b-aecf27b08b83)
Reference site: [https://wovenwhisky.com](https://wovenwhisky.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:15:35.734Z
Refero modified: 2026-06-05T10:16:22.422Z
Theme: light
Category: E-commerce

## Style Summary

Explore Woven's light E-commerce design system: Parchment Cream #eeede5, Ink Black #232323 colors, Spezia Semi-Mono, Spezia Medium typography, and DESIGN.md...

North star: Ink on cream parchment. A distiller's editorial spread where warm cream canvases, a single dark ink color, and wide-tracked uppercase type create the only visual structure; product photography provides all the color.

## What To Borrow

- Parchment Cream `#eeede5` for Page canvas, footer surface, and dominant background - the warm off-white that gives the entire site its editorial, paper-like feel
- Ink Black `#232323` for Primary text, all hairline borders, footer ink, and the near-black that forms every structural line on the page
- Pure White `#ffffff` for Product card surfaces, alternating section backgrounds, and high-contrast text on dark or photographic surfaces
- Iron Gray `#4a4a4a` for Secondary body text, subdued borders, and the muted text layer that sits between primary ink and background
- Soft Stone `#ddddda` for Subtle surface differentiation beneath cards and secondary panels - barely warmer than the cream canvas

- Spezia Semi-Mono `--font-spezia-semi-mono` for The workhorse typeface for body copy, navigation links, card text, list items, and most UI labels. Semi-mono construction gives it a precise, typeset quality that reinforces the editorial identity. 700 weight is used sparingly for emphasis within mono-spaced blocks.
- Spezia Medium `--font-spezia-medium` for Headline and display font - the proportional companion to the Semi-Mono, used for the hero wordmark 'WOVEN' and section titles. Single weight keeps the type system disciplined; contrast comes from size and tracking, not weight.
- Figtree `--font-figtree` for Small UI utility font for buttons, icon labels, and tight navigation tags. Rounds out the system where a humanist sans feels warmer than the mono family.
- Spezia Semi-Mono Light `--font-spezia-semi-mono-light` for Lighter voice for inputs, helper text, and link descriptions - a whisper-weight variation that creates hierarchy without bold.

## Avoid

- Never add a chromatic accent color, gradient, or brand fill - the system is 0% colorful by design
- Never use rounded corners on cards, buttons, inputs, or images - 0px radius is intentional and defines the editorial print look
- Never apply box-shadow, drop-shadow, or blur effects - surfaces separate through color and hairline borders only
- Never use bold (700) weight for body paragraphs; reserve 700 for short emphasized spans within mono text blocks
- Never set headings left-aligned with body copy; section titles are always centered with generous vertical space above and below
- Never introduce an icon system with fills, duotones, or color - icons are single-weight 1.5-2px #232323 line work only
- Never place text directly on a product photograph without a cream or white surface underneath; readability requires a solid layer
- Never use display sizes below 32px for the wordmark or section openers; the type scale's authority comes from its restraint at small sizes and generosity at large ones

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
