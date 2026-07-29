# Creative Giants - Style Reference

## North Star

Build the page like an art-book poster with only the necessary web controls attached. The warm cream canvas is the structure, the photography is the visual mass, and the display type is large enough to become image-like. Keep everything thin, sharp, quiet, and deliberate.

## Theme

Light. Bone White is the only page canvas. Black text and black pill controls provide contrast. Chromatic accents appear only as card surfaces, small fills, borders, badges, or hover signals.

## Color Tokens

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Bone White | `#fffef7` | `--color-bone-white` | Page canvas, card surfaces, text on dark accents, warm paper tone |
| Ink Black | `#000000` | `--color-ink-black` | Text, icons, black menu pill, high contrast details |
| Graphite | `#666666` | `--color-graphite` | Secondary body text, captions, metadata, helper copy |
| Ash | `#aaaaaa` | `--color-ash` | Input borders, inactive links, tertiary dividers, quiet outlines |
| Charcoal Scale | `#4d4c4a` | `--color-charcoal-scale` | Warm gray for list borders and rare dark gradient track |
| Magenta Bloom | `#8a0467` | `--color-magenta-bloom` | Decorative pink accent, low-frequency emphasis, editorial borders |
| Forest Teal | `#03624c` | `--color-forest-teal` | Saturated accent for card frames, strokes, and duotone treatments |
| Powder Blue | `#a5c8eb` | `--color-powder-blue` | Soft card background, cool wash, muted illustration fill |
| Candy Pink | `#ffacea` | `--color-candy-pink` | Pastel card surface and high-key editorial tint |
| Mint Wash | `#a5ebd6` | `--color-mint-wash` | Pastel card surface and calm cool accent block |
| Navy Ink | `#101731` | `--color-navy-ink` | Deep accent card surface and rare inverted text ground |
| Signal Yellow | `#ffd001` | `--color-signal-yellow` | Tiny badges, tag pills, hover state, sporadic high-chroma highlight |

## Typography

Use Switzer if available. Otherwise use Inter, Sohne, or another geometric humanist sans with a real 300 weight.

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| Caption | 12px | 400 | 1.43 | -0.018em |
| Body Small | 14px | 400 | 1.43 | -0.018em |
| Body | 16px | 400 | 1.4 | -0.018em |
| Body Large | 18px | 300 | 1.4 | -0.018em |
| Subheading | 20px | 300 | 1.4 | -0.018em |
| Heading Small | 34px | 300 | 1.25 | -0.02em |
| Heading | 54px | 300 | 1 | -0.023em |
| Poster | 64px | 300 | 1 | -0.027em |
| Display | 84px | 300 | 1 | -0.04em |

Rules:

- Use one family across the system.
- Use weight 300 for display, hero, section headlines, and oversized editorial text.
- Use weight 400 for controls, metadata, captions, and standard body where readability needs it.
- Never bold a heading.
- Tighten tracking more as the type gets larger.
- Keep display statements to one or two lines.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | Comfortable |
| Base unit | 8px |
| Section gap | 64px |
| Card padding | 24px |
| Element gap | 8px |

Spacing scale: 8, 16, 24, 32, 48, 64, 80, 112.

Radius scale:

- Cards: 0px.
- Images: 0px.
- Buttons: 1440px.
- Tags: 1440px.
- Pills: 1440px.

Shadow rule:

- Default to no shadow.
- The only acceptable subtle outline is `rgba(255, 255, 255, 0.2) 0px 0px 0px 1px` on rare dark surfaces.

## Components

### Pill Menu Button

Black fill, Bone White text, 16px type, 400 weight, 1440px radius, 12px vertical padding, 24px horizontal padding, no border. It should sit with generous white space and act as the only visually heavy header control.

### Header Lockup

Use a two-line uppercase eyebrow at 12px, 400 weight, Ink Black, paired with a 32px circular logo mark. Place the Menu pill at the opposite edge. Do not add a header background; the page canvas is the header background.

### Display Poster Headline

Use 84px Switzer, weight 300, line-height 1, tracking -0.04em, Ink Black. It should span almost the whole viewport width and stay to two lines or fewer.

### Hero Image Band

Use full-width editorial photography with no radius and no shadow. Place small location or category metadata and a 34px lightweight headline near the lower-left edge with about 32px padding.

### Section Title Block

Use a small all-caps eyebrow in Graphite followed by a 34px to 54px statement headline at weight 300. Let whitespace separate the block from surrounding content.

### Project Or News Card

Use a 3-column grid where the image sits above the copy. Keep card borders, shadows, and radius at zero. Use 18px to 20px lightweight titles, 14px Graphite body copy, and an optional 1px Magenta Bloom or Forest Teal accent border on the image edge.

### Chromatic Accent Card

Use Candy Pink, Mint Wash, Powder Blue, or Navy Ink as occasional card fills. Use Ink Black text on pastel fills and Bone White text on Navy Ink. Keep radius at 0px and padding at 24px to 32px. Do not use more than one chromatic card in a row.

### Carousel Arrow Control

Use a 32px circular outline button, 1px Ash border, transparent fill, centered 16px Ink Black chevron icon. On hover, darken only the border.

### Meta Eyebrow

Use 12px Switzer, 400 weight, uppercase, Graphite, single-line. Apply to locations, categories, section names, and project metadata.

### Full-Bleed Footer

Keep the footer on the same Bone White canvas with a 1px hairline divider. Use multi-column link lists at 14px, 400 weight, Ink Black, and 8px row gaps. Reserve any charcoal-to-black gradient only for rare dark footer variants.

### Tag Or Category Pill

Use 8px vertical padding, 12px horizontal padding, 1440px radius, 12px uppercase text. Default is transparent fill, Ink Black text, and 1px Ash border. Accent variant uses Signal Yellow fill and Ink Black text.

## Layout And Imagery

- Let the cream canvas provide structure through negative space.
- Use hairline margins and sharp edges instead of panels or floating cards.
- Put one giant headline, one full-bleed photograph, and one quiet metadata line above the fold.
- Keep grids editorial: image first, copy second, no decorative containers.
- Use full-bleed or edge-to-edge imagery where possible.
- Favor art direction, public installation photography, gallery shots, contact sheets, performance stills, and studio documentation.

## Do

- Use Bone White as the only page background.
- Set all major headlines at 300 weight.
- Push display type to 64px to 84px when the viewport allows.
- Use 1440px radius only for buttons, menu controls, tags, and pills.
- Keep cards and images sharp at 0px radius.
- Let full-bleed photographs carry most of the emotional weight.
- Use chromatic accents as small fills, borders, single-card highlights, and tags.
- Keep section gaps around 48px to 64px.

## Do Not

- Do not bold headlines.
- Do not use pure white.
- Do not add shadows for elevation.
- Do not round card or image corners.
- Do not use chromatic colors as primary CTA fills.
- Do not let display headlines run beyond two lines.
- Do not allow browser-default link blue into the UI.
