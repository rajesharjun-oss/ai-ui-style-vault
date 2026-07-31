# AI Implementation Prompt

Build a ethereum.org-inspired interface using this source-derived style bundle.

Reference site: https://ethereum.org
Theme: light
Category: Crypto
North star: Lilac architecture in flat editorial space - a printed open-source almanac where the Ethereum diamond floats above duotone crowds of people.

Use these palette anchors:

- Lavender Paper `#ece0ff` for Page canvas, soft card surfaces, hero wash - near-gray violet that reads as neutral paper across the entire site
- Pure White `#ffffff` for Card surface above canvas, icon strokes, inverse text on violet buttons, nav background
- Ash Gray `#cfcfcf` for Hairline dividers, card borders, input borders, separator rules - the dominant border tone at 2484 occurrences
- Onyx `#121212` for Primary text, heading fill, dark icon strokes - the only body-color the UI commits to
- Graphite `#616161` for Secondary body text, muted helper copy, nav subtext
- Fog `#8c8c8c` for Tertiary text, disabled nav items, low-priority borders
- Ethereum Violet `#6c24e0` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Deep Iris `#41128c` for Hover state on violet, dark accent surface, gradient origin - the violet pushed to its shadow end
- Hot Magenta `#f60e9d` for Secondary accent for inline links inside feature cards, tag pills, illustration accent
- Sapphire `#3d4ceb` for Tertiary accent for links, icon variants, illustration cool-tone accents
- Mint `#0f9972` for Green supporting accent for decorative details and low-frequency emphasis. Use as a supporting accent, not as a status color

Use these typography anchors:

- Inter `--font-inter` for Sole workhorse - body at 16px/400, section headings at 24-30px/700, and display at 48-64px/900. The 900 weight at 60-64px is the signature: headlines are not politely bold, they are geometric slabs that anchor every section
- IBM Plex Mono `--font-ibm-plex-mono` for Used only for keyboard shortcut hints in the search bar (cmd/k label). Never used for body or heading

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 64px.
- Card padding: 32px.
- Element gap: 8px.

Build these component patterns where relevant:

- Primary Filled Button: Main call-to-action across landing and section pages
- Ghost Outline Button: Secondary actions in card footers and inline links
- Eyebrow Label: Section category tag sitting above headlines
- Hero Illustration Band: Full-bleed visual anchor at the top of landing and section pages
- Feature Card (Pastel): Three-column content tiles in the 'A new way to use the internet' section
- Popular Topic Card: Two-column quick-link tiles in the 'What is Ethereum?' section
- Top Navigation Bar: Sticky header across all pages
- Search Command Bar: Keyboard-driven search trigger in the nav
- Two-Column Section Block: Editorial text + illustration layout (e.g. 'What is Ethereum?')
- Full-Width Editorial Card: Lavender panel introducing a content theme (e.g. 'A new way to use the internet')
- Icon: Recurring Ethereum diamond octahedron used everywhere
- Card Arrow Link: Inline action link at the end of a card or paragraph

Do:

- Use Inter 900 at 48-64px for any section display heading - the geometric slab weight is non-negotiable for the brand
- Use #6c24e0 for every primary action, eyebrow label, and active link - reserve all other chromatic colors for secondary text accents and illustration
- Set feature card backgrounds to one of the pastel tints (lavender #ece0ff, mint, peach, pink) at 16px radius, with no shadow and no border
- Place an eyebrow label (Inter 700, 14px, uppercase, #6c24e0, pill on #ece0ff) directly above every section heading
- Use 4px radius on primary buttons - the square-shouldered button is a signature, not a pill
- Anchor every section with at least one illustration or icon; text-only sections should be the exception
- Use 64px vertical padding between major sections and 32px inside cards

Avoid:

- Don't use drop shadows for elevation - hierarchy comes from flat surface tints, not depth
- Don't use 600 or 800 weight for headlines - the system commits to 900 or 700 only, and 900 only at display sizes
- Don't introduce new saturated colors beyond the existing four (#6c24e0, #f60e9d, #3d4ceb, #0f9972) - the palette is rationed
- Don't use pill-shaped buttons (9999px) for primary actions - that radius is reserved for search triggers and tags
- Don't stack text directly on the full-bleed illustration without the centered headline block underneath it
- Don't use centered body text - body paragraphs are always left-aligned at max 65ch width
- Don't use photography as the primary visual - illustration owns this system, photos should only appear in editorial context if at all

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
