# Components

### Sparse Top Navigation
**Role:** Primary site navigation

Three text links absolutely positioned across the top edge: brand mark at far left, primary nav item in the center-left, and a secondary link at far right. Uses Alpha at 16px / weight 400, color #000000, sitting on the bare #ffffff canvas with no background, no border, no padding. The nav occupies less than 2% of the viewport vertically - deliberately negligible so the hero geometry dominates.

### Geometric Ring Hero
**Role:** Brand-defining visual composition

Two massive black ring/donut forms rendered in #000000 fill, each approximately 60-70% of viewport height in diameter, with stroke width roughly 25-30% of the outer radius. The inner counter reveals #ffffff. Positioned to dominate the full viewport width, with the rings partially cropped at the page edges. No border-radius because the geometry is already circular - the shape IS the radius. This component is the brand identity rendered at architectural scale.

### Display Headline Block
**Role:** Primary text statement on hero

Alpha font at 60px / weight 400 / lineHeight 1.00, color #000000. The tight lineHeight makes multi-line headlines stack as a solid rectangular mass rather than airy text. No letter-spacing manipulation - sits at default tracking. Positioned with generous margin (139-208px from viewport edges) to feel placed rather than centered.

### Subhead Text Block
**Role:** Secondary descriptive copy

Takt font at 36px / weight 400 / lineHeight 1.11, color #000000. Runs as stacked paragraph blocks under display headlines. The tight 1.11 lineHeight creates a dense editorial column. Left-aligned with no decorative treatment - the type itself is the visual element.

### Hairline Divider
**Role:** Structural section separator

1px solid #e5e7eb rule spanning the full content width or the full viewport. The only use of the gray tone in the system. No padding, no margin above/below except to define section rhythm. Functions as the only architectural detail in an otherwise bare composition.

### Text-Link Nav Item
**Role:** Inline navigation element

Alpha or Takt at 16px / weight 400, color #000000, no underline, no background, no padding. Inline with surrounding text or spaced across the top bar. Hover state is the only interactive feedback and it should stay minimal - a subtle color shift or underline appearance, never a fill or transform.

### Body Paragraph
**Role:** Long-form descriptive text

Takt at 16px / weight 400 / lineHeight 1.50, color #000000. Runs in single-column blocks with no max-width constraint beyond the content flow. Generous paragraph spacing (32px column-gap) between blocks. The 1.50 lineHeight on Takt is the most relaxed setting in the type system, creating readable editorial rhythm.

### Image Placeholder Counter
**Role:** Visual break / negative space element

The white inner circle of a ring form, or a standalone white circular cutout within a black field. Functions as a 'hole' in the composition that draws the eye and gives the black geometry its meaning. Pure #ffffff - no border, no shadow, no texture.
