# Sequel - Style Reference

## Positioning

Sequel feels like a private screening room for a founder network or family office. The interface should be almost entirely black, with a single warm cream light used for primary actions. It is not a neon dark mode, a SaaS dashboard dark mode, or a luxury palette with gold accents. The restraint is the identity.

## Theme

- Theme: dark
- Mood: private cinema, warm lamp, family-office discretion
- Best fit: invite-only communities, premium membership, founder stories, private advisory, intimate editorial products

## Visual Principles

1. Start with pure black.
2. Use cream only for the primary filled action.
3. Let warm cinematic photography carry emotion.
4. Keep surfaces shadowless; use charcoal tone for elevation.
5. Make interactive controls pill-shaped.
6. Use a single serif italic word for emotional emphasis, not full serif paragraphs.
7. Avoid all chromatic accents.

## Color System

| Token | Value | Role |
| --- | --- | --- |
| Lamp Cream | `#f5f5f0` | Primary filled action, the only warm accent |
| Void Black | `#000000` | Page canvas, nav background, deepest icon fill |
| Charcoal | `#202020` | Elevated card and panel surface |
| Graphite | `#333333` | Hairline borders, badge outlines, subtle dividers |
| Smoke | `#999999` | Muted text, captions, secondary labels |
| Pure White | `#ffffff` | Primary text, ghost button border, icon strokes |

## Typography

Use VisueltPro as the main interface and editorial font. It should cover navigation, body copy, buttons, labels, headlines, and story text. Use weight 300 for quiet large headings and weight 500 for display, headings, and buttons.

Use Bradford only as an italic accent word inside a headline. It should feel like an editorial whisper, not a separate type system.

Recommended fallbacks:

- Primary sans: `VisueltPro`, `Inter`, `Satoshi`, `General Sans`, `ui-sans-serif`, `system-ui`
- Accent serif: `Bradford`, `Canela`, `Tiempos Headline`, `GT Super`, `Georgia`, `serif`

OpenType features:

```css
font-feature-settings: "ss01" 1, "cv11" 1;
```

### Type Scale

| Role | Size | Line Height | Weight | Tracking |
| --- | ---: | ---: | ---: | ---: |
| Label Small | 11px | 1.5 | 500 | 0.55px |
| Body | 16px | 1.5 | 400 | 0 |
| Body Large | 20px | 1.5 | 400 | 0 |
| Subheading | 30px | 1.2 | 500 | -0.75px |
| Heading | 54px | 1.2 | 300 | 0 |
| Heading Large | 57px | 1 | 500 | -2.85px |
| Display | 128px | 1 | 500 | -3.2px |

## Spacing And Shape

- Base unit: 4px
- Density: comfortable
- Page max width: 1200px
- Section gap: 96px to 120px
- Element gap: 16px
- Card padding: 0px, unless inner content requires local padding
- Card and media radius: 10px
- Buttons, chips, and badges: 9999px
- Inputs: square, 0px radius when needed
- Play button: circular, 50% radius

## Layout

Use a pure black page canvas and a 1200px content column. The hero should feel cinematic and full-bleed, with the navigation floating transparently over it. Below the hero, alternate large editorial headline blocks, cinematic media cards, and quiet text sections with generous vertical breathing room.

Use a bottom gradient scrim only over media when text needs readability. Do not use decorative gradients elsewhere.

## Imagery

Use warm, cinematic, documentary-style portraits and film stills. The photography should feel private, dimly lit, human, and editorial. Avoid stock SaaS photos, neon abstractions, colored 3D objects, and generic business illustrations.

## Components

### Primary Filled Pill Button

Lamp Cream background, Void Black text, 9999px radius, VisueltPro 16px weight 500. Use this for the one primary action on a screen.

### Ghost Outline Pill Button

Transparent background, 1px Pure White border, Pure White text, 9999px radius, VisueltPro 16px weight 500. Use for secondary actions.

### Frosted Glass Badge

Translucent gray fill, 20px backdrop blur, Pure White uppercase label, pill radius, and a subtle inset rim. Use over media, not as a generic decoration.

### Elevated Card

Charcoal background, 10px radius, no border and no shadow. Elevation is created by the jump from black to charcoal.

### Cinematic Media Card

Full-bleed warm image, 10px radius, optional bottom scrim, bottom-left text overlay, and optional frosted badge. Do not add padding or a heavy frame.

### Video Play Button

Circular outline with a play glyph and small uppercase label. Place it near the bottom-right of hero media.

### Section Display Heading

Large white VisueltPro heading, sometimes with a single Bradford italic accent word. Keep the heading sparse and cinematic.

### Top Navigation

Transparent over hero, black after scroll if needed. Left wordmark, center or right links, and one cream CTA. No nav border, no heavy background, and no boxed tabs.

## Rules

- Use Lamp Cream only for the main filled action.
- Keep all chromatic color out of the interface.
- Use 9999px radius for buttons, badges, chips, and pill controls.
- Use 10px radius for cards and media.
- Use negative tracking on display text at 57px and above.
- Use positive tracking for uppercase labels and badges.
- Use Charcoal surfaces instead of shadows.
- Do not use bold weights above 500.
- Do not use gradients except a media readability scrim.
- Do not add a third accent color.
