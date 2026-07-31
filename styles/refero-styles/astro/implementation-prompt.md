# AI Implementation Prompt

Build a Astro-inspired interface using this source-derived style bundle.

Reference site: https://astro.build
Theme: dark
Category: Dev Tools
North star: Deep space mission control with a single purple nebula glow

Use these palette anchors:

- Void Canvas `#1f232e` for Primary page background - the base layer for hero, sections, and footer. Slight cool-blue undertone, never pure black, so colored elements feel like they're floating in space rather than printed on paper
- Abyss `#0c0f19` for Deeper surface level for elevated cards, code blocks, and inset wells. One step darker than the canvas to create depth without using shadows
- Singularity `#060913` for Darkest surface for terminal windows, CLI boxes, and high-contrast containers. Almost pure black with a blue whisper
- Carbon `#17191e` for Mid-elevation card surface, sitting between canvas and abyss. Used for theme preview tiles and nested cards
- Lunar White `#f2f6fa` for Primary text and high-contrast foreground. The slightly cool tint keeps it from feeling clinical against the dark canvas
- Platinum `#e5e7eb` for Secondary text, icon strokes, and light dividers. Most-used achromatic token for hairline borders and muted foregrounds
- Mist `#bfc1c9` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color
- Steel `#858b98` for Muted body text and subdued descriptions. The default for paragraphs that should recede behind headlines
- Gunmetal `#545864` for Hairline borders and dividers on the dark canvas. Low contrast on purpose - structural, not decorative
- Aurora Mint `#4bf3c8` for Teal supporting accent for decorative details and low-frequency emphasis
- Plasma Blue `#54b9ff` for Blue supporting accent for decorative details and low-frequency emphasis
- Ultraviolet `#acafff` for Code keywords, violet link variant, and decorative highlight. A desaturated violet that complements the nebula gradient without competing
- Electric Cyan `#00daef` for Secondary syntax token - reserved for specific code contexts and rare accent strokes
- Amber `#ffd493` for Yellow supporting accent for decorative details and low-frequency emphasis
- Signal Blue `#61dafb` for Decorative dot and badge accent - used for version pills and notification indicators

Use these typography anchors:

- ui-sans-serif `--font-ui-sans-serif` for Body and UI text - system stack fallback. Weight 400 for body copy, 500/600 for button labels and nav, 700 for subheadings. Line-height 1.65 at 14px keeps dense UI readable without feeling airy.
- Obviously `--font-obviously` for Display and headline face - the custom workhorse. Weight 300/400 used for the largest headlines, 700 for the hero. The cv09 and salt alternates give it a distinctive wide, slightly retro character; ss06 and ss11 add quirky details. No web-safe substitute captures the feel - Inter Black or Space Grotesk Bold approximate it.
- ui-monospace `--font-ui-monospace` for Code blocks, terminal commands, and inline code. Fixed 14px with generous 1.65 line-height for readability of multi-line snippets.
- MDIO `--font-mdio` for Icon and badge face - used at 12-16px with widened tracking (0.0250em) for small labels and version chips. The slight letter-spacing and geometric forms give badges a technical, instrument-panel feel.
- Inter `--font-inter` for Inter - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 16px.

Build these component patterns where relevant:

- Primary Pill Button: Main call-to-action (e.g., 'Get Started')
- Terminal Command Box: CLI install command display
- Version Badge: Release announcement pill (e.g., 'Astro 6.1')
- Feature Icon Circle: Icon container in feature columns
- Theme Preview Card: Showcase tile for theme marketplace
- Filter Tab Pill: Category filter for grids (e.g., 'Trending', 'E-Commerce')
- Logo Cloud Item: Customer/partner logo display
- Section Header: Eyebrow label + headline + description block
- Navigation Bar: Top-level site navigation
- Hero Gradient Backdrop: Atmospheric background glow behind hero content
- Stats Bar: Performance metric display (e.g., '% of real-world sites with good Core Web Vitals')

Do:

- Use 9999px radius for all interactive elements (buttons, tabs, badges, chips)
- Set the primary CTA to white background (#ffffff) with dark text (#1f232e) - inversion is the system's signature action pattern
- Use the nebula gradient (linear-gradient(83.21deg, #3245ff, #b845ed)) only for hero atmospheric backdrops and stat bars - never for buttons or cards
- Set section eyebrows (14px weight 600) in chromatic accent colors (#4bf3c8, #acafff, #54b9ff) to create the only color punctuation in each section
- Use Obviously at weight 300-400 for headlines to keep the voice whisper-confident rather than shouty
- Maintain 4px base unit for all spacing - element gaps at 8px or 16px, section gaps at 80px
- Place colored borders (1px) on circular icon containers in feature columns using Aurora Mint, Plasma Blue, or Amber

Avoid:

- Don't use drop shadows for elevation - the system relies on 1px borders in slightly lighter dark shades
- Don't apply the nebula gradient to text - it destroys legibility against the dark canvas
- Don't use chromatic colors for large background fills - they break the cosmic void atmosphere
- Don't use radius values between 12px and 16px on cards - the system snaps to 8px, 12px, or 16px
- Don't set body text below 14px or above 18px - the type scale is tight to maintain the instrument-panel density
- Don't use obviously > 700 for headlines - the weight 300-400 range is the signature restraint
- Don't add decorative icons inside buttons - pills should be text-only or text + chevron

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
