# Seed - Style Reference

## North Star

Build the interface like a living organism viewed through laboratory glass: clean, quiet, organic, precise, and almost weightless. Let deep forest green create authority, let warm off-white create calm, and use lime only as a small functional signal.

## Theme

Light. The default surface is Snow White, with Forest Depths used for dark product bands, filled actions, navigation accents, and strong contrast moments.

## Color Tokens

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Forest Depths | `#1c3a13` | `--color-forest-depths` | Primary brand color, filled CTAs, dark sections, nav surfaces, primary text |
| Lime Pulse | `#d3fa99` | `--color-lime-pulse` | Sale badges, highlight pills, small functional emphasis |
| Sage Moss | `#757c5d` | `--color-sage-moss` | Muted green product accent and supporting botanical tone |
| Olive Gold | `#9f995b` | `--color-olive-gold` | Muted yellow wash, secondary botanical highlight |
| Eucalyptus | `#698e79` | `--color-eucalyptus` | Product variant accent, calm green-gray support |
| Ink | `#000000` | `--color-ink` | High-contrast text on light surfaces, used sparingly |
| Pewter | `#666666` | `--color-pewter` | Secondary text, captions, helper copy |
| Ash | `#b3b3b3` | `--color-ash` | Disabled states, soft borders, subdued text |
| Frosted Glass | `#c4c7c4` | `--color-frosted-glass` | Translucent overlays and muted card surfaces |
| Warm Stone | `#eeeee9` | `--color-warm-stone` | Secondary page bands and low-contrast section backgrounds |
| Snow White | `#fcfcf7` | `--color-snow-white` | Page canvas, light cards, inverse text on green |

## Typography

Use Seed Sans if available. Otherwise use Inter or General Sans with similar lightweight behavior.

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| Micro | 10px | 400 | 1 | 0 |
| Label | 12px | 500 | 1.5 | 0 |
| Caption | 14px | 400 | 1.4 | 0 |
| Body Small | 16px | 400 | 1.5 | 0 |
| Body | 18px | 400 | 1.3 | -0.18px |
| Subheading | 24px | 350 | 1.2 | -0.48px |
| Heading Small | 32px | 350 | 1.5 | -0.48px |
| Heading | 36px | 350 | 1 | -0.54px |
| Heading Large | 40px | 300 | 1.1 | -0.4px |
| Display | 48px | 300 | 1.1 | -0.72px |

Rules:

- Use 300 to 350 weights for headings at 32px and above.
- Keep body, buttons, labels, and nav at 400 to 500.
- Avoid 600+ headline weights.
- Enable OpenType `"ss05"` when the selected font supports it.
- Use Seed Sans Mono for product codes, ingredient specs, and small formula-like lists.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | Comfortable |
| Base unit | 8px |
| Max width | 1200px |
| Section gap | 64px |
| Card padding | 16px |
| Element gap | 8px |

Spacing scale: 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 128.

Radius scale:

- Inputs: 8px.
- Cards: 16px.
- Large feature cards: 32px.
- Buttons, badges, tags, and pill controls: 1000px.

## Components

### Primary Filled Button

Use Forest Depths background, Snow White text, 1000px radius, 16px vertical padding, 24px horizontal padding, 16px text, 400 weight, no border, no shadow.

### Ghost Outlined Button

Use transparent fill, 1.5px Snow White border, Snow White text, 1000px radius, and the same button padding rhythm.

### Inverted Light Button

Use Snow White background, Forest Depths text, 1.5px Forest Depths border, and 1000px radius.

### Text Link With Arrow

Use no fill, no border, Forest Depths text, underline, small padding, and a right arrow glyph when the surrounding UI supports it.

### Sale Badge

Use Lime Pulse background, Forest Depths text, 1000px radius, 6px vertical padding, 8px horizontal padding, 12px label text.

### Product Tag Badge

Use a translucent Snow White background on dark green product cards, Snow White text, 1000px radius, and compact label sizing.

### Product Card

On dark sections, keep product cards visually embedded. Use transparent background, 16px radius, no shadow, no border, product code pill, product name, product image, Shop Now action, and price.

### Feature Card

Use transparent or Frosted Glass surfaces, 16px radius, no shadow, no heavy outline. Frosted variants may use backdrop blur around 37.5px.

### Nav Bar

Use Snow White background, sticky placement, brand wordmark with green dot, calm nav links, ghost sign-in action, primary get-started action, 64px to 80px height, and 24px to 48px horizontal padding.

### Promo Banner

Use a thin 40px top band with Snow White background, Forest Depths text, 12px uppercase Seed Sans, an icon, an announcement, and one inline link.

### Input Field

On dark sections, use transparent fill, 1.5px Snow White border, Snow White text, 8px radius, 14px to 20px padding, and clear placeholder contrast.

### Product Code Pill

Use 1.5px outline, 1000px radius, 6px vertical padding, 8px horizontal padding, and 12px Seed Sans at 500 weight.

## Layout And Imagery

- Alternate Snow White sections with deep Forest Depths product bands.
- Keep content in a 1200px max-width container.
- Use generous vertical air: 64px section gaps, with larger 80px to 128px pauses for hero or product families.
- Product photography should feel clinical and close to the surface: isolated bottles, capsules, hands, jars, or simple packaging on warm light backgrounds.
- Avoid decorative botanical illustrations unless they are very restrained.
- Avoid gradients, ornamental borders, heavy shadows, and saturated color variety.

## Do

- Use Forest Depths for CTAs, dark sections, primary text, and brand-defining surfaces.
- Use Lime Pulse only for sale badges, new tags, highlight pills, and tiny emphasis.
- Use 1000px radius for buttons, badges, tags, and pills.
- Keep headings thin, airy, and tracked slightly tighter at large sizes.
- Use Seed Sans Mono for product codes and formula-like information.
- Choose Snow White or Forest Depths for major sections rather than many middle surfaces.

## Do Not

- Do not use shadows or elevation as the main hierarchy system.
- Do not use gradients as backgrounds.
- Do not use pure white `#ffffff` as the main canvas.
- Do not add saturated accent colors outside the green and lime family.
- Do not set display headlines in heavy weights.
- Do not make cards look glossy, busy, or app-dashboard-like.
