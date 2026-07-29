# Flying Papers Style Reference

## Summary

Flying Papers is a loud, flat, riso-poster design system. The page is a full-bleed Dusk Violet stage with giant headline type, cartoon mascot illustration, and a handful of saturated accent colors. It should not feel like a polished SaaS page. It should feel printed, cheeky, and fearless.

Every screen should have one dominant idea. The usual composition is a huge headline, one mascot or character, one small action, and lots of violet space around it.

## Theme

Light.

## Personality

- Cartoon
- Poster-scale
- Cheeky
- Saturated
- Flat
- Riso-like
- Character-led
- Anti-corporate

## Color System

Dusk Violet is the stage. Hi-Vis Yellow is the loudest signal. Buttery Yellow softens display type. Lilac Shadow creates nested blocks. Accent colors behave like paint swatches, not semantic status colors.

| Name | Value | Token | Use |
| --- | --- | --- | --- |
| Dusk Violet | `#8584bd` | `--color-dusk-violet` | Full page canvas and hero stage |
| Hi-Vis Yellow | `#f4ed36` | `--color-hi-vis-yellow` | Outlined actions, linked labels, strongest accent |
| Buttery Yellow | `#f9cc73` | `--color-buttery-yellow` | Secondary display text and softer borders |
| Lilac Shadow | `#61609a` | `--color-lilac-shadow` | Nested blocks on violet stage |
| Bubblegum Pink | `#f8c1ba` | `--color-bubblegum-pink` | Decorative card and confetti accent |
| Matcha Cream | `#b5c995` | `--color-matcha-cream` | Dusty sage decorative card accent |
| Magenta Punch | `#ac4f98` | `--color-magenta-punch` | Standout accent card surface |
| Firecracker Red | `#c94245` | `--color-firecracker-red` | Red wash for highlight blocks |
| Bone White | `#f9f5f2` | `--color-bone-white` | Light cards, cream pill fill, reverse text |
| Ink Black | `#1a1a1a` | `--color-ink-black` | Body text, card borders, text on cream |
| Pure Black | `#000000` | `--color-pure-black` | Hard outlines, mascot strokes, text on yellow |

## Typography

The display type is the main event. Use ObviouslyVariable or a similarly wide condensed substitute. Keep leading tight so multi-line headlines become solid graphic blocks.

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| Display | 341px | 900 | 0.8 | 6.82px |
| Heading Large | 184px | 900 | 0.85 | 3.68px |
| Heading | 149px | 900 | 0.85 | 2.98px |
| Heading Small | 100px | 900 | 0.9 | 2px |
| Subheading | 30px | 800 | 0.9 | 0.6px |
| Body Large | 18px | 800 | 0.9 | 0.36px |
| Body | 16px | 700 | 1 | 0.8px |
| Caption | 10px | 400 | 1 | normal |

## Font Roles

- ObviouslyVariable: display and large headings, 800-900 weight, 18px to 341px.
- DegularVariable: tiny neutral UI copy around 10px.
- bergen_monoregular: mono micro-copy, tags, labels, and disclaimers at 12px or 14px.
- DegularDisplay-Bold: CTA labels and emphasized micro-copy at 16px with 0.05em tracking.

Disable contextual alternates on the display and mono fonts using `font-feature-settings: "calt" 0;`.

## Spacing And Shape

- Base unit: 4px
- Density: comfortable
- Section gap: 40px
- Card padding: 17px
- Element gap: 17px
- Cards: 6px radius
- Tags: 100px radius
- Buttons: 100px radius

The contrast between sharp printed blocks and soft pill actions is part of the identity.

## Surfaces

| Level | Surface | Value | Role |
| --- | --- | --- | --- |
| 0 | Dusk Violet Stage | `#8584bd` | Full-bleed page canvas |
| 1 | Bone White Card | `#f9f5f2` | Light cards and cream buttons |
| 2 | Lilac Shadow Block | `#61609a` | Nested violet blocks |
| 3 | Hi-Vis Yellow Surface | `#f4ed36` | Strongest accent surface |
| 4 | Accent Paint Card | `#f8c1ba` | Confetti card surface, with alternate accent fills |

