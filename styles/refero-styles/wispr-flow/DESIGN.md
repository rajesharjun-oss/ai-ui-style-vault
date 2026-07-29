# Wispr Flow Style Reference

## Summary

Wispr Flow is an editorial software system: warm cream paper, deep black chambers, lavender action surfaces, and classical serif headlines at enormous scale. It should feel like a broadsheet with voice-product controls layered into it.

The layout alternates bright cream sections and dark rounded chambers. Every important component has a visible 2px ink edge. Elevation comes from color contrast, section alternation, and radius, not shadows.

## Theme

Mixed.

## Personality

- Editorial
- Warm
- Voice-led
- Border-driven
- Softly rounded
- Print-inspired
- Confident
- Human

## Color System

The working palette is disciplined: cream, ink, lavender, forest teal, and rare ember. Do not import ordinary SaaS blues or greens.

| Name | Value | Token | Use |
| --- | --- | --- | --- |
| Lavender Whisper | `#f0d7ff` | `--color-lavender-whisper` | Primary CTA fill and accent card surfaces |
| Forest Ink | `#034f46` | `--color-forest-ink` | Secondary brand surface, teal badges, inner dark-panel cards |
| Ember Glow | `#ffa946` | `--color-ember-glow` | Live states, active mic indicators, notification dots |
| Vast Ink | `#1a1a1a` | `--color-vast-ink` | Primary text, borders, dark section backgrounds |
| Charcoal | `#222222` | `--color-charcoal` | Secondary button and nav text |
| Fog | `#8a8a80` | `--color-fog` | Muted captions, helper text, de-emphasized labels |
| Lumen Stone | `#e4e4d0` | `--color-lumen-stone` | Subtle dividers, nav pill background, low-contrast separation |
| Lumen Cream | `#ffffeb` | `--color-lumen-cream` | Main page canvas, cream cards, button fills, light text on dark |
| Pure White | `#ffffff` | `--color-pure-white` | Badge borders on dark surfaces, icon strokes, light text on color |

## Typography

Use Eb Garamond for display and editorial headings. Use Figtree for body, UI labels, nav, buttons, and badges.

| Role | Font | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- | --- |
| Display | Eb Garamond | 120px | 400 | 0.85 | -3.6px |
| Heading Large | Eb Garamond | 64px | 400 | 0.95 | -1.92px |
| Heading | Eb Garamond | 48px | 400 | 0.95 | normal |
| Heading Small | Eb Garamond | 32px | 400 | 1.3 | -0.96px |
| Subheading | Figtree | 24px | 400 | 1.3 | normal |
| Body | Figtree | 20px | 400 | 1.3 | normal |
| Body Small | Figtree | 16px | 400 | 1.3 | normal |
| Caption | Figtree | 14px | 400 | 1.3 | normal |

## Font Rules

- Do not use bold display serif.
- Display authority comes from size and tight leading.
- Use Eb Garamond weight 400 for 32px, 48px, 64px, and 120px headings.
- Use Figtree 400 as the default body and UI weight.
- Reserve Figtree 500 to 700 for button labels, nav items, and badges.

## Spacing And Shape

- Base unit: 8px
- Density: comfortable
- Max width: 1200px
- Section gap: 64px to 96px
- Card padding: 32px
- Element gap: 8px to 16px
- Inputs: 12px radius
- Buttons: 12px radius
- Cards: 32px radius
- Badges: 9999px radius
- Sections: 40px to 80px radius

## Surfaces

| Level | Surface | Value | Role |
| --- | --- | --- | --- |
| 0 | Cream Canvas | `#ffffeb` | Default warm paper-like background |
| 1 | Dark Chamber | `#1a1a1a` | Alternating dark section and card background |
| 2 | Lavender Accent | `#f0d7ff` | Action fill and accent card surface |
| 3 | Forest Panel | `#034f46` | Secondary accent, badges, inner dark cards |

## Elevation

