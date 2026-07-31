# AI Implementation Prompt

Build a Watch new Originals-inspired interface using this source-derived style bundle.

Reference site: https://www.disneyplus.com
Theme: dark
Category: Media
North star: Cinematic void with electric spotlight. Picture a darkened theater lobby where a single cyan marquee light is the only chromatic thing in sight - everything else is monochrome depth leading the eye to the posters on the wall.

Use these palette anchors:

- Midnight Canvas `#040714` for Page background, hero background, primary canvas - deep near-black navy that absorbs the eye and makes artwork pop
- Abyss `#010104` for Deepest surface layer, navigation background - the near-pure black undercarriage beneath the canvas
- Eclipse `#0e0b14` for Footer background, alternate dark surface - slightly warmer dark for depth variation
- Carbon `#1e1f24` for Elevated dark surface - used for cards or panels sitting above the canvas
- Slate Veil `#282a36` for Neutral form states, badge text, and quiet UI feedback where color should stay understated. Do not promote it to the primary CTA color
- Luminous `#fafafa` for Primary text, heading text, icon fills, link text, button labels - the dominant light element across the interface
- Pearl `#e5e7eb` for Border color used at scale (hairs, dividers, card edges) - the structural skeleton of the UI
- Mist `#b7b8bd` for Body text, secondary text, helper copy - muted gray for non-primary reading
- Fog `#c0c0c0` for List text, icon fills, secondary metadata - the lightest level of secondary text
- Deep Ink `#02172a` for Gray text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color
- Onyx Label `#17171c` for Dark text for inverted or high-contrast button labels on light fills
- Electric Cyan `#33ddff` for Primary CTA buttons (SIGN UP NOW, plan tier cards) - the sole chromatic action color; neon-cyan against the void creates cinema-marquee urgency
- Teal Pulse `#02d6e8` for Accent text, promotional price highlights ( 4.99), link emphasis, body emphasis - the slightly darker teal sibling used for inline chromatic moments that aren't buttons

Use these typography anchors:

- Inspire `--font-inspire` for Sole typeface across the entire interface - headings, body, buttons, labels, nav. The single-font commitment is deliberate: it means Inspire must carry both 12px micro-labels and 40px display moments without losing character. Use 700 for headings, price, and emphasis; 400 for everything else.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 48-64px.
- Card padding: 16px.
- Element gap: 8px.

Build these component patterns where relevant:

- Cyan CTA Button: Primary conversion action - sign up, subscribe, plan selection
- Plan Tier Card: Subscription option display (Standard with Ads, Standard, Premium)
- Email Input Field: Newsletter / sign-up email capture
- Content Tile Card: Movie/series poster card in carousels and grids
- Top 10 Ranked Card: Hero content ranking with large numeral overlay
- Feature Comparison Row: Plan comparison table - concurrent streams, Dolby Atmos, ads, etc.
- Section Heading: Content section title (e.g., 'Top 10 Today', 'Choose your plan', 'Watch the way you want')
- Top Navigation Bar: Primary site navigation
- Hero Pricing Banner: Central conversion offer overlay on poster-grid background
- Ghost Outline Button: Secondary action - 'View all plans', 'Learn more'
- Footer: Legal links, fine print, bottom-of-page content
- Promotional Price Highlight: Strikethrough or savings callout in pricing contexts

Do:

- Use #33ddff (Electric Cyan) exclusively for filled CTA buttons and active plan tier cards - no other fills should carry this color
- Keep all text on the dark canvas in #fafafa for primary, #b7b8bd for secondary, #c0c0c0 for tertiary - never use a chromatic color for body text
- Use Teal Pulse (#02d6e8) for inline emphasis, savings callouts, and informational highlights - not for buttons
- Apply Inspire at all sizes with the same 0.025em letter-spacing - do not tighten tracking on display sizes
- Use 12px border-radius for all buttons and content cards; 8px for inputs and nav elements
- Let poster artwork occupy the full card area - never wrap posters in visible card frames, borders, or shadows
- Center-align section headings and let generous 48-64px vertical space create the cadence between content rails

Avoid:

- Do not introduce additional accent colors - the system is monochrome with one cyan and one teal; any other chromatic is off-system
- Do not apply box-shadows to cards, buttons, or content tiles - the design uses flat color and borders for structure, not elevation
- Do not use cyan (#33ddff) for non-action text, icons, or decorative elements - reserve it strictly for filled buttons
- Do not override the positive letter-spacing on large headings - 0.025em at 40px produces 1px tracking, which is the intended whisper-not-shout scale
- Do not place light text on cyan fills without testing contrast - use #02172a (Deep Ink) for dark text on cyan, not #17171c or pure black
- Do not add background fills to content poster cards - the artwork is the card; adding a frame reduces the cinematic effect
- Do not use a secondary typeface for display or hero moments - Inspire carries the full type scale, from 12px captions to 40px headings

Source prompt cues:

**Quick Color Reference**
- text (primary): #fafafa
- text (secondary): #b7b8bd
- background (canvas): #040714
- border / hairline: #e5e7eb
- accent (informational emphasis): #02d6e8
- primary action: #33ddff (filled action)

**Example Component Prompts**

1. Create a Primary Action Button: #33ddff background, #17171c text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. **Plan Tier Card**: Full-width card with fill #33ddff, border-radius 12px, padding 24px. Plan name in Inspire 700 at 18px, color #02172a. Price in Inspire 700 at 20px, color #02172a. Savings line in #02d6e8, Inspire 400, 14px.

3. **Content Poster Tile**: No background, no border, no shadow. Poster artwork fills a 2:3 portrait frame with border-radius 12px. Rank numeral overlaid top-left in Inspire 700, 40px, color #33ddff. Title below in Inspire 700, 14px, #fafafa. Genre/year in Inspire 400, 12px, #b7b8bd.


5. **Section Heading + Subheading**: Inspire 700, 28px, #fafafa, letter-spacing 0.7px, center-aligned. Subheading below: Inspire 400, 18px, #b7b8bd, center-aligned. 64px space above heading, 24px gap to content below.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
