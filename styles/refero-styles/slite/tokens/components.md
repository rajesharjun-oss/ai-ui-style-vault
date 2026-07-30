# Components

### Primary CTA Button (Ember Pill)
**Role:** The single orange button on the page - reserved for the main conversion action.

Filled #f67748 background, white text, UniversalSans 17px weight 600, line-height 1, border-radius 999px (full pill), padding 12px 24px. Appears at most once above the fold. The only color-saturated button on the page.

### Dark CTA Button (Charcoal Pill)
**Role:** Secondary high-emphasis action, typically 'Start for free'.

Filled #2d2f34 (or #3f434a) background, white text, UniversalSans 17px weight 600, border-radius 999px, padding 12px 20px. Used in the header nav for the highest-intent action.

### Outlined Pill Button
**Role:** Medium-emphasis action - Book demo, secondary nav actions.

Transparent background, 2px solid #2d2f34 border, #2d2f34 text, UniversalSans 15-17px weight 500-600, border-radius 999px, padding 10px 20px.

### Ghost Text Button
**Role:** Low-emphasis inline action - nav items, sub-actions inside cards.

Transparent background, no border, #3f434a text, UniversalSans 14-15px weight 500, padding 4px 8px. Minimal padding signals 'I am a label, not a control'.

### Square Ghost Button
**Role:** Compact UI control - close buttons, icon toggles, inline editors.

Transparent background, #2d2f34 text, border-radius 8px, padding 0px 8px. The 8px radius is the sharpest button radius in the system - used only for tiny inline controls.

### Dust Tag Chip
**Role:** Feature highlight tags and category labels - the most-repeated component on the page.

#f9efe4 background, #3f434a text, UniversalSans 13-15px weight 500, border-radius 9999px, padding 8px 16px. Always pill-shaped, always warm. Used in rows of 3-4 to label a section's sub-topics.

### Status Pill (Verified / Self-maintained)
**Role:** Trust and maintenance indicators inside product screenshots.

Tag Violet (#4b51c3) or Verification Green (#479a53) text on white, paired with a small filled icon. UniversalSans 13px weight 500. Sits inline above content titles.

### Cream Feature Card
**Role:** Primary marketing card - 3-column feature grid items, testimonial cards.

#fdf9f4 or #f9efe4 background, border-radius 32px, padding 48px top / 32px bottom / 24px sides, no shadow. The 32px radius is Slite's signature - generous but not pillow-soft. Optionally bordered with a 2px #f67748 ember stroke to denote 'selected' or 'highlighted' cards.

### White Product Card
**Role:** Product screenshot containers and tooltips stacked on the cream canvas.

#ffffff background, border-radius 12px, box-shadow 0 1px 3px rgba(0,0,0,0.1) + 0 2px 6px rgba(0,0,0,0.05) + 0 4px 12px rgba(0,0,0,0.01). The three-layer shadow is the only place Slite uses depth - the rest of the page stays flat.

### Compact UI Card
**Role:** Inline product UI mock elements - sidebar items, list rows, agent chips.

#fdfdfd (near-white) background, border-radius 16px, padding 12px 16px, no shadow. The tighter 16px radius signals 'I am a UI element inside a product mock, not a marketing card'.

### Ember Testimonial Card
**Role:** Featured customer quote - the only orange-filled card.

#f67748 background, white text, border-radius 16px, padding 32px. Used at most once per page as the visual punctuation between sections of cream cards.

### Logo Trust Bar
**Role:** Social proof - '3,000+ companies trust Slite' row.

Horizontal row of monochrome black customer logos (Doodle, Lush, Frontify, Karbon, Visma, Omnisend) on the cream canvas, with a small 13px caption beneath each ('Migrated from Notion'). Logos are rendered at a single visual weight and aligned to a shared baseline.

### Scribble Annotation
**Role:** Hand-drawn circle or underline around a key word in a headline.

1.5-2px solid #f67748 stroke, no fill, slightly imperfect oval shape (roughened path), placed behind or around a single word ('Verified'). The visual signature that makes headlines feel hand-edited rather than rendered.

### Underline Link
**Role:** Inline text link inside paragraphs.

#3f434a text, no underline by default, 1px underline on hover with a #f67748 ember accent color. The hover color is the only place the ember orange appears in text.

### Hero Product Frame
**Role:** Large product screenshot shown below the headline.

A White Product Card containing a product mockup - sidebar navigation, breadcrumb, content area. Framed by the canvas and dropped onto the page with a subtle offset (rotation 0-1deg optional). Always 12px radius, always #ffffff, always with the three-layer shadow.
