# AI Implementation Prompt

Build a Customer.io-inspired interface using this source-derived style bundle.

Reference site: https://customer.io
Theme: mixed
Category: SaaS
North star: dark spruce forest meeting cream paper

Use these palette anchors:

- Spruce Abyss `#00191c` for Deepest background - footer canvas, dramatic section breaks
- Spruce 900 `#032125` for Primary dark surface - headers, hero, main navigation background; dominant text color on light surfaces
- Spruce 700 `#0b363b` for Primary CTA fill on dark backgrounds, elevated card surfaces, border accent
- Spruce 500 `#437278` for Muted teal accent - illustration fills, secondary icon color
- Spruce 200 `#a1c2c6` for Decorative stroke, muted link text, icon outlines on dark surfaces
- Spruce Mist `#354d51` for Body text on light surfaces, secondary heading color
- Charcoal 100 `#ebebeb` for Hairline borders, dividers, subtle separators across the interface
- Charcoal Mist `#fafafa` for Alternate section background, subtle card backgrounds
- Cream Warm `#fffcf6` for Primary light surface - content sections, card backgrounds
- Pure White `#ffffff` for Elevated card surface, button text on dark fills, content blocks
- Verdant 300 `#abffae` for Interactive glow - CTA button fill, focus ring halo, active state border; vivid green signals action without aggression
- Verdant Whisper `#eafde8` for Primary page canvas and white card surfaces. Use as a supporting accent, not as a status color
- Wave 700 `#123a88` for Violet text accent for links, tags, and emphasized short phrases.
- Wave 500 `#0a6de6` for Heading accent color for keyword highlights in display text
- Wave Frost `#e2f4ff` for Hairline borders, dividers, input outlines, and card edges on light surfaces. Use as a supporting accent, not as a status color
- Zest 700 `#863d1c` for Orange text accent for links, tags, and emphasized short phrases.
- Zest Blush `#fdf0e9` for Hairline borders, dividers, input outlines, and card edges on light surfaces. Use as a supporting accent, not as a status color
- Mustard 700 `#83611c` for Yellow text accent for links, tags, and emphasized short phrases.

Use these typography anchors:

- Saans `--font-saans` for Custom display + body typeface used for everything. Weight 475 dominates - a near-medium voice that feels calm and confident rather than aggressive.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 96px.
- Card padding: 32px.
- Element gap: 24px.

Build these component patterns where relevant:

- Primary Pill Button: Main CTA - 'Get started'
- Secondary Outline Button: Secondary CTA - 'Book a demo'
- Ghost Navigation Button: Nav item with dropdown
- Small Tag Button: 'New' badge, 'case study' link
- Content Card: Feature card, platform overview tile
- Dark Section Card: Card on dark spruce background
- Tinted Feature Surface: Section background with soft color wash
- Footer Column: Footer link column
- Logo Strip Card: Customer logo in trust strip
- Heading with Keyword Accent: Display headline with colored words
- Trust Indicator Row: Social proof list - '14-day free trial'
- Interactive Product Preview: Hero product screenshot

Do:

- Use 2px border-radius on all cards, inputs, images, and containers - pill shapes (9999px) are reserved exclusively for buttons
- Use weight 475 for all text including 96px display headlines - never bold above 600 except for 20px subheadings
- Use 1px solid #ebebeb hairline borders for card edges and dividers - never thicker
- Color individual words in display headlines using #863d1c (orange), #123a88 (blue), #41a251 (green), #b52473 (pink) - words stay inline, never separate blocks
- Use #abffae exclusively for primary CTA fills and focus glow rings - never as body text or background tint
- Use 24px for element gaps, 32px for card padding, 96px for section vertical gaps - the 4px base unit scales through these three tiers
- Use #fffcf6 as the default light surface; alternate to #032125 for dark sections; tint with #e2f4ff, #fdf0e9, or #eafde8 for semantic accent bands
- Use 4px colored focus glow rings (0px 0px 0px 4px) for interactive focus states instead of outline or shadow changes

Avoid:

- Never use drop shadows for elevation - depth comes from colored 4px glow rings only
- Never use bold weights above 600 for display or heading text - the signature is the calm 475 voice
- Never use corner radius above 2px on non-button elements - sharp-cornered cards define this system
- Never use #0000ee or default browser blue for links - links use #032125 or #a1c2c6
- Never place #abffae on white or light backgrounds without sufficient contrast - it is a glow color, not a fill
- Never use more than 4 columns in content grids - the system favors generous spacing over density
- Never use the heading accent colors (#863d1c, #123a88, etc.) for UI chrome - they exist only for inline keyword coloring in display text

Source prompt cues:

**Quick Color Reference**
- text (primary): #032125
- text (secondary): #354d51
- text (muted/link): #a1c2c6
- background (light): #fffcf6
- background (dark): #032125
- border (hairline): #ebebeb
- accent (highlight keywords in headings): #863d1c
- primary action: #0b363b (filled action)

**Example Component Prompts**

1. **Hero headline**: Render at 96px Saans weight 475, line-height 1.0, color #032125, letter-spacing 0.0020em. Use the word 'messaging' in #863d1c and 'AI' in #123a88 as inline accent colors within the same line.

2. Create a Primary Action Button: #0b363b background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

3. **Dark section card**: Background #0b363b, 32px padding all sides, 2px corner radius, 1px #0b363b border, body text #a1c2c6 at 16px weight 475, heading in white at 24px weight 475.

4. **Trust indicator row**: Three inline items at 14px weight 475 in #032125, each preceded by a small #abffae checkmark icon, separated by 24px gap, no dividers.

5. **Tinted feature section**: Full-bleed #e2f4ff background, 96px vertical padding, centered 1200px content container, heading at 40px weight 475 in #032125, 3-column grid of feature items below with 2px-radius white cards inside.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
