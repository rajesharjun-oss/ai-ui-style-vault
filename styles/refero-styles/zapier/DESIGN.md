# Zapier - Style Reference

## North Star

Build the interface like a sunlit maker's notebook for automation: warm paper surfaces, practical product UI, open editorial headings, one bright orange action, and human-friendly spacing. It should feel like craft and systems thinking, not infrastructure.

## Theme

Light. Cream Paper is the primary canvas. Parchment is the secondary band and card surface. Ember Orange is the singular chromatic UI accent. Iris Ink belongs only inside illustrations.

## Color Tokens

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Ember Orange | `#ff4f00` | `--color-ember-orange` | Brand mark, filled buttons, key highlights, small icon accents |
| Iris Ink | `#2b2358` | `--color-iris-ink` | Illustration-only violet accent, never UI chrome, buttons, or text |
| Cream Paper | `#fffefb` | `--color-cream-paper` | Primary canvas, card surfaces, input backgrounds |
| Parchment | `#f8f4f0` | `--color-parchment` | Secondary surface, section bands, soft elevated cards |
| Stone Linen | `#eceae3` | `--color-stone-linen` | Hairline borders, dividers, muted surface tints |
| Driftwood | `#c5c0b1` | `--color-driftwood` | Muted borders, disabled backgrounds, low-contrast dividers |
| Ash Mist | `#b7b6b3` | `--color-ash-mist` | Disabled text, placeholders, very subtle borders |
| Ink Brown | `#201515` | `--color-ink-brown` | Primary text, dark UI elements, logo wordmark |
| Bark | `#36342e` | `--color-bark` | Secondary headings, nav text, medium-emphasis body copy |
| Coffee Stone | `#413735` | `--color-coffee-stone` | Tertiary text, resting links, breadcrumb text |
| Stone Gray | `#939084` | `--color-stone-gray` | Muted helper text, captions, metadata, compliance lines |
| Obsidian | `#000000` | `--color-obsidian` | Maximum-contrast icons, footer text, logo detail only |

## Typography

Use Inter for functional UI, Degular Display for brand/editorial headings, and GT Alpina for rare serif lift.

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| Caption | 12px | 500 | 1.5 | -0.1px |
| Body Large | 16px | 400 | 1.5 | -0.16px |
| Subheading | 18px | 400 | 1.43 | -0.18px |
| Heading Small | 24px | 600 | 1.33 | -0.43px |
| Heading | 32px | 400 | 1.25 | -0.58px |
| Heading Large | 36px | 500 | 1.2 | -0.72px |
| Display | 48px | 500 | 1.14 | -1.34px |
| Display Large | 56px | 500 | 1.1 | -1.57px |

Font roles:

- Inter: nav, buttons, forms, card body, captions, and product UI. Use 400 for body, 500 for buttons/nav, 600 for emphasis.
- Degular Display: hero headlines, section headings, uppercase eyebrow labels. Use positive tracking: 0.020em at small labels, 0.033em at 30px, 0.042em at 40px, 0.071em at 80px. Enable `"ss01"` if available.
- GT Alpina: one editorial heading per page, weight 250 or 300, 40px to 48px, line-height 1.08 to 1.20, tracking -0.040em.

Rules:

- Do not tighten Degular Display; its open tracking is the point.
- Do not use GT Alpina for body, navigation, cards, forms, or buttons.
- Use warm near-black text rather than pure black for primary copy.
- Use negative tracking on Inter as it grows larger.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | Comfortable |
| Base unit | 4px |
| Max width | 1200px |
| Section gap | 64px to 96px |
| Card padding | 24px to 32px |
| Element gap | 8px to 16px |

Spacing scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 56, 64, 72, 80, 96, 112, 160.

Radius scale:

- Tags: 4px.
- Inputs: 4px.
- Cards: 8px.
- Buttons: 20px.
- Large panels: 32px.
- True pills: 9999px.

Elevation:

- Default to no drop shadow.
- Separate surfaces with Stone Linen and Driftwood hairline borders.
- Product showcase panels may use a subtle warm shadow around `rgba(32, 21, 21, 0.08) 0px 4px 24px`.

## Components

### Brand-Orange Filled Button

