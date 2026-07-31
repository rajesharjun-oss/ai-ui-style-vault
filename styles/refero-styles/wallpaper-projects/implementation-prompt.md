# AI Implementation Prompt

Build a Wallpaper Projects-inspired interface using this source-derived style bundle.

Reference site: https://wallpaperprojects.com
Theme: light
Category: Agency
North star: Editorial gallery on warm paper - a spread from a 12x16 art monograph where cream stock, near-black ink, and one enormous serif do all the talking.

Use these palette anchors:

- Ink Black `#1e1e1e` for Primary text, dark pill button fills, borders, heading strokes - the only ink in the system
- Paper White `#ffffff` for Primary canvas, image backgrounds, button text on dark fills
- Warm Cream `#fbf9f3` for Alternate surface - the signature cream stock that gives the system its editorial warmth, used for secondary sections and cards
- Pure Black `#000000` for Maximum contrast moments, occasional true-black text where #1e1e1 isn't dark enough

Use these typography anchors:

- Cardinal Fruit `--font-cardinal-fruit` for The signature display serif - exclusively used for hero headlines, section openers, and any moment that needs to feel like a magazine cover. The medium weight (500) is reserved for the most massive treatments (132-180px) where hairline strokes would disappear. Negative letter-spacing tightens the massive forms into a cohesive block of ink.
- Soehne Breit Buch `--font-soehne-breit-buch` for The workhorse grotesque with widened proportions. At small sizes (10-14px) the 0.1em tracking creates the editorial 'kicker' label aesthetic. At 72-80px it serves as a secondary display face for contexts where serif would feel too precious. The 600 weight is used sparingly for emphasis.
- Soehne Mono Buch `--font-soehne-mono-buch` for Monospaced UI face for technical labels, metadata, button text, and small data displays. Its presence signals 'system metadata' versus 'editorial content' - the mono is the interface voice, the serif is the gallery voice.

Use these layout rules:

- Base spacing: 4px.
- Density: spacious.
- Page max-width: 1440px.
- Section gap: 100px.
- Card padding: 24px.
- Element gap: 20px.

Build these component patterns where relevant:

- Dark Pill Button (Primary Action): The only button style that matters - the system's single interactive punctuation mark
- Ghost Outline Button: Secondary action for less critical interactions
- Section Kicker Label: Tiny uppercase label that opens every content section like a magazine department header
- Editorial Display Headline: The hero/cover headline that defines the page
- Asymmetric Section Header: Left-column header for split text+image sections
- Full-Bleed Hero with Overlay Type: The page-opening canvas - atmospheric photography as backdrop, type as subject
- Two-Column Image Grid: Quick visual proof beneath introductory text
- Split Content Section (Text Left / Image Right): The primary content arrangement for project showcases and about sections
- Minimal Navigation Header: Persistent top bar - almost invisible by design
- Footer Single-Line: Minimal page closure
- Scroll Indicator: Vertical guide suggesting 'there's more below'

Do:

- Use Cardinal Fruit at 48-180px for all display headlines; never below 36px
- Set all buttons to 20px border-radius with 7-8px vertical and 16px horizontal padding in Soehne Mono 12px
- Alternate section backgrounds between #ffffff and #fbf9f3 to create editorial rhythm
- Prefix every content section with a Soehne Breit 10px uppercase kicker label at 1.0px letter-spacing
- Use 100px section gaps and 20px element gaps as the standard rhythm
- Let images fill their containers edge-to-edge with zero border-radius
- Reserve #1e1e1 for text, borders, and button fills only - never as a decorative wash

Avoid:

- Never introduce chromatic colors - the 0% colorfulness is the entire brand
- Never use box-shadow for elevation; let surface color contrast do the work
- Never use a border-radius other than 20px for interactive elements or 0px for images/cards
- Never set body text below 14px or above 18px; the editorial scale is fixed
- Never use the display serif (Cardinal Fruit) at sizes below 36px - it loses its character
- Never add visible dividers, rules, or borders between sections - whitespace is the only separator
- Never darken or overlay hero photography; let the type sit directly on the raw image

Source prompt cues:

**Quick Color Reference:**
- text: #1e1e1e
- background: #ffffff
- alternate surface: #fbf9f3
- border: #1e1e1e
- primary action: #1e1e1e (filled action)
- accent: none - the system has no chromatic accent

**Example Component Prompts:**

1. *Create a dark pill CTA button:* Fill #1e1e1e, text #ffffff in Soehne Mono 12px with 0.3px letter-spacing, 20px border-radius, 8px top padding, 7px bottom padding, 16px left/right padding. Label in uppercase.

2. *Create a section opener:* Warm cream background (#fbf9f3). Top: Soehne Breit 10px uppercase kicker in #1e1e1e with 1.0px letter-spacing, 10px bottom margin. Below: Cardinal Fruit 48px weight 500 in #1e1e1e, letter-spacing -1.2px. Below: Soehne Breit 14px body text in #1e1e1e, line-height 1.6. No card, no border - content sits directly on the cream surface.

3. *Create a split content section:* Two-column grid at 35/65 ratio. Left column on #ffffff: kicker label (Soehne Breit 10px tracked), Cardinal Fruit 48px heading, 14px body text, dark pill button (20px radius). Right column: full-bleed interior photography, zero radius, no overlay. 100px vertical section padding.

4. *Create a full-bleed hero:* Background image fills 100vw x 85vh, no border-radius. Overlaid text: Cardinal Fruit 180px weight 500 in #fbf9f3, letter-spacing -9px, centered. A thin 1px vertical scroll indicator in #fbf9f3, ~120px tall, centered below the headline, ending in a small downward arrow.

5. *Create a minimal nav header:* Transparent background, position sticky. Left: two-line wordmark in Soehne Breit 12px #1e1e1e (first line, second line below). Right: single hamburger icon in #1e1e1e, 24px. No background bar, no visible nav links.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
