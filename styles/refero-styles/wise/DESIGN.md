# Wise - Style Reference

> Deep moss with lime voltage: forest-green authority, sparse lime action, giant block display type, pill controls, and circular global identity markers.

## Theme

Light. Paper white is the default canvas, with Fog and Linen Mist for soft surfaces and Forest Ink for dark inverted sections. The brand energy comes from clean green inversions, not gradients.

## Design Story

Build around a confident finance-product voice. Use giant Wise Sans display headlines for hero and section openers, then let Inter handle the quieter product details. The UI should feel friendly, direct, global, and trustworthy.

Lime Voltage is powerful but sparse. Use it for primary actions, selected tabs, and key emphasis on dark green sections. Do not scatter multiple lime elements close together.

## Tokens - Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Forest Ink | `#163300` | `--color-forest-ink` | Dominant brand dark, dark sections, nav text, primary copy, icon strokes |
| Lime Voltage | `#9fe870` | `--color-lime-voltage` | Primary action fill, active tabs, highlight surfaces on dark green |
| Spruce | `#054d28` | `--color-spruce` | Secondary dark green for dark-section depth and supporting iconography |
| Linen Mist | `#e2f6d5` | `--color-linen-mist` | Pale green wash for soft highlights, tinted cards, nav hover states |
| Signal Blue | `#0b4c72` | `--color-signal-blue` | Low-frequency supporting accent |
| Alarm Red | `#cb272f` | `--color-alarm-red` | Low-frequency supporting accent, not a status system by default |
| Charcoal | `#454745` | `--color-charcoal` | Body text, dense UI text, softened black on white |
| Obsidian | `#0e0f0c` | `--color-obsidian` | Display headings and maximum contrast moments |
| Pebble | `#868685` | `--color-pebble` | Muted secondary text, placeholders, input borders, icon strokes |
| Slate | `#6a6c6a` | `--color-slate` | Supporting body text and helper labels |
| Fog | `#e8ebe6` | `--color-fog` | Card surfaces, soft panels, dividers, subtle section backgrounds |
| Paper | `#ffffff` | `--color-paper` | Page canvas, inverted cards, button text on lime fill |

## Typography

Display font: Wise Sans.

- Use Wise Sans weight 900 for display headlines at 89px to 105px.
- Use line-height 0.85 and tight negative tracking.
- Use for hero, section openers, and campaign-level statements.
- Fallback: Inter Black 900 with tight tracking.
- Do not use Inter for headings above 60px.

UI and body font: Inter.

- Use Inter for body, labels, nav, forms, feature rows, cards, and smaller headings.
- Use weights 400, 500, 600, and 700.
- Use tight tracking that increases with size.
- Enable `calt` when the font pipeline supports it.

## Type Scale

| Role | Size | Weight | Line height | Tracking |
| --- | --- | --- | --- | --- |
| Micro | 12px | 400 or 500 | 1.63 | -0.036px |
| Caption | 14px | 400 or 500 | 1.55 | -0.07px |
| Body Small | 16px | 400 | 1.5 | -0.096px |
| Body | 18px | 400 | 1.5 | -0.126px |
| Body Large | 25px | 400 or 500 | 1.3 | -0.225px |
| Subheading | 36px | 700 | 1.25 | -0.396px |
| Heading Small | 45px | 700 | 1.1 | -0.495px |
| Heading | 61px | 700 | 1.1 | -0.915px |
| Heading Large | 89px | 900 | 0.85 | -2.67px |
| Display | 105px | 900 | 0.85 | -3.15px |

## Spacing And Shape

- Base unit: 4px.
- Density: comfortable.
- Page max width: 1200px.
- Section gap: 64px to 80px.
- Card padding: 24px.
- Element gap: 8px to 12px.
- Tags: 9999px radius.
- Buttons: 9999px radius.
- Nav segments: 9999px radius.
- Cards: 10px radius.
- Inputs: 10px radius.
- Image masks and flags: 1000px radius.
- Large cards: 28px radius.

## Elevation

Use subtle structural shadows only:

