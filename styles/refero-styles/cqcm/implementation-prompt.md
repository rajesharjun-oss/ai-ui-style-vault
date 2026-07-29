# AI Implementation Prompt

Build a CQCM-inspired interface using this source-derived style bundle.

Reference site: https://cqcm.coop
Theme: light
Category: Other
North star: Verdant cooperative megaphone. A vivid green slab screams a civic message across a white grid while black pill buttons ground the chromatic energy.

Use these palette anchors:

- Cooperative Green `#44d991` for Hero panel fill, primary stat block, decorative dot overlays - the loudest brand voice; the color that makes the page feel activated
- Civic Blue `#4c92e9` for News card surfaces, secondary stat blocks - chromatic but cooler, reserved for media/content contexts rather than primary brand expression
- Sunset Coral `#ff6a51` for Accent stat block only - appears once as data emphasis, treated as a single-note punctuation rather than a system color
- Mint Whisper `#eaf9f2` for Card and nav surface tint - a barely-there green echo of the hero green, softens white space without breaking the light theme
- Ink Black `#000000` for Primary text, pill button fill, all borders and dividers - does the structural work of the system, the only color used for controls
- Paper White `#ffffff` for Page canvas, text on filled buttons, image surfaces
- Steel Gray `#666666` for Muted helper text, secondary nav borders - the only mid-gray in the system, used sparingly for de-emphasis

Use these typography anchors:

- Athletics `--font-athletics` for Display and badge type - used for hero headlines (48-78px), card labels, and uppercase tags. The wide letter-spacing (0.04em) is a French institutional signature that turns every headline into a civic declaration. Custom face; substitute with Archivo Black, Anton, or Druk for similar uppercase weight and tracking, or with a wide-tracked geometric like Bebas Neue for closer feel.
- Manrope `--font-manrope` for Body, navigation, button labels, and small text - the working font. Slightly opened tracking (0.01-0.011em) is a subtle departure from default; it keeps dense French text feeling breathable without becoming display-like. Pairs cleanly with Athletics because both share geometric, humanist proportions.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1280px.
- Section gap: 80px.
- Card padding: 20px.
- Element gap: 20px.

Build these component patterns where relevant:

- Hero Green Panel: Primary brand surface - declares the organization's mission at full volume
- Pill Button (Filled): Primary action - the only filled button variant in the system
- Pill Button (Ghost): Secondary navigation - for less prominent calls
- Circular Image Frame: Signature image treatment - softens the grid-heavy layout
- Dot Pattern Overlay: Decorative brand texture on hero imagery
- News Card: Content card for articles, communiques, and nouvelles
- Stat Block: Large data display - one color per metric, stacked for rhythm
- Category Tag: Content classification - COMMUNIQUE, NOUVELLES, etc.
- Top Navigation Bar: Primary site navigation
- 'See All' Link: Section-level navigation - to full listings
- Section Heading: Top-of-section title - minimalist and structural
- Hero Image Panel: Left half of the hero - photography with brand dot overlay

Do:

- Use Athletics 400-500 for all display and badge text with letter-spacing 0.04em - the wide tracking is the brand's typographic identity, not a stylistic option
- Set pill buttons at 100px radius with #000000 fill and #ffffff text in 14-16px Manrope, uppercase
- Reach for #44d991 (Cooperative Green) as the dominant chromatic surface - hero, stat blocks, and decorative dots - not for buttons or text accents
- Crop images to circles inside blue (#4c92e9) news cards; reserve the circle shape for imagery only
- Stack stat blocks in a 5-block staircase with ~30px vertical and horizontal offset between each
- Use #eaf9f2 (Mint Whisper) for soft card and nav surfaces when white feels too clinical
- Separate nav items with 20-30px horizontal gap; keep the nav a single non-sticky white bar

Avoid:

- Do not use any chromatic color as a button fill - buttons are always #000000 or outlined; color is for surfaces and decoration only
- Do not add shadows to cards, buttons, or content - the system is flat by design; the only shadow is the nav bar's soft halo
- Do not mix Athletics into body copy or Manrope into hero headlines - the font split is strict: Athletics displays, Manrope reads
- Do not use letter-spacing tighter than 0.01em on Manrope or 0.04em on Athletics - the opened tracking is part of the brand's breathable French-institutional feel
- Do not use coral (#ff6a51) more than once per surface - it is a single-note punctuation, not a system color
- Do not use square corners on buttons - pill shape (100px) is the only button geometry; cards get 8px, small elements get 4px
- Do not introduce gradients, blurs, or glass effects - the system is unapologetically flat, saturated, and solid

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
