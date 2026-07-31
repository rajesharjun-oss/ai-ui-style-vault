# Astro

Source: [Refero Style](https://styles.refero.design/style/e8c604cc-1c8d-42a3-aeca-fcfc25e70344)
Reference site: [https://astro.build](https://astro.build)
Captured: 2026-07-31
Refero published: 2026-01-26T19:37:08.000Z
Refero modified: 2026-06-05T09:10:47.643Z
Theme: dark
Category: Dev Tools

## Style Summary

Explore Astro's dark Dev Tools design system: Void Canvas #1f232e, Abyss #0c0f19 colors, ui-sans-serif, Obviously typography, and DESIGN.md for AI agents.

North star: Deep space mission control with a single purple nebula glow

## What To Borrow

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

- ui-sans-serif `--font-ui-sans-serif` for Body and UI text - system stack fallback. Weight 400 for body copy, 500/600 for button labels and nav, 700 for subheadings. Line-height 1.65 at 14px keeps dense UI readable without feeling airy.
- Obviously `--font-obviously` for Display and headline face - the custom workhorse. Weight 300/400 used for the largest headlines, 700 for the hero. The cv09 and salt alternates give it a distinctive wide, slightly retro character; ss06 and ss11 add quirky details. No web-safe substitute captures the feel - Inter Black or Space Grotesk Bold approximate it.
- ui-monospace `--font-ui-monospace` for Code blocks, terminal commands, and inline code. Fixed 14px with generous 1.65 line-height for readability of multi-line snippets.
- MDIO `--font-mdio` for Icon and badge face - used at 12-16px with widened tracking (0.0250em) for small labels and version chips. The slight letter-spacing and geometric forms give badges a technical, instrument-panel feel.
- Inter `--font-inter` for Inter - detected in extracted data but not described by AI

## Avoid

- Don't use drop shadows for elevation - the system relies on 1px borders in slightly lighter dark shades
- Don't apply the nebula gradient to text - it destroys legibility against the dark canvas
- Don't use chromatic colors for large background fills - they break the cosmic void atmosphere
- Don't use radius values between 12px and 16px on cards - the system snaps to 8px, 12px, or 16px
- Don't set body text below 14px or above 18px - the type scale is tight to maintain the instrument-panel density
- Don't use obviously > 700 for headlines - the weight 300-400 range is the signature restraint
- Don't add decorative icons inside buttons - pills should be text-only or text + chevron

## Bundle Contents

- [DESIGN.md](DESIGN.md): full source-derived implementation reference.
- [implementation-prompt.md](implementation-prompt.md): ready-to-paste prompt for an AI builder.
- [style.json](style.json): structured style metadata and token summary.
- [tokens/colors.md](tokens/colors.md): palette and surface rules.
- [tokens/typography.md](tokens/typography.md): type scale and font rules.
- [tokens/spacing-shape.md](tokens/spacing-shape.md): spacing and radius rules.
- [tokens/components.md](tokens/components.md): component recipes.
- [tokens/guidelines.md](tokens/guidelines.md): do and do-not guidance.
- [tokens/layout-imagery.md](tokens/layout-imagery.md): layout and imagery direction.
- [code/css-variables.css](code/css-variables.css): CSS variable starter.
- [code/tailwind-v4.css](code/tailwind-v4.css): Tailwind v4 token starter.
- [code/design-tokens.json](code/design-tokens.json): portable token JSON.
- [screenshots/README.md](screenshots/README.md): source media references.
