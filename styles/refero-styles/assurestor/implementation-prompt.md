# AI Implementation Prompt

Build a Assurestor-inspired interface using this source-derived style bundle.

Reference site: https://www.assurestor.com
Theme: dark
Category: SaaS
North star: Electric terminal in a deep forest vault - lime phosphor on midnight olive.

Use these palette anchors:

- Forest Canopy `#203400` for Primary page background, nav strip, footer canvas - the dominant surface that defines the entire brand atmosphere
- Vault Floor `#1b2d00` for Card surfaces, recessed panels, elevated content blocks within the forest canvas
- Canopy Mid `#335400` for Elevated card variant, highlighted surface tier above the base canvas
- Lime Phosphor `#bdff00` for Primary action buttons, active state indicators, illustrative highlight panels, brand-accent moments - the sole chromatic signal in the system
- Moss Border `#586740` for Hairline dividers, list separators, subtle table borders - barely-there green-on-green rules
- Fern `#73a303` for Secondary accent strokes, table emphasis borders, mid-saturation green used sparingly for variety within lime contexts
- White `#ffffff` for Body text, heading text, icon strokes, ghost button borders, link colors, input fields - the only neutral light tone in the palette

Use these typography anchors:

- Denim Ink `--font-denim-ink` for All interface text - from tiny labels to massive display headlines. The custom geometric face is the voice of the brand; weight 400 covers body and body-large, 600 for subheadings and emphasized inline, 700 reserved for the largest display moments. Extreme size jumps (40 64 86 94) create a poster-like hierarchy where the largest text dwarfs everything else on the page.
- Courier New `--font-courier-new` for Tiny monospaced labels (8px) for micro-annotations, likely near icons or status indicators. Ultra-tight tracking (-0.14em) at this size reads as a decorative tech-glitch element rather than readable text.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1280px.
- Section gap: 80px.
- Card padding: 40px.
- Element gap: 24px.

Build these component patterns where relevant:

- Lime Primary Button: High-emphasis action - booking calls, starting contact flows
- Ghost Outline Button: Secondary action - press releases, read-more links, navigation
- Pill Navigation Link: Top-nav items and supplementary action chips
- Featured Lime Panel: Decorative-content block - large visual moment with solid lime fill
- Dark Content Card: Section containers, content blocks, feature cards
- Elevated Accent Card: Highlighted variant for emphasis or hover/active states
- Hairline Divider: Section separator, list rule, table border
- Active Dot Indicator: Status marker beside section labels ("NG Powered by HYCU", "360 Protection")
- Section Eyebrow Label: Small green dot + tiny caption introducing each section
- Headline Block: Hero and section headlines at display scale
- Ghost Input Field: Form inputs, search fields, email capture
- CTA Card / Feature Card with Image: Feature cards combining text and visual

Do:

- Use #bdff00 lime as the ONLY filled action color in the system; never substitute another hue for primary CTAs.
- Set headlines at 64-94px with Denim Ink weight 600-700 and -0.045em tracking - the extreme size and tight tracking is the brand's visual signature.
- Maintain the monochromatic green discipline: layer surfaces using #1b2d00 #203400 #335400, never introduce gray neutrals.
- Use 32px radius for all cards and 16px radius for all buttons; pill shapes (9999px) are reserved for nav items and tag chips.
- Place an 8px lime dot before every section eyebrow label - it is the brand's 'live signal' indicator.
- Keep body text in Denim Ink weight 400 at 16-20px, #ffffff, with line-height 1.5 and -0.02em tracking.
- Allow sections to breathe with 80px vertical gaps and full-width dark bands - density comes from content, not from tight spacing.

Avoid:

- Never use #bdff00 as a large background outside of one featured decorative panel per page - rationing lime is what makes it feel like a signal.
- Do not introduce drop shadows for elevation; the system separates layers through color tier shifts, not shadow depth.
- Do not use gray (#808080, #999, etc.) for any UI element - the palette is green-monochrome plus white and lime only.
- Never set body text below 16px except for the 8px Courier New micro-labels - legibility is non-negotiable.
- Do not mix multiple accent greens (#73a303, #586740) into the same component - one accent per surface keeps the hierarchy clean.
- Do not add gradients - the design relies on flat color blocks for its terminal/phosphor aesthetic.
- Do not use heavy font weights below 32px - Denim Ink at weight 700 in body sizes destroys readability; reserve 700 for display moments only.

Source prompt cues:

Quick Color Reference:
- text: #ffffff
- background: #203400
- card surface: #1b2d00
- elevated card: #335400
- border / hairline: #586740
- accent / decoration: #bdff00
- primary action: #bdff00 (filled action)

3-5 Example Component Prompts:

1. Create a Primary Action Button: #bdff00 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. Create a two-column feature section: dark background (#203400). Left column (60%): lime 8px dot eyebrow + Denim Ink 64px weight 600 headline in #ffffff, letter-spacing -0.045em, followed by 16px body text in #ffffff at line-height 1.5. Lime filled button below (18px 32px padding, 16px radius). Right column (40%): a large solid-lime (#bdff00) panel with 32px radius and 40px padding, containing a white geometric illustration centered inside.

3. Create a dark content card: background #1b2d00, 32px radius, 40px padding. Title in Denim Ink 32px weight 600, #ffffff, letter-spacing -0.022em. Body in Denim Ink 16px weight 400, #ffffff, line-height 1.5. No shadow, no border - the card floats on the forest canvas purely through color shift.

4. Create a ghost outline button: 1px solid #ffffff border, transparent background, Denim Ink 16px weight 400 in #ffffff, 16px border-radius, 18px 32px padding, line-height 1. Pair it next to a filled lime button with identical sizing but #bdff00 background and #1b2d00 text.

5. Create a section eyebrow label: an 8px #bdff00 dot positioned inline-block, followed by a Denim Ink 16px caption in #ffffff with -0.02em tracking. Vertically centered. Used as the identifier marker above every major section headline.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
