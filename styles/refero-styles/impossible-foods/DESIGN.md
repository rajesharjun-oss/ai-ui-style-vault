# Home Page | Impossible Foods - Style Reference

> Blood-red punk poster in velvet darkness: giant condensed display type, wine-dark surfaces, one red signal, flat product cards, and organic food-photo masks.

## Theme

Dark. The foundation is a velvet wine canvas, not black alone. Burgundy surfaces create depth without shadows, while impossible red provides all emphasis and action.

## Design Story

Build the page like a punk food manifesto. The type should shout product claims in viewport-filling uppercase display text. Product photography supports the claim: packaged goods sit in flat carousel cards, while food shots float near hero text in irregular organic masks.

The system is aggressive but disciplined. Do not add gradients, shadows, or extra colors. Hierarchy comes from color contrast, compact UI, and huge type scale.

## Tokens - Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Velvet Wine | `#260212` | `--color-velvet-wine` | Page canvas and deepest section background |
| Burgundy Stage | `#4f0423` | `--color-burgundy-stage` | Section surfaces, card surfaces, lifted bands |
| Impossible Red | `#e10600` | `--color-impossible-red` | Primary action, active toggles, display text, icon emphasis |
| Blush Highlight | `#ffc7c6` | `--color-blush-highlight` | Soft secondary text, inactive toggles, tonal relief |
| Butcher Black | `#000000` | `--color-butcher-black` | Navigation background, card outlines, hairline borders |
| Bone White | `#ffffff` | `--color-bone-white` | Navigation text, button text, copy on dark surfaces |

## Typography

Primary font: sans-meat.

- Use this face for everything from micro labels to giant hero statements.
- Display uses weight 700 and extremely large sizes.
- UI, nav, and body use weights 400 and 500.
- Fallback display choices: Druk Wide or Knockout-style condensed sans.
- Fallback body choices: Inter or Sohne-style geometric sans.

Display text is intentionally oversized. Most hero and section moments should use 103px or larger. The line-height is tight at 0.73 to 0.75, with slightly positive tracking so the uppercase blocks read like shouted labels.

## Type Scale

| Role | Size | Weight | Line height | Tracking |
| --- | --- | --- | --- | --- |
| Caption | 10px | 400 or 500 | 1.4 | 0.02px |
| Body Small | 14px | 400 or 500 | 1.4 | 0.02px |
| Body | 18px | 400 or 500 | 1.4 | 0.02px |
| Subheading | 24px | 500 or 700 | 1.15 | 0.02px |
| Heading Small | 32px | 700 | 1.1 | 0.02px |
| Heading | 48px | 700 | 0.9 | 0.02px |
| Heading Large | 103px | 700 | 0.75 | 0.03px |
| Display | 160px | 700 | 0.73 | 0.06px |

## Spacing And Shape

- Base unit: 4px.
- Density: compact.
- Page max width: 1280px.
- Section gap: 40px to 64px.
- Card padding: 16px to 24px.
- Element gap: 6px to 16px.
- Nav radius: 15px.
- Card radius: 12px.
- Button radius: 15px.
- Toggle radius: 15px.
- Feature card radius: 38px.

## Components

### Sticky Top Navigation

Use a full-width Butcher Black bar. Place the Impossible wordmark in Impossible Red at the left, white nav links in the center, and a right-side utility/dropdown plus red CTA. The bar stays sticky and visually anchors every section.

### Primary CTA Button

Impossible Red fill, Bone White text, sans-meat 14px weight 500, uppercase, 0.02em tracking, 15px radius, 10px 14px padding, and a small right-side caret.

### Ghost CTA Button

Transparent fill, 1px Bone White border, Bone White text, same typography, radius, and padding as the primary CTA. Use next to filled CTAs for paired actions like learn more and find it.

### Filter Pill Toggle

15px radius, 10px 16px padding, 6px gap, uppercase sans-meat 14px to 18px weight 500. Active state uses Impossible Red fill and Bone White text. Default state uses transparent fill with Blush Highlight or Bone White text.

### Hero Display Block

Centered stack on Velvet Wine or Burgundy Stage. Eyebrow at 14px to 18px uppercase red. Display headline at 160px to 231px, weight 700, red, line-height 0.73, and positive tracking. Use parenthetical asides as structural line breaks.

### Product Carousel Card

Burgundy Stage surface, optional 1px Butcher Black border, 12px radius, no shadow. Product packaging photo fills the top area. Product name uses 22px to 24px uppercase sans-meat in Blush Highlight or Bone White. Pair filled and ghost CTAs below.

### Category Tab With Number Badge

Uppercase label at 20px to 24px, Blush Highlight, with a small circular count badge. Active tab uses an Impossible Red underline.

### Masked Food Photography

Use high-saturation food shots cropped into irregular organic shapes. These are decorative around hero type, not cards. No border, no shadow, no geometric circle.

### Recipe Or Product Grid Card

Burgundy Stage surface, 1px Butcher Black hairline, 12px radius or 38px for a featured card, and 16px to 24px padding. Use clean rectangular product images inside these cards only.

## Layout

Use a full-bleed dark canvas with centered content stacks. The hero is not a two-column split. It is a centered display-type block with floating masked food images. Below, alternate between huge display sections and horizontal product carousels. Product grids can use four columns. Section dividers are made with spacing only, not lines or color bands.

## Imagery

Use product photography, not illustration. Packaging shots should be tight and saturated on dark wine surfaces. Decorative food images should be mask-cut into rough blob-like shapes around hero text. Use minimal flat icons only for caret arrows and location pins.

## Rules

Do:

- Use display type at 103px or larger for major statements.
- Keep display line-height around 0.73 to 0.75.
- Reserve Impossible Red for actions, active state, and display type.
- Pair filled red CTAs with white-outlined ghost CTAs.
- Use 15px radius for buttons, nav controls, and toggles.
- Use organic food masks near hero text.
- Keep the nav bar solid black.

Do not:

- Do not add drop shadows, glows, or gradients.
- Do not introduce additional chromatic colors.
- Do not use red for body copy or secondary text.
- Do not use rectangular food photos in hero zones.
- Do not use a light or white page background.
- Do not soften display line-height above 0.80.
- Do not turn the system into a conventional polished SaaS layout.
