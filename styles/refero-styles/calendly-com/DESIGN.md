# Calendly.com - Style Reference

> Navy ink on cool marble.

Theme: light

Calendly.com is a calm scheduling SaaS style built around cool near-white surfaces, generous spacing, crisp product cards, and deep navy text. The key move is using Ink Navy for nearly all text, icons, buttons, and links, which keeps the interface softer and more editorial than pure black.

Signal Blue carries primary action and active states. Magenta and cyan appear as decorative blobs behind product mockups, never as UI fills. Cards use generous radii, thin borders, and blue-tinted shadows so product screenshots float over the Cloud canvas without feeling heavy.

## Tokens - Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Ink Navy | `#0b3558` | `--color-ink-navy` | Primary text, headings, icons, dark CTA fills, and nav links. |
| Signal Blue | `#006bff` | `--color-signal-blue` | Primary CTA fill, active nav, selected states, and link accents. |
| Deep Cobalt | `#004eba` | `--color-deep-cobalt` | Badge text and informational labels. |
| Slate Gray | `#476788` | `--color-slate-gray` | Secondary copy, helper text, and muted labels. |
| Mist Gray | `#a6bbd1` | `--color-mist-gray` | Disabled text, inactive labels, and light icon strokes. |
| Hairline | `#d4e0ed` | `--color-hairline` | Card borders, input borders, dividers, and underline defaults. |
| Pebble | `#f0f3f8` | `--color-pebble` | Badge backgrounds, input fills, subtle dividers, and hover washes. |
| Cloud | `#f8f9fb` | `--color-cloud` | Page canvas, footer, and secondary surfaces. |
| Paper | `#ffffff` | `--color-paper` | Card surfaces, elevated panels, and text on dark fills. |
| Carbon | `#0a0a0a` | `--color-carbon` | Pure-black fallback and logo glyphs only. |
| Coral Magenta | `#e55cff` | `--color-coral-magenta` | Decorative accent blob behind product cards. |
| Sky Cyan | `#0099ff` | `--color-sky-cyan` | Decorative accent blob and gradient wash partner. |

## Tokens - Typography

### Gilroy

Geometric humanist sans for the full interface.

- Substitute: Manrope, Inter, system-ui, sans-serif
- Weights: 400, 500, 600, 700
- Sizes: 12px, 14px, 16px, 18px, 20px, 24px, 28px, 38px, 50px, 68px, 80px
- Letter spacing: normal across sizes
- Role: all interface text
- Rule: 700 carries hero and section headlines, 600 carries buttons and subheads, 500 carries labels and card titles, 400 carries body.

### Type Scale

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| caption | 12px | 500 | 1.5 | 0 |
| body-sm | 14px | 500 | 1.4 | 0 |
| body | 16px | 400 | 1.0 | 0 |
| button | 18px | 600 | 1.6 | 0 |
| body-lg | 20px | 500 | 1.4 | 0 |
| subheading-sm | 24px | 600 | 1.4 | 0 |
| subheading | 28px | 600 | 1.4 | 0 |
| heading-sm | 38px | 700 | 1.21 | 0 |
| heading | 50px | 700 | 1.2 | 0 |
| heading-lg | 68px | 700 | 1.2 | 0 |
| display | 80px | 700 | 1.2 | 0 |

## Tokens - Spacing And Shape

- Density: comfortable
- Base unit: 8px
- Page max width: 1200px
- Section gap: 48px to 64px
- Card padding: 24px
- Element gap: 8px to 16px
- Scale: 8, 16, 24, 32, 40, 48, 56, 64, 72, 96px

### Radius

| Element | Value |
| --- | --- |
| Small details | 4px |
| Inputs | 8px |
| Buttons | 8px |
| Product cards | 16px |
| Feature panels | 24px |
| Badges | 9999px |

### Elevation

Use blue-tinted shadows rather than neutral black shadows:

