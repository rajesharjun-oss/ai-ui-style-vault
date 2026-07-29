# ON.energy - Style Reference

> High-voltage caution yellow on midnight steel: full-bleed industrial sections, whisper-light type, flat surfaces, and a single yellow signal.

## Theme

Mixed. The page alternates between dark image sections, pure yellow statement sections, and industrial white content sections. There is no single gentle canvas; the rhythm is built from hard section changes.

## Design Story

Build the interface like industrial signage wrapped around hardware photography. The system should feel precise, restrained, and engineered. Yellow is the voltage moment. Black is the steel floor. White is the technical document surface.

Do not create hierarchy with shadows or gradients. Use contrast, full-bleed section changes, tight tracking, light type weights, and generous 120px section gaps.

## Tokens - Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Caution Yellow | `#fff313` | `--color-caution-yellow` | CTA fill, full-bleed yellow sections, accent borders, small emphasis |
| Midnight Steel | `#000000` | `--color-midnight-steel` | Page canvas, dark hero, nav background, text on yellow |
| Industrial White | `#eeeeee` | `--color-industrial-white` | Light section backgrounds, text on dark, news card surfaces |
| Carbon | `#333333` | `--color-carbon` | Nav pills, dark cards, elevated dark surfaces without shadow |
| Gunmetal | `#4b4b4b` | `--color-gunmetal` | Hairline borders, dividers, subtle dark structure |
| Aluminum | `#afafaf` | `--color-aluminum` | Muted body text on dark backgrounds, footer text |

## Typography

Only typeface: Univers Next Pro.

- Use weight 300 for all display, headlines, section statements, and hero text.
- Use weight 400 for body, UI, nav, and buttons.
- Do not use weights 500, 600, or 700.
- Substitute with Inter 300/400, Neue Haas Grotesk, or Helvetica Neue Light/Regular if the font is unavailable.
- Use tight tracking at larger sizes: `-0.04em` at 36px and above, `-0.02em` at 16px to 24px.

## Type Scale

| Role | Size | Weight | Line height | Tracking |
| --- | --- | --- | --- | --- |
| Micro | 10px | 400 | 1.2 | normal |
| Caption | 12px | 400 | 1.2 | normal |
| Body Small | 14px | 400 | 1.2 | normal |
| Body | 16px | 400 | 1.2 | -0.02em |
| Heading | 24px | 300 | 1.17 | -0.48px |
| Heading Large | 36px | 300 | 1.13 | -1.44px |
| Display | 64px | 300 | 1 | -2.56px |

## Spacing And Shape

- Base unit: 4px.
- Density: comfortable.
- Section gap: 120px.
- Card padding: 24px.
- Element gap: 16px.
- Navigation controls: 6px radius.
- Buttons: 6px radius.
- Cards: 9px radius.
- Images: 16px radius.
- Sections: 24px radius when a section itself needs rounding.

## Components

### Yellow CTA Button

Caution Yellow fill, Midnight Steel text, 6px radius, 7px vertical padding, 16px horizontal padding, Univers Next Pro 400 at 14px. No shadow, no gradient. This is the only chromatic interactive button.

### Dark Navigation Pill

Carbon background, Industrial White text, 6px radius, 5px vertical padding, 14px horizontal padding, Univers 400 at 14px. Use as a row of compact nav pills over yellow or image sections.

### Logo Mark

Small Caution Yellow square with black `ON` text. Keep corners sharp. It acts as a compact signal mark against dark navigation.

### Hero Headline

Univers Next Pro 300 at 64px, line-height 1, tracking `-0.04em`, Industrial White on dark product photography. Left align and leave large negative space below.

### Product Highlight Card

Dark Carbon or near-black surface, 9px radius, 24px padding, optional Gunmetal border or yellow accent. Include product thumbnail on the right and yellow label text on the left.

### Full-Bleed Yellow Statement Section

Caution Yellow fills the full viewport width and often the full viewport height. Use large weight-300 Univers statements at 36px to 64px. Text should be black or a carefully muted yellow tone, never low-contrast decorative clutter.

### News Image Card

Industrial White section with image card grid. Images use 16px radius. Title uses Univers 300 at 24px in black. Arrange in a 2-column grid with 16px gaps.

### Section Heading

Univers 300 at 36px, line-height 1.13, tracking `-0.04em`, black on light sections. Left align with generous spacing above.

### Body Text Block

Univers 400 at 16px, line-height 1.2. Use black on yellow or white sections, Aluminum on dark sections. Constrain to about 400px to 500px width.

### Navigation Bar Container

Transparent or semi-transparent over hero images, solid black or Carbon over yellow and light sections. Contains logo left, nav pills center, and yellow CTA right.

## Layout

Use a full-bleed page model without a global max-width constraint for the major sections. Structure the page as a sequence of three visual modes:

- Dark industrial hero with product photography and white headline.
- Pure yellow statement section with large ghosted or black text.
- Industrial white content sections with left-aligned copy and 2-column image grids.

Light content can use a centered column with 400px to 500px copy width. Keep 120px between major visual sections so each section reads like a separate act.

## Imagery

Use industrial product photography: metal panels, rack hardware, power equipment, infrastructure, and deployment shots. Use dark moody lighting for hero images. Avoid lifestyle context, people operating equipment, staged office scenes, abstract graphics, and decorative 3D renders. Hardware should be the hero.

## Rules

Do:

- Use weight 300 for display and heading text.
- Use weight 400 for body and UI.
- Use Caution Yellow only for CTAs, full yellow sections, and small accents.
- Alternate full-bleed dark image, yellow, and industrial white sections.
- Use fixed contrast pairs: black on yellow, white on dark.
- Use 6px radius on nav and buttons, 9px on cards.
- Maintain 120px major section gaps.

Do not:

- Do not add shadows.
- Do not add gradients.
- Do not use type weights 500, 600, or 700.
- Do not use yellow body text on yellow backgrounds.
- Do not use black text on black.
- Do not use large radii above 16px on functional elements.
- Do not constrain full-bleed color sections to a max-width container.