## Elevation

Elevation is absent. Do not use shadows, glows, or inner shadows. Depth comes from color contrast, stacking, overlap, and hard outlines.

## Components

### Gate Pill Button

Cream fill, 100px radius, about 17px horizontal padding, DegularDisplay-Bold 16px with 0.05em tracking, Pure Black text. No shadow.

### Outlined Display Button

Transparent fill with a 2px to 3px Hi-Vis Yellow border. Use Hi-Vis Yellow text, 100px radius, DegularDisplay-Bold 16px, and about 17px horizontal padding. This is an outlined action, not a filled CTA.

### Underline Text Link

Bone White text on violet, no background, 1px underline. Use Bergen Mono at 12px with 0.80 leading. It should feel like a disclaimer.

### Hero Display Headline

ObviouslyVariable 800-900 at 184px to 341px, line-height 0.80 to 0.85, tracking 0.02em. Use Hi-Vis Yellow and Buttery Yellow. Let type fill most of the viewport.

### Brand Wordmark

Centered single-line wordmark in ObviouslyVariable 800, 30px, Hi-Vis Yellow. Do not add a separate icon mark.

### Mascot Illustration

Cartoon character with 2px to 3px Pure Black outline, cream fill, and flat accent colors. It can peek through, lean on, or overlap the headline. No shading.

### Confetti Card

Flat card in one accent color: Bubblegum Pink, Matcha Cream, Magenta Punch, or Firecracker Red. Use 6px radius, 17px padding, no shadow, no border. Do not line up every accent color in one row.

### Dark Text Card

Bone White fill, 6px radius, 17px padding, Ink Black text, optional 1px Ink Black border.

### Color Swatch Card

Solid color block with 6px radius and 17px padding. Label the color using DegularDisplay-Bold or Bergen Mono.

### Top Nav Bar

Transparent nav on the violet stage. Centered wordmark, minimal or no menu items, 17px vertical padding.

### Mono Label Tag

Bergen Mono 12px with 0.80 leading, optional 1px border, no fill unless needed. It should read like a stamped label.

### Footer Block

Solid block in a brand or accent color. Use Bergen Mono 12px, Bone White text, and compact 17px to 25px padding.

## Layout

Use full-bleed poster layouts with no traditional max-width constraint. The page stays on Dusk Violet, with flat color blocks placed on top. Each viewport is one composition:

- One enormous headline.
- One mascot or character.
- One inline action.
- Wide violet breathing room.

Loose 2-column or 3-column card grids can appear lower on the page, but cards should be content-sized and irregular rather than uniform dashboard tiles.

## Imagery

Use illustration only. Mascots should have thick black outlines, flat fills, and no shading. Icons are simple line drawings in Pure Black or Bone White. The image should carry mood while the typography carries the message.

Avoid photography, 3D renders, glassmorphism, gradients, and realistic depth.

## Do

- Set hero display type between 184px and 341px.
- Use ObviouslyVariable 800-900 with line-height around 0.80 to 0.85.
- Use Hi-Vis Yellow for outlined action borders.
- Stack one huge headline, one mascot, and one inline action per screen.
- Keep cards at 6px radius and buttons or tags at 100px radius.
- Use flat cards on the violet stage with 17px padding.
- Use one accent card color at a time.
- Set micro-copy in Bergen Mono at 12px with tight leading.

## Do Not

- Do not introduce filled yellow CTAs.
- Do not use display type below 18px or above 341px.
- Do not add shadows, glows, inner shadows, or glossy depth.
- Do not combine more than two accent colors in one composition.
- Do not change the page canvas to white or cream.
- Do not round cards beyond 6px.
- Do not enable contextual alternates for the display font.
