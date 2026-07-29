# Superr Style Reference

## Summary

Superr is a warm schoolyard notebook system: cream paper, leather notebooks, sticker labels, colored pencils, marker-orange handwriting, and chunky lowercase display type. It feels tactile and slightly mischievous, like a product page made from desk objects.

The page should be object-led. Real product photography does the visual work. Stickers and hand-drawn arrows add personality, but they are decorative punctuation, not a system icon set.

## Theme

Light.

## Personality

- Warm
- Tactile
- Schoolyard
- Playful
- Object-led
- Hand-labeled
- Matte
- Slightly mischievous

## Color System

The palette is warm and paper-like. Marker Orange is the only functional accent. Sticker colors are reserved for illustrations and should not enter buttons, links, or structural UI.

| Name | Value | Token | Use |
| --- | --- | --- | --- |
| Cream Paper | `#fdfbf9` | `--color-cream-paper` | Page canvas, card surfaces, button fills |
| Dew Drop | `#f7efe9` | `--color-dew-drop` | Secondary surface tint and warmer card layer |
| Cocoa Ink | `#2b1a07` | `--color-cocoa-ink` | Headlines and decorative borders |
| Charcoal | `#171717` | `--color-charcoal` | Text, borders, button strokes, structural edges |
| True Black | `#000000` | `--color-true-black` | Highest-emphasis headline moments and hard edge cases |
| Shadow Mist | `#bebcbb` | `--color-shadow-mist` | Soft shadow base |
| Marker Orange | `#ff6f1e` | `--color-marker-orange` | Handwritten captions, inline highlights, footer band |
| Burnt Sienna | `#ce500a` | `--color-burnt-sienna` | Darker orange for accent borders or text when needed |
| Sky Sticker | `#3b82f6` | `--color-sky-sticker` | Decorative sticker color only |
| Bubblegum Sticker | `#ff66cf` | `--color-bubblegum-sticker` | Decorative sticker color only |
| Sprout Sticker | `#22c55e` | `--color-sprout-sticker` | Decorative sticker color only |

## Typography

Gelica owns the display, headings, and most body copy. Geist is a supporting grotesque used sparingly for nav, captions, and UI labels.

| Role | Font | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- | --- |
| Display | gelica | 104px | 600 | 1.08 | normal |
| Heading Large | gelica | 46px | 400 | 1.2 | normal |
| Heading | gelica | 36px | 400 | 1.2 | normal |
| Heading Small | gelica | 28px | 400 | 1.4 | normal |
| Subheading | gelica | 24px | 400 | 1.4 | normal |
| Body | gelica | 20px | 500 | 1.5 | normal |
| Body Small | Geist | 18px | 400 | 1.5 | normal |
| Caption | gelica | 16px | 400 | 1.5 | normal |

## Font Rules

- Use lowercase for display headlines.
- Do not add letter spacing.
- Use gelica for all display and headline work.
- Use Geist only for supporting labels and cleaner UI moments.
- Keep display headlines no longer than three lines.
- After the first line, avoid centered headline stacks; keep the hand-notebook rhythm left-aligned.

## Spacing And Shape

- Base unit: 4px
- Density: comfortable
- Page max width: 1200px
- Section gap: 64px
- Card padding: 32px
- Element gap: 12px
- Inputs: 8px radius
- Cards: 12px radius
- Buttons: 20px radius
- Tags: 20px radius
- Footer top edge: 56px radius

## Shadows

Use extremely light paper-lift shadows only:

```css
--shadow-card: rgba(0, 0, 0, 0.06) 0 2px 20px 0;
--shadow-button: rgba(0, 0, 0, 0.25) 0 1px 2px 0;
```

Do not use heavier shadows or glossy elevation.

## Surfaces

| Level | Surface | Value | Role |
| --- | --- | --- | --- |
| 0 | Canvas | `#fdfbf9` | Warm cream page background |
| 1 | Surface Tint | `#f7efe9` | Secondary card or panel layer |
| 2 | Brand Band | `#ff6f1e` | Footer accent stripe |

## Components

### Pill Action Button

Cream Paper fill, 1.5px Charcoal border, 20px radius, 28px horizontal padding, 10px to 11px vertical padding, gelica 16px weight 500 Charcoal text, subtle button shadow. The button identity is its border, not a fill color.

### Display Headline

Lowercase gelica 104px, weight 600, line-height 1.08, Cocoa Ink, normal tracking. Treat the headline like a tactile object. Avoid uppercase and tight letter spacing.

### Handwritten Caption

Gelica 20px to 24px weight 400 in Marker Orange. Slightly rotate or align it with a hand-drawn arrow pointing toward a product object.

### Marker Highlight

Inline Marker Orange word or phrase with a rough hand-drawn underline in the same color. Use 2px to 3px stroke.

### Product Notebook

Photographed notebook object, tilted about 5 to 8 degrees, with visible sticker label and colored pencil. Use product photography as the main visual.

### Name Label Sticker

White card with 1px Charcoal border and 8px radius. Include Name, Class, and Roll No fields in handwritten-feeling gelica text.

### Sticker Illustration

Flat sticker characters with 2px dark outlines and vivid fills. Rotate 5 to 15 degrees and place as if physically stuck on the page. Never align them to a grid.

### Hand-Drawn Arrow

Thin 1.5px Charcoal curved arrow with a slight wobble. It connects a handwritten caption to the object it labels.

### Pre-Order Info Block

Small gelica 16px line below the primary button, Cocoa Ink, 8px gap, no icon.

### Footer Brand Band

Full-width Marker Orange band with 56px asymmetric top radius. Use gelica text in Charcoal or cream as the brand closer.

### Top-Left Brand Mark

Small hand or pointing icon in Charcoal, around 32px, placed with about 16px margin. No wordmark beside it.

### Top-Right Action

Persistent pill action button, 16px page margin, same treatment as the main CTA.

## Layout

Use asymmetric editorial layouts. The hero is usually a two-column split:

- Left: giant lowercase headline, handwritten caption, body copy, outlined pill CTA, pre-order line.
- Right: large tilted product notebook photo with sticker illustrations.

Below the fold, alternate product photography blocks and typographic moments. Keep content left-aligned and let product photography occasionally break the 1200px container for spontaneity.

## Imagery

Use real product shots: leather notebooks, cloud-pattern covers, pink covers, colored pencils, sticker labels. Use flat sticker illustrations as secondary personality. Use hand-drawn arrows and marker captions to connect copy with products.

Avoid abstract graphics, 3D renders, stock photos, glass effects, neon, or UI-only mockups.

## Do

- Use gelica 600 at 104px for lowercase display headlines.
- Use Cocoa Ink for headlines.
- Use Marker Orange only for captions, highlights, underlines, and footer band.
- Use Charcoal for text, borders, button strokes, and structure.
- Keep Cream Paper as the canvas.
- Use Dew Drop as a subtle secondary surface.
- Use product photography as the hero.
- Scatter stickers at 5 to 15 degree rotations.
- Use outlined cream pill buttons.

## Do Not

- Do not use sticker blue, pink, or green for functional UI.
- Do not use filled CTA buttons.
- Do not capitalize headlines.
- Do not add letter spacing.
- Do not use heavy shadows.
- Do not center-align multi-line headlines after the first line.
- Do not use gradients, glass, or neon accents.
- Do not use Geist for headlines.
