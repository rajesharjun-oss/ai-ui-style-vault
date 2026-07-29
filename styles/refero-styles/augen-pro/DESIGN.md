# Augen Pro Style Reference

## Summary

Augen Pro is a weightless clinical-white product system. It feels like a high-end Apple keynote at half volume: deep charcoal typography, PP Neue Montreal-like 350-weight text, soft pill controls, enormous negative space, and Signal Blue used only as wireframe interaction.

The page should feel expensive because it refuses to shout. Hierarchy comes from scale, spacing, surface tone, and precision, not bold type, color fills, shadows, or decoration.

## Theme

Light.

## Personality

- Clinical
- Premium
- Weightless
- Surgical
- Quiet
- High-tech
- Minimal
- Editorial

## Color System

The live UI is monochrome plus Signal Blue. Blue is functional wireframe color, not paint.

| Name | Value | Token | Use |
| --- | --- | --- | --- |
| Off-Black | `#0f1012` | `--color-off-black` | Primary text, hero and footer backgrounds, icon fills |
| Pure Black | `#020201` | `--color-pure-black` | Secondary text, hard emphasis, maximum contrast details |
| Steel Gray | `#5e5e5e` | `--color-steel-gray` | Muted body text, captions, inactive labels |
| Ash Gray | `#8f8f8f` | `--color-ash-gray` | Disabled text, tertiary helper text, very low-emphasis labels |
| Off-White | `#f2f2f4` | `--color-off-white` | Page canvas and large light fills |
| Pure White | `#fdfdfd` | `--color-pure-white` | Elevated panels, nav pills, inputs, cards |
| Signal Blue | `#0071e3` | `--color-signal-blue` | Text links, tag borders, interactive outlines, small link icons |

## Typography

Use PP Neue Montreal if available. Otherwise use Inter, General Sans, or Sohne-style fallback at light/regular weights. Weight 350 carries almost everything.

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| Heading | 27px | 350 | 32.4px | -0.54px |
| Subheading | 18px | 350 | 21.6px | -0.36px |
| Body | 16px | 350 | 19.2px | -0.32px |
| Small Body | 14px | 350 | 16.8px | -0.28px |
| Button Label | 13px | 400 | 15.6px | -0.26px |
| Micro | 12px | 350 | 14.4px | -0.24px |
| Caption | 10px | 350 | 12px | -0.2px |

## Font Rules

- Use weight 350 by default for all text from 10px to 27px.
- Use 400 only for tiny button or icon labels.
- Never use medium, semibold, bold, or black weights.
- Apply `letter-spacing: -0.0200em` uniformly.
- Use stylistic alternates when available: `ss01`, `ss02`, `cv01`, `cv11`.

## Spacing And Shape

- Density: spacious
- Max width: 1200px
- Section gap: 90px to 100px
- Card padding: 69px
- Element gap: 6px
- Nav top offset: 34px
- Footer top padding: 50px
- Floating nav horizontal padding: 11px to 30px
- Hairline element radius: 1.8px
- Nav pills: 10px radius
- Buttons: 26px radius
- Large cards: 54px radius
- Body containers: 63px radius
- Tags and links: 9999px radius

## Surfaces

| Level | Surface | Value | Role |
| --- | --- | --- | --- |
| 0 | Page Canvas | `#f2f2f4` | Full-page cool off-white background |
| 1 | Elevated Panel | `#fdfdfd` | Cards, nav, tag chips, inputs, secondary panels |
| 2 | Dark Surface | `#0f1012` | Footer and full-contrast dark bands |

## Elevation

Do not use shadows. Elevation comes from Pure White panels on Off-White canvas and from 0.5px hairline borders.

Use:

```css
border: 0.5px solid rgba(0, 0, 0, 0.06);
```

For softer structural lines:

```css
border-color: rgba(0, 0, 0, 0.04);
```

## Components

### Pill Navigation Bar

Floating horizontal Pure White bar, 10px radius, about 11px to 30px horizontal padding, positioned around 34px from the top. Include a small star or compass icon and simple text links. This is a floating control, not a full-width header.

### Ghost Link Button

No fill and no border. Off-Black text at 16px weight 350. Underline may appear on hover.

### Signal Blue Text Link

Signal Blue text, no fill, no underline at rest, optional 0.5px Signal Blue bottom border on hover. Use 16px weight 350.

### Pill Tag Chip

9999px radius, 0.5px Signal Blue border, Signal Blue text, no fill, 2px vertical and 10px horizontal padding, 10px to 12px weight 350.

### Rounded Card

Pure White surface, 54px radius, 0.5px semi-transparent black hairline, 69px padding, no shadow.

### Floating CTA Pill

26px radius, near-transparent charcoal wash, Pure Black 13px weight 400 text, and a small Signal Blue link icon. It should feel present but quiet.

### Dark Band Footer

Full-width Off-Black band with centered Pure White text at 10px to 16px weight 350. Use 50px top padding and 69px horizontal padding.

### Section Label Pair

Muted 10px to 12px Ash Gray label above a 27px Off-Black title, both weight 350. Hierarchy comes from size only.

### Inline Icon Link

Small Signal Blue link icon paired with Signal Blue text. Use for research links, updates, and navigation affordances.

### Update Banner

Small floating banner with a translucent charcoal wash, quiet text, and a Signal Blue outlined NEW badge. Keep it small and restrained.

## Layout

Use full-bleed sections with 1200px centered content. The navigation floats at the top center. The hero is full-viewport with a 3D render centered-right and text bottom-left. Below the hero, use editorial sections separated by 90px to 100px vertical gaps.

The Breakthrough-style section can use an asymmetric 3-column grid:

- Narrow label column.
- Wide 27px heading column.
- Supporting paragraph column.

Footer is a full-width dark band. Keep long body copy left-aligned.

## Imagery

Imagery is extremely sparse. Use one high-fidelity 3D rendered human or device portrait that fades into white. Avoid photography, illustration, gradients, patterns, and product screenshots. The render carries visual depth; the UI stays nearly weightless.

Iconography should be minimal: small star or compass mark, tiny link glyphs, simple strokes.

## Do

- Use weight 350 as the default for all text.
- Use Signal Blue only for links, outlines, icons, and interactive edges.
- Use 54px radius on large cards.
- Use 9999px radius on tags and pills.
- Keep 90px to 100px section gaps.
- Use Off-Black on light surfaces and Pure White on dark surfaces.
- Render nav and controls as floating pills, not full bars.
- Use -0.0200em tracking everywhere.
- Use tone shifts and hairline borders for elevation.

## Do Not

- Do not use drop shadows.
- Do not fill any element with Signal Blue.
- Do not use font weights above 400.
- Do not center-justify multi-line body copy.
- Do not add decorative gradients, patterns, or background imagery.
- Do not use green, orange, or yellow as UI accents.
- Do not exceed 1200px content width.
- Do not turn the system into a busy dashboard.
