# dope.security Style Reference

dope.security is a midnight security terminal with violet runway lighting. The foundation is flat black, white type, hairline strokes, frosted navigation, and tightly rationed violet. Typography carries the identity: Whyte Inktrap for the interface, Whyte Inktrap Mono for stamped section signposts, and GrandSlang italic for the largest dramatic phrases.

## Theme

Dark, cybersecurity, terminal, premium, secretive, luxury travel editorial, violet signal.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Near Black | `#090909` | `--color-near-black` | Page canvas, card surfaces, filled button backgrounds, and the default void. |
| Iron | `#423738` | `--color-iron` | Dark borders, separators, ghost washes, and subtle panel fills. |
| Graphite | `#474747` | `--color-graphite` | Card internal text and subtle dividers. |
| Ash | `#6b6b6b` | `--color-ash` | Nav dividers, helper text, and low-emphasis body copy. |
| Steel | `#828384` | `--color-steel` | Muted secondary text, inactive button surfaces, and subdued borders. |
| Soft White | `#f0f0f0` | `--color-soft-white` | Stamped uppercase section label text. |
| Almost White | `#f7f9fa` | `--color-almost-white` | Primary text, icon strokes, nav labels, and hairline borders. |
| Signal Violet | `#af50ff` | `--color-signal-violet` | The only chromatic signal: feature card glow, one primary fill, and accent strokes. |
| Lavender Mist | `#e1bdff` | `--color-lavender-mist` | Soft tint paired with Signal Violet for contrast-safe text and washed accents. |
| Frosted Nav | `rgba(51, 50, 72, 0.7)` | `--color-frosted-nav` | Sticky navigation background with backdrop blur. |
| Pink Wash | `rgba(237, 195, 196, 0.05)` | `--color-pink-wash` | Ghost pill and boarding-pass translucent panel fill. |

## Typography

### Whyte Inktrap

Use as the primary workhorse for body, nav, buttons, links, and most headings.

- Token: `--font-whyte-inktrap`
- Fallback: Inter, General Sans
- Weights: 300, 400, 500, 700
- Sizes: 10px to 88px
- Letter spacing: tight on display, wide on labels
- Role: precise geometric UI with warm inktrap cuts.

### Whyte Inktrap Mono

Use for stamped section headings and coordinate/data stamps.

- Token: `--font-whyte-inktrap-mono`
- Fallback: JetBrains Mono, IBM Plex Mono
- Weight: 400
- Sizes: 14px and 74px
- Letter spacing: 0.2em
- Role: section signposting and terminal-stamp copy.

### GrandSlang

Use only for the hero and large editorial echoes.

- Token: `--font-grandslang`
- Fallback: Tiempos Headline, Lora Italic
- Weights: 300, 400
- Sizes: 32px, 50px, 64px, 88px, 146px
- Letter spacing: -0.03em
- Role: warm brush-italic display drama.

Do not use GrandSlang for body, nav, labels, or anything under 32px.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | 10px | 1.00 | 1.8px | `--text-caption` |
| Body SM | 14px | 1.50 | 0 | `--text-body-sm` |
| Body | 16px | 1.50 | 0 | `--text-body` |
| Subheading | 20px | 1.00 | -0.2px | `--text-subheading` |
| Heading SM | 32px | 1.20 | -0.32px | `--text-heading-sm` |
| Heading | 48px | 1.20 | -0.48px | `--text-heading` |
| Heading LG | 64px | 1.20 | -0.64px | `--text-heading-lg` |
| Section Stamp | 74px | 0.90 | 14.8px | `--text-section-stamp` |
| Display | 88px | 0.80 | -2.64px | `--text-display` |

## Spacing And Shape

- Density: comfortable.
- Base unit: 4px.
- Max width: 1200px.
- Section gap: 120px.
- Card padding: 40px.
- Element gap: 16px.

### Spacing Scale

`4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 72, 80, 96, 128, 136, 160`

### Radius Scale

| Element | Radius |
|---|---:|
| Small controls | 6px |
| Buttons | 8px |
| Cards | 19.2px |
| Pills | 1584px |

## Components

### Hero Boarding Pass

Full-viewport dark hero over atmospheric twilight sky photography. Left side uses GrandSlang italic and Whyte Inktrap hero type. Right side uses a 19.2px translucent boarding-pass card with a faint pink wash, 1px low-opacity Almost White border, label, origin/destination line, vertical barcode, and two pill CTAs.

### Stamped Section Heading

Whyte Inktrap Mono, 74px, uppercase, 0.2em tracking, Soft White. Use as the main section signpost. No underline or decoration. The tracking is the design.

### Filled Action Button

Near Black background, 1px Almost White border, 8px radius, 16px padding, Almost White text in Whyte Inktrap 16px/400. Used for nav actions like Book a Demo and Log In.

### Ghost Pill Button

Pink Wash fill, no border, 1584px radius, 20px by 32px padding, Almost White text. Use for secondary actions inside translucent cards.

### Compact Outlined Button

Almost White at 8 percent fill, 1px Almost White border, 6px radius, 9px by 15px padding. Use for compact toolbars and inline controls.

### Frosted Nav Bar

Fixed top bar, Frosted Nav background, backdrop-filter blur(10px), 1px bottom Ash border, brand on the left, uppercase tracked nav in the center, and two bordered actions on the right.

### Comparison Card

19.2px radius, full-bleed gradient or violet bloom background, 40px padding, no border, no shadow. Cards may connect with route-line strokes and circular nodes.

### Feature Row Card

Transparent row with 19.2px radius and no visible container. Left link, right Whyte Inktrap body copy. Spacing defines the card.

### Violet Bloom Card

Signal Violet or violet radial bloom, 19.2px radius, 40px padding. Use one or two times per page at most.

### Coordinate Footer

Full-bleed dark footer with small plus icon, Fly Direct/Secure Web Gateway labels, and coordinate stamp in Whyte Inktrap 14px.

### Hairline Divider

0.5px or 1px Almost White stroke at 10 to 20 percent opacity. Use instead of shadow or heavy borders.

## Layout

Use full-bleed sections with a centered 1200px content max-width. The hero is split about 55/45, with text left and boarding-pass card right. Below the hero, use edge-to-edge dark bands, generous 120px section gaps, stacked stamped headings, comparison grids up to four columns, and left-aligned text rhythm.

## Imagery

Use one dramatic atmospheric hero photo: twilight sky, purple/lavender clouds, glowing horizon, and an airplane streak. After the hero, rely on typography, rules, icon glyphs, and radial bloom cards. Avoid product screenshots, lifestyle stock, and repeated photography.

## Do

- Use Signal Violet only for one feature glow, one filled action, and one accent stroke per page.
- Set section headings in Whyte Inktrap Mono at 74px uppercase with 0.2em tracking.
- Use 19.2px cards with translucent fills or layout-defined boundaries.
- Use low-opacity hairlines for separation.
- Use GrandSlang italic at 88px to 146px for the largest display moments.
- Use frosted nav with blur and a hairline bottom border.
- End pages with a coordinate stamp footer.

## Don't

- Do not apply box shadows beyond the nav hairline.
- Do not use Signal Violet for borders, text, or body backgrounds.
- Do not use GrandSlang below 32px.
- Do not mix Whyte Inktrap Mono with GrandSlang on the same line.
- Do not introduce another accent color.
- Do not center body copy or use multi-column text layouts.
- Do not use 0px or 4px buttons; use 8px buttons or huge pill CTAs.
