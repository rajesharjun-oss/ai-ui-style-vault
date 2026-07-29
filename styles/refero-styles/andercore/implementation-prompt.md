# AI Implementation Prompt

Build a Andercore-inspired interface using this source-derived style bundle.

Reference site: https://www.andercore.com
Theme: dark
Category: SaaS
North star: Steel blueprint at midnight

Use these palette anchors:

- Signal Red `#e32735` for Red action color for filled buttons, selected navigation states, and focused conversion moments
- Carbon `#0b0405` for Primary section background, full-bleed dark canvases, secondary button fill
- Graphite `#150e0f` for Alternate near-black surface for cards and elevated panels on dark sections
- Steel `#382e30` for Hairline borders on dark surfaces, card edges, table dividers, UI mockup outlines
- Slate `#858182` for Secondary text, badge borders, badge labels, muted helper copy
- Chalk `#ffffff` for Primary text on dark, nav and hero overlay type, inverted button text, light section backgrounds
- Foil `#000000` for SVG icon fills, decorative vector detail

Use these typography anchors:

- Archivo `--font-archivo` for All interface type - headlines (40/56px, weight 500), subheads (24px, weight 500), body and UI (14/16px, weight 400), nav links (12/14px). The geometric grotesque with tight -0.02em tracking gives industrial precision; weight 500 (not 700) for display type keeps the system restrained rather than shouty.
- Space Mono `--font-space-mono` for Badge labels, step counters ('01', '02', '03'), industrial tag stamps - the monospace face signals instrumentation and serial-number precision, contrasting Archivo's proportional geometry

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 32px.
- Element gap: 24px.

Build these component patterns where relevant:

- Primary CTA Button (Red Filled): The single high-priority action on any surface
- Ghost/Dark Button: Secondary action when a primary red CTA is present
- Navigation Header: Top-level site navigation and authentication
- Industrial Badge / Tag: Category labels, section eyebrows, status stamps
- Step Progress Indicator: Multi-step process navigation (Request Quote Track'n'Trace)
- Feature Card with UI Mockup: Three-column challenge/solution display
- Dark Content Section: Primary content blocks after the hero
- Chat Interface Card: Product walkthrough visualization
- Hero with Photographic Overlay: Above-the-fold brand statement
- Connector Line / Accent Divider: Visual flow between cards or sections
- Eyebrow / Section Label: Tiny uppercase or tracked label above section headings

Do:

- Use Signal Red #e32735 exclusively for the single primary action per surface - never as a decorative or background fill
- Set all corners to 4px radius - no exceptions, no pill shapes, no zero-radius hard edges
- Separate dark sections with 80px vertical padding and rely on background-value shift rather than dividers or shadows
- Use Archivo 500 (not 700) for headings 40px and above to keep weight restrained and consistent
- Apply -0.02em letter-spacing to all Archivo type at all sizes for tight industrial density
- Stamp step numbers, serial codes, and technical labels in Space Mono 12px - never Archivo for these
- Define card and panel edges with 1px #382e30 borders on dark, never with box-shadow or background tint shifts

Avoid:

- Don't introduce drop shadows, glows, or blur-based elevation - structure is line-based only
- Don't use #e32735 for body text, icons, or secondary UI - it's an action color, rationed
- Don't round corners beyond 4px - no 8px, 12px, 16px, or pill radii anywhere
- Don't set headings in bold (700+); weight 500 Archivo at 40-56px is the maximum voice
- Don't alternate between light and dark sections within a single content flow - the page is dark-dominant after the hero
- Don't use Archivo for numeric step counters, product codes, or instrumentation labels - those are Space Mono territory
- Don't add gradient fills to buttons or cards - the one gradient in the system (white red) is reserved for the hero-to-content transition

Source prompt cues:

**Quick Color Reference**
- text: #ffffff (on dark) / #0b0405 (on light)
- background: #0b0405 (dark sections) / #ffffff (nav)
- border: #382e30 (on dark) / #858182 (badges)
- accent: #e32735 (Signal Red)
- muted text: #858182 (Slate)
- primary action: #e32735 (filled action)

**3-5 Example Component Prompts**

1. *Create a dark hero section*: #0b0405 full-bleed background, 80px vertical padding. Display headline at 56px Archivo weight 500, #ffffff, letter-spacing -1.12px, line-height 1.10. Subtext at 16px Archivo weight 400, #858182. Primary CTA: #e32735 fill, white text 14px Archivo weight 500, 12px 24px padding, 4px radius. Ghost button beside it: #150e0f fill, 1px #382e30 border, white text, same padding and radius.

2. *Create a three-column feature row*: #0b0405 background, 32px between columns. Each card: 1px #382e30 border, 32px padding, 4px radius. Eyebrow badge above: Space Mono 12px, #858182 text, 1px #858182 border, 8px 12px padding. Card heading at 24px Archivo weight 500, #ffffff. Body at 14px Archivo weight 400, #858182.

3. *Create a step progress indicator*: horizontal row on #0b0405. Three steps labeled 'Request', 'Quote', 'Track'n'Trace' in Archivo 14px. Active step: #e32735 text with a 2px #e32735 underline bar. Inactive: #858182 text, no underline. Step numbers '01', '02', '03' in Space Mono 12px #858182, right-aligned.

4. *Create a dark content section*: #0b0405 background, max-width 1200px centered, 80px vertical padding. Section heading at 40px Archivo weight 500, #ffffff, -0.80px letter-spacing. Body paragraph at 16px Archivo weight 400, #858182. Red accent CTA button top-right: #e32735 fill, white 'Get access now' text, 12px 24px padding, 4px radius.

5. *Create an industrial badge/tag*: transparent fill, 1px #858182 border, Space Mono 12px text in #858182, padding 8px 12px, 4px radius. Used as section eyebrows above headings.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
