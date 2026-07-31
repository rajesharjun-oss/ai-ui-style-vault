# Layout & Imagery

## Layout

Three-column desktop layout: an ~80px left icon rail (Threads logo, nav icons, compose button, profile avatar), a centered 640px-max-width feed column with 18px radius and subtle elevation, and empty right gutter that breathes out to the viewport edge. The feed is a single vertical scroll - no grid, no masonry, no horizontal carousels. Posts stack linearly with 1px dividers. The top header is a fixed ~53px bar with a centered 'Home' label and right-aligned Log In. Section transitions are seamless: no banding, no alternating backgrounds, no section headers - the feed reads as one continuous document.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Page Canvas | `#fafafa` | Outermost background visible around the feed container and in the sidebar gutters |
| 1 | Backdrop Tint | `#efefef` | The slightly darker plane revealed by the feed container's spread shadow - exists only as shadow artifact, not a painted surface |
| 2 | Feed Column | `#fafafa` | The elevated rounded container that holds all posts; visually identical to the canvas but lifted by the 12px shadow halo and 18px radius |
| 3 | Post Surface | `#fafafa` | Inherited from the feed column - posts are flat, separated only by 1px dividers, never by card backgrounds |

## Elevation

- **Feed Container:** `0 0 12px rgba(0,0,0,0.04), 0 0 0 48px #fafafa`

## Imagery

User-generated content dominates - photographs, screenshots, and video thumbnails appear inside link preview cards and inline media blocks at their natural aspect ratios. No brand illustration, no decorative graphics, no hero imagery. The product itself is the canvas for other people's images. All embedded media sits within 8px-radius containers with no overlay chrome beyond a small site-name attribution line.
