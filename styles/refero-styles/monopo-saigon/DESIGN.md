# monopo saigon Style Reference

monopo saigon is a black-and-white editorial gallery wrapped around one liquid iridescent hero moment. The interface is restrained to the point of austerity: sharp text links, sharp images, no shadows, no card chrome, and monumental Roobert typography. The only softness is reserved for 75px pill controls and the full-viewport hero media.

## Theme

Light, monochrome, editorial, immersive, gallery-like, restrained, fluid media.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Obsidian | `#000000` | `--color-obsidian` | Primary text, SVG strokes, overlay fills, borders, and dark inverse bands. |
| Paper | `#ffffff` | `--color-paper` | Main canvas, inverse labels, and high-contrast text on dark surfaces. |
| Inkstone | `#181818` | `--color-inkstone` | Footer body copy and softened black reading blocks. |
| Slate Pill | `#636363` | `--color-slate-pill` | Filled neutral button background for consent and utilitarian confirmations. |
| Felt Gray | `#6d6d6d` | `--color-felt-gray` | Muted helper text, addresses, legal copy, and receding annotations. |
| Pewter | `#808080` | `--color-pewter` | Secondary mid-tone neutral for hover or muted state layers. |
| Ash Mist | `#9a9a9a` | `--color-ash-mist` | Disabled states, low-contrast surfaces, and quiet grayscale layers. |
| Iridescent Fade | `linear-gradient(90deg, rgb(160, 224, 171), rgb(255, 172, 46) 50%, rgb(165, 45, 37))` | `--gradient-iridescent-fade` | Hero media atmosphere only. Never use this as a UI fill. |

## Typography

### Roobert

Roobert is the primary typeface across navigation, hero headlines, body copy, lists, project titles, and footer text.

- Token: `--font-roobert`
- Fallback: Inter or Sohne
- Weights: 300, 400, 600
- Sizes: 11px through 225px
- Line height: 0.70 to 2.34
- Role: geometric-humanist editorial sans, scaling from tiny labels to full-viewport headlines.

### Raleway

Raleway is a rare heading accent. Use it sparingly, usually around 54px.

- Token: `--font-raleway`
- Fallback: Montserrat or Jost
- Weight: 400
- Role: occasional narrower, elegant heading contrast.

### system-ui

Use system-ui for micro labels, cookie copy, and fine print only.

- Token: `--font-system-ui`
- Weights: 400
- Sizes: 9px and 16px

### Type Scale

| Role | Size | Line Height | Token |
|---|---:|---:|---|
| Caption | 12px | 1.19 | `--text-caption` |
| Body SM | 16px | 1.15 | `--text-body-sm` |
| Body | 18px | 1.21 | `--text-body` |
| Subheading | 39px | 1.19 | `--text-subheading` |
| Subheading LG | 45px | 1.15 | `--text-subheading-lg` |
| Heading SM | 54px | 1.39 | `--text-heading-sm` |
| Heading | 78px | 1.10 | `--text-heading` |
| Heading LG | 94px | 0.76 | `--text-heading-lg` |
| Display | 225px | 1.25 | `--text-display` |

## Spacing And Shape

- Density: spacious.
- Base unit: 4px.
- Page max width: 1078px.
- Section gap: 46px.
- Card padding: 34px.
- Element gap: 14px.

### Spacing Scale

`8, 12, 28, 40, 48, 64, 68, 152`

### Radius Scale

| Element | Radius |
|---|---:|
| Buttons | 75px |
| Tags | 75px |
| Cards | 0px |
| Images | 0px |
| Inputs | 0px |
| Text links | 0px |

Never use intermediate radii between 1px and 74px. The system jumps from sharp editorial corners to full pills.

## Components

### Ghost Pill Button On Dark Surface

Transparent fill, 1px translucent white border, Paper text, 75px radius, Roobert 16px/400, and about 11px vertical by 33px horizontal padding. Use over the iridescent hero or dark media.

### Ghost Pill Button On Light Surface

Transparent fill, 1px Obsidian border, Obsidian text, 75px radius, Roobert 16px/400, and the same pill sizing as the dark variant.

### Filled Neutral Pill

Slate Pill fill, Paper text, 1px Paper border, 75px radius. Use for cookie consent or utilitarian confirmations. Do not turn this into a marketing CTA.

### Underline-Free Text Link

No background, no border, no underline, and 0px radius. Use Roobert 12px to 16px. Color should be Obsidian on light and Paper on dark.

### Hero Display Headline

Roobert 225px, weight 400, Paper text over full-viewport iridescent media. The headline is the hero. Avoid crowding it with subheads, cards, or heavy CTA stacks.

### Section Heading - Whisper

Roobert 78px, weight 300, line-height 1.10. Use for manifesto and atmospheric statements. It should feel quiet, not shouty.

### Section Heading - Anchor

Roobert 94px, weight 400, line-height 0.76. Use for dense editorial statement blocks where the text becomes the visual object.

### Project List Row

No card surface, no border, no radius, no shadow. Use a full-width image inside the 1078px container with sharp corners. Put the project title below in Roobert 16px to 18px.

### Top Navigation Bar

Transparent, fixed, about 66px tall. Wordmark on the left, locale switcher centered, menu stack on the right. No background fill, no shadow, no bordered nav container.

### Rotating Scroll Indicator

Circular typographic SVG badge near the lower-left hero area. Keep it black or white depending on surface. It is a quiet ornament, not a primary button.

## Layout

Use a centered 1078px content container for editorial sections, then break it with full-bleed dark and iridescent hero bands. The hero is full viewport with one monumental centered phrase over liquid media. After that, use spacious editorial pacing, asymmetric text-and-image pairings, full-width project entries, and a compact three-column footer address block.

## Motion

Use slow transitions with `cubic-bezier(0.19, 1, 0.22, 1)`. Transform and reveal motion can run from 0.8s to 1.25s. Do not make interactions snappy or springy. The feeling is patient and cinematic.

## Imagery

Use one massive iridescent fluid texture or video in the hero: sage green through molten amber into oxblood. Project images should be editorial photography or case-study stills with sharp corners and no frame. Avoid icons, illustrations, decorative shapes, and repeated gradients.

## Do

- Let a 225px Roobert display headline own the hero.
- Keep all UI colors in black, white, and gray.
- Reserve the iridescent gradient for hero media only.
- Use 75px radius exclusively for buttons and tags.
- Keep cards, images, inputs, and links at 0px radius.
- Use weight 300 at 78px for quiet editorial headlines.
- Use slow gliding motion.
- Use no shadows.

## Don't

- Do not introduce a chromatic UI color.
- Do not use gradients in buttons, badges, cards, or controls.
- Do not use border radii between 1px and 74px.
- Do not use heavy display weights above 45px.
- Do not center-align body copy in lists, addresses, or project descriptions.
- Do not use Raleway for body or navigation.
- Do not fill every section with imagery.
