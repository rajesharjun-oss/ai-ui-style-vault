# Cal.com Style Reference

## Summary

Cal.com is a compact monochrome utility system. It feels like a precise scheduling instrument: mostly black, white, and controlled grays, with rounded action shapes and subtle shadows that keep the page human instead of harsh.

The product is the visual center. Use scheduling widgets, calendar cards, availability grids, meeting cards, integration logos, and compact workflow components. Avoid decorative imagery. The system wins by being useful, direct, and quiet.

## Theme

Light.

## Personality

- Monochrome
- Precise
- Functional
- Friendly
- Compact
- Product-led
- Rounded
- Scheduling-first

## Color System

Use monochrome for nearly all UI. Action Blue is rare and functional. Google colors are allowed only inside integration logos.

| Name | Value | Token | Use |
| --- | --- | --- | --- |
| Ink | `#101010` | `--color-ink` | Primary CTAs, active states, strongest UI text |
| Graphite | `#242424` | `--color-graphite` | Headlines and primary body text |
| Slate | `#6b7280` | `--color-slate` | Secondary text, descriptions, disabled states |
| Stone | `#898989` | `--color-stone` | Placeholder text and quiet decorative UI |
| Silver | `#e5e7eb` | `--color-silver` | Borders, dividers, and subtle fills |
| Paper | `#f4f4f4` | `--color-paper` | Main page background |
| White | `#ffffff` | `--color-white` | Card surfaces and text on dark buttons |
| Info Banner BG | `#eff6fe` | `--color-info-banner-bg` | Pale information banner background |
| Action Blue | `#0099ff` | `--color-action-blue` | Rare secondary links and information highlights |
| Google Blue | `#4285f4` | `--color-google-blue` | Google integration logo only |
| Google Yellow | `#fbbc04` | `--color-google-yellow` | Google integration logo only |
| Google Green | `#34a853` | `--color-google-green` | Google integration logo only |
| Google Red | `#ea4335` | `--color-google-red` | Google integration logo only |

## Typography

Cal Sans gives the page its identity, but it is for headings. Body copy uses a lighter UI face with compact negative tracking. Smaller utility labels can use Inter or Matter.

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| Display | 64px | 600 | 1.1 | 0.64px |
| Heading Large | 48px | 600 | 1.1 | 0.48px |
| Heading | 24px | 600 | 1.3 | 0.24px |
| Heading Small | 20px | 600 | 1.3 | 0.2px |
| Subheading | 18px | 300 | 1.4 | -0.2px |
| Body | 16px | 300 | 1.5 | -0.19px |
| Body Small | 14px | 500 | 1.5 | -0.2px |
| Caption | 12px | 400 | 1.4 | -0.24px |

## Font Roles

- Cal Sans: headings at 20px and above, weight 600.
- Cal Sans UI Variable Light: body and primary UI copy, weight 300.
- Inter: small labels, calendar controls, complex UI text, weights 400, 500, 600.
- Matter: captions and metadata where neutral legibility is needed.

## Spacing And Shape

- Density: compact
- Max width: 1200px
- Section gap: 96px
- Card padding: 24px
- Scheduling widget padding: 16px
- Primary and secondary page CTAs: 9999px radius
- Header CTA: 8px radius
- Inputs: 8px radius
- Cards: 12px radius
- Tags: 9999px radius

## Elevation

Cards use subtle, diffuse gray shadows. Shadows separate cards more than borders do.

```css
box-shadow: rgba(36, 36, 36, 0.05) 0 4px 8px 0;
```

Use a slightly richer shadow on hover or focused cards:

```css
box-shadow: rgba(36, 36, 36, 0.7) 0 1px 5px -4px,
  rgba(36, 36, 36, 0.05) 0 4px 8px 0;
```

## Components

### Primary CTA Button

Pill button with Ink background, White text, 9999px radius, Cal Sans UI at 14px to 16px, and about 12px vertical by 24px horizontal padding.

### Secondary Ghost Button

Pill button with transparent or Paper background, Graphite text, 1px Silver border, 9999px radius, and the same sizing as the primary CTA.

### Header CTA Button

Compact rectangular button in the sticky header. Ink background, White text, 8px radius, Cal Sans UI at 14px, and about 8px vertical by 16px horizontal padding.

### Tag Button

Small pill used for filters or categories. Use Paper or Silver fill, Graphite text, 9999px radius, and about 4px vertical by 12px horizontal padding.

### Scheduling Widget Card

The hero component. White surface, 12px radius, 16px padding, subtle shadow, and an interactive calendar or booking UI inside. It should feel like the real product, not decoration.

### Feature Card

White card, 12px radius, 24px padding, subtle shadow. Include a small tag or number, a 20px Cal Sans heading, and compact body text.

### Navigation Link

Text-only Graphite link, Cal Sans UI at 14px to 16px, no underline by default.

### Information Banner

Pale blue background with Action Blue text or links. Keep it informational, not promotional.

### Integration Logo Row

Logos may use their own colors. Confine multicolor accents to the logo artwork and do not echo those colors in page chrome.

## Layout

Use a centered 1200px container with generous side breathing room and deliberate 96px vertical section gaps. The hero usually pairs a large headline stack with a prominent scheduling widget card. Below the hero, use centered section headings followed by 3-column feature cards or alternating text-and-product blocks.

## Imagery

Imagery is product-centric and contained. Use:

- Scheduling widgets.
- Calendar UIs.
- Availability grids.
- Meeting booking cards.
- Integration logos.
- Product screenshots.

Do not use lifestyle photography, abstract graphics, or full-bleed illustration.

## Do

- Use Cal Sans weight 600 for headings 20px and above.
- Keep 99 percent of the core UI monochrome.
- Use pill CTAs for primary and secondary page actions.
- Use 12px radius for content cards and large containers.
- Use subtle diffuse shadows for card elevation.
- Use Cal Sans UI Variable Light for body copy with tight tracking.
- Reserve Action Blue for rare links and informational highlights.

## Do Not

- Do not introduce new colors into core UI.
- Do not use sharp corners on buttons or cards.
- Do not use font weights above 600.
- Do not use heavy bordered cards.
- Do not use gradients on buttons or card backgrounds.
- Do not set body text in Cal Sans; reserve it for headings.
- Do not let integration colors escape outside logos.
