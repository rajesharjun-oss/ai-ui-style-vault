# Layout & Imagery

## Layout

Centered, max-width-1200px contained layout with full-bleed photographic sections breaking the container. The page rhythm is: minimal top nav centered hero with oversized headline monochrome logo strip centered product section header (Sana Learn) on a Linen band with a 4-column feature row below full-bleed editorial product showcase full-bleed testimonial with overlaid quote footer. Hero is a single centered headline with no hero image. Section transitions alternate between white and Linen #efefed bands rather than using dividers. Feature grids use 4 equal columns at 24-40px gaps. The entire layout breathes: vertical section gaps of 80-120px and generous internal padding give it the feel of a printed document rather than a dashboard.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Canvas | `#ffffff` | Primary page background - the default reading surface |
| 1 | Band | `#efefed` | Section background that breaks the page into rhythmic alternating bands without using color or shadows |
| 2 | Card | `#ffffff` | Card surface on Linen bands - white-on-warm-white creates the only soft elevation in the system |

## Elevation

The system intentionally avoids shadows entirely. Depth is achieved through surface color shifts (#ffffff on #efefed) and through photography, not through drop shadows. This keeps the visual language feeling like printed editorial design rather than software UI. Never add box-shadow to components.

## Imagery

Photography is the only chromatic element in the system and is treated as editorial content, not decoration. Two dominant types: (1) editorial product still-lifes - laptops, notebooks, coffee cups, and office objects arranged in tactile compositions on neutral surfaces, used to present product screenshots within a real-world context; (2) full-bleed portrait photography for testimonials, warm-toned and slightly underexposed, with the subject's face partially in shadow. Both styles are desaturated, warm, and unglamorous - they feel like magazine photography, not marketing photography. Product UI itself is shown only as a screenshot inside the editorial photography, never as a floating mockup with shadow. The only other visual element is a small set of monochrome line icons (24px, Ink stroke) used sparingly for feature labels.
