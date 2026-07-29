# AI Implementation Prompt

Build a Impilo-inspired interface using this source-derived style bundle.

Reference site: https://impilo.health
Theme: dark
Category: Other
North star: Midnight clinical observatory a violet command console where health data glows in cyan.

Use these palette anchors:

- Deep Iris `#16165c` for Page canvas, hero background, primary surface the brand-defining midnight violet that sets the entire dark mode identity
- Iris Shadow `#232269` for Elevated card surfaces on dark canvas, secondary card backgrounds one step lighter than canvas for depth without breaking the violet atmosphere
- Iris Glow `#403cd5` for Mid-tone accent surface, footer background, highlighted metric blocks mid-violet for tertiary elevation and accent fills
- Iris Pulse `#5350cc` for Violet action color for filled buttons, selected navigation states, and focused conversion moments.
- Iris Border `#4846c6` for Card border outlines, subtle surface edges on dark mode keeps card perimeters defined without breaking the violet mood
- Iris Veil `#524fe1` for Body and card border accent, secondary surface outline lighter violet for hairline separators on dark surfaces
- Lilac Mist `#b1a6f6` for Line-art illustration stroke, decorative SVG fills, wireframe graphics soft violet for technical/medical illustration overlay
- Clinical Cyan `#00b1ff` for Data highlights, chart strokes, icon accents, inline links, interactive borders the primary data-viz and link color across the UI

Use these typography anchors:

- Gilroy Sole typeface across the entire system weight 500 for body, links, buttons, cards; weight 600 for all headings and display. Gilroy's geometric humanism gives medical data a friendly, non-clinical warmth `--font-gilroy`

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Respect the extracted card, section, and element spacing.
- Preserve the source radius system.

Build these component patterns where relevant:

- Pill CTA Button (Primary): Primary action trigger in hero and navigation
- Pill Button (Ghost): Secondary or outline action on dark canvas
- Pill Button (Light Section): Primary action in inverted Pearl sections
- Dark Canvas Card: Data dashboard panel, elevated content block
- Highlighted Metric Card: Hero metric display (e.g., 'Blood Pressure Average 127/73')
- Tab Strip (Dashboard): Metric category selector within dashboard
- Patient Profile Card: Sidebar patient identity block
- Billing Summary List: Categorized list with icon-prefixed rows

Do:

- Use Deep Iris (#16165c) as the page canvas for all dark sections never introduce a neutral gray or pure black background
- Set all buttons and tags to 9999px border-radius pill geometry is non-negotiable and defines the brand silhouette
- Apply -0.075em letter-spacing at 92px+ display sizes to make headlines feel compressed and engineered rather than airy
- Reserve Clinical Cyan (#00b1ff) for data, links, and chart strokes never as a decorative fill
- Pair Mint Vital (#00ffaa) with health-positive data (vitals in range, active status) to give green semantic meaning beyond decoration
- Use the dotted-outline Word Highlight Box for the single most important word in any headline one per page maximum
- Break between dark and light sections with a hard color cut at Pearl (#f4f4f6) no gradient transitions between themes

Avoid:

- Never use a neutral gray (e.g., #1a1a1a, #2a2a2a) as a background all dark surfaces must stay in the violet family
- Do not mix weight 400 or 700 into the type system Gilroy speaks only in 500 and 600
- Never apply Clinical Cyan (#00b1ff) as a large solid fill on buttons or hero blocks it is a data/link color, not a surface color
- Do not use Mint Vital (#00ffaa) for error states or warnings its meaning is locked to positive health signals
- Avoid sharp corners (0-4px radius) on any container minimum 7px for icons, 16px for inputs, 24px for cards
- Do not introduce a second typeface Gilroy at weights 500/600 covers every typographic need
- Never use white (#ffffff) as a card background on the dark canvas the light inversion section is the only place Cloud White surfaces belong
- Do not use gradient transitions between dark and light sections the hard cut is a signature choice

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
