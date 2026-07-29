# AI Implementation Prompt

Build a Apollo-inspired interface using this source-derived style bundle.

Reference site: https://apolloworkspace.com
Theme: light
Category: Other
North star: Warm brick atelier at golden hour

Use these palette anchors:

- Espresso Bark `#3c261c` for Primary text, navigation background, structural borders - a warm near-black that anchors every screen without the harshness of pure #000000
- Terracotta Ember `#e97451` for Primary action borders, active nav state, decorative accents - rationed to moments of intent, never used as a large surface fill
- Iris Ink `#4a43dd` for Decorative display headings, logo monogram stroke - a vivid violet that breaks the warm palette for brand-voice headlines only
- Honey Parchment `#f7efc5` for Subtle highlight washes, eyebrow label backgrounds, warm text tint - a muted yellow that warms the cream canvas without competing with terracotta
- Warm Linen `#f9f8f0` for Page canvas, content section backgrounds - the dominant surface, never pure white, always slightly cream
- Ash Mist `#dddedf` for Hairline borders, dividers, card edges - the most-used color on the site (1,300+ occurrences), creates the cool rule-lines that structure every layout
- Blush Cream `#fcede8` for Warm tinted surface for hover states and soft callout blocks - a peach wash that warms the cream canvas
- Lilac Mist `#e4e3f2` for Cool surface accent for secondary panels - a lavender-tinted gray that introduces gentle contrast against the warm cream
- Carbon `#000000` for True black used sparingly for image fills and footer text - Espresso Bark handles all structural dark needs

Use these typography anchors:

- MonaSans `--font-monasans` for Body text, navigation, buttons, section headings, UI labels - the workhorse sans-serif. Uppercase instances at 0.07-0.1em tracking are signature; the wide tracking on 12-14px labels reads like a museum placard, not a UI label.
- paradigm-pro `--font-paradigm-pro` for Display headings and hero text only - a whisper-thin custom serif at weight 300. The ultra-light weight is anti-convention: most editorial sites use 400-500 serifs for headlines, but this 300 creates authority through restraint. Tight line-height (0.95) lets the letters interlock like a logotype.

Use these layout rules:

- Base spacing: .
- Density: spacious.
- Page max-width: 1200px.
- Section gap: 68px.
- Card padding: 45px.
- Element gap: 20px.

Build these component patterns where relevant:

- Primary CTA Button: Main conversion action - reserve space, book a tour
- Ghost Button: Secondary actions on dark navigation
- Navigation Bar: Top-level site navigation, sticky
- W Logo Monogram: Brand identity mark, center of navigation
- Hero Display Headline: Full-bleed hero text overlay
- Hero Eyebrow Label: Pre-headline context above the hero display
- Section Eyebrow Label: Small uppercase label introducing each content section
- Section Heading: Primary heading for content sections
- Display Heading (Serif): Hero or large editorial display text on content sections
- Body Text Block: Primary paragraph content
- Feature List: Bulleted feature list in content sections
- Content Section: Alternating text+image content blocks

Do:

- Use 3px border-radius on every interactive element, card, and image - this is non-negotiable and defines the print-publication feel
- Use Ash Mist (#dddedf) for all hairline borders, dividers, and card edges - it is the most-used color on the site and structures every layout
- Use Espresso Bark (#3c261c) for all body text and structural dark needs; reserve #000000 for image fills only
- Use Terracotta Ember (#e97451) only for primary action borders, active nav states, and the logo monogram - never as a large surface fill
- Use paradigm-pro at weight 300 for all display and hero headlines - the whisper-thin serif is the site's most distinctive typographic signature
- Apply uppercase with 0.07-0.1em letter-spacing to all section headings, nav links, and eyebrow labels - this tracking is what makes the design read as editorial rather than web
- Maintain 68px vertical section gaps and 45px card/section padding for the spacious, breathing-room rhythm

Avoid:

- Do not use border-radius larger than 3px - no pill buttons, no rounded cards, no soft corners anywhere
- Do not use #ffffff as a background - always use Warm Linen (#f9f8f0) to maintain the cream canvas warmth
- Do not use drop shadows or box-shadow elevation - separation comes from hairline borders and tonal surface shifts only
- Do not use Terracotta Ember as a large fill color - it is an accent, rationed to borders, active states, and the logo only
- Do not use Iris Ink (#4a43dd) for body text or navigation - it is reserved for decorative display headings and the logo monogram stroke
- Do not use font-weight above 300 for the paradigm-pro display serif - the whisper-thin weight is the entire point
- Do not mix multiple accent colors in a single view - terracotta speaks alone; adding iris or honey to the same component creates noise

Source prompt cues:

primary action: #e97451 (filled action)
Create a Primary Action Button: #e97451 background, #3c261c text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
**Quick Color Reference**
- Page background: #f9f8f0 (Warm Linen)
- Primary text / structural dark: #3c261c (Espresso Bark)
- Hairline borders: #dddedf (Ash Mist)
- Primary action accent: #e97451 (Terracotta Ember)
- Decorative display heading: #4a43dd (Iris Ink)
- Highlight wash: #f7efc5 (Honey Parchment)
- All interactive elements: 3px border-radius

**Example Component Prompts**


2. *Content Section with Feature List*: Warm Linen (#f9f8f0) background, 68px vertical padding, max-width 1200px centered. Two-column grid: left column is text, right column is a photograph (3px radius). Section eyebrow label in MonaSans weight 600, 12px, uppercase, letter-spacing 1.2px, color #3c261c. Section heading in MonaSans weight 500, 32px, uppercase, letter-spacing 2.24px, color #3c261c. Body text in MonaSans weight 400, 18px, line-height 1.55, color #3c261c. Feature list below: each item is MonaSans weight 400, 18px, line-height 1.84, with a 6px Terracotta Ember (#e97451) dot bullet, 14px vertical gap between items.

3. *Navigation Bar*: Full-width, background #3c261c, height ~60px, padding 17px 34px on link items. Three zones: left-aligned nav links in MonaSans weight 500, 12px, uppercase, letter-spacing 1.2px, color #f9f8f0; center-aligned W monogram in #e97451; right-aligned ghost button (1px #f9f8f0 border, 3px radius, padding 17px 34px, text MonaSans weight 500, 12px, uppercase, letter-spacing 0.84px, color #f9f8f0). Active nav link gets a 1px #e97451 border-bottom.

4. *Editorial Display Heading*: paradigm-pro weight 300, 36px, line-height 0.97, letter-spacing 1.08px, color #4a43dd. Use for brand-voice section openers or pull-quote text. Never use for body content or navigation.

5. *Image Card / Workspace Photo*: Full-column-width image, 3px border-radius, no border, no shadow. Sits directly on Warm Linen (#f9f8f0) canvas. Pair with a text column on the opposite side at 68px vertical gap from the previous section.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
