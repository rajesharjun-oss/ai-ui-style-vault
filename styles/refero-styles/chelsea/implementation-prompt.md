# AI Implementation Prompt

Build a CHELSEA-inspired interface using this source-derived style bundle.

Reference site: https://www.chelsea.com
Theme: dark
Category: Agency
North star: Black-box cinema with a single blue spotlight - the roster plays, the chrome disappears.

Use these palette anchors:

- Void Black `#000000` for Page canvas, all section backgrounds, negative space - the floor everything sits on
- Spotlight Blue `#4490ff` for Primary action, interactive links, roster name listings, focal dot indicator, highlighted borders - the only chromatic voice in an otherwise monochrome system
- Carbon Slate `#1f2937` for Headings, heavy borders, structural borders on dark surfaces - near-black with a slight cool cast for separation from the pure black canvas
- Bone White `#f4efe9` for Warm off-white for text and subtle borders - softer than pure white, evoking film stock and gallery walls against the black canvas
- Pure White `#ffffff` for Maximum-contrast text and dividers when absolute clarity is needed over photography or dark media
- Ash Gray `#e5e7eb` for Light-mode surfaces, neutral borders on cards or panels, secondary dividers - provides a paper-like counterpoint when a section lifts off the black canvas

Use these typography anchors:

- Neue Haas Unica Pro `--font-neue-haas-unica-pro` for All UI and content type - nav labels at 14px, body at 16px, section headings at 32px, display at 48px

Use these layout rules:

- Base spacing: 8px.
- Density: compact.
- Page max-width: .
- Section gap: 96px.
- Card padding: 16px.
- Element gap: 8px.

Build these component patterns where relevant:

- Cinema-Full-Bleed Media Frame: Hero and section media containers
- Thin Top Navigation Bar: Primary site navigation
- Focal Dot Indicator: Brand punctuation and active-state marker
- Pill Button / Pill Link: All interactive controls
- Roster Name Listing: Talent directory display
- Wordmark Lockup: Brand identity stamp
- Hairline Divider: Section separation
- Credit Caption: Metadata under media

Do:

- Use #4490ff as the only chromatic color in the system - every link, every accent, every focal dot uses it
- Set all interactive elements to 9999px border-radius for the pill shape that defines the brand
- Keep the canvas pure #000000; never introduce a card surface, a gray panel, or a light section mid-page
- Let media bleed edge-to-edge with zero margin, zero radius, and zero frame
- Use Neue Haas Unica Pro weight 400 for body and weight 700 only for the wordmark and button labels
- Set headlines and body at tight line-heights (1.0-1.15) to maintain the credit-roll density
- Use 8px for element gaps and 16px for component padding; jump to 96px between major sections

Avoid:

- Do not introduce drop shadows, elevation layers, or card containers - the system is flat by design
- Do not add a second accent color or any warm tone; the palette is black + white + one blue
- Do not round images or media frames - they must be sharp rectangles bleeding to the viewport edge
- Do not use #0000ee or browser-default link blue; links must be #4490ff
- Do not add a visible logo block, nav background, or header bar - the nav is text floating on black
- Do not set body type above 1.5 line-height; the credit-roll feel depends on tight leading
- Do not introduce semantic colors (green/yellow/red) for status - the system has no UI states to encode

Source prompt cues:

primary action: #4490ff (filled action)
Create a Primary Action Button: #4490ff background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
QUICK COLOR REFERENCE
- Canvas/background: #000000
- Primary action / accent: #4490ff (pill buttons, links, focal dot, roster names)
- Body text on canvas: #ffffff
- Warm text/border: #f4efe9
- Heavy border / structural: #1f2937
- Light surface (rare): #e5e7eb

EXAMPLE COMPONENT PROMPTS

1. Full-bleed hero section: pure #000000 canvas, top nav in 14px Neue Haas Unica Pro weight 400 #ffffff evenly spaced across the viewport (Roster, Latest, Team, Collaborators) with a 1px #1f2937 hairline beneath. A 12px #4490ff solid circle sits inline at the far left of the nav. Main visual is a full-viewport photograph bleeding to all four edges with zero radius. Wordmark 'CHELSEA' stacked in three lines (CH / EL / SEA.) in 48px Neue Haas Unica Pro weight 700 #ffffff, bottom-left, 32px inset.

2. Pill link button: 1px #4490ff border, transparent fill, 16px horizontal / 8px vertical padding, 9999px border-radius, 14px Neue Haas Unica Pro weight 700 #4490ff text. No shadow, no hover state change beyond opacity.

3. Roster name listing: two-column layout on #000000. Left column: small 12px Neue Haas Unica Pro weight 700 #4490ff region labels (US, UK), 16px left padding. Right column: continuous block of names in 32px Neue Haas Unica Pro weight 400 #4490ff, line-height 1.12, separated by periods and spaces, no bullets or dividers.

4. Caption over media: 12px Neue Haas Unica Pro weight 400 #f4efe9, positioned 16px from the bottom-left corner of a full-bleed media frame, no background plate.

5. Section transition: from one full-bleed media screen to the next, separated by 96px of pure #000000 void with no divider, no label, no indicator - the gap itself is the transition.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
