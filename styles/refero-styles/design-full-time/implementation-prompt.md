# AI Implementation Prompt

Build a Design Full-Time-inspired interface using this source-derived style bundle.

Reference site: https://designfulltime.com
Theme: dark
Category: Other
North star: black-box cinema with a single warm spotlight

Use these palette anchors:

- Pure Black `#000000` for Page canvas, dominant background - absorbs everything so content and the warm gradient banner can command attention
- Surface Black `#111111` for Card backgrounds, elevated panels, filled neutral button surface - one step off the canvas creates depth without gray noise
- Lifted Charcoal `#252525` for Mid-elevation surfaces, hover states, and subtle card depth - bridges the page black and border tones
- Border Gray `#343434` for Hairline dividers, card outlines, table rules - defines structural edges in a flat world
- Edge Gray `#4d4d4d` for Heavier borders on outlined buttons and grouped control frames
- Muted Text `#888888` for Secondary body text, metadata, timestamps, supporting copy
- Helper Gray `#a0a0a0` for Body text borders and subtle helper text where full white feels too loud
- Pure White `#ffffff` for Primary headings, nav text, button text, logo fill - the only color allowed to compete with the gradient banner
- Amber Glow `#fa3a19` for Promotional banner start - the cool-yellow origin of the warm spotlight gradient (also gradient)
- Ember Orange `#ff8a00` for Supporting palette color for small decorative accents when the core palette needs contrast. Do not promote it to the primary CTA color
- Crimson Heat `#ff8a00` for Supporting palette color for small decorative accents when the core palette needs contrast. Do not promote it to the primary CTA color

Use these typography anchors:

- Inter `--font-inter` for Sole typeface. Inter 700/800 for the wordmark and section headlines (confident, instructor-led); 600 for video titles and nav labels; 400 for body copy and metadata. No display-size font in the system - the brand keeps type compact (capped at 24px) and lets the gradient banner and video thumbnails carry visual weight instead.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 48px.
- Card padding: 16px.
- Element gap: 8px.

Build these component patterns where relevant:

- Top Navigation Bar: Primary site navigation
- Brand Wordmark: Logo / identity
- Promo Banner (Gradient Strip): Conversion / offer highlight
- Promo Gradient Button: Primary conversion CTA on banner
- Outlined Nav Button: Secondary account action
- Video Lesson Card: Course / free lesson entry point
- Video Duration Badge: Thumbnail metadata overlay
- Section Heading: Section title
- Video Title: Lesson card primary label
- Category Label: Lesson card metadata

Do:

- Use #000000 as the page canvas and keep all non-promo content achromatic - let the warm gradient banner be the only chromatic event on the page.
- Apply the linear-gradient(90deg, #ff8a00, #fa3a19) exclusively to the promo CTA button; never use it for nav, icons, or course cards.
- Use Inter 700/800 for all headings and Inter 400/600 for body - never mix in a second typeface family.
- Define card edges with 1px #343434 borders on #111111 surfaces; skip shadows and rely on flat color steps for hierarchy.
- Set video card padding to 16px and maintain an 8px gap between thumbnail, title, and category label inside each card.
- Keep the type scale capped at 24px - let video thumbnails and the gradient banner carry visual scale instead of oversized headlines.
- Use #ffffff for interactive text and headings, #a0a0a0 / #888888 for metadata and secondary copy.

Avoid:

- Don't introduce any blue, green, or purple accent - the brand is a two-tone system (monochrome + warm gradient) and extra hues will dilute the spotlight effect.
- Don't apply the warm gradient to body text, icons, or borders - reserve it for the promo banner surface and its CTA button only.
- Don't use shadows or heavy rounded corners (>=12px); the system is intentionally flat with 4-6px radii and hairline borders.
- Don't set headings above 24px; oversized display type breaks the compact, instructor-led feel.
- Don't use #111111 as a button background for primary actions - that role belongs exclusively to the warm gradient CTA.
- Don't introduce a second typeface, custom display face, or serif - Inter alone carries the brand at every weight.
- Don't place the gradient banner inside cards or repeated lists; it must remain a singular full-width conversion event.

Source prompt cues:

primary action: #111111 (filled action)
Create a Primary Action Button: #111111 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

Example Component Prompts:

1. Promo banner: full-width bar, 4px radius, 1px subtle border, soft amber crimson wash background (12% 10% opacity). Left zone: 'Save 60%' in gradient text (amber #ffc840 crimson #fa3a19, Inter 700/20px). Center zone: white Inter 600/16px text. Right zone: gradient-filled button (90deg, #ff8a00 #fa3a19), white Inter 700/15px label, 6px radius, 8px 16px padding.

2. Video lesson card: #111111 surface, 1px #343434 border, 6px radius, 16px padding. Thumbnail (16:9) fills top, bottom-right duration badge (#000000 80% opacity, 4px radius, Inter 600/13px white). 8px gap to title (Inter 700/16px #ffffff), 4px gap to category (Inter 400/15px #a0a0a0).

3. Outlined nav button: transparent background, 1px #343434 border, 6px radius, 8px 16px padding, Inter 600/15px white label. Used for 'Student Login'.

4. Section heading: left-aligned Inter 700/24px #ffffff, 16px bottom margin, no decoration. Followed by a 4-column equal-width video grid with 16px gaps.

5. Page canvas: #000000 full-bleed background, 1200px max-width centered content container, 48px vertical gap between major sections, no shadows, no alternating bands.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
