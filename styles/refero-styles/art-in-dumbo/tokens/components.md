# Components

### Logo Wordmark Block
**Role:** Brand mark in the top-left of every screen

Stacked three-cell grid: 'ART', 'IN', 'DUMBO' on three lines. Each letter sits in its own black-bordered cell on a white ground. Borders are 1px black, no fill, no radius. Cells are flush - no gap between them - so the mark reads as a single printed stamp.

### Sticky Header Bar
**Role:** Persistent navigation across all pages

White background, no border. Left: logo wordmark. Right: three text links (Events, Exhibitions, First Thursdays) in 16-19px Helvetica 500, #000000, flush right. No icons, no background pills - nav is just type.

### Full-Bleed Hero Photograph
**Role:** Above-the-fold visual anchor on the landing page

Documentary-style photograph of artists at work, edge-to-edge with no container or radius. The logo overlays top-left in a solid white-backed block. No text overlay other than the wordmark.

### Display Heading
**Role:** Section openers and welcome statements

63-68px Helvetica 500, #000000, line-height ~1.05, tracking normal. Sentence case, no max-width clamp - runs nearly full bleed for editorial weight. Sage-green horizontal rule (3-4px) sometimes underlines the heading or its first word.

### Body Paragraph
**Role:** Welcome copy, event descriptions, editorial text

22-27px Helvetica 500, #000000, line-height 1.20-1.27, no max-width cap. Generous, readable, never condensed.

### Email Input Field
**Role:** Newsletter capture on the welcome block

2px border-radius, #f1f2f2 fill, no visible border. Placeholder text in 16px Helvetica 500, #000000 at ~40% opacity. Inline adjacent to a ghost Subscribe button.

### Ghost Text Button (Subscribe)
**Role:** Secondary action paired with form fields

No background, no border, no radius. Label in 16px Helvetica 500, #000000, followed by a small right-pointing arrow glyph. Sits flush right of its input.

### Sage Pill Button (Map & Directory)
**Role:** Primary floating CTA, sticky bottom-right

50px border-radius (full pill), #71cc98 fill, #000000 text, 16-19px Helvetica 500, horizontal padding ~20px. A small filled sage dot (8px) sits inside the left padding as a status indicator. Subtle shadow: rgba(0,0,0,0.25) 0 0 10px. This is the only chromatic fill button in the system.

### Exhibition List Row
**Role:** Primary content unit on the Exhibitions page

Horizontal row: square thumbnail (~80px, 4px radius), then a four-column meta block (Date range / Title / Gallery name / Open hours). Rows separated by 1px solid #000000 hairlines - no zebra striping, no card backgrounds. Meta text in 16-22px Helvetica 500; gallery hours in #bdbdbd.

### Urgency Tag (Closing Soon)
**Role:** Status indicator for time-sensitive items

Inline text label, no background, no border. 16px Helvetica 500 in #ff7f41. Sits directly under the date range in an exhibition row.

### Status Meta (Open hours)
**Role:** Secondary metadata in list rows

16-19px Helvetica 500, #bdbdbd. Always one line, never wrapped. Communicates operational state without competing with primary text.

### Sticky Floating Action
**Role:** Persistent wayfinding CTA

Same component language as the Sage Pill Button, but position:fixed bottom-right. Reappears on scroll with the same shadow and radius. Functions as a quiet, always-on directory shortcut.
