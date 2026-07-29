# Galileo-ft - Style Reference

Theme: dark

Galileo-ft's Refero style is a deep-space fintech observatory. The surface system is almost entirely dark navy and indigo, separated by lavender hairlines rather than shadows. The signature is extremely thin typography: large headlines use weight 100 and often negative tracking, with cobalt acting as the single high-voltage action color.

## Core Principles

- Use deep navy as the page canvas.
- Use deep indigo for cards and panels.
- Separate surfaces with 1px lavender/violet borders, not shadows.
- Use Pulse Cobalt only for primary filled actions and active states.
- Use teal only as a supporting signal or gradient origin.
- Use Plain-style ultrathin display typography for all large headings.
- Keep buttons pill-shaped and cards generously rounded.
- Use gradients only on full-bleed brand banners, not inside cards.

## Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Void Navy | `#03081a` | `--color-void-navy` | Page canvas and primary dark background. |
| Deep Indigo | `#020626` | `--color-deep-indigo` | Card surfaces, panels, and secondary dark fills. |
| Inkline Violet | `#292f66` | `--color-inkline-violet` | Hairline borders, dividers, and structural icon strokes. |
| Dusk Iris | `#4d5499` | `--color-dusk-iris` | Muted borders, disabled states, and low-priority outlines. |
| Mist Lilac | `#7a83cc` | `--color-mist-lilac` | Tertiary text and low-emphasis supporting UI. |
| Quartz Lavender | `#aab1f2` | `--color-quartz-lavender` | Secondary text, outlined link borders, inactive nav. |
| Glacier White | `#f5f6ff` | `--color-glacier-white` | Light cards, light section surfaces, high contrast text. |
| Pure White | `#ffffff` | `--color-pure-white` | Primary dark-surface text and button borders. |
| Pulse Cobalt | `#3d50fc` | `--color-pulse-cobalt` | Primary filled action, active tab, and brand signal. |
| Signal Teal | `#05e0e0` | `--color-signal-teal` | Supporting icon, tertiary link, and data-viz signal. |
| Cyan Teal | `#05cee0` | `--color-cyan-teal` | Decorative gradient origin and atmospheric accent. |
| Gradient Teal Blue | `linear-gradient(90deg, #05a1c9 0%, #3d50fc 100%)` | `--gradient-teal-blue` | Full-bleed announcement or brand banner sweep. |

## Typography

### Fonts

- Primary: Plain.
- Display ultrathin: Plain Ultrathin.
- Mid-scale ultralight: Plain Ultralight.
- Body/detail: Plain Light.
- Fallbacks: Inter Thin/Light, Neue Haas Grotesk Display Thin, Untitled Sans Light, system-ui.
- Incidental extraction: Times at 16px exists in source data, but it is not a core design driver.

### Type Scale

| Role | Size | Weight | Line Height | Tracking | Use |
| --- | --- | --- | --- | --- | --- |
| eyebrow | 10px | 400 | 1.2 | 2.5px | Uppercase category labels. |
| caption | 12px | 300 | 1.5 | 0 | Small support copy. |
| body | 16px | 300 | 1.3 | 0 | Body copy and buttons. |
| subheading | 28px | 100 | 1.3 | -0.56px | Card headings and product category headings. |
| heading-sm | 42px | 100 | 1.1 | -0.84px | Smaller section headlines. |
| heading | 56px | 100 | 1.1 | -1.12px | Section headlines. |
| heading-lg | 83px | 100 | 1 | -1.66px | Hero headline. |
| display | 147px | 100 | 0.8 | -2.94px | Rare oversized display statement. |

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | comfortable |
| Base unit | 4px |
| Page max width | 1200px |
| Section gap | 64px |
| Card padding | 32px |
| Element gap | 9px |

### Spacing Scale

`4px`, `16px`, `20px`, `52px`, `64px`, `104px`, `196px`

### Radius

| Element | Value |
| --- | --- |
| tags | 17px |
| cards | 35px |
| inputs | 35px |
| buttons | 48px |

## Components

### Primary Filled Button

