# AI Implementation Prompt

Build a Eat Real Food-inspired interface using this source-derived style bundle.

Reference site: https://realfood.gov
Theme: light
Category: Other
North star: government health brief on cream parchment

Use these palette anchors:

- Press Ink `#110000` for Primary text, dark hero surfaces, filled pill buttons, navigation dots - near-black with a warm undertone replaces the cold #000000 to keep the palette feeling printed rather than digital
- Aged Parchment `#fdfbee` for Page canvas, body text on dark surfaces, filled button backgrounds - the warm off-white that gives the entire site its paper-like quality
- Newsprint White `#ffffff` for Card surfaces, elevated panels, button text on dark fills
- Wheat Field `#f3f0d6` for Accent surface, secondary button fill, soft highlight wash - a desaturated straw tone that sits between parchment and olive
- Fog `#e5e5e5` for Hairline borders, dividers, card edges - the structural neutral that defines component boundaries at 1px weight
- Dusty Brick `#8d7d7d` for Muted secondary text, small labels - warm gray-brown that recedes without going cold
- Ash `#bebcb3` for Subtle image borders, soft shadow base - warm gray for non-critical structural lines
- Stone `#d2d0c6` for Card shadow base tone, subtle elevation warmth
- Alert Red `#d50000` for Data emphasis blocks, statistics backgrounds, alarm callouts - the only chromatic color in the system, reserved for moments when numbers must cut through the editorial calm

Use these typography anchors:

- Die Grotesk D `--font-die-grotesk-d` for Display and heading - weight 700 only, the single heaviest voice in the system. Used at enormous sizes (96-170px) with extremely tight line-heights (0.84-0.96) that make headlines stack into solid editorial blocks. This is the voice that shouts.
- Die Grotesk B `--font-die-grotesk-b` for Mid-scale headings and emphasized body - the bridge between display and text. Slight negative tracking (-0.019em) tightens medium sizes without making them feel clinical.
- Die Grotesk A `--font-die-grotesk-a` for Body text, navigation, buttons, links, lists, cards - the workhorse. Negative tracking (-0.02em to -0.03em) at body sizes keeps the grotesque feeling sharp. Weight 600 is available for inline emphasis.
- Geist Mono `--font-geist-mono` for Monospaced labels, section markers, micro-copy - the only monospace voice. Wide tracking (+0.06em) gives it a typewriter/telegraph quality that signals 'official data' or 'system label'.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 24px.

Build these component patterns where relevant:

- Dark Hero Band: Opening section with massive headline
- Filled Pill Button: Primary action
- Outlined Pill Button: Secondary action
- Video Play Trigger: Embedded video launch
- Statistics Data Block: Health data emphasis
- Section Label Tag: Category or section identifier
- Government Banner: Official site identifier
- Navigation Pill: Top navigation item
- Card with Soft Shadow: Content grouping panel
- Section Progress Dots: Page-level section indicator
- Image Container: Media wrapper

Do:

- Use the cream canvas #fdfbee as the default page background for all body content
- Reserve #d50000 exclusively for statistics, data emphasis, and alarm-level callouts - never for decoration or branding
- Use Die Grotesk D weight 700 at 96px or larger for hero and section-opening headlines with line-height at or below 0.96
- Apply 40px border-radius to all buttons and interactive pills to maintain the soft, rounded system voice
- Use Geist Mono with +0.06em tracking for labels, tags, and machine-stamped metadata
- Apply the double-layer card shadow (10px/40px + 20px/60px) to any elevated white surface that needs to separate from the cream canvas
- Keep body text at 16-21px Die Grotesk A weight 400 with -0.02em to -0.03em tracking

Avoid:

- Don't introduce additional chromatic colors - the palette is Press Ink, parchment neutrals, and one Alarm Red
- Don't use #000000 for body text or backgrounds - always use the warmer #110000
- Don't apply Alert Red (#d50000) to buttons, links, or navigation - it is for data blocks only
- Don't use sharp corners (0-4px radius) on buttons or cards - the system is defined by its pill and rounded softness
- Don't set display headlines at standard line-height (1.2+) - tight stacking (0.84-0.96) is the signature
- Don't use heavy drop shadows on dark sections - the near-black surfaces should feel flat and printed, not elevated
- Don't use photography for decorative atmosphere - imagery should be content-bearing (data, video, diagrams) or absent

Source prompt cues:

primary action: #110000 (filled action)
Create a Primary Action Button: #110000 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
**Quick Color Reference**
- Canvas: #fdfbee
- Card surface: #ffffff
- Primary text / dark surface: #110000
- Accent surface: #f3f0d6
- Hairline border: #e5e5e5
- Data emphasis: #d50000

**3-5 Example Component Prompts**
1. Create a dark hero section: #110000 full-width background. Headline 'Real Food Wins' at 170px Die Grotesk D weight 700, #fdfbee color, line-height 0.84, centered. Subtitle at 21px Die Grotesk A weight 400, #fdfbee, max-width 600px, centered below.
2. Create a statistics grid: 3-column layout, 80px section gap above. Each block is solid #d50000 with no border or radius. Percentage at 155px Die Grotesk D weight 700, #ffffff, top-left. Description at 16px Die Grotesk A weight 400, #ffffff, below the percentage.
3. Create a filled pill button: #fdfbee background, #110000 text, 40px border-radius, 18px 24px padding, 14px Die Grotesk A weight 500, no shadow, no border.
4. Create a section label tag: #110000 background, #ffffff text in Geist Mono 12px weight 400 with 0.72px letter-spacing, 6px 16px padding, 100px border-radius.
5. Create an elevated content card: #ffffff background, 16px border-radius, 24px padding, box-shadow rgba(0,0,0,0.1) 0px 10px 40px, rgba(0,0,0,0.1) 0px 20px 60px -10px. Heading at 33px Die Grotesk B weight 700 #110000. Body at 16px Die Grotesk A weight 400 #110000.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