Use Ember Orange background, Cream Paper text, no border, 20px radius, 12px vertical padding, 20px horizontal padding, Inter 15px at 500 weight, tracking about -0.15px, and no shadow. This is the only chromatic filled button in the system.

### Outlined Button

Use Cream Paper background, 1px Ink Brown border, Ink Brown text, 20px radius, 12px vertical padding, 20px horizontal padding, and Inter 15px 500. Optional lead icon can use its natural color with a 12px gap.

### Ghost Text Link

Use no fill, no border, Coffee Stone text, Inter 15px at 500 weight, tracking -0.15px, and underline only on hover. Do not make this a pill.

### Navigation Bar

Use Cream Paper background, 64px height, logo left, nav items in Inter 15px 500 Ink Brown, 24px link gap, and right cluster with text links plus Ember Orange Sign up button. Sticky state may add a Stone Linen bottom border.

### Announcement Bar

Use Ink Brown or a similarly dark warm background, Cream Paper text, 13px Inter 500, centered single-line copy, and 8px vertical by 16px horizontal padding. Close icon sits at the right.

### Template Card

Use Cream Paper background, 1px Stone Linen border, 8px radius, 24px padding, top row of 2 to 3 app icons at 24px square with 8px gap, and a 16px Inter 600 Ink Brown heading. On hover, darken the border to Driftwood. Do not add shadow.

### Feature Section Card

Use Parchment background, no border, 8px radius, 32px padding, 24px Inter 600 Ink Brown headline, 15px Inter 400 Bark body, and optional small Ember Orange icon accent.

### Security Or Trust Badge

Use Cream Paper background, 1px Stone Linen border, 4px radius, 6px vertical padding, 12px horizontal padding, Inter 13px 500 Bark text, and optional small icon in Ember Orange or Coffee Stone.

### Eyebrow Label

Use text-only Inter 12px 600 Ember Orange, uppercase, letter-spacing 0.042em. May be preceded by a small orange rule or dot. No background.

### Text Input

Use Cream Paper background, 1px Driftwood border, 4px radius, 16px padding, placeholder in Ash Mist, Inter 16px 400, and Ink Brown focus border. No glow ring. Minimum height about 56px.

### Partner Logo Strip

Use flat grayscale logos in Coffee Stone or Stone Gray on Cream Paper. Arrange 6 logos per row, each around 80px to 120px wide with 64px gaps. No hover effects, badges, or captions.

### Product Showcase Panel

Use a full-bleed warm photographic blur as the outer background. Place a centered product UI frame around 960px wide with Cream Paper surface, 1px Stone Linen border, 8px radius, 20px padding, and subtle warm shadow. Optional play button can sit in a white circle.

### Footer Link Group

Use no background. Group title is Inter 13px 600 Ink Brown with 0.042em tracking. Links are Inter 15px 400 Coffee Stone with 12px row gap and no underlines.

## Layout And Imagery

- Use a 1200px max-width centered container.
- Include a full-bleed top announcement bar when needed.
- Use a sticky 64px navigation bar.
- Hero often uses a 2-column split: left headline and CTA stack, right editorial illustration.
- Trust logo strip is centered as one grayscale row.
- Product showcase sections may break full-bleed with a centered 960px product frame.
- Template sections use 3-column grids on warm cream.
- Major vertical gaps can range from 80px to 120px.
- Use editorial illustration in Ember Orange, Iris Ink, and Cream Paper.
- Product screenshots are dominant; lifestyle photography and stock imagery are not.

## Do

- Use Cream Paper or Parchment for all page and card backgrounds.
- Use Ember Orange only for filled buttons, the logo glyph, and small icon accents.
- Keep Ember Orange under about 5 percent of any layout.
- Use Degular Display with positive letter spacing.
- Use GT Alpina weight 250 once per page for editorial lift.
- Set button radius to 20px.
- Layer warm neutrals for text hierarchy.
- Follow the 4px spacing rhythm.

## Do Not

- Do not use stark white or pure black as primary surfaces.
- Do not apply negative letter spacing to Degular Display headings.
- Do not use Iris Ink in UI chrome, buttons, or text.
- Do not add heavy drop shadows.
- Do not let Ember Orange fill large background areas.
- Do not use cool blue-grays.
- Do not exceed 56px for body headings or 160px for hero display without checking the type scale.
