# Components

### Distributed Top Nav
**Role:** Primary navigation - replaces a conventional logo-cluster layout

A single horizontal row pinned to the very top of the viewport, 40px horizontal padding, items distributed across the full width using flexbox space-between (no centered logo, no hamburger). Four text items: the owner name (Diatype 500/700), the descriptor ('Designer & filmmaker'), the email address, and an availability status. Font: Diatype 500 at 26px, color #111111. The first item (owner name) is set at weight 700 to act as the only visual anchor in an otherwise flat row.

### Section Label
**Role:** Marker that introduces a new category block

Small, wide-tracked, acts as a typographic flag above each project list. Font: New Grotesk 600, ~12-14px, letter-spacing 0.069em, all uppercase or sentence case. Color: #111111 on light sections, #ffffff on the dark section. Sits 40-56px above the first project name. No underline, no icon - the tracking does the work.

### Project List Item - Large
**Role:** The primary content unit; project names that form the page's structure

Oversized text in Teg 500 or 600, 86px on desktop, line-height 1.04, letter-spacing -0.033em. Color: #111111 on light sections, #ffffff on the dark section. Stacked vertically with 0-4px gap between lines (the lines nearly touch, creating a continuous block). No bullet, no link styling, no metadata - the name is the entire item.

### Project List Item - Secondary
**Role:** Typographic counterpoint in the list stack

Slightly smaller project names at 58px, set in Beatricedisplay or Teg weight 500, line-height 1.05, letter-spacing -0.017em. Appears alongside the 86px names to create a rhythmic size alternation in the list - some names shout, others speak. Same color rules as the large variant.

### Light Canvas Section
**Role:** The default page surface for design work

Full-bleed white (#ffffff) background, left-aligned content column starting at the 40px page margin, 104px top/bottom internal padding. Contains the section label and project list. No borders, no shadows, no card containers.

### Dark Canvas Section
**Role:** Inverted surface for the film category

Full-bleed near-black (#111111) background with identical layout rhythm to the light section - same 40px left margin, same 104px vertical padding, same typographic structure. Text and labels invert to #ffffff. The alternation between the two surfaces is the page's only visual section break; there is no dividing line or gradient between them.

### Content Column
**Role:** The single left-aligned text column that holds all content

Left-pinned at 40px from the viewport edge, extends rightward as far as the longest line needs. No max-width cap on the text itself, but the longest project names (e.g. 'Iceland in Winter') naturally bound the column at roughly 800-900px. No centering, no right rail.
