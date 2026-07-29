# Anthropic - Design Reference

> Scientific field journal on warm parchment: quiet ivory surfaces, serif-led editorial voice,
> sans-serif UI chrome, flat paper-stack elevation, and a single clay action accent.

## Theme

Anthropic reads like a curated research publication rather than a conventional tech landing page.
Warm ivory and oat surfaces replace cool-gray SaaS defaults. The serif carries the main voice,
including body text, while the sans-serif handles navigation, buttons, footers, badges, and utility
chrome. Clay appears only when the user must take a decisive action.

The design should feel thoughtful, editorial, calm, and research-oriented. Use surface tone shifts and
hairline borders for hierarchy instead of shadows, glows, gradients, or heavy UI decoration.

## Core Visual Rules

- Use Ivory Medium (`#f0eee6`) as the page canvas.
- Use Ivory Light (`#faf9f5`) for cards and elevated paper surfaces.
- Use Manilla (`#f5e3c7`) only for featured editorial cards.
- Use Clay (`#d97757`) for one consequential filled CTA.
- Use serif at 20px for body copy and editorial paragraphs.
- Use sans-serif at 12px to 16px for UI chrome and navigation.
- Keep inline links persistently underlined.
- Use 24px radius for card-level paper surfaces.
- Use bottom-only radius on filled ivory buttons when matching the signature button style.
- Avoid box shadows; elevation comes from surface tone and 1px borders.

## Quick References

- **Text:** `#141413`
- **Canvas:** `#f0eee6`
- **Card surface:** `#faf9f5`
- **Featured surface:** `#f5e3c7`
- **Deep warm surface:** `#e3dacc`
- **Border:** `#cccbc8`
- **Muted text:** `#b0aea5`
- **Primary action:** `#d97757`
- **Primary action hover:** `#c6613f`
- **Page max width:** `1280px`
- **Section gap:** `80px` to `120px`
- **Card padding:** `24px` to `32px`
- **Element gap:** `8px`
- **Card radius:** `24px`

## Implementation Notes

Start from `code/css-variables.css` or `code/tailwind-v4.css`. Build primitives for text-link buttons,
filled ivory buttons with bottom-only radii, outlined dark buttons, clay filled CTAs, featured hero
cards, release cards, editorial hero heading blocks, inline underlined links, transparent badges, cookie
consent bars, skip links, and dark footer link grids.

For original work, keep the system logic but replace source-specific brand marks, illustrations, names,
copy, and exact compositions.

