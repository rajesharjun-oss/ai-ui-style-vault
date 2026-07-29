# Apple Watch Ultra 3 Style Reference

## Summary

Apple Watch Ultra 3 is a cinematic dark-stage hardware system. The product is the hero: a single titanium object floating in negative space against pure black. Typography, product photography, and surface alternation do almost all the work.

The system alternates black feature stages with white detail bands. Blue is for buying and links. Orange, violet, and teal are category signals, never generic UI decoration.

## Theme

Mixed.

## Personality

- Cinematic
- Premium
- Hardware-first
- Minimal
- Tactile
- Dark-stage
- Precision retail
- Product-led

## Color System

Apple Blue is the only filled chromatic button color. Category colors can label content, but they should not compete with the CTA.

| Name | Value | Token | Use |
| --- | --- | --- | --- |
| Apple Blue | `#0071e3` | `--color-apple-blue` | Primary CTA fill and only filled chromatic button |
| Link Blue | `#0066cc` | `--color-link-blue` | Text links and inline learn-more actions on light surfaces |
| Halo Blue | `#2997ff` | `--color-halo-blue` | Link and accent text on dark surfaces |
| Signal Orange | `#f56900` | `--color-signal-orange` | Category eyebrows and activity labels |
| Iris Violet | `#8668ff` | `--color-iris-violet` | Secondary product-category accent |
| Reef Teal | `#00a1b3` | `--color-reef-teal` | Tertiary product-category accent |
| Pure Black | `#000000` | `--color-pure-black` | Hero and feature stage background |
| Carbon | `#111111` | `--color-carbon` | Subtle elevated dark surface and badge background |
| Obsidian | `#1d1d1f` | `--color-obsidian` | Primary dark canvas and text on light sections |
| Graphite | `#333336` | `--color-graphite` | Secondary surfaces, nav dividers, dark controls |
| Smoke | `#424245` | `--color-smoke` | Hairline borders and low-contrast dividers |
| Platinum | `#86868b` | `--color-platinum` | Muted body text, descriptions, captions |
| Silver Mist | `#cccccc` | `--color-silver-mist` | Nav borders, button outlines, inactive chrome |
| Frost White | `#f5f5f7` | `--color-frost-white` | Text on dark surfaces and soft light section tint |
| Paper White | `#ffffff` | `--color-paper-white` | Light section surfaces and text on filled blue buttons |

## Typography

Use SF Pro Display for headlines and SF Pro Text for everything below headline scale. Negative tracking is part of the identity.

| Role | Font | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- | --- |
| Hero | SF Pro Display | 80px | 600 | 1.05 | -0.24px |
| Display | SF Pro Display | 56px | 600 | 1.07 | -0.84px |
| Large Body Statement | SF Pro Text | 44px | 400 | 1 | -0.44px |
| Heading Large | SF Pro Display | 32px | 700 | 1.14 | -0.32px |
| Heading | SF Pro Display | 24px | 600 | 1.17 | -0.24px |
| Heading Small | SF Pro Display | 19px | 600 | 1.21 | -0.28px |
| Body | SF Pro Text | 14px | 400 | 1.43 | -0.22px |
| Caption | SF Pro Text | 10px | 400 | 1.83 | -0.37px |

## Font Rules

- Use SF Pro Display for all large headlines, section openers, and feature titles.
- Use SF Pro Text for body, nav, buttons, captions, and legal text.
- Use weight 600 to 700 for headline impact.
- Use weight 400 for paragraphs and legal copy.
- Use weight 600 for nav items, buttons, labels, and category eyebrows.
- Keep negative tracking at all sizes.

## Spacing And Shape

- Base unit: 4px
- Density: comfortable
- Max width: 1440px
- Section gap: 88px to 120px
- Card padding: 28px
- Element gap: 10px to 12px
- Links: 10px radius
- Cards: 28px radius
- Buttons: 36px radius
- Nav: 980px radius
- Pills and chips: 980px radius

## Surfaces

