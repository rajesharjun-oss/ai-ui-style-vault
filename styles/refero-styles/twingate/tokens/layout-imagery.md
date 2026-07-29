# Layout & Imagery

## Layout

Full-bleed dark layout with a max content width of ~1200px. The hero is a split composition: large left-aligned headline stack (4 lines, the last accented in chartreuse) with a right-aligned diagram visual. Below the hero, sections are full-width bands with 80px vertical padding and centered or left-aligned content stacks. Feature cards are arranged in a 3-column grid with equal-width columns and ~20px gaps, followed by a customer logo strip. The platform section introduces a 2-column layout (text-left, product-card-right). Testimonials use a responsive grid (3-column at desktop, wrapping on smaller viewports). A floating G2 review widget sits absolutely-positioned at center-screen, overlapping the testimonial grid. The overall rhythm is: bold hero 3-column features logo strip 2-column product testimonial grid. Navigation is a top bar with a persistent utility strip above it.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Void | `#000000` | Page canvas - hero, full-bleed sections, body background |
| 1 | Obsidian | `#0e0f11` | Primary card/panel surface above the page |
| 2 | Carbon | `#141617` | Nested containers, input fields, secondary cards |
| 3 | Graphite | `#1d2023` | Button resting fills, elevated chips, hover surfaces |
| 4 | Slate | `#21223a` | Spotlight/featured surface with violet undertone for hero product cards |

## Elevation

- **Buttons and links:** `inset 0 0 0 0.5px rgba(255, 255, 255, 0.1) - hairline inner highlight, no outer drop shadow`
- **Primary CTA fill:** `inset 0 2.5px 0 -2px rgba(255, 255, 255, 0.1) - subtle top inner highlight giving a subtle beveled-LED appearance`
- **Decorative borders:** `inset 0 2.5px 0 -2px rgba(255, 255, 255, 0.15), inset 0 0 0 0.5px rgba(255, 255, 255, 0.15)`

## Imagery

The site is primarily typographic and diagrammatic rather than photographic. The hero visual is a custom line-art network diagram (concentric circles, lock icons in teal, hexagonal node with gear, laptop) that communicates 'decentralized privileged access' through geometry rather than realism. The only product imagery is a small UI mockup (a dark login card) shown inside a chartreuse-tinted panel as a product showcase. The customer logo strip is monochrome white wordmarks - no lifestyle photography, no human faces outside tiny testimonial avatars. The visual language is instrument-panel/control-room: clean vector geometry, teal circuit accents, and a strict absence of photography. Iconography is consistently line-based with 1-1.5px stroke weights, monocolor (teal or white), and no fill decoration.
