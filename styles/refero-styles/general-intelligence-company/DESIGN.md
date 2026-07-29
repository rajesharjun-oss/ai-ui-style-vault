# General Intelligence Company - Style Reference

> Literary journal beside a bonfire.

Theme: light

General Intelligence Company reads like a quiet editorial research site for an AI company. The base is warm off-white rather than sterile white. Painted atmospheric scenes create the emotional peaks, while the usable interface stays restrained: white content blocks, thin green-gray borders, compact labels, and a single blue action accent.

Typography is the main brand signal. Use `ppmondwest` for display and editorial copy at 27px and above, with light weights and tight tracking. Use `af` for body, nav, labels, buttons, and data-heavy UI. The result should feel set, edited, and thoughtful, not like generic marketing software.

## Tokens - Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Parchment | `#fefffc` | `--color-parchment` | Warm base canvas with a book-page feel. |
| Paper | `#ffffff` | `--color-paper` | Cards, content bands, footer, and clean elevated areas. |
| Linen | `#f9faf7` | `--color-linen` | Input fields, subtle washes, and low-opacity nav fill. |
| Ink Black | `#171717` | `--color-ink-black` | Strong foreground text where maximum contrast is needed. |
| Graphite | `#2c2c2c` | `--color-graphite` | Headlines and important body copy. |
| Charcoal | `#444141` | `--color-charcoal` | Secondary copy, button labels, and everyday UI text. |
| Ash | `#646464` | `--color-ash` | Muted descriptions, helper text, and quiet metadata. |
| Fog | `#b4b8b4` | `--color-fog` | Disabled states and tertiary border tones. |
| Mist | `#dee2de` | `--color-mist` | Signature hairline border for cards, buttons, and dividers. |
| Twilight | `#282834` | `--color-twilight` | Cool near-black for nav borders, icons, and neutral outlines. |
| Dusk | `#1f1f29` | `--color-dusk` | Rare filled dark button and high-emphasis dark surface. |
| Signal Blue | `#41a1cf` | `--color-signal-blue` | Outlined action border, links, and lightweight emphasis. |
| Cerulean | `#0081c0` | `--color-cerulean` | Rare saturated illustration or atmospheric surface. |

## Tokens - Typography

### ppmondwest

Custom display serif for headings and editorial copy.

- Substitute: Fraunces, Recoleta, GT Sectra, serif
- Weights: 400, 500
- Sizes: 27px, 40px, 48px, 54px
- Line height: 1.1 for display, 1.5 for lead editorial copy
- Letter spacing: about -0.04em at 27px and -0.02em from 40px to 54px
- OpenType: disable standard ligatures when the font supports it
- Rule: keep the weight light. The serif shape carries the emphasis.

### af

Custom sans for product UI, body copy, nav, labels, and buttons.

- Substitute: Inter, Geist, Sohne, system-ui, sans-serif
- Weights: 400, 500, 600, 700
- Sizes: 13px, 15px, 16px, 18px
- Line height: 1.0 for compact nav, 1.3 for small headings, 1.5 for readable body text
- Letter spacing: slight negative tracking around -0.01em
- Rule: use 500 for controls and labels, 400 for body.

### Type Scale

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| caption | 13px | 500 | 1.3 | -0.13px |
| body-sm | 15px | 500 | 1.0 | -0.15px |
| body | 16px | 400 | 1.5 | -0.16px |
| subheading | 18px | 500 | 1.3 | -0.18px |
| heading-sm | 27px | 400 | 1.5 | -1.08px |
| heading | 40px | 500 | 1.1 | -0.8px |
| heading-lg | 48px | 500 | 1.1 | -0.96px |
| display | 54px | 400 | 1.1 | -1.08px |

## Tokens - Spacing And Shape

- Density: comfortable
- Base unit: 4px
- Page max width: 1200px
- Section gap: 32px to 64px
- Large editorial breathing room: 64px to 96px
- Card padding: 16px
- Element gap: 8px to 12px
- Main scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80px

