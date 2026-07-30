# AI Implementation Prompt

Build a Titan-inspired interface using this source-derived style bundle.

Reference site: https://www.titan.com
Theme: light
Category: Fintech
North star: warm-toned monochrome archive

Use these palette anchors:

- Ink `#111111` for Primary text, filled button background, icon strokes - near-black ink that carries the entire brand identity. The slight softness vs pure #000 keeps it from feeling sterile
- Pure White `#ffffff` for Page canvas, card surfaces, button text - the dominant light field the entire interface sits on
- Mist Border `#e9eaeb` for Primary hairline borders, nav pill background, structural dividers - cool gray that defines edges and containers without competing with content
- Cream Surface `#f3efeb` for Warm card and section surfaces - the warm signature tone that gives the system its editorial, paper-like quality against the cool white canvas
- Tan Divider `#d8d3cc` for Secondary borders on warm surfaces, subtle background washes - extends the cream warmth into the border layer
- Warm Subtle `#615e5b` for Muted helper text, secondary copy - warm gray that recedes on cream surfaces while staying readable on white
- Mid Gray `#888888` for Tertiary text and disabled states - only when even Warm Subtle is too prominent
- Pure Black `#000000` for Rare SVG fills and graphic accents - used sparingly where absolute black is required
- Obsidian `#1e1e1d` for Footer background, dark section inversions - the only dark surface in the system, creating a terminal moment at page bottom

Use these typography anchors:

- Geist `--font-geist` for Primary interface and headline typeface - used at weight 500 (not 700) for all headings, a deliberate restraint that gives headlines editorial weight without shouting. Variable substitute: Inter.
- Geist Mono `--font-geist-mono` for Numerical stats, metadata, small labels - reserved for figures like $1.2B, 10,000+, 2017 where monospaced digits create an editorial financial-journalism quality. Variable substitute: JetBrains Mono.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1280px.
- Section gap: 80-120px.
- Card padding: 56px.
- Element gap: 16-24px.

Build these component patterns where relevant:

- Filled Pill Button (Primary): Primary call-to-action across the site
- Outline Pill Button (Secondary): Secondary actions, less prominent CTAs
- Inverse Pill Button: Actions on dark backgrounds
- Circular Icon Button: Compact icon-only controls
- Cream Editorial Card: Content blocks that need warmth and breathing room
- Borderless Feature Card: Inline content blocks without surface weight
- Stat Block: Displaying numerical proof points ($1.2B, 10,000+, 2017)
- Feature Item with Icon: Feature lists with small circular icon + text
- Navigation Bar: Top-level site navigation
- Hero Split Layout: Above-the-fold page entry
- Dark Footer: Site-wide footer with links and legal

Do:

- Use pill buttons with 160px border-radius for all primary actions - never square or slightly-rounded buttons
- Set all headlines to weight 500 in Geist with -0.03em tracking at 32px+; reserve weight 400 for body copy
- Use Geist Mono 48px weight 500 for all large numerical stats - the mono typeface for financial figures is signature
- Pair cream #f3efeb card surfaces with the white canvas to create depth; never add box-shadow for elevation
- Keep the interface fully monochrome - do not introduce accent colors, the absence of color IS the brand identity
- Use 1px solid #e9eaeb for hairline borders on white surfaces and #d8d3cc for borders on cream surfaces
- Apply 0.03em positive tracking to all uppercase labels and micro-copy (10-14px) for an editorial-tag quality

Avoid:

- Do not use weight 600 or 700 for headings - weight 500 at large sizes with tight tracking is the system's voice
- Do not add box-shadow, gradients, or any form of elevation - depth comes from surface color contrast only
- Do not introduce blue, green, or any chromatic accent - the 0% colorfulness is intentional
- Do not use sharp corners (0-8px radius) on buttons or cards - the pill (160px) and large-rounded (32px) geometry is mandatory
- Do not center body text - left-align all paragraphs, descriptions, and feature lists
- Do not use pure #000000 for body text or button backgrounds - use #111111 for a softer near-black
- Do not place dark cards on light backgrounds outside the footer - the Obsidian #1e1e1d inversion is reserved for terminal page sections only

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
