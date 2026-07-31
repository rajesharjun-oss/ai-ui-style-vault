# Components

### Grid Canvas
**Role:** Structural background

White (#ffffff) page with visible thin gray grid lines forming a modular lattice. Grid cells define all content placement. The grid is the layout - there is no separate container system.

### Color Block Panel
**Role:** Large chromatic content surface

Full-bleed flat color rectangle snapped to grid cells. Background fills with a single brand palette color (Tangerine #ff8c19, Sky Cyan #3dd3ee, Dropbox Blue #0061fe, Sun Yellow #fad24b, etc.). 8px border-radius. Contains white reverse-type text or sits empty as visual punctuation. No border, no shadow.

### Editorial Headline Block
**Role:** Primary heading display

Bold type in Dbsharpgroteskvariable Vf at 30-36px, weight 700, color Dropbox Blue (#0061fe), letter-spacing -0.02em. Left-aligned within a white grid cell. No decorative elements - the grid lines frame the type.

### Inverted Text Panel
**Role:** White text on color

White (#ffffff) body text in Atlasgrotesk Web 14px, line-height 1.67, placed inside a Color Block Panel. Creates a color/text duality where the panel is both a color swatch and a readable surface.

### Hairline Divider
**Role:** Structural separator

1px line in Ink (#1e1919). Used to define grid cell boundaries, section separations, and content edges. The dominant border treatment - appears with freq=300 in border contexts.

### Text Link
**Role:** Inline navigation

Atlasgrotesk Web 14px weight 500, color Dropbox Blue (#0061fe). Often with a 1px bottom border in the same color. The 8px border-radius applies to link containers if wrapped in a button-like element.

### Outlined Action
**Role:** Primary call-to-action border

Ghost/outlined button: transparent background, 1px border in Dropbox Blue (#0061fe), text in Dropbox Blue. 8px border-radius, 12-16px padding. This is the only CTA pattern - the system never uses filled buttons.

### Nav Label
**Role:** Navigation text

Atlasgrotesk Web 12px, weight 500, color Ink (#1e1919). Sits within 8px vertical and 14px horizontal padding containers. Compact, utility-scale type.

### Brand Mark
**Role:** Logo/identity anchor

The Dropbox glyph in Dropbox Blue (#0061fe) - the four-triangle box mark. Appears at the bottom-left of the grid as a constant identity anchor.

### Chevron Scroll Indicator
**Role:** Scroll affordance

Down-chevron icon in Atlasgrotesk Web or as an SVG stroke, positioned at the bottom-right of the grid. Single visual cue that more content exists below.

### Color Swatch Cell
**Role:** Brand palette documentation

Small rectangular fill in one of the ten brand palette colors (Sun Yellow, Lime, Tangerine, Sky Cyan, Coral, Lavender, Magenta, Slate Navy, Dropbox Blue, Dropbox Light). Functions both as documentation of the palette and as inline color samples within grid cells.
