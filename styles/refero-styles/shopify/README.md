# Shopify

Source: [Refero Style](https://styles.refero.design/style/f212ff99-24fa-4646-a0f2-46a815736ecd)
Reference site: [https://www.shopify.com](https://www.shopify.com)
Captured: 2026-07-30
Refero published: 2026-04-29T00:21:46.446Z
Refero modified: 2026-06-05T12:44:03.588Z
Theme: dark
Category: E-commerce

## Style Summary

Explore Shopify's dark E-commerce design system: Midnight Forest #02090a, Deep Lichen #061a1c colors, Neue Haas Grotesk, Inter Variable typography, and...

North star: Midnight greenhouse - merchants' brands blooming against deep teal-black, lit by a single mint spark.

## What To Borrow

- Midnight Forest `#02090a` for Page canvas, hero backgrounds, section backgrounds
- Deep Lichen `#061a1c` for Primary card surfaces, elevated panels, content blocks
- Shaded Fern `#072720` for Navigation bar, secondary cards, subtle panel lift
- Spruce Border `#1e2c31` for Hairline card borders, divider lines, input outlines
- Abyss Indigo `#000a1e` for Secondary surface for product/demo embeds, feature panels
- Pure White `#ffffff` for Primary text, button fills, heading copy, logo marks
- Mist Gray `#a1a1aa` for Body text, secondary copy, muted labels, footer links
- Sage Gray `#99b3ad` for Body paragraphs, description text with subtle teal warmth
- Faded Steel `#9dabad` for Link text, breadcrumb labels, tertiary copy
- Soft Pearl `#9797a2` for Helper text, micro-copy, metadata labels
- Carbon Black `#000000` for Icon fills, nav SVG strokes, maximum-contrast text
- Slate `#71717a` for Headings needing reduced emphasis, section eyebrows
- Graphite `#333333` for Disabled button backgrounds, inactive control states
- Shopify Mint `#36f4a4` for Active nav indicators, focus rings, highlight tags, link hover accents - the single chromatic spark that makes interactivity feel switched on against the dark canvas
- Mossy Edge `#133b32` for Inset borders on elevated cards, subtle separator strokes with teal undertone

- Neue Haas Grotesk `--font-neue-haas-grotesk` for Primary type system - display headlines at 70-96px weight 330-400 whisper scale rather than shout it; body at 16-18px weight 400-500; nav and UI at 14-16px weight 500-550. The ultra-light 330 weight at display sizes is the signature: it says confidence through restraint, not volume.
- Inter Variable `--font-inter-variable` for Secondary utility type - used in nav chrome, small UI labels, tab controls, footer micro-copy. The slightly higher x-height and more standard tracking make it more legible at compact sizes. Also serves where weight 420 fills the gap between regular and medium.

## Avoid

- Don't use weight 600+ at display sizes - it overpowers the whisper-light headlines and collapses the system's contrast between headline and body.
- Don't introduce new chromatic colors for buttons or CTAs - white pill on dark is the only primary action; ghost white-bordered pill is the only secondary.
- Don't use #36f4a4 as a background fill or large surface color - it loses its power as a functional spark when applied broadly.
- Don't add drop shadows beyond the subtle inset highlights - heavy shadows break the flat dark-surface language and the inset-bright border convention.
- Don't use radius values other than 12px (cards), 4px (inputs), or 9999px (pills) - inconsistent rounding breaks the geometric consistency.
- Don't use light-theme colors (white surfaces, dark text) except inside merchant/product embeds where the merchant's own content takes over.
- Don't set body copy in #ffffff - use #99b3ad or #a1a1aa so the hierarchy between headline (white) and paragraph (muted) remains intact.

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
