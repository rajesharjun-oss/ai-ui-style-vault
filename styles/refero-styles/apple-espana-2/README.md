# Apple Espana

Source: [Refero Style](https://styles.refero.design/style/569ba4c0-0431-44fb-92df-0dbea7f3e63d)  
Reference site: [https://www.apple.com/apple-watch-se-3](https://www.apple.com/apple-watch-se-3)  
Captured: 2026-07-29  
Refero published: 2026-05-10T23:17:26.250Z  
Refero modified: 2026-06-03T19:27:03.561Z  
Theme: light  
Category: E-commerce

## Style Summary

Explore Apple (Espaa)'s light E-commerce design system: Pure Canvas #f5f5f7, Paper White #ffffff colors, SF Pro Display, SF Pro Text typography, and...

North star: white museum gallery at noon

## What To Borrow

- Pure Canvas `#f5f5f7` as Page background, section bands, card surfaces a near-white that separates structural surfaces from pure white product highlights without introducing tint
- Paper White `#ffffff` as Elevated card surfaces, icon fills, and inverted text on dark/colored backgrounds
- Obsidian `#1d1d1f` as Primary text, headlines, card borders, nav rules the singular dark anchor; not pure black, a graphite that softens contrast on white
- Iron Gray `#707070` as Secondary nav borders, list dividers, subdued UI metadata
- Slate `#474747` as Nav borders, link underlines, secondary text in dense lists
- Charcoal `#333336` as Nav text, button labels on neutral surfaces slightly cool graphite for UI controls
- SF Pro Display Hero headlines, section headings, and the page-level brand statement. Set in semibold at very large sizes (6496px) with aggressive negative tracking (-0.019em to -0.005em) that tightens the headline into a single confident block. Smaller sizes (2128px) carry section headings and card titles. The signature choice: weight 600 is the heaviest weight on the entire site Apple trusts display weight 600 over 700+ to command the page `--font-sf-pro-display` for the source typography voice
- SF Pro Text Body copy, nav labels, button text, spec text, and large display numerals (44px). Weight 400 is the paragraph default; weight 600 marks links, button labels, and emphasis within body text. The 44px instance is a display-numeral role used for prices or large data it borrows SF Pro Text rather than Display because the data needs to feel tabular, not editorial `--font-sf-pro-text` for the source typography voice
- source-defined base spacing with comfortable density
- Source radius system: nav 980px, cards 28px, links 10px, buttons 980px

## Avoid

- Do not introduce box-shadows, glows, or drop-shadows elevation comes from surface contrast and 1px hairlines only
- Do not use the chromatic accent colors (green, violet, orange, teal) for backgrounds, buttons, or large fills they are word-tints only
- Do not use #0000ee or any unstyled browser-default link color always #0066cc with a 1px underline
- Do not set body copy above 20px or below 14px; 17px is the singular paragraph size
- Do not use a border-radius value other than 10px, 28px, 32px, 36px, or 980px these are the only radii in the system
- Do not center the hero headline or the price+CTA cluster left-alignment is structural, not stylistic
- Do not apply gradients to text, buttons, or cards; gradients are reserved for potential future decorative use and are not a current pattern on the product surface

## Bundle Contents

- [DESIGN.md](DESIGN.md): implementation notes.
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