- Hairline: `0 0 0 1px rgba(14, 15, 12, 0.12)`
- Inset line: `inset 0 0 0 1px #868685`
- Large card: `0 10px 32px rgba(0,0,0,0.15), 0 40px 40px rgba(0,0,0,0.04)`
- Panel: `0 6px 20px rgba(0,0,0,0.08)`

Avoid decorative glows, blurs, and gradients.

## Components

### Primary CTA Pill Button

Fully rounded button with Lime Voltage fill and Charcoal or Forest Ink text. Use Inter 500 at 16px, 11px vertical padding, and 24px horizontal padding. No border and no shadow. Use one primary lime action per visible section.

### Outlined Pill Button

White fill, 1px Forest Ink border, Forest Ink text, full pill radius, same 16px Inter 500 voice. Use for account actions such as sign up or for secondary CTAs when lime would compete with another active state.

### Text Link Button

Forest Ink underlined text at 16px Inter 500. Use as the secondary action next to a filled primary CTA. Do not place two filled CTAs side by side.

### Top Navigation Bar

White background, about 64px tall. Logo on the left. Center uses a pill segmented switcher for Personal, Business, and Platform. Right cluster includes flag/language, Help, Log in, and outlined Sign up pill.

### Segmented Tab Control

Full pill container with multiple labels. Active tab uses Lime Voltage fill and Charcoal text. Inactive tabs are transparent with Charcoal text. Height is about 40px with 12px horizontal padding per segment.

### Display Headline

Wise Sans 900 at 89px to 105px, line-height 0.85, and tight negative tracking. Use Obsidian or Forest Ink on light sections; use Lime Voltage on Forest Ink sections.

### Feature Row

Three-column trust signal block on desktop, single column on mobile. Each item has a 24px Charcoal stroke icon, Inter 700 18px heading, and Inter 400 16px Pebble body.

### Country Grid Item

Circular flag thumbnail around 56px, 12px gap, and country name in Inter 500 16px Forest Ink. Use a 5-column desktop grid with generous 32px row gaps. Underline country names on hover.

### Dark Section Card

Forest Ink background, 28px radius, 40px padding. Use Lime Voltage for the headline, Paper for body text, and a nested white card for currency selectors.

### Currency Selector Pill

White pill inside a dark card. Left side has circular flag and country name in Charcoal. Right side has an outlined Change button in Forest Ink. Use full pill radius and 8px vertical padding.

### Input Field

10px radius, 1px Pebble border, 12px vertical and 16px horizontal padding. Inter 400 at 16px. Focus state uses Forest Ink border with no glow ring.

### Floating QR Badge

Fixed bottom-right badge, Forest Ink background, 16px radius, about 120px wide. QR code in Paper at top; label uses Lime Voltage Inter 500 12px below.

## Layout

Use a centered 1200px container for regular content, while hero and dark sections can go full-bleed. The rhythm alternates Paper, Fog, Linen Mist, and Forest Ink. Hero uses a centered display headline and a large painted globe illustration breaking the lower viewport. Supporting sections use two-column text and visual compositions, three-column feature rows, and a five-column country grid.

## Imagery

Use painted 3D-style illustrations of a globe and coins as the brand motif. Country flags appear as circular thumbnails. Photography is minimal and casual when used. Avoid abstract patterns, heavy stock photography, and decorative gradients.

## Rules

Do:

- Use Wise Sans 900 for display type above 60px.
- Use Lime Voltage sparingly for action and active states.
- Default to pill shapes for buttons, tags, nav segments, and tabs.
- Use Forest Ink instead of pure black for brand-dark surfaces.
- Use Charcoal instead of pure black for body text.
- Pair a filled CTA with an underlined text link.
- Invert sections to Forest Ink for rhythm.

Do not:

- Do not set display headlines in Inter.
- Do not use Lime Voltage as body text on light backgrounds.
- Do not stack many lime elements in one viewport.
- Do not introduce gradients, decorative blurs, or heavy drop shadows.
- Do not use sharp corners on buttons, tags, or nav.
- Do not use pure black for normal body copy.
