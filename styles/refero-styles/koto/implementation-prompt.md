# AI Implementation Prompt

Build a Koto-inspired interface using this source-derived style bundle.

Reference site: https://koto.com
Theme: dark
Category: Agency
North star: Obsidian gallery at midnight. A near-black stage where a single yellow mark is the only warm light, and condensed type floats in vast negative space like exhibition placards.

Use these palette anchors:

- Void Black `#060606` for Primary page canvas - the dominant background where all content floats; not pure black, but a warmthless near-black that keeps contrast at AAA
- Graphite Surface `#141414` for Elevated card and icon backgrounds - one step lighter than canvas, used to subtly separate surfaces without breaking the dark mood
- Smoke Border `#202020` for Hairline borders and dividers - barely visible structural lines that define regions without adding visual weight
- Iron Mute `#595959` for Muted text and secondary borders - body text at reduced emphasis, footer meta, tertiary labels
- Ash Gray `#989898` for Secondary body text and medium-emphasis borders - the most-used neutral after white, for body copy and structural outlines
- Silver Whisper `#b4b4b4` for Light body text - softer than white for inline body content where pure white would feel too sharp
- Paper White `#ffffff` for Primary text, heading strokes, and all key borders - the brightest mark in the system, reserved for content that must read first
- Signal Yellow `#ffe800` for Yellow decorative accent for icons, marks, and small graphic details.

Use these typography anchors:

- gtKotoheim `--font-gtkotoheim` for All UI, body, navigation, button, and small-display text. Custom monospace-feeling sans with 'salt' alternate glyphs - weight 350 is the default body, 400 for slightly stronger emphasis. The only typeface for everything below display size.
- gtKotoheimCondensed `--font-gtkotoheimcondensed` for Display headings only. Condensed cut at weight 300 with tight 1.0-1.1 leading and -0.01em tracking - these headlines whisper rather than shout, letting the vast negative space amplify their presence. Reserved for hero statements and section titles.

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: 1200px.
- Section gap: 48px.
- Card padding: 36px.
- Element gap: 8px.

Build these component patterns where relevant:

- Top Navigation Bar: Primary site navigation
- Koto Logo Mark: Brand identity in nav
- Navigation Link: Section navigation items
- UTC Time Indicator: Live timezone display in nav
- Hero Headline Statement: Opening typographic declaration
- Body Text Block: Paragraph content
- Dark Surface Card: Content container for images or grouped content
- Outlined Action Border: Interactive border treatment
- Footer City List: Office locations meta
- Active Nav Dot: Current page indicator

Do:

- Set page background to #060606 (Void Black); never use pure #000000
- Use gtKotoheimCondensed weight 300 at 38-48px only for display headlines; pair with -0.48px letter-spacing at 48px
- Use gtKotoheim at 12-16px for all UI, body, and navigation text with the 'salt' font-feature enabled
- Reserve #ffe800 (Signal Yellow) exclusively for the logo mark; it must not appear in any UI component, button, or text
- Communicate elevation through lightness shifts (canvas #141414 cards), not through shadows or borders
- Keep element gaps at 8px and section gaps at 48px; the rhythm comes from these fixed multiples of the 4px base unit
- Left-align all text and let negative space carry the layout - never center body copy or add decorative dividers

Avoid:

- Don't introduce any color outside the neutral scale and Signal Yellow; the system is 0% colorful by design
- Don't use filled buttons or colored CTAs; interactive elements are ghost/outlined with #ffffff borders on transparent fills
- Don't apply shadows, gradients, or blur effects to any element - the flat void treatment is non-negotiable
- Don't use radius values other than 2px, 6px, or 10px; mixing radii breaks the geometric discipline
- Don't set body copy in gtKotoheimCondensed or display in gtKotoheim regular; the two families are strictly separated by size and role
- Don't use pure #ffffff for body text - reserve it for headings, borders, and the UTC indicator; body copy uses #b4b4b4
- Don't add icons, illustrations, or imagery to the base layout; the page is typographic-first and visual assets should only appear inside Dark Surface Cards

Source prompt cues:

primary action: no distinct CTA color

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
