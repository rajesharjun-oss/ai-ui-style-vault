# Clyde Style Reference

> A dark luxury protection showroom: near-black gallery canvas, warm cream typography, massive editorial serif type, and one warm gradient spotlight.

## Theme

Dark.

Clyde treats product protection like a luxury editorial experience. The page is mostly black and warm cream, with surface contrast handled by tonal shifts and hairline borders. Large Recoleta-style serif headings create the magazine-cover moment, while Oldschool Grotesk keeps navigation, body copy, buttons, labels, and cards calm and practical.

## Core Principles

1. Keep the interface almost achromatic.
2. Use the Solstice Gradient only as a decorative or product accent.
3. Use serif display type for all major text 36px and above.
4. Use grotesk sans type for UI, body, navigation, and buttons.
5. Make interactive controls pill-shaped at 100px radius.
6. Use borders and surface contrast instead of shadows.
7. Let product objects sit inside clean white or bone containers.

## Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Obsidian | `#000000` | `--color-obsidian` | Main dark canvas, dark borders, inverted UI |
| Char | `#1a1a1a` | `--color-char` | Near-black surface separation and card edges |
| Slate | `#7d7d7d` | `--color-slate` | Mid-gray controls, active filters, muted fills |
| Bone | `#f6f6f4` | `--color-bone` | Warm text on dark, light sections, ghost outlines |
| Paper | `#ffffff` | `--color-paper` | Inner product containers and high-contrast cards |
| Solstice Gradient | `linear-gradient(90deg, #feed7a 0%, #ff8400 48.96%, #df91f7 100%)` | `--gradient-solstice` | Decorative 3D shape and limited product accent |

## Typography

Use three roles:

| Role | Family | Fallback | Use |
| --- | --- | --- | --- |
| Display | Recoleta | GT Super, Canela, Tiempos Headline | Headings from 36px to 125px |
| Primary | Oldschool Grotesk | Sohne, Inter, Neue Haas Grotesk | UI, body, buttons, nav, card copy |
| Annotation | Times system fallback | Times New Roman, Georgia | Rare secondary notes |

## Type Scale

| Role | Size | Weight | Line Height | Letter Spacing |
| --- | --- | --- | --- | --- |
| Body small | 15px | 300 or 400 | 1.6 | 0.15px |
| Body | 16px | 300 or 400 | 1.4 to 1.6 | -0.16px |
| Body large | 21px | 300 | 1.3 | -0.42px |
| Subheading | 36px | 400 | 1.1 | -0.36px |
| Heading small | 47px | 400 | 1.1 | -0.94px |
| Heading | 61px | 400 | 1.1 | -1.22px |
| Heading large | 80px | 400 | 1 | -2.4px |
| Display | 125px | 400 | 1 | -3.75px |

Display text should be tight and sculptural. Body copy should be quiet, lightweight, and compact.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | comfortable |
| Base unit | 4px |
| Max width | 1200px |
| Section gap | 80px |
| Card padding | 24px |
| Element gap | 20px |
| Input radius | 4px |
| Link radius | 12px |
| Card radius | 16px |
| Large panel radius | 38px |
| Tag radius | 100px |
| Button radius | 100px |

Use these radius values as a closed scale. Do not invent intermediate roundness.

## Layout

Use a full-bleed dark page canvas with centered 1200px content. Sections alternate between Obsidian and Bone bands. The page rhythm should feel like a gallery with large type, restrained cards, and low visual density.

Recommended flow:

1. Bone announcement strip.
2. Transparent dark navigation header.
3. Full dark hero with massive serif headline.
4. Floating Solstice Gradient 3D shape.
5. Light product feature section.
6. Dark credibility or stats strip.
7. Product protection cards or case studies.
8. Dark or Bone closing section.

## Components

### Announcement Bar

Full-width Bone band, centered text, 12px vertical padding. Use Oldschool Grotesk 15px regular in Obsidian. No shadow or border.

