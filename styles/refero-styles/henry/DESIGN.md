# Henry - Style Reference

Theme: mixed

Henry's Refero style is a warm monochrome broadside. It feels printed rather than rendered: near-black ink on cream paper, then inverted cream type on ink sections. There is no color accent, no product art, no shadows, and no gradient system. The brand is typography: huge serif headlines, stamped ultra-condensed mastheads, tight grotesque UI text, and full-bleed section flips.

## Core Principles

- Use Paper and Ink as the primary binary.
- Let typography carry the visual intensity.
- Use no chromatic accent colors.
- Alternate full-bleed Paper and Ink sections.
- Keep all cards, buttons, and tags at 12px radius.
- Use no shadows, glow, gradients, or elevated panels.
- Keep imagery monochrome and halftone.
- Use dense regions sparingly: ticker bands, bylines, and small editorial metadata.

## Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Paper | `#fafafa` | `--color-paper` | Cream-white page ground, card surface, and inverted section text. |
| Headline Ink | `#2a2722` | `--color-headline-ink` | Primary text, body ink, rules, borders, and dark section background. |
| Sepia | `#3e3b36` | `--color-sepia` | Strong secondary border or darker supporting heading text. |
| Ash | `#666666` | `--color-ash` | Muted UI text, secondary borders, and low-emphasis dividers. |
| Midstone | `#9f9f9f` | `--color-midstone` | Muted borders and light decorative rules on dark sections. |
| Pebble | `#b3b3b3` | `--color-pebble` | Inactive nav text and quiet borders. |
| Hairline | `#eeeeee` | `--color-hairline` | Subtle card and tile borders on Paper. |

## Typography

### Fonts

- UI/body: Neue Montreal.
- UI fallback: Inter, Sohne, General Sans, system-ui, sans-serif.
- Editorial display: Louize Display.
- Editorial fallback: Fraunces, GT Sectra, Lyon Display, Georgia, serif.
- Short serif copy: Louize.
- Masthead display sans: Manuka.
- Masthead fallback: Druk, Condor, Antonio, Impact, sans-serif.

### Type Scale

| Role | Size | Weight | Line Height | Tracking | Use |
| --- | --- | --- | --- | --- | --- |
| caption | 12px | 400 or 700 | 1.5 | -0.12px | Ticker, nav, tags, metadata. |
| body | 16px | 400 | 1.5 | -0.16px | Body copy and UI text. |
| subheading | 20px | 400 or 700 | 1.3 | -0.2px | Small UI headings. |
| heading-sm | 24px | 400 | 1.2 | -0.24px | Short Louize copy and ticker names. |
| heading | 32px | 400 | 1.1 | -0.32px | Editorial letter body and small headlines. |
| heading-lg | 77px | 400 | 0.9 | 0 | Section hero headline. |
| display | 132px | 400 | 0.8 | 0 | Marquee serif headline. |
| display-xl | 371px | 400 | 0.75 | 0 | Extreme Manuka masthead. |

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | comfortable |
| Base unit | 4px |
| Section gap | 64-96px |
| Card padding | 16px |
| Element gap | 16px |

### Spacing Scale

`4px`, `8px`, `12px`, `16px`, `20px`, `24px`, `32px`, `64px`, `80px`, `224px`

### Radius

| Element | Value |
| --- | --- |
| cards | 12px |
| buttons | 12px |
| tags | 12px |

## Components

### Masthead Display Headline

Large Louize Display headline at 116-132px, weight 400, line-height around 0.8. Use Headline Ink on Paper or Paper on Ink. Italic fragments can sit inside the same typographic block at a smaller size. Do not add icons or decoration.

### Stamped Display Section Header

Manuka at 226-371px, uppercase, one weight, one color. Use as a full-bleed section stamp on Paper or Ink. The oversized condensed letterforms are the section identity.

### Top Ticker Banner

Full-bleed announcement strip above the masthead. Use Neue Montreal 12px, uppercase, tight negative tracking, and thin horizontal rules. Padding is only 4-6px vertical.

### Inverted Editorial Letter

Full-bleed Ink section with centered Louize Display/Louize editorial copy in Paper. Use optional tiny Neue Montreal eyebrow labels above and below. Align this serif block center only inside Ink sections.

### Nav Link Uppercase

Top-left navigation items in Neue Montreal 12-16px, bold, uppercase, Headline Ink. No underline, no bar, no background. Active state uses scale, not color.

### Section Divider Rule

Full-bleed 1px rule in Headline Ink on Paper or Paper on Ink. It is structural and typographic, not decorative.

### Brand Ticker Strip

Full-bleed Ink band with repeated Louize wordmarks in Paper. Keep gaps tight and horizontal. This is one of the few intentionally dense areas.

### Coming Soon Tag

Outlined ghost tag with 12px radius, 1px Paper border, uppercase Neue Montreal 12px, and 4px 8px padding. No fill.

### Coordinate Footer

Small uppercase metadata line in Neue Montreal 12px with tight tracking. Use coordinate, time, location, and byline-like information. Keep it monochrome.

### Hero Halftone Plate

Square or full-height monochrome halftone illustration block, often on the right side of the hero. No radius, no color, no caption, and no overlap tricks.

### Footnotes And Meta Line

Small all-caps caption beneath a major work or editorial entry. Use Neue Montreal 12px with tight tracking and Headline Ink.

## Surfaces

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 1 | Paper | `#fafafa` | Cream-white page canvas and default background. |
| 2 | Ink | `#2a2722` | Full-bleed dark section surface with Paper text. |

## Elevation

There is no elevation. Hierarchy comes from typography, full-bleed inversion, and 1px rules. Do not add card shadows, drop shadows, glow, blur, or Material-style depth.

## Imagery

Use monochrome halftone illustration only. Avoid photography, color images, gradients, product screenshots, UI pictograms, and icon sets. Client/social-proof marks should be rendered as text or wordmarks, not image-logo strips.

## Layout

Use full-bleed editorial bands rather than app containers. The hero can be split: huge serif headline on the left and a monochrome halftone plate on the right. Later sections alternate between centered serif letters, giant stamped headers, ticker bands, and small footer metadata. Avoid SaaS card grids, pricing tables, feature matrices, and dashboards.

## Do

- Use Louize Display at 77px or larger for section-defining headlines.
- Use Neue Montreal for UI/body at 12, 16, 20, 24, and 32px with tight tracking.
- Alternate Paper and Ink as full-bleed bands.
- Use 12px as the only radius for cards, buttons, and tags.
- Set display type in Ink on Paper or Paper on Ink.
- Use Manuka only at oversized masthead scale.
- Let most of the page remain empty Paper or Ink.

## Don't

- Do not introduce any chromatic accent color.
- Do not create filled colored CTAs.
- Do not use shadows, glow, gradients, blur, or elevated panels.
- Do not use body copy in oversized Louize Display sizes.
- Do not use any radius other than 12px.
- Do not break the Paper/Ink binary with gray panels or tinted sections.
- Do not center-align Neue Montreal body copy.