No box shadows. Separation comes from:

- Flat fill changes.
- 2px ink borders.
- Large 32px to 80px radii.
- Alternation between cream and dark chambers.

## Components

### Primary CTA Button

Lavender Whisper fill, Vast Ink text, 2px Vast Ink border, 12px radius, Figtree 500 at 16px, 14px compact padding or 16px by 24px standard padding. May include a platform icon prefix.

### Outlined Secondary Button

Lumen Cream fill, Vast Ink text, 2px Vast Ink border, 12px radius, Figtree 500 at 16px, 16px by 24px padding.

### Ghost Text Button

No background, no border, Vast Ink text, Figtree 400 at 16px, underline on hover.

### Floating Navigation Pill

Lumen Cream pill with 9999px radius and 2px Vast Ink border. Contains logo, nav items, chevrons, and a lavender CTA pinned to the right.

### Cream Content Card

Lumen Cream fill, 32px radius, 32px padding, no shadow, optional 2px Vast Ink border. Keep 32px radius even on smaller cards.

### Dark Feature Card

Vast Ink fill, 40px to 80px radius, 55px to 70px padding, no shadow, Lumen Cream text. These should feel like dark velvet rooms.

### Teal Status Badge

Forest Ink fill, Lumen Cream text, 1000px radius, 8px by 16px padding, Figtree 500 at 14px. May include a checkmark or icon prefix.

### Platform Pill Badge

Transparent fill on dark backgrounds, Lumen Cream text, 1px to 2px Pure White border, full pill radius, 8px by 16px padding, platform icon prefix.

### Dark Square Badge

Vast Ink fill, Lumen Cream text, 8px radius, 8px by 16px padding. This tight radius is a deliberate counterpoint to the dominant soft geometry.

### Waveform Visualizer

Cream pill with 9999px radius and 2px Vast Ink border. Interior uses 5 to 7 vertical Vast Ink bars from 8px to 24px tall. Animate bars for active recording.

### Phone Mockup

Flat dark device frame with 40px radius. Screen shows cream chat bubbles, avatar circle, and waveform visualizer. Avoid photorealistic bezel effects.

### Section Container

Alternating Lumen Cream and Vast Ink full-bleed bands. Use 40px to 80px outer radius and 64px to 96px vertical gaps.

### Hand-Drawn Underline Accent

Lavender Whisper SVG wavy underline beneath one or two headline words. Use 3px to 4px stroke and slight path irregularity.

## Layout

Use centered 1200px max-width content with full-bleed section backgrounds. The hero is a centered serif headline on cream canvas with floating nav above and a single CTA below. Dark chambers alternate with cream sections and use big rounded corners.

Feature sections commonly use text-left and visual-right layouts, with a phone mockup or waveform element on the visual side. Data sections may use side-by-side comparison cards. Keep 64px to 96px between major sections and 8px to 16px between related elements.

## Imagery

Imagery is sparse and editorial. Use app icons in rows, flat phone mockups, waveform visualizers, curved text arcs, and lavender hand-drawn underlines. Photo backgrounds may appear only inside dark feature cards as blurred, low-contrast atmosphere.

Avoid stock photography, abstract gradients, glossy 3D renders, and generic illustration.

## Do

- Use Lavender Whisper as the sole primary action color.
- Keep display headlines in Eb Garamond weight 400.
- Apply 2px Vast Ink borders to interactive elements.
- Alternate cream and dark sections page-wide.
- Use 32px radius on standard cards.
- Use 40px to 80px radius on dark chambers.
- Use Figtree 400 as default body weight.
- Pair Lavender Whisper with Forest Ink as complementary brand colors.

## Do Not

- Do not use bold display serif.
- Do not use box shadows for card elevation.
- Do not introduce blue or unrelated action colors.
- Do not use button radii below 12px.
- Do not use card radii below 32px.
- Do not use gradients.
- Do not center body text.
- Do not place cream content on cream canvas without a border or background change.
