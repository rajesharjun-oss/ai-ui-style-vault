# AI Implementation Prompt

Build a Zora-inspired interface using this source-derived style bundle.

Reference site: https://zora.co
Theme: light
Category: Crypto
North star: Neon gallery on graphite glass.\n\n{

Use these palette anchors:

- Void Black `#121212` for Dark supporting neutral for text, icons, and strong contrast. Do not promote it to the primary CTA color
- Graphite `#4d4d4d` for Secondary text, body copy, icons, nav labels, metadata
- Fog Gray `#878787` for Muted helper text, tertiary metadata, inactive icon strokes
- Ash `#cacaca` for Placeholder text, light borders, disabled strokes
- Hairline `#e6e6e6` for Input borders, dividers, subtle separators
- Pure White `#ffffff` for Canvas background, card surfaces, button text on dark fills
- Reactor Green `#00df00` for Green supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Voltage Pink `#ff00f0` for Secondary accent for live indicators, countdown timers, hot tags, creator highlights
- Onyx `#000000` for Icon fills, logo mark, maximum-contrast text on light backgrounds

Use these typography anchors:

- MonumentGrotesk `--font-monumentgrotesk` for Sole typeface across all UI: nav labels, body text, button text, metadata, card titles. The custom geometric grotesque's compressed forms and uniform 410-500 weights create a label-density voice rather than a reading voice; it treats copy as UI chrome, not as prose. No display-weight contrast is used - hierarchy is achieved through size and color, not weight amplitude.

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: .
- Section gap: 24px.
- Card padding: 12px.
- Element gap: 8px.

Build these component patterns where relevant:

- Buy Button (Primary Action): Purchase CTA on every collectible card
- Sign Up Button (Dark Fill): Account creation in top-right header
- Log In Button (Ghost): Returning-user entry in top-right header
- Follow Button (Pill Outline): Subscribe to a creator in the right rail
- Collectible Card (Feed Post): Primary content unit in the center feed
- Left Navigation Rail: Persistent icon-based navigation column
- Top Search Bar: Global search/command input
- Suggested Follows Panel: Right-rail discovery unit
- Price/Timer Bar: Live auction status on collectible cards
- QR Code CTA Widget: App-download prompt overlay bottom-right
- Comment Input Field: Inline comment composer on each card
- Zora Logo Mark: Brand identifier in bottom-left corner

Do:

- Use #00df00 exclusively for purchase/buy actions - never for decoration, tags, or non-transactional UI
- Set all text at -0.015em letter-spacing; the tight tracking is part of the system's visual identity, not optional
- Keep card padding at 12px and element gaps at 8px or 4px - the compact density is intentional, not cramped
- Use 9999px border-radius for all social actions (Follow) and 8px for transactional actions (Buy, Log In) - the radius difference signals intent
- Reserve #ff00f0 for time-sensitive or live-status indicators (countdown timers, live auctions, real-time pulses)
- Place all navigation icons in a persistent 56px left rail with no labels - icon-only navigation is part of the gallery-tool language
- Use MonumentGrotesk weight 500 for all interactive elements and weight 410/450 for body metadata to create subtle hierarchy without weight contrast

Avoid:

- Don't add shadows to cards - surfaces sit flat against the canvas, elevation is expressed by background contrast only
- Don't introduce additional accent colors beyond #00df00 and #ff00f0 - the two-color neon system is deliberately limited
- Don't use weights above 600 - the type system is calibrated for label density, not editorial display
- Don't center-align body text or card titles - left-align everything except hero headlines
- Don't use border-radius values other than 8px (buttons/inputs), 12px (cards), or 9999px (pills) - mixing radii breaks the system
- Don't add gradients to UI chrome - the gray gradient is reserved for skeleton/loading states only
- Don't use color to indicate state on form inputs - use border color shift (#cacaca #121212) instead of fills

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
