# Peak Design - Style Reference

> Gallery wall, half lit.

Theme: light

Peak Design is a premium commerce style where product photography and editorial typography carry almost the entire experience. The interface alternates between crisp white commerce sections and deep near-black editorial panels. The most recognizable pattern is a split hero: one side holds a dark typographic story block, and the other side holds a full-bleed product or lifestyle image.

The system feels engineered rather than decorated. There are no chromatic button fills, decorative gradients, or shadows. Structure comes from hairline dividers, strict corner radii, uppercase condensed labels, and generous whitespace. Ember Red appears only as a rare emphasis, not as the default CTA color.

## Tokens - Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Carbon Ink | `#1a211e` | `--color-carbon-ink` | Primary text, dark hero panels, icons, and borders on light surfaces. |
| Paper White | `#ffffff` | `--color-paper-white` | Main commerce canvas, product grids, and light sections. |
| True Black | `#000000` | `--color-true-black` | Maximum contrast elements, announcement bars, and sharp icon strokes. |
| Obsidian | `#0c0c0c` | `--color-obsidian` | Deep panel surfaces and dark editorial split sections. |
| Fog | `#eef1f0` | `--color-fog` | Subtle input and secondary component backgrounds. |
| Mist | `#e0e0e0` | `--color-mist` | Divider lines, disabled states, and structural separators. |
| Graphite | `#606562` | `--color-graphite` | Muted body text, metadata, and secondary navigation. |
| Ash Border | `#cccfcd` | `--color-ash-border` | Hairline input borders and soft pencil-line dividers. |
| Slate | `#363537` | `--color-slate` | Navigation text and mid-weight borders. |
| Pewter | `#4e4e4e` | `--color-pewter` | Supporting neutral, secondary UI, and badge fills. |
| Ember Red | `#cc2e39` | `--color-ember-red` | Rare sale, urgency, or brand punctuation accent. |

## Tokens - Typography

### Geist

Neutral grotesque for functional readability.

- Substitute: Inter, Sohne, Helvetica Neue, system-ui, sans-serif
- Weights: 400, 600, 700
- Sizes: 14px, 16px
- Line height: 1.0 to 1.5
- Role: body copy, product titles, descriptions, form inputs, link text, and footer content
- Rule: use 400 for normal body, 600 or 700 only for product names and inline emphasis.

### Exposure-Style Serif

Display serif for editorial moments.

- Substitute: Playfair Display, GT Super, Tiempos Headline, Georgia, serif
- Weight: 400
- Sizes: 40px, 48px, 80px
- Line height: 1.10
- Letter spacing: about -0.025em at 40px to 80px
- Role: hero and section-display headlines only
- Rule: never use this for body, navigation, inputs, or small UI.

### Bryant-Style Condensed Sans

Compressed uppercase label voice.

- Substitute: Druk Wide, Inter Display Bold, Neue Haas Grotesk Display Bold, sans-serif
- Weight: 700
- Sizes: 14px, 16px, 24px, 32px
- Line height: 1.10 to 1.40
- Letter spacing: positive tracking around 0.038em to 0.057em
- Role: nav labels, category filters, button text, eyebrows, section tags, and secondary headings
- Rule: always uppercase. Do not use mixed case.

### Geist Mono

Technical micro-data face for SKUs, specifications, and small aligned labels.

- Substitute: JetBrains Mono, IBM Plex Mono, monospace
- Weight: 400
- Size: 14px
- Line height: 1.0

### Type Scale

| Role | Size | Weight | Line Height | Tracking | Font |
| --- | --- | --- | --- | --- | --- |
| caption | 14px | 400 | 1.0 | 0 | Geist |
| button-label | 16px | 700 | 1.1 | 0.91px | Bryant-style |
| heading-sm | 24px | 700 | 1.2 | 0.91px | Bryant-style |
| heading | 32px | 700 | 1.2 | 0 | Bryant-style |
| heading-lg | 48px | 400 | 1.1 | -1.2px | Exposure-style |
| display | 80px | 400 | 1.1 | -2px | Exposure-style |

## Tokens - Spacing And Shape

- Density: comfortable
- Base unit: 4px
- Page max width: 1440px
- Section gap: 80px
- Card padding: 24px
- Element gap: 24px
- Scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64px

### Radius

