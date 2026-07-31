# Components

### Project Table Row
**Role:** The primary repeating element on the page - each project is one row in a four-column table.

Flat table cell with no fill, no padding-top, 12px padding-bottom, 4px padding-left. 1px solid #000000 bottom border separates each row. Project name (left column) in 16px NHaasGrotesk weight 400 #000000, left-aligned with 4px indent. Type, Location, and Year columns are right-aligned in the same 16px #000000. No hover state, no zebra striping, no rounded corners.

### Table Column Header
**Role:** Labels the four columns above the project list.

Small caps (or CSS text-transform: uppercase with default tracking) set in 15px NHaasGrotesk weight 400 #999999. Same 12px bottom padding as data rows. Words: PROJECT, TYPE, LOCATION, YEAR. The lighter gray distinguishes the header label from the data row beneath without changing weight or size drastically.

### Inline Navigation Link
**Role:** Site-level navigation - about, contact, imprint, read more.

Inline text with a 1px #000000 underline. No pill shape, no fill, no border-radius. Often prefixed with a arrow glyph and separated by 30px right margin. Wraps inline with the surrounding paragraph text. Hover state: no change - color and weight stay constant.

### Arrow Glyph ( )
**Role:** The only icon in the entire system. Marks navigability.

U+2192 RIGHTWARDS ARROW rendered in NHaasGrotesk at the same size and color as the adjacent text. Used to prefix every link ( about, contact, Open Project, read more) and as left/right nav controls ( ) beside the news count. Never replaced by a graphic icon or SVG.

### Hero Photograph
**Role:** Large editorial image occupying the right half of the viewport on first load.

Full-bleed within its column, no border, no border-radius, no padding, no caption overlaid. Aspect ratio is determined by the viewport - it is simply the right half of the screen at 100% height. Subject is always architectural site documentation at high contrast (stone, concrete, interior, tunnel, building). No filter, no duotone, no gradient overlay.

### Intro Paragraph
**Role:** Landing text describing the practice, anchored in the upper-left column.

30px NHaasGrotesk weight 400 #000000, line-height 0.90, letter-spacing -0.33px. Wraps at approximately 45% of viewport width to leave room for the hero image. The display scale is used here rather than the body scale - there is no separate headline element.

### News/Featured Project Caption
**Role:** Metadata strip directly under the hero image.

Three-part inline row: 'News 2/19' in 15px #999999 on the left, nav arrows in 16px #000000 centered, project title ('Castle museum Linz - New underground city access') and ' Open Project' link in 16px #000000 on the right. No box, no border, no background.
