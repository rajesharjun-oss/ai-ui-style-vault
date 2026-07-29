# Components

### Project Tile Card
**Role:** Container for a single showcase image (phone mockup) with label and navigation arrow

White paper surface, 8px radius, no border, 16px internal padding. A pill label sits top-left at 40px corner radius with 1px Ink border, 10px vertical / 8px horizontal padding, Inter 12px. A 32px circular arrow button with 1px Ink border sits top-right. Caption text (Inter 12px Graphite) sits centered beneath the card with 8px gap.

### Pill Label
**Role:** Project category tag overlaid on each card

Fully rounded capsule (40px radius) on white paper. 1px Ink border, 6px padding top/bottom, 8px padding left/right. Text: Inter 12px, color Ink, letter-spacing -0.0170em.

### Arrow Navigation Button
**Role:** Compact circular control to open a project

32px circle, white fill, 1px Ink border, centered right-pointing arrow icon at 16px radius geometry. No shadow, no fill state - the border is the only affordance.

### Header Bar
**Role:** Top-of-page identity, nav, and social link strip

Full-bleed white band with 16px padding. Four text columns separated by generous white space: name+role (left), showreel link (center-left), social links (center-right), index+about (right). All Inter 12px, Ink, letter-spacing -0.0170em. No dividers between columns - whitespace carries the rhythm.

### Intro Block
**Role:** Two-column intro: contact email on the left, welcome paragraph on the right

40px row gap between the email and the welcome copy. Email is Inter 12px Ink; the welcome paragraph is Inter 24px Graphite at line-height 1.23 - this is the largest type in the system, used exactly once.

### Project Grid
**Role:** Responsive grid of project tiles filling the rest of the page

5 columns at full width, 16px gutters. Each tile occupies a fixed aspect slot (roughly 3:5 portrait). The grid recedes visually - its job is to hold images, not to assert itself.

### Caption Label
**Role:** One-line description under each tile describing the project type

Inter 12px, Graphite (#858585), centered, 8px below the card. Format is 'X Y' or a short noun phrase.
