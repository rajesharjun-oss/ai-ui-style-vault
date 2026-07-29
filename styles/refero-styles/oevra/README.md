# Oevra

Source: [Refero Style](https://styles.refero.design/style/01d6013d-a176-4a22-b7dd-fbd113592956) 
Reference site: [https://oevra.com](https://oevra.com) 
Captured: 2026-07-29 
Refero published: 2026-04-30T00:13:02.300Z 
Refero modified: 2026-06-05T05:23:50.837Z 
Theme: light 
Category: Productivity

## Style Summary

Explore Oevra's light Productivity design system: Eucalyptus #778643, Ink Black #000000 colors, space-regular, Suisse Int'l typography, and DESIGN.md for AI...

North star: sage greenhouse at dawn

## What To Borrow

- Eucalyptus `#ffffff` for Headline accents, body text emphasis, hairline borders, single filled CTA - the only chromatic voice in the entire system. Muted enough to never shout, present enough to carry the brand; Full-bleed background gradient behind hero and section text. The green is a breath, not a wall - it fades to white at the edges so text remains the focus
- Ink Black `#000000` for Primary text, dividers, image borders, icon strokes. Used at 1px hairline weight almost exclusively - never as a fill
- Pure Canvas `#ffffff` for Page background, card surfaces, button text on filled green CTAs. The dominant surface color across the entire site
- Graphite `#4e4e4e` for Secondary body text, muted link borders, helper copy, footer text. Quieter than black but still AA-readable on white
- Mist `#c8c8c8` for Subtle surface wash for elevated panels, image placeholder backgrounds, very faint dividers. Used sparingly to add depth without darkening the page

- space-regular `--font-space-regular` for space-regular - detected in extracted data but not described by AI
- Suisse Int'l `--font-suisse-intl` for Display and headline face. Light weight at 45-90px is the signature - headlines whisper instead of shout, creating a contemplative, editorial tone. Used for all section headlines, hero copy, and feature titles.
- Suisse Int'l `--font-suisse-intl` for Secondary body and footer text. Regular weight adds density to descriptions and supporting paragraphs beneath light-weight headlines.
- Space Grotesk `--font-space-grotesk` for Primary body, UI labels, buttons, and navigation text. The geometric counter-forms pair with Suisse to give dense text a different texture from the display headlines.
- System Sans `--font-system-sans` for Micro-utility text, scroll indicators, and fine-print captions where a 1-2 word label sits in the margins.
- ui-sans-serif `--font-ui-sans-serif` for ui-sans-serif - detected in extracted data but not described by AI
- suisse-light `--font-suisse-light` for suisse-light - detected in extracted data but not described by AI
- suisse-regular `--font-suisse-regular` for suisse-regular - detected in extracted data but not described by AI

## Avoid

- Do not introduce a second chromatic color - the entire palette is one green and four neutrals
- Do not use bold or semibold weights for headlines; light weight at large size is the signature
- Do not apply box-shadows, glows, or blur effects for elevation - separation comes from whitespace and hairlines
- Do not use sharp corners (0-4px radius) on any surface or interactive element
- Do not use #778643 as a solid page or section background - it must always be diluted by the gradient or rendered as a thin line
- Do not crowd the layout with small text; if a paragraph exceeds 3 lines, the type is too small for the system
- Do not use icon fills or saturated illustrations - the visual language is photography, type, and gradient only

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
