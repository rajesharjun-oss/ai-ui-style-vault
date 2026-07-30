# Beau

Source: [Refero Style](https://styles.refero.design/style/c73ba3d8-42fe-4d53-bec1-b6643949c582)
Reference site: [https://beau.to](https://beau.to)
Captured: 2026-07-30
Refero published: 2026-04-30T03:48:13.480Z
Refero modified: 2026-06-05T12:42:13.381Z
Theme: light
Category: SaaS

## Style Summary

Explore Beau's light SaaS design system: Paper White #ffffff, Warm Parchment #f6f4f1 colors, Geist typography, and DESIGN.md for AI agents.

North star: Ink on warm parchment - confident monochromatic editorial with a single theatrical gradient spotlight.

## What To Borrow

- Paper White `#ffffff` for Primary page canvas, card surfaces, button text on dark fills
- Warm Parchment `#f6f4f1` for Alternate section surface - gives the cream/ivory warmth that stops the page from feeling clinical
- Ink Black `#000000` for Primary text, dark feature card surfaces, filled pill button background, hairline borders - the structural backbone of every screen
- Soft Graphite `#666666` for Secondary text, muted helper copy, quiet borders on neutral sections
- Mid Ash `#999999` for Tertiary metadata, section subtitles, low-emphasis text
- Pale Mist `#b3b3b3` for Disabled badge fill, very low-emphasis surface washes

- Geist `--font-geist` for Sole typeface across nav, body, headings, and buttons. Weight 400 carries body and most copy; weight 500 is reserved for subheadings, labels, and emphasis. The Geist stylistic sets ss01, ss03, ss04 are enabled - these alter the alternate single-storey 'a', the geometric 'g', and the modernist '$' to give the type a custom editorial feel. Substitute with Inter at the same weights if Geist is unavailable.

## Avoid

- Do not introduce any chromatic color outside the broadcast gradient - the system is monochrome by design
- Do not use 6px or 8px radius on buttons or pills - only 200px (full pill) is correct
- Do not use heavy shadows or elevation - the only approved shadow is the 2px 6%-black atmospheric haze
- Do not use type weights outside 400 and 500 - bold and semibold would break the restrained editorial voice
- Do not place white cards on the gradient band - use dark (#000000) feature cards or let the gradient breathe
- Do not use #0000ee or browser-default link blue - links are always black with optional underline
- Do not crowd sections - if a section feels tight, increase the 72px gap rather than reducing font sizes

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
