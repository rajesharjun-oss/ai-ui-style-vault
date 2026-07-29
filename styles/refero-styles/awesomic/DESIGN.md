# Awesomic - Design Reference

> Editorial zinc marketplace grid with dark CTAs, compact neutral typography, generous rounded cards,
> hairline borders, image-led category cards, and one orange credential accent.

## Theme

Awesomic is a neutral-first marketplace style. A zinc-gray palette carries nearly the whole interface,
while one vivid orange accent appears only as badge punctuation for startup credentials or category
emphasis. The system feels efficient, confident, and infrastructure-grade: compact text, precise spacing,
large rounded content surfaces, and minimal chromatic noise.

Typography uses a single geometric sans family across every role. Display headlines are bold and editorial,
while body and UI text stay compact and practical.

## Core Visual Rules

- Use the zinc neutral scale as the main palette.
- Use Obsidian (`#09090b`) for primary dark CTAs and dominant display text.
- Use Ember (`#ff5a00`) only for small credential or category badges.
- Keep display headings at weight 600 or higher.
- Keep body text around 14px to 15px in a Cosmica-like geometric sans.
- Use 36px radius for cards and 14px radius for buttons/inputs.
- Use 1px Cloud (`#ececee`) borders instead of drop shadows for cards.
- Use real imagery in category cards and full-width image divider sections.

## Quick References

- **Canvas:** `#f4f4f5`
- **Card surface:** `#ffffff`
- **Subtle card:** `#fafafa`
- **Primary text:** `#09090b`
- **Body text:** `#18181b`
- **Muted text:** `#52525b`
- **Border:** `#ececee`
- **Orange accent:** `#ff5a00`
- **Rare decorative accent:** `#fe45e2`
- **Page max width:** `1200px`
- **Section gap:** `80px`
- **Card padding:** `28px`
- **Element gap:** `8px`
- **Card radius:** `36px`
- **Button/input radius:** `14px`
- **Badge radius:** `12px`

## Implementation Notes

Start from `code/css-variables.css` or `code/tailwind-v4.css`. Build primitives for primary dark CTAs,
white ghost actions, light neutral buttons, category image cards, dark feature cards, tag badges, orange
accent badges, email inputs, logo strips, stat blocks, full-width image dividers, and sticky navigation.

For original work, keep the system logic but replace source-specific brand marks, screenshots, names,
copy, photographs, and exact compositions.

