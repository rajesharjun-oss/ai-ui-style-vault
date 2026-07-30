# Framer

Source: [Refero Style](https://styles.refero.design/style/d417b42f-824d-45ba-a02e-cbef3b8ea0d8)
Reference site: [https://framer.com](https://framer.com)
Captured: 2026-07-30
Refero published: 2026-03-20T16:32:24.000Z
Refero modified: 2026-07-03T11:24:26.020Z
Theme: dark
Category: Design

## Style Summary

Explore Framer's dark Design design system: Void #000000, Graphite #111111 colors, sans-serif, GT Walsheim typography, and DESIGN.md for AI agents.

North star: neon gallery in the void

## What To Borrow

- Void `#000000` for Page canvas, nav background, card surfaces, icon fills - the infinite black that swallows all non-essential content
- Graphite `#111111` for Elevated card surfaces one step above the void - large feature cards and modal containers
- Obsidian `#171717` for Mid-tier surface for buttons, secondary cards, UI fills - separates interactive elements from the canvas
- Slate `#242424` for Hover states, input fields, and elevated panels - the brightest neutral before reaching text territory
- Ash `#333333` for Deep fill for inactive backgrounds and structural elements
- Smoke `#666666` for Disabled text, low-emphasis body copy, tertiary strokes
- Fog `#888888` for Borders, dividers, icon strokes - the structural outline color
- Mist `#999999` for Secondary body text, captions, metadata - readable but never competing with headlines
- Pearl `#cccccc` for Light body text for contrast pairs on dark surfaces
- Bone `#ffffff` for Primary headings, body text on dark canvas, button backgrounds - the sole light source
- Electric Blue `#0099ff` for Accent borders, glows, link underlines, badge outlines, active states - the only chromatic punctuation in the entire system
- Deep Current `#00406b` for Dark accent fills and box-shadows paired with Electric Blue - the saturated shadow underneath blue glows
- Midnight Tide `#002238` for Subtle blue-tinted surface washes and shadow tints - keeps the blue accent feeling atmospheric even in flat fills
- Signal Green `#4cd963` for Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color
- Vivid Violet `#0066ff` for Primary action button fill - the only place a solid chromatic button background appears in the interface
- Alert Red `#ff0022` for Red wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color
- Amber `#ffbb00` for Yellow wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color
- Lime `#cbff00` for CSS token hint - secondary accent available in the design system but not actively surfaced in core pages

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- GT Walsheim `--font-gt-walsheim` for Display and heading type - the signature typeface. Aggressively compressed with line-height 0.8-1.1 and tracking -0.04em to -0.05em at 44-68px. This isn't decoration; GT Walsheim's geometric warmth at tight metrics creates the system's voice - confident, compact, slightly futuristic. Substitute: Inter Tight or Space Grotesk Bold for similar geometric presence.
- Inter Variable `--font-inter-variable` for Body, nav, and secondary headings - the workhorse. Inter Variable's variable axis allows smooth weight interpolation. Tracking tightens as size grows: -0.001em at 18px to -0.027em at 22px. The variable version enables the site's fluid micro-animations. Substitute: Inter (Google) is a near-identical fallback.
- Inter `--font-inter` for Static Inter for UI controls, buttons (500/600), and uppercase labels (700 at 9px). Used where variable weight isn't needed. The 20px/600/lh=1.2 heading style with -0.04em tracking provides a compact sub-heading tier below GT Walsheim displays.
- Input Mono `--font-input-mono` for Code snippets, monospace tags, and technical metadata - appears in product UI screenshots and code-context moments. The mono voice contrasts the geometric sans-serif to signal 'this is structural, not prose'.
- JetBrains Mono `--font-jetbrains-mono` for Secondary monospace for code blocks - shares the developer-tool vocabulary with Input Mono but used in longer-form code contexts.
- Inter Medium `--font-inter-medium` for Inter Medium - detected in extracted data but not described by AI

## Avoid

- Don't introduce additional accent colors beyond Electric Blue (#0099ff) and Vivid Violet (#0066ff) - the system is deliberately monochromatic with one accent
- Don't use #ffffff as a background fill for cards - white is reserved for text and primary CTAs, cards stay in the #111-#242424 range
- Don't apply box-shadows to standard cards - depth is communicated through luminance stepping (#000 #111 #171 #242), not elevation
- Don't set body text below 12px - the minimum size protects readability against the dark canvas
- Don't use warm grays or chromatic neutrals - the palette is strictly cool/achromatic in its grays, with blue as the only chromatic direction
- Don't mix font families within a single text block - GT Walsheim for display, Inter for everything else, mono for code only
- Don't use border-radius values outside the defined scale (8, 15, 20, 25, 9999) - every radius in the system maps to a specific component type

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
