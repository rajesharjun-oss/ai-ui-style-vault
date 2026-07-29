# Dyotanya - Style Reference

> Editorial sketchbook on warm paper: oversized serif statements, dusty-blue borders, coral links, circular imagery, and hand-drawn black line work.

## Theme

Light. The base is warm paper, not sterile white. The system should feel analog, personal, and a little irregular, while still being clean enough for a modern portfolio.

## Design Story

Build the page like a designer's annotated sketchbook. Use huge serif type as the primary visual element. Let thin black SVG lines loop around text, connect cards, underline phrases, and create a hand-drawn rhythm.

Cards, buttons, and inputs should look pasted onto the paper. Avoid soft shadows and glass effects. Elevation is a hard charcoal offset, paired with rounded white surfaces and dusty-blue borders.

## Tokens - Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Warm Paper | `#f5f5f3` | `--color-warm-paper` | Page canvas and analog off-white base |
| Ink Black | `#000000` | `--color-ink-black` | Main text, line art, borders, icons |
| Charcoal | `#333333` | `--color-charcoal` | Hard offset shadows, inverted surfaces, secondary dark text |
| Pure White | `#ffffff` | `--color-pure-white` | Card surfaces, button fills, high-contrast light panels |
| Dusty Sky | `#81aed9` | `--color-dusty-sky` | Decorative borders, inputs, brand stroke, soft blue action fills |
| Cobalt Wash | `#55a1ea` | `--color-cobalt-wash` | Brighter blue interactive state |
| Coral Link | `#ff8562` | `--color-coral-link` | Inline link text only |

## Typography

Display serif: Simeiz, with Playfair Display or DM Serif Display as accessible substitutes.

- Use for all major headings and expressive words.
- Use 300 weight for large roman text.
- Use 400 italic for emotional words inside a heading.
- Use at 80px for hero statements, 46px to 48px for section titles, and 24px to 30px for smaller headings.

Functional UI: Manrope, with Inter or DM Sans as fallback.

- Use for nav, buttons, captions, form fields, labels, and body support text.
- Use weights 400, 500, and 600.
- Keep functional text compact and slightly tracked at about `-0.036em`.

Fallback serif: Times, with Times New Roman as fallback.

- Use only as a simple body fallback if the signature serif is unavailable.

## Type Scale

| Token | Size | Weight | Line height | Role |
| --- | --- | --- | --- | --- |
| Caption | 12px | 400 | 1.2 | Fine labels and tiny notes |
| Body Small | 14px | 400 | 1.2 | Card body, captions, support copy |
| Body | 16px | 400 | 1.56 | Regular text |
| Body Large | 18px | 300 | 1.55 | Larger editorial body copy |
| Subheading | 24px | 300 | 1.35 | Serif subheadings |
| Heading Small | 30px | 300 | 1.33 | Project card headings |
| Heading | 48px | 300 | 1 | Section titles |
| Display | 80px | 300 | 1 | Hero statement |

## Spacing And Shape

- Density: compact details inside generous sections.
- Page max width: 1200px.
- Section gap: 80px.
- Card padding: 48px.
- Element gap: 10px to 20px.
- Border width: 1.5px.
- Cards: 20px to 30px radius.
- Buttons: 30px radius or 3000px pill radius.
- Inputs: 30px radius.
- Circular images: 120px radius.

## Elevation

Use hard offset shadows only:

- Cards: `5px -5px 0 0 #333333`
- Buttons: `4px -4px 0 0 #333333`

No blur, no soft alpha shadow, no glass, and no glow.

## Components

### Hero Serif Statement

Large warm-paper hero with flowing 80px serif text. Mix roman and italic words within the same line. Place a circular portrait or decorative line inside the text flow. Do not split the hero into a standard text-left/image-right layout.

### Pill CTA Button

Large rounded capsule with 1.5px black border, hard charcoal offset shadow, Manrope 14px medium uppercase text, and either white or dusty-blue fill depending on hierarchy. Never use coral as a button fill.

### Client Showcase Card

White card, 30px radius, 1.5px dusty-blue border, 48px padding, and a hard charcoal offset shadow. Use circular project images, a serif project title, small Manrope description text, and an editorial number marker.

### Circular Portrait

Crop portraits and project images to a 120px circular shape with a 1.5px black border. Use sparingly and let the image sit inline with type when possible.

### Hamburger Menu Trigger

Small circular top-right button with black border, hard offset shadow, and three simple black strokes.

### Hand-Drawn Line

Inline SVG path with no fill, `#000000` stroke, 1.5px stroke width, and organic curves. These lines should connect layout elements rather than sit as isolated decoration.

### Input Field

30px radius, 1.5px dusty-blue border, 20px horizontal padding, Manrope 16px text, and minimal focus treatment.

## Layout

Use asymmetric editorial composition. Keep content inside a 1200px frame, but allow oversized type and SVG lines to break the strict grid. Portfolio cards can stagger and overlap rather than forming equal columns. Navigation is minimal and may collapse into a single circular trigger.

## Imagery

Use sparse circular portraits and circular project thumbnails. Keep images muted, personal, and portfolio-specific. Avoid full-bleed hero photography, SaaS product mockups, stock lifestyle imagery, and icon-heavy grids.

## Rules

Do:

- Use warm paper as the page background.
- Use Simeiz-style serif for every display moment above 20px.
- Mix roman and italic within display headings.
- Use 1.5px dusty-blue borders on cards and inputs.
- Use coral only for inline links.
- Use hard offset shadows for all elevation.
- Add hand-drawn black SVG line work as a structural motif.

Do not:

- Use pure white as the page background.
- Use soft shadows, blur, glow, or opacity-based elevation.
- Use Manrope for large headings.
- Use coral for button fills or borders.
- Use sharp corners on interactive elements.
- Align the hero like a rigid corporate split layout.
