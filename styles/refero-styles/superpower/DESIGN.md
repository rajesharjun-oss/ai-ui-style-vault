# Superpower - Style Reference

## Positioning

Superpower turns clinical health into a cinematic command center. The page should feel serious and precise, but not cold. A dark atmospheric hero creates emotional weight, then the product moves into clean white surfaces, tight typography, pill actions, and clinical detail rows.

## Theme

- Theme: light
- Mood: bioluminescent health command center
- Best fit: diagnostics, health membership, longevity, lab testing, wellness platforms, clinical dashboards, personal health products

## Visual Principles

1. Open with dark, cinematic photography.
2. Float navigation as a dark contained pill over the hero.
3. Use crisp white sections for clinical clarity.
4. Keep color dichromatic: coral plus neutral grays.
5. Use coral sparingly for filled actions and brand moments.
6. Use tight geometric typography everywhere.
7. Avoid heavy elevation, glows, and extra chromatic colors.

## Color System

| Token | Value | Role |
| --- | --- | --- |
| Sunrise Coral | `#fc5f2b` | Filled primary action pills, brand mark, active thumbnail border |
| Coral Glow | `linear-gradient(88deg, #fc5f2b, #ff8b64 90%, #ffffff)` | One-off membership card wash |
| Pure Black | `#000000` | Logo wordmark and deepest contrast borders |
| Carbon Black | `#18181b` | Primary text, floating nav fill, headings, icon strokes |
| Zinc Gray | `#71717a` | Body copy, descriptions, helper text, metadata |
| Ash Gray | `#a1a1aa` | Tertiary text, inactive borders, disabled states |
| Mist Gray | `#e4e4e7` | Hairline borders, card outlines, dividers, button borders |
| Fog Gray | `#f4f4f5` | Muted background, subtle surface, image scrim base |
| Paper White | `#ffffff` | Page background, cards, text on dark imagery, button text |

## Typography

Use NB International Pro or a close geometric substitute for everything: display, headings, body, navigation, buttons, and UI labels. The signature is tight negative tracking that grows stronger as type gets larger.

Use NB International Mono Pro only for tabular metadata, clinical labels, micro-copy, and technical annotation moments.

Recommended fallbacks:

- Sans: `NB International Pro`, `Inter Tight`, `General Sans`, `Switzer`, `ui-sans-serif`, `system-ui`
- Mono: `NB International Mono Pro`, `JetBrains Mono`, `IBM Plex Mono`, `ui-monospace`, `monospace`

### Type Scale

| Role | Size | Line Height | Weight | Tracking |
| --- | ---: | ---: | ---: | ---: |
| Caption | 11px | 1.5 | 400 | -0.005em |
| Body | 15px | 1.5 | 400 | -0.005em |
| Body Large | 17px | 1.4 | 400 | -0.009em |
| Subheading | 19px | 1.4 | 400 | -0.009em |
| Heading Small | 22px | 1.25 | 400 | -0.012em |
| Heading | 30px | 1.2 | 400 | -0.013em |
| Heading Large | 45px | 1.13 | 400 | -0.015em |
| Display | 66px | 1 | 400 | -0.025em |

## Spacing And Shape

- Density: compact
- Base unit: 4px
- Page max width: 1200px
- Section gap: 75px
- Card padding: 19px
- Element gap: 11px
- Small cards: 5px radius
- Icon/squircle checks: 7.5px radius
- Cards: 15px radius
- Floating nav: 15px radius
- Buttons and CTA pills: 9999px radius
- Shadow: only a faint 2px hairline shadow when needed

## Layout

Use a dark hero with centered overlay copy and a floating pill nav. The main page content should transition into a Paper White background with controlled sections, 1200px max-width, crisp surface contrast, and restrained card grids. Pair every conversion block with a trust row directly underneath.

## Imagery

Hero imagery should be dark, atmospheric, and photographic: a silhouetted person or human figure against deep teal-blue darkness. Keep the photo legible for white headline text by using a dark scrim. Secondary imagery should be tight product crops, membership card artwork, dashboard screenshots, and thumbnail strips. Avoid illustrations, 3D renders, and generic wellness stock imagery.

## Components

### Floating Pill Navigation

Carbon Black pill bar floating over hero imagery. Logo on the left, muted white navigation links in the center, and a Sunrise Coral CTA pill on the right. It should sit as a contained capsule, not touch the viewport edges.

### Primary Pill CTA

Sunrise Coral fill, Paper White text, 9999px radius, 15px to 17px text, weight 700, tight tracking, and an optional right chevron. No heavy shadow.

### Ghost Text Link

No background and no border. Use white over the hero or Carbon Black on light sections. Add underline only on hover.

### Hero Overlay Headline

66px display, weight 400, line-height 1, -0.025em tracking, Paper White text, centered over dark photography. Do not bold display headings.

### Hero Subhead

17px body large, weight 400, max-width around 480px. Use white at reduced opacity on dark hero and Zinc Gray on light sections.

### Membership Visual Card

Organic marbled Coral Glow artwork with 15px radius, around 320px wide. It contains membership branding and price copy in white. Treat this as a unique asset, not a reusable page background.

### Membership Feature List

Vertical benefits with Coral filled checkmark squircles, 19px Carbon Black text, and 11px row gaps.

### Section Heading

45px to 56px, weight 400, tight negative tracking, Carbon Black, with generous bottom spacing.

### FAQ Item Or Read More Row

Large text row with a small right-aligned ghost text link. No box, no border, and no heavy container.

### Trust Badge Row

Small 11px to 13px labels and icons in Zinc Gray and Carbon Black, placed directly below the primary CTA.

### Photo Thumbnail Strip

Horizontal row of small thumbnails, 80px to 100px wide, 5px radius. Active item can use a Sunrise Coral border.

## Rules

- Use Sunrise Coral for filled primary action pills, brand marks, and active states only.
- Do not use coral for body text, icons, or broad decorative backgrounds.
- Set display headlines at weight 400, line-height 1, and -0.025em tracking.
- Float navigation as a dark pill capsule over imagery.
- Use 9999px radius for buttons and nav CTAs.
- Layer surfaces as Paper White, Fog or Mist Gray, and Carbon Black.
- Use the Coral Glow marbled pattern only on the membership card.
- Pair primary CTAs with a trust badge row.
- Avoid heavy shadows.
- Do not introduce additional accent colors.
