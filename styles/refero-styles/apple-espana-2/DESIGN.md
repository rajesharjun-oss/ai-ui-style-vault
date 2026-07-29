# Apple Espana Design Reference

## North Star

white museum gallery at noon

## Theme

light style for E-commerce interfaces.

## Color System

- Pure Canvas `#f5f5f7` for Page background, section bands, card surfaces a near-white that separates structural surfaces from pure white product highlights without introducing tint
- Paper White `#ffffff` for Elevated card surfaces, icon fills, and inverted text on dark/colored backgrounds
- Obsidian `#1d1d1f` for Primary text, headlines, card borders, nav rules the singular dark anchor; not pure black, a graphite that softens contrast on white
- Iron Gray `#707070` for Secondary nav borders, list dividers, subdued UI metadata
- Slate `#474747` for Nav borders, link underlines, secondary text in dense lists
- Charcoal `#333336` for Nav text, button labels on neutral surfaces slightly cool graphite for UI controls
- Mist `#e2e2e5` for Neutral pill button fill, secondary surface tier for compact controls and list rows
- Fog `#d6d6d6` for List row backgrounds, hairline separators in data-dense sections

Use the listed source colors as the authoritative palette. Keep the most saturated or highest-contrast color for primary action moments unless the component notes say otherwise.

## Typography

- SF Pro Display Hero headlines, section headings, and the page-level brand statement. Set in semibold at very large sizes (6496px) with aggressive negative tracking (-0.019em to -0.005em) that tightens the headline into a single confident block. Smaller sizes (2128px) carry section headings and card titles. The signature choice: weight 600 is the heaviest weight on the entire site Apple trusts display weight 600 over 700+ to command the page `--font-sf-pro-display`
- SF Pro Text Body copy, nav labels, button text, spec text, and large display numerals (44px). Weight 400 is the paragraph default; weight 600 marks links, button labels, and emphasis within body text. The 44px instance is a display-numeral role used for prices or large data it borrows SF Pro Text rather than Display because the data needs to feel tabular, not editorial `--font-sf-pro-text`

Use the source font pairing to preserve the visual voice. When custom fonts are not available, choose close substitutes with similar weight, width, and editorial character.

## Layout And Spacing

- Base unit: source-defined
- Density: comfortable
- Page max-width: 1440px
- Section gap: 80-120px
- Card padding: 28px
- Element gap: 8-12px

## Components

- Primary Action Button: The purchase or key conversion moment Apple's only filled chromatic button
- Neutral Pill Button: Secondary action 'Learn more', 'See all', disclosure expanders
- Pill Disclosure Item: Expandable spec detail rows in the 'Ms de cerca' (closer look) section
- Product Hero Block: Full-bleed product showcase above the fold
- Headline with Tinted Accent Words: Signature typographic pattern the colored-word-in-headline technique
- Feature Card: Large rectangular card for product close-up photography with caption
- Sticky Top Navigation: Global product line nav with pill background utility area
- Utility Bar: Slim promotional band above the main nav

## Implementation Guidance

- Use SF Pro Display weight 600 for any display-size headline; never go heavier than 600 the restraint is the authority
- Tint single words in headlines using #03aa49, #0066cc, #8668ff, #ed6300, or #00a1b3; keep the rest of the line #1d1d1f
- Use #0071e3 fill on a 980px pill as the sole primary action never apply this blue to text, borders, or non-button surfaces
- Set headlines left-aligned within a left-aligned content column; do not center display type
- Use 28px border-radius for cards and 980px (full pill) for buttons these two radii carry the entire shape language
- Pair every chromatic button with a #1d1d1f text label nearby (price, kicker) so the blue pill remains the singular attention point
- Let product photography fill the card; place caption text at the card's edge in a narrow column rather than overlaying the image

## Guardrails

- Do not introduce box-shadows, glows, or drop-shadows elevation comes from surface contrast and 1px hairlines only
- Do not use the chromatic accent colors (green, violet, orange, teal) for backgrounds, buttons, or large fills they are word-tints only
- Do not use #0000ee or any unstyled browser-default link color always #0066cc with a 1px underline
- Do not set body copy above 20px or below 14px; 17px is the singular paragraph size
- Do not use a border-radius value other than 10px, 28px, 32px, 36px, or 980px these are the only radii in the system
- Do not center the hero headline or the price+CTA cluster left-alignment is structural, not stylistic
- Do not apply gradients to text, buttons, or cards; gradients are reserved for potential future decorative use and are not a current pattern on the product surface
