# Jitter Style Reference

## North Star

Jitter reads as a kinetic playground rendered with Swiss-design precision. It should feel playful because the cards float, colors spark, and animation previews carry the experience. It should feel premium because the type is tight, the accents are scarce, and every radius and shadow has a strong rule.

The base is a soft off-white studio canvas. White preview cards hover above it with deep diffuse shadows. A near-black Ink neutral carries most text, while violet is reserved for one hero CTA or a small number of brand highlights.

## Color

The palette is light, neutral, and chromatically scarce.

- `Studio Off-White` `#f2f1f3`: page canvas and recessed section backgrounds.
- `Pure White` `#ffffff`: card surfaces, elevated panels, preview tiles, and text on dark fills.
- `Hairline Gray` `#e5e4e7`: subtle borders, divider lines, muted card backgrounds.
- `Soft Mist` `#97979b`: muted secondary text and placeholder labels.
- `Slate` `#6e6e73`: body copy in card contexts and secondary descriptive text.
- `Ink` `#19171c`: primary text, nav links, dark buttons, footer text, and high-contrast blocks.
- `Pure Black` `#000000`: icon fills or maximum-contrast surfaces only; avoid as the primary system text.
- `Eclipse Violet` `#7a40ed`: the singular hero CTA and rare brand-forward emphasis.
- `Deep Plum` `#17082c`: dark violet heading warmth and text on pale violet tags.
- `Lilac Wash` `#a981ff`: violet decorative accent and highlighted labels.
- `Lavender Mist` `#cab3f8`: pill badge and soft violet highlight washes.
- `Electric Blue` `#00b2ff`: animated highlight rings, icon accents, and card border highlights.
- `Sky Tint` `#e6f4ff`: cool blue-tinted card backgrounds and soft washes.
- `Ice Blue` `#a9dbff`: decorative fills in illustrations and animated graphics.
- `Volt` `#f5ff63`: electric yellow-green tag/status accent, used sparingly.

Limit accent use. One violet CTA per view is enough. Blue and Volt should appear as tags, animation details, status-like marks, or tiny highlights rather than broad UI fills.

## Typography

Use a split type system:

- Display/headings: `TWK Lausanne`, with Inter Tight, Switzer, or General Sans fallback.
- Body/UI: `Inter`, already broadly available.

TWK Lausanne owns everything from large section headings up to enormous hero type. It uses high weights and tight tracking, with compressed line heights at display sizes.

Inter owns nav, buttons, body copy, card descriptions, badges, forms, and medium-sized content.

Recommended roles:

- UI label: 12px to 14px, Inter, weight 500, tracking 0.
- Body: 15px to 18px, Inter, weight 400 to 500, line-height 1.4 to 1.6, modest negative tracking from 15px up.
- Body subhead: 26px, Inter, weight 600 to 800.
- Section heading: 40px to 48px, TWK Lausanne, weight 700 to 800, tracking around -0.03em.
- Hero heading: 80px, TWK Lausanne, weight 750 or 800, line-height 0.95, tracking -0.032em.
- Monumental display: up to 200px, TWK Lausanne, line-height 0.85, tracking -0.044em.

Do not use Inter for display type above 26px. Jitter's display voice comes from TWK Lausanne.

## Layout

The page is a vertical stack of horizontal bands on Studio Off-White:

- Sticky top navigation.
- Centered hero stack with badge, headline, CTA, and logo cloud.
- Two-column feature sections with text plus animation preview card.
- Horizontal-scrolling rows of template or animation cards.
- Large whitespace between sections, usually 80px to 120px.

Use a centered max width around 1200px. Avoid sidebars and dense dashboard rails. The hero is typographic rather than image-led; visual richness builds as preview cards appear lower on the page.

## Shape And Elevation

The rounded geometry is the signature:

- Buttons: 50px radius.
- Cards and preview tiles: 40px radius.
- Badges and tags: 40px radius.
- Dark inputs: 26px radius.
- Circular menu button: fully round.

Avoid radii below 20px. The system is pillow-like and capsule-shaped.

Elevation is dramatic but soft. Use the four-layer diffuse stack for preview cards:

```css
0 152px 61px rgba(25, 23, 28, 0.01),
0 85px 51px rgba(25, 23, 28, 0.05),
0 38px 38px rgba(25, 23, 28, 0.09),
0 9px 21px rgba(25, 23, 28, 0.10)
```

Do not use hard-edged, single-layer shadows.

## Components

### Navigation Header

White background, sticky, about 64px tall. Use Ink logo and nav links, 14px to 16px Inter 500. Include a ghost login link and a dark filled pill CTA on the right.

### Dark Filled Pill Button

Ink fill, Pure White text, 50px radius, 14px to 16px Inter 500 to 600, 20px to 24px horizontal padding. Use for navigation and overlay CTAs.

### Violet Filled Pill Button

Eclipse Violet fill, Pure White text, 50px radius, 16px Inter 600, 16px 32px padding. Use as the singular hero CTA.

### Pill Badge Or Tag

40px radius, compact padding, 12px to 14px Inter 500. Use Lavender Mist, Volt, or Lilac Wash backgrounds. Place one badge above section headings, never a stack of badges.

### Animation Preview Card

Pure White fill, 40px radius, edge-to-edge media, no internal padding, and the four-layer diffuse shadow. This is the primary showcase object.

### Logo Cloud Strip

Centered social proof row on Studio Off-White. Use Slate intro text and Ink logos. Keep spacing even and avoid separators.

### Hero Section

Centered typographic hero with one badge, large TWK Lausanne headline, one violet CTA, and logo cloud. Do not add a hero image.

### Two-Column Feature Section

Alternate text/media order. Use 40px to 48px TWK Lausanne heading on one side and an Animation Preview Card on the other.

### Template Card Grid

Horizontal scrolling row of rounded preview cards, usually 4 to 5 visible on desktop. A dark pill CTA can float above or over the row.

### Dark Input Field

Dark plum fill, white text, 26px radius, 14px to 16px Inter, and soft muted placeholder.

## Imagery

Use animation software screenshots, template previews, motion artifacts, timeline/video frames, colorful tags, and UI mockups. Avoid generic illustration-first hero pages, stock photography, or dashboard-heavy enterprise pages.

## Do

- Use Studio Off-White as the canvas.
- Use a single Eclipse Violet CTA in the hero.
- Use Ink for body text, nav links, and dark nav CTAs.
- Use 50px button radius and 40px card/badge radius.
- Use TWK Lausanne for large display type.
- Use Inter for body/UI.
- Use the diffuse four-layer shadow stack on elevated preview cards.
- Keep accent color sparse.

## Do Not

- Do not use sharp corners or radii below 20px.
- Do not put the violet CTA in the navigation bar.
- Do not use pure black as the default text or button fill.
- Do not use hard, single-layer shadows.
- Do not use Volt on dark backgrounds without dark text.
- Do not set display type above 26px in Inter.
- Do not add extra chromatic accents beyond violet, blue, and Volt.
