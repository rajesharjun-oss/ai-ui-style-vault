# Wope - Style Reference

> Violet horizon interface.

Theme: dark

Wope feels like a dark observatory table lit from below by ultraviolet light. The canvas stays close to Night Violet, while product screenshots, callouts, and controls are separated by translucent white borders, low-opacity glass fills, and purple glow fields. The system should feel embedded and luminous, not stacked with normal drop shadows.

Rebond Grotesque is the large-scale voice for hero and section headlines. Inter V handles everything else: navigation, body copy, controls, badges, links, inputs, and compact UI. Controls are soft pills, while cards are more architectural 16px frames.

## Tokens - Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Night Violet | `#0a0118` | `--color-night-violet` | Global page background, section canvas, cards, footer, and screenshot frames. |
| Void Plum | `#0c0616` | `--color-void-plum` | Occasional dark text on pale treatments and deep UI detail. |
| Soft Quartz | `#ffffff` | `--color-soft-quartz` | Primary headings, high-emphasis copy, icons, borders, and button text. |
| Muted Steel | `#d2d0dd` | `--color-muted-steel` | Secondary headings and brighter muted text over dark sections. |
| Ash Lilac | `#9b96b0` | `--color-ash-lilac` | Body copy, navigation links, supporting labels, and low-emphasis UI. |
| Dim Fog | `#85808c` | `--color-dim-fog` | Inactive icons, subtle separators, and tertiary details. |
| Ultraviolet Core | `#713dff` | `--color-ultraviolet-core` | Primary accent, active links, luminous highlights, and focal glow. |
| Lilac Beam | `#b7a4fb` | `--color-lilac-beam` | Cool flare color for glow edges and light rays. |
| Horizon Glow | `#8562ff` | `--color-horizon-glow` | Gradient midpoint and energized violet hotspot. |
| Glass White 04 | `rgba(255, 255, 255, 0.04)` | `--color-glass-white-04` | Ghost pill fills, badge backgrounds, and translucent overlays. |
| Glass White 10 | `rgba(255, 255, 255, 0.10)` | `--color-glass-white-10` | Hairline borders on pills and glass panels. |
| Ultraviolet Horizon | `linear-gradient(180deg, rgba(183, 164, 251, 0) 0%, rgba(183, 164, 251, 0.5) 50%, rgba(133, 98, 255, 0.5) 75%, rgba(133, 98, 255, 0) 100%)` | `--gradient-ultraviolet-horizon` | Hero light field, illuminated dividers, and ambient section glow. |
| Violet Beam | `linear-gradient(180deg, rgba(183, 164, 251, 0) 0%, #b7a4fb 50%, #8562ff 75%, rgba(133, 98, 255, 0) 100%)` | `--gradient-violet-beam` | Crisp beam and halo treatments. |
| Deep Fade Veil | `linear-gradient(180deg, rgba(11, 2, 23, 0) 22.69%, rgba(22, 9, 42, 0.5) 100%)` | `--gradient-deep-fade-veil` | Section overlays and bottom fades. |

## Tokens - Typography

### Inter V

System UI face for product and text layers.

- Substitute: Inter, system-ui, sans-serif
- Weights: 400, 500, 700
- Sizes: 14px, 16px, 18px, 20px, 24px, 28px
- Line heights: 1.15 to 1.71
- Letter spacing: negative tracking for most UI text, wide positive tracking only for utility labels
- Role: navigation, body copy, links, buttons, badges, inputs, and smaller headings
- Rule: use 400 for body, 500 for controls and links, 700 for compact emphasis.

### Rebond Grotesque

Headline and hero display face.

- Substitute: Sora, Inter, system-ui, sans-serif
- Weight: 700
- Sizes: 20px, 24px, 56px, 72px
- Line heights: 1.11, 1.14, 1.33, 1.60
- Letter spacing: -0.40px at 20px, -0.48px at 24px, -1.12px at 56px, -1.44px at 72px
- Role: hero statements and major section titles
- Rule: do not use for body text, labels, buttons, or dense UI.

### Type Scale

| Role | Size | Weight | Line Height | Tracking | Font |
| --- | --- | --- | --- | --- | --- |
| caption | 14px | 400 | 16px | -0.28px | Inter V |
| body | 16px | 400 | 21px | -0.16px | Inter V |
| subheading | 18px | 400 | 28px | -0.36px | Inter V |
| heading-sm | 24px | 700 | 36px | -0.48px | Rebond Grotesque |
| utility-heading | 28px | 400 | 48px | 2.24px | Inter V |
| heading-lg | 56px | 700 | 74px | -1.12px | Rebond Grotesque |
| display | 72px | 700 | 80px | -1.44px | Rebond Grotesque |

