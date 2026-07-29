# Reflect Notes - Style Reference

## North Star

Build the interface like a dark observatory for thought: notes float as constellations on a violet-black canvas, panels catch subtle rim light, and one lavender accent guides attention. The UI should feel calm, intelligent, and focused rather than dashboard-like.

## Theme

Dark. Void Canvas is the base. Midnight Surface and Deep Indigo create depth. Lilac White is the main readable text color. Lavender Accent is the only primary chromatic signal. Gradients are reserved for accent text and thin strokes.

## Color Tokens

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Void Canvas | `#030014` | `--color-void-canvas` | Page background, hero canvas, deepest surface layer |
| Midnight Surface | `#060317` | `--color-midnight-surface` | Elevated surface, card backgrounds, nav pill, panels |
| Deep Indigo | `#10093a` | `--color-deep-indigo` | Most elevated surface, hover states, prominent panels, deep button surface |
| Steel | `#54525f` | `--color-steel` | Deepest muted text, disabled labels, dark-mode border contrast |
| Dusk | `#72707b` | `--color-dusk` | Secondary borders, inactive icon strokes, subtle background tints |
| Fog | `#918ea0` | `--color-fog` | Tertiary text, metadata, helper text, inactive controls, border lines |
| Ash | `#a8a6b7` | `--color-ash` | Secondary body text and card labels |
| Mercury | `#cdccd0` | `--color-mercury` | Bright dividers, subtle borders, light-on-dark surface tints |
| Lilac White | `#f4f0ff` | `--color-lilac-white` | Primary text, headings, icons, high-contrast UI elements |
| Pearl | `#ffffff` | `--color-pearl` | Text on violet-filled elements and maximum contrast headlines, used sparingly |
| Lavender Accent | `#9382ff` | `--color-lavender-accent` | Links, active icons, focus rings, gradient endpoints, highlight punctuation |
| Iris | `#5046e4` | `--color-iris` | Supporting violet accent for buttons, decorative details, and low-frequency emphasis |
| Cosmic Gradient | `linear-gradient(90.01deg, #e59cff 0.01%, #ba9cff 50.01%, #9cb2ff 100%)` | `--color-cosmic-gradient` | Accent text and thin decorative strokes only |
| Aurora | `linear-gradient(180deg, rgba(183,164,251,0) 0%, #b7a4fb 50%, #8562ff 100%, rgba(133,98,255,0) 100%)` | `--color-aurora` | Divider lines and edge highlights only |

## Typography

Use AeonikPro for headings at 24px and above. Use Inter V for body and UI.

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| Caption | 12px | 400 | 1.33 | 0 |
| Body Small | 14px | 400 | 1.43 | 0 |
| Body | 16px | 400 | 1.5 | 0 |
| Body Large | 18px | 400 | 1.56 | 0 |
| Subheading | 24px | 500 | 1.33 | 0 |
| Heading Small | 32px | 500 | 1.25 | -0.2px |
| Heading | 48px | 500 | 1.17 | -0.3px |
| Heading Large | 56px | 500 | 1.14 | -0.4px |
| Display | 72px | 500 | 1.11 | -0.5px |

Font roles:

- AeonikPro: display and heading typeface at 24px and above. Weight 500 only. Fallback: Aeonik, Inter, DM Sans.
- Inter V: body, nav, buttons, inputs, badges, testimonials, and interface labels. Weights 400 and 500. Fallback: Inter, Geist, system-ui.

Rules:

- Do not use bold or extra-bold weights.
- Use AeonikPro 500 for 48px to 72px headings.
- Use Inter V 16px/1.5 for body text.
- Keep Pearl for button text and special maximum contrast moments; body text should use Lilac White or Ash.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | Comfortable |
| Base unit | 4px |
| Max width | 1200px |
| Section gap | 96px to 120px |
| Card padding | 24px to 32px |
| Element gap | 8px to 16px |

Spacing scale: 4, 8, 12, 16, 20, 24, 28, 32, 36, 48, 52, 56, 64, 72, 108, 232.

Radius scale:

- Buttons: 5px.
- Inputs: 5px.
- Cards and screenshots: 16px.
- Feature blocks: 24px.
- Badges: 32px.
- Nav pill: 999px.

Elevation:

