# AI Implementation Prompt

Build a Kinfolk-inspired interface using this source-derived style bundle.

Reference site: https://www.kinfolk.com
Theme: light
Category: Media
North star: Editorial broadsheet on bone-white linen - generous margins, ink-black serif, and a single warm-paper accent for section breaks.

Use these palette anchors:

- Ink Black `#000000` for Primary type, borders, icon strokes, and all hairline rules. The only foreground color in the system
- Bone White `#ffffff` for Primary canvas, card surfaces, and reverse text on dark photo overlays
- Paper Mist `#f4f4f4` for Soft surface elevation for insets, input fields, and section backgrounds that need to step down from pure white without introducing a hue
- Sage Paper `#dbded5` for Warm greenish-gray paper tint used as a section-break wash and full-bleed band. Provides the only chromatic moment in the system without becoming a brand color

Use these typography anchors:

- Kinfolk-Serif-Text `--font-kinfolk-serif-text` for Long-form body copy, captions, and article decks at 20px (lead paragraphs) and 15px (body). Normal letter-spacing lets the text breathe at reading size; the elevated line-height (1.5 at 15px) gives prose an airier, more literary rhythm than typical web body text.
- Kinfolk-Serif-Display `--font-kinfolk-serif-display` for Hero and feature headlines (60px, lh 1.0, tracking -0.025em / -1.5px). The tight tracking on a single 400 weight produces compressed, almost carved letterforms - authority through restraint, not volume. Used sparingly for the largest editorial moments.
- Kinfolk-Serif-Deck `--font-kinfolk-serif-deck` for Section titles, article headlines, and deck/sub-deck lines at 50/32/25px. Same 400-only discipline as the display face but at intermediate optical sizes. Tracking is still negative at the top end (-0.5px at 50px) for that dense editorial feel.
- Kinfolk-Sans `--font-kinfolk-sans` for UI chrome, metadata, category labels, navigation, button text, and small functional text. Tracking opens up dramatically at the small end (0.06em / ~0.78px at 13px) - a common editorial convention that makes all-caps metadata read as labels rather than body. One weight only, with scale doing all the differentiation.
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1400px.
- Section gap: 80px.
- Card padding: 20px.
- Element gap: 20px.

Build these component patterns where relevant:

- Editorial Cover Hero: Issue cover / feature image for the current issue
- Full-Bleed Editorial Photo Section: Immersive lifestyle/editorial photography that anchors a story
- Article Card Grid: 5-up grid of latest stories on the issue landing
- Article Title Block: Feature-story headline beneath the article grid
- Latest Stories Sidebar: Compact list of supplemental links in the lower-right of editorial sections
- Header Bar: Top-level site navigation
- Subscribe CTA Button: Primary conversion in the persistent bottom bar
- Footer Bar: Persistent subscription prompt at the bottom of the viewport
- Category Label: Issue/section tag above article titles
- Cover Link Pair: Read/Buy action beneath a featured cover

Do:

- Set all primary headlines in Kinfolk-Serif-Deck or Kinfolk-Serif-Display at weight 400 only - never bold or medium.
- Reserve #dbded5 for full-bleed section bands; never use it for small surfaces, badges, or icons.
- Use negative letter-spacing at every display size: -0.025em at 60px, -0.01em at 50px, -0.005em at 32px.
- Let full-bleed photography carry visual weight; keep UI chrome to under 10% of the viewport at any scroll position.
- Use 0px border-radius on every card, button, and image - the 2px radius appears only on inline text links.
- Set body line-height to 1.5 at 15px and 1.33 at 20px; tighter line-heights are reserved for display sizes above 32px.
- Reverse type (#ffffff on #000) only inside the persistent footer bar and over full-bleed photography; never on white-canvas cards.

Avoid:

- Do not introduce any chromatic color beyond #dbded5 - the 0% colorfulness is the brand.
- Do not use filled buttons; every action is a text link with a 1px hairline border at most.
- Do not add shadows or elevation to cards - the surface hierarchy is purely typographic and positional.
- Do not use sans-serif for headlines, deck lines, or pull quotes; serif carries the entire editorial voice.
- Do not bold or italicize any of the Kinfolk type families; weight 400 is the only registered weight.
- Do not mix the #f4f4f4 mist and #dbded5 sage in adjacent surfaces - they read as conflicting neutrals.
- Do not use tracking above 0.06em on any text size; wide tracking is a 13px-and-below convention only.

Source prompt cues:

**Quick Color Reference**
- text: #000000 (Ink Black)
- background: #ffffff (Bone White)
- border: #000000 1px hairline
- accent: #dbded5 (Sage Paper) - section bands only
- reverse text: #ffffff on #000000 (footer, photo overlays)
- primary action: no distinct CTA color

**3 Example Component Prompts**

1. *Build a feature headline block on white:* Canvas #ffffff, no border, no shadow. Eyebrow line in Kinfolk-Sans 25px, weight 400, #000000, 0.25px letter-spacing. Main title in Kinfolk-Serif-Deck 50px, weight 400, line-height 1.04, letter-spacing -0.5px, #000000, centred. Subtitle in Kinfolk-Serif-Deck 32px, weight 400, line-height 1.16, letter-spacing -0.16px, #000000, centred. 60px vertical gap between each line.

2. *Build a full-bleed editorial photo section:* Edge-to-edge image at 100vw, 0px radius, no border. Overlay text anchored to the lower-left with 32px page padding. Headline in Kinfolk-Serif-Deck 50px, weight 400, line-height 1.04, letter-spacing -0.5px, #ffffff. Category label above the headline in Kinfolk-Sans 13px, #ffffff, letter-spacing 0.78px, sentence-case.

3. *Build an article card:* No card background, no border, no shadow. Top: full-column-width image with 0px radius. 20px gap below image. Category label in Kinfolk-Sans 13px, #000000, letter-spacing 0.78px, then 8px gap, then headline in Kinfolk-Sans 16px, weight 400, #000000, then 10px gap, then excerpt in Kinfolk-Serif-Text 15px, line-height 1.5, #000000. Card sits in a 5-column grid with 20px column gaps.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