## Tokens - Spacing And Shape

- Density: comfortable
- Base unit: 4px
- Page max width: 1248px
- Section gap: 108px
- Major band padding: 124px
- Card padding: 28px
- Element gap: 16px
- Scale: 4, 8, 12, 16, 20, 24, 28, 32, 40, 64, 80, 96, 108, 112, 120, 124px

### Radius

| Element | Value |
| --- | --- |
| Inputs | 0px |
| Overlay cards | 10px |
| Cards | 16px |
| Buttons | 999px |
| Badges | 999px |

### Elevation

Avoid conventional elevation. Use:

- 1px translucent white borders.
- Purple underlighting gradients.
- Backdrop blur around 4px.
- Blur around 8px for overlays.
- Dark surfaces nearly matching the canvas.

## Components

### Primary Glass CTA Pill

Main action button for hero or high-attention areas. Use a 999px pill, `rgba(255,255,255,0.04)` fill, 1px `rgba(255,255,255,0.1)` border, white label text, and 7px by 24px padding.

### Header Outline Pill Button

Secondary header action such as login. Use transparent fill, 1px translucent white border, 999px radius, 4px by 16px padding, and either white or Ash Lilac text depending on emphasis.

### Text Navigation Pill

Transparent nav pill with no visible border, white text, and 4px by 24px padding. Use when spacing should feel pill-like without adding a frame.

### Hero Trial Badge

Compact pill badge above or below hero copy. Use Glass White 04 fill, white text, 999px radius, and 4px by 14px padding.

### Feature Surface Card

Dark Night Violet card with 16px radius, 28px padding, no shadow, and a translucent border or glow edge. Use for feature summaries and product panels.

### Frosted Info Card

Secondary glass panel with `rgba(255,255,255,0.02)` fill, 16px radius, 28px padding, no shadow, and optional backdrop blur.

### Overlay Mini Card

Floating stat, tooltip, or inset card with `rgba(10,1,24,0.2)` fill, 10px radius, blur, and a thin translucent white border.

### Product Screenshot Frame

Large 16px rounded frame in Night Violet with subtle internal glow and ultraviolet underlighting. The screenshot should appear embedded in the purple light field rather than floating above it.

### Header Bar

Full-width dark header over the canvas. Center contents in 1248px max width, use Ash Lilac links, 16px grouping gaps, and action pills aligned right.

### Borderless Input Field

Transparent input with no visible border and 0px radius. Use white text and place it inside a card, form frame, or underline treatment.

### Logo Rail

Horizontal row of monochrome partner logos in white or Dim Fog. Keep it low contrast and evenly spaced.

### Section Block

Transparent major section wrapper with about 124px vertical padding. Center content and use 16px or 24px internal stacks.

## Layout

Use a centered 1248px content rail over a full-page Night Violet canvas. Hero sections are text-dominant first, then show a large product screenshot frame immersed in violet glow. Major sections should have large vertical rhythm: 108px gaps and around 124px top/bottom padding.

Cards and screenshot frames stay dark. Do not place opaque white content cards on the page. Purple glow should concentrate around proof moments: hero frame, active product areas, illuminated dividers, and key focal points.

## Imagery

Imagery is product-visual first: large contained screenshots of the SEO/product UI, framed by rounded dark containers and ultraviolet glow. Abstract atmosphere can appear as grid lines, light rays, horizon blooms, and dark gradient fades. Logos should be monochrome and quiet.

Avoid illustration-heavy scenes, stock photography, bright non-violet accents, and opaque light cards.

## Do

- Use Night Violet as the dominant canvas.
- Use Rebond Grotesque 56px or 72px for major headlines.
- Use Ash Lilac for body and support copy.
- Use Soft Quartz for primary content and high-emphasis UI.
- Use full-pill radius for buttons and badges.
- Use 16px radius for cards and 10px for floating overlays.
- Build glow with ultraviolet gradients instead of black shadows.
- Use 1px translucent white borders on glass and framed surfaces.
- Keep large vertical rhythm.

## Do Not

- Do not add bright non-violet accents.
- Do not use square or lightly rounded buttons.
- Do not place opaque white cards on the dark page.
- Do not add conventional black drop shadows.
- Do not use Rebond Grotesque for body, labels, or buttons.
- Do not collapse muted copy and primary copy into one color.
- Do not use boxed rectangular inputs.

