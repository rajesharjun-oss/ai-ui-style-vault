# Wiza - Style Reference

> Twilight prospecting observatory bathed in lavender mist: deep violet authority, compact contact-data UI, white floating cards, and a soft gradient atmosphere.

## Theme

Light. The foundation is white, paper-gray, and lavender wash. Deep violet supplies authority for headlines and filled actions, while neutral grays keep data tables readable.

## Design Story

Build the page as a polished SaaS dashboard preview, not an image-heavy marketing site. The hero should feel bright and atmospheric: white-to-lavender gradients, centered headline, dual CTA buttons, and a floating product screenshot. The product visuals are contact tables, prospect cards, profile previews, logo bars, and compact data rows.

Purple is hierarchical. Use Deep Iris for headlines and primary button fills. Use Royal Amethyst for links, focus, icons, and small accents. Use Mist Violet for tags and atmospheric sections. Do not turn all body copy purple.

## Tokens - Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Deep Iris | `#26114a` | `--color-deep-iris` | Headlines, filled button backgrounds, primary brand weight |
| Plum Velvet | `#312749` | `--color-plum-velvet` | Navigation text, card titles, footer copy |
| Royal Amethyst | `#3e0079` | `--color-royal-amethyst` | Links, input focus rings, accent strokes, icon highlights |
| Mist Violet | `#edecff` | `--color-mist-violet` | Soft highlight washes, tinted sections, pill tag backgrounds |
| Lavender Glow | `#b99aff` | `--color-lavender-glow` | Hero gradient stop and decorative glow |
| Canvas | `#ffffff` | `--color-canvas` | Page background, cards, inputs, button text on dark fills |
| Paper | `#f6f7fa` | `--color-paper` | Subtle surface lift, table row alternation, secondary cards |
| Mist | `#e6e2e3` | `--color-mist` | Hairline borders, dividers, separators |
| Smoke | `#c1c7cf` | `--color-smoke` | Disabled states, skeletons, muted blocks |
| Ash | `#9491a1` | `--color-ash` | Helper text, placeholders, secondary metadata |
| Slate | `#615e6e` | `--color-slate` | Secondary body text, descriptions, table metadata |
| Charcoal | `#333333` | `--color-charcoal` | Neutral logo bar, link text, icon strokes |
| Carbon | `#222222` | `--color-carbon` | Dark UI elements and near-black accents |
| Ink | `#000000` | `--color-ink` | Maximum contrast details |

## Gradients

| Name | Value | Role |
| --- | --- | --- |
| Lavender Wash | `linear-gradient(90deg, rgb(185, 154, 255), rgb(125, 67, 255) 10%, rgba(125, 67, 255, 0))` | Directional hero glow and feature atmosphere |
| Twilight Beam | `linear-gradient(to right, rgb(207, 138, 255), rgb(255, 102, 193), rgb(255, 173, 116), rgb(170, 129, 255))` | Special highlight beam used sparingly |

## Typography

Display font: Britti Sans.

- Use only for headings from 24px to 64px.
- Use weight 500.
- Use line-height exactly 1.
- Substitute with Plus Jakarta Sans 500 or General Sans 500.
- Do not use for body, nav, forms, or table rows.

UI font: Inter.

- Use for body, nav, buttons, inputs, table headers, table data, captions, badges, and cards.
- Use weights 400, 500, and 700.
- Keep the UI range compact from 12px to 16px.
- Use this compactness to signal a data-dense product.

## Type Scale

| Role | Size | Weight | Line height | Font |
| --- | --- | --- | --- | --- |
| Caption | 12px | 500 | 1.3 | Inter |
| Body Small | 14px | 400 or 500 | 1.4 | Inter |
| Body | 16px | 400 or 500 | 1.5 | Inter |
| Subheading | 24px | 500 | 1 | Britti Sans |
| Heading Small | 32px | 500 | 1 | Britti Sans |
| Heading | 40px | 500 | 1 | Britti Sans |
| Heading Large | 56px | 500 | 1 | Britti Sans |
| Display | 64px | 500 | 1 | Britti Sans |

## Spacing And Shape

- Base unit: 8px.
- Density: compact.
- Page max width: 1200px.
- Section gap: 64px to 80px.
- Card padding: 16px to 24px.
- Element gap: 8px.
- Cards: 8px radius.
- Icons: 8px radius.
- Inputs: 8px radius.
- Buttons: 8px radius.
- Large panels: 24px radius.
- Pills, tags, rating badges, and nav capsules: 1440px radius.

## Elevation

Use subtle blue or violet-tinted shadows:

