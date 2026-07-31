# AI Implementation Prompt

Build a Vectary-inspired interface using this source-derived style bundle.

Reference site: https://vectary.com
Theme: light
Category: Design
North star: Graphite blueprint with violet signal

Use these palette anchors:

- Graphite `#252525` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color
- Charcoal `#313131` for Secondary dark surface, nav panel background
- Slate `#595959` for Body text, secondary headings - the readable gray for paragraph copy
- Fog `#949494` for Muted helper text, captions, links at rest
- Paper `#ffffff` for Page background, text on dark fills
- Electric Violet `#6100ff` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Soft Violet `#9d50ff` for Supporting palette color for small decorative accents when the core palette needs contrast. Do not promote it to the primary CTA color

Use these typography anchors:

- Inter `--font-inter` for Single-family system: weight 400 for body and UI labels, weight 700 for section headings and button text, weight 900 reserved for display headlines (83px). The dramatic jump from 26px to 83px creates a two-tier hierarchy - page-heading-class copy lives at 22-26px, and only true hero moments reach 83px. Negative letter-spacing tightens with size: -0.012em at 14px scaling linearly to -0.039em at 83px, so display text optically squares up while small text stays crisp.

Use these layout rules:

- Base spacing: 6px.
- Density: comfortable.
- Page max-width: 800px.
- Section gap: 60px.
- Card padding: 30px.
- Element gap: 20px.

Build these component patterns where relevant:

- Primary CTA Button: Single conversion action on the page
- Secondary Filled Button: Lower-emphasis dark action paired with the primary CTA
- Top Navigation Bar: Persistent site header
- Nav Dropdown Link: Center-section menu items with sub-navigation
- Display Heading: Hero-level headline (homepage/marketing only)
- Section Heading: Page-title and sub-section labels
- Body Text Block: Paragraph copy and legal prose
- Bulleted List: Enumerated constraints and requirements
- Inline Text Link: Reference links within body copy
- Date/Metadata Label: Secondary status line under page title
- Brand Logo: Wordmark in nav

Do:

- Use Inter exclusively across the entire interface; never substitute a second typeface family
- Set border-radius to 8px on every rounded element - buttons, cards, nav containers, tags all share the same radius for a unified geometric language
- Reserve the violet gradient (linear-gradient(129deg, #6100ff, #9d50ff)) for the single primary CTA per screen; never duplicate it
- Use weight 900 only at the display size (83px); weights 400 and 700 cover everything else
- Apply negative letter-spacing at every size: -0.17px at 14px scaling to -3.24px at 83px
- Build vertical rhythm from the 6px base unit: 30px for card padding, 60px for section gaps, 20px between inline elements
- Keep the page background pure #ffffff; the system has no tinted canvas variants

Avoid:

- Do not introduce a second chromatic accent - the system is monochromatic plus one violet, and adding red/green/blue/yellow breaks the drafting-tool identity
- Do not use weight 900 for body, labels, or section headings; it is loud and will flatten the hierarchy
- Do not add drop shadows, glows, or blur effects - the design language is flat; elevation comes from background tone, not shadow
- Do not use #6100ff on decorative icons, tags, illustrations, or non-action UI - the violet earns its place by being scarce
- Do not use #313131 as a page or card background; it is a nav-level surface only
- Do not set letter-spacing to 0 or positive values - the system always tightens, even at 14px body size
- Do not place violet text on a violet gradient background; the gradient already carries the brand and needs white text for contrast

Source prompt cues:

Quick Color Reference:
- text: #252525
- background: #ffffff
- muted text: #595959 / #949494
- primary action: no distinct CTA color
- dark surface: #252525

Example Component Prompts:
No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.
2. Create a secondary dark button: #252525 background, 14px Inter weight 700, white text, 8px border-radius, padding 12px 24px.
3. Create a display heading: 83px Inter weight 900, #252525, line-height 1.0, letter-spacing -3.24px. Use once per page maximum.
4. Create a section heading: 26px Inter weight 700, #252525, line-height 1.09, letter-spacing -0.88px.
5. Create a body text block: 18px Inter weight 400, #595959, line-height 1.40, letter-spacing -0.45px, on #ffffff background.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
