# Zeus Jones

Source: [Refero Style](https://styles.refero.design/style/b619e1b9-86ee-4a10-b6e6-47b10927c3a2)
Reference site: [https://zeusjones.com](https://zeusjones.com)
Captured: 2026-07-31
Refero published: 2026-04-30T03:11:09.802Z
Refero modified: 2026-06-05T11:45:54.499Z
Theme: light
Category: Agency

## Style Summary

Explore Zeus Jones's light Agency design system: Midnight Ink #1a1c2c, Warm Parchment #fcfaf3 colors, ZJSansDisplay, FeatureDeckLight typography, and...

North star: risograph broadsheet on warm cream - a page that prints like a zine and loads like a gallery.

## What To Borrow

- Midnight Ink `#1a1c2c` for Primary text, filled pill buttons, hairline borders, dark surfaces - the only chromatic color in the system; near-black with a barely-perceptible cool navy cast that softens the contrast against warm cream without losing the gravitas of pure black
- Warm Parchment `#fcfaf3` for Page canvas and light surface base - a creamy off-white that replaces the default SaaS pure-white with paper warmth, making the page feel printed rather than rendered
- Soft Linen `#ebe9e4` for Elevated card and panel surface - one step darker than the canvas, used sparingly to lift a card or a section band without introducing a new color
- Obsidian `#000000` for SVG icon fills and decorative monochrome marks - reserved for vector assets where true black reads cleaner than the navy-tinted Midnight Ink
- Blush Coral `#fd9494` for Sporadic warm accent - emerges from the hero aurora and may surface in tag dots or decorative washes; the only warm hue that earns a place in an otherwise cool-neutral system

- ZJSansDisplay `--font-zjsansdisplay` for Primary typeface for body, navigation, subheadings, and the 40-48px heading range. The 12px eyebrow and tag text carries +0.05em tracking (letter-spacing: 0.6px at 12px) to read as a small caps eyebrow; everything at 16px and above sits at -0.02em (-0.32px at 16px) for tight, editorial density. This is the working sans that does 95% of the page's communicative labor.
- FeatureDeckLight `--font-featuredecklight` for Hero display face used at 60-90px with line-height compressed to 1.07-1.11. Weight 100 is the anti-convention signature: while every agency site uses 600-800 for display, this hairline weight makes the largest text the lightest on the page - authority through restraint, not volume. The italic cut is used for poetic emphasis words inside the headline (e.g. 'the world').

## Avoid

- Never use box-shadows or drop-shadows - the system is flat by design; use 1px borders and surface tonal steps for separation instead.
- Never use a bold or 600+ weight for display headlines - weight 100 at 60-90px is the signature; a bold version would erase the brand voice.
- Never introduce a new accent color for buttons, links, or interactive elements - the action is always filled Midnight Ink on Warm Parchment.
- Never use pure white (#ffffff) as a background - the canvas is Warm Parchment #fcfaf3; pure white would break the printed-paper quality.
- Never add a gradient to UI components, buttons, or cards - the system is solid-fill only; color gradients are reserved for the single full-bleed hero image.
- Never use sharp corners (0-4px radius) on cards or buttons - the system is either 20px rounded or fully pill-shaped; no in-between.
- Never use decorative dividers, background patterns, or ornamental graphics below the hero - the body of the site is typographic and photographic only.

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
