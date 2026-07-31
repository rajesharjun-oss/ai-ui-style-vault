# Layout & Imagery

## Layout

Full-bleed single-screen-per-color layout. The viewport is divided into two horizontal bands: a top header zone (~40% height) containing the massive multi-line display headline spanning full width, a one-line subtitle beneath it, and one hero album cover image; and a content zone below containing a uniform grid of square album cover tiles. No sidebar, no max-width constraint, no centered column - everything is edge-to-edge. The only off-canvas element is a 90 -rotated label pinned to the right edge. Navigation is absent; the user is invited to refresh rather than click. The grid density scales with viewport but tile size stays large - this is a poster, not a feed.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Canvas | `#e4822` | Full-viewport colored field that changes on refresh - the dominant surface |
| 1 | Album Tile | `#ffffff` | Default album cover background within the grid |
| 2 | Dark Album Tile | `#000000` | Dark album cover backgrounds for contrast within the grid |

## Elevation



## Imagery

The site's only imagery is a uniform grid of 1:1 album cover thumbnails. The covers are user-submitted editorial objects - they are the content, not decoration. The grid is unframed, radius-less, and bleeds directly into the canvas color. There is no lifestyle photography, no illustration, no abstract graphics. The colored background functions as the visual atmosphere; the album covers are the products on display. Above the grid, a single magazine-cover-style layout positions the massive headline, subtitle, and one featured album hero - the visual hierarchy is editorial poster, not web page.