- Elevated card: `rgba(71, 103, 136, 0.04) 0 4px 5px, rgba(71, 103, 136, 0.03) 0 8px 15px, rgba(71, 103, 136, 0.08) 0 30px 50px`
- Link card: `rgba(71, 103, 136, 0.04) 0 4px 5px, rgba(71, 103, 136, 0.03) 0 4px 10px, rgba(71, 103, 136, 0.05) 0 10px 20px`
- Button: `rgba(71, 103, 136, 0.04) 0 4px 5px, rgba(71, 103, 136, 0.03) 0 8px 15px, rgba(71, 103, 136, 0.06) 0 15px 30px`

## Components

### Primary CTA Button

Filled Signal Blue button with white text, 18px Gilroy weight 600, 8px radius, no border, and compact or comfortable padding. Use for the main action such as sign-up, get started, or start free.

### Dark CTA Button

Filled Ink Navy button with white text, 18px weight 600, and 8px radius. Use as a secondary filled action or provider-specific sign-in button.

### Ghost Text Link

No background, no border, Ink Navy text at 14px to 18px with weight 500 or 600. Use for inline actions such as integrations, learn more, and view all.

### Outlined White Button

White text and white border with transparent fill. Use only on dark or image backgrounds. Radius is 4px for this variant.

### Social Sign-In Button

Full-width sign-in control with provider logo at left. Google variant uses Paper fill, Ink Navy text, and Hairline border. Microsoft variant uses Ink Navy fill and white text. Both use 8px radius and 12px by 16px padding.

### Elevated Product Card

White surface, 16px radius, no internal padding when the screenshot fills the card, and blue-tinted shadow stack. Place a Coral Magenta or Sky Cyan blob behind it, offset by 20px to 40px.

### Feature Accordion Item

Active item uses Ink Navy heading and Signal Blue icon. Inactive item uses Mist Gray text. Include a left icon, right chevron, and Hairline divider.

### Pill Badge

Pebble-tinted background, Deep Cobalt text at 12px weight 500, 50px or full radius, and 4px by 8px padding. Use for savings, hiring, and low-emphasis status.

### Trust Logo Strip

Single row of muted partner logos in Mist Gray. No card, border, or background. Let logos float on the canvas.

### Booking Widget Card

White scheduling preview card with 16px radius. Use three zones: organizer info, date grid, and time slots. Selected dates and active time slots use Signal Blue.

### Section Header Block

Centered H2 at 50px to 68px weight 700 in Ink Navy, with Slate Gray support copy below and optional CTA. Keep the copy max width around 640px.

### Footer

Cloud background with link columns. Use Ink Navy links at 14px weight 500 and Slate Gray uppercase headings at 12px weight 600.

## Layout

Use a centered 1200px max-width layout with generous desktop margins. The hero is a two-column split: headline, copy, and sign-in buttons on the left; booking widget card and decorative blobs on the right. A trust logo strip usually follows the hero.

Subsequent sections prefer centered header blocks followed by two-column feature blocks. Alternate text-left/product-right and product-left/text-right. Card grids are rare. Navigation is a 64px sticky top bar with logo left, centered menu, and CTA cluster right.

## Imagery

Product screenshots are the primary visuals. Use clean scheduling UI mockups on white cards with generous corner radius. Place magenta or cyan blobs behind them, offset and softly blurred. Avoid photography and lifestyle imagery.

Icons should be line-style at 1.5px to 2px stroke, in Ink Navy or Signal Blue.

## Do

- Use Ink Navy for all primary text.
- Use Signal Blue only for filled primary CTAs and selected states.
- Use 16px radius for product cards and 24px for larger feature panels.
- Use blue-tinted shadows for all elevation.
- Use Gilroy 700 at 50px to 80px for hero and section headlines.
- Place product visuals in front of magenta or cyan decorative blobs.
- Keep buttons at 8px radius.

## Do Not

- Do not use pure black for regular text.
- Do not use neutral black shadows.
- Do not use magenta or cyan as UI fills.
- Do not make buttons pill-shaped.
- Do not make H2 headings too small.
- Do not use Deep Cobalt as a CTA color.
- Do not add gradients to page backgrounds.
- Do not place blue and navy CTAs too close without spacing.

