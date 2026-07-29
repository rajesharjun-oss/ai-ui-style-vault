# AI Implementation Prompt

Build a Akash Tyagi-inspired interface using this source-derived style bundle.

Reference site: https://akashtyagi.com
Theme: dark
Category: Agency
North star: midnight gallery wall with hot pink markers

Use these palette anchors:

- Obsidian Canvas `#000000` for Page background, card surfaces, inverted text on pink fills
- Parchment `#efe6d8` for Primary body and heading text - warm near-white with sepia undertone, replaces the typical cool white of dark UIs
- Bone `#aca69c` for Secondary text, button borders, metadata - mid-tone warm gray
- Ash `#736e68` for Muted body text, subtle link borders, inactive labels
- Charcoal `#605c56` for Hairline dividers, low-emphasis borders, heading underlines on dark
- Neon Petal `#ffa1f7` for Primary action buttons, active nav states, selected markers, occasional heading accents - the single chromatic punctuation in the system
- Acid Lime `#4dff00` for Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color

Use these typography anchors:

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- Geist `--font-geist` for Primary UI and body typeface - medium and semibold weights, tight negative tracking at -0.013em to -0.031em. Used for body copy, links, navigation, and small headings.
- Geist Pixel Triangle `--font-geist-pixel-triangle` for Display and section-label typeface - pixel/decorative variant used for all-caps section headers like 'SELECTED WORK' and the year range '2015 - 2026'. The pixel treatment gives editorial weight without serifs.
- Geist Mono `--font-geist-mono` for Metadata typeface - timestamps, email, technical labels, year stamps. The monospace signals system/data language against the proportional body.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1400px.
- Section gap: 200px.
- Card padding: 0px.
- Element gap: 16px.

Build these component patterns where relevant:

- Pill CTA Button: Primary action trigger
- Ghost Text Link: Secondary navigation and inline links
- Status Availability Indicator: Live availability signal
- Section Header with Date Range: Editorial section divider
- Project Showcase Card: Portfolio project entry
- Minimal Header Bar: Identity and time stamp
- Two-Column Intro Block: Personal statement
- Footer Social Link: External profile references

Do:

- Use #000000 as the universal background for every screen - never introduce a lighter or colored canvas
- Apply #ffa1f7 only to the single primary action per view; treat it as the system's only chromatic voice
- Set section labels in Geist Pixel Triangle 30px with -0.033em tracking for editorial weight
- Maintain 200px vertical gaps between major sections to preserve the gallery-wall rhythm
- Use warm neutrals (#efe6d8 #aca69c #736e68 #605c56) in descending tonal order for text hierarchy
- Use the green dot (#4dff00) exclusively for live status/availability - never as a generic accent or button color
- Render all project imagery edge-to-edge with no card chrome, radius, or shadow

Avoid:

- Never introduce box-shadows, gradients, or glow effects - flatness is the point
- Never use #ffa1f7 for body text, backgrounds, or decorative purposes - it is an action color only
- Never round image corners on project showcases - images must meet the canvas edge
- Never add more than one filled CTA per screen - the system is single-action
- Never use cool blue-grays or pure whites for text - the warm sepia palette is the identity
- Never use icons in the header or footer - plain text links only
- Never reduce section gaps below 104px - the generous whitespace is structural, not optional

Source prompt cues:

Quick Color Reference:
- text: #efe6d8 (Parchment)
- background: #000000 (Obsidian)
- border: #605c56 (Charcoal) / #736e68 (Ash)
- accent: #ffa1f7 (Neon Petal)
- status: #4dff00 (Acid Lime) - availability dot only
- primary action: #ffa1f7 (filled action)

Example Component Prompts:

1. Create a section header: 200px top padding. Left-aligned label 'SELECTED WORK' in Geist Pixel Triangle 30px, #efe6d8, letter-spacing -1px. Right-aligned date range '2015 - 2026' in Geist Mono 13px, #736e68.

2. Create a status row: 8px green circle (#4dff00, 1000px radius) followed by 'Available for work' in Geist 500, 14px, #efe6d8, separated by 8px gap.

3. Create a pill CTA: 40px border-radius, #ffa1f7 background, 12px 24px padding, 'Book an intro call' in Geist 500 13px, #000000 text, no border.

4. Create a footer link row: three text links 'X.com', 'LinkedIn', 'Dribbble' in Geist Mono 400, 13px, #736e68, 24px gap between each, left-aligned.

5. Create a project showcase: full-width image edge-to-edge on #000000 canvas, no border or radius, 104px top padding, caption below in Geist 500 14px #efe6d8.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
