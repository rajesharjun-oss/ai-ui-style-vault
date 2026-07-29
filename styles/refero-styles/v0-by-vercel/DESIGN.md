# v0 by Vercel Style Reference

## North Star

v0 feels like a functional schematic on a stark white drafting table. It is not trying to charm through decoration. It is trying to make the user input feel like the center of the product.

The visual language is achromatic, spacious, and utility-first. The only meaningful hierarchy comes from type, spacing, borders, filled versus outlined actions, and the large prompt input.

## Color

The palette is deliberately narrow:

- `Paper White` `#ffffff`: card surfaces, pill button backgrounds, and text on dark buttons.
- `Canvas` `#fafafa`: primary page background.
- `Line` `#eaeaea`: borders for headers, ghost buttons, chips, inputs, and dividers.
- `Subtext` `#666666`: secondary text, navigation links, placeholder text.
- `Icon` `#7d7d7d`: inactive icons and tertiary UI elements.
- `Ink` `#171717`: primary text, headlines, and primary button backgrounds.
- `Onyx` `#000000`: logo, icons, and maximum-contrast text only.

Do not add saturated UI chrome. Any color should come from user-generated template previews, not navigation, buttons, panels, dividers, or background treatments.

## Typography

Use GeistSans for all text. GeistMono is reserved for tiny technical annotations or aligned stats.

GeistSans guidance:

- Body: 16px, weight 400, normal tracking.
- Small UI: 13px to 14px, weight 400 to 500.
- Buttons: 14px, weight 500.
- Section heading: 24px to 32px, weight 600, negative tracking.
- Display: 48px, weight 600, line-height 1.0, letter-spacing around -2.88px.

Use font features such as `zero`, `ss09`, and `ss05` where available. Avoid 700+ weights. Use 600 weight and larger size for emphasis.

GeistMono guidance:

- 10px, weight 400, line-height 1.5.
- Use for technical annotations, counts, or small aligned metadata.

## Layout

The layout is centered and spacious:

- Full-width header with 1px bottom border.
- Hero as a centered stack: headline, main prompt input, suggestion chips.
- Body sections separated by about 96px of vertical whitespace.
- Content grids such as a 3-column template gallery.
- Generous max-width container around 1440px.

Avoid dense layouts. The page should breathe. Product previews can be shown in grids, but surrounding chrome should remain quiet.

## Shape And Elevation

Allowed radii are strict:

- 6px for small suggestion chips.
- 8px for buttons.
- 12px for cards and prompt inputs.
- 9999px for filter pills only.

Do not invent new radius values. Do not use soft marketing pills everywhere.

Elevation is minimal:

- Buttons and inputs should not use shadows.
- Template cards can use a subtle ring plus tiny shadow.
- Modals and popovers can use a stronger system shadow.

Template card shadow:

```css
0 0 0 1px rgba(0, 0, 0, 0.08),
0 2px 1px rgba(0, 0, 0, 0.04)
```

Modal/popover shadow:

```css
0 25px 50px -12px rgba(0, 0, 0, 0.25)
```

## Components

### Primary CTA Button

Ink background, Paper White text, 8px radius, GeistSans 14px/500, about 8px vertical and 12px horizontal padding.

### Ghost Navigation Link

Transparent background, Subtext text, no border by default, GeistSans 14px/400.

### Prompt Suggestion Chip

Transparent background, 1px Line border, Subtext 13px text, 4px vertical and 8px horizontal padding, 6px radius.

### Filter Pill Button

Pill-shaped button with Paper White background, Ink text, faint 1px black-alpha border, and 9999px radius. Use for content category filters.

### Main Prompt Input

Large input surface with 12px radius, 1px Line border, Subtext placeholder, transparent internal textarea, and a subtle focus glow. It is the primary interaction point.

### Header Divider

Full-width 1px solid Line border separating sticky header from page content.

### Template Card

White card with 12px radius, subtle ring/shadow, and raw product preview content inside. Imagery is confined to the preview.

## Imagery

This style uses no decorative imagery. Visuals are strictly product output previews inside template cards. Do not use gradients, background images, abstract illustrations, mascot graphics, or atmospheric hero media.

## Do

- Use GeistSans for all text.
- Use GeistMono only for tiny technical annotations.
- Use negative tracking for headings 24px and larger.
- Keep the palette achromatic.
- Use 1px Line borders for dividers and structure.
- Use solid fill for primary actions, border for secondary actions, and text-only tertiary links.
- Maintain at least about 96px between major content sections.

## Do Not

- Do not introduce saturated UI colors.
- Do not use system fonts or other brand fonts.
- Do not use shadows on buttons or inputs.
- Do not use gradients or background images.
- Do not use bold 700+ font weights.
- Do not create dense layouts.
- Do not use border radii outside 6px, 8px, 12px, and 9999px.
