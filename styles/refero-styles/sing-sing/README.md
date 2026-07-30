# Sing-sing

Source: [Refero Style](https://styles.refero.design/style/12b20c12-27f8-4938-89ba-569404d36fe8)
Reference site: [https://sing-sing.co](https://sing-sing.co)
Captured: 2026-07-30
Refero published: 2026-04-30T03:51:20.805Z
Refero modified: 2026-06-05T12:20:58.193Z
Theme: light
Category: Agency

## Style Summary

Explore Sing-sing's light Agency design system: Marigold #fcd579, Sea Glass #81d6b9 colors, untitledsans, signifier typography, and DESIGN.md for AI agents.

North star: butter-paper broadsheet at golden hour - a warm saffron canvas with sea-glass ink.

## What To Borrow

- Marigold `#fcd579` for Page canvas, full-bleed backgrounds, the base layer every other element sits on
- Sea Glass `#81d6b9` for Decorative stroke accent - horizontal stripe pattern, top page divider, wordmark underline, gradient terminus
- Inkstone `#171717` for Primary text, nav labels, headings, logo wordmark, and all interface borders
- Marigold Gradient `#81d6b9` for Right terminus of the signature horizontal gradient (teal warm gold) used for stripe fades and section dividers

- untitledsans `--font-untitledsans` for Primary typeface across all contexts - body copy, nav, footer, links, and the colossal display wordmark. The 147px size at tight tracking (-0.025em) is the identity: the word 'Sing' becomes a spatial event, not a heading. Weight 400 carries body and nav; weight 700 anchors headings and footer emphasis. Kern feature is active throughout to manage the extreme size range.
- signifier `--font-signifier` for Secondary editorial typeface - used for rotated/vertical captions beside photography and occasional body annotations. Its serif presence contrasts the grotesk wordmark to introduce a magazine-like voice. Normal letter-spacing; the small size keeps it as whisper copy, never a headline.

## Avoid

- Do not introduce shadows, cards, or elevated surfaces - the system is flat by design
- Do not add white, gray, or off-white backgrounds; marigold is the only canvas
- Do not use teal (#81d6b9) as a button fill or large color block - it is a line/stroke accent only
- Do not create rounded corners on any element; the aesthetic is architectural and sharp
- Do not use multiple accent colors; the system is two chromatic notes (teal + yellow) on black ink
- Do not add decorative borders, boxes, or containers around text or images
- Do not use a traditional grid card system - layout is art-directed, not modular

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
