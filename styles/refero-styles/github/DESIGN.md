# GitHub Style Reference

> A cosmic developer command deck: deep dark surfaces, violet atmosphere, translucent glass panels, and one warm green action beacon.

## Theme

Dark.

GitHub operates like a developer observatory in deep space. The page uses near-black surfaces, cool gray copy, translucent glass cards, violet radial glows, and a single Terminal Green CTA. Mona Sans is the main voice, with a distinctive 64px display setting at weight 425 and tight tracking. Mona Sans Mono handles tags, nav micro-labels, and code-adjacent metadata.

## Core Principles

1. Use Deep Void as the default canvas.
2. Use Terminal Green for one primary CTA per screen.
3. Keep secondary actions transparent or dark, never green.
4. Build major cards as translucent glass panels, not opaque boxes.
5. Use violet and purple as atmosphere or rare card border accents.
6. Use Sky for low-frequency text, links, and icon accents.
7. Preserve the shape vocabulary: 6px buttons, 24px cards, 60px pills.
8. Show product value with IDE frames, browser chrome, code, and synthetic illustrations.

## Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Deep Void | `#0d1117` | `--color-deep-void` | Page canvas, sections, footer |
| Abyss | `#000000` | `--color-abyss` | Hero canvas and terminal/code surfaces |
| Carbon | `#090d0a` | `--color-carbon` | Near-black button surface and accent fill |
| Obsidian | `#151a22` | `--color-obsidian` | Elevated dark controls and inputs |
| Slate Edge | `#21262d` | `--color-slate-edge` | Hairline borders, card outlines, dividers |
| Iron | `#3d4145` | `--color-iron` | Subtle elevated card surface |
| Fog | `#484f58` | `--color-fog` | Stronger dividers and secondary borders |
| Moss | `#7c8980` | `--color-moss` | Tertiary headings and low-emphasis text |
| Mercury | `#818b98` | `--color-mercury` | Muted borders and inactive outlines |
| Ash | `#9ea0a2` | `--color-ash` | Reduced-contrast strokes and borders |
| Pearl | `#a4aea6` | `--color-pearl` | Body copy and muted navigation labels |
| Snow | `#ffffff` | `--color-snow` | Primary text, headings, button text |
| Terminal Green | `#08872b` | `--color-terminal-green` | Single primary CTA fill |
| Phosphor | `#5fed83` | `--color-phosphor` | Green wash and soft emphasis |
| Canopy | `#0d3024` | `--color-canopy` | Green-gray supporting accent surface |
| Ultraviolet | `#8c93fb` | `--color-ultraviolet` | Featured card border and rare selected state |
| Sky | `#8dd6ff` | `--color-sky` | Link text, body accent, icon fill |
| Cobalt | `#1f6feb` | `--color-cobalt` | Low-frequency marketing accent |

## Typography

Use Mona Sans where available. Inter is the closest practical fallback. Use Mona Sans Mono for code-related labels and technical tags.

| Role | Family | Fallback | Use |
| --- | --- | --- | --- |
| Primary | Mona Sans | Inter | Display, body, nav, buttons, headings |
| Code | Mona Sans Mono | JetBrains Mono | Code labels, tags, micro-copy, terminal metadata |

## Type Scale

| Role | Size | Weight | Line Height | Letter Spacing |
| --- | --- | --- | --- | --- |
| Caption | 12px | 500 | 1.5 | 0.18px |
| Body small | 14px | 400 | 1.5 | normal |
| Body | 16px | 400 | 1.5 | normal |
| Body large | 18px | 400 | 1.5 | 0.01em |
| Subheading | 22px | 480 | 1.4 | normal |
| Heading small | 24px | 600 | 1.5 | normal |
| Heading | 40px | 460 | 1.2 | normal |
| Heading large | 48px | 800 | 1.0 | normal |
| Display | 64px | 425 | 1.08 | -0.035em |

The display weight 425 is the signature. Do not replace it with ordinary 700 bold. Body text should stay at 16px/400/1.5 for the main reading rhythm.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | comfortable |
| Base unit | 4px |
| Max width | 1200px |
| Section gap | 64px to 96px |
| Card padding | 24px |
| Element gap | 16px to 24px |
| Input radius | 6px |
| Button radius | 6px |
| Image radius | 16px |
| Card radius | 24px |
| Pill button radius | 60px |
| Tag radius | 9999px |

Keep component types consistent. Filled and outlined actions use 6px. Glass cards use 24px. Nav pills and tag controls use 60px or fully rounded.

## Layout

Use a full-bleed dark page with centered content blocks around 1200px. The hero is centered over a violet radial glow, with a headline, readable body copy, an email/action row, and product evidence below. Later sections alternate centered section headers, translucent card grids, tabbed product panels, customer logos, and a footer link grid.

