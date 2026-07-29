# Components

### Dark Pill Button
**Role:** Primary action control

Filled dark button at #292929 background, #fafafa text, Aspekta 500 at 16px. Radius 100px creates the pill shape. Padding 11px vertical, 22px horizontal. Used for the main 'Login / Sign up' action and any single primary CTA per screen. No visible border - the dark fill IS the boundary.

### Light Pill Button
**Role:** Secondary action control

Ghost button at #f4f4f5 background with #292929 text. Radius 100px. Same dimensions as the dark pill. Used when a secondary action sits next to a primary one without competing for weight.

### Floating Content Card
**Role:** Content panel - feedback widget, feature block

White surface (#fafafa) with 32px radius. Layered shadow: hairline ring (rgba(19,19,22,0.05) 0px 0px 0px 1px) + soft drop (rgba(0,0,0,0.04) 0px 2px 3px 0px, rgba(34,42,53,0.04) 0px 4px 6px 0px, rgba(0,0,0,0.05) 0px 1px 1px 0px). Padding 24-32px. Contains structured lists with icon + title + description rows separated by 16-24px gaps.

### Modal/Card with Deep Elevation
**Role:** Elevated overlay or popover

Same 32px radius and #fafafa surface, but with stronger shadow: adds rgba(47,48,55,0.05) 0px 24px 68px 0px to the standard card shadow stack. Used for elements that need to feel detached from the page surface.

### Rounded Image Frame
**Role:** Image container

16px radius border with subtle drop shadow (rgba(16,24,40,0.08) 0px 17px 23px -6px, rgba(16,24,40,0.03) 0px 6px 9px -3px). Used for product screenshots, portraits, and editorial images that need to feel lifted from the page.

### Navigation Bar
**Role:** Top-level page navigation

Full-width bar on Bone (#fafafa) background. Three-zone layout: brand mark left ('QP' wordmark), centered logo (the 'Q.' glyph), utility links right ('Blog' text link + dark pill button). No visible border or background fill - sits on the page canvas. Height ~60px.

### Centered Hero Block
**Role:** First-screen hero pattern

Vertically stacked, horizontally centered. Fasthand 32px accent line at #696969, then Aspekta 48-56px display headline at #080808 in 2 lines, then 16-18px body subtext at #696969. No background, no border - pure type on canvas. Generous vertical padding (80-120px top/bottom).

### Two-Column Letter Layout
**Role:** Long-form narrative sections

Left column: Fasthand kicker + Aspekta heading-lg subhead, max-width ~40% of container. Right column: body text at 18px weight 400, #696969, line-height 1.56. Columns separated by 40-60px gap. The asymmetric split creates editorial rhythm.

### Feedback Option Row
**Role:** Selectable item in the feedback widget

Horizontal row: icon (24px, #292929 stroke) + title (16px Aspekta 500, #080808) + description (14px Aspekta 400, #696969). Padding 12px vertical. Separated from neighbors by subtle background change or 8px gap, not a visible divider line.

### Grid Background Pattern
**Role:** Subtle page texture

Very faint square grid (1px lines at #e4e4e7 or similar low-contrast) behind the hero section. Not a component but a visual foundation - gives the flat canvas a sense of structure and technical precision.

### Wordmark Lockup
**Role:** Brand identity in header/footer

Small uppercase 'QP' set in Aspekta 500 at 14px, or the standalone 'Q.' glyph at 24px with the period as a design detail. Charcoal (#080808) on the light canvas. No logo color - identity is purely typographic.

### Illustrative Crowd Border
**Role:** Decorative full-bleed illustration

Hand-drawn doodle characters in a rainbow spectrum (blue, yellow, pink, orange, green) forming a crowd border at the bottom of the hero. Full-bleed width, organic edge (not clipped to a rectangle). This is the ONLY color in the system - purely decorative, never applied to UI controls or text.

### Text Link
**Role:** Inline navigation link

Aspekta 400 at 16px, #292929, no underline by default. Appears in nav and body copy. 28 borderColor uses of #fafafa suggest links may have a subtle background or underline treatment in certain states.

### Hairline Divider
**Role:** Section separator within cards or lists

1px line at #e4e4e7 (Silk) or #b2b2b2 (Ash). No vertical padding - just a thin horizontal rule. Used between content rows inside the feedback widget card.
