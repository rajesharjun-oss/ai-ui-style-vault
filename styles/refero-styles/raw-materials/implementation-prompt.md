# AI Implementation Prompt

Build a Raw Materials-inspired interface using this source-derived style bundle.

Reference site: https://therawmaterials.com
Theme: light
Category: Design
North star: brutalist editorial on warm cream

Use these palette anchors:

- Ember Orange `#ff3d00` for Orange supporting accent for decorative details and low-frequency emphasis
- Pulse Violet `#5900cc` for Violet supporting accent for decorative details and low-frequency emphasis.
- Cobalt Blue `#2835f8` for Violet supporting accent for decorative details and low-frequency emphasis.
- Crimson `#ff003d` for Red supporting accent for decorative details and low-frequency emphasis
- Caution Yellow `#ffff00` for Yellow supporting accent for decorative details and low-frequency emphasis.
- Voltage Green `#05ff00` for Green supporting accent for decorative details and low-frequency emphasis
- Electric Blue `#1b73e6` for Headings and body text on cream, mid-saturation blue used in content
- Sky Cyan `#00c2ff` for Headings and accent text, cool counterpoint to warm cream
- Forest `#008163` for Card fills, moderate green for body-level content blocks
- Tangerine `#ff5c00` for Card fills, warm orange variant for content blocks
- Signal Red `#ee2526` for Red supporting accent for decorative details and low-frequency emphasis. Use as a supporting accent, not as a status color
- Ink `#0e0e0e` for Dark supporting neutral for text, icons, and strong contrast.
- Bone Cream `#f4e9e1` for Primary page canvas, nav text on color blocks, card surface
- Paper White `#ffffff` for Active nav card, elevated card surface, input fields
- Charcoal `#242320` for Dark surface fill, image overlays, secondary text on light
- Sage `#cee4cd` for Tinted section background, warm green wash
- Blush `#e4d0cd` for Tinted section background, warm pink wash
- Sand `#e7e4d0` for Tinted section background, warm yellow wash, card fill
- Sky Tint `#cddae4` for Tinted section background, cool blue wash, image-related surfaces
- Celadon `#ddded3` for Tinted section background, muted green wash
- Olive Slate `#444639` for Dark olive section background, secondary text
- Forest Slate `#374936` for Dark green section background, heading text on light
- Cocoa Slate `#4a3937` for Dark warm section background, heading text on light
- Plum Slate `#493648` for Dark purple section background, heading text on light

Use these typography anchors:

- StabilGrotesk `--font-stabilgrotesk` for Workhorse - every nav label, body text, button, badge, card label, and sub-heading up to 46px. The only font that touches interactive UI
- Optimistic Text `--font-optimistic-text` for Large display headlines at 80-193px, sometimes body pull-quote at 23px
- KlarheitKurrent `--font-klarheitkurrent` for The largest display voice - 200-259px hero type, also mid-size editorial headings at 79-107px
- HTQ-Waldenburg-FettSchmal `--font-htq-waldenburg-fettschmal` for Narrow bold display for compressed-impact headlines, the only font using "case" feature
- RightGrotesk `--font-rightgrotesk` for Bold geometric display for 199px poster-scale headlines
- Moderat `--font-moderat` for Wide-tracked display - the +0.084em tracking is a signature, used for all-caps subhead labels
- Courier New `--font-courier-new` for Monospaced system fallback for data tables, tiny index numbers

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: .
- Section gap: 48-80px.
- Card padding: 16-24px.
- Element gap: 8-16px.

Build these component patterns where relevant:

- Numbered Section Nav Card: Primary navigation - each card labels a page section with its index number and title
- Active Section Nav Card: Indicates the section currently in viewport
- Display Headline: Section hero type - the dominant visual on every page section
- Page Header: Persistent top bar - brand identity and tagline
- Scroll Progress Bar: Bottom-of-viewport reading progress indicator
- Color Block Content Card: Content containers in Work, Talent, and case-study sections
- Tinted Section Background: Alternating full-bleed section backgrounds between content blocks
- Pill Tag: Category labels, skill tags, metadata
- Rounded Badge: Index numbers, status indicators, small annotations
- Image Frame: Container for photography in Work and Talent sections
- Ghost Button: Secondary action - 'Read more', 'View project', section transitions
- Body Text Block: Paragraph content, descriptions, bios

Do:

- Use StabilGrotesk for every interactive element and any type below 80px - it's the only font that touches UI controls
- Set all type to feature-settings: 'ss02' - this stylistic alternate is applied to every font on the site and is part of the visual identity
- Lock display headlines to line-height 1.00-1.03 so the type touches itself vertically
- Use 16px radius for all cards, buttons, images, and nav blocks - never mix in 8px or 4px corners
- Assign each page section one of the seven nav colors and carry that color into its content blocks, badges, and accent type
- Let display headlines bleed past their container - do not constrain them to a max-width
- Alternate between cream canvas and one of the five warm tinted backgrounds (Sage, Blush, Sand, Sky, Celadon) to create section rhythm

Avoid:

- Don't add drop-shadows, inner-shadows, or any blur effects - the system is entirely flat
- Don't use a single 'primary' brand color for CTAs - buttons inherit their section's accent color
- Don't set body text below 16px or above 20px - the body range is tight by design
- Don't apply letter-spacing wider than +0.01em to body or subheading text - only the +0.084em Moderat all-caps labels and +0.112em Optimistic uppercase use wide tracking
- Don't introduce a new color outside the seven nav hues and the five tinted washes - the palette is deliberately finite
- Don't use rounded corners smaller than 16px on any container - 4px or 8px corners will read as a different system
- Don't place display headlines centered on the canvas - they are always left-aligned and bleed right

Source prompt cues:

**Quick Color Reference**
- text: #0e0e0e (Ink)
- background: #f4e9e1 (Bone Cream)
- border: #0e0e0e at 1-1.5px
- accent: section-dependent (Ember Orange #ff3d00, Pulse Violet #5900cc, Cobalt Blue #2835f8, Crimson #ff003d, Caution Yellow #ffff00, Voltage Green #05ff00)
- card surface: #ffffff (Paper White)
- primary action: no distinct CTA color

**Example Component Prompts**

1. **Numbered Section Nav Card**: 150px wide, 16px border-radius, fill #ff3d00. Two lines: '01' at 12px StabilGrotesk 400 in #f4e9e1, then 'Hello' at 18px StabilGrotesk 400 in #f4e9e1. 16px horizontal padding, 12px vertical. No shadow.

2. **Display Headline**: 'We are Raw Materials' at 200px KlarheitKurrent 400, #0e0e0e, line-height 1.00, letter-spacing -4px, feature-settings 'ss02'. No max-width - type bleeds right.

3. **Scroll Progress Bar**: Full viewport width, 4px tall, fixed to bottom. Fill #ff3d00. Grows left-to-right with scroll position.

4. **Tinted Section Background**: Full-width band, 80px vertical padding, background #cee4cd (Sage). Contains a 24px StabilGrotesk 400 subheading in #0e0e0e, then 18px body in #0e0e0e at line-height 1.38, max-width 640px.

5. **Ghost Button**: 16px border-radius, 1.5px border #0e0e0e, transparent fill, 12px 20px padding. Text 'View project' at 16px StabilGrotesk 400 in #0e0e0e. On hover: border thickens to 3px, no fill change.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