| Element | Value |
| --- | --- |
| Navigation | 4px |
| Inputs | 4px |
| Buttons | 4px |
| Cards | 8px |
| Images | 8px |
| Rounded buttons | 32px |
| Badges and filter pills | 9999px |

### Elevation

Do not use shadows. Separation is handled by:

- White and near-black section contrast.
- 1px hairline borders in `#e0e0e0` or `#cccfcd`.
- Product image radius.
- Whitespace between cards.

## Components

### Announcement Bar

Full-width dark strip around 32px tall. Use white uppercase Bryant-style text at 14px with positive tracking. Keep content centered and utility-focused: shipping, warranty, returns, store finder, or mission links.

### Primary Navigation

White header around 64px tall with a hairline bottom border. Use the logo at left, uppercase category links, a full search field, and icon-only account/cart controls. No shadow, no tinted nav background, no decorative hover block.

### Category Filter Bar

Horizontal row of pill chips below nav. Active chip uses Carbon Ink fill with white uppercase text. Inactive chips are transparent with Ash Border and Slate text. Include overflow arrows when needed.

### Product Card

White background, no visible border, no shadow. Product image sits at the top with 8px radius and usually 1:1 aspect. Below the image, stack title, variant or brand label, and price in Geist. Use whitespace instead of containers.

### New Badge

Small pill over the product image. Use Pewter fill, white uppercase Bryant-style text, compact padding, and 9999px radius.

### Hero Split Panel

Full-width 50/50 section. One side is a deep Carbon Ink or Obsidian text panel with uppercase eyebrow, Exposure-style serif headline, short Geist copy, and button pair. The other side is a full-bleed product or lifestyle image flush to the viewport edge.

### Filled Button On Dark

White fill, Carbon Ink text, 4px radius, 12px by 20px padding, uppercase Bryant-style label. It should feel like a hard contrast block, not a soft pill.

### Outlined Button On Dark

Transparent fill, white 1px border, white uppercase Bryant-style text, 4px radius, 12px by 20px padding. Use as a secondary action inside dark panels.

### Ghost Button On Light

No background, no border, uppercase Bryant-style text in Carbon Ink. Use for low-emphasis commerce links.

### Carousel Pagination Dots

Small dot row below product carousels. Active dot is a short Carbon Ink pill. Inactive dots are Ash Border circles.

### Search Field

Fog fill, Ash Border, 4px radius, 40px height, 14px Geist placeholder in Graphite, and a simple search icon. It belongs in the nav, not as a hero centerpiece.

### Section Heading Block

Large left-aligned Exposure-style headline in Carbon Ink, 48px to 80px, tight tracking, and optional short terminal mark. Use at the top of content or carousel sections.

### Navigation Icon Button

Icon-only button with no fill or border. Use 20px to 24px line icons, 1.5px stroke, Carbon Ink color, and a small clickable hit area.

## Layout

Use full-bleed sections that alternate between white and deep near-black. Section containers can be full width, while content inside maxes out near 1440px. The dominant hero is a 50/50 split with text on one side and image on the other.

Product grids usually use 4 equal columns with 24px to 32px gaps. Category filters sit directly beneath the nav. The rhythm should feel like an editorial product magazine: light band, dark band, light product grid, dark split panel.

## Imagery

Product photography is the hero. Use studio-grade images of bags, slings, camera gear, and hardware on pure white backgrounds. Show material texture and construction details. Lifestyle images appear only in full-bleed editorial panels.

Avoid illustrations, abstract graphics, 3D renders, decorative icon art, and generic lifestyle stock. In hero contexts, images are flush to the section edge with no radius. In card contexts, images use 8px radius.

## Do

- Use the Exposure-style serif only for display headlines at 48px and above.
- Use Geist 400 at 16px with 1.5 line height for body copy.
- Use Bryant-style condensed uppercase labels for nav, buttons, filters, and eyebrows.
- Alternate white and near-black full-bleed sections.
- Keep cards and product images at 8px radius.
- Keep buttons and inputs at 4px radius.
- Use 9999px only for badges and filter pills.
- Use Ember Red only once per viewport for special emphasis.
- Keep product cards borderless and shadowless.

## Do Not

- Do not introduce colored UI backgrounds for buttons, cards, or panels.
- Do not add box shadows or drop shadows.
- Do not use the serif for body or UI text.
- Do not set Bryant-style text in mixed case.
- Do not place Ember Red on repeated elements.
- Do not use radii above 8px on cards or images.
- Do not center-align product descriptions.

