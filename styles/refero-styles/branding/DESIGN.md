# Branding - Style Reference

Branding feels like a dark gallery wall: massive white display type, almost no conventional UI chrome, hairline borders, rare red punctuation, and editorial typography that behaves more like signage than interface.

**Theme:** dark

## Summary

Build this style as a full-bleed black editorial canvas. Avoid dashboard language. The page should feel asymmetric, sparse, typographic, and cinematic. Scale and type contrast create hierarchy. Red appears as a border, dot, cursor, underline, or primary brand mark, not a broad surface.

## Tokens - Colors

| Name | Value | Token | Role |
|---|---:|---|---|
| Void Canvas | `#080808` | `--color-void-canvas` | Main page background and dark floor |
| Absolute Black | `#000000` | `--color-absolute-black` | Deepest surface, image overlays, decorative shapes |
| Charcoal Plate | `#171617` | `--color-charcoal-plate` | Footer and off-void dark panels |
| Smoke Plate | `#262525` | `--color-smoke-plate` | Secondary dark surfaces and image treatments |
| Graphite Lift | `#393939` | `--color-graphite-lift` | Subtle elevated card surface |
| Bone White | `#fcfcfc` | `--color-bone-white` | Primary text, borders, icon strokes |
| Linen | `#f3efef` | `--color-linen` | Inverted body panels and light editorial sections |
| Ash | `#d4d2d2` | `--color-ash` | Muted text, labels, subtle borders |
| Pebble | `#b5b2b2` | `--color-pebble` | Tertiary text and disabled borders |
| Iron | `#525252` | `--color-iron` | Link underlines, dividers, separators |
| Arterial Red | `#fe1e34` | `--color-arterial-red` | Sole saturated brand accent, featured borders, dots, CTA fill |
| Crimson Pure | `#ff0000` | `--color-crimson-pure` | Typographic underline/fill accent only |

## Typography

Kmr Waldenburg is the main voice for display, nav, body, buttons, and labels. Editorialnew appears as a soft italic companion between display words. Dirtyline 36 Daysoftype 2022 is used only for ornamental, single-letter spectacle.

| Role | Font | Size | Weight | Line Height | Tracking |
|---|---|---:|---:|---:|---:|
| Caption/nav | Kmr Waldenburg | 10px | 400 | 1.2 | 0.8px |
| Body | Kmr Waldenburg | 14px | 400 | 1.5 | -0.24px |
| Subheading | Kmr Waldenburg | 24px | 700 | 1.1 | -0.91px |
| Heading small | Kmr Waldenburg | 32px | 700 | 1.05 | -1.6px |
| Heading | Kmr Waldenburg | 42px | 700 | 1.05 | -2px |
| Heading large | Kmr Waldenburg | 64px | 700 | 1.0 | -4.8px |
| Display | Kmr Waldenburg | 80px | 700 | 0.9 | -6px |
| Display XL | Kmr Waldenburg | 160px | 700 | 0.9 | -12.8px |
| Italic connective | Editorialnew | 14-32px | 300 | 1.0-1.5 | tight |
| Ornament | Dirtyline 36 Daysoftype 2022 | 24-160px | 400 | 0.9-1.1 | tight |

## Spacing And Shape

- Page max width: none; the system is full-bleed.
- Section gap: 48-64px, with occasional 80px hero breathing room.
- Element gap: 24px.
- Card padding: 12-24px.
- Nav radius: 3px.
- Card radius: 8px.
- Button radius: 8px for outlined actions.
- Pill/action radius: 9999px for filled red action dots or compact pills.
- Large card radius: 14.4px.

## Components

**Ghost CTA Link**

Uppercase 12px Kmr Waldenburg with tracked letters, Bone White on Void Canvas, paired with a diagonal arrow icon. No fill, no border, no box. Treat calls to action as editorial pull-quotes.

**Discovery Call Outlined Button**

Top-right header affordance. Use uppercase 12px tracked text, 8px radius rectangle, 1px Ash border, 12px 24px padding, and a diagonal arrow icon.

**Primary Red Action**

Arterial Red background, Bone White text, compact pill padding, 9999px radius. Use rarely for true primary action or punctuating the design system.

**Hero Display Headline**

160px Kmr Waldenburg weight 700, all caps, 0.9 line height, very tight tracking, Bone White on Void Canvas. Editorialnew italic words can sit inline as connective tissue.

**Section Transition Headline**

80px Kmr Waldenburg caps with tight tracking, paired with one oversized Dirtyline ornamental letter. Use as a dramatic mid-page punctuation mark.

**Bordered Brand Card**

Void or Smoke background, 1px Arterial Red border, 8px radius, 24px padding. The red border is a featured marker, not decoration.

**Standard Card**

Void or Linen background, 1px hairline border, 8px radius, 12-24px padding. Dark variants may use a white inset highlight to suggest edge light.

**Hairline Link**

12-14px uppercase Kmr Waldenburg, tracked, with Iron or Pebble underline. No bright hover color.

**Top Navigation**

Transparent over the void. Logo at top-left, four column groups in the center, Discovery Call outlined action at top-right. No background fill.

**Footer Panel**

Full-bleed Charcoal Plate with Bone White text. Mirror the nav column structure and use at least 48px vertical padding.

**Accent Dot**

16-24px Arterial Red circle. No border and no shadow. Use as cursor-like punctuation near CTAs or as a small rhythm mark.

**Decorative Background Shape**

Oversized dark geometric shapes or letters in Charcoal Plate and Smoke Plate tones. Let them bleed off-canvas behind display type.

**Editorial Body Panel**

Linen background with Void Canvas text, 14px body copy, 1.5 line height, and compact section padding. Use as the single bright reading surface.

## Layout And Imagery

- Use full-bleed dark canvas with no max-width wrapper.
- Compose with internal padding rather than centered cards.
- Hero can fill the viewport and be dominated by display type.
- Alternate Void Canvas sections with occasional Linen inverted panels.
- Use 2-3 column card grids with 24px gaps only when needed.
- Use high-contrast editorial photography, collage, animal pattern textures, and oversized geometric shapes.
- Use full-bleed imagery with no rounded frames.
- Keep iconography minimal: 1px arrows and strokes in Bone White.

## Implementation Rules

Refuse conventional SaaS chrome. No bulky buttons, no bright icon sets, no gradient fills, and no busy card stacking. Let the dark canvas and aggressive display type do the work.
