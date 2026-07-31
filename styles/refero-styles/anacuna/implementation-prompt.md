# AI Implementation Prompt

Build a Anacuna-inspired interface using this source-derived style bundle.

Reference site: https://anacuna.com
Theme: light
Category: Design
North star: Oversized broadsheet with blush punctuation - a page where type IS the design and the single pink pill is the only color the eye can find.

Use these palette anchors:

- Ink Black `#000000` for Primary text, all borders, every hairline divider, filled language toggle - the entire structural skeleton of the page
- Paper White `#ffffff` for Page background, card surfaces, pill interiors, button text on dark fills
- Blush Bloom `#ffc8c8` for Brand mark fill (the ANA CUNA pill in the header) and the sole chromatic accent - a whisper of warmth that marks identity without ever shouting

Use these typography anchors:

- ABCMonumentGrotesk-Regular `--font-abcmonumentgrotesk-regular` for Sole typeface for the entire system. One weight - regular - is used at all three sizes: 94px for project titles (display), 31px for secondary headings, 15px for body, nav, tags, and footer. The refusal to introduce a bold or italic weight is a signature editorial choice; hierarchy comes purely from size, not weight.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: .
- Section gap: 48-80px.
- Card padding: 14px.
- Element gap: 7px.

Build these component patterns where relevant:

- Brand Seal Pill: Site identity in the top-left corner - the only chromatic element on the page
- Project Title Row: The dominant unit of the portfolio - one project per row
- Client Tag Pill: Client attribution label nested at the right end of each project row
- Outlined Nav Button: Primary navigation (PLAY, ABOUT) in the top-right header
- Language Toggle: EN/ES language switcher in the header
- Hairline Divider: Horizontal separator between project rows
- Footer Bar: Persistent copyright and legal links at the page bottom

Do:

- Set every project title in ABC Monument Grotesk Regular at 94px with line-height 1.00 - never introduce a bold or italic weight to create hierarchy.
- Separate every project row with a 1px #000000 hairline, flush against the type with no vertical margin.
- Use the 27px pill radius for every clickable element - nav, tags, brand mark, language toggle.
- Reserve #ffc8c8 exclusively for the ANA CUNA brand seal; it is the only chromatic color permitted on the page.
- Let display text bleed past the right viewport edge - the truncation is intentional editorial framing.
- Set body, nav, tags, and footer text at 15px ABC Monument Grotesk Regular with line-height 1.11.
- Keep the page background pure #ffffff and all text/borders pure #000000 - no intermediate grays.

Avoid:

- Do not add a bold, semibold, or italic weight to the type system - Monument Grotesk Regular at varying sizes is the entire hierarchy.
- Do not introduce card backgrounds, drop shadows, or elevated surfaces - the design is flat ruled paper, not a card system.
- Do not use #ffc8c8 for hover states, secondary CTAs, or decorative washes - it is locked to the brand mark only.
- Do not center-align project titles or constrain them to a max-width container - the full-bleed left alignment is the layout.
- Do not add intermediate neutral grays (#666, #999, etc.) - the system is binary black-on-white.
- Do not use 8px or 12px border-radius on any element - the 27px pill is the only radius in the system.
- Do not add icons, illustrations, or imagery to the index page - the typography alone carries the portfolio.

Source prompt cues:

**Quick Color Reference**
- text: #000000
- background: #ffffff
- border: #000000 (1px hairlines)
- accent: #ffc8c8 (brand seal only)
- primary action: #ffc8c8 (filled action)

**Example Component Prompts**

1. *Project Title Row*: Full-width row on #ffffff background. Title in ABC Monument Grotesk Regular at 94px, line-height 1.00, #000000, left-aligned, allowed to bleed past the right edge. A 1px solid #000000 hairline sits flush above the text. 48-80px of vertical space between rows.

2. *Client Tag Pill*: Outlined pill, 1px #000000 border, #ffffff fill, 27px border-radius, 6-8px vertical padding, 14px horizontal padding. Text in ABC Monument Grotesk Regular at 15px, line-height 1.11, #000000. Anchored to the right end of the project title row.

3. *Brand Seal Pill*: Filled pill, #ffc8c8 background, 27px border-radius, 6-8px vertical padding, 14px horizontal padding. Text 'ANA CUNA' at 15px ABC Monument Grotesk Regular, #000000. Top-left of header.

4. *Language Toggle*: Single pill, #000000 background, 27px border-radius, containing two 15px labels in #ffffff ABC Monument Grotesk Regular. The active language is displayed in #ffffff against the black fill; the inactive language may be dimmed or shown in a lighter tone. Top-right of header.

5. *Hairline Divider*: 1px solid #000000 line spanning 100% viewport width, with zero vertical margin - sits flush against adjacent type.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
