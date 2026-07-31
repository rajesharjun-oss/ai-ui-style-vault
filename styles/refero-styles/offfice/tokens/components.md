# Components

### Top Navigation Bar
**Role:** Minimal two-anchor header - brand mark left, contact CTA right

Full-bleed, no background fill, sits directly on Onyx canvas. Left: 'offfice studio' in ak 12px weight 400, Paper White. Right: 'GET IN TOUCH' in ak 12px weight 700, Paper White. No border, no shadow, no hamburger menu. Padding: 16px from viewport edges.

### Display Headline Block
**Role:** Hero-scale typographic wall that defines the first viewport

ak weight 400 at 216px, line-height 0.80, Paper White. Text deliberately overflows viewport edges - 'OFFICE FOR' bleeds off the right, 'FUTURE' bleeds off the left. No max-width constraint. The tight leading stacks glyphs into a slab that reads as a graphic shape, not a sentence. This is the signature element.

### Product Sculpture (3D Hero Object)
**Role:** Centered product showcase - the only non-text element on the canvas

A single dark-toned 3D render of furniture, positioned in the viewport center. Renders in the same tonal range as the Onyx background (near-black) with subtle specular highlights from form, not from a light effect. No background, no platform, no shadow - it floats in the void. In scroll sequences, it overlaps archive list text to create a z-axis depth effect.

### Description Caption
**Role:** Small editorial body text adjacent to the product showcase

ak 12px weight 400, line-height 1.56, Paper White, all-caps tracking. Text reads: 'FUTURE LIVING DESIGN RESEARCH STUDIO. INSTALLATIONS, COMMERCIAL AND PRIVATE SPACES.' No paragraph break, no emphasis - flat, informational, gallery-wall-label tone.

### Locale Switcher
**Role:** Three-letter language selector

ak 12px weight 400, Paper White, positioned at the far right below the nav. Format: 'IT / ES / CH' separated by spaces and forward slashes. No active-state styling difference - all three are the same weight and color, implying availability not state.

### Archive Project Entry
**Role:** Single row in the project archive list

Four-column horizontal layout: project title in gs 72px serif weight 400 (Paper White) on the left, year in ak 12px weight 400, category labels ('PROJECT DETAILS', 'Armchair', 'Interior') in ak 12px weight 400 spaced across the row. Entries are separated by 32px vertical gap. The serif title and sans metadata create a deliberate type-mixing effect within a single row.

### Archive List (Full)
**Role:** Vertically stacked project archive - the index page in list form

Six to eight Archive Project Entries stacked vertically with 32px gaps. No section header, no dividers, no cards. The list occupies the full viewport width. Product 3D renders float over the list on scroll, creating parallax overlap without explicit z-index manipulation beyond natural stacking.

### Section Label (Inline)
**Role:** Minimal in-content metadata markers

ak 12px weight 400, Paper White, used for 'US / WW' region codes, 'Archive' contextual labels, and other micro-annotations. No background, no badge shape, no padding - text only, relying on position and size for hierarchy.
