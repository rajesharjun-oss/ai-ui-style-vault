# AI Implementation Prompt

Build a International Magic-inspired interface using this source-derived style bundle.

Reference site: https://intmagic.com
Theme: dark
Category: Agency
North star: midnight gallery wall - a single spotlight, a piece of work, and a wall of black velvet

Use these palette anchors:

- Void `#0a0a0a` for Page background, primary canvas - the dark field that holds every piece of work
- Chalk `#f7f7f7` for Hairline borders, dividers, input outlines, and card edges on light surfaces. Do not promote it to the primary CTA color
- Ivory `#ebebeb` for Button labels and button borders - marginally warmer than Chalk, used on neutral pill buttons to feel pressed but not clinical
- Ash `#7c7c7c` for Secondary link and body text, subdued dividers - mid-gray for de-emphasized type that still needs to read
- Graphite `#4d4d4d` for Heading borders and low-emphasis heading text - darker mid-gray that recedes behind primary Chalk type
- Smoke `#707070` for Badge text - sits between Ash and Charcoal, calm and unreadable as ornament
- Steel `#616161` for Badge borders - paired with Smoke text for outlined tag affordance
- Charcoal `#585858` for Elevated surface for the single neutral filled button - barely lighter than Void so the button whispers rather than shouts

Use these typography anchors:

- Wand UI Pro `--font-wand-ui-pro` for Sole typeface - used for everything from 96px display headlines down to 10px badge labels. The 475 and 550 weights are the workhorses; 650 is reserved for emphasis. The font is custom but has the personality of a contemporary geometric grotesk with subtle humanist warmth, tight apertures, and a tall x-height.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 640px.
- Section gap: 120px.
- Card padding: 16px.
- Element gap: 12px.

Build these component patterns where relevant:

- Top Bar Navigation: Site-wide header
- Display Headline (Centered): Hero / project title
- Subtitle (Centered, Muted): Supporting label below display
- AD Badge: Project type / category tag
- Subscribe Button (Outlined Ghost): Primary action on content pages
- Subscribe Button (Filled Neutral): Alternative primary action on lighter frames
- Phone / Device Mockup Frame: Hero visual container for video or app work
- Portrait Thumbnail Card: Small creator / contributor tile
- Section Divider (Invisible): Vertical rhythm separator

Do:

- Keep every screen fully achromatic - palette is Void, Chalk, and three mid-grays; no chromatic accents.
- Center all content in a 640px column and let 120px of Void separate every section.
- Use the 24px radius on any container that holds a piece of work (device, video, image), and 9999px radius on any tag, badge, or button.
- Lift featured work with the single ambient shadow `0px 64px 72px 0px rgba(0,0,0,0.25)` - never stack a second tier.
- Set display headlines at 96px / weight 400 / letter-spacing -1.632px; the whisper weight is the brand.
- Use `ordn` and `ss01` font features wherever Wand UI Pro appears - they are part of the voice.
- Treat the top bar as a sentence, not a bar: three words, 11px / 550, no background, no border.

Avoid:

- Don't introduce any hue - no blue, no red, no warm grays with chroma. The page is 0% colorful by design.
- Don't add a filled primary-color CTA. Actions stay ghost (outlined Ivory) or neutral-charcoal.
- Don't use sharp 0-4px corners on device or card surfaces - the 24px radius is what makes the dark canvas feel soft.
- Don't crowd sections. If vertical space between blocks drops below 80px, the void stops working.
- Don't use weights above 650 in Wand UI Pro; the type system caps there and going heavier breaks the quiet voice.
- Don't add secondary shadows, colored shadows, or border-glow effects to lift work - the 64/72/25% ambient shadow is the only elevation.
- Don't left-align hero content. Every headline, subtitle, badge, and CTA in the main column is centered.

Source prompt cues:

Quick Color Reference
- canvas: #0a0a0a
- text: #f7f7f7
- secondary text: #7c7c7c
- border: #f7f7f7 (hairline) or #4d4d4d (low-emphasis)
- badge text: #707070 / badge border: #616161
- primary action: no distinct CTA color

3 Example Component Prompts
1. Centered display headline: 96px Wand UI Pro (use Inter as substitute) weight 400, color #f7f7f7, line-height 1.0, letter-spacing -1.632px, centered in a 640px column on #0a0a0a canvas. Optional 11px / 550 weight AD badge above at letter-spacing +0.25px with 1px #616161 border and 9999px radius.
2. Ghost subscribe button: 15px Wand UI Pro weight 475, color #ebebeb, 1px solid #ebebeb border, 9999px radius, 8px vertical / 20px horizontal padding, transparent background, centered, sitting 24px below the last content block.
3. Phone mockup hero frame: 24px outer radius container, vertical aspect ratio (~9:16), holding a video still, wrapped in the single ambient shadow `0px 64px 72px 0px rgba(0,0,0,0.25)`. Frame is centered in the 640px column with at least 80px of empty Void above and below.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
