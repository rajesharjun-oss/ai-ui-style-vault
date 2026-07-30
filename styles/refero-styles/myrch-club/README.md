# Myrch Club

Source: [Refero Style](https://styles.refero.design/style/528683fb-6b17-4fc6-b37e-d831ee1b20e2)
Reference site: [https://www.myrch.club](https://www.myrch.club)
Captured: 2026-07-30
Refero published: 2026-04-30T03:20:21.933Z
Refero modified: 2026-06-05T12:56:26.316Z
Theme: light
Category: Media

## Style Summary

Explore Myrch Club's light Media design system: Canvas White #ffffff, Gallery Gray #f9f9f9 colors, Times New Roman, Arial Narrow typography, and DESIGN.md...

North star: white-walled exhibition vitrine - editorial serif labels floating in generous negative space, disrupted by a single red script signature

## What To Borrow

- Canvas White `#ffffff` for Page background, image surfaces, inverted text on dark chips
- Gallery Gray `#f9f9f9` for Card and product tile backgrounds - sets objects apart from the page with a whisper of warmth
- Hairline Gray `#cfcfcf` for Dividers, secondary borders, placeholder structure
- Caption Gray `#888888` for Secondary text, metadata, timestamps, muted helper labels
- Ink Black `#111111` for Primary text, filled filter chips, button borders, headings - the dominant interface color
- True Black `#000000` for Hard borders and text where maximum contrast is needed
- Signature Red `#ff0000` for The wordmark only - a pure, unmoderated red used at oversized scale behind the header as a brand watermark; never used for buttons, links, or functional UI

- Times New Roman `--font-times-new-roman` for Primary body and interface type - used for descriptions, product metadata, and general reading text. The serif choice signals editorial/archive intent; a humanist serif substitute like EB Garamond or Lora preserves the curatorial atmosphere
- Arial Narrow `--font-arial-narrow` for Secondary structural type - condensed sans for compact labels, filter chips, navigation, and the 42px brand name in the header. The narrow proportions contrast the serif body and create catalog/inventory utility. Substitute with a condensed grotesk like Barlow Condensed or Roboto Condensed

## Avoid

- Do not use #ff0000 for buttons, links, tags, error states, or any functional UI element.
- Do not introduce additional accent colors - the system is strictly monochrome with one red artwork exception.
- Do not use heavy or stacked shadows; the single 20px 30%-opacity blur is the maximum elevation allowed.
- Do not use bold or display-weight typography; both Times and Arial Narrow appear at weight 400 only.
- Do not fill buttons with chromatic colors - buttons should be #111111 fill on #ffffff or outlined #111111.
- Do not use rounded or pill shapes (9999px radius) - the 10px radius is deliberate and consistent.
- Do not add gradients, glows, or colored backgrounds to the product cards.

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
