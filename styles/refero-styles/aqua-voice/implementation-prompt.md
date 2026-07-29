# AI Implementation Prompt

Build a Aqua Voice-inspired interface using this source-derived style bundle.

Reference site: https://withaqua.com
Theme: light
Category: SaaS
North star: Whisper on paper - ultra-light type resting on near-white with a single blue drop of color

Use these palette anchors:

- Sky Signal `#67beff` for Blue action color for filled buttons, selected navigation states, and focused conversion moments
- Electric Iris `#4288ff` for Outlined/ghost action border, inline link accent, focus rings - cooler and slightly deeper than Sky Signal
- Paper White `#fafbfc` for Page canvas, primary surface, inverted text on dark bars
- Mist `#f3f7fa` for Subtle band backgrounds, section alternation, elevated surface tint
- Fog `#f2f6fa` for Card surface, soft fill behind product screenshots
- Linen `#e5e8ec` for Hairline dividers, faint borders, disabled surfaces
- Ash `#efefef` for Ghost button background, subtle hover fill
- Inkstone `#292c3d` for Primary text, strongest contrast - carries the 200-weight headlines
- Slate `#3e4150` for Body text, secondary headings, dense body copy
- Pewter `#686a76` for Muted body text, helper text, inactive nav
- Graphite `#7d7e7e` for Tertiary text, footer links, faint labels
- Silver `#c2c3c8` for Placeholder text, very faint borders, decorative strokes
- Obsidian `#171719` for Top announcement bar background, dark surface, inverted text fill
- Midnight `#1e1e20` for Dark card surface, secondary dark fill

Use these typography anchors:

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- PP Neue Montreal `--font-pp-neue-montreal` for Primary typeface - weight 200 for display and headlines (anti-convention; most sites use 600-700, this whisper-weight gains authority through restraint), weight 400 for body and subheadings. Custom Pangram Pangram face with Polish alternates and character variants.
- PP Neue Montreal `--font-pp-neue-montreal` for Medium cut for UI controls, buttons, nav links, and small labels where the Book weight feels too quiet to anchor interaction
- Inter `--font-inter` for System-level fallback and small UI text - nav micro-labels, metadata, the smallest body sizes
- Geist Mono `--font-geist-mono` for Monospaced face for keyboard hints (the Hold/Space key chips), code, and technical micro-labels
- IBM Plex Mono `--font-ibm-plex-mono` for IBM Plex Mono - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1200px.
- Section gap: 80-120px.
- Card padding: 20-24px.
- Element gap: 10px.

Build these component patterns where relevant:

- Announcement Bar: Top utility strip
- Primary Navigation: Top site nav
- Filled CTA Button: Primary action
- Ghost Button: Secondary action
- Hero Headline: Primary page headline
- Key Hint Chip: Keyboard indicator
- Product Screenshot Card: Feature demonstration
- Inline Link: Text link accent
- Status Dot: Live indicator
- Feature Section: Content section
- Subtle Background Pattern: Decorative atmosphere

Do:

- Use weight 200 for all display and headline text in PP Neue Montreal - the ultra-light cut is the brand's visual signature.
- Use Sky Signal (#67beff) only for the filled primary CTA and the live-status dot; never extend it to backgrounds, illustrations, or decorative fills.
- Set headline line-height to 1.00-1.10 - the tight leading is essential to the whisper aesthetic and prevents the light weight from looking fragile.
- Keep card padding in the 20-24px range and radii at 12-20px; tighter and it feels cramped, wider and it competes with the generous page-level spacing.
- Use Ghost buttons (transparent + Slate text) for all secondary actions; reserve the filled Sky Signal button exclusively for the single primary action on each screen.
- Apply the hairline Linen (#e5e8ec) border pattern with rgba(0,0,0,0.02) shadow for elevated surfaces - the system uses depth in millimeters, not millimeters turned into centimeters.
- Center text blocks at max-width 680px for readability; let the surrounding negative space carry the page rhythm.

Avoid:

- Do not use weights above 500 for PP Neue Montreal - the Medium 500 is already the upper bound; 600+ destroys the whisper character of the system.
- Do not add color to body copy, headings, or backgrounds beyond the Inkstone/Slate/Pewter neutral scale - chromatic text breaks the monochrome contract.
- Do not apply large or saturated shadows; the system intentionally operates at rgba(0,0,0,0.02) to rgba(0,0,0,0.1) depth only.
- Do not use pill shapes (9999px radius) for primary buttons - 8px is the button radius; pill shapes are reserved for tags and status chips.
- Do not introduce gradients, glassmorphism, or heavy blur effects - the design language is flat, matte, and paper-like.
- Do not set headline letter-spacing to negative values - PP Neue Montreal is already optically balanced; additional tracking adjustment creates inconsistency with the font's native rhythm.
- Do not use Electric Iris (#4288ff) as a fill - it is an outline/link/ghost action color only; Sky Signal owns the filled action role.

Source prompt cues:

**Quick Color Reference**
- text: #292c3d (Inkstone) for headlines, #3e4150 (Slate) for body
- background: #fafbfc (Paper White) canvas, #f3f7fa (Mist) section bands
- border: #e5e8ec (Linen) hairline
- accent: #67beff (Sky Signal) - filled CTA only
- link/outline action: #4288ff (Electric Iris) - borders, ghost actions, inline links
- primary action: #67beff (filled action)

**Example Component Prompts**

1. *Hero Headline Block*: 1200px max-width container, left-aligned text at 680px width. Headline: 56px PP Neue Montreal weight 200, color #292c3d, line-height 1.10. Subtext: 16px PP Neue Montreal weight 400, color #3e4150, line-height 1.50. 80px vertical padding above and below.

2. *Filled Download CTA*: Sky Signal (#67beff) background, 8px border-radius, padding 10px 16px. Text: 14px PP Neue Montreal Medium 500, color white. No border, no shadow. Centered or right-aligned in nav bar.

3. *Ghost Secondary Button*: Transparent background, 8px border-radius, padding 10px 16px. Text: 14px PP Neue Montreal Medium 500, color #3e4150. Hover state: #efefef background fill. No border in default state.

4. *Product Screenshot Card*: Mist (#f2f6fa) or Fog (#f2f6fa) background, 20px border-radius, 1px Linen (#e5e8ec) border, padding 24px. Contains a product UI screenshot with 12px inner radius. Apply rgba(0,0,0,0.02) layered shadow stack.

5. *Key Hint Chip*: White background, 1px #e5e8ec border, 4px border-radius, padding 4px 10px. Text: 13px Geist Mono weight 500, color #3e4150. Used inline within instructional sentences to denote keyboard keys.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
