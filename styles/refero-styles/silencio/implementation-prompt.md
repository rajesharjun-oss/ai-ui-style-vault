# AI Implementation Prompt

Build a Silencio-inspired interface using this source-derived style bundle.

Reference site: https://silencio.es
Theme: light
Category: Design
North star: white room with floating artifacts. A warm-paper gallery vitrine where every element earns its space against negative volume, and silence is a deliberate design material.

Use these palette anchors:

- Ink Black `#000000` for Primary text, iconography, hairline rules, table borders the only high-contrast element on the page
- Paper Warm Gray `#dbdad9` for Card surfaces, soft fills, the single chromatic departure from pure white, gentle gradient origin
- Graphite Border `#808080` for Subtle table dividers and secondary rule lines used when #000000 would feel too heavy
- Bleach White `#ffffff` for Supporting palette color for small decorative accents when the core palette needs contrast.

Use these typography anchors:

- HaasR Workhorse grotesque for body, subheadings, and mid-size headings. Weight 100 is used for restraint in body contexts; 700 sparingly for emphasis. The single most-used face carries the page. `--font-haasr`
- HaasT Display-only face at 141px with tightened leading (0.90). Used for hero statements and singular set-pieces the only moment typography shouts, and it shouts at full volume against pure white. `--font-haast`
- PT Mono Metadata, spec labels, catalog tags the typographic equivalent of a printed museum label. Appears at 11px only; functions as a quiet signature rather than informational copy. `--font-pt-mono`

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Respect the extracted card, section, and element spacing.
- Preserve the source radius system.

Build these component patterns where relevant:

- Pill Button: Primary interactive element
- Ghost Link: Inline navigation and content links
- Paper Card: Grouped content surface
- Display Headline: Hero and section set-pieces
- Museum Label: Metadata, catalog tags, object captions
- Hairline Divider: Section separation
- Table Rule: Data and catalog row separation
- Floating Product Showcase: Primary visual carrier

Do:

- Use the full 141px HaasT weight 100 for display headlines it is the only moment this system is allowed to be loud
- Reach for #dbdad9 as the only chromatic surface departure; every other surface stays #ffffff or #000000
- Separate content with 1px #000000 hairlines, not padding, not shadows, not color blocks
- Pair every display headline with a PT Mono 11px museum label directly beneath it
- Use radius 7.2px for cards and 129.6px for buttons do not interpolate intermediate values
- Set lineHeight at 0.90 for any type at 39px or above; tight leading is a signature, not an accident
- Let product photography float on pure white with no frame, no caption box, and no drop shadow

Avoid:

- Never introduce a chromatic color the palette ends at #000000, #dbdad9, #808080, and #ffffff
- Never use drop shadows for elevation; the gradient #dbdad9 #ffffff is the only depth the system allows
- Never set type above 141px or below 9px the 132px range is the entire expressive spectrum
- Never use #0000ee or any default browser link color links are #000000, no exception
- Never fill a button with color; the pill is always transparent with a 1px #000000 border
- Never center body text in paragraphs; only display statements and labels earn centered alignment
- Never use shadows, blurs, or glows on photographs or product imagery

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
