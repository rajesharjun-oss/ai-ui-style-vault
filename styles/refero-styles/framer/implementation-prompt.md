# AI Implementation Prompt

Build a Framer-inspired interface using this source-derived style bundle.

Reference site: https://framer.com
Theme: dark
Category: Design
North star: neon gallery in the void

Use these palette anchors:

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

Use these typography anchors:

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- GT Walsheim `--font-gt-walsheim` for Display and heading type - the signature typeface. Aggressively compressed with line-height 0.8-1.1 and tracking -0.04em to -0.05em at 44-68px. This isn't decoration; GT Walsheim's geometric warmth at tight metrics creates the system's voice - confident, compact, slightly futuristic. Substitute: Inter Tight or Space Grotesk Bold for similar geometric presence.
- Inter Variable `--font-inter-variable` for Body, nav, and secondary headings - the workhorse. Inter Variable's variable axis allows smooth weight interpolation. Tracking tightens as size grows: -0.001em at 18px to -0.027em at 22px. The variable version enables the site's fluid micro-animations. Substitute: Inter (Google) is a near-identical fallback.
- Inter `--font-inter` for Static Inter for UI controls, buttons (500/600), and uppercase labels (700 at 9px). Used where variable weight isn't needed. The 20px/600/lh=1.2 heading style with -0.04em tracking provides a compact sub-heading tier below GT Walsheim displays.
- Input Mono `--font-input-mono` for Code snippets, monospace tags, and technical metadata - appears in product UI screenshots and code-context moments. The mono voice contrasts the geometric sans-serif to signal 'this is structural, not prose'.
- JetBrains Mono `--font-jetbrains-mono` for Secondary monospace for code blocks - shares the developer-tool vocabulary with Input Mono but used in longer-form code contexts.
- Inter Medium `--font-inter-medium` for Inter Medium - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 45px.
- Element gap: 10px.

Build these component patterns where relevant:

- Primary Pill Button: Hero CTA - the only action that demands immediate attention
- Ghost Translucent Button: Secondary action with low visual weight
- Solid Filled Button: Standard interactive button
- Dark Surface Button: Tertiary button on dark surfaces
- Large Pill Button: Oversized CTA for landing conversion
- Void Feature Card: Large content card - product showcases, feature highlights
- Graphite Feature Card: Elevated card one step above void
- Obsidian Content Card: Mid-tier card for grouped content
- Padded Showcase Card: Feature card with breathing room
- Blue Accent Border: Active state, highlight border, interactive emphasis
- Electric Glow Shadow: Ambient glow for accent elements
- Community Feed Container: Dark-window chrome for product UI embedding

Do:

- Use GT Walsheim Medium weight 500 at 44-68px for all display headings - never substitute a different geometric sans-serif for display type
- Set display headings with line-height 0.8-1.1 and letter-spacing -0.04em to -0.05em - the compression is signature
- Apply Electric Blue (#0099ff) exclusively as 1px borders, glows, and link accents - never as a filled surface in hero sections
- Use Vivid Violet (#0066ff) only for the primary CTA button background - it is the single filled chromatic button in the system
- Set all buttons and tags to 9999px border-radius - fully pill-shaped controls are non-negotiable
- Use card radii from the 15px 20px 25px scale - match radius to card importance, not to a single global value
- Keep section gaps at 80px and element gaps at 10px - the compact density with generous section breathing is intentional

Avoid:

- Don't introduce additional accent colors beyond Electric Blue (#0099ff) and Vivid Violet (#0066ff) - the system is deliberately monochromatic with one accent
- Don't use #ffffff as a background fill for cards - white is reserved for text and primary CTAs, cards stay in the #111-#242424 range
- Don't apply box-shadows to standard cards - depth is communicated through luminance stepping (#000 #111 #171 #242), not elevation
- Don't set body text below 12px - the minimum size protects readability against the dark canvas
- Don't use warm grays or chromatic neutrals - the palette is strictly cool/achromatic in its grays, with blue as the only chromatic direction
- Don't mix font families within a single text block - GT Walsheim for display, Inter for everything else, mono for code only
- Don't use border-radius values outside the defined scale (8, 15, 20, 25, 9999) - every radius in the system maps to a specific component type

Source prompt cues:

**Quick Color Reference:**
- Text primary: #ffffff
- Text secondary: #999999
- Background (page): #000000
- Surface elevated: #111111
- Border accent: #0099ff
- primary action: #0066ff (filled action)

**3-5 Example Component Prompts:**

1. **Hero Headline**: 68px GT Walsheim Medium, weight 500, line-height 1.0, letter-spacing -3.4px, color #ffffff. Left-aligned on #000000 canvas. Below: a pill button (#000000 fill, #ffffff text, 9999px radius, 10px 14px padding, 12px Inter weight 500).

2. **Section Display**: 54px GT Walsheim Medium, weight 500, line-height 0.8, letter-spacing -2.16px, color #ffffff. 80px section gap above. Left-aligned, max-width 1200px centered container.

3. **Feature Card**: #111111 background, 25px border-radius, 45px horizontal padding, no shadow, no border. Contains 20px Inter weight 600 subheading at -0.8px tracking, then 14px Inter Variable body at #999999.

4. **Blue Accent Badge**: 1px solid #0099ff border, transparent fill, 9999px radius, 6px 12px padding. Text: 12px Inter weight 500, #0099ff color, uppercase. Optional: rgba(0, 153, 255, 0.2) 0px 5px 5px 0px glow shadow.

5. **Primary CTA Button**: #0066ff background, #ffffff text, 8px border-radius (not pill - this is the one filled chromatic button), 10px 14px padding, 12px Inter weight 500. Use only for the single primary conversion action per page.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