- Cards and elevated surfaces: inset white glow, `rgba(255,255,255,0.04) 0px 0px 24px 0px inset` or `rgba(255,255,255,0.06) 0px 0px 24px 0px inset`.
- Pill badges and AI labels: inset violet glow, `rgba(164,143,255,0.12) 0px -7px 11px 0px inset`.
- Do not use external drop shadows.

## Components

### Navigation Pill

Use a floating centered pill with 999px radius, Midnight Surface background, and subtle inset white glow. It contains logo, nav links, login text link, and a filled CTA. Height is about 40px with compact horizontal padding. Nav links use Inter V 15px 400 Lilac White. Login uses Fog.

### Primary CTA Button

Use Iris background, Pearl text, 5px radius, Inter V 15px 500, and 10px vertical by 16px horizontal padding. Hover may move toward Deep Indigo or a lighter violet wash. Do not use gradients as button fills.

### Ghost Text Button

Use no background, Inter V 15px 400, Fog text, 5px radius, and hover to Lilac White. Use for login and secondary actions.

### AI Badge Pill

Use 32px radius, Midnight Surface background, Iris border, Inter V 13px 500 Lilac White text, optional sparkle icon, and inset violet glow. Use above hero or section headings.

### Hero Product Screenshot

Use a full-width app screenshot in the hero, 16px radius, low-opacity Fog or Mercury border, and inset white glow. It should show a notes editor, sidebar, daily notes panel, calendar, or AI writing surface.

### Feature Card

Use no visible card background or border. Place a 1.5px stroke icon, then an AeonikPro 18px to 20px 500 title in Lilac White, then Inter V 15px 400 description in Fog. Cards float directly on the Void Canvas.

### Feature Icon

Use 24px outlined geometric icons, 1.5px stroke, Lilac White, no fill. Good shapes include clock, globe, phone, lock, calendar, cursor, square, and search.

### Testimonial Card

Use Midnight Surface background, 16px radius, 24px padding, inset white glow, circular 40px avatar, name in Inter V 15px 500 Lilac White, handle in Inter V 14px 400 Fog, and quote text in Inter V 15px 400 Lilac White. Inline mentions may use Lavender Accent.

### Section Header

Use centered AeonikPro 48px to 56px 500 Lilac White headline and Inter V 18px 400 Fog subtitle. May be preceded by an AI Badge Pill.

### Text Link With Chevron

Use Inter V 15px 500 Lavender Accent with a small chevron icon. Hover may transition to Lilac White. Keep radius at 5px.

### Star Field Background

Use tiny low-opacity Pearl dots on Void Canvas, 1px to 2px, scattered gently in the hero. It should feel like a constellation, not confetti.

### Aurora Divider

Use a 1px horizontal or vertical line with Aurora gradient. Use sparingly as a section separator or feature-grid edge highlight.

## Layout And Imagery

- Use a centered max-width around 1200px with 24px to 48px horizontal padding.
- Navigation is a floating pill centered at the top, not a full-width bar.
- Hero is full-bleed dark with centered headline, subtitle, and wide product screenshot below.
- Use 96px to 120px vertical gaps between sections.
- Keep the page as one continuous Void Canvas, not alternating background bands.
- Feature sections use 4-column grids, often 8 features in 2 rows.
- Testimonials use 3-column grids, often 6 cards in 2 rows.
- Use product screenshots, icons, and small avatars. Avoid lifestyle photography, illustrations, and 3D renders.

## Do

- Set the page background to Void Canvas.
- Use Lilac White or Ash for body text.
- Use AeonikPro 500 at 48px to 72px for headings.
- Use 5px radius for buttons, inputs, and interactive elements.
- Use 16px radius for cards and screenshots.
- Use 32px radius for pill badges.
- Use 999px only for the nav container.
- Apply inset rim-light glows instead of drop shadows.
- Use Lavender Accent only for links, active states, focus rings, and small accent icons.
- Use Cosmic Gradient only on text and thin strokes.

## Do Not

- Do not use pure black for the page canvas.
- Do not use bold or extra-bold text.
- Do not use drop shadows on cards or panels.
- Do not use accent color for large fills or backgrounds.
- Do not use gradients as button or section backgrounds.
- Do not use body text in pure white.
- Do not introduce semantic red, green, or yellow status colors.
- Do not introduce a second accent hue.
