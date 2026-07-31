# Components

### Buy Button (Primary Action)
**Role:** Purchase CTA on every collectible card

Background #00df00, text #121212 at 15px MonumentGrotesk weight 500, padding 10px 16px, border-radius 8px. No shadow. The radioactive green is the only fill color in the system that isn't grayscale; it makes the transaction unmistakable against the monochrome feed. Letter-spacing -0.015em.

### Sign Up Button (Dark Fill)
**Role:** Account creation in top-right header

Background #121212, text #ffffff at 13px MonumentGrotesk weight 500, padding 8px 16px, border-radius 8px. The dark inverted counterpart to the green Buy button; serves the secondary auth action.

### Log In Button (Ghost)
**Role:** Returning-user entry in top-right header

Transparent background, text #121212 at 13px MonumentGrotesk weight 500, padding 8px 16px, no border, border-radius 8px. Sits to the left of the Sign Up button with minimal visual weight.

### Follow Button (Pill Outline)
**Role:** Subscribe to a creator in the right rail

Background #121212, text #ffffff at 13px MonumentGrotesk weight 500, padding 8px 16px, border-radius 9999px. Fully pill-shaped. Inverted dark fill against the white card.

### Collectible Card (Feed Post)
**Role:** Primary content unit in the center feed

Flat white surface, no shadow, border-radius 12px. Contains: creator header row (avatar 32px circular + name + timestamp), 1:1 or 4:5 media fill, action bar (heart, comment, share icons in #4d4d4d), title at 15px weight 500 #121212, Buy button right-aligned. Cards stack vertically with 12-16px gap; separated by #e6e6e6 hairlines.

### Left Navigation Rail
**Role:** Persistent icon-based navigation column

Fixed 56px-wide left column, icons only (no labels), vertically centered, 24px vertical gap between icons. Icon color #4d4d4d default, #121212 active. A circular avatar sits at the top; a hamburger menu at the bottom. Background white, no border.

### Top Search Bar
**Role:** Global search/command input

Centered in the top bar, ~480px wide, 8px border-radius, background #ffffff, border #e6e6e6 1px. Placeholder 'Search' in #cacaca. Left-aligned search icon in #878787. No visible focus ring - relies on border color shift.

### Suggested Follows Panel
**Role:** Right-rail discovery unit

Header 'Suggested follows' at 13px weight 600 #121212, three rows of avatar + username + Follow button. Avatars 40px circular. Buttons are dark pill (#121212 bg, white text, 9999px radius). No card container - sits directly on canvas with internal spacing.

### Price/Timer Bar
**Role:** Live auction status on collectible cards

Horizontal bar beneath media showing current bid in #121212 at 15px weight 500, countdown timer in #ff00f0 at 15px weight 500 (right-aligned). Thin #e6e6e6 top border separates from media.

### QR Code CTA Widget
**Role:** App-download prompt overlay bottom-right

Fixed position card, white background, 12px border-radius, 1px #e6e6e6 border. Contains a QR code, 'Get the App' header at 13px weight 600, 'Learn More' link in #4d4d4d. No shadow.

### Comment Input Field
**Role:** Inline comment composer on each card

Borderless or #e6e6e6 1px border, 8px border-radius, placeholder 'Add a comment...' in #cacaca at 15px. No visible label. Sits below the action bar with 8px gap.

### Zora Logo Mark
**Role:** Brand identifier in bottom-left corner

Wordmark 'Zora' in MonumentGrotesk weight 500 at 15px #4d4d4d. Unobtrusive, anchored to the page corner. No logo symbol - pure typographic mark.
