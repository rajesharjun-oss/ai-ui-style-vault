# Kajabi - Style Reference

## North Star

Build the interface like a clean gallery wall for human expertise. The UI should almost disappear: pure white canvas, near-black type, sharp rectangular controls, and no brand color. Photography and video supply all warmth and emotion.

## Theme

Light. Paper White is the default surface. Charcoal appears only for dark bands and video framing. Every non-photo UI color is achromatic or warm gray.

## Color Tokens

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Paper White | `#ffffff` | `--color-paper-white` | Page canvas, card surfaces, inverse text on dark backgrounds |
| Ink Black | `#0a0a0a` | `--color-ink-black` | Primary text, filled CTA buttons, navigation, footer |
| Charcoal | `#1f1f1e` | `--color-charcoal` | Dark section backgrounds, video frame borders, elevated dark surfaces |
| Smoke | `#333333` | `--color-smoke` | Input text, focused form borders, higher-emphasis neutral copy |
| Stone | `#535250` | `--color-stone` | Secondary body text, muted helper text, subdued list and border accents |
| Driftwood | `#949189` | `--color-driftwood` | Tertiary text, icon strokes, subtle borders |
| Sand | `#bcb9ae` | `--color-sand` | Link borders at rest, muted borders, decorative dividers |
| Graphite | `#d4d3ce` | `--color-graphite` | Stronger form borders, table separators, visible dividers |
| Ash | `#e0dedc` | `--color-ash` | Hairline borders, card outlines, dividers between content blocks |
| Mist | `#e9e8e7` | `--color-mist` | Light surface tint, input backgrounds, secondary card surfaces |

## Typography

Use Haffer if available. Fallback to Inter, Sohne, or General Sans.

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| Caption | 12px | 400 | 1.5 | 0 |
| Body Small | 14px | 400 | 1.45 | 0 |
| Body | 16px | 400 | 1.5 | 0 |
| Subheading | 20px | 400 | 1.4 | 0 |
| Heading Small | 24px | 500 | 1.3 | -0.4px |
| Heading | 32px | 500 | 1.2 | -0.64px |
| Heading Large | 40px | 600 | 1.1 | -0.8px |
| Poster | 48px | 500 | 1 | -1.2px |
| Display | 60px | 400 | 1 | -1.8px |

Rules:

- Use one typeface across the entire system.
- Let scale create hierarchy more than weight.
- Use Haffer 400 for most headlines.
- Use 500 for subheadings and emphasis.
- Reserve 600 for stats and numerical display, not marketing headlines.
- Apply tight tracking only at 40px and larger.
- Keep body copy at normal tracking.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | Comfortable |
| Base unit | 4px |
| Max width | 1280px |
| Section gap | 64px to 80px |
| Card padding | 20px |
| Element gap | 12px to 24px |

Spacing scale: 4, 8, 12, 16, 20, 24, 32, 40, 44, 64, 68, 120.

Radius scale:

- Buttons: 2px.
- Inputs: 2px.
- Cards: 2px.
- Images: 2px.
- Pill tabs and tags: 9999px.
- Course overlay cards may use 8px when floating above video.

Surface rules:

- Buttons, inputs, and standard cards are flat.
- Do not add shadows to ordinary controls.
- Use a slight shadow only for product UI overlays above video.

## Components

### Primary Filled Button

Use Ink Black background, Paper White text, Haffer 16px at 500 weight, 2px radius, 12px vertical padding, 24px horizontal padding, and no shadow.

### Secondary Outlined Button

Use transparent fill, 1px Ink Black border, Ink Black text, Haffer 16px at 500 weight, 2px radius, 12px vertical padding, and 20px horizontal padding.

### Email Input With Inline CTA

Use Paper White background, 1px Ash border, 2px radius, Haffer 16px text, and Driftwood placeholder. Attach or tightly align the filled black CTA button to create a single horizontal signup unit around 48px tall.

### Top Navigation Bar

Use a white top bar around 64px to 72px high. Place logo and wordmark left, center links in Haffer 14px at 500 weight, and Login plus Start Free Trial actions right. Use a 1px Mist bottom border or no visible separation.

### Expert Portrait Card

Use full-bleed portrait photography with 2px radius or sharp edges. Add a dark bottom gradient overlay for name and title. Arrange portrait cards in a horizontal strip with zero or minimal gaps so the people become the color band.

### Category Tab Pill

Use 9999px radius, 8px vertical padding, 16px horizontal padding, Haffer 14px at 500 weight. Active tabs invert to Ink Black background and Paper White text. Inactive tabs use transparent or Mist surface.

### Stats Display

Use large numerical values at 48px, Haffer 400 or 600 depending on emphasis, tight tracking, and Ink Black. Labels below use 16px Stone. Arrange as a centered three-column row on desktop.

### Video Hero Frame

Use a Charcoal section background with a near-full-width video frame at 2px radius. Add a white circular play control if needed and allow a course content card to float on the right.

### Course Content Card Overlay

Use a Paper White surface, 8px radius, about 24px padding, thumbnail-and-title rows, 16px 600 title text, and 14px supporting copy. This is one of the few places where a subtle lift is allowed.

### Dark Section Band

Use full-width Charcoal background, about 80px vertical padding, centered white headline, and optional pill tabs or content grid.

### Two-Column Text And Form

Use white background, text left, email input plus button right, 28px to 32px headline, 16px Stone description, and about 40px gap from previous section content.

### Logo Lockup

Use a small dark abstract mark with the kajabi wordmark in Haffer 20px at 600 weight. Keep an 8px gap and align on the baseline.

## Layout And Imagery

- Center content in a 1280px max-width container.
- Build the hero as a centered text stack with headline, subtext, and email plus CTA.
- Use a full-width horizontal portrait strip below the hero.
- Use a centered three-column stats row.
- Use Charcoal bands to frame video or category areas.
- Return to Paper White for newsletter and editorial sections.
- Keep navigation thin, white, and restrained.
- Let expert portraits, creator photos, warm video, and real human environments supply color.

## Do

- Use `#0a0a0a` for filled buttons and primary text.
- Keep all rectangular UI at 2px radius.
- Use 9999px radius only for pill tabs and tags.
- Let photography and video carry all chromatic color.
- Apply tight tracking at display sizes 40px and above.
- Maintain 64px to 80px vertical breathing room between major sections.
- Use Haffer 400 for headlines and scale for hierarchy.

## Do Not

- Do not introduce chromatic brand colors.
- Do not use 8px or 12px radius on normal buttons, cards, or inputs.
- Do not use 600+ weight for marketing headlines.
- Do not add drop shadows to standard buttons, inputs, or cards.
- Do not break the white page with colored backgrounds other than Charcoal inversion.
- Do not letter-space body text.
- Do not use icon strokes outside the 1.5px to 2px range.
