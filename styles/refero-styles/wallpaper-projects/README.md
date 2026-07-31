# Wallpaper Projects

Source: [Refero Style](https://styles.refero.design/style/0a2bcda6-b5b9-463d-bc8d-2c7ccaa2b776)
Reference site: [https://wallpaperprojects.com](https://wallpaperprojects.com)
Captured: 2026-07-31
Refero published: 2026-04-30T02:08:17.397Z
Refero modified: 2026-06-05T11:49:44.063Z
Theme: light
Category: Agency

## Style Summary

Explore Wallpaper Projects's light Agency design system: Ink Black #1e1e1e, Paper White #ffffff colors, Cardinal Fruit, Soehne Breit Buch typography, and...

North star: Editorial gallery on warm paper - a spread from a 12x16 art monograph where cream stock, near-black ink, and one enormous serif do all the talking.

## What To Borrow

- Ink Black `#1e1e1e` for Primary text, dark pill button fills, borders, heading strokes - the only ink in the system
- Paper White `#ffffff` for Primary canvas, image backgrounds, button text on dark fills
- Warm Cream `#fbf9f3` for Alternate surface - the signature cream stock that gives the system its editorial warmth, used for secondary sections and cards
- Pure Black `#000000` for Maximum contrast moments, occasional true-black text where #1e1e1 isn't dark enough

- Cardinal Fruit `--font-cardinal-fruit` for The signature display serif - exclusively used for hero headlines, section openers, and any moment that needs to feel like a magazine cover. The medium weight (500) is reserved for the most massive treatments (132-180px) where hairline strokes would disappear. Negative letter-spacing tightens the massive forms into a cohesive block of ink.
- Soehne Breit Buch `--font-soehne-breit-buch` for The workhorse grotesque with widened proportions. At small sizes (10-14px) the 0.1em tracking creates the editorial 'kicker' label aesthetic. At 72-80px it serves as a secondary display face for contexts where serif would feel too precious. The 600 weight is used sparingly for emphasis.
- Soehne Mono Buch `--font-soehne-mono-buch` for Monospaced UI face for technical labels, metadata, button text, and small data displays. Its presence signals 'system metadata' versus 'editorial content' - the mono is the interface voice, the serif is the gallery voice.

## Avoid

- Never introduce chromatic colors - the 0% colorfulness is the entire brand
- Never use box-shadow for elevation; let surface color contrast do the work
- Never use a border-radius other than 20px for interactive elements or 0px for images/cards
- Never set body text below 14px or above 18px; the editorial scale is fixed
- Never use the display serif (Cardinal Fruit) at sizes below 36px - it loses its character
- Never add visible dividers, rules, or borders between sections - whitespace is the only separator
- Never darken or overlay hero photography; let the type sit directly on the raw image

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
