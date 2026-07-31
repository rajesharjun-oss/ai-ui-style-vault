# AI Implementation Prompt

Build a Extract-inspired interface using this source-derived style bundle.

Reference site: https://extract.studio
Theme: light
Category: Agency
North star: Editorial monolith on gallery paper

Use these palette anchors:

- Gallery White `#ffffff` for Neutral form states, badge text, and quiet UI feedback where color should stay understated. Do not promote it to the primary CTA color
- Ink Black `#070707` for Primary text, hairline borders, filled buttons, nav text - the structural linework of the entire system; Dark surface for project cards and editorial spreads - the inverse of the canvas, used to make featured work feel like a framed plate
- Spearmint Wash `#e7feda` for Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color

Use these typography anchors:

- Feature Deck `--font-feature-deck` for Display and section-heading face used exclusively for monumental wordmark treatments. The 104px 'Extract' lockup and 44px subheadings carry the entire brand voice through scale alone - no other display serif or grotesque is needed.
- ABC Diatype `--font-abc-diatype` for Universal workhorse - body copy (18-19px), nav and meta (19px), subheadings (21px), and card titles (34px). Weight 700 is used sparingly for emphasis within body contexts. The tight 1.25 line-height on larger sizes keeps the editorial density.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 59px.
- Card padding: 19px.
- Element gap: 19px.

Build these component patterns where relevant:

- Floating Pill Navigation: Persistent site navigation
- Display Wordmark: Brand identity at hero scale
- Editorial Project Card (Dark): Featured work showcase on light canvas
- News Article Card: Editorial/blog entry on mint section
- Hairline Section Divider: Vertical separation between content zones
- Ghost Text Link: Inline navigation ('View all', project titles)
- Outlined Input Field: Form input for contact/newsletter
- Hero Image Plate: Full-bleed editorial photography
- Section Header: Introductory heading for content blocks
- Footer: Site closure

Do:

- Use #070707 for all text, borders, and filled UI controls - it is the only structural color in the system
- Reserve #e7feda mint for full section backgrounds, never for buttons, icons, tags, or text
- Set the display wordmark at 104px in Feature Deck with no letter-spacing adjustment - let the natural metrics carry the impact
- Use 9.3px border-radius for all cards, images, and content containers; 4.6px for inputs and small controls; 9999px only for the floating nav pill
- Maintain 1px hairline #070707 borders for all separation - never use shadows to lift elements off the canvas
- Pair Feature Deck 44px section heads with ABC Diatype 19px body - the scale jump is the hierarchy, not weight or color
- Keep the floating nav centered, persistent, and visually identical on every screen - it is the only persistent chrome

Avoid:

- Do not introduce a second accent color - the system is built on the tension between black, white, and one mint wash
- Do not apply the mint #e7feda to buttons, links, icons, or hover states - it is atmospheric only
- Do not add drop shadows, inner glows, or any elevation effects - flatness is the signature
- Do not use Feature Deck for body copy or sub-100px text - it is display-only and loses legibility below 44px
- Do not use colored backgrounds inside cards on the mint section - let the section color be the unifying field
- Do not center body text - only the display wordmark and nav are centered; all editorial copy is left-aligned
- Do not use border-radius values outside the 4.6px / 9.3px / 9999px scale - the system is intentionally tight

Source prompt cues:

Quick Color Reference:
- text: #070707
- background: #ffffff
- border: #070707 (1px)
- accent: #e7feda (section background only)
- primary action: no distinct CTA color

Example Component Prompts:
1. Build a floating pill navigation: 1px #070707 border, white background, border-radius 9999px, padding 9px 14px. Links set in ABC Diatype 19px weight 400, #070707, separated by 19px gaps. No shadow, centered horizontally.
2. Build a hero section: #ffffff background. Display wordmark 'Extract' in Feature Deck 104px weight 400, #070707, line-height 1.0, bleeding to the right edge. Below: ABC Diatype 34px serif tagline in #070707. Full-bleed editorial photograph with 9.3px border-radius beneath.
3. Build a news article card on a #e7feda section: transparent background, 9.3px-radius image at top, title in ABC Diatype 19px weight 700 #070707, body in ABC Diatype 18px weight 400 #070707 line-height 1.5. No border, no shadow.
4. Build a dark project card: #070707 background, 9.3px border-radius, full-bleed media inside (typographic spread or photograph), no internal padding, no border, no shadow.
5. Build a section header: ABC Diatype 34px weight 400 #070707 left-aligned, paired with a right-aligned 'View all' ghost link (ABC Diatype 19px #070707, 1px underline). 59px top margin, 19px bottom margin.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
