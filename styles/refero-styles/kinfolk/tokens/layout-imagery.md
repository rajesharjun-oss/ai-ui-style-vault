# Layout & Imagery

## Layout

The site is a max-width ~1400px centred canvas on #ffffff, with full-bleed editorial sections that break out to 100vw. The first screen is a centred, vertically-stacked composition (wordmark top-left / hamburger top-right / centred issue title / centred cover image) - quiet and symmetrical. Below that, full-bleed photo sections alternate with white-space article grids, creating a print-magazine reading rhythm. The article grid is a 5-column equal-width row at desktop, collapsing to fewer columns on smaller breakpoints. Text is almost always left-aligned within cards and centred for hero/feature moments. The only persistent UI chrome is the 64px top header and the ~48px black footer bar; between them the page reads as uninterrupted editorial.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 1 | Canvas | `#ffffff` | Base page background and majority of editorial card surfaces |
| 2 | Inset Mist | `#f4f4f4` | Subtle elevation for form fields, secondary content blocks, and gentle band separation |
| 3 | Sage Band | `#dbded5` | Full-bleed paper-tint section that reads as a magazine spread break rather than a colored block |

## Elevation

Philosophy

This system deliberately avoids box-shadows and fill-based elevation. Hierarchy is established through: (1) the contrast of full-bleed photography against bone-white canvas, (2) the sage paper band (#dbded5) as a step-down surface for section breaks, and (3) typographic scale alone - no card needs to lift off the page because nothing on the page is pretending to be a windowed UI. The only border treatment is the 1px hairline, used on text links and the subscribe CTA. A designer who needs to add a shadow should first ask whether the element belongs in a different surface layer.

## Imagery

Full-bleed editorial photography is the dominant visual asset: lifestyle, interiors, fashion, and art-direction imagery shot in muted, naturalistic palettes with a slightly desaturated, film-like quality. Photos are presented edge-to-edge (0px radius, no borders, no overlays) and act as the background for overlaid white serif type. The magazine cover and article-grid thumbnails use tight vertical and square crops. There are no illustrations, no abstract graphics, and no iconography beyond a single hamburger glyph; icons are absent because the serif type and the photography carry all semantic weight. Image density is high but never decorative - every photograph serves a story, never an empty card.
