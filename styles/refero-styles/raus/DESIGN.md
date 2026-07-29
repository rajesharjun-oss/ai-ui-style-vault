# Raus Style Reference

## North Star

Raus feels like a digital cabin booking ledger laid over a folded trail map. It is warm, grounded, and quietly organized. The system should help users choose a place to escape without feeling like a generic travel marketplace.

The visual signature is a warm paper canvas, rounded cabin cards, topographic map panels, forest-green markers, and a single campfire-ochre action color. It should feel outdoorsy, calm, and trustworthy.

## Color

The palette is earthy and restrained:

- `Charcoal Ink` `#25231f`: primary text, headings, dark UI, and high-contrast map labels.
- `Warm Paper` `#f7f4ed`: page canvas and main warm background.
- `Pure White` `#ffffff`: elevated cards, nav surfaces, modal surfaces, and high-contrast interiors.
- `Parchment Border` `#e8e0d2`: hairline borders, input outlines, and card separators.
- `Stone Gray` `#8f887d`: secondary text, metadata, helper copy.
- `Campfire Ochre` `#c98a3f`: primary booking CTA, price/action highlights, warm active state.
- `Forest Green` `#1f4f3a`: map markers, nature icons, selected location accents.
- `Sand` `#d8c6a3`: map panels, contour-line backgrounds, muted outdoor washes.
- `Linen Wash` `#f1ece3`: muted section bands, input fills, nested panels.
- `Taupe` `#b7a98d`: disabled states, tertiary labels, inactive map detail.

Do not use generic hotel-booking blue. Do not make ochre a broad background. Ochre works best as the booking action and small emphasis.

## Typography

Use Inter or a close system sans-serif for the whole interface. The typography is quiet, legible, and functional rather than decorative.

Recommended roles:

- Micro: 12px, 500, line-height 1.33.
- Small UI: 14px, 500, line-height 1.43.
- Body: 16px, 400, line-height 1.6.
- Lead: 18px, 400, line-height 1.55.
- Card title: 24px, 600, line-height 1.25, letter-spacing -0.01em.
- Section heading: 40px, 600, line-height 1.1, letter-spacing -0.03em.
- Hero: 64px, 600, line-height 0.95, letter-spacing -0.05em.

Use ui-monospace sparingly for map coordinates, grid references, or technical location annotations.

## Layout

The layout should feel like booking logic joined with a map:

- Centered max width around 1200px.
- Warm Paper page canvas.
- Top navigation with simple text links and a booking CTA.
- Hero or search area with a map panel and stay/booking controls.
- Map/list split for browsing destinations.
- Cabin cards in a grid or list.
- Sticky or right-side booking panel for date, guests, and price.
- Editorial sections with nature imagery and soft card stacks.

Keep major sections around 96px apart. Use 16px element gaps, 24px to 32px card padding, and a 360px booking panel width when a side panel is present.

## Shape And Elevation

Raus uses soft, natural geometry:

- Cards: 20px.
- Booking card: 24px.
- Buttons: 9999px.
- Inputs: 12px.
- Map markers: 9999px or 40px circles.

Elevation should be subtle, warm, and paper-like:

```css
0 20px 50px -24px rgba(37, 35, 31, 0.08)
```

Map marker shadow:

```css
0 8px 20px -8px rgba(37, 35, 31, 0.25)
```

Do not use glossy SaaS shadows or heavy dark overlays.

## Components

### Header Navigation

Use a Pure White or transparent warm-paper nav, about 72px tall. Text links use Charcoal Ink or Stone Gray. The primary action is a Campfire Ochre pill.

### Primary CTA Pill

Campfire Ochre fill, Pure White text, 9999px radius, 14px/600, 12px 20px padding. Use for booking, reserve, or search actions.

### Outline Pill Filter

Transparent or Pure White fill, Parchment Border outline, Charcoal Ink text, and pill shape. Selected state can use Charcoal Ink fill with Pure White text.

### Location Card

Warm Paper or Pure White surface, 20px radius, cabin image, price pill, location metadata, and subtle shadow. Use rounded images and calm spacing.

### Booking Panel

Pure White surface, 24px radius, 1px Parchment Border, 32px padding, date selectors, guest controls, price details, and one ochre CTA.

### Map Marker Button

40px circle or compact pill, Forest Green or Charcoal Ink fill, Pure White icon/text, and marker shadow. Use for selected locations and cabin pins.

### Topographic Map Panel

Sand or Linen Wash background, soft contour lines, muted map labels, Forest Green markers, and 24px radius. It should feel custom, not like default map tiles.

### Date Input

Pure White or Linen Wash fill, Parchment Border, 12px radius, 14px text, and calm focus state.

### Editorial Card

Warm Paper surface, 20px radius, nature photo or cabin detail, short copy, and low-contrast border.

## Imagery

Use real cabin photography, nature scenes, trail-map linework, terrain textures, map pins, booking cards, and route/location diagrams. Avoid generic hotel stock photos, city imagery, loud travel gradients, or default Google Maps styling.

## Do

- Use Warm Paper as the page canvas.
- Use Charcoal Ink for primary text.
- Use Campfire Ochre for the single main booking action.
- Use Forest Green for map markers and outdoor accents.
- Use rounded cabin cards and booking panels.
- Use topographic or trail-map cues.
- Keep photography natural, quiet, and product-relevant.

## Do Not

- Do not use generic travel blue.
- Do not introduce neon or saturated accent colors.
- Do not use hard black as the main text color.
- Do not make map panels look like default map embeds.
- Do not use glossy hotel marketplace cards.
- Do not use sharp cards or square CTAs.
- Do not crowd the layout with dense tables.