- Small control shadow: `0 2px 4px rgba(18, 55, 105, 0.08), 0 1px 1px rgba(18, 55, 105, 0.04), 0 0 0 1px rgba(18, 55, 105, 0.08)`
- Large panel shadow: `0 32px 24px -12px rgba(14, 59, 101, 0.06), 0 11px 4px rgba(14, 59, 101, 0.01), 0 6px 4px rgba(14, 59, 101, 0.02), 0 3px 3px rgba(14, 59, 101, 0.03), 0 1px 1px rgba(14, 59, 101, 0.04)`
- Purple inset highlight: `inset 0 -6px 20px rgba(114, 49, 255, 0.32), 0 11px 12px rgba(47, 1, 151, 0.12), 0 3px 3px rgba(47, 1, 151, 0.12), 0 1px 1px rgba(47, 1, 151, 0.12), 0 0 0 1px rgba(47, 1, 151, 0.08)`

Keep shadows soft and low-contrast. Do not use heavy elevation.

## Components

### Filled Brand Button

Deep Iris fill, Canvas text, 8px radius, 16px vertical padding, 24px horizontal padding, Inter 500 at 16px. Use for the primary conversion only.

### Ghost Outlined Button

Transparent fill, 1px Deep Iris border, Deep Iris text, same 8px radius and 16px by 24px padding. Pair beside the filled button in hero CTA clusters.

### Pill Navigation Button

True capsule with 1440px radius, 8px vertical padding, 16px horizontal padding, Inter 500 at 14px, Plum Velvet text. Active state can use Mist Violet background.

### Logo Lockup

Purple triangular icon with a lavender-to-violet gradient, paired with a Wiza wordmark in Britti Sans 500 or Inter 700. Often sits in a white container with 8px radius and subtle shadow.

### Product Screenshot Frame

White card, 8px radius, large blue-tinted panel shadow, and no heavy border. Floats over lavender gradient background.

### Data Table Row

Alternate Canvas and Paper row backgrounds. Use 1px Mist bottom borders. Table cells use 12px to 16px padding. Data text is Inter 400 14px, headers are Inter 500 12px. Use colored status dots sparingly.

### Logo Cloud Bar

Centered row of monochrome Charcoal logos. Keep every logo visually calm and desaturated.

### Rating Badge Pair

White pill cards with 1440px radius, subtle border, Inter 500 14px scores, and Inter 400 12px platform labels. Star can use Royal Amethyst or a muted yellow.

### Section Heading Block

Optional pill tag above heading: Mist Violet background, Royal Amethyst text, 1440px radius, 4px by 12px padding, Inter 500 12px. Main heading uses Britti Sans 500 at 40px to 56px, Deep Iris. Subtext uses Inter 400 16px to 18px, Slate.

### Profile Card

White surface, 8px radius, subtle border, 12px by 16px padding. Include 32px circular avatar, Inter 500 14px name in Deep Iris, Inter 400 12px title in Slate, and Inter 400 12px company metadata in Ash.

### Floating Navigation Bar

White background, 8px radius, layered shadow, centered over the hero. Contains logo, pill nav links, and login or signup actions.

### Input Field

1px Mist border, 8px radius, 10px by 14px padding, Inter 400 14px, Ash placeholder. Focus state uses Royal Amethyst ring or border.

### Feature Icon Tile

16px or 24px tile with 8px radius, Mist Violet background, and a purple stroke icon inside. Use sparingly.

## Layout

Use a centered max-width 1200px container with 64px to 80px section gaps. The hero is a full-bleed white-to-lavender gradient with centered headline, subtext, dual CTA buttons, and a floating product screenshot below. Content alternates between white sections and light lavender sections. Use centered heading blocks followed by two-column and three-column grids. The floating nav sits above the hero.

## Imagery

Use product screenshots, data tables, contact cards, company logos, avatars, and simple icon tiles. Avoid lifestyle photography, stock imagery, rounded photos in feature illustrations, and people-in-office scenes. Trust logos should be monochrome.

## Rules

Do:

- Use 8px radius for rectangular UI surfaces.
- Use 1440px radius only for pills, tags, rating badges, and capsule nav.
- Keep Britti Sans headings at line-height 1.
- Use Deep Iris for headings and filled button backgrounds.
- Pair every filled hero CTA with a matching ghost CTA.
- Use pill tags above section headings.
- Use lavender gradients behind white content surfaces.
- Keep Inter at 12px to 16px for dense UI text.

Do not:

- Do not use Royal Amethyst for body text.
- Do not apply 4px or 12px radius to cards.
- Do not loosen Britti Sans heading line-height above 1.
- Do not introduce non-violet accent colors.
- Do not use heavy shadows.
- Do not center multi-line body paragraphs.
- Do not put dark text directly on lavender gradients without a white surface.
- Do not use photography as the primary illustration language.
