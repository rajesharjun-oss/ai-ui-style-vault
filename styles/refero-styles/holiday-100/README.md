# Holiday 100

Source: [Refero Style](https://styles.refero.design/style/48fa5bef-d910-40e1-b9b0-c0fcad055c6f)
Reference site: [https://shopping.google.com/m/bestthings](https://shopping.google.com/m/bestthings)
Captured: 2026-07-30
Refero published: 2026-04-30T03:56:15.894Z
Refero modified: 2026-06-05T12:24:15.793Z
Theme: dark
Category: E-commerce

## Style Summary

Explore Holiday 100's dark E-commerce design system: Onyx Canvas #333438, Graphite Card #202124 colors, Crimson Pro, Google Sans typography, and DESIGN.md...

North star: midnight gift gallery - the serif headline acts as the spotlight, the dark canvas is the velvet wall, and each product image hangs like a curated frame.

## What To Borrow

- Onyx Canvas `#333438` for Page background - the primary dark surface that absorbs all surrounding chrome and lets photography and accent color carry visual weight
- Graphite Card `#202124` for Card and product tile surfaces - one step lifted from the canvas, used for product listings, trending panels, and secondary groupings
- Charcoal Border `#1f1f1f` for Hairline borders on inputs, icons, and button edges - barely visible, defines boundaries without breaking the dark atmosphere
- Muted Iron `#9e9e9e` for Muted helper text, secondary icon strokes, and low-emphasis metadata
- Fog `#45474c` for Subtle link borders and tertiary structural lines
- Snow `#e8e8e8` for Hairline borders, dividers, input outlines, and card edges on light surfaces. Do not promote it to the primary CTA color
- Ice Blue `#99c3ff` for Outlined accent borders and decorative strokes on links, images, and card frames - the cool chromatic signature that brands links and featured borders without filling them
- Crimson Spotlight `#980b0b` for Red outline accent for tags, dividers, and focused UI edges.
- Royal Blue `#113979` for Category tile background for Electronics - a saturated mid-blue that gives gadgets a stage
- Powder Wash `#d2e3fc` for Light blue category background for Accessories - a desaturated counterweight to the deeper Royal Blue
- Forest `#073618` for Category tile background for Toys & Games and Home & Garden - deep green anchors the more organic categories
- Mint `#a8dab5` for Light green category background for Health & Wellness - the fresh, airy counterpart to Forest
- Butter `#ffedb8` for Category tile background for Beauty - warm pale yellow that softens the cosmetic category
- Sky Tint `#e8f0fe` for Lightest blue wash, used as a text/foreground pairing on dark accent backgrounds to guarantee AAA contrast
- Violet Whisper `#c58af9` for Rare accent - appears on a small number of links, probably AI-related or featured annotation links

- Crimson Pro `--font-crimson-pro` for Display serif for the editorial headline moments. The 220px weight 200 'Holiday 100' wordmark is the single most identifiable element - a high-contrast serif at extreme size that signals 'curated annual feature' rather than a standard product page. Also used at 80px for section headers with italic emphasis on category names ('Beauty Maven' in italic).
- Google Sans `--font-google-sans` for Primary UI and body typeface. Used for subtitles, category labels, card titles, button text, and product metadata. The weight 200 light variant is a distinctive choice - it keeps body text from feeling heavy against the dark canvas and pairs naturally with the serif display weights. The consistent -0.02em tracking across all sizes tightens the type into a controlled grid.
- Arial `--font-arial` for System fallback for ancillary content; sparse usage means it serves as safety net for elements not styled in the custom fonts.

## Avoid

- Do not add drop shadows or elevation effects - the design uses flat tonal contrast, not shadows.
- Do not fill any button or CTA with a saturated color - all actions are ghost/outlined against the dark canvas.
- Do not use Crimson Pro for body or UI text - it is display-only, and mixing it into small sizes breaks the editorial hierarchy.
- Do not use light-theme surfaces or white card backgrounds - this is a dark-only system.
- Do not pair more than two accent colors in a single component - the category tiles work because each tile commits to one color.
- Do not use gradients - the design is built on flat color blocks and photography, no smooth transitions.
- Do not reduce the display headline below 80px - the editorial weight depends on the extreme scale.

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
