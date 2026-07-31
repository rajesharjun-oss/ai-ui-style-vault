# AI Implementation Prompt

Build a Dot Inc.-inspired interface using this source-derived style bundle.

Reference site: https://pad.dotincorp.com
Theme: light
Category: Productivity
North star: white laboratory with a single orange spark

Use these palette anchors:

- Ember Orange `#ff5a2f` for Primary action buttons, active badges, accent borders - the system's only chromatic voice, used to signal interactivity and emphasis
- Ember Orange (link variant) `#f15b2b` for Orange text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color
- Carbon Black `#000000` for Primary text, icons, image overlays, card headings - maximum contrast against white canvas
- Graphite `#1f1f1f` for Headings, body emphasis, dark surface alternative - slightly softened black for large display text
- Slate Dark `#333333` for List items, secondary body text, card content
- Stone `#555555` for Navigation labels, subdued body text
- Pewter `#707070` for Muted descriptions, inactive list items, heading borders
- Steel `#a5a5a5` for Disabled or decorative text
- Mist `#b7bfc1` for Card borders, subtle button shadows - cool-tinted gray that defines container edges
- Cloud `#cbcbcb` for Alternate card backgrounds, disabled surfaces
- Fog `#dddddd` for Neutral secondary button fill, placeholder surfaces
- Paper `#e5e7eb` for Hairline dividers, borders across all contexts - the structural neutral that separates sections
- Pearl `#f5f5f5` for Card surfaces, subtle backgrounds, alternate section bands
- Canvas White `#ffffff` for Page background, nav surface, card fill, button text - the dominant canvas

Use these typography anchors:

- Plus Jakarta Sans `--font-plus-jakarta-sans` for Sole typeface for all text - body, headings, nav, buttons, badges, icons. The wide weight range (300-800) carries the entire visual hierarchy; display sizes reach 80px at weight 300 for a light, expansive headline, while UI text sits at 14-16px weight 400-500

Use these layout rules:

- Base spacing: 4px.
- Density: spacious.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 40px.
- Element gap: 24px.

Build these component patterns where relevant:

- Primary CTA Button (Ember Fill): Main call-to-action - 'Find a Reseller' style
- Secondary Ghost Button: Companion action - 'Request a Demo' style
- Neutral Pill Button: Tertiary or disabled action
- Bordered Card: Product content container
- Shadowed Card (elevated): Featured product showcase
- Hero Banner: Full-width dark product showcase strip
- Section Heading: Page section title
- Badge (Ember Outline): Tag or category label
- Top Navigation Bar: Site-wide primary navigation
- Breadcrumb: Page location indicator
- Rounded Image Container: Product photography frame
- Text Link: Inline hyperlink

Do:

- Use #ff5a2f exclusively for primary action buttons and active state accents - it should appear on no more than 3-5 elements per viewport.
- Set border-radius to 20px for cards and images, 30px for buttons and badges, and 12-20px for inline images.
- Use Plus Jakarta Sans weight 300 or 400 for headlines 40px and above to maintain the light, spacious typographic feel.
- Apply 1px #e5e7eb borders for all card and section dividers - never use heavier borders or decorative lines.
- Space sections with 80px vertical gaps and use 24px for inter-element gaps within cards and lists.
- Keep backgrounds white (#ffffff) as the default canvas; use #f5f5f5 only for alternating content bands or subtle card elevation.
- Reserve the shadow token rgba(0,0,0,0.25) 0px 4px 10px 0px for the single primary CTA button per view.

Avoid:

- Do not introduce additional chromatic colors - the system's identity depends on the 2% colorfulness ceiling.
- Do not use border-radius below 8px for any interactive element; the soft, rounded geometry is a core brand trait.
- Do not apply shadows to cards, images, or navigation - only the primary CTA may have elevation.
- Do not use #000000 for body text at sizes above 20px; switch to #1f1f1f for large headings to avoid harshness.
- Do not use bold (weight 700-800) for body or heading text - reserve weights 700-800 for short labels or tags only.
- Do not create flat hard-edged rectangular blocks; every container needs 20-30px radius.
- Do not use gradients - the system is entirely flat with single solid color fills.

Source prompt cues:

**Quick Color Reference**
- Text: #1f1f1f (headings) / #333333 (body) / #707070 (muted)
- Background: #ffffff (page) / #f5f5f5 (cards)
- Border: #e5e7eb (hairline) / #b7bfc1 (card outline)
- Accent: #ff5a2f (Ember Orange - CTA fill, badges, active states)
- primary action: #ff5a2f (filled action)

**Example Component Prompts**
1. Build a primary CTA button: 30px border-radius, #ff5a2f background, white text, Plus Jakarta Sans 16px weight 500, padding 14px 24px, shadow rgba(0,0,0,0.25) 0px 4px 10px 0px. Use as 'Find a Reseller'.
2. Build a product hero banner: full-bleed dark photographic background, centered white headline at 50px Plus Jakarta Sans weight 300, white subtext at 18px weight 400, container border-radius 20px.
3. Build a bordered content card: white background, 1px #e5e7eb border, 20px border-radius, 40px padding, internal gap 24px between child elements.
4. Build an accent badge: transparent background, 1px #ff5a2f border, #ff5a2f text, Plus Jakarta Sans 12px weight 500, padding 4px 14px, border-radius 20px.
5. Build a secondary ghost button: transparent background, #333333 text, no border, 30px border-radius, padding 14px 24px, Plus Jakarta Sans 16px weight 500. Use as 'Request a Demo'.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
