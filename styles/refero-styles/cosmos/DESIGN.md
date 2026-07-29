# Cosmos Style Reference

## Creative Direction

Create a warm, flat, image-first gallery interface. The page should feel like curated photographs and clippings arranged on a linen wall. The product chrome must stay quiet: black ink text, white paper surfaces, subtle gray text, low-opacity black borders, and no decorative interface color.

## Visual Priorities

1. Use `#f7f5f3` as the root page background.
2. Use `#0d0d0d` instead of pure black for text and filled controls.
3. Use `#ffffff` only for cards, inputs, buttons, and light elevated surfaces.
4. Let images carry the color.
5. Use one main radius: 16px for cards, buttons, inputs, and video.
6. Use 12px radius only for small floating image tiles.
7. Avoid shadows on normal UI surfaces.
8. Use editorial serif typography at low weights with tight tracking.

## Screen Composition

Use a floating pill navigation bar at the top, then a centered hero stack surrounded by scattered image tiles. The page should continue into a wide video or media block, then a strict 3-column image-led feature grid. Keep the page max width around 1280px and give sections breathing room with 80px spacing.

## Material Language

The system is intentionally flat. Depth comes from surface contrast and the physical feeling of image tiles on a canvas, not from UI shadows. Buttons, cards, inputs, and media containers share 16px rounding and simple border logic. The product should feel restrained, editorial, and gallery-like.

## AI Implementation Notes

When generating a UI from this style, build image-led components first: floating tiles, gallery cards, video/media blocks, saved collections, and visual search. Do not turn it into a dashboard, table, analytics screen, or colorful SaaS landing page. The rule is simple: if it is not navigation, input, or a button, it should probably be an image card or media object.