Recommended flow:

1. Slim transparent top navigation.
2. Centered hero with violet halo.
3. Email capture or CTA cluster with Terminal Green primary action.
4. IDE or browser frame screenshot.
5. Section header with optional 3D icon.
6. Tab navigation row using 60px pill buttons.
7. Glass card grid or featured card.
8. Customer logos or proof section.
9. Multi-column dark footer.

## Components

### Primary CTA Button

Terminal Green fill, Snow text, no border, 6px radius, 6px by 20px padding, Mona Sans 16px/400. Use for sign-up or a similarly high-intent action. This is the only filled chromatic button.

### Ghost Button

Transparent fill, Snow text and/or border, either 0px for compact icon buttons or 60px for text pills. Used for secondary actions and nav-adjacent controls.

### Pill Button

Transparent fill, Snow text, 1px Snow or low-opacity Snow border, 60px radius, 8px by 16px padding. Use for topic tags, tab navigation, filters, and category selectors.

### Outlined Action Button

Dark translucent fill, Sky text, Snow border, 6px radius, 6px by 20px padding. Use for a cooler secondary action beside the green CTA.

### Email Input Field

Transparent or dark fill, Slate Edge border, 6px to 8px radius, Pearl placeholder at 16px. Can be paired inline with the green CTA.

### Glass Surface Card

rgba white fill from 0.06 to 0.2, 1px low-opacity white or Slate Edge border, 24px radius, backdrop blur around 20px, no shadow. This is the signature surface.

### Featured Card

Same as Glass Surface Card, but use an Ultraviolet border. Reserve for a highlighted feature, selected state, or premium card.

### Top Navigation Bar

About 64px high, transparent over the dark page. White logo on the left, Mona Sans nav items, dropdown chevrons, a dark search field, and sign-in/up actions on the right.

### Section Header Block

Centered stack with optional 3D icon, 40px Mona Sans headline at weight 460, and 18px Pearl body text with max-width around 640px.

### Tab Navigation Row

Horizontal pill buttons at 60px radius. Active state can use Snow fill or stronger border. Inactive state is transparent with faint border. Use around 32px gap below before content.

### Hero Gradient Banner

Radial violet gradient behind hero content, blurred about 60px and fully diffused. It should make the black canvas feel inhabited, not create a visible blob edge.

### IDE Or Device Frame

Browser or IDE frame with traffic-light dots, tab names, and code editor content. Use 8px outer radius and 6px internal panels. It can sit inside a glass card or over a gradient halo.

### Footer Link Grid

Deep Void background. Four columns of links. Column headings use Snow at 16px/600. Links use Pearl at 14px/400 with 12px vertical spacing. Use whitespace rather than vertical borders.

## Surfaces

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 0 | Void | `#0d1117` | Base page canvas |
| 1 | Abyss | `#000000` | Hero and terminal contexts |
| 2 | Carbon | `#151a22` | Elevated buttons and input fields |
| 3 | Iron | `#3d4145` | Subtle card surface |
| 4 | Glass | `rgba(255, 255, 255, 0.06)` | Translucent panels |
| 5 | Frost | `rgba(255, 255, 255, 0.2)` | Highest translucency for overlays |

## Elevation

Elevation comes from translucency, backdrop blur, and borders. Do not use drop shadows for cards or buttons. Cards float because they are translucent panels over the dark atmospheric canvas.

## Imagery

Use synthetic and product-native imagery: 3D rounded characters, code editor frames, IDE screenshots, browser chrome, line icons, gradient halos, and constellation-like layouts. Avoid real photography of people or offices.

## Do

- Use Terminal Green only for the single primary CTA.
- Use Mona Sans 16px/400/1.5 for body copy.
- Use 64px display at Mona Sans weight 425 with -0.035em tracking.
- Use glass cards with rgba white fills and 1px borders.
- Use violet radial halos behind hero or illustration content.
- Use Mona Sans Mono 12px uppercase with 0.015em tracking for technical micro-labels.
- Keep 24px radius for major cards.

## Don't

- Do not use blue as the primary action color.
- Do not apply green to tags, secondary actions, or decorations.
- Do not use 4px or 8px radius for major feature cards.
- Do not use drop shadows for cards or buttons.
- Do not use solid purple/violet fills for buttons or broad surfaces.
- Do not use Cobalt as the general link color; prefer Sky.
- Do not replace the display weight 425 with ordinary bold.

## AI Builder Notes

If the page feels too flat, add a blurred violet radial halo or increase glass translucency contrast before adding shadows. If it feels too colorful, remove chromatic accents until Terminal Green is clearly the main action beacon.
