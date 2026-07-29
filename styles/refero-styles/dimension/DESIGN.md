# Dimension Style Reference

Dimension is a dark AI-workspace system built from matte black, frosted overlays, pill controls, medium-weight geometric type, and a single soft violet pulse. The design should feel intentional and quiet: every module is placed with space, every edge is a hairline, and every color beyond gray is rare.

## Theme

Dark, AI workspace, frosted glass, editorial product, monochrome, pill controls, restrained gradient, developer productivity.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Ink Black | `#000000` | `--color-ink-black` | Icon strokes, SVG fills, and deep contrast details on light surfaces. |
| Void Canvas | `#0a0a0a` | `--color-void-canvas` | Primary page background and dark UI shell. |
| Graphite | `#161616` | `--color-graphite` | Elevated dark surface for nav, panels, modals, and cards. |
| Slate | `#686868` | `--color-slate` | Muted text, metadata, timestamps, and quiet links. |
| Smoke | `#b2b2b2` | `--color-smoke` | Disabled text and idle integration labels. |
| Ash | `#c2c2c2` | `--color-ash` | Secondary body text, helper copy, and de-emphasized labels. |
| Frosted Glass | `#d4d4d4` | `--color-frosted-glass` | Translucent panel fill at 10 percent opacity over dark surfaces. |
| Hairline | `#e5e5e5` | `--color-hairline` | 1px borders on dark-surface controls and glass panels. |
| Bone | `#ededed` | `--color-bone` | Primary readable text on dark surfaces, softer than pure white. |
| Snow White | `#ffffff` | `--color-snow-white` | Primary CTA fill, strong headline text, and inverted card surfaces. |
| Dusk Violet | `#6b62f2` | `--color-dusk-violet` | The only chromatic accent; use at partial opacity in glow or gradient washes only. |

## Typography

### DM Sans

Use for display, body, navigation, buttons, and most UI.

- Token: `--font-dm-sans`
- Fallback: Inter, system-ui
- Weight: 500 for display; 400 to 500 for UI/body
- Sizes: 13px, 14px, 15px, 16px, 18px, 40px, 72px
- Line height: 1.00 to 1.56
- Letter spacing: -0.035em at 72px and 40px, +0.025em at 13px to 16px
- Role: geometric restraint for the main brand voice.

### Geist

Use for section headings, feature titles, and denser product/editorial copy.

- Token: `--font-geist`
- Fallback: Inter, system-ui
- Weights: 400, 500, 600
- Sizes: 14px, 16px, 18px, 24px, 32px, 36px, 48px
- Line height: 1.00 to 1.71
- Role: more technical, product-aware emphasis in section content.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | 13px | 1.50 | 0.33px | `--text-caption` |
| Body | 16px | 1.50 | 0 | `--text-body` |
| Subheading | 18px | 1.50 | 0 | `--text-subheading` |
| Heading SM | 24px | 1.33 | 0 | `--text-heading-sm` |
| Heading | 36px | 1.11 | 0 | `--text-heading` |
| Heading LG | 48px | 1.00 | 0 | `--text-heading-lg` |
| Display | 72px | 1.00 | -2.52px | `--text-display` |

## Spacing And Shape

- Density: comfortable.
- Base unit: 4px.
- Max width: 1200px.
- Section gap: 64px to 80px.
- Card padding: 28px.
- Element gap: 8px to 16px.

### Spacing Scale

`4, 6, 8, 10, 12, 14, 16, 20, 22, 24, 28, 32, 40, 44, 48, 56`

### Radius Scale

| Element | Radius |
|---|---:|
| Icons | 4px |
| UI controls | 10px |
| Cards | 24px |
| Large cards | 40px |
| Panels | 42px |
| Buttons and pills | 9999px |

### Elevation

| Name | Token | Value |
|---|---|---|
| Subtle inset | `--shadow-subtle` | `rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset` |

Use the inset line, translucency, and backdrop blur instead of external shadows.

## Components

### White Pill CTA

Snow White fill, Graphite text, 9999px radius, 8px vertical and 12px horizontal padding, DM Sans 14px to 16px. This is the main filled action and should be rare.

### Ghost Nav Button

Transparent fill, white text at reduced opacity, 1px Hairline border, 9999px radius, 6px vertical and 14px horizontal padding. Use inside floating nav.

### Floating Frosted Nav

Graphite or translucent Graphite surface, 19px asymmetric radius, 4px backdrop blur, 1px Hairline border, compact internal link padding. The nav should feel detached and glass-like.

### Hairline Ghost Button

Transparent fill, Bone or Smoke text, 1px Hairline border, 10px radius, tight 8px padding. Use for integration labels and secondary actions that should not become pills.

### Frosted Glass Feature Card

Frosted Glass at 10 percent opacity over Void Canvas, 24px radius, 1px translucent Hairline border, no shadow, optional 4px backdrop blur. Content sits inside the panel.

### Gradient Hero Panel

Full-bleed hero atmosphere with warm amber/coral on one side and cobalt blue on the other. Place 72px DM Sans display text in white or Bone, a compact bullet list, a white pill CTA, and a product/device mockup.

### Numbered Accordion Row

Feature name in Bone, two-digit number in Ash, no visible background, no card shell, and generous 20px row rhythm. Use this for capability lists.

### Bulleted Feature Row

Small monochrome icon, 16px DM Sans text in Bone, 12px gap, and 16px vertical rhythm. No borders or backgrounds.

### Device Mockup Frame

Large rounded product frame with 40px top corners and 0px bottom corners. Screenshot bleeds to edges. Use for laptop or monitor UI previews.

### Status Banner Pill

Pill announcement bar at the top of the page. Dark/translucent background, 9999px radius, small icon, short text, and arrow. Keep compact.

### Section Header

Geist 32px/600 or 36px/500 in Bone, followed by 18px Geist or DM Sans supporting text in Ash.

### Icon Glyph

Monochrome, simple geometry, 16px to 20px, 1.5px stroke, optional 4px squircle container.

## Layout

Use a 1200px content rail on a full-bleed Void Canvas. The hero can be a split layout with large text and feature bullets on the left and a laptop/product mockup on the right. Navigation is floating and glass-like rather than a full-width bar. Feature sections use glass cards, numbered rows, and dark panels with generous spacing. Keep sections to 64px to 80px vertical rhythm and avoid dense marketing clutter.

## Imagery

Use product UI screenshots, laptop mockups, integration tiles, AI workspace surfaces, simple glyph icons, and warm-to-cool atmospheric hero gradients. Avoid photography, lifestyle imagery, multicolor icon sets, solid violet buttons, and decorative background blobs. The violet glow should be a soft spotlight or line wash, not a shape or fill.

## Do

- Use 9999px radius for primary buttons, nav links, and pill tags.
- Set display headlines in DM Sans 72px, weight 500, with -2.52px tracking.
- Use Bone for readable text instead of pure white body copy.
- Use 1px Hairline borders on dark-surface controls.
- Apply warm-to-cool gradients only to hero or spotlight sections.
- Keep element gaps between 8px and 16px.
- Use Dusk Violet only in gradient washes or glows.
- Use translucency and backdrop blur for depth.

## Don't

- Do not use box-shadow for elevation.
- Do not introduce additional brand colors.
- Do not use Dusk Violet as a solid fill, text color, button, or card background.
- Do not use 700+ weight hero typography.
- Do not place large white cards directly on Void Canvas unless they are product mockups.
- Do not make every card frosted; reserve glass for feature panels and navigation.
- Do not add photographic hero imagery.
