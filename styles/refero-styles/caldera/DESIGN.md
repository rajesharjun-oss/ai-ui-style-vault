# Caldera Style Reference

Caldera feels like blockchain infrastructure forged inside a volcanic brand world: warm stone paper, lava-black typography, molten orange controls, violet halftone diagrams, sulfur tags, and inflated rounded containers. It should feel technical and energetic without becoming neon, glassy, or cyberpunk.

## Theme

Light, warm, volcanic, technical, infrastructure, web3, playful but serious.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Lava Black | `#000000` | `--color-lava-black` | Primary text, logos, nav labels, icon strokes, and high-contrast borders. |
| Obsidian | `#111111` | `--color-obsidian` | Dark footer panels, modal backdrops, and inverted cards. |
| Basalt | `#212121` | `--color-basalt` | Secondary dark text and deep UI surfaces. |
| Charcoal | `#343434` | `--color-charcoal` | Muted text, dark border states, and disabled controls. |
| Ash | `#6c6c6c` | `--color-ash` | Secondary body copy, captions, helper labels, and muted metadata. |
| Stone | `#b6b0aa` | `--color-stone` | Hairline dividers, disabled borders, and quiet graphic strokes. |
| Pumice | `#e3ded8` | `--color-pumice` | Main page background and warm neutral section surfaces. |
| Chalk | `#f2ede7` | `--color-chalk` | Cards, inputs, light chips, and slightly raised surfaces. |
| Steam | `#ffffff` | `--color-steam` | Rare white highlights and contrast text on saturated surfaces. |
| Ember Orange | `#ff6828` | `--color-ember-orange` | Primary CTA, active tags, key borders, illustration heat, and focus states. |
| Molten Coral | `#ff7b54` | `--color-molten-coral` | Hover accents and softer orange fills. |
| Violet Rift | `#6c35ff` | `--color-violet-rift` | Halftone hero graphics, developer nodes, and secondary action highlights. |
| Deep Violet | `#2d165f` | `--color-deep-violet` | Dark purple shadow field and contrast for violet graphics. |
| Sulfur | `#e8ff50` | `--color-sulfur` | Small tags, network badges, and notification sparks. |
| Signal Blue | `#1c69ff` | `--color-signal-blue` | Rare link or network state highlight. |

## Typography

### Display

Use PP Neue Montreal-style type for all major statements. Headlines should be huge, dense, and tightly tracked.

- Token: `--font-pp-neue`
- Fallback: Arial Narrow, Helvetica Neue Condensed, Inter Tight, sans-serif
- Weight: 530
- Sizes: 48px, 64px, 128px
- Letter spacing: about `-3px` to `-5.76px` at display sizes

### UI And Body

Use DM Sans for body copy, nav, labels, cards, buttons, and forms.

- Token: `--font-dm-sans`
- Fallback: Inter, system-ui, sans-serif
- Weight: mostly 500, with 600 for emphasis
- Body sizes: 16px and 24px

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Micro | 14px | 1.1 | 0 | `--text-micro` |
| Body | 16px | 1.25 | 0 | `--text-body` |
| Body LG | 24px | 1.15 | 0 | `--text-body-lg` |
| Heading | 48px | 1.05 | -1.44px | `--text-heading` |
| Display | 128px | 0.95 | -5.76px | `--text-display` |

## Spacing And Shape

- Density: spacious.
- Base unit: 4px.
- Page max width: 1280px.
- Section gap: 160px.
- Card padding: 40px.
- Element gap: 16px.

### Spacing Scale

`4, 8, 12, 16, 20, 24, 32, 40, 48, 56, 64, 80, 96, 120, 160, 200`

### Radius Scale

| Element | Radius |
|---|---:|
| Buttons | 40px |
| Inputs | 32px |
| Cards | 40px |
| Chips and tags | 800px |
| Modals | 48px |
| Hero visual | 56px |

## Components

### Primary Pill Button

Use Ember Orange fill, Lava Black or Steam text depending contrast, 40px radius, DM Sans 16px/600, and generous horizontal padding. The button should feel like a molten capsule rather than a standard SaaS button.

### Secondary Outline Button

Use transparent or Chalk fill, 1px Lava Black border, 40px radius, Lava Black text. Use it for lower-priority navigation and paired CTA actions.

### Rounded Card

Use Chalk or Pumice fill, 1px Lava Black or Stone border, 40px radius, 40px padding. Avoid nested cards. Use these as major content modules, not tiny widgets.

### Hero Halftone Panel

Use Violet Rift and Deep Violet halftone geometry over Pumice or Chalk. Pair with a large PP Neue headline and one Ember Orange CTA.

### Network Badge

Use Sulfur fill, Lava Black text, 800px radius, small DM Sans label. Use only for tiny status tags or network markers.

### Input

Use Chalk fill, 1px Stone or Lava Black border, 32px radius, 16px DM Sans text, 16px by 24px padding. Focus border should use Ember Orange.

### Process Diagram

Use thin Lava Black strokes, circular nodes, occasional Violet or Ember fill, and short DM Sans labels. Keep the diagram clean and flat.

## Layout

Use a wide 1280px center container with very large section gaps. Hero layout should feel poster-like: huge headline, compact copy, one or two large pill actions, and a bold halftone/developer visual. Sections should breathe heavily and use large rounded panels rather than dense tables.

## Imagery

Use custom abstract halftone graphics, node diagrams, network maps, protocol illustrations, and thin line art. Avoid generic crypto coin imagery, lifestyle photos, glossy 3D cubes, and blue-purple cyberpunk gradients.

## Do

- Use Pumice as the full-page canvas.
- Make headlines large and tightly tracked.
- Use Ember Orange as the single dominant action color.
- Keep Violet Rift in graphic and developer-diagram moments.
- Use Sulfur only for small tags and signal sparks.
- Use 40px radii for cards and buttons.
- Use chunky but flat shapes.

## Don't

- Do not use pure white as the broad page background.
- Do not add new saturated accent colors.
- Do not use small 8px SaaS cards.
- Do not use glassmorphism or glowing gradients.
- Do not use generic blockchain coin imagery.
- Do not make every accent violet.
- Do not use serif type.
