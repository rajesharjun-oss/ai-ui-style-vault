# Sequence Style Reference

> Blueprint paper with violet annotations: a near-white finance editorial interface where grayscale structure does the work and one violet pulse marks the important action.

## Theme

Light.

Sequence reads like a premium finance publication rendered as product UI. The page stays near-white and grayscale, with dense but calm product chrome. TWK Lausanne carries almost all interface text. A light Moderat Serif headline appears only at the largest marketing display size, adding editorial gravity without taking over the product language. Violet Pulse is the single chromatic action color.

## Core Principles

1. Keep the page anchored to white and near-white surfaces.
2. Use Violet Pulse for exactly one filled primary CTA per screen.
3. Use TWK Lausanne for almost all UI and text.
4. Reserve Moderat Serif for the largest 40px to 46px display headline only.
5. Use Ash hairline borders as the structural backbone.
6. Use compact spacing, 8px cards, 4px inputs, and pill controls.
7. Let product UI mockups, tables, forms, and contract cards replace photography.
8. Build depth with rings and tight shadow stacks, not heavy blur.

## Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Violet Pulse | `#a565ff` | `--color-violet-pulse` | Primary CTA, active icon, brand glow |
| Indigo Ink | `#5e5cff` | `--color-indigo-ink` | Links, secondary emphasis, accent strokes |
| Lavender Wash | `#ebebff` | `--color-lavender-wash` | Tinted callouts, focus rings, active fields |
| Iris Glow | `#e0c9ff` | `--color-iris-glow` | Violet halo and low-frequency supporting accent |
| Ledger Green | `#2e7317` | `--color-ledger-green` | Green text accent for links, tags, and success badges |
| Paper White | `#ffffff` | `--color-paper-white` | Canvas, cards, elevated surfaces, button fills |
| Bone | `#f7f7f7` | `--color-bone` | Recessed surfaces and subtle panels |
| Fog | `#f1f1f1` | `--color-fog` | Disabled fills, row alternates, recessed UI |
| Silver | `#efefef` | `--color-silver` | Inset borders, outlines, shadow ring fills |
| Marble | `#fff6df` | `--color-marble` | Announcement bars and warm highlight bands |
| Graphite | `#1d1d20` | `--color-graphite` | Primary headings and body text |
| Slate | `#42424a` | `--color-slate` | Secondary headings and emphasized text |
| Iron | `#505050` | `--color-iron` | Default body text and navigation text |
| Steel | `#757575` | `--color-steel` | Muted helper text and secondary table text |
| Smoke | `#92939e` | `--color-smoke` | Placeholder text, disabled labels, tertiary cells |
| Ash | `#e5e7eb` | `--color-ash` | Default hairline border |
| Mist | `#d1d9e4` | `--color-mist` | Input borders and stronger section dividers |
| Olive Gray | `#808076` | `--color-olive-gray` | SVG illustration strokes and fills |
| Noir | `#000000` | `--color-noir` | Icon fills and hard contrast anchors |

## Typography

Use three roles:

| Role | Family | Fallback | Use |
| --- | --- | --- | --- |
| Primary UI | TWK Lausanne | Inter, IBM Plex Sans, Sohne | Body, nav, buttons, labels, cards, most headings |
| Editorial Display | Moderat Serif | GT Sectra, Tiempos Headline, Canela | Single largest h1 display headline |
| Mono Microtext | SF Mono | JetBrains Mono, IBM Plex Mono | API references, code snippets, technical labels |

## Type Scale

| Role | Size | Weight | Line Height | Letter Spacing |
| --- | --- | --- | --- | --- |
| Caption | 11px | 400 or 500 | 1.45 | -0.022px |
| Body | 14px | 400 | 1.57 | normal |
| Body large | 16px | 400 | 1.63 | normal |
| Subheading | 18px | 400 or 500 | 1.56 | normal |
| Heading small | 24px | 300 to 500 | 1.33 | -0.048px |
| Heading | 40px | 300 | 1 | -1px |
| Display | 46px | 300 | 1 | -1.15px |

Set headings 24px and above with lighter weights. Use Moderat Serif only for the largest display h1, never for product UI or subheadings.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | compact |
| Base unit | 4px |
| Max width | 1200px |
| Section gap | 80px |
| Card padding | 24px |
| Element gap | 8px |
| Card radius | 8px |
| Badge radius | 9999px |
| Input radius | 4px |
| Button radius | 9999px |
| Large panel radius | 16px |

Use pill radius for all buttons, badges, tags, and nav pill controls. Cards remain compact at 8px.

## Layout

Use a 1200px centered container with 24px gutters. The page stacks sections vertically with 80px gaps. Navigation is a fixed top bar with logo left, nav links in the middle, and sign-in plus a violet demo CTA on the right.

