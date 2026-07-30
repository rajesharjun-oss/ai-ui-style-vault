# Layout & Imagery

## Layout

The page model is max-width contained (1280px) with full-bleed sectional bands. The hero is a full-viewport-height dark or white panel with a left-aligned display headline (48-92px) and an image collage on the right, anchored by a filled primary button. Below the hero, content flows in alternating white and Bone Warm (#f6f2eb) bands, each with 80px vertical section padding. Feature offerings appear in a 4-column card grid (each card is image-top, text-bottom) on white. A single dark Obsidian (#212121) feature band appears mid-page for contrast punctuation, then returns to white. Spacing is generous and editorial - sections breathe with 80px gaps, never crammed. Navigation is a sticky 64px top bar with left logo, center pill nav links, and right-side language switcher + ghost login + filled CTA. Grid is rigid 4-column at desktop, collapsing to 2-column on tablet and single-column on mobile.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Paper White | `#ffffff` | Base canvas for the majority of the page - all content sections, card backgrounds, and form surfaces. |
| 1 | Ash Mist | `#f5f5f5` | Input fields and inset wells - slight cool lift from the paper canvas to indicate interactivity. |
| 2 | Bone Warm | `#f6f2eb` | Sectional warm wash - used between content bands to create editorial pacing and break monochrome fatigue. |
| 3 | Obsidian | `#212121` | Dark surface block - hero panels, navigation, filled actions. The only dark surface tier in the light theme. |
| 4 | Pure Black | `#000000` | Reserved for maximum-contrast accent moments - not a background tier, only for type and strokes. |

## Elevation

The system deliberately avoids drop shadows and elevation effects. The only 'shadow' pattern detected is a 1px inset border on links (rgb(0,0,0) 0px 0px 0px 1px inset) - used to create a subtle inner line that mimics a printed underline. Separation between elements is achieved through hairline 1px borders in #666666, generous whitespace, and the occasional warm Bone Wash (#f6f2eb) section background. This flat-by-design approach reinforces the editorial, print-catalog feel - surfaces should feel like pages laid on a table, not cards floating in a digital space.

## Imagery

Photography is the sole source of color in an otherwise achromatic system. WGSN uses tightly cropped, high-quality editorial product and lifestyle photography - fashion, food, materials, interiors - treated with natural color and studio lighting (no duotone or desaturation filters). Images are always presented in 16px-rounded containers, never full-bleed, and frequently composed as multi-image collages with 12-16px gaps and gentle overlaps. Iconography is monochrome line-based, drawn in #333333 or #212121 at consistent 1.5-2px stroke weight. No illustrations, no 3D renders, no abstract graphics - the photography does all the decorative work, and the UI frames it like a museum wall.
