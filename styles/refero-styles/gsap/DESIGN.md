# GSAP Style Reference

GSAP is a dark motion-library system built like an animated chalkboard. The foundation is near-black and warm cream, while vivid accents identify animation disciplines. Typography and motion-coded taxonomy do the brand work; conventional marketing cards and filled CTAs should stay out of the system.

## Theme

Dark, motion library, developer tool, chalkboard, cream-on-black, taxonomy color, outlined pills, huge type, organic gradients.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Just Black | `#0e100f` | `--color-just-black` | Page canvas, footer surface, and deep section backgrounds. |
| Off Black | `#191919` | `--color-off-black` | Alternative dark surface for nested panels, code blocks, and footer layers. |
| Surface 25 | `#42433d` | `--color-surface-25` | Hairline borders, dividers, and low-contrast outlines against the black canvas. |
| Surface 50 | `#7c7c6f` | `--color-surface-50` | Muted secondary text, idle icon fills, subhead annotations, and disabled labels. |
| Surface Cream | `#fffce1` | `--color-surface-cream` | Primary text, outlined button borders, nav links, card text, headings, and ghost controls. |
| GSAP Green | `#0ae448` | `--color-gsap-green` | GSAP/core labels, brand marks, primary gradient stroke start, and short link accents. |
| Light Green | `#abff84` | `--color-light-green` | Primary gradient stroke end, GSAP short accents, and secondary green highlights. |
| Core Green | `#dfffd1` | `--color-core-green` | Subtle brand-tinted background washes for core feature cards. |
| Orangey | `#ff8709` | `--color-orangey` | SVG category label, orange tool icon fills, and orange gradient endpoints. |
| Pink | `#fec5fb` | `--color-pink` | Scroll category label, decorative splashes, and pink gradient endpoints. |
| Lilac | `#9d95ff` | `--color-lilac` | Text category label, thin illustration strokes, and violet gradient endpoints. |
| Blue | `#00bae2` | `--color-blue` | UI category label, blue gradient endpoints, and interface-tool accents. |
| Lipstick Pink | `#f100cb` | `--color-lipstick-pink` | Deep decorative gradient stop only; not for text or UI. |

## Typography

### Mori

Use as the single typeface across the system.

- Token: `--font-mori`
- Fallback: Inter Tight, Sohne, DM Sans
- Weights: 400, 600
- Sizes: 14px, 16px, 19px, 23px, 34px, 44px, 66px, 101px, 224px
- Line height: 0.90 to 1.40
- Letter spacing: -0.02em at 224px display, -0.011em for large headings, -0.01em for body and UI
- Role: all display, body, nav, labels, pills, cards, and footer copy.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | 14px | 1.40 | -0.14px | `--text-caption` |
| Body SM | 16px | 1.15 | -0.16px | `--text-body-sm` |
| Body | 19px | 1.15 | -0.19px | `--text-body` |
| Body LG | 23px | 1.38 | -0.23px | `--text-body-lg` |
| Subheading | 34px | 1.20 | -0.34px | `--text-subheading` |
| Heading SM | 44px | 1.20 | -0.44px | `--text-heading-sm` |
| Heading | 66px | 1.20 | -0.66px | `--text-heading` |
| Heading LG | 101px | 1.00 | -1.11px | `--text-heading-lg` |
| Display | 224px | 0.90 | -4.48px | `--text-display` |

## Spacing And Shape

- Density: comfortable.
- Base unit: 4px.
- Max width: 1280px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 16px.

### Spacing Scale

`8, 12, 16, 20, 24, 32, 76, 96, 108`

### Radius Scale

| Element | Radius |
|---|---:|
| Cards | 8px |
| Small tags | 8px |
| Buttons | 100px |
| Pills | 9999px |

## Components

### Outlined Cream Pill Button

Transparent fill, Surface Cream text, 1px Surface Cream border, 100px radius, 15px vertical and 24px horizontal padding, Mori 18px/600. Use for navigation entry points, explore links, and secondary actions. Never fill it with color.

### Gradient-Stroked CTA Pill

Transparent fill, Surface Cream text, 1.5px to 2px green-to-light-green gradient stroke, 100px radius, same sizing as other pills. This is the maximum CTA emphasis and should be reserved for the main download/get action.

### Ghost Nav Link

No background, no border, Surface Cream or Surface 50 text, Mori 16px/400, tight row gaps. Hover can shift toward Surface Cream.

### Borderless Icon Button

Round icon-only control, no visible background, cream icon, compact hit area. Use for menu/close/utility controls only.

### Category Color Label

Mori 19px to 24px/400, single-word discipline name in a fixed color mapping: GSAP green, SVG orange, Scroll pink, Text lilac, UI blue. The mapping must remain stable across all instances.

### Curly-Bracket Annotation

Small Mori 16px to 19px/400 Surface Cream text wrapped in literal curly braces. Use before every major section as a recurring signature.

### Hero Display Headline

Mori 224px/600, line-height 0.9, -0.02em tracking, Surface Cream. Let it wrap across two lines and bleed toward viewport edges. Do not constrain it to a narrow centered column.

### Tool Feature Block

Two-column row with organic gradient illustration on one side and category label, cream heading, body copy, and outlined pill on the other. Separate rows with a 1px Surface 25 hairline divider.

### Organic Gradient Illustration

Soft 3D-like pill, dome, liquid blob, or splash using a discipline accent gradient. It can overlap adjacent text and should feel lit from within. No card frame and no drop shadow.

### Showcase Card

Off Black or near-black surface, 8px radius, 24px padding, cream heading at 24px to 33px, contained preview area, no visible border. Use in 2-column or 3-column showcase grids.

### Announcement Banner

Full-bleed dark band with centered 14px Mori text in Surface Cream and optional GSAP Green inline link. No tinted background.

### Footer

Off Black footer with Surface 25 top divider, multi-column cream links, muted secondary text, and generous 60px to 80px vertical padding.

## Layout

Use a full-bleed Just Black shell. The hero lets the 224px display headline dominate and bleed toward edges, with organic color splashes overlapping text. Content sections use 1280px max width, 80px vertical rhythm, and clear tool-section rows divided by hairlines. The layout should feel like a motion showcase, not a SaaS grid.

## Imagery

Use organic gradient 3D-style shapes tied to the discipline color. Use soft internal lighting and loose overlap. Avoid stock photography, product dashboard screenshots, generic icons, neon glows, and conventional framed illustrations. Shapes should feel animated or about to move.

## Do

- Use Surface Cream instead of pure white.
- Use Just Black instead of pure black.
- Use the fixed discipline color mapping consistently.
- Render buttons as outlined 100px-radius pills.
- Reserve the gradient-stroked pill for the primary CTA.
- Push the hero headline to 224px/600 with 0.9 line-height.
- Introduce sections with curly-bracket annotations.
- Use Surface 25 dividers between tool feature rows.

## Don't

- Do not add filled solid CTA buttons.
- Do not use pure white text or pure black background.
- Do not reuse a discipline color for another discipline.
- Do not use color as random decoration.
- Do not center the hero inside a narrow max-width container.
- Do not add drop shadows to organic shapes.
- Do not introduce serif fonts or a second text family.