### Radius

| Element | Value |
| --- | --- |
| Buttons | 4px or 8px |
| Cards | 12px or 16px |
| Large illustrated surfaces | 24px |
| Floating nav pill | 50px |

### Elevation

- Use soft shadows for nav, content cards, diagram cards, and atmospheric panels.
- Buttons should not rely on shadows.
- The main edge language is a 1px green-tinted hairline, not heavy elevation.

## Components

### Frosted Navigation Pill

Top-centered floating pill with a translucent light fill, backdrop blur, 50px radius, and a 1px border. It holds a small landscape/sun mark, a few short nav links, and a compact outlined CTA. It should look like it is floating above the illustrated hero.

### Primary Outlined CTA

Transparent button with 8px radius, 1px `#41a1cf` border, matching blue text, and compact padding. Use it as an outline, not a filled blue button. Pair it with a small arrow or directional icon when appropriate.

### Secondary Outlined Button

Same compact button geometry as the primary CTA, but with `#282834` for border and text. Use for neutral secondary actions beside the blue outline.

### Filled Dark Button

Rare high-emphasis button with `#1f1f29` fill, white text, `#282834` border, and 8px radius. Use in footer or conversion-heavy moments only.

### Ghost Text Link

Borderless text action in charcoal or twilight, often paired with a simple arrow icon. Good for editorial links and tertiary navigation.

### Frosted Hero Overlay Card

Glasslike card over a painted hero scene. Use 24px radius, translucent background, backdrop blur, and generous padding. Text can switch between dark and white depending on the image behind it.

### White Content Card

Paper-white card with 12px radius, `#dee2de` border, and a soft layered shadow. Use for article excerpts, explanations, content blocks, and product copy.

### Atmospheric Illustration Card

Large 24px-radius illustrated or color field section. This is where saturated color can appear, especially cerulean. Keep it rare so it feels like punctuation.

### Diagram Card

Soft framed container for line-art explanations, coordinator diagrams, and agent systems. Use 16px radius, semitransparent white, subtle shadow, and compact internal padding.

### Input Field

Paper-form input with `#f9faf7` fill, charcoal text, and a bottom border. Keep the top and side borders visually absent. The field should feel editorial and quiet.

### Cookie Banner

Small white notification surface with compact sans text and text-only Accept or Decline actions. Keep urgency low and avoid loud accent use.

### Footer

White editorial band with a large serif statement and compact sans link groups. Treat it like the colophon of a publication.

## Layout

Build vertically, alternating immersive illustrated sections with clean content bands. The hero can be 100vh with the nav pill floating near the top and a frosted editorial card anchored near the bottom. Content sections should be centered around a 1200px max width with generous vertical spacing.

Diagram sections often work as a 6-column plus 6-column split: explanatory text on one side and a framed diagram on the other. Avoid dense dashboards. Give each screen one clear idea.

## Imagery

Use painted digital illustrations with atmosphere and texture: night skylines, meadow scenes, warm fields, or carefully stylized pixel-art interruptions. Avoid stock photography, product screenshot collages, glossy 3D blobs, and generic vector art. Icons should stay minimal and line-based.

## Do

- Use the serif for any heading 27px and above.
- Keep display weights at 400 or 500.
- Use `#dee2de` as the recurring hairline border.
- Keep buttons compact and outlined.
- Use `#41a1cf` as an outline or link accent, not as a filled CTA.
- Keep the page canvas warm with `#fefffc`.
- Pair display text with 1.1 line height and body text with 1.5.

## Do Not

- Do not use pure black for text.
- Do not add shadows to buttons.
- Do not introduce extra accent colors.
- Do not use heavy weights on the display serif.
- Do not make body text translucent.
- Do not use radii above 24px except for the nav pill.
- Do not fill primary buttons with blue.

