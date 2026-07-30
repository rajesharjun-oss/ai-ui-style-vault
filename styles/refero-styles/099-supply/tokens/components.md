# Components

### Mockup Tile Card
**Role:** Primary unit - displays a 3D mockup asset with catalog-style metadata strip

White background, 1px solid #e0e0e0 border, 8px radius. Top portion: centered mockup image on white. Bottom metadata strip: padded 10px top/bottom, 12px right/left, separated from image by a 1px #e0e0e0 horizontal divider. Left metadata label in Soehne Mono 11px weight 400 #555 (format 'M 005'). Right label in Soehne Mono 12px weight 400 #555 uppercase with 0.08em tracking (asset name like 'IPHONE'). No shadow.

### Framer Component Tile Card
**Role:** Second tile variant for interactive component previews

White background, 1px solid #e0e0e0 border, 6px or 8px radius. Centered component preview (toggle, loader, browser frame). Bottom label strip same format as mockup tile but prefixed 'C' instead of 'M' (e.g. 'C 000 THEME TOGGLE'). Expand icon (two arrows) sits in the top-right corner as a 16px #555 stroke.

### Section Heading
**Role:** Section label above each grid block

Soehne Mono 26px weight 500, uppercase, #999999, letter-spacing 0.18em (4.68px). Acts as a quiet, tracked-out curator's heading. Examples: '3D MOCKUPS', 'FRAMER COMPONENTS'. No underline, no decoration.

### Primary Button
**Role:** Filled dark button for 'Buy' and conversion actions

Background #101010, text #ffffff, Soehne Mono 12px weight 400 uppercase with 0.08em tracking, 9999px (pill) radius, padding ~10px 16px. Hover: background shifts to #999999. Used sparingly - appears in modal CTAs and the browser-frame demo.

### Ghost Button
**Role:** Secondary outlined button paired with primary

Background transparent, border 1px #999999, text #555555, same Soehne Mono 12px uppercase treatment, 9999px radius, padding ~10px 16px. Appears alongside Primary Button in modal demo ('Close').

### Metadata Label
**Role:** Catalog-style tag below each tile

Soehne Mono 12px weight 400, uppercase, 0.08em letter-spacing, #555555. Left-aligned: asset ID (e.g. 'M 005'). Right-aligned: asset name (e.g. 'IPHONE'). No background, no border, sits on the card's metadata strip.

### Modal Panel
**Role:** Overlay for copy/info interactions

White background, 1px #e0e0e0 border, 8px radius. Header text Soehne Mono 16px weight 400 #101010 ('Less is more'). Body copy Soehne Mono 11px #555. Footer contains a Ghost Button + Primary Button pair right-aligned.

### Theme Toggle
**Role:** Interactive component demo - pill switch

Pill-shaped (999px radius), 1px #e0e0e0 border, white background, inner circle thumb at left position showing #ffffff fill on #101010 track, or reversed when toggled.

### Loader Ring
**Role:** Circular progress component demo

Two concentric arcs forming a ring: lighter arc #e0e0e0 (background ring), darker arc #101010 (progress arc, ~270 sweep). No fill, pure stroke composition.

### Browser Frame
**Role:** Windowed screenshot frame component

Rounded rectangle with 8px radius, 1px #e0e0e0 border. Top chrome bar: three small circles (traffic lights) and a URL pill input with #c8c8c8 placeholder text ('https://'). Interior content area displays a globe or page preview.

### Compare Slider
**Role:** Before/after image comparison component

Rectangular frame split vertically: left side shows light-mode garment, right side dark-mode variant, divided by a 1px #101010 handle/bar with a draggable circle grip.

### Table Component
**Role:** Structured data table demo

Header row: 'COMPANY' / 'FOUNDED ' in Soehne Mono 12px uppercase #999999 with 0.08em tracking. Body rows alternating white background, 1px #e0e0e0 horizontal dividers, text in Soehne Mono 12px #101010. No vertical borders.

### Form Builder Checkbox
**Role:** Form control component demo

Small 16px square with 4px radius. Unchecked: 1px #e0e0e0 border, white fill. Checked: #101010 fill with white checkmark stroke at ~2px weight.

### Counter Display
**Role:** Large numeric typographic component

Soehne Mono weight 400 at large display size (~54px or scaled), rendered as three stacked digits '099' in #101010 on white. Pure typographic exercise - no frame, no border.
