# AI Implementation Prompt

Build a Monzo-inspired interface using this source-derived style bundle.

Reference site: https://monzo.com
Theme: light
Category: Fintech
North star: Warm coral on cool mint paper - confident restraint with a single hot accent.

Use these palette anchors:

- Hot Coral `#ff4f40` for Brand signature - logo, links, headings, icons, card product. One vivid accent against the achromatic interface; every chromatic moment in the system draws from this single hue
- Midnight Ink `#091723` for Dark supporting neutral for text, icons, and strong contrast. Do not promote it to the primary CTA color
- Deep Navy `#112231` for Secondary surface tint and footer accents. Slightly lighter than Midnight Ink for layered dark elements
- Page Mist `#f2f8f3` for Page canvas - the dominant background behind all content sections. A barely-green off-white that gives the interface warmth without competing with white surfaces
- Pure White `#ffffff` for Card surfaces, elevated panels, button text on dark fills. Sits one layer above the mint canvas
- Soft Mint `#e3ebe4` for Hover washes, subtle filled buttons, inset surface treatment. Sits between the page canvas and white cards
- Fog `#b5b9bd` for Tertiary text, placeholder, low-emphasis borders
- Steel `#6b747b` for Secondary body text, metadata, descriptive copy. The workhorse neutral for supporting information
- Ash `#75817e` for Icon strokes, decorative line work, subtle dividers
- Slate Button `#3b4c54` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color
- Pure Black `#000000` for Maximum-contrast text, the darkest token in the system. Used sparingly for the highest-emphasis text on light surfaces

Use these typography anchors:

- MonzoSansText `--font-monzosanstext` for Body and UI text - navigation labels, button copy, descriptive paragraphs, card content, footer text. The custom -0.05em letter-spacing tightens running text for a dense, modern feel; the 400/600/700 spread lets the same family handle everything from captions to subheadings. Substitute with Inter or DM Sans if unavailable.
- MonzoSansDisplay `--font-monzosansdisplay` for Headlines and display text - hero statements, section headings, large product titles. Bolder weights (up to 800) at large sizes (39-61px) create confident, blocky headlines that feel architectural. No custom letter-spacing, letting the weight do the work. Substitute with Inter or Manrope at heavy weights.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 64-80px.
- Card padding: 30-32px.
- Element gap: 24px.

Build these component patterns where relevant:

- Pill Nav Toggle: Segment-style personal/business selector in the top bar
- Sign Up CTA (Dark Pill): Primary dark action in the top-right navigation
- White Pill CTA: Light-on-image call-to-action over the hero carousel
- Category Link List: Expandable topic links in the help/footer navigation panel
- Carousel Card: Full-width hero image slider
- Product Card: Showcase for a banking product (current account, savings, etc.)
- Which? Badge: Third-party endorsement / trust signal
- FSCS Badge: Regulatory trust mark
- Arrow Control (Circular): Carousel pagination buttons
- Fixed Bottom Search Bar: Persistent help/search input docked at the viewport bottom
- Sticky Top Bar: Global navigation header
- Menu Label: Bold category heading in the expandable navigation panel

Do:

- Use 500px border-radius for all interactive pills - buttons, nav toggles, tag chips, and the search bar. This is the system's defining shape.
- Keep the interface 95% achromatic. Let Hot Coral (#ff4f40) appear only on the logo, links, headings, icons, and the card product - never as a background fill for UI controls.
- Use MonzoSansDisplay 600-800 for all headings at 36px and above. The heavier weight range is non-negotiable for display type.
- Apply -0.05em letter-spacing to all MonzoSansText usage. This is a brand-defining typographic detail, not optional.
- Layer surfaces on the mint canvas (#f2f8f3 #ffffff #e3ebe4) instead of using shadows. Elevation is communicated by color stepping, not by drop shadows.
- Set body text at 20px with 1.4 line-height for descriptive paragraphs. Monzo's text size runs larger than typical SaaS - 16px is the floor, not the default.
- Use 64px border-radius on all large containers - hero cards, product showcases, section panels. This generous rounding is as recognizable as the coral.

Avoid:

- Don't use Hot Coral as a button background fill. It is for text, icons, logos, and the card product only - never for a solid CTA surface.
- Don't add drop shadows to cards or buttons. The system uses a single rgba(0,0,0,0.1) 0px 0px 10px shadow sparingly; most separation comes from surface color stepping on the mint canvas.
- Don't use system fonts or non-brand sans-serifs. Always specify MonzoSansText for body and MonzoSansDisplay for headings.
- Don't use letter-spacing other than -0.05em on MonzoSansText or normal on MonzoSansDisplay. Deviating breaks the brand's typographic fingerprint.
- Don't mix red and dark navy as a gradient or color pair on the same element. Coral is the accent; navy is the ground. They alternate, they don't blend.
- Don't use square or 8px radii on primary buttons or large containers. 500px pills and 64px containers are the two shape languages - anything between looks generic.
- Don't set body text below 16px or headlines below 32px. The type scale is deliberately generous; small text breaks the warm, spacious feel.

Source prompt cues:

**Quick Color Reference**
- text: #091723 (Midnight Ink)
- background: #f2f8f3 (Page Mist mint canvas)
- surface: #ffffff (white card)
- border: #e3ebe4 (Soft Mint hairline)
- accent: #ff4f40 (Hot Coral - links, headings, icons, logo only)
- primary action: no distinct CTA color

**Example Component Prompts**

1. **Sticky Top Bar**: Transparent background, 72px height. Monzo wordmark logo in #ff4f40 on the left. Center-left: pill segment toggle with 500px radius, 8px/16px padding, #f2f8f3 active fill, MonzoSansText 16px weight 600 in #091723. Right: dark pill button - #091723 fill, white text, 500px radius, 12px/24px padding, MonzoSansText 16px weight 600.

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

3. **Category Link List**: Full-width panel on #f2f8f3 background. Each row: MonzoSansDisplay 32px weight 700 in #ff4f40, 60-72px row height, 1px bottom border in #e3ebe4. No icons, no backgrounds - pure typographic navigation.

4. **Product Showcase Row**: Two-column layout on #f2f8f3 canvas. Left: Hot Coral card image (flat red rectangle, 200px wide, 64px radius). Right: 500px padding-left gap. MonzoSansDisplay 36px weight 700 in #091723 heading, MonzoSansText 20px weight 400 in #6b747b body text. Circular arrow controls (40px, 1.5px stroke #091723) above the heading.

5. **Floating Bottom Search Bar**: Fixed to viewport bottom, 56px height, full width minus 40px margins, 64px radius, #ffffff fill, rgba(0,0,0,0.1) 0px 0px 10px 0px shadow. Left edge: 2px #ff4f40 accent stripe. Placeholder: MonzoSansText 16px weight 400 in #6b747b.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
