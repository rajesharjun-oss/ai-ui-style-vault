# Monzo

Source: [Refero Style](https://styles.refero.design/style/e8a1d114-6924-4f03-acd2-996dd30f15a6)
Reference site: [https://monzo.com](https://monzo.com)
Captured: 2026-07-31
Refero published: 2026-03-20T11:28:18.000Z
Refero modified: 2026-06-05T09:07:11.459Z
Theme: light
Category: Fintech

## Style Summary

Explore Monzo's light Fintech design system: Hot Coral #ff4f40, Midnight Ink #091723 colors, MonzoSansText, MonzoSansDisplay typography, and DESIGN.md for...

North star: Warm coral on cool mint paper - confident restraint with a single hot accent.

## What To Borrow

- Hot Coral `#ff4f40` for Brand signature - logo, links, headings, icons, card product. One vivid accent against the achromatic interface; every chromatic moment in the system draws from this single hue
- Midnight Ink `#091723` for Dark supporting neutral for text, icons, and strong contrast. Do not promote it to the primary CTA color
- Deep Navy `#112231` for Secondary surface tint and footer accents. Slightly lighter than Midnight Ink for layered dark elements
- Page Mist `#f2f8f3` for Page canvas - the dominant background behind all content sections. A barely-green off-white that gives the interface warmth without competing with white surfaces
- Pure White `#ffffff` for Card surfaces, elevated panels, button text on dark fills. Sits one layer above the mint canvas
- Soft Mint `#e3ebe4` for Hover washes, subtle filled buttons, inset surface treatment. Sits between the page canvas and white cards
- Fog `#b5b9bd` for Tertiary text, placeholder, low-emphasis borders
- Steel `#6b747b` for Secondary body text, metadata, descriptive copy. The workhorse neutral for supporting information
- Ash `#75817e` for Icon strokes, decorative line work, subtle dividers
- Slate Button `#3b4c54` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color
- Pure Black `#000000` for Maximum-contrast text, the darkest token in the system. Used sparingly for the highest-emphasis text on light surfaces

- MonzoSansText `--font-monzosanstext` for Body and UI text - navigation labels, button copy, descriptive paragraphs, card content, footer text. The custom -0.05em letter-spacing tightens running text for a dense, modern feel; the 400/600/700 spread lets the same family handle everything from captions to subheadings. Substitute with Inter or DM Sans if unavailable.
- MonzoSansDisplay `--font-monzosansdisplay` for Headlines and display text - hero statements, section headings, large product titles. Bolder weights (up to 800) at large sizes (39-61px) create confident, blocky headlines that feel architectural. No custom letter-spacing, letting the weight do the work. Substitute with Inter or Manrope at heavy weights.

## Avoid

- Don't use Hot Coral as a button background fill. It is for text, icons, logos, and the card product only - never for a solid CTA surface.
- Don't add drop shadows to cards or buttons. The system uses a single rgba(0,0,0,0.1) 0px 0px 10px shadow sparingly; most separation comes from surface color stepping on the mint canvas.
- Don't use system fonts or non-brand sans-serifs. Always specify MonzoSansText for body and MonzoSansDisplay for headings.
- Don't use letter-spacing other than -0.05em on MonzoSansText or normal on MonzoSansDisplay. Deviating breaks the brand's typographic fingerprint.
- Don't mix red and dark navy as a gradient or color pair on the same element. Coral is the accent; navy is the ground. They alternate, they don't blend.
- Don't use square or 8px radii on primary buttons or large containers. 500px pills and 64px containers are the two shape languages - anything between looks generic.
- Don't set body text below 16px or headlines below 32px. The type scale is deliberately generous; small text breaks the warm, spacious feel.

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
