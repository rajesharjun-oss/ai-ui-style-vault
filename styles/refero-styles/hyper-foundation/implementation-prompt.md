# AI Implementation Prompt

Build a Hyper Foundation-inspired interface using this source-derived style bundle.

Reference site: https://hyperliquid.xyz
Theme: dark
Category: Crypto
North star: Living emerald sanctuary a deep forest vault where a single luminous mint glow breathes through organic, shadowed forms.

Use these palette anchors:

- Forest Depths `#072724` for Page canvas, hero background, deep surface layer the dominant dark field that everything else floats on
- Midnight Tide `#0f3933` for Primary text on canvas, strong borders, secondary surface tint readable white-space-equivalent for dark mode
- Shadow Teal `#23524c` for Elevated surface, card fills, subtle borders one step lighter than the canvas for layer separation
- Charcoal Hairline `#2c2e33` for Subtle dividers and default 1px borders across cards, images, and icons almost invisible on the dark canvas, used for structural quietness
- Abyss Green `#122d28` for Decorative background blob deepest atmospheric tint behind organic hero shapes
- Deep Lagoon `#1c3f38` for Decorative mid-tone blob in the hero atmosphere, sits between canvas and surface
- Mist Gray `#b0c5c1` for Muted body text, secondary descriptions, captions desaturated enough to recede behind the mint accent
- Pure Light `#ffffff` for Headline text on dark canvas, high-contrast text inside mint-filled buttons

Use these typography anchors:

- Teodor Display and editorial headlines, brand statements, section titles. Custom serif with sharp contrast between thick and thin strokes; at 90px with 0.75 leading it creates a magazine-cover authority that is the signature typographic gesture of the site. Subheading scale at 24px carries the same character into smaller contexts. `--font-teodor`
- Inter Body copy, UI labels, navigation, buttons, captions. The weight 300 default across most sizes keeps the interface quiet against the display serif the contrast between Teodor's editorial presence and Inter's whisper-light functional text is a defining rhythm of the system. `--font-inter`

Use these layout rules:

- Base spacing: source-defined.
- Density: comfortable.
- Respect the extracted card, section, and element spacing.
- Preserve the source radius system.

Build these component patterns where relevant:

- Pill Primary Button: Main call-to-action (e.g. Start Trading, Launch App)
- Pill Ghost Button: Secondary action (e.g. Start Building)
- Navigation Pill: Top-right primary nav action (Launch App)
- Top Navigation Bar: Global header
- Brand Mark / Logo Glyph: Standalone brand icon (butterfly/dumbbell shape)
- Logo Lockup: Brand identifier in nav and footer
- Hero Section: Above-the-fold brand statement
- Glow Card: Featured content surface with elevated emphasis

Do:

- Use Mint Glow (#97fcd7) as the only fully saturated color on any screen restrict it to one CTA, one brand mark, or one highlight per viewport.
- Set display headlines in Teodor weight 400 at 90px with 0.75 line-height; this tight leading is the signature editorial gesture.
- Set body and UI text in Inter weight 300 by default; reserve weight 400 for interactive controls and emphasis.
- Use 60px border-radius for every button, tag, and pill element sharp corners would feel off-system.
- Express elevation with the mint outer-glow shadow on cards, never with gray drop-shadow stacks.
- Build backgrounds from organic, softly-edged shapes in Abyss Green, Deep Lagoon, and Shadow Teal layered over Forest Depths never flat solid fills for hero regions.
- Keep paragraph text in Mist Gray (#b0c5c1), reserving Pure Light for headlines only this is what makes the typography feel layered rather than uniformly white.

Avoid:

- Do not introduce any new saturated hue the entire chromatic vocabulary is mint; adding red, blue, or yellow breaks the rarified atmosphere.
- Do not use box-shadow with gray or black tones; the only allowed shadow color is the mint glow rgba(151,252,215,0.4).
- Do not set Teodor below 24px its editorial detail collapses at small sizes and Inter should take over.
- Do not use square or 4px corner radii on interactive elements; the system is defined by 60px pill geometry.
- Do not place mint text directly on the Forest Depths canvas at small sizes without enough weight mint on dark needs at least 16px / 400 weight to read.
- Do not use the Charcoal Hairline (#2c2e33) as a visible decorative border it is for near-invisible structural hairlines only.
- Do not center-align body paragraphs; keep body text left-aligned to maintain the editorial reading rhythm.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
