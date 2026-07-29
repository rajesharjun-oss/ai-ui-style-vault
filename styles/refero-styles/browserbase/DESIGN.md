# Browserbase Style Reference

> Editorial developer tooling: giant geometric headlines, mono metadata, black pill actions, soft technical cards, and one hot orange accent used like punctuation.

## Theme

Light.

Browserbase feels like a data terminal laid out by a magazine art director. The interface is mostly black, white, and off-white, with pastel surfaces used to group content. Signal orange appears sparingly in headline highlights and the footer, while primary actions stay black.

## Core Principles

1. Use orange as emphasis, not as the primary action color.
2. Make black pill buttons the action language.
3. Pair oversized editorial headlines with tiny mono metadata.
4. Use pastel card fills to create grouping without shadows.
5. Keep cards flat with small radii and hairline borders.
6. Use digital-native imagery: dots, pixels, terminal blocks, code cards, and browser mockups.

## Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Ink Black | `#000000` | `--color-ink-black` | Primary text, button fill, borders, dividers |
| Paper White | `#ffffff` | `--color-paper-white` | Page canvas, card surfaces, button text |
| Graphite | `#686562` | `--color-graphite` | Muted body text and secondary borders |
| Signal Orange | `#ff4500` | `--color-signal-orange` | Headline highlight, focused edges, footer band |
| Blue Gray Mist | `#c5d3e8` | `--color-blue-gray-mist` | Hero tint, code-card surfaces, soft borders |
| Sky Tint | `#c4edff` | `--color-sky-tint` | Terminal/card backgrounds and inline washes |
| Lavender Mist | `#e2e9f3` | `--color-lavender-mist` | Feature cards and grouped content surfaces |
| Faint Slate | `#f8fafc` | `--color-faint-slate` | Logo strips and secondary panels |
| Cream Wash | `#fffde6` | `--color-cream-wash` | Warm secondary cards, badges, callouts |

## Typography

Use three distinct roles:

| Role | Family | Fallback | Use |
| --- | --- | --- | --- |
| Display | gtPlanar | GT America, Inter Tight | Editorial headings and hero type |
| Plain | plain | Inter, Geist | Body copy, nav, buttons, UI labels |
| Mono | gtStandardMono | JetBrains Mono, IBM Plex Mono | Eyebrows, captions, stat labels, code-adjacent metadata |

## Type Scale

| Role | Size | Weight | Line Height | Letter Spacing |
| --- | --- | --- | --- | --- |
| Caption | 14px | 400 | 1.2 | 0.6px |
| Body | 16px | 400 | 1.5 | 0.11px |
| Subheading | 24px | 500 | 1.3 | -0.12px |
| Heading | 34px | 400 or 500 | 1.15 | -0.68px |
| Heading large | 45px | 500 | 1.1 | -0.9px |
| Display | 189px | 500 | 1 | -9.45px |

Display text should use tight tracking. If using `gtPlanar`, apply the `ss05` feature when available. Mono labels should be uppercase and positively tracked.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | compact |
| Base unit | 4px |
| Max width | 1200px |
| Section gap | 64px to 96px |
| Card padding | 16px to 24px |
| Element gap | 8px to 16px |
| Card radius | 4px |
| Button radius | 50px |
| Tag radius | 999px |

Cards should feel crisp and flat. Use 4px radius for panels and 50px radius for buttons. Avoid soft SaaS-style roundness everywhere else.

## Layout

Use a full-bleed hero with a tinted atmospheric background, centered headline, and CTA stack. Content sits in a 1200px rail. Sections alternate between centered editorial headers, logo strips, feature card grids, and two-column product rows.

Recommended flow:

1. Sticky or flat top nav with black pill CTA.
2. Hero with blue-gray atmospheric background and oversized display headline.
3. Quiet logo strip on faint-slate cards.
4. Editorial feature sections with orange headline highlights.
5. Two-column product blocks with code or browser mockups.
6. Four-column feature card grid.
7. Full-width orange footer.

## Components

### Primary Pill Button

Black fill, white text, 16px plain font at medium weight, 8px by 21px padding, 50px radius. This is the only primary action surface.

### Ghost Button

Transparent background, 1px black border, black text, same pill geometry as the primary button. Use for secondary actions and utility actions.

### Orange Highlight Box

Inline block inside a headline. Use Signal Orange background with black text, matching the size and weight of surrounding display text. Padding should be tight, around 2px by 6px. Use once per headline.

### Navigation Bar

White background with a soft lavender border. Logo left, nav links centered or next to logo, auth links and black pill CTA on the right. Keep links plain black.

### Feature Card

Lavender Mist surface, 4px radius, 16px to 24px padding. Include a browser mockup or simplified product illustration, a compact headline, Graphite body copy, and optionally a black pill button.

### Logo Card

Faint Slate background, 4px radius, centered grayscale logo. Use a row or grid with tight 6px to 8px gaps.

### Code Or Terminal Card

Blue Gray Mist or Sky Tint background, 4px radius, 16px to 24px padding. Use mono labels and white input/code surfaces inside.

### Browser Window Mockup

White surface with a light lavender border and very small radius. Add three small window-control dots in the top bar. Keep inner UI simplified and monochrome with occasional orange emphasis.

### Section Header

Centered eyebrow in mono uppercase, then a GT Planar-style headline with one orange highlight box, then a 16px Graphite subtitle.

### Footer Band

Full-width Signal Orange background with black text. Use plain centered links and metadata. This is the only large orange surface.

## Surfaces

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 0 | Paper White | `#ffffff` | Main canvas and content sections |
| 1 | Faint Slate | `#f8fafc` | Logo strip and quiet secondary panels |
| 2 | Lavender Mist | `#e2e9f3` | Feature cards and grouped blocks |
| 3 | Blue Gray Mist | `#c5d3e8` | Hero atmosphere and code cards |
| 4 | Cream Wash | `#fffde6` | Warm badges and callouts |
| 5 | Signal Orange | `#ff4500` | Footer and typographic highlight |

## Elevation

Avoid box shadows. Depth is created through background color steps, 1px borders, and spacing. A soft blue-gray glow can appear behind a hero illustration, but normal cards should stay flat.

## Imagery

Use pixel art, dotted textures, terminal cursors, browser mockups, code cards, simplified UI diagrams, and coarse data visualizations. Do not use photography. The visual language should feel built from product primitives rather than stock illustration.

## Do

- Use black filled pill buttons for primary actions.
- Use Signal Orange for a single inline headline highlight or the footer.
- Apply tight negative tracking to display headlines.
- Use mono uppercase labels for metadata and section eyebrows.
- Use pastel panels to group content.
- Use 1px borders and flat surfaces instead of shadows.
- Keep the page mostly monochrome.

## Don't

- Do not use orange for normal button backgrounds or hover states.
- Do not use default blue links.
- Do not use shadows for card elevation.
- Do not put multiple orange highlights in one headline.
- Do not use display fonts for body text.
- Do not turn buttons into fully round 999px capsules.
- Do not use colorful text for body copy.

## AI Builder Notes

If the interface feels too plain, add a better headline composition or a more specific product mockup before adding more color. The brand energy should come from type scale, mono details, and the single orange punctuation mark.
