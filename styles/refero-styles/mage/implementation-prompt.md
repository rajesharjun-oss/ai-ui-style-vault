# AI Implementation Prompt

Build a Mage-inspired interface using this source-derived style bundle.

Reference site: https://www.mage.ai
Theme: light
Category: AI
North star: data alchemy on parchment. Warm off-white canvas, whisper-weight Inter headlines, one cobalt switch for action, dark-mode product islands floating inside a bright editorial page.

Use these palette anchors:

- Electric Cobalt `#244cff` for Primary action fill - CTA buttons, active nav state, the single switched-on color in an otherwise muted system
- Lavender Mist `#c3aeff` for Brand illustration accent - decorative fills in the hero artwork and supporting graphics, echoes the cobalt at lower saturation
- Parchment `#f7f7f1` for Page canvas - warm off-white background that gives the whole site its editorial, paper-like quality
- Snow `#ffffff` for Card surfaces, text on dark backgrounds, product thumbnail containers
- Ice Wash `#e8f8ff` for Tinted card surface - subtle blue-white variant for differentiated cards (logo bar, feature callouts)
- Sky Tint `#d6f2ff` for Decorative card wash - pale blue background for illustration overlays and feature card accents
- Lemon Wash `#ffffbd` for Decorative card wash - warm yellow tint for illustration card backgrounds and feature highlights
- Blush `#fcc2cd` for Decorative card wash - soft pink for illustration card backgrounds
- Buttercream `#fced9f` for Decorative card wash - warm cream-yellow for illustration card backgrounds
- Azure `#3388ff` for Illustration accent - mid-blue used in hero artwork and data visualization elements
- Slate Blue `#5487a1` for Illustration accent - muted blue for decorative borders and secondary graphic elements
- Amber `#9e770b` for Illustration accent - warm dark-yellow for decorative graphic elements
- Lilac Pop `#ba9ffc` for Illustration accent - vivid lavender for hero artwork highlights
- Deep Cobalt `#294dba` for Illustration accent - darker blue for hero artwork depth and contrast
- Pure Black `#000000` for Primary text, hairline borders, high-contrast edges
- Graphite `#2b2b2b` for Secondary text, body copy on light surfaces - softer than pure black for reading comfort
- Obsidian `#1d1f21` for High-contrast neutral action fill for primary buttons on light surfaces.
- Ash `#878787` for Muted text - captions, helper text, secondary metadata
- Fog `#b0b0b0` for Borders, dividers, disabled state outlines, muted link text

Use these typography anchors:

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- Inter `--font-inter` for Workhorse body and UI text - body copy at 400, buttons/labels at 500-600, bold callouts at 700. The font's open apertures and tall x-height make it readable at 12-16px on the warm canvas
- Inter Variable `--font-inter-variable` for Display and heading sizes - 60px display headlines, 38px section headers, 30px subheadings. Weight stays at 400 even at display size: the headlines whisper rather than shout, authority through scale not weight
- Geist `--font-geist` for Small bold labels - compact uppercase-style tags and category markers at 14px weight 600

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 64px.
- Card padding: 24-40px.
- Element gap: 10px.

Build these component patterns where relevant:

- Primary CTA Button: High-emphasis action - 'Start Building', form submissions
- Dark CTA Button: Secondary high-emphasis - 'Try Mage' in nav, product entry points
- Ghost Text Link: Low-emphasis action - 'Get a demo', inline navigation
- Navigation Bar: Top-level site navigation
- Hero Product Thumbnail: Embedded product preview in the hero section
- Trust Logo Bar: Social proof - 'Trusted by data teams at leading companies'
- Feature Card (Product Screenshot): Feature showcase - 'Build pipelines', 'Connect data', 'Run continuously', 'Fix and recover'
- Section Heading Group: Section titles and descriptions
- Illustration Overlay: Decorative hero artwork - people interacting with a data orb
- Data Source Icon Grid: Integration showcase within the product UI

Do:

- Use Electric Cobalt #244cff exclusively for primary action fills - never as a decorative element or text color
- Set all buttons to pill radius (100px) for both the cobalt primary and obsidian dark variants
- Keep headlines at Inter weight 400 - authority comes from size (38px section, 60px display), not weight
- Use Parchment #f7f7f1 as the page canvas for all marketing pages; reserve Snow #ffffff for elevated cards and containers
- Embed dark-mode product screenshots (#1d1f21 surface) as visual anchors inside the light page - this light-dark contrast is the signature
- Apply Inter font features "cv03", "cv04", "cv09", "cv11" to get the alternate glyph sets that distinguish Mage's Inter from default Inter
- Use 6px radius for cards and product thumbnails, 16px for larger image containers, 100px (pill) for all interactive controls

Avoid:

- Do not use multiple vivid colors as action buttons - the system has one action color (cobalt) and one dark variant; everything else is text or surface
- Do not set headlines to weight 600 or 700 - the whisper-weight 400 at large size is the signature; bolding breaks the editorial tone
- Do not add drop shadows to cards on the Parchment canvas - the warm tonal contrast between #f7f7f1 and #ffffff is enough separation
- Do not use the illustration palette colors (#fcc2cd, #fced9f, #ba9ffc) as UI chrome - they are reserved for the hero artwork and decorative card washes
- Do not mix Light Slate Blue #5487a1 or Amber #9e770b into text or border roles - they are illustration-only accents
- Do not use sharp corners (0px radius) on cards or images - the 6px minimum radius is a system-wide baseline
- Do not put body text below 14px - the Inter 12px usage is limited to micro-labels and metadata, never running prose

Source prompt cues:

**Quick Color Reference**
- Canvas: #f7f7f1 (Parchment)
- Card surface: #ffffff (Snow)
- Tinted surface: #e8f8ff (Ice Wash)
- Primary text: #000000 / #2b2b2b
- Muted text: #878787 / #b0b0b0
- Accent: #244cff (Electric Cobalt)
- Dark surface: #1d1f21 (Obsidian)
- primary action: no distinct CTA color

**Example Component Prompts**
No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

2. **Create a feature card**: No card background (sits on Parchment). Section heading at 38px Inter Variable weight 400, #000000. Subtitle at 16px Inter 400, #2b2b2b. Dark product screenshot below with 6px border-radius, 24px internal padding, showing a code editor with dark sidebar.


4. **Create a navigation bar**: Transparent over Parchment. Left: logo + 5 nav links in Inter 500 at 15px, #000000. Right: 'Demo' ghost text link (#2b2b2b) + dark 'Try Mage' pill button (#1d1f21 background, white text, 8px 16px padding, 100px radius).

5. **Create a trust logo bar**: Full-width Parchment background. Caption 'Trusted by data teams' at 14px Inter 400, #878787. Row of 7 company logos in #000000, evenly spaced, max-height 24px each, with 10px gap between logos.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
