# Layout & Imagery

## Layout

The page uses a two-column layout: a fixed left sidebar (~340px) for 'Your Library' and navigation, and a flexible main content area that scrolls independently. The main area is organized as vertically stacked horizontal rails - each rail is a section heading (24px left-aligned, 'Show all' right-aligned) followed by a horizontally scrolling row of cards. Cards are uniform-width within each rail (albums: 180px squares, artists: 180px circles). Spacing between rails is 32px; between cards within a rail is 16px. The top bar is a full-width navigation strip with left-cluster icons/search and right-cluster text links and action buttons. A full-width gradient premium banner is sticky at the bottom of the viewport. There are no section dividers, background color changes, or visual separators between rails - the surface stays uniformly #000000, and hierarchy comes from typography and spacing alone.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Void Canvas | `#000000` | Page background, left sidebar, footer areas |
| 1 | Obsidian Card | `#121212` | Album cards, playlist prompt cards, content surfaces |
| 2 | Graphite Control | `#1f1f1f` | Search bar, elevated buttons, hover states |

## Elevation

- **Album / Playlist Card:** `0px 8px 24px 0px rgba(0, 0, 0, 0.5)`

## Imagery

Imagery IS the product. The interface is a frame for user-consumed content: square album covers, circular artist portraits, and playlist cover art. Treatment is clean, uncropped (except to square or circle), no filters or overlays on content imagery. Card shadows (0px 8px 24px rgba(0,0,0,0.5)) give artwork dimensional lift off the void canvas. No illustrations, no abstract graphics, no lifestyle photography in the UI itself - the page is a gallery. Icons are minimal, monochromatic, and outlined or filled in white at reduced opacity. The only branded graphic element is the gradient premium banner.
