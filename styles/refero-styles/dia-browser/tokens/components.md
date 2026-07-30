# Components

### Hero Download Button
**Role:** Primary conversion - the most prominent CTA on the hero

White background (#ffffff), 20px radius, 0px vertical padding with 16px horizontal padding, text in pure black (#000000) at 16px ABC Oracle Triple. Sits centered below the tagline. The 20px radius (not full pill) gives it a soft, rounded-rectangle presence rather than a full pill - distinct from nav pills.

### Pill Navigation Button
**Role:** Top-level nav items in the glassmorphic nav bar

Transparent background with rgba(0,0,0,0.85) text, 20px radius, 0px vertical padding with 16px horizontal padding. Sits inside a frosted-glass nav container with backdrop blur 12-24px. Text is 14px ABC Oracle weight 400.

### Glass Navigation Bar
**Role:** Fixed top navigation - the floating command center

Bone background (#f8f8f8) with 16px radius, 1px border, backdrop blur 12-24px. Shadow: rgba(0,0,0,0.06) 0px 2px 8px. Contains logo mark (left) and nav pills (center) and Download CTA (right). Floats with margin from viewport edge.

### Text Link with Arrow
**Role:** Inline navigation within content sections

Transparent background, rgba(0,0,0,0.85) text, 16px radius, 20px vertical and 24px horizontal padding. ABC Oracle Triple at 16px. Used for 'Learn more' style links with trailing arrow.

### Pill Watch Button (Hero Video)
**Role:** Secondary hero CTA - watch the scream

Semi-transparent black background rgba(0,0,0,0.65), white text, 9999px full pill radius, 10px vertical and 20px right / 12px left padding. Contains a play icon (white triangle) at left, 16px ABC Oracle Triple label at right. Sits overlaid on the dark hero image.

### Feature Card (Decks / Live Work / Better Meetings)
**Role:** Product feature showcase cards in the grid sections

Bone or white background with subtle 1px border, large border-radius (12-24px), generous internal padding. Contains a tag pill at top (see below), heading, description text, and a product screenshot. Cards are large - nearly half the viewport width each in 2-column layout.

### Category Tag Pill
**Role:** Feature category labels (Decks, Live Work, Better Meetings, Profiles)

Linen background (#efefef) or similar light fill, 9999px full pill radius, small padding (~8px 16px). Text in dark gray or black at 14px ABC Oracle. Sits top-left of feature cards.

### Editorial Section Header
**Role:** Large section titles and subheadings

Exposure VAR at 48px weight 650, -0.05em letter-spacing, line-height 1.17, in pure black. Sometimes paired with a step number eyebrow (01, 02, 03) in 13px ABC Favorit Mono uppercase. Creates magazine-chapter feel.

### Numbered Step List
**Role:** Feature explanation sections (01, 02, 03)

Vertical list with 14px row-gap. Each step: 13px mono uppercase number in Carbon (#636363) above 18-20px heading in pure black above 16px body text in Carbon. Active step has bolder weight or darker text. Left-aligned with a thin vertical accent line.

### Product Screenshot Frame
**Role:** Browser/window chrome containers around product mockups

White background card with traffic-light dots (red, yellow, green) at top-left, tab bar with favicons, and 12px corner radius. Large drop-shadow filter (3-layer blur stack) makes the window float above the page surface.

### Dark Hero Section
**Role:** Opening full-viewport dramatic section

Void Black (#020204) background, full-bleed, with a large human photograph (screaming face) centered. Logo (Dia wordmark in white) at top, tagline in white at 18-22px below, Download button centered, and a pill watch button overlaid on the photo lower-center.

### Spectrum Gradient Bar
**Role:** Brand-defining rainbow motion element

Animated marquee gradient traveling left-to-right: pink (#FD02F5) red (#FA3D1D) yellow (#FFB005) lavender (#E1E1FE) blue (#0358F7) brown (#340B05). Appears as a thin horizontal line/bar between sections or as a animated underline. The --student-marquee token value: linear-gradient(270deg, #FD02F5, #FA3D1D 15.94%, #FFB005 42.76%, #E1E1FE 72.48%, #0358F7 100.02%, #340B05 150.75%).

### Settings Toggle Row
**Role:** Privacy/personalization toggle items

Horizontal row with label text left, toggle switch right. 16px ABC Oracle weight 400. Toggle: pill shape with sliding indicator. Minimal chrome, no background fill on the row itself - sits on the page canvas.
