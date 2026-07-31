# Components

### Numbered Section Nav Card
**Role:** Primary navigation - each card labels a page section with its index number and title

Vivid solid-fill card, 16px radius, full width of sidebar (~150px). Two-line layout: tiny '00'-'07' index number in Bone Cream (#f4e9e1) at 12-13px StabilGrotesk 400, then the section label in Bone Cream at 16-18px StabilGrotesk 400. Padding 12-16px vertical, 16px horizontal. One card per section color: Ember Orange, Pulse Violet, Ink, Cobalt Blue, Crimson, Caution Yellow, Voltage Green.

### Active Section Nav Card
**Role:** Indicates the section currently in viewport

Same 16px-radius dimensions as a Numbered Section Nav Card, but filled Paper White (#ffffff) with Ink (#0e0e0e) text. The color inversion reads as 'you are here' without needing an underline or dot indicator.

### Display Headline
**Role:** Section hero type - the dominant visual on every page section

100-259px using KlarheitKurrent 400-500 or RightGrotesk 700. Ink (#0e0e0e) on cream, or Bone Cream on a color block. Line-height locked to 1.00-1.03 - the type touches itself. Letter-spacing -0.02em to -0.04em at display sizes. No max-width constraint; type bleeds to the container edge or wraps to 2-3 lines.

### Page Header
**Role:** Persistent top bar - brand identity and tagline

Full-width, sits on the cream canvas with ~24px padding. Left: 'Raw Materials' at 17-18px StabilGrotesk 400 in Ink. Right: 'An Unusual Design Company' in the same size and weight, Ink. No logo mark - the wordmark IS the logo. No border, no background fill - type sits directly on cream.

### Scroll Progress Bar
**Role:** Bottom-of-viewport reading progress indicator

Full-width Ember Orange (#ff3d00) bar, 4-6px tall, fixed to viewport bottom. Fills left-to-right as the user scrolls. Also includes a tiny '01/01' section counter in Ink at 12px StabilGrotesk on the right edge.

### Color Block Content Card
**Role:** Content containers in Work, Talent, and case-study sections

Full-saturation fill in one of the accent colors or dark slates, 16px radius, 24px padding. Content inside is Bone Cream or Paper White type at 16-18px StabilGrotesk 400. No shadow, no border. Often used as a 2-column or 3-column grid element.

### Tinted Section Background
**Role:** Alternating full-bleed section backgrounds between content blocks

Full viewport-width band in one of the five warm washes: Sage (#cee4cd), Blush (#e4d0cd), Sand (#e7e4d0), Sky (#cddae4), or Celadon (#ddded3). No border between sections - the color shift itself is the divider. 48-80px vertical padding. Type inside is Ink.

### Pill Tag
**Role:** Category labels, skill tags, metadata

99.36px radius (full pill), 6-8px vertical padding, 12-16px horizontal. Filled with a section color or Ink, text in Bone Cream or Paper White at 12-13px StabilGrotesk 400.

### Rounded Badge
**Role:** Index numbers, status indicators, small annotations

24px radius (slightly more than fully rounded at small sizes), 4-8px padding. Filled with a section accent color. Text at 12px StabilGrotesk 400 in Bone Cream or Paper White.

### Image Frame
**Role:** Container for photography in Work and Talent sections

16px radius, no border, no shadow. Image fills the frame edge-to-edge. Sits on cream canvas or inside a Color Block Content Card.

### Ghost Button
**Role:** Secondary action - 'Read more', 'View project', section transitions

Transparent fill, 1.5-2px Ink border (#0e0e0e), 16px radius, 12px 20px padding. Text at 16px StabilGrotesk 400 in Ink. No fill on hover - instead the border thickens to 3px. This is the system default; filled colored buttons only appear in nav.

### Body Text Block
**Role:** Paragraph content, descriptions, bios

StabilGrotesk 400, 16-18px, line-height 1.38, Ink (#0e0e0e) on cream, or Bone Cream on dark/colored surfaces. Max reading width ~640px even though the container is wider - text doesn't stretch full-bleed.

### Section Index Header
**Role:** Small marker above each section - '01', '02', etc.

12-14px StabilGrotesk 400 in Ink or Bone Cream, letter-spacing -0.05em. Sits above a display headline, left-aligned, with 8px gap to the headline.

### Link Inline
**Role:** Inline text links within body copy

StabilGrotesk 400 at body size, Ink with a 1px Ink underline. On hover: text color shifts to the accent color of the current section. No color-only differentiation - always underlined.
