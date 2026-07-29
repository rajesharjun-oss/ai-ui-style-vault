# Dock Style Reference

## North Star

Dock feels like a sunlit cream paper workspace with a single cobalt pulse. The system is warm, quiet, and product-led. It should feel like a polished B2B workspace, not a loud marketing page.

The canvas is soft cream. Product screenshots sit inside ivory cards with large rounded corners, fine beige borders, and feather-light shadows. Cobalt appears only when something is actionable or active.

## Color

The palette is warm neutral plus one decisive blue:

- `Velvet Ink` `#16042c`: primary text, headings, footer text, and high-contrast UI.
- `Paper Cream` `#fcf8ed`: page-level canvas.
- `Ivory Card` `#fffdf8`: primary card surfaces, product mockup frames, and content panels.
- `Hairline Beige` `#e8dcc8`: card borders, dividers, and soft separators.
- `Warm Gray` `#776f64`: secondary text and descriptions.
- `Soft Tan` `#c9bda6`: tertiary labels, placeholder text, and quiet metadata.
- `Electric Cobalt` `#385bff`: primary CTA, active links, focus rings, and selected states.
- `Cobalt Hover` `#2748e8`: hover and active state for cobalt actions.
- `Dark Cobalt` `#1530b8`: deeper blue states and high-contrast active details.
- `Pale Blue` `#eef2ff`: blue-tinted hover backgrounds and subtle active surfaces.
- `Morning Mist` `#f6f0e4`: alternate cream section bands and nested panels.
- `Pure White` `#ffffff`: button text on cobalt and screenshot interiors.

Do not introduce a second accent color. Cobalt is the only strong chromatic signal.

## Typography

Use Roobert as the main brand typeface, falling back to Inter or Plus Jakarta Sans. Product Sans or Google Sans can support navigation, buttons, and form labels, with Inter fallback.

Roobert guidance:

- Body: 16px, 400, line-height 1.5.
- Small UI: 14px to 16px, 500 to 600.
- Card heading: 22px, 600, line-height 1.3.
- Section heading: 36px to 48px, 700 to 800, negative tracking.
- Hero heading: 64px, 800, line-height around 1.05, letter-spacing about -0.04em.

Use generous but not theatrical type. Headings can be confident, but the product should still feel approachable.

## Layout

Use a centered max width around 1280px. The main landing pattern is:

- Sticky cream header with a thin bottom border.
- Two-column hero on desktop: text and CTA on the left, product screenshot stack on the right.
- Alternating section bands using Paper Cream and Morning Mist.
- 96px to 128px vertical padding between major sections.
- Three-column feature grids on desktop.
- Centered CTA bands with a cobalt pill action.

Avoid sidebars, dense control rails, and heavily framed dashboard layouts on the first screen.

## Shape And Elevation

Dock uses friendly rounded surfaces:

- Buttons: 9999px pill.
- Tags: 9999px pill.
- Cards: 24px.
- Product screenshots: 18px.
- Inputs: 12px.

Elevation is soft and sparse. Use shadows mainly for product screenshot cards:

```css
0 24px 64px rgba(22, 4, 44, 0.08),
0 8px 24px rgba(22, 4, 44, 0.06)
```

Feature cards can hover with:

```css
0 12px 32px rgba(22, 4, 44, 0.06)
```

Do not use heavy dark shadows or glassy depth.

## Components

### Header Navigation

Cream background, about 72px tall, 1px Hairline Beige bottom border. Use Velvet Ink logo, Warm Gray nav links, and cobalt hover. Place a ghost sign-in link and a cobalt pill CTA on the right.

### Primary Cobalt Pill Button

Electric Cobalt fill, Pure White text, 9999px radius, 14px to 16px type, 14px 24px padding. Hover uses Cobalt Hover. Use one primary CTA per section.

### Secondary Outline Pill

Transparent or cream fill, Hairline Beige border, Velvet Ink text, 9999px radius. Hover can use Pale Blue and a cobalt border.

### Product Screenshot Card

Ivory Card surface, 24px radius, 1px Hairline Beige border, 12px to 16px padding, and soft screenshot shadow. Inner screenshot can use 12px to 18px radius.

### Feature Card

Ivory Card background, 24px radius, Hairline Beige border, 32px padding, 22px/600 heading, 16px Warm Gray body copy, optional cobalt icon.

### Testimonial Quote Card

Morning Mist or Ivory Card background, 24px radius, Roobert quote text around 24px to 36px, avatar/attribution row, and subtle border.

### Pill Tag

Pale Blue background, Electric Cobalt text, 9999px radius, 14px/500, 6px 12px padding. Use for category labels and small product tags.

### Input Field

Ivory or Pure White fill, 1px Hairline Beige border, 12px radius, 16px text, and cobalt focus outline.

### Logo Cloud

Muted Warm Gray logos or text, 48px to 64px gaps, no dividers.

## Imagery

Use real product screenshots, interface mockups, client portal previews, document/workspace cards, and clean UI composites. Do not use generic stock photography as a hero. Do not use decorative illustration when product screenshots can explain the value.

## Do

- Use Paper Cream as the dominant canvas.
- Use Ivory Card for product surfaces.
- Use Electric Cobalt for the primary CTA and active states.
- Use Roobert for headings and body.
- Use pill buttons and rounded cards.
- Use real product screenshots as the visual anchor.
- Keep section rhythm generous.

## Do Not

- Do not use pure white as the page canvas.
- Do not introduce a second accent color.
- Do not use sharp cards or square CTAs.
- Do not apply cobalt as a full section background.
- Do not use heavy dark shadows.
- Do not rely on generic illustrations when product UI is available.