| Level | Surface | Value | Role |
| --- | --- | --- | --- |
| 0 | Pure Black Stage | `#000000` | Hero and cinematic feature sections |
| 1 | Carbon Surface | `#111111` | Subtle badge or nested dark surface |
| 2 | Obsidian Stage | `#1d1d1f` | Secondary dark stage and text on light sections |
| 3 | Paper Detail Band | `#ffffff` | Light detail sections |
| 4 | Frost Band | `#f5f5f7` | Soft light gray product sections |

## Elevation

Do not use drop shadows, box shadows, or CSS elevation. Depth comes from:

- Product photography.
- Pure Black, Carbon, and Obsidian contrast.
- White detail bands.
- Rounded image edges.
- Negative space.

## Components

### Hero Stage

Full-viewport Pure Black stage with a centered 1440px max-width. Product image occupies about 50 to 60 percent of viewport height and floats directly on black with no card. Headline sits bottom-left at 80px SF Pro Display, Frost White, and tight negative tracking.

### Primary CTA Button

Apple Blue fill, Paper White text, 36px radius, 10px vertical and 20px horizontal padding, SF Pro Text 14px weight 600. This is the only filled chromatic button in a viewport.

### Ghost Price Label

Transparent background, Frost White text on dark stages, SF Pro Text 14px weight 400, 36px radius, 10px by 20px padding. It sits beside the CTA without competing.

### Category Eyebrow Tag

Plain Signal Orange text, SF Pro Text 17px weight 600, no background, no border, no chip. Use above activity or feature headlines.

### Feature Card Dark Stage

Rounded image card on dark sections, 28px radius, around 28px internal padding. Image may be black-and-white product-in-use photography with Frost White overlay text. No border or shadow.

### Light Section Content Block

Paper White background with two-column text and image layout. Text column uses Signal Orange eyebrow, 56px SF Pro Display headline in Obsidian, body in Platinum, and optional inline feature link.

### Top Navigation Bar

Pure Black or translucent black pill nav with 980px radius, about 10px vertical padding, Apple glyph at left, SF Pro Text 12px nav items, search and bag icons right. May use backdrop blur on scroll.

### Promo Banner

Slim Obsidian bar above nav, centered SF Pro Text 12px Frost White text, inline Link Blue action, about 3px vertical padding.

### Section Headline Dark

Large left-aligned SF Pro Display headline at 56px to 80px, Frost White, negative tracking, and no subtitle. Let the headline stand alone in generous black space.

### Inline Feature Link

Small circular icon plus two-line label in SF Pro Text 17px weight 600. Use Obsidian text on light sections and Halo Blue for dark links when needed.

### Product Spec Tile

Dark or light block with 28px radius. Use concise labels, product-detail imagery, and Platinum body text. Avoid generic dashboard UI.

## Layout

Use a 1440px max-width inside full-bleed stages. Alternate Pure Black feature stages and Paper White detail bands. Section gaps are large, 88px to 120px. Let product images be huge. Avoid dense grids unless they are photo-led or spec-led.

The hero should not look like a card. The product object floats in the stage, with text anchored low and away from the object.

## Imagery

Use:

- High-resolution product renders.
- Watch hardware macro crops.
- Black-and-white product-in-use photography.
- Huge edge-to-edge product photos.
- Feature photos with text overlays.

Avoid:

- Stock photography.
- Generic illustrations.
- App dashboard screenshots as the hero.
- Decorative gradients.
- Extra UI cards around the product.

## Do

- Use Apple Blue as the only filled chromatic CTA.
- Keep only one filled chromatic button in a viewport.
- Use 28px radius for all photo cards and content containers.
- Use 36px radius for standard buttons.
- Use 980px radius for pill nav and chips.
- Alternate Pure Black feature stages with Paper White detail bands.
- Use Signal Orange only for category eyebrows.
- Render body copy in Platinum on light sections or Frost White on dark sections.
- Use huge product imagery with no card chrome.

## Do Not

- Do not use drop shadows or CSS elevation.
- Do not use multiple filled chromatic buttons in the same viewport.
- Do not apply Signal Orange to body text or buttons.
- Do not use pure white for paragraph copy on dark stages.
- Do not add decorative gradients.
- Do not wrap the hero product in a visible card.
- Do not use tiny product imagery.