### Dark Navigation Header

Transparent over the dark canvas. Logo centered or left, nav links in Bone, login and demo actions on the right. No filled nav background, no bottom border, no sticky complexity.

### Hero Display Section

Full-bleed Obsidian background. Centered Recoleta-style headline from 80px to 125px, Bone color, tight line height, negative tracking. Add a floating Solstice Gradient 3D shape below or near the headline as the only chromatic atmosphere.

### Filled Pill Button

Use on light Bone surfaces. Obsidian fill, Bone text, 100px radius, 20px by 28px padding, Oldschool Grotesk 15px regular. No shadow and no gradient.

### Ghost Pill Button

Use on dark surfaces. Transparent fill, 1px Bone border, Bone text, 100px radius, 20px by 28px padding.

### Product Protection Card

Bone background, 16px radius, 24px padding. Product image goes inside a Paper container. Heading uses Oldschool Grotesk 21px regular in Obsidian. Feature list uses 15px lightweight grotesk text.

### Program Performance Card

Bone background with 16px radius and generous horizontal padding. Include tab/filter pills at the top and a chart area below. Active filter can use Slate. Keep the data panel flat.

### Stats Feature Bar

Dark horizontal row with 4 or 5 credibility items. Separate items with 1px Bone hairlines. Each item combines a small circular check mark and 15px Bone text.

### Case Study Card

Char or Obsidian surface, 16px radius, 24px padding, Bone text, client logo box, body copy, ghost pill CTA, and a lower product illustration area with very small gradient accents.

### Filter Tab Pill

100px radius, 10px by 16px padding. Inactive state is transparent with Obsidian border on light surfaces. Active state can use Slate.

### Section Heading Block

Left-aligned Recoleta-style heading from 47px to 80px. Use Bone on dark sections and Obsidian on light sections. No decorative eyebrow is needed; the heading carries the section.

### Body Description Block

Max width around 520px. Use Oldschool Grotesk 16px at weight 300 or 400 with quiet opacity on dark surfaces. Keep paragraph styling simple.

## Surfaces

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 0 | Obsidian Canvas | `#000000` | Default page and dark section background |
| 1 | Bone Section | `#f6f6f4` | Light alternating sections, cards, announcement band |
| 2 | Slate Surface | `#7d7d7d` | Active filters and mid-tone controls |
| 3 | Paper Card | `#ffffff` | Product image containers |
| 4 | Char Edge | `#1a1a1a` | Subtle dark surface separation |

## Elevation

Use no box shadows. Depth comes from 1px borders, radius, and tonal contrast. On dark sections, Bone hairlines define edges. On light sections, Char or Obsidian hairlines do the same.

## Imagery

Use two image modes:

1. A soft, organic 3D blob or abstract object using the Solstice Gradient.
2. Clean product objects contained in Paper or Bone cards.

Keep imagery sparse. Avoid stock lifestyle photography, dense icon systems, and illustrative clutter.

## Do

- Use Recoleta-style serif for all headings 36px and above.
- Tighten display tracking as size increases.
- Use 100px radius for buttons, tags, filters, and tabs.
- Keep the palette almost entirely black, cream, white, and gray.
- Use the gradient only in decorative 3D shapes or tiny product accents.
- Use hairline borders instead of shadows.
- Use Oldschool Grotesk weight 300 for descriptive copy and 400 for UI.

## Don't

- Do not introduce new chromatic UI colors.
- Do not make gradient buttons, gradient text, or gradient borders.
- Do not use serif display type for body copy below 36px.
- Do not add box shadows to cards.
- Do not use zero or positive tracking on large display type.
- Do not invent radius values outside the defined scale.
- Do not mix colored button systems.

## AI Builder Notes

If the design feels too quiet, increase the headline scale or add a better product crop before adding color. The premium signal is the restraint: black, cream, border, radius, type, and one decorative glow.
