# AI Implementation Prompt

Build a Shopify-inspired interface using this source-derived style bundle.

Reference site: https://www.shopify.com
Theme: dark
Category: E-commerce
North star: Midnight greenhouse - merchants' brands blooming against deep teal-black, lit by a single mint spark.

Use these palette anchors:

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

Use these typography anchors:

- Neue Haas Grotesk `--font-neue-haas-grotesk` for Primary type system - display headlines at 70-96px weight 330-400 whisper scale rather than shout it; body at 16-18px weight 400-500; nav and UI at 14-16px weight 500-550. The ultra-light 330 weight at display sizes is the signature: it says confidence through restraint, not volume.
- Inter Variable `--font-inter-variable` for Secondary utility type - used in nav chrome, small UI labels, tab controls, footer micro-copy. The slightly higher x-height and more standard tracking make it more legible at compact sizes. Also serves where weight 420 fills the gap between regular and medium.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1280px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 12px.

Build these component patterns where relevant:

- Primary Pill Button: Main call-to-action
- Ghost Pill Button: Secondary action
- Dark Surface Card: Content container
- Raised Showcase Card: Hero/feature card with lift
- Navigation Bar: Top-level site navigation
- Feature Image Card: Merchant showcase tile
- Product Preview Card: Inline product/storefront embed
- Eyebrow Label: Section pre-title / category tag
- Display Headline: Page-level hero text
- Body Copy: Paragraph text and descriptions
- Minting Link: Inline text link with accent
- Flag/Icon Chip: Country selector or status indicator

Do:

- Use weight 330-400 Neue Haas Grotesk at 70-96px for display headlines - the ultra-light weight at extreme size is the system's most distinctive signature.
- Set the canvas to #02090a for all pages; use #061a1c for cards and #1e2c31 for hairline borders to build the layered dark surface stack.
- Use pill buttons (9999px radius) for all primary and secondary actions - square or slightly rounded buttons break the system's silhouette.
- Reserve #36f4a4 for functional moments: active nav, focus rings, key link accents, highlight tags. Never use it for decorative fills or large background areas.
- Apply letter-spacing 0.015-0.04em on Neue Haas Grotesk at 48px+; tight tracking on heavy display type but slightly opened on small sizes.
- Use 12px radius for cards and 4px for inputs/buttons - these two values carry the geometric identity.
- Set font-feature-settings to "ss03" on both type families to preserve the alternate character set that defines the brand's typographic feel.

Avoid:

- Don't use weight 600+ at display sizes - it overpowers the whisper-light headlines and collapses the system's contrast between headline and body.
- Don't introduce new chromatic colors for buttons or CTAs - white pill on dark is the only primary action; ghost white-bordered pill is the only secondary.
- Don't use #36f4a4 as a background fill or large surface color - it loses its power as a functional spark when applied broadly.
- Don't add drop shadows beyond the subtle inset highlights - heavy shadows break the flat dark-surface language and the inset-bright border convention.
- Don't use radius values other than 12px (cards), 4px (inputs), or 9999px (pills) - inconsistent rounding breaks the geometric consistency.
- Don't use light-theme colors (white surfaces, dark text) except inside merchant/product embeds where the merchant's own content takes over.
- Don't set body copy in #ffffff - use #99b3ad or #a1a1aa so the hierarchy between headline (white) and paragraph (muted) remains intact.

Source prompt cues:

**Quick Color Reference**
- canvas: #02090a
- card surface: #061a1c
- border: #1e2c31
- primary text: #ffffff
- body text: #99b3ad
- accent: #36f4a4
- primary action: #ffffff (filled action)

**Example Component Prompts**

1. **Dark hero with full-bleed image**: Background photo at 100% viewport width. Centered overlay: headline 70px Neue Haas Grotesk weight 330, #ffffff, letter-spacing 0.04em. Subtext 18px weight 400, #99b3ad. Two pill buttons below: white fill #ffffff with #02090a text, and ghost with 1px #ffffff border and white text; both 9999px radius, 12px 24px padding, 16px Inter Variable weight 550.

2. **Feature card grid**: Three columns on dark canvas #02090a, 16px gap. Each card: #061a1c fill, 1px #1e2c31 border, 12px radius, 24px padding. Image at top at 12px radius. Heading 24px Neue Haas Grotesk weight 500, #ffffff. Body 16px weight 400, #99b3ad.

3. **Product embed panel**: Floating card on #02090a canvas. Card: #072720 fill, 20px radius, 32px padding, with inset border 1px #133b32. Inside: product image on white (#ffffff) sub-surface at 12px radius, product title 18px weight 500 #ffffff, price 16px #99b3ad, dark pill buy button (#02090a fill, #ffffff text, 9999px radius).

4. **Mint accent link block**: Section heading 48px weight 400 #ffffff, followed by inline link text 16px weight 500 in #36f4a4, no underline by default, 1px solid #36f4a4 on hover. Eyebrow above: 12px Inter Variable weight 550, 0.06em tracking, uppercase, #99b3ad.

5. Create a Primary Action Button: #ffffff background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
