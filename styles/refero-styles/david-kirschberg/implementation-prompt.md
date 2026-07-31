# AI Implementation Prompt

Build a David Kirschberg-inspired interface using this source-derived style bundle.

Reference site: https://kirschberg.co.nz
Theme: dark
Category: Agency
North star: midnight gallery wall - a darkened room where spotlit work is the only color, and the frame around it is intentionally invisible.

Use these palette anchors:

- Obsidian `#181818` for Page canvas, primary background - the dominant surface that recedes so work thumbnails advance
- Graphite `#262626` for Elevated surface, card thumbnail backgrounds, and content containers that need to sit one level above the page
- Bone `#fafafa` for Primary text, hero headlines, card titles - near-white that reads as soft rather than clinical against the dark canvas
- Ash `#a3a3a3` for Muted secondary text, subtitles, card descriptions - one step quieter than primary text for hierarchy without color

Use these typography anchors:

- Inter `--font-inter` for All body text, subtitles, card titles, UI labels, navigation - single weight (400) across every context, relying on size and color contrast rather than weight shifts for hierarchy
- twkLausanne `--font-twklausanne` for Sole display face for the hero headline - a custom typeface with tight tracking and unusually compressed line-height that gives the 32px headline editorial gravitas without bold weight. The -0.04em letter-spacing is aggressive for body size but measured for display, pulling characters close enough to read as a unified mark rather than individual letters

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: .
- Section gap: 24px.
- Card padding: 0px.
- Element gap: 8px.

Build these component patterns where relevant:

- Navigation Pill: Floating top navigation
- Hero Headline: Page-level statement
- Hero Subtitle: Contextual description below headline
- Project Card Thumbnail (Dark): Work preview for projects with dark or photographic content
- Project Card Thumbnail (Elevated): Work preview for app/UI projects needing visible surface separation
- Card Title with Arrow Link: Project name and navigation indicator
- Card Description: One-line project summary
- Horizontal Scroll Gallery: Full-bleed project showcase
- Card Stack: Thumbnail + meta group

Do:

- Use #181818 as the sole page background - never introduce lighter or darker canvas variants
- Use 24px border-radius for all card-shaped surfaces; use 16px for the navigation pill only
- Use twkLausanne at exactly 32px with -1.28px letter-spacing for headlines; never use this typeface for body text
- Use Inter weight 400 for all body, UI, and label text - never introduce weight 500, 600, or 700
- Keep all spacing on the 4px grid; use 8px as the default element gap
- Let project artwork and identity work provide all color on the page - the interface itself stays achromatic
- Center the hero text block in the viewport and float the nav as a centered pill, not a full-width bar

Avoid:

- Never add drop shadows, inner shadows, or box-shadows to any element - depth comes from surface color contrast only
- Never introduce accent colors, brand colors, or saturated hues into the UI chrome - the palette is locked to four neutrals
- Never use font weights other than 400 - hierarchy is built through size and color (Bone vs Ash), not weight
- Never use sharp corners on containers - all surfaces are rounded (16px or 24px)
- Never stack project cards in a multi-row grid - the gallery is a single horizontal scroll row only
- Never add gradients, textures, patterns, or decorative backgrounds to the interface
- Never use letter-spacing wider than -0.009em on body text - the slight tightening is part of the voice

Source prompt cues:

**Quick Color Reference**
- text: #fafafa (primary), #a3a3a3 (muted)
- background: #181818 (page), #262626 (elevated)
- border: #fafafa (neutral action border) or #a3a3a3 (subtle)
- accent: none observed
- primary action: no distinct CTA color

**Example Component Prompts**

1. *Build the hero section*: Dark canvas at #181818. Centered headline in twkLausanne weight 400 at 32px, color #fafafa, letter-spacing -1.28px, line-height 1.10. Below it, a subtitle in Inter weight 400 at 17px, color #a3a3a3, line-height 1.29, constrained to ~560px width and centered. 24px vertical gap between headline and subtitle.

2. *Build the navigation pill*: A centered floating bar with 16px border-radius, dark background (#262626 or #181818 with subtle border), padding ~8px 16px. Contains the word "Kirschberg" in Inter weight 400 at 16px #fafafa, and a hamburger icon (three horizontal lines) on the right side. Positioned at top center with ~24px margin from viewport edge.

3. *Build a project card*: 24px border-radius thumbnail filled with #262626 (elevated variant) or #181818 (flat variant), dimensions roughly 400x500px. Below the thumbnail, the project title in Inter 400 at 16px #fafafa followed by a arrow character. Below that, description text in Inter 400 at 16px #a3a3a3. 8px gap between thumbnail and title, 4px between title and description.

4. *Build the horizontal gallery section*: Full-bleed row of project cards, no left/right page padding. Cards arranged in a single horizontal flex row with 8px column gap. The section scrolls horizontally on overflow. No section header, no background change from the page canvas.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
