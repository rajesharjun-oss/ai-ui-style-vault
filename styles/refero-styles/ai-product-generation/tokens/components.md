# Components

### Display Headline
**Role:** Hero and section titles at editorial scale

Renders at 73-100px, weight 400, line-height 0.94, tracking -3.1%. Color #020108. Two-tone treatment: one noun or phrase is swapped to Ember Orange (#fd7b03) as inline emphasis while the rest stays Ink Black. The orange word is a continuation of the sentence, not a separate label - the sentence reads as a single typographic unit with a colored pivot.

### Section Heading
**Role:** Mid-page section introductions

43-53px, weight 500, tracking -0.645 to -1.06px. #020108. Same orange inline highlight pattern as display headlines. Often paired with a 15-17px body paragraph in Pewter (#818084).

### Pill Button (Primary Ghost)
**Role:** Call-to-action and navigation links

Border-radius 9999px. Thin border in #333333 or #020108 (1px). Padding 12px 20px. Text 14-15px weight 500, #020108. No background fill - ghost/outlined style. Inherits the system's flat, borderless-to-border contrast.

### Feature Card
**Role:** Container for product shots and video previews

Background #f7f7f7, padding 27px, border-radius 7px (tight radius keeps it utilitarian). No border, no shadow. Contains an inner image area with its own 20-27px radius. The card itself is a subtle tonal step from the page canvas.

### Image Tile
**Role:** Product photography thumbnail in grid

Border-radius 20-27px. Fills its grid cell edge-to-edge. Often presented as part of a 5-column grid. No border, no shadow. The image does the work; the chrome is invisible.

### Section Tag Badge
**Role:** Small contextual label above sections

Text 11-12px, weight 500, #020108. Prefixed with a small upward triangle or arrow glyph ( ). No background, no border - purely typographic. Examples: ' AI Fashion Photoshoot', ' AI Product Shots'.

### Product Card Header
**Role:** Label strip on AI-generated output tiles

Pill shape with border-radius 1.3px (nearly square). 7px vertical padding, ~12px horizontal. White background (#ffffff) with a thin #333333 border. Contains small orange dot indicator + product code text in #020108 at 10-11px.

### Sidebar Nav Item
**Role:** Left-edge 'What you can do' navigation

Plain text 13-14px, weight 400, #020108. No background, no active state chrome. Vertically stacked with ~20px gaps. A thin vertical rule separates it from the main content.

### Media Player Strip
**Role:** Top bar of the app preview window

Dark background (#020108) bar with traffic-light dots (red/orange/green) and a centered product breadcrumb in #ffffff. Border-radius matches the container (7px) at the top corners only. Serves as a meta-frame around the app preview content.

### Expand/Action Floating Button
**Role:** Bottom-right interactive control on sections

Perfectly circular, white (#ffffff) background, thin #333333 border. Contains four outward-pointing arrows (expand glyph) in #020108. Diameter ~48px. Floats with 20px offset from the section edge.

### Highlighted Inline Word
**Role:** Editorial emphasis within running text

A single word or short phrase within a headline or body sentence rendered in Ember Orange (#fd7b03) instead of #020108. No underline, no bold, no background - purely a color swap. Used sparingly: one or two per section maximum.

### Split Section (Text + Visual)
**Role:** Primary content section layout

Two-column grid at desktop: text block (40% width) on the left, visual block (60% width) on the right. 40-80px gap between columns. Text block contains tag heading body. Visual block is a bordered app-preview window containing a media strip and image grid.

### Image Gallery Grid
**Role:** Product photography collection

5-column grid of image tiles. All tiles same height, slight horizontal scroll overflow possible. Each tile has 20-27px radius. No gap between tiles in some variants, 7px gap in others.
