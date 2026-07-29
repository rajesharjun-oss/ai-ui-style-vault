# Supahub Design Reference

## North Star

Build a friendly, sunlit SaaS feedback platform. The interface should feel approachable, rounded, and product-led: white canvas, vivid violet action, soft lavender/pink/amber atmosphere, floating product previews, and testimonial walls that feel like social proof wallpaper.

The style borrows energy from consumer apps, but keeps the hierarchy and text clarity of a serious SaaS product.

## Theme

- Mode: light.
- Canvas: white.
- Primary action: vivid violet.
- Support surfaces: fog, lavender, mint, and white cards.
- Text: midnight ink.
- Geometry: rounded and friendly.
- Atmosphere: gradient orbs behind mockups.

## Color System

Core colors:

- Voltage Violet: `#862fe7` for primary CTAs, active nav, key accent text, and high-emphasis badges.
- Ultra Violet: `#5f259e` for hover states, deeper gradient stops, and emphasis text.
- Lavender Mist: `#ad6df4` for decorative violet tints, icon fills, and gradient mid-stops.
- Orchid Wash: `#bd8ff0` for soft decorative violet surfaces.
- Magenta Spark: `#ff5fe4` for pink washes and highlights, not primary actions.
- Hot Pink Ray: `#e22ba4` for saturated pink gradient stops.
- Amber Pulse: `#dc5f05` for warm gradient counterpoint.
- Midnight Ink: `#111827` for primary headings, body text, dark buttons, and strong borders.
- Graphite: `#3f4654` for secondary text and muted UI.
- Slate: `#6b7589` for tertiary text, helper copy, icons, and metadata.
- Pure White: `#ffffff` for the main canvas, cards, button text, and product surfaces.
- Fog: `#f1f5f9` for alternate section backgrounds.
- Mist: `#d8e0ea` for hairline borders, inputs, focus rings, and dividers.
- Mint Wash: `#d6fcf4` for soft highlighted panels and badges.
- Lavender Field: `#ebdafd` for feature bands and soft emphasis blocks.

Only Voltage Violet should carry primary action weight.

## Typography

Display and heading family: Bricolage Grotesque.  
Body and UI family: Inter.

Bricolage Grotesque:

- Used for hero headlines, section headlines, and emphasized display copy.
- Keep it at 20px and above.
- Use 48-56px for hero and major sections.
- Use 32px for section headings.
- Use weight 600 for emphasis and weight 400 for calmer display text.
- Tighten large text with around -0.025em tracking.

Inter:

- Used for nav, buttons, body copy, captions, testimonials, metadata, and dense UI.
- Use 12px uppercase labels with 0.1em tracking.
- Use 14-16px for most interface and body text.
- Use 18-20px for larger supporting paragraphs.

Type scale:

- Caption: 12px, line-height 1.5, letter-spacing 1.2px.
- Body small: 14px, line-height 1.6.
- Body: 16px, line-height 1.75.
- Subheading: 20px, line-height 1.5.
- Heading small: 24px, line-height 1.3, letter-spacing -0.6px.
- Heading: 32px, line-height 1.2, letter-spacing -0.8px.
- Display: 56px, line-height 1.0, letter-spacing -1.4px.

## Layout

- Page max width: 1200px.
- Display text column: 680-720px.
- Base unit: 4px.
- Hero: centered or left-aligned inside a constrained column.
- Hero copy: short, with CTA pair below.
- Feature band: full-width lavender or fog section with two-column content.
- Product preview: floating white mockup with gradient orb behind it.
- Testimonial wall: repeated rounded cards.
- Social proof: overlapping circular avatars plus stars.

Do not let the display headline stretch across the full 1200px container. The line breaks are part of the brand voice.

## Shape

- Nav: 8px radius.
- Buttons: 12px radius.
- Images and product previews: 16px radius.
- Cards: 24px radius.
- Featured card: 40px radius.
- Pills, avatars, tags, badges: 9999px radius.

The rounded geometry should feel friendly and tactile, not toy-like.

## Elevation

Avoid a broad shadow system. Use depth through:

- Violet button inset ring.
- One soft shadow on floating product preview cards.
- Surface color contrast between white, fog, lavender, and mint.
- Hairline borders.

Cards should not look like they lift on hover by default.

## Gradient Atmosphere

Gradient orbs are signature decorative atmosphere:

- Violet orb: transparent to violet at 0.3-0.4 opacity and back to transparent.
- Pink orb: transparent to pink at around 0.3 opacity and back to transparent.
- Amber orb: transparent to amber at around 0.4 opacity and back to transparent.

Place orbs behind product mockups. Do not put them behind text or buttons.

## AI Build Notes

Start with a white page, a constrained Bricolage headline, one violet CTA, and a product preview with a violet orb behind it. Add testimonial cards and avatar social proof after the core product story is clear.

