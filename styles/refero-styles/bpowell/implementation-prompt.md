# AI Implementation Prompt

Build a Bpowell-inspired interface using this source-derived style bundle.

Reference site: https://www.bpowell.co
Theme: mixed
Category: Design
North star: type as architecture on white plaster

Use these palette anchors:

- Plaster White `#ffffff` for Primary canvas for the light sections; text color on the dark sections; hairline dividers on the dark sections
- Carbon `#111111` for Page background for the dark/film section; primary body text on light sections; structural fill for project name typography
- Ink Black `#000000` for Secondary text and fill on light sections; used where maximum contrast is needed against the white canvas
- Graphite `#2b2b2b` for Subtle darker border for low-emphasis rules on light surfaces

Use these typography anchors:

- Teg `--font-teg` for Display - reserved for the largest project names and the hero text. The aggressive -0.033em tracking at 86px tightens the letters into a near-monolithic block; this is the font that creates the 'stacked concrete' reading. Substitute: Migra, Editorial New, or Canela Display.
- Beatrice Display `--font-beatrice-display` for Mid-scale editorial type - appears as secondary project list text alongside the larger Teg names, providing typographic counterpoint at a calmer scale. Substitute: Tiempos Headline, Canela, or Reckless.
- Beatrice `--font-beatrice` for Body-weight Beatrice variant for the same 26px role but with the text-figure character set. Substitute: same as Beatrice Display.
- Diatype `--font-diatype` for Workhorse sans for body copy, nav items, and supporting text. Weight 500 is the default; 700 is reserved for the nav name 'Ben Powell' to give it anchor weight in the distributed nav. Substitute: Sohne, Inter, or ABC Diatype.
- New Grotesk `--font-new-grotesk` for Wide-tracked all-caps label face for section markers ('Design', 'Film'). The extreme +0.069em tracking turns short words into spaced-out type-art - this is the system's only 'decorative' choice. Substitute: ABC Diatype Mono Upper, Space Grotesk, or Neue Haas Grotesk Display.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1400px.
- Section gap: 104px.
- Card padding: 0px.
- Element gap: 16px.

Build these component patterns where relevant:

- Distributed Top Nav: Primary navigation - replaces a conventional logo-cluster layout
- Section Label: Marker that introduces a new category block
- Project List Item - Large: The primary content unit; project names that form the page's structure
- Project List Item - Secondary: Typographic counterpoint in the list stack
- Light Canvas Section: The default page surface for design work
- Dark Canvas Section: Inverted surface for the film category
- Content Column: The single left-aligned text column that holds all content

Do:

- Use exactly two surfaces - #ffffff and #111111 - and alternate them as full-bleed sections to create rhythm without any divider lines
- Set project names in Teg at 86px / line-height 1.04 / letter-spacing -0.033em on desktop; this aggressive tracking is what makes the list read as a wall of text
- Use New Grotesk 600 with 0.069em tracking for all section labels - the wide spacing is the system's only 'decorative' typographic move
- Distribute nav items across the full viewport width with space-between; never cluster them in a corner or center them
- Anchor the leftmost nav item at weight 700 (Diatype) so the owner's name reads as the only visual weight in an otherwise flat row
- Maintain 40px left padding from the viewport edge for the content column on all sections
- Use 104px for the major vertical section padding - it is the largest spacing unit in the system and defines the page's breathing rhythm

Avoid:

- Do not introduce any color beyond #ffffff, #111111, #000000, and #2b2b2b - the system is monochrome by design
- Do not add images, thumbnails, or preview artwork to project list items; the name alone is the entry
- Do not center project names or align them to a grid - they are pinned to the left margin and let their own length determine the column
- Do not use card containers, rounded corners, or drop shadows; the system has zero elevation and zero radius
- Do not set body or nav text larger than 26px; the scale jumps directly to 58px for sub-headings and 86px for display, and bridging that gap destroys the contrast
- Do not add hover color changes, underlines, or button styles to project names - they read as a list, not as links
- Do not use more than one typeface per text block; mixing Teg with Beatricedisplay inside the same line breaks the typographic system

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
