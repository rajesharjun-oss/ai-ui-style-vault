# AI Implementation Prompt

Build a until-inspired interface using this source-derived style bundle.

Reference site: https://www.untillabs.com
Theme: light
Category: AI
North star: warm parchment monograph under a single olive tree.

Use these palette anchors:

- Parchment `#f7f3ec` for Page background, card surfaces, nav container - warm off-white that replaces pure white to soften the entire system
- Ink `#121212` for Primary text, all borders, card outlines, nav links - near-black with a whisper of warmth, drives every structural line on the page
- Black `#000000` for Link borders, footer accents, and icon fills - pure black reserved for high-emphasis micro elements
- Paper `#ffffff` for Button fills, elevated surface accents, footer background - pure white used sparingly for contrast punctuation against the cream canvas
- Mist `#bebebe` for Disabled or secondary body text and subtle dividers - sits below the ink line
- Olive Branch `#6c853b` for Heading color and accent borders - the sole chromatic note, an organic olive green that gives the brand its botanical, anti-corporate feel
- Bone `#121c0f` for Deep text on light backgrounds where extra weight is needed - almost-black with a green undertone matching the olive

Use these typography anchors:

- neueHaasDisplay `--font-neuehaasdisplay` for Display and headings - from subhead at 24px to hero at 69px, with tight line-heights (0.90-1.10) and aggressive negative tracking (up to -0.037em) creating a compressed Swiss-editorial feel
- neueHaasText `--font-neuehaastext` for Body copy, nav links, button labels, card text - 14px and 16px with moderate negative tracking (-0.025em at 14px, -0.009em at 16px), reads as a clean grotesque but not clinical
- Geist Mono `--font-geist-mono` for Captions, annotations, code-like labels, scroll prompts - 12-14px with +0.05em tracking on the 12px size, adds a technical/research-lab accent

Use these layout rules:

- Base spacing: 8px.
- Density: compact.
- Page max-width: 1200px.
- Section gap: 48px.
- Card padding: 24px.
- Element gap: 8px.

Build these component patterns where relevant:

- Pill Navigation Bar: Primary site navigation
- Pill Primary Button: Main call-to-action
- Pill Ghost Button: Secondary action
- Hero Display Headline: First-screen editorial headline
- Editorial Image Card: Team / lab photography card
- Feature Image Card Grid: Four-column lab/team showcase
- Recruitment Copy Block: Hiring section text
- Scroll Prompt Caption: Editorial micro-label
- Top Header Strip: Above-nav utility bar
- Full-Bleed Hero Image: First-viewport visual
- Nav Pill Container: Floating navigation capsule
- Borderless Stacked Section: Content block separator

Do:

- Use #f7f3ec as the page background on every screen; never substitute pure white for the main canvas.
- Set all headings in Neue Haas Display with letter-spacing between -0.020em and -0.037em - the negative tracking is the brand's editorial signature.
- Round all interactive elements to 64px (full pill) and all cards to 32px; the softness is non-negotiable.
- Use #6c853b olive only on heading text, heading underlines, and small annotation labels - never as a button fill or large surface.
- Use Geist Mono 12px with +0.05em tracking for bracketed micro-labels like '[ Scroll to discover ]' - these are decorative research-journal accents.
- Keep shadows to the single inset-highlight pattern (rgba(255,255,255,0.1) inset top and bottom + rgba(0,0,0,0.05) 0 3px 17px outer); avoid heavy drop-shadows.
- Maintain 48-96px vertical gaps between major sections; the page breathes like a printed magazine spread.

Avoid:

- Do not use pure black (#000000) for body text - use #121212, which has a slight warmth matching the cream canvas.
- Do not introduce additional chromatic colors; the olive is the only accent and overusing it dilutes the botanical restraint.
- Do not use sharp corners (0-6px radius) on cards, buttons, or images - the rounded language defines the softness.
- Do not place text on tinted overlays over photography; headlines sit directly on images or on the cream canvas.
- Do not set body text below 14px or above 16px; the type scale is deliberately narrow and editorial.
- Do not use filled colored buttons - every CTA is a pill with a 1px #121212 border, either white or ghost.
- Do not use box-shadows heavier than the defined inset/outer combo; the system relies on cream-on-cream layering, not elevation.

Source prompt cues:

Quick Color Reference:
- text: #121212
- background: #f7f3ec
- border: #121212
- accent: #6c853b
- surface (elevated): #ffffff
- primary action: no distinct CTA color

Example Component Prompts:

1. Create a hero section: full-bleed photograph background, no overlay tint. Headline at 69px neueHaasDisplay weight 400, color #ffffff, letter-spacing -2.55px, line-height 0.90, positioned bottom-left. Below the headline, add a 12px Geist Mono caption in white with +0.7px tracking: '[ Scroll to discover ]'.

2. Create a four-column image card grid: each card 32px border-radius, 1px solid #121212 border, 1px inset highlight rgba(255,255,255,0.1). Above each card, a small olive label in 12px Geist Mono: '| 1 |', '| 2 |', etc., color #6c853b. 24px gap between cards, all on #f7f3ec background.

3. Create a floating nav pill: white #ffffff fill, 64px border-radius, 1px solid #121212 border, horizontal padding 24px, vertical padding 8px. Contains two small black dots (8px circles) on the left and a 'Join Us' text button on the right in 14px neueHaasText weight 500, color #121212.

4. Create a recruitment copy block: two-column layout on #f7f3ec. Left column: headline at 39px neueHaasDisplay weight 500, color #121212, letter-spacing -1.17px. Right column: body text at 16px neueHaasText weight 400, color #121212, line-height 1.5. Below left column, a pill button: white fill, 64px radius, 1px #121212 border, padding 8px 16px, label 'Join the team' in 14px neueHaasText weight 500.

5. Create a secondary ghost button: transparent fill, 64px border-radius, 1px solid #121212 border, padding 8px 16px, label in 14px neueHaasText weight 500, color #121212. Sits on the cream canvas.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
