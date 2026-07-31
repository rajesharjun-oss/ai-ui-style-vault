# Studio Oker

Source: [Refero Style](https://styles.refero.design/style/e045b276-ae8d-442e-98de-fa8650e284de)
Reference site: [https://oker.com](https://oker.com)
Captured: 2026-07-31
Refero published: 2026-04-30T02:58:18.049Z
Refero modified: 2026-06-05T10:19:36.327Z
Theme: dark
Category: Agency

## Style Summary

Explore Studio Oker's dark Agency design system: Pure Black #000000, Soft Black #101010 colors, NextBook, Circular Std typography, and DESIGN.md for AI agents.

North star: darkened gallery with scarlet punctuation - a black-walled portfolio room where white type floats and one red whisper cuts through the silence.

## What To Borrow

- Pure Black `#000000` for Page canvas, section backgrounds, project card fills - the void everything else floats on
- Soft Black `#101010` for Subtle surface elevation over the pure black canvas, card backgrounds in tight stacks
- Bone White `#ffffff` for Primary text, headings, hairline borders, nav text - the only light in the room
- Fog Gray `#a0a0a0` for Secondary text, metadata, captions, image borders, inactive labels
- Graphite `#484848` for Footer borders, section dividers, rare structural lines that recede into the dark
- Scarlet Signal `#e4002b` for Supporting palette color for small decorative accents when the core palette needs contrast.
- Rose Brand Spectrum `#f5a5a5` for Brand color exploration panel - a pink-to-black swatch that walks from #f5a5a5 #e85a5a #d42020 #7a0a0a #2a0606 #000000 as a literal brand-color system reveal

- NextBook `--font-nextbook` for The studio's own custom display and text face. Weight 300 whispers in section headings and 80px display; weight 400 carries body, labels, and nav. Used across every context - hero, body, heading, link, list, icon, footer.
- Circular Std `--font-circular-std` for Referenced inside project case studies (the 'AaBbCc 1234' specimen tile) as a client font example - not part of Studio Oker's own UI system

## Avoid

- Don't add drop shadows, inner shadows, or glow effects - the system uses void, not elevation, to separate elements
- Don't introduce a second accent color - the scarlet is the only chromatic signal in the entire system
- Don't use bullet points, numbered lists, or icon prefixes in body copy - the Services list and Studio stat block prove that raw stacked text carries more weight than decorated lists
- Don't center-align body paragraphs - every long-form block is left-aligned and reads as a typographic column, not a display statement
- Don't use buttons with backgrounds - actions are dots, links, or text; the red dot IS the button
- Don't add gradients to UI elements (the rose panel is a single brand artifact, not a pattern to replicate on cards, buttons, or backgrounds)
- Don't use NextBook weight 600+ - the system only operates at 300 and 400; bolder weights would break the whisper-confident voice

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
