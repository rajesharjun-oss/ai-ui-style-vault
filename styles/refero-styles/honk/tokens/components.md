# Components

### Blue Hero Canvas
**Role:** Full-bleed hero section

100% viewport-width section filled with #008fff. Contains a two-column layout: left = stacked headline + sub + notification strip; right = floating phone mockup with decorative speech-bubble shapes. No top/bottom padding asymmetry - the blue extends edge-to-edge as the brand canvas.

### Highlighted Headline
**Role:** Hero/section H1

Honk Header 700 at 52px, white, -0.012em tracking, line-height 1.23. Typically split across 2-3 lines with 1-2 inner words wrapped in a <span> set to #ffe400 (Signal Yellow). The yellow word is never underlined or bolded differently - only color shifts.

### Hero Sub-headline
**Role:** Body intro under headline

Honk Sans 400 at 19px, white, line-height ~1.55, no emphasis styling. Sits 24-32px below the headline with no divider.

### Notification Banner
**Role:** Embedded chat notification UI

White (#ffffff) panel, 16px radius, 16-20px vertical padding, full-width within the hero column. Contains a tiny yellow location-pin icon at right, a 'Read Announcement ' label in small Honk Sans, and a bold message line. Functions as a live-product proof card, not a CTA - it shows the app in use.

### Phone Mockup Frame
**Role:** Device illustration for product showcase

Rendered iPhone-style frame (dark bezel) containing a green game screen. Sits at a slight tilt or float on the right side of the hero. Scaled to roughly 45-55% of the hero width. Never has a drop shadow - sits on the blue with color contrast alone.

### Speech Bubble Decoration
**Role:** Floating emoji-shaped UI nubs

Soft, rounded shapes (16-20px radius) in white with a single icon (heart, settings gear) centered. Float off the phone mockup as scattered confetti - these are brand decoration, not interactive elements. Two to three per hero at most.

### In-Phone Game Screen
**Role:** Product-internal UI (device screen content)

Green (#3fcc6b) fill inside the phone frame with white tic-tac-toe grid, avatar bubbles, and small white circular action buttons (volume, mute, mic) along the bottom. This is the ONLY context where green appears.

### Ghost Link Button
**Role:** Lightweight text link / action

Honk Sans 500 at 14-16px, white, no background, no border. Often paired with a chevron or arrow glyph. Used for 'X Chatter', footer links, and secondary actions. The 6px-radius token applies if a pill-shaped variant is needed.

### Footer Section
**Role:** Closing dark or blue band

Continues the blue field or shifts to a deeper tone. White text, Honk Sans 400 at 14-16px, link rows with minimal padding. No card-based footer columns - the footer reads as a flat list of links, not a card grid.
