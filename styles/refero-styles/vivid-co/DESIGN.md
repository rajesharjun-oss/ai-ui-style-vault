# Vivid+Co Style Reference

Vivid+Co is a cinematic dark creative-agency system. It pairs an obsidian void with sculptural Neue Montreal type, restrained navigation, sparse borders, and a single RGB-split prism artwork. The effect is not colorful UI; it is monochrome typography interrupted by one optical artifact.

## Theme

Dark, creative agency, cinematic, monochrome, prism artifact, oversized type, restrained navigation, portfolio index.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Bone White | `#fffdf9` | `--color-bone-white` | Primary text, nav labels, link color, heading fill, and almost every interactive element. |
| Obsidian | `#101010` | `--color-obsidian` | Page canvas, hero void, and full-bleed dark sections. |
| Graphite Veil | `#495764` | `--color-graphite-veil` | Cool dark slate surface behind headings and content blocks. |
| Ash Border | `#403f3f` | `--color-ash-border` | Hairline divider and rare card outline. |
| Fog Blue | `#6f879c` | `--color-fog-blue` | Muted secondary text, ghost labels, and de-emphasized metadata. |
| Pure Black | `#000000` | `--color-pure-black` | Decorative SVG icon and illustration fill; not a page background. |
| Prism Red | `#ff2a2a` | `--color-prism-red` | RGB prism artifact channel only; not a UI token. |
| Prism Cyan | `#2a7fff` | `--color-prism-cyan` | RGB prism artifact channel only; not a UI token. |
| Prism Lime | `#2aff2a` | `--color-prism-lime` | RGB prism artifact channel only; not a UI token. |

## Typography

### Neue Montreal

Use as the only typeface.

- Token: `--font-neue-montreal`
- Fallback: Sohne, Inter, General Sans, system-ui
- Weights: 400, 700
- Sizes: 14px, 15px, 17px, 18px, 20px, 21px, 22px, 32px, 33px, 36px, 56px, 105px, 136px
- Line height: 1.00 to 1.50
- Letter spacing: -0.02em at 136px display, -0.01em at 33px to 56px headings, +0.01em at 15px to 21px body, +0.02em at 17px uppercase labels
- OpenType: enable stylistic set 1 when available
- Role: everything: headings, nav, links, body, labels, footer, and buttons.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | 15px | 1.20 | 0.15px | `--text-caption` |
| Body SM | 18px | 1.50 | 0 | `--text-body-sm` |
| Body | 20px | 1.20 | -0.2px | `--text-body` |
| Body LG | 22px | 1.20 | -0.22px | `--text-body-lg` |
| Heading SM | 33px | 1.20 | -0.33px | `--text-heading-sm` |
| Heading | 36px | 1.50 | 0 | `--text-heading` |
| Heading LG | 56px | 1.13 | -0.56px | `--text-heading-lg` |
| Display SM | 105px | 1.01 | -2.1px | `--text-display-sm` |
| Display | 136px | 1.00 | -2.72px | `--text-display` |

## Spacing And Shape

- Density: comfortable.
- Base unit: 4px.
- Max width: 1440px.
- Section gap: 108px.
- Card padding: 20px.
- Element gap: 7px.

### Spacing Scale

`16, 20, 40, 56, 60, 64, 72, 108`

### Radius Scale

| Element | Radius |
|---|---:|
| Navigation outline | 5px |
| Cards | 15px |
| Tags | 9999px |
| Buttons | 0px |

## Components

### Ghost Nav Button

Transparent fill, Bone White text, uppercase Neue Montreal 14px to 15px, 0px radius, no padding, no underline, no border. Use for links such as expertise, work, team, and careers.

### Outlined Contact Button

Transparent fill, 1px Bone White border, 5px radius, 9px by 15px padding, uppercase 14px Bone White text. This is the only explicit bordered header action.

### Ghost Service Label

Transparent fill, Fog Blue text, 0px radius, 20px top padding, 30px bottom padding, Neue Montreal 20px. Use below case-study titles as service taxonomy.

### Display Headline Block

Neue Montreal 400 at 105px to 136px, line-height 1.00 to 1.01, -0.02em tracking, Bone White. Stack across multiple lines and let the headline occupy half the viewport.

### Hero Lead Paragraph

Neue Montreal 400 at 18px to 22px, line-height 1.5, Bone White, max-width around 440px. Place it below or beside the prism artifact, not full-width.

### Prism Artifact

Four to six glass cubes arranged as a staggered cluster, with Pure Black cores, Bone White highlights, and RGB channel-offset red/cyan/lime edges. This is the only full-color object.

### Section Heading

Small section statement at 18px to 22px, Bone White, max-width around 440px, above a larger display headline. Keep it left-aligned and quiet.

### Footer Hairline Divider

1px Ash Border rule, full width, with compact top spacing. Use as the primary footer separator.

### Case Study Title Link

Neue Montreal 400 at 33px, Bone White, line-height 1.2, -0.01em tracking, no underline. Hover can shift to Fog Blue only.

### Eyebrow Label

Uppercase Neue Montreal 17px or 32px, weight 400, letter-spacing +0.02em at small size. Use restraint instead of boldness.

### Rounded Pill Tag

9999px radius, rare metadata chip. Use sparingly; most UI stays square-edged.

## Layout

Use a full-bleed Obsidian canvas and a 1440px content rail. The hero centers the prism artifact and lets oversized display text wrap around or overlap it. Navigation is a thin top row with wordmark left, ghost links right, and one outlined contact button. Sections are mostly single-column statements and case-study links, not card grids. Footer is a quiet metadata band separated by one hairline.

## Imagery

The prism artifact is the brand image. Use a 3D glass-cube cluster with chromatic aberration and RGB split edges. Avoid photography, people, product screenshots, generic illustrations, textures, decorative gradients, and multicolor icon sets. If icons are needed, make them monoline and near-white.

## Motion

Motion should be expressive but restrained. Use slow opacity and transform transitions, around 0.5s, with a precise cubic-bezier curve such as `cubic-bezier(0.52, 0.01, 0, 1)`. The prism can shimmer slowly. Avoid bounce, spring, scale-pop, and busy cursor effects.

## Do

- Use Bone White for nearly all text and interactive elements.
- Use Fog Blue only for de-emphasized metadata.
- Let scale create hierarchy instead of heavier weights.
- Keep Neue Montreal weight 400 as the default.
- Reserve weight 700 for rare 36px subheadings.
- Set display type at 105px to 136px with line-height near 1.00.
- Use 0px radius for buttons and most UI.
- Make the prism artifact the only chromatic element.

## Don't

- Do not introduce filled buttons, CTA colors, badges, or broad gradients.
- Do not use Prism Red, Cyan, or Lime anywhere outside the prism artwork.
- Do not use weight 600 to 800 for display headings.
- Do not add box shadows to cards, nav, or artwork.
- Do not loosen tracking above 22px.
- Do not lighten the canvas beyond Graphite Veil.
- Do not build multi-column SaaS grids or pricing-card layouts.
