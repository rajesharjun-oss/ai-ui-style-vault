# shadcn/ui Design Notes

The shadcn/ui style is a compact monochrome component system. It feels more like a workshop than a marketing site: dense but breathable, quiet but exact. It uses a mostly black, white, and zinc-gray palette, with red reserved for destructive and error states.

## Visual Principles

- Let structure do the work: borders, spacing, radius, and type hierarchy carry the interface.
- Use white as the main page and card surface.
- Use gray surfaces for recessed areas, disabled controls, and frosted panels.
- Use color only when the state demands it.
- Keep typography compact and legible.
- Favor composable primitives over custom decorative sections.

## Color System

The palette is almost monochrome. Canvas, cards, panels, borders, text, and muted text come from the zinc-gray family. Red exists, but it is not a brand accent for regular decoration. Use it for destructive buttons, error text, and danger borders.

## Typography

Geist Sans is the main system voice. Body, labels, tabs, nav, and headings all use the same family. Geist Mono is strictly for code, keyboard shortcuts, token labels, and command-like technical text.

Display scale is restrained. The largest text is around 48px, and most UI lives between 12px and 16px.

## Layout

Use contained layouts around `1200px` to `1400px`. Common patterns include docs sidebars, command-palette panels, dashboard cards, two-column settings screens, and component preview grids.

## Elevation

Normal cards use `1px #e4e4e7` borders and no shadow. Use a very small shadow only for overlays, popovers, command palettes, and modal-like surfaces.
