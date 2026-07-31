# AI Implementation Prompt

Build a Adcker-inspired interface using this source-derived style bundle.

Reference site: https://adcker.com
Theme: light
Category: Agency
North star: Giant brutalist poster on warm museum paper

Use these palette anchors:

- Ink Black `#191919` for All text, headlines, borders, link colors - the sole foreground color in the entire system. Near-black rather than pure black adds warmth that harmonizes with the cream canvas
- Bone Canvas `#efedea` for Page background, card surfaces, nav bar - the warm off-white ground that makes the near-black ink read with high contrast (15.1:1 AAA) without feeling harsh or clinical
- Stone Veil `#e3e1de` for Subtle surface variation against Bone Canvas - used sparingly for secondary panels or section backgrounds to create depth without introducing color

Use these typography anchors:

- nhm `--font-nhm` for Primary type system spanning body (16-21px) to extreme display (173-185px). Weight 400 carries both the whisper-quiet metadata and the 185px display headlines - the system trusts the scale to create hierarchy rather than reaching for bold weights. Letter-spacing tightens aggressively to -0.05em at display sizes to prevent the large counters from feeling airy.
- psl `--font-psl` for Mid-scale display for subheadings and section titles. Sits between body text and the extreme display tier, carrying -0.015em tracking for controlled density at smaller display sizes.
- psr `--font-psr` for Body text alternative at 21px with normal tracking - used for longer-form passages where the tighter nhm spacing would feel constrained.
- Kumbh Sans `--font-kumbh-sans` for Alternate display family at extreme sizes, sharing the same -0.05em tracking and tight 0.78-0.80 line-height as nhm. Provides a geometric counterpoint to nhm's neo-grotesque character for typographic variation within display lockups.

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: 1400px.
- Section gap: 200px.
- Card padding: 32px.
- Element gap: 8px.

Build these component patterns where relevant:

- Top Navigation Bar: Minimal site header
- Editorial Display Headline: Hero typographic lockup
- Metadata Label: Small editorial annotation
- Showreel Player: Video showcase container
- Case Study Card: Project portfolio entry
- Text Link: Inline navigation
- Section Divider: Visual section break
- Full-Bleed Image Block: Photography showcase

Do:

- Use display sizes exclusively at 173px or 185px - anything between 70px and 170px breaks the typographic extremes the system is built on
- Maintain line-height 0.78-0.80 for display type to keep the massive headlines from drifting apart vertically
- Set letter-spacing to -0.05em on all display text (nhm and Kumbh Sans tiers) to compensate for the wide counters at extreme sizes
- Use the full 200px section gap between major content blocks - compact spacing here would undermine the editorial gravitas
- Embed photographs inline within display text lockups rather than placing them as separate elements beside the text
- Keep all text weight 400 unless explicitly calling for the nhm 700 weight - the system derives hierarchy from scale, not weight
- Let the Bone Canvas (#efedea) serve as both background and surface - the monochromatic discipline is the point

Avoid:

- Never introduce chromatic colors, brand accents, or semantic state colors - the 0% colorfulness is the system
- Never apply border-radius to any element - all corners are sharp (0px) to preserve the brutalist editorial feel
- Never use shadows, glows, or elevation effects - the system is completely flat
- Never use body text larger than 21px or smaller than 16px - the gap between body and display is intentional and vast
- Never use a centered CTA button with a colored fill - interactive elements are text links with underlines, not buttons
- Never set display type at line-height above 0.85 - the tight leading is what makes 185px text feel like a single sculptural object
- Never overlay text on dark backgrounds to create contrast - invert by using Ink Black (#191919) as a full surface, not as a treatment

Source prompt cues:

Quick Color Reference:
- Canvas/background: #efedea (Bone Canvas)
- Text/headlines: #191919 (Ink Black)
- Borders/dividers: #191919 (Ink Black)
- Accent: none (monochromatic system)
- primary action: no distinct CTA color
- Surface variation: #e3e1de (Stone Veil)

Example Component Prompts:

1. Editorial Display Headline: Center the text 'BUILD SOMETHING' at 185px using nhm 400, color #191919, letter-spacing -9.25px, line-height 0.80, on a #efedea background. Text fills the viewport width.

2. Top Navigation Bar: Place 'Adcker' in nhm 700 at 16px in the top-left corner and 'Menu' in nhm 400 at 16px in the top-right corner. Both in #191919. No background, no border, no padding beyond 4px vertical.

3. Metadata Label: Position a small text label 'Showreel' at 16px nhm 400 in #191919, with 15px padding from the nearest display text element. No background, no border.

4. Case Study Card: Create a section with a project title at 69px psl 400 in #191919 (letter-spacing -1.035px), 32px padding, on a #efedea background. Below it, a caption at 16px nhm 400 in #191919.

5. Full-Bleed Photography: Place a candid portrait photograph edge-to-edge at 0px radius with no border, no shadow, directly on the #efedea canvas. The image should feel warm-toned and natural, not filtered.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
