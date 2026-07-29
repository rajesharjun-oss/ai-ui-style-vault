# AI Implementation Prompt

Build a ALSO-inspired interface using this source-derived style bundle.

Reference site: https://ridealso.com
Theme: light
Category: E-commerce
North star: Bicycle zine on cream paper

Use these palette anchors:

- Cream Paper `#fcf7fa` for Page canvas, soft section background - warm off-white with a barely-there pink cast, never pure white
- Pure Card `#ffffff` for Card surfaces, elevated panels, button text on violet fills
- Ash Mist `#f1f1f1` for Tertiary surface, muted dividers, subtle background washes
- Carbon Black `#000000` for Primary text, default borders, icon strokes - the structural ink of the system
- Graphite Input `#212121` for Input field borders, secondary dark surfaces
- Obsidian Pill `#1a1a1a` for Dark CTA fill - the secondary action button (e.g. Reserve), pairs with white text and violet shadow
- Electric Violet `#ac74fc` for Primary accent - link borders, active states, icon highlights, section accent borders. The brand's signal color
- Lilac Pill `#c181ff` for Primary CTA button fill - the dominant call-to-action, sits on violet hard shadow with black text
- Deep Plum `#381b5e` for Dark violet text variant, deep accent borders, section-level emphasis when Electric Violet feels too bright
- Shadow Plum `#48316a` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Acid Lime `#b1ff8f` for Sparingly used highlight wash or accent surface for urgency moments (limited drops, reservation states)
- Signal Blue `#1276a9` for Outlined action border - secondary ghost button or informational outline accent

Use these typography anchors:

- ABCCameraPlainVariable `--font-abccameraplainvariable` for Primary UI and display typeface - handles body, headings, navigation, and product copy
- SerialC-Heavy `--font-serialc-heavy` for Uppercase eyebrows, button text, section labels, mono-influenced captions
- SerialC `--font-serialc` for SerialC - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 16px.

Build these component patterns where relevant:

- Primary CTA Button (Lilac Pill): The dominant call-to-action - "LEARN MORE", "EXPLORE", primary product actions
- Dark CTA Button (Obsidian Pill): Secondary high-emphasis action - "RESERVE NOW" top banner button
- Green CTA Button (Acid Lime): Scarce/limited state CTA - reservation confirmations, low-stock urgency
- Ghost Navigation Link: Top-bar nav items (BIKE, QUAD, HELMET, GEAR, COMPANY)
- Section Eyebrow Label: Uppercase section markers - "WHEN YOU RIDE ON ALSO, YOU SEE, FEEL, AND NOTICE THINGS"
- Product Card (Hero Showcase): Large illustrated/photographic product cards in the grid - bikes, quads, helmets, riders
- Feature Card (Three-Column Grid): Editorial cards in the "SEE, FEEL, NOTICE" section - TM-B, Alpha Wave, Our Company
- Story Card (Purple Section): Editorial story cards in the Stories carousel - "Join ALSO at the Sea Otter Classic 2026"
- Pagination Control: Carousel navigation - "01/03" counter with prev/next circle buttons
- Input Field: Form inputs (email, address, reservation details)
- Top Announcement Bar: Site-wide reservation banner - "RESERVE NOW TO RIDE SOONER"
- Logo Wordmark: Brand mark - "ALSO." with period

Do:

- Set all buttons and tags to 9999px radius - the pill is non-negotiable across every variant (primary, dark, green, ghost).
- Use the single Shadow Plum (#48316a) 2px solid hard shadow on every elevated element - never use blur, never stack shadows, never change the offset.
- Use Electric Violet (#ac74fc) for links, active states, icon highlights, and section borders - it is the signal color and should appear in functional roles, not decoration.
- Set SerialC-Heavy labels in uppercase with positive tracking (0.036-0.063em) - never use it in mixed case or tight tracking.
- Push ABCCameraPlainVariable line-heights tighter as size grows: 1.5 at body, 1.0 at heading-lg, 0.93 at display - the system is defined by compression at scale.
- Maintain 8px base unit spacing: 16px element gap, 24px card padding, 80px section gap - never break to a 4px or 12px base.
- When a section flips to Electric Violet (#ac74fc) background, keep the same component structure, shadows, and type system - only the canvas color changes.

Avoid:

- Never use soft drop shadows with blur - the 2px solid hard shadow is the only shadow in the system.
- Never use Pure White (#ffffff) as page canvas - always start from Cream Paper (#fcf7fa); white is reserved for cards and elevated surfaces.
- Never set ABCCameraPlainVariable with positive letter-spacing on body or heading text - the system compresses at scale, it does not expand.
- Never use rounded corners on product images, story cards, or hero photography - these are sharp-edged; only buttons, inputs, and feature cards get radius.
- Never add a second chromatic accent - Electric Violet is the system; Acid Lime and Signal Blue are rare utility colors for specific states only.
- Never use a different shadow color - Shadow Plum (#48316a) stays constant even on dark or green buttons, keeping the brand cohesive across all CTA variants.
- Never set SerialC-Heavy in lowercase or sentence case - it is an uppercase-only typeface in this system; using it otherwise breaks the typographic rhythm.

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #fcf7fa
- card surface: #ffffff
- border: #000000
- accent / brand signal: #ac74fc
- primary action: #c181ff (filled action)

**Example Component Prompts**

1. *Hero centered headline section*: Cream Paper (#fcf7fa) background. Headline "One machine for every being." at 60px ABCCameraPlainVariable weight 400, color #000000, line-height 0.93, letter-spacing 3px. Single Lilac Pill CTA below at 20px 40px padding, #c181ff fill, #000000 text in SerialC-Heavy 900 uppercase 14px with 0.05em tracking, 9999px radius, 2px solid #48316a hard shadow.

2. *Product card with rider cutout*: No card chrome. Full-bleed photographic cutout of a rider on a bike, sharp corners, sitting directly on the #fcf7fa canvas. Small counter "1,043" in SerialC-Heavy 14px black at top-left of the card. Card width ~320px, no border, no shadow, no padding.

3. Create a Primary Action Button: #c181ff background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

4. *Story card on violet section*: Full Electric Violet (#ac74fc) background as the card itself. Title "Join ALSO at the Sea Otter Classic 2026." at top-left in ABCCameraPlainVariable 20px black. Date "04-08-2026" below in SerialC-Heavy 14px uppercase with 0.063em tracking. Landscape photograph fills the bottom half of the card, sharp corners, no rounding.

5. *Section eyebrow label*: SerialC-Heavy 400 uppercase at 14px, tracking 0.063em, color #000000, centered above the section content with 40px bottom margin. The marker that signals a new section is beginning.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
