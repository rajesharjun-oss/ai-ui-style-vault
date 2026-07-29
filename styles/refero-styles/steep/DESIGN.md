# Steep - Design Reference

> Editorial analytics on warm paper: serif headlines, quiet white surfaces, soft product cards,
> pill controls, and one rare peach accent for emphasis.

## Theme

Steep turns analytics into a product magazine spread. The visual system is mostly white and achromatic,
with near-black typography, soft gray utility surfaces, and a single warm peach/brown accent pair. Product
UI fragments float around the headline as editorial artifacts rather than living inside a dense dashboard.

The design should feel calm, intelligent, spacious, and premium. Use large serif display type for editorial
authority and a precise sans for product UI, nav, buttons, labels, and body copy.

## Core Visual Rules

- Use a white paper canvas as the dominant surface.
- Use Signifier-style serif display type at 44px, 64px, and 90px.
- Keep the serif at weight 400; do not bold it.
- Use Sohne-style sans for body, navigation, cards, buttons, and metadata.
- Use peach/brown sparingly, usually one editorial accent card per page.
- Pair filled dark pill CTAs with ghost pill secondary actions.
- Let product UI artifacts float with subtle shadow; keep content cards flat.
- Avoid extra chromatic accents such as blue, green, or purple.

## Quick References

- **Text:** `#17191c`
- **Canvas:** `#ffffff`
- **Muted text:** `#777b86`
- **Card mist:** `#f2f2f3`
- **Section fog:** `#fafafb`
- **Peach accent:** `#fbe1d1`
- **Brown accent ink:** `#5d2a1a`
- **Page max width:** `1200px`
- **Section gap:** `80px`
- **Card padding:** `20px`
- **Element gap:** `8px`
- **Button radius:** `9999px`
- **Card radius:** `24px`
- **Product artifact radius:** `20px`

## Implementation Notes

Start from `code/css-variables.css` or `code/tailwind-v4.css`. Build primitives for filled and ghost
pill buttons, editorial text links, neutral cards, rare peach accent cards, floating product artifacts,
AI composer inputs, stat cards, avatar bubbles, and quiet typographic tags.

For original work, keep the system logic but replace source-specific brand marks, screenshots, names,
copy, data, and exact compositions.

