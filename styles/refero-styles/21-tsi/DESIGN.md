# 21 TSI - Style Reference

> Luxury fashion editorial on black void: white Saans typography, ghost pill controls, a single hairline rule, and crimson photography carrying all emotion.

## Theme

Dark. The system is black by default and deliberately flat. Depth comes from the photograph, not from UI effects.

## Design Story

Build the interface like a runway campaign page. The UI chrome should feel printed onto the edge of the image: tiny uppercase labels, thin borders, transparent controls, and no decorative styling beyond primitive geometry.

The photograph is the hero. It should be full-bleed, near viewport-height, dramatically crimson, and not interrupted by text overlays. Text belongs above or below image sections, with its own black space.

## Tokens - Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Black Void | `#000000` | `--color-black-void` | Page canvas, deepest background, inverted button border on light fragments |
| Paper White | `#ffffff` | `--color-paper-white` | Primary text, nav labels, hairline rules, icon primitives, ghost button borders |
| Smoke | `#4d4d4d` | `--color-smoke` | Muted border for body cards and secondary structural lines |
| Crimson Heat | `#b62b1a` | `--color-crimson-heat` | Photo-only crimson atmosphere; do not apply as a UI fill |

## Typography

Only typeface: Saans.

- Use Saans for every glyph in the system.
- If Saans is unavailable, use Inter, Manrope, or a precise geometric sans fallback.
- Use weights 300, 380, 570, and 790.
- Weight 380 is the default UI voice.
- Weight 300 is used for dramatic oversized editorial display.
- Weight 570 is used for declarative display or stronger labels.
- Weight 790 is rare and should feel like a black shout.

## Type Scale

The scale has a deliberate gap. Below 20px it is UI chrome. From 47px upward it becomes editorial display. Avoid intermediate heading sizes.

| Role | Size | Weight | Line height | Tracking |
| --- | --- | --- | --- | --- |
| Micro UI | 12px | 380 | 1.14 | 0.6px or 0.05em |
| Small UI | 14px | 380 | 1.2 | 0.05em for uppercase |
| Body | 16px | 380 | 1.43 | 0.8px |
| Large UI | 18px | 380 | 1.2 | 0.05em for uppercase |
| Utility Large | 20px | 380 | 1.2 | 0.05em for uppercase |
| Display Small | 47px | 300 or 570 | 1.0 to 1.14 | -0.025em |
| Display Medium | 79px | 300 or 570 | 1.0 to 1.14 | -0.025em |
| Display Large | 106px | 300 or 570 | 1.0 to 1.14 | -0.025em |
| Display Hero | 130px | 300 | 1.08 | -3.25px |
| Display Max | 245px | 300 | 1.0 | -0.025em |

## Spacing And Shape

### Spacing Scale

| Token | Value |
| --- | --- |
| `--spacing-10` | 10px |
| `--spacing-11` | 11px |
| `--spacing-15` | 15px |
| `--spacing-19` | 19px |
| `--spacing-20` | 20px |
| `--spacing-23` | 23px |
| `--spacing-27` | 27px |
| `--spacing-30` | 30px |
| `--spacing-36` | 36px |
| `--spacing-38` | 38px |
| `--spacing-60` | 60px |
| `--spacing-63` | 63px |
| `--spacing-108` | 108px |
| `--spacing-150` | 150px |
| `--spacing-172` | 172px |

### Radius

| Element | Value |
| --- | --- |
| Body card | 8px |
| Ghost buttons | 70px |
| Circular frame | 594px |

## Components

### Top Hairline Navigation

Use a 1px white rule edge-to-edge at the top. Below it, place white 12px uppercase Saans labels. Use about 38px horizontal spacing between nav groups. The logo is text based: `21|TSI`, with the bar drawn as a 1px white primitive.

### Ghost Pill Button

Transparent fill, 1px white border, 70px radius, 10px vertical padding, 20px horizontal padding, 12px uppercase Saans, weight 380, and 0.6px tracking. Contact-style active buttons may include a 4px white leading dot.

### Text Utility Control

No border and no background. Use white uppercase 12px Saans with the same tracking as pill controls. Hover can be a slight opacity change only.

### Full-Bleed Editorial Hero

Use a 100vw photograph at about 90vh or more. No overlay, no gradient, no scrim, no text placed over the image. Subject should sit off-center with crimson lighting and deep black shadow.

### Display Headline

Set oversized Saans in white on black, outside the image area. Use 79px to 245px depending on the moment. Avoid the 20px to 47px middle range.

### Circular Portrait Frame

Use a square crop with 594px radius for a full circle. This is a rare geometric counterpoint to the full-bleed photography.

### Body Card

Use only when a text block truly needs containment. Transparent or black fill, 1px Smoke border, 8px radius, 20px padding, 16px Saans body text, and no shadow.

## Layout

The layout is full-bleed by design. Do not use a standard max-width content container. Let images occupy the whole viewport width, and give type separate black sections with generous empty space. UI chrome should hug the top edge rather than forming a heavy header block.

## Imagery

The imagery should be cinematic fashion editorial. Use a single human subject, profile or three-quarter pose, off-frame or downcast gaze, warm crimson side lighting, crushed black shadows, bronzed skin tones, motion in hair or fabric, and slight grain. Avoid multiple subjects, daylight studio whites, direct eye contact, and busy compositions.

## Rules

Do:

- Keep UI chrome to black, white, and one 1px rule.
- Use Saans or a precise geometric sans for all type.
- Use positive tracking for 12px to 20px uppercase UI labels.
- Use 70px pill radius on interactive controls.
- Keep crimson inside the photography.
- Use full-bleed images and separate text space.

Do not:

- Do not use solid red CSS backgrounds or red buttons.
- Do not use filled colored CTAs.
- Do not place body copy over photography.
- Do not add shadows, glow, glass, blur, or elevation.
- Do not introduce a second typeface or icon font.
- Do not use a max-width page container.
- Do not invent medium heading sizes between 20px and 47px.
