# Craft

Source: [Refero Style](https://styles.refero.design/style/329075e8-97ed-4722-8952-d9bf001de233)
Reference site: [https://itscraft.com](https://itscraft.com)
Captured: 2026-07-31
Refero published: 2026-04-30T00:23:24.812Z
Refero modified: 2026-06-05T10:23:25.403Z
Theme: light
Category: Agency

## Style Summary

Explore Craft's light Agency design system: Bone Linen #f7f5f2, Oat Milk #eae6df colors, ABC Arizona Flare Condensed Variable, ABC Arizona Flare Variable...

North star: botanical conservatory on warm parchment - cream pages holding vivid green specimens and one quiet forest room.

## What To Borrow

- Bone Linen `#f7f5f2` for Page canvas, body backgrounds - the warm off-white that carries almost every section and makes the dark hero and green accents feel like specimens on display
- Oat Milk `#eae6df` for Card surfaces, elevated panels, secondary containers - a half-step darker than the canvas for gentle separation without shadow
- Driftwood `#d7d2cc` for Hairline borders, dividers, structural separators - warm gray that reads as line work, not as color
- Ash Mauve `#645757` for Secondary text, captions, muted labels - used where near-black would be too heavy, sits at 80 instances
- Mahogany Hush `#504344` for Dark accent for small headings and emphasis - warmer alternative to the primary text color when a touch of depth is needed
- Obsidian Plum `#2a1a1d` for Primary text, body copy, all headings, nav links - a near-black with warm plum undertone that pairs with the cream canvas at 15.3:1 contrast
- Forest Depths `#1d3023` for Hero section background, dark surface, outlined ghost-button borders - the deep green room that introduces the brand and reappears as a dark contrast panel
- Lime Pulse `#26d862` for Primary action buttons, inline links, accent words inside headlines, active nav states - vivid green used sparingly as functional punctuation, never as decoration
- Peacock Teal `#0e634f` for Stat numbers, data emphasis - a deeper teal that shares hue with the forest hero but reads quieter so it can carry numerical data in stat cards

- ABC Arizona Flare Condensed Variable `--font-abc-arizona-flare-condensed-variable` for Display and large headings - the condensed serif runs at 180px for the hero statement and steps down through 104, 48, 26, 20px for section headlines. Weight 300 carries the largest sizes, weight 400 takes the mid range. Negative tracking tightens at every size.
- ABC Arizona Flare Variable `--font-abc-arizona-flare-variable` for Body, nav, buttons, cards, captions, and mid-size headings up to 32px. Weight 350 handles 32px headings, weight 400 takes body and UI. The lighter weight at 32px keeps subheadings from competing with the condensed display sizes.

## Avoid

- Don't introduce a new font family - the system runs on exactly two custom serifs (Arizona Flare and Arizona Flare Condensed) and the contrast between them is the signature
- Don't use Lime Pulse #26d862 for body text, borders, or decorative fills - it is exclusively an action and link color
- Don't apply box-shadows to cards or buttons - separation comes from the two-tone cream surface and 8px radius
- Don't mix line-height styles within a size - 0.85 for display (48px+), 1.08 for subheadings (20-32px), 1.18-1.50 for body (12-18px)
- Don't center-align body paragraphs longer than 2 lines - left-align at max-width 720px for readability
- Don't use the Peaacock Teal #0e634f outside of numerical data contexts - it is reserved for stat numbers and data emphasis
- Don't place colored text on the dark Forest Depths hero unless it's Bone Linen #f7f5f2 - the contrast math is tuned for cream-on-forest, not green-on-forest

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
