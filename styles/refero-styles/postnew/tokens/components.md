# Components

### Top Nav Bar
**Role:** Minimalist site navigation - three labels centered on a dark canvas

Centered horizontal row of three text links (Index, Feed, Profile). System sans-serif at 12px, #fafafa color, letter-spacing normal. 10px row-gap between items. No background, no border - floats on the canvas with no visual weight. Active state not visually distinct in the data; treat as ghost navigation.

### Scroll Position Indicator
**Role:** Vertical dot column tracking scroll progress

Thin vertical strip of 10-12 small dots positioned at the left edge of the viewport, ~120px from the left. 5px row-gap between dots. Filled dots in #5d5d5d, active dot in #fafafa. This is the only persistent left-side UI element.

### View Toggle
**Role:** Switch between grid and list layout modes for content

Bottom-center floating control with two icon buttons side by side. Slate Surface (#242424) background, 12px horizontal padding, 8px vertical padding. Icons in #fafafa at 12px. 13px gap between the two toggle buttons.

### Vitrine Frame
**Role:** Dark container that presents a single work or art object in isolation

Full-viewport or large-centered dark panel with #1a1a1a background, 0px radius (sharp edges), no border. The object sits centered within, surrounded by generous negative space. This is the 'gallery wall' component - it frames content with the discipline of a museum vitrine.

### Editorial Spread
**Role:** Full-bleed two-page-style layout combining imagery and bold type

Edge-to-edge layout with no padding from viewport edges. Left half: photography or 3D render bleeding off all sides. Right half: oversized display type overlapping the image, often in #000000 with chromatic abstract shapes layered on top. The type uses ABC Diatype Medium at 22px but visually appears much larger due to the 100vh scale. No border, no radius - the spread IS the page.

### Abstract Shape Decoration
**Role:** Sculptural 3D blob/bead elements that punctuate editorial spreads

Glossy 3D-rendered organic shapes in saturated colors (magenta, lime, blue, yellow, pink) placed over the spread. Not part of the design system palette - they belong to the content layer. When recreating, generate them as content, not as tokens.

### Ghost Button
**Role:** Secondary interactive element - minimal, no fill

12px horizontal padding, 8px vertical padding, 0px radius. Background #242424 (Slate Surface). Text in #fafafa at 12px system sans. No border, no shadow. Used for the view toggle and any low-emphasis interaction.

### Brand Mark Lockup
**Role:** Logo + product name combination for sponsored or featured content

Centered or right-aligned lockup: brand wordmark (e.g. NIKE) in bold black sans, with product line label (e.g. AIR MAX) below in tracked-out caps at 12px. Appears within editorial spreads as a content element, not as persistent UI.
