# AI Implementation Prompt

Build a Craft-inspired interface using this source-derived style bundle.

Reference site: https://itscraft.com
Theme: light
Category: Agency
North star: botanical conservatory on warm parchment - cream pages holding vivid green specimens and one quiet forest room.

Use these palette anchors:

- Bone Linen `#f7f5f2` for Page canvas, body backgrounds - the warm off-white that carries almost every section and makes the dark hero and green accents feel like specimens on display
- Oat Milk `#eae6df` for Card surfaces, elevated panels, secondary containers - a half-step darker than the canvas for gentle separation without shadow
- Driftwood `#d7d2cc` for Hairline borders, dividers, structural separators - warm gray that reads as line work, not as color
- Ash Mauve `#645757` for Secondary text, captions, muted labels - used where near-black would be too heavy, sits at 80 instances
- Mahogany Hush `#504344` for Dark accent for small headings and emphasis - warmer alternative to the primary text color when a touch of depth is needed
- Obsidian Plum `#2a1a1d` for Primary text, body copy, all headings, nav links - a near-black with warm plum undertone that pairs with the cream canvas at 15.3:1 contrast
- Forest Depths `#1d3023` for Hero section background, dark surface, outlined ghost-button borders - the deep green room that introduces the brand and reappears as a dark contrast panel
- Lime Pulse `#26d862` for Primary action buttons, inline links, accent words inside headlines, active nav states - vivid green used sparingly as functional punctuation, never as decoration
- Peacock Teal `#0e634f` for Stat numbers, data emphasis - a deeper teal that shares hue with the forest hero but reads quieter so it can carry numerical data in stat cards

Use these typography anchors:

- ABC Arizona Flare Condensed Variable `--font-abc-arizona-flare-condensed-variable` for Display and large headings - the condensed serif runs at 180px for the hero statement and steps down through 104, 48, 26, 20px for section headlines. Weight 300 carries the largest sizes, weight 400 takes the mid range. Negative tracking tightens at every size.
- ABC Arizona Flare Variable `--font-abc-arizona-flare-variable` for Body, nav, buttons, cards, captions, and mid-size headings up to 32px. Weight 350 handles 32px headings, weight 400 takes body and UI. The lighter weight at 32px keeps subheadings from competing with the condensed display sizes.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 56-64px.
- Card padding: 16-24px.
- Element gap: 16-24px.

Build these component patterns where relevant:

- Floating Pill Navigation: Primary site navigation, sticky at top center
- Filled Primary Button: Primary call-to-action - form submits, key conversions
- Ghost Outlined Button: Secondary actions, less important links
- Hero Section: Full-viewport opening statement
- Centered Section Statement: Mission/positioning text block in light sections
- Stat Card: 4-column data display strip
- Flower Image Card: Full-bleed photography in content grids
- Section Label: Small uppercase or letter-spaced label above section content
- Inline Green Link: Highlighted text within paragraphs and headlines
- Body Paragraph: Long-form descriptive text
- Menu Toggle: Hamburger/menu open trigger in nav

Do:

- Use the 180px condensed serif only for the hero statement - it's the loudest voice in the system and should appear once per page
- Apply #26d862 (Lime Pulse) filled buttons sparingly - one primary action per viewport, never stack two green buttons side by side
- Set letter-spacing explicitly: -5.4px at 180px, -3.12px at 104px, -0.48px at 32px, scaling proportionally through the type ramp
- Use the surface color difference (#f7f5f2 #eae6df) for card separation instead of box-shadows - the system is intentionally flat
- Let full-bleed flower imagery sit edge-to-edge in 8px-radius cards with no captions - the image is the content
- Anchor any dark moment to the Forest Depths #1d3023 - never use pure black, the warm green undertone is what makes it feel like a room rather than a void
- Pick one weight tier per size: weight 300 for 104-180px display, weight 400 for 20-48px mid-headlines, weight 350 only at 32px subheadings, weight 400 everywhere else

Avoid:

- Don't introduce a new font family - the system runs on exactly two custom serifs (Arizona Flare and Arizona Flare Condensed) and the contrast between them is the signature
- Don't use Lime Pulse #26d862 for body text, borders, or decorative fills - it is exclusively an action and link color
- Don't apply box-shadows to cards or buttons - separation comes from the two-tone cream surface and 8px radius
- Don't mix line-height styles within a size - 0.85 for display (48px+), 1.08 for subheadings (20-32px), 1.18-1.50 for body (12-18px)
- Don't center-align body paragraphs longer than 2 lines - left-align at max-width 720px for readability
- Don't use the Peaacock Teal #0e634f outside of numerical data contexts - it is reserved for stat numbers and data emphasis
- Don't place colored text on the dark Forest Depths hero unless it's Bone Linen #f7f5f2 - the contrast math is tuned for cream-on-forest, not green-on-forest

Source prompt cues:

**Quick Color Reference**
- text: #2a1a1d
- background: #f7f5f2
- card surface: #eae6df
- border: #d7d2cc
- accent/link: #26d862
- primary action: #26d862 (filled action)

**Example Component Prompts**

1. **Dark Hero Section**: Full-bleed background #1d3023. Headline 'UNEARTHING WHAT'S NEXT' in ABC Arizona Flare Condensed Variable weight 300 at 180px, color #f7f5f2, line-height 0.85, letter-spacing -5.4px. Flowing abstract green organic shape behind the text as decoration. Supporting paragraph at 18px, #eae6df, max-width 420px.

2. **Stat Card Grid**: 4 cards in a row on #f7f5f2 canvas. Each card: background #eae6df, 8px radius, 24px padding. Large number in ABC Arizona Flare Condensed weight 400 at 48px, color #0e634f, line-height 0.95. Description below in ABC Arizona Flare at 15px, color #645757, line-height 1.50. Gap between cards: 16px.

3. **Full-Bleed Image Card**: Single card, 1 of 4 in a row. Edge-to-edge image clipped by 8px radius. No padding, no overlay, no caption. Image is a close-up botanical subject (flower, plant). Gap between cards: 16px.

4. **Floating Pill Navigation**: Centered pill at top of page. Background #f7f5f2, 4px radius, 8px vertical padding, 24px horizontal padding. Contains 'Hire' and 'Move' tabs at 15px #1d3023, the wordmark 'Craft' in ABC Arizona Flare Condensed at 20px #2a1a1d centered, and a square menu toggle button with 1px border and 3-dot icon at the right end.

5. **Centered Mission Statement**: On #f7f5f2 canvas, max-width 800px centered. Headline in ABC Arizona Flare Condensed weight 400 at 48px, color #2a1a1d, line-height 0.95, letter-spacing -1.2px. Accent phrases within the headline colored #26d862 (Lime Pulse). Body paragraph below at 16px ABC Arizona Flare, #645757, line-height 1.50. Section label kicker above at 12px uppercase #645757.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
