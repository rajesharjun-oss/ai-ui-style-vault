# AI Implementation Prompt

Build a Handsome Frank-inspired interface using this source-derived style bundle.

Reference site: https://www.handsomefrank.com
Theme: light
Category: Agency
North star: Curator's atelier with living murals - a warm-paper gallery where illustrated worlds bloom against indigo frames.

Use these palette anchors:

- Indigo Frame `#160572` for Navigation strokes, display headlines, footer band - the deepest anchor in the system, commanding authority without shouting
- Cream Paper `#f2ebe6` for Primary page canvas for content sections - warm eggshell that softens black text and lets illustration breathe
- Pure White `#ffffff` for Card surfaces, reversed text on dark bands, and the clean counterpoint to cream - the gallery wall
- Obsidian Hairline `#000000` for Dominant border, text, and icon stroke - used as a 1-2px frame line across nav, cards, and decorative elements
- Slate Ink `#2c2c2c` for Secondary text and softer borders where pure black feels too severe
- Fog Wash `#eef4fb` for Pale blue-tinted background for muted emphasis blocks
- Buttermilk `#fef9ee` for Subtle warm wash for highlighted text or callout backgrounds
- Crimson Spotlight `#ea0706` for Editorial accent for critical announcements and bold display statements - the marquee marker
- Vermillion `#d64e2e` for Warm secondary accent on project card titles, links, and illustrative borders
- Apricot Whisper `#e29675` for Soft warm accent for icon strokes and decorative borders
- Peach Blush `#eea883` for Mid-warmth accent on icon outlines and link underlines
- Tangerine Pop `#ff7701` for Filled action button background - the only true filled CTA, used for the play/forward action in the footer
- Cobalt Stage `#2544a0` for Filled action button background for primary browse/enter actions
- Plum Velvet `#4b0f4d` for Filled action button background for dark editorial CTAs
- Rose Petal `#d98199` for Filled action button background for soft secondary entries
- Electric Teal `#24e3dc` for Interactive link and menu accent - the only cool chromatic in the system, reserved for navigation affordances
- Acid Green `#24e34c` for Secondary interactive link accent for hover/active states
- Daffodil `#f9e44d` for Decorative icon and link accent - cheerful punctuation
- Highlighter Yellow `#ffff00` for Badge background for editorial tags and callout labels

Use these typography anchors:

- Arial `--font-arial` for Arial - detected in extracted data but not described by AI
- Millik `--font-millik` for Display serif for hero headlines, artist names, and editorial display copy. The extreme negative letter-spacing (-0.05em at 88px down to -0.018em at 20px) and tight line-height (0.95-1.00 at large sizes) is the signature: the type sits dense and confident, not airy. Use weight 400 for editorial body, 700 for display headlines.
- Klarheit Grotesk `--font-klarheit-grotesk` for Workhorse grotesque for navigation, body text, buttons, badges, and supporting labels. Regular (400) is the default; Semibold (600) appears at 22px for subheadings; Bold (700) at 24px for nav emphasis. The grotesque is intentionally quiet - it holds the structure while the serif does the talking.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 64-80px.
- Card padding: 20-24px.
- Element gap: 20px.

Build these component patterns where relevant:

- Full-Bleed Illustrated Hero: Opening visual statement
- Hero Display Headline: Primary value statement
- Script Wordmark: Brand identity
- Circular Menu Trigger: Primary navigation opener
- Editorial Section Headline: Section opener on cream canvas
- Artist Portfolio Card: Artist thumbnail in browse grid
- Featured Project Card: Editorial project highlight
- Pill Button (Filled): Primary or secondary action
- Outlined Link: Inline editorial link
- Highlighter Badge: Editorial tag or label
- Announcement Banner: Breaking news or signing announcement
- Indigo Footer Band: Closing call-to-action bar

Do:

- Use Millik serif for all display headlines and editorial titles; let it carry the personality with negative letter-spacing and tight line-height (0.95-1.10)
- Reserve #160572 indigo for navigation strokes, editorial headlines, and the closing footer band - it is the thread that stitches the page together
- Use the full pill shape (30px radius) for all filled action buttons, and pick from the four chromatic button backgrounds (#2544a0, #ff7701, #4b0f4d, #d98199) by context
- Apply 1-2px solid #000000 hairlines as decorative frames around cards, nav elements, and illustration containers - the gallery-frame motif
- Let illustrated or photographic content fill its container edge-to-edge with no border or radius - the artwork defines its own boundary
- Use #ffff00 as a flat badge/tag background with black text for editorial callouts - treat it like a highlighter pen mark
- Keep body text at 16px Klarheit Grotesk Regular with line-height 1.36 on the cream (#f2ebe6) canvas - the warmth softens the otherwise stark black/white system

Avoid:

- Don't use neutral grays for primary buttons - the system has no gray CTA; buttons are always chromatic and pill-shaped
- Don't apply border-radius to project cards, illustration thumbnails, or content cards - only pill buttons get curves (30px), everything else stays sharp-edged
- Don't use the chromatic accent colors (teal, green, red, yellow, orange) for body text or large text blocks - they are reserved for links, icons, badges, and decorative strokes only
- Don't drop shadows on cards or images - the design uses hairline borders and flat color blocks for separation, never elevation
- Don't set body text below 14px or use letter-spacing looser than normal on small sizes - the system relies on compact, confident type
- Don't use gradient backgrounds or colored overlays on imagery - illustrations and photos display raw, edge-to-edge, on their own colors
- Don't center-align body paragraphs or nav items - the layout is left-aligned for text blocks and centered only for display headlines and footer CTAs

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
