# AI Implementation Prompt

Build a Foodnoms-inspired interface using this source-derived style bundle.

Reference site: https://foodnoms.com
Theme: light
Category: Productivity
North star: Sunlit fruit market on white porcelain warm orange, fresh green, and generous rounded forms

Use these palette anchors:

- Ember Orange `#ff5406` for Orange supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Verdant Green `#00b33f` for Green supporting accent for decorative details and low-frequency emphasis
- Signal Red-Orange `#ff3400` for Secondary warm accent visible in app screen UI elements and supporting brand moments. Sits one step hotter than Ember Orange for emphasis on selected or active app states
- Sky Blue `#00a9dd` for Cool counter-accent for app-internal data categories (carbs/protein/other nutrient groupings). Balances the warm-dominant palette inside phone mockups
- Mist Blue `#72a2c5` for Muted cool accent softens Sky Blue for secondary data labels and chart backgrounds inside the app surfaces
- Sunset Orange `#ff6d00` for Warm accent for secondary headings and emphasis text within the marketing pages
- Amber `#945300` for Deep warm accent for data-heavy text and chart labels in the app's nutrition displays
- Alert Red `#ff001e` for Red supporting accent for decorative details and low-frequency emphasis

Use these typography anchors:

- Aquawax Pro Medium Aquawax Pro Medium detected in extracted data but not described by AI `--font-aquawax-pro-medium`
- Aquawax Pro Primary brand typeface used across all display, heading, and body contexts. The custom face has a wide x-height, rounded geometric forms, and friendly proportions. Bold (700) is used for the 60px display and 30px section headlines these are the system's typographic anchors. DemiBold (600) handles subheadings and button labels at 1416px. Medium (500) carries body copy at 1720px with generous 1.61.8 line-height for comfortable reading. `--font-aquawax-pro`
- System sans-serif Fallback for very small UI text and icon labels. Aquawax Pro is not used at micro sizes; system font handles them to keep render weight low. `--font-system-sans-serif`
- Aquawax Pro DemiBold Aquawax Pro DemiBold detected in extracted data but not described by AI `--font-aquawax-pro-demibold`

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Respect the extracted card, section, and element spacing.
- Preserve the source radius system.

Build these component patterns where relevant:

- Brand Wordmark: Site identity in header and footer
- Header Filled Button: Primary brand action in the navigation bar
- Ghost Nav Link: Secondary navigation items
- App Store Badge: Download CTA in the hero
- Two-Tone Display Headline: Hero page title
- Section Accent Heading: Feature section titles
- Phone Mockup Carousel: Visual showcase of the app interface
- Press Logo Grid: Social proof / media mentions

Do:

- Use 26px border-radius on every interactive element and card this is the system's signature softness
- Apply the two-tone headline pattern: one color for the outcome word, Graphite (#2f2f2f) for the rest
- Use Aquawax Pro Bold at 60px for hero displays and 30px for section headings never interpolate intermediate sizes
- Pair Verdant Green (#00b33f) with positive/progress data and Signal Red-Orange (#ff3400) with negative/overage data inside app screens
- Use generous 96px section gaps between major page sections to let phone mockups breathe
- Keep all text on white or Fog (#f5f5f5) never place chromatic text on chromatic backgrounds
- Show 3+ phone mockups side-by-side in the hero, slightly overlapping, to demonstrate the breadth of the app experience

Avoid:

- Don't use box-shadows or drop-shadows anywhere the system is deliberately flat
- Don't use a border-radius other than 26px on buttons, cards, tags, or inputs
- Don't call any color a 'CTA' or 'primary action' in the token system describe them by their brand role instead
- Don't use Aquawax Pro at sizes below 12px fall back to system sans-serif for micro UI
- Don't place chromatic text on a chromatic background always pair color text with white or Fog
- Don't use gradient backgrounds or gradient buttons the system is solid color only
- Don't introduce new chromatic colors for marketing pages the warm-primary + cool-accent + app-data palette is complete

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