Recommended flow:

1. Fixed top navigation.
2. Full-bleed white hero with centered eyebrow, serif display h1, paragraph, and CTA pair.
3. Floating product screenshot grid below the hero.
4. Customer logo strip with rating.
5. Alternating product suite sections with text and UI mockups.
6. Two-column feature section with diagram and icon-text grid.
7. Announcement or warm highlight band.
8. Footer with grayscale links and brand lockup.

## Components

### Primary Action Button

Filled Violet Pulse background, Paper White text, 9999px radius, 10px by 20px padding, TWK Lausanne 14px weight 500. Add a low-opacity Iris Glow halo. This is the only filled chromatic button.

### Secondary Action Button

Transparent or Paper White background, 1px Silver border, Graphite text, 9999px radius, 10px by 20px padding. Hover can shift to Bone. Use a thin layered ring shadow, not a colored glow.

### Navigation Link

Iron text, TWK Lausanne 14px weight 500, no underline by default. Active state shifts to Graphite and may add a 1px Graphite underline.

### Display Headline Block

Moderat Serif, weight 300, 46px, line-height 1, -0.025em tracking, Graphite color. Pair with TWK Lausanne 16px body copy in Iron. Use once per page or major marketing surface.

### Product Feature Card

Paper White background, 1px Ash border, 8px radius, 24px padding. Icon top-left in Graphite. Title uses TWK Lausanne 18px weight 500. Description uses 14px Steel text. No resting shadow.

### Product Screenshot Card

Paper White background, 1px Ash border, 8px radius, 16px padding. Use layered thin-ring shadow. Internal UI uses Bone fills and Lavender Wash highlights.

### Input Field

Paper White background, 1px Mist border, 4px radius, 8px by 12px padding. Placeholder Smoke. Focus state uses Violet Pulse border and a Lavender Wash outer ring.

### Integration Logo Tile

Paper White background, 1px Ash border, 8px radius, 16px padding. Center the logo mark without text. Keep logos monochrome or low-chroma.

### Status Badge

Lavender Wash or Bone background, Indigo Ink or Ledger Green text, 11px weight 500, 9999px radius, 2px by 10px padding.

### Announcement Bar

Full-bleed Marble background, Graphite text at 13px, centered, 8px vertical padding. Inline arrow link can use Indigo Ink.

### Logo Lockup

Graphite hex-cluster glyph plus Sequence wordmark in TWK Lausanne 18px weight 500. No tagline.

### Section Header

TWK Lausanne eyebrow at 12px weight 500 in Steel, then 40px light heading in Graphite. Centered for hero sections, left-aligned in product sections.

### Customer Logo Strip

No background or border. Center monochrome customer wordmarks with a star rating above. Use 48px to 80px column gaps.

## Surfaces

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 0 | Page Canvas | `#ffffff` | Base page and hero background |
| 1 | Recessed Surface | `#f7f7f7` | Subtle panels and cards |
| 2 | Tinted Surface | `#ebebff` | Highlighted fields and callouts |
| 3 | Warm Accent | `#fff6df` | Announcement bars and warm highlight bands |

## Elevation

Use thin rings and short, tight offset shadows. Avoid heavy drop shadows. The primary CTA gets the brand-specific Iris Glow halo. Screenshot cards get a layered ring plus subtle vertical depth. Secondary controls get a simple 1px ring.

## Imagery

Use product UI mockups only: contract interfaces, billing forms, invoice tables, product cards, logo tiles, diagrams, and line icons. Avoid lifestyle photography, stock imagery, and decorative illustrations. Use soft blue-violet radial washes behind product UI for atmosphere.

## Do

- Use Violet Pulse only for the single primary CTA per screen.
- Use Ash 1px borders across cards, inputs, dividers, and tiles.
- Use TWK Lausanne for all UI and most headings.
- Use Moderat Serif only for the largest h1.
- Use 9999px pill radius for buttons, badges, tags, and nav pills.
- Keep card padding at 24px and section gaps at 80px.
- Use Lavender Wash with Iris Glow for focus and highlight states.

## Don't

- Do not add new chromatic colors.
- Do not use Indigo Ink as a button background.
- Do not use Moderat Serif below 40px or for product UI.
- Do not use large colored blocks for content sections.
- Do not use heavy shadows or blurry elevation.
- Do not set body text below 12px.
- Do not use 8px radius for buttons or tags.

## AI Builder Notes

If the page starts to feel generic, sharpen the grayscale structure and make the violet action more intentional. The premium signal is not more color; it is compact product detail, clean borders, disciplined typography, and one unmistakable action pulse.
