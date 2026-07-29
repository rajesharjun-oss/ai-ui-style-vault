# xAI - Style Reference

## North Star

Build the interface like a warm laboratory bench for frontier AI tools: mostly white, softly cream layered surfaces, huge quiet headlines, terminal details, and one pure near-black pill CTA. The page should feel technical and editorial without becoming cold.

## Theme

Light. Paper is the page canvas. Cream is the elevated surface. Jet Ink is the main text and action color. Accent color is rare and belongs to beta tags, terminal dots, and product mockup interiors.

## Color Tokens

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Jet Ink | `#0a0a0a` | `--color-jet-ink` | Primary text, filled CTA buttons, logo mark, main hierarchy anchor |
| Charcoal | `#151515` | `--color-charcoal` | Dark code-block surface behind terminal demos |
| Slate | `#3b3b3b` | `--color-slate` | Muted heading variant, secondary section labels |
| Steel | `#545454` | `--color-steel` | Mid-weight body text, inline stats, spec lines |
| Fog | `#858585` | `--color-fog` | Secondary text, icon strokes, inactive nav items, link copy |
| Pewter | `#9d9d9d` | `--color-pewter` | Tertiary text, metadata, decorative fills |
| Dove | `#d5d9e2` | `--color-dove` | Hairline borders, input rings, button focus outlines |
| Sand | `#f2ede5` | `--color-sand` | Warm wash backgrounds, subtle highlight zones, beta pill surface |
| Cream | `#f9f8f6` | `--color-cream` | Card surfaces, secondary panels, tag backgrounds |
| Paper | `#ffffff` | `--color-paper` | Page background, button text on filled CTAs, icon foreground on dark surfaces |
| Ember | `#ff5f57` | `--color-ember` | Terminal traffic-light red dot only |
| Sunbeam | `#ffbd2e` | `--color-sunbeam` | Terminal yellow dot and rare novelty signal |
| Sprout | `#28c840` | `--color-sprout` | Terminal traffic-light green dot only |

## Typography

Use universalSans for interface and body copy, universalSansDisplay for H1/H2, and GeistMono for technical fragments.

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| Caption | 12px | 400 | 20px | -0.12px |
| Body Small | 14px | 500 | 20px | 0 |
| Body | 16px | 400 | 24px | 0 |
| Utility | 18px | 400 | 29px | 0 |
| Heading Small | 24px | 500 | 32px | -0.6px |
| Subheading | 30px | 400 | 36px | -0.75px |
| Heading | 48px | 400 | 48px | -1.2px |
| Heading Large | 60px | 500 | 60px | -1.5px |
| Display | 72px | 400 | 72px | -1.8px |

Font roles:

- universalSans: nav, body, buttons, cards, labels, inline links. Use weights 400 and 500.
- universalSansDisplay: H1 and H2 only. Use 400 and 500, sizes 24px to 72px, line-height 1.0 to 1.33, and tracking around -0.025em.
- GeistMono: terminal mockups, code snippets, metadata, and language tabs. Use 10px to 13px with line-height 1.50 to 1.85 and tracking -0.01em.

Rules:

- Authority comes from type size and line-height, not heavy weight.
- Headlines should be massive, quiet, tightly tracked, and close to 1.0 line-height.
- Keep body between 14px and 18px.
- Do not use bold body copy as hierarchy.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | Comfortable |
| Base unit | 4px |
| Max width | 1200px |
| Section gap | 80px |
| Card padding | 40px |
| Element gap | 12px |

Spacing scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 96, 144.

Radius scale:

- Inputs: 6px.
- Small cards: 8px.
- Cards: 16px.
- Terminal mockups: 12px.
- Buttons, tags, and language tabs: 9999px.

Elevation:

- Compact nav button and ghost focus ring: `rgba(10, 10, 10, 0.15) 0px 0px 0px 1px`.
- Sticky header: `rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px`.
- Elevated cream card: `rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(15, 23, 42, 0.18) 0px 18px 40px -24px`.

