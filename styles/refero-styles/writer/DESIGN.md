# WRITER - Style Reference

## Positioning

WRITER feels like enterprise AI presented through editorial design. The interface should not feel like a dense admin console or a playful AI toy. It is a white newsroom-like workspace with confident centered type, pill controls, sparse violet accents, and dark content sections that create a magazine-meets-control-center rhythm.

## Theme

- Theme: light
- Mood: editorial AI atelier on a white marble newsroom canvas
- Best fit: enterprise AI, agent platforms, writing software, AI governance, knowledge tools, productivity systems, content operations, B2B AI platforms

## Visual Principles

1. Lead with Pure White and strong black typography.
2. Highlight exactly one key word in Orchid Accent.
3. Use Iris Brand only for a few high-attention actions.
4. Keep controls pill-shaped and soft.
5. Use 12px radius for cards, images, and icons.
6. Alternate white editorial sections with Obsidian dark bands.
7. Use typography and whitespace instead of shadows.

## Color System

| Token | Value | Role |
| --- | --- | --- |
| Orchid Accent | `#a95ef8` | One highlighted word in display headlines |
| Iris Brand | `#5551ff` | Scarce violet action and outline accent |
| Lavender Wash | `#e4e9ff` | Soft section wash and subtle separation |
| Cobalt Spark | `#007aff` | Low-frequency decorative or product detail accent |
| Ink Black | `#000000` | Main text, headings, strong borders, icons |
| Pure White | `#ffffff` | Page canvas, cards, inputs, button text |
| Obsidian | `#27272b` | Dark section background, neutral filled buttons |
| Graphite | `#2d2d2d` | Dark surface level and secondary dark fills |
| Slate | `#666666` | Helper text, placeholders, metadata |
| Ash | `#bdbdbd` | Placeholder text and low-priority labels |
| Fog | `#d2d4d7` | Muted text, secondary borders, disabled states |
| Mist | `#e4e7ed` | Hairline borders, dividers, subtle card edges |
| Privacy Banner Gradient | `linear-gradient(50deg, #f7c8ed 50px, #e5ecff 130px, #e5ecff 100%)` | Soft announcement banner wash |

## Typography

Use Poppins for product UI, navigation, buttons, labels, headings, and display. It is geometric but editorial in its spacing: display type is tight, while tiny labels use wide positive tracking.

Use CanelaDeck only as a body-size serif accent to add editorial texture. It should not replace the main heading system.

Recommended fallbacks:

- Primary: `Poppins`, `Inter`, `DM Sans`, `Manrope`, `ui-sans-serif`, `system-ui`
- Serif accent: `CanelaDeck`, `Playfair Display`, `DM Serif Display`, `Lora`, `serif`

OpenType for Poppins:

```css
font-feature-settings: "clig" 0, "liga" 0;
```

### Type Scale

| Role | Size | Line Height | Weight | Tracking |
| --- | ---: | ---: | ---: | ---: |
| Caption | 11px | 1.5 | 500 | 0.143px |
| Body Small | 14px | 1.55 | 600 | 0 |
| Body | 16px | 1.5 | 400 | 0 |
| Subheading | 20px | 1.4 | 600 | -0.2px |
| Heading Small | 25px | 1.25 | 500 | -0.4px |
| Heading | 40px | 1.2 | 500 | -0.8px |
| Heading Large | 44px | 1.15 | 500 | -0.88px |
| Display | 64px | 1 | 500 | -1.98px |

## Spacing And Shape

- Base unit: 4px
- Density: comfortable
- Page max width: 1200px
- Section gap: 80px to 120px
- Card padding: 24px
- Element gap: 12px to 16px
- Cards: 12px radius
- Icons: 12px radius
- Buttons: 60px radius
- Inputs: 72px radius
- Large pill variants: up to 82px radius

## Layout

Use centered editorial hero sections with max-width around 800px for display copy. Alternate Pure White content with Obsidian dark resource bands. Keep resource cards and agent output cards clean, with white surfaces, 12px corners, light borders, and no heavy shadows.

## Imagery

Use product screenshots, AI workflow cards, agent output examples, grayscale trust logos, and minimal product diagrams. Imagery should feel like enterprise software made editorial, not like generic abstract AI art.

## Components

### Primary Pill Button

Obsidian fill, Pure White text, Poppins 14px to 16px weight 500 to 600, 16px by 32px padding, 60px radius, no shadow.

### Accent Pill Button

Iris Brand fill, Pure White text, Poppins 14px weight 500, 12px by 24px padding, 60px radius. Use sparingly for a high-attention entry point.

### Ghost Outlined Button

Transparent fill, Iris Brand border, Iris Brand text, Poppins 14px weight 500, 60px radius. Use as a violet pair to the accent action.

### Pill Email Input

Pure White fill, Ash border, Slate placeholder text, Poppins 14px to 16px, 16px by 20px padding, 72px radius. Often sits inline with a pill button.

### Hero Display Headline

Centered Poppins 64px weight 500, Ink Black, line-height 1, -1.98px tracking, with exactly one word in Orchid Accent.

### Eyebrow Label

Poppins 11px to 12px, uppercase, weight 500, wide 0.077em to 0.300em tracking, centered above the headline.

### Feature Card

Pure White surface, no heavy border or shadow, 24px padding, image or icon at 12px radius, heading in Poppins 20px to 25px weight 600, body in Poppins 14px to 16px.

### Agent Output Card

Pure White surface, subtle Mist border, 12px radius, 20px to 24px padding, task title, checklist, circular status icons, and small indicators.

### Trust Logo Bar

Centered row of grayscale logos in Ash on Pure White. Keep all logos monochrome so they do not compete with the violet accent.

### Dark Resource Section

Obsidian or near-black background, Pure White text, Poppins 40px to 44px headline, white resource cards on top.

### Floating Action Card

Dark promotional card with subtle gradient/noise, Pure White copy, Iris Brand pill button, 16px to 20px radius, slightly offset or rotated if needed.

### Navigation Bar

Pure White background, WRITER wordmark left, Poppins 14px weight 500 links, and right-side pill actions. The nav may be sticky and should remain clean.

### Announcement Banner

Soft privacy gradient strip above the nav, Ink Black Poppins 12px to 13px text, and small dismiss control.

### Back-To-Top Control

Small fixed Obsidian square with a white up-arrow. Minimal utility only.

## Rules

- Highlight exactly one word per display headline in Orchid Accent.
- Do not use Orchid Accent outside headline word highlights.
- Use Iris Brand for at most one or two high-attention elements per viewport.
- Use 60px radius on buttons and 72px on email inputs.
- Use 12px radius on cards, images, and icons.
- Keep body text between 14px and 18px.
- Use wide tracking only at label and caption scale.
- Do not add drop shadows to cards or buttons.
- Do not use full black as a large background fill; use Obsidian instead.
- Do not introduce new accent colors beyond the defined violet and blue accents.