Pulse Cobalt fill, Pure White text, 48px radius, 22px horizontal padding, 14px vertical padding, Plain Light/Plain weight 300 at 16px. No shadow and no border.

### Ghost Outline Button

Transparent background, 1px Pure White border, Pure White text, 48px radius, 22px by 14px padding. Use beside primary CTAs for secondary paths.

### Pill Navigation Link

Transparent pill with 1px Pure White or Quartz Lavender border, 48px radius, and 13-14px thin Plain text. Lavender border signals lower-priority nav.

### Dark Card

Deep Indigo background, 1px Inkline Violet border, 35px radius, and 32px padding. No shadow. Surface separation comes from the violet hairline.

### Light Card

White or Glacier White surface with a Mist Lilac/Dusk Iris border, 35px radius, 32px padding, and dark text. Use for dashboard screenshots and product panels.

### Tab Pill

Active tab uses Pulse Cobalt fill, white text, 17px radius, and 22px by 14px padding. Inactive tabs are transparent with faint violet border.

### Eyebrow Label

Plain 10px uppercase with 0.25em letter spacing. Use Quartz Lavender or Signal Teal above large weight-100 headings.

### Outlined Link

No background. Use Quartz Lavender text with a 1px Quartz Lavender bottom border instead of a solid underline.

### Floating Chat Trigger

Glacier White pill fixed at bottom center, 48px radius, light border, optional avatar icon, and 14-16px Plain text.

### Announcement Bar

Full-bleed teal-to-cobalt gradient, white 14px thin Plain text, ghost learn-more button, and dismiss control. This is one of the only places a gradient belongs.

### Hero Headline

Plain Ultrathin weight 100, Pure White, 56-83px, -0.02em tracking, left-aligned. Pair with a 3D cobalt glass sculpture or product mockup on the right.

### Dashboard Product Screenshot

Dashboard or product visual inside a 35px-radius bordered card. Internal UI uses dark surface, cobalt, and teal data accents.

### Navigation Menu

Right-aligned vertical nav list using Pure White text and 14-16px thin Plain. Login can be a 48px ghost pill.

### Brand Logo Lockup

White glyph/wordmark lockup at top left with slim Plain text. Keep it minimal and high contrast.

## Surfaces

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 0 | Void Canvas | `#03081a` | Page-level deep-space base. |
| 1 | Deep Indigo Card | `#020626` | Card and panel surface. |
| 2 | Light Content Surface | `#ffffff` | Light cards, dashboard mockups, and contrast panels. |

## Elevation

No drop shadows. Depth is created with `#292f66` and `#4d5499` hairline borders, subtle dark surface shifts, and generous rounding.

## Imagery

Use a large 3D translucent cobalt glass sculpture or liquid-chain form in the hero. It should occupy around 40% of the hero viewport. Beyond the hero, use product dashboard screenshots in rounded cards. Avoid lifestyle photography, people, environmental shots, and generic stock visuals.

## Layout

Use a 1200px centered container with 32-64px outer gutters. The hero is a full-bleed dark split: ultrathin headline on the left, 3D glass sculpture on the right. Product sections can use two-column layouts with text and CTA on the left, rounded dashboard card on the right, and tab pill navigation above. Keep 64px vertical gaps between major sections.

## Do

- Use Plain Ultrathin weight 100 for all large headings.
- Use 48px radius for buttons and nav pills.
- Use 35px radius for cards, panels, and content containers.
- Use Pulse Cobalt for primary filled actions and active states only.
- Use 0.25em tracking on 10px uppercase eyebrow labels.
- Use 1px violet hairlines instead of drop shadows.
- Use teal-to-cobalt gradients only on full-bleed banners.

## Don't

- Do not use 600 or 700 headline weights.
- Do not add drop shadows to cards or buttons.
- Do not use more than one vivid accent on the same surface.
- Do not use solid underlines for links.
- Do not set body copy below weight 300.
- Do not use sharp 0px or 4px corners on interactive elements.
- Do not introduce other dark canvas colors beyond Void Navy and Deep Indigo.