## Components

### Filled Primary Button

Use Jet Ink background, Paper text, 9999px radius, 12px vertical padding, 20px horizontal padding, universalSans 14px/20px at 500 weight, no border, and no shadow. This is the single high-contrast action on the page.

### Ghost Secondary Button

Use transparent background, Jet Ink text, 9999px radius, 12px vertical padding, 20px horizontal padding, universalSans 14px/20px at 500 weight, and no visible border by default. Hover or focus may add a Dove or subtle ring.

### Compact Nav Button

Use Paper background, Jet Ink text, 9999px radius, 6px vertical padding, 12px horizontal padding, and 1px Dove border. It is smaller than hero buttons and belongs in the sticky header.

### Beta Tag Pill

Use Sand background, Jet Ink text, 9999px radius, 2px vertical padding, 8px horizontal padding, and universalSans 12px at 500 weight. Use only for feature-release or beta moments.

### Flat Cream Card

Use Cream background, 8px to 16px radius, no shadow, no border, and media flush to the surface edge. Product mockups such as chat, voice, build, and imagine tiles sit here.

### Pricing Tier Card

Use Cream background, 16px radius, 40px padding, no shadow, tier name in 24px universalSansDisplay at 500 weight, and body/spec lines in 14px universalSans.

### Terminal Code Block

Use Charcoal background, 12px radius, GeistMono 12px to 13px, and traffic-light dots at the top-left: Ember, Sunbeam, and Sprout. Syntax highlight colors stay inside the mockup and are not global brand tokens.

### Language Tab Pill

Use 9999px radius, 6px vertical padding, 12px horizontal padding, and GeistMono 13px. Active state uses Jet Ink background with Paper text. Inactive state uses transparent background and Fog text.

### Navigation Link

Use universalSans 14px/20px at 500 weight, Fog text by default, Jet Ink on hover, no underline, no background. Focus may underline.

### News Card

Use no card surface, no border, no radius, and no padding. Place image first, date metadata in 11px Fog text, and title in 16px Jet Ink 500 weight. The news grid should feel like an index, not a gallery.

### Feature Stat Block

Use an 18px Jet Ink number above an 11px Pewter label. No wrapper card. Keep it inline within a feature column.

### Checklist Row

Use universalSans 14px/20px at 400 weight in Jet Ink with a leading Jet Ink check stroke. Stack rows with 8px gap and no dividers.

## Layout And Imagery

- Center the page in a 1200px max-width container on a full-bleed Paper canvas.
- Use 80px vertical gaps between major sections.
- Hero is text-first and centered, with one filled primary CTA and one ghost secondary action.
- Follow the hero with a 2-column product-card row.
- Alternate into text-left and product-mockup-right feature sections.
- Use a 4-column news index.
- End with 2-column pricing or CTA tier cards.
- Navigation is a single sticky top bar around 64px high with logo, horizontal menu, and two right-aligned actions.
- Product visuals should be UI screenshots, code panels, waveform cards, and warm gradient mockups.
- Do not use lifestyle photography, 3D renders, stock images, or human figures.

## Do

- Use Jet Ink for the primary filled button.
- Set all headlines at 24px and above with tight negative tracking.
- Apply 9999px radius to buttons, tags, and language tabs.
- Use Cream for surfaces that sit above the page.
- Reach for GeistMono whenever the content is technical.
- Keep beta and release badges rare.
- Use ghost or outlined buttons for non-primary actions.

## Do Not

- Do not use chromatic colors for buttons or links.
- Do not stack shadows.
- Do not set body text below 14px or above 18px on screen.
- Do not add background colors to nav links, news cards, or inline list items.
- Do not use line-heights above 1.63 for running text.
- Do not introduce new radii beyond 6px inputs, 8px small cards, 16px cards, 12px terminal, and 9999px pills.
- Do not use pure black `#000000`; use Jet Ink `#0a0a0a`.
