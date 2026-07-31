# Components

### Top Navigation Bar
**Role:** Primary site navigation

Sticky top bar on #b7ffb4 canvas. Left: 'NaN' wordmark in NaN Holo Mono 14px uppercase. Center: nav links (FONTS, COMMISSIONS, PROJECTS, TXT, SHOP, STUDIO) in NaN Holo Mono 14px uppercase, #262626, letter-spacing 0.075em, 32px gap. Right: CART (0), ACCOUNT, then a tri-color circle icon and a small 'NaN' dot. No background fill, no shadow - sits directly on canvas. Bottom edge: no border, sections define their own top spacing.

### Hero Statement Block
**Role:** Opening brand description

Left-aligned paragraph in NaN Holo Mono 26px weight 400, #262626, line-height 2.25. Content fills roughly 75% of viewport width. No background, no border - the text IS the hero. A lime-green (#00ff00) SVG scribble overlays the right portion at ~40% opacity, drawing the eye past the text without blocking it.

### Live Font Tester
**Role:** Interactive type specimen controller

Sectioned widget with four control rows stacked vertically on a #b7ffb4 canvas. Row 1: small section label ( Our Latest Font Release, NaN Holo Mono 14px #262626, 0.075em tracking). Row 2: Size slider (left-aligned label 'Size 220px', then NaN Holo Mono 12px, line-track 1px #262626 with 6px #262626 thumb) + Leading slider (right-side label 'Leading', identical track style) + two select dropdowns (NaN Holo Mono 13px, 1px #262626 border, 2px radius, no fill). Row 3: keyboard-shortcut chips (rounded squares, 1px #262626 border, NaN Holo Mono 12px) + a pear emoji. Row 4: a massive display specimen in the selected family at the selected size. No drop shadows - borders and whitespace define the frame.

### Aurora CTA Button
**Role:** Sole chromatic primary action

Filled pill button, 29.4px radius, horizontal aurora gradient (pink #ffa3b6 violet #dda9ff blue #a2d1ff pink). Label in NaN Holo Mono 14px weight 500, #262626, uppercase, 0.075em tracking. Padding 14px 20px. Sits centered below the display specimen. One per page - this gradient is rationed because it is the only warm element in a cool palette.

### Display Headline (Specimen)
**Role:** Full-bleed type demonstration

Massive custom typeface rendered at 216-336px, weight 400, #000000 or #262626, line-height 0.80-0.90 depending on face. Text bleeds to both edges of the viewport (no max-width clamp) so the letterforms define the page's lateral scale. No background, no border - the type floats on the mint canvas.

### Font Specimen Card
**Role:** Library entry in the 'You Might Have Missed' grid

Three-column grid on the mint canvas. Each card: 1px #262626 border, 18px radius, transparent fill (shows mint through). Interior padding 20px. The card's own family name is rendered IN that family at 86px, weight 400, #262626, line-height 1.0 - the card is its own specimen. Two-line stack: 'NaN' (smaller) above 'Rage Zipp' (larger). No shadow, no hover elevation - the 1px border does all the work.

### Section Label
**Role:** Subsection heading

Left-aligned ' Section Name' in NaN Holo Mono 14px weight 400, #262626, 0.075em tracking. The hollow circle ( ) is a recurring typographic bullet that marks every new section without using color or weight changes. Followed by generous vertical breathing space (60-80px) before the section content.

### Select Dropdown
**Role:** Form control within the font tester

Inline select element, NaN Holo Mono 13px, #262626, 1px #262626 border, 2px radius, transparent fill. No focus ring color change - interaction is communicated through a 1-2px border darkening to #000000 on hover/focus. Inline with text controls on a single row.

### Range Slider
**Role:** Numeric control for size/leading

Native range input styled as a 1px #262626 line track with a 6px square #262626 thumb. Label text in NaN Holo Mono 12px, #262626, sits above the track. No value tooltip - the display specimen updates in real time as the user drags, providing feedback.

### Keyboard Hint Chip
**Role:** Reveals power-user shortcuts

Small rounded-square button, ~20x20px, 1px #262626 border, 2px radius, NaN Holo Mono 11px #262626 label. Used to surface shortcuts (e.g. 'R', arrows, 'OT') adjacent to the font tester controls.
