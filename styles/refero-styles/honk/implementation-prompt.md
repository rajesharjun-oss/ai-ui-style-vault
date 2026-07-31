# AI Implementation Prompt

Build a Honk-inspired interface using this source-derived style bundle.

Reference site: https://honk.me
Theme: light
Category: Productivity
North star: Cobalt billboard with a yellow highlighter slash

Use these palette anchors:

- Honk Blue `#008fff` for Full-viewport page canvas, hero background, all top-level sections - the electric blue IS the brand surface, not a secondary accent
- Honk Sky `#00a0ff` for Secondary blue for gradient bands, large decorative shapes, and depth layers behind the primary canvas
- Signal Yellow `#ffe400` for Accent words inside headlines, heading border underlines, and highlight punctuation - the only chromatic accent on the blue field, used sparingly for emphasis rather than decoration
- Honk White `#ffffff` for Hairline borders, dividers, input outlines, and card edges on light surfaces. Do not promote it to the primary CTA color
- Carbon `#111111` for Primary text on light surfaces, dark borders, near-black detail work - used where text leaves the blue field
- True Black `#000000` for SVG fills, graphic detail, maximum-contrast text where the design needs to drop to absolute black
- Slate `#363636` for Secondary graphic fills, dark illustration detail, softer-than-black accents in SVG work
- Game Green `#3fcc6b` for Phone screen content (in-game UI inside device mockups) - a single-hue secondary color reserved for product-internal screens so the blue/yellow/white trio stays clean on the marketing surface

Use these typography anchors:

- Honk Header `--font-honk-header` for Hero and section display headlines - custom heavy display face at a single 52px size, tightly tracked at -0.012em. This is the signature wordmark voice: chunky, loud, slightly condensed, designed to read at billboard scale on the blue field
- Honk Sans `--font-honk-sans` for Body copy, sub-headings, button labels, link text, footer, icons - a neutral grotesk covering the full UI scale from 13px micro-labels to 19px lead paragraphs. Negative tracking across the board (-0.026em at 13px, -0.006em at 19px) tightens the grotesque to feel modern rather than airy

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 20-24px.
- Element gap: 16px.

Build these component patterns where relevant:

- Blue Hero Canvas: Full-bleed hero section
- Highlighted Headline: Hero/section H1
- Hero Sub-headline: Body intro under headline
- Notification Banner: Embedded chat notification UI
- Phone Mockup Frame: Device illustration for product showcase
- Speech Bubble Decoration: Floating emoji-shaped UI nubs
- In-Phone Game Screen: Product-internal UI (device screen content)
- Ghost Link Button: Lightweight text link / action
- Footer Section: Closing dark or blue band

Do:

- Use #008fff as the full-viewport canvas for every top-level section - never place the headline on a white card with a blue background behind it; the blue IS the surface.
- Flip one or two words inside a 52px Honk Header headline to #ffe400 to create emphasis. Never underline, italicize, or bold the highlighted word - color is the only differentiator.
- Set all body copy in Honk Sans at 16-19px with the negative tracking values from the type scale (-0.018em at 16px, -0.006em at 19px) - the tightened grotesque is part of the voice.
- Use the 16px-radius token for any white panel embedded in the blue field (notification banners, content cards, image containers) and the 6px-radius token for small pills or chips.
- Place the phone mockup on the right side of the hero at 45-55% column width, surrounded by 2-3 floating white speech-bubble decorations - never center it, never add a drop shadow.
- Use #3fcc6b green exclusively inside the phone screen for product-internal UI; keep the marketing surface to the blue/yellow/white trio only.
- Keep icon strokes at 2px in Honk Sans weight, white on blue - icons are line-style, never filled, never chromatic.

Avoid:

- Don't use white or light-gray page backgrounds for marketing screens - the design system assumes the blue field is always present, so a white page reads as broken.
- Don't use #ffe400 for body text, button backgrounds, or large fill areas - Signal Yellow is a word-level highlight only, not a surface color.
- Don't introduce a third saturated color to the marketing surface (purple, red, orange) - only the blue field, yellow accents, white text, and the green inside device mockups are permitted.
- Don't use heavy drop shadows on cards, buttons, or the phone mockup - elevation comes from color contrast against the blue, not from shadow stacks.
- Don't split the headline across more than 3 lines or highlight more than 2 words with yellow - the system relies on a single punctuation moment, not scattered emphasis.
- Don't use a different font family for sub-headings, buttons, or links - Honk Sans at varied weights covers the entire UI; Honk Header is display-only.
- Don't use the 6px-radius token on cards or large panels, and don't use the 16px-radius token on buttons - keep small-radius on small elements, large-radius on large surfaces.

Source prompt cues:

**Quick Color Reference**
- background: #008fff (full-viewport canvas)
- text: #ffffff (on blue), #111111 (on light panels)
- border: #ffffff (on blue), #111111 (on light)
- accent: #ffe400 (headline word highlights, small accent borders)
- primary action: no distinct CTA color
- device screen green: #3fcc6b (inside phone mockup only)

**3-5 Example Component Prompts**
1. **Hero Headline Block**: Blue #008fff full-viewport background. Headline 'Really, real-time messaging.' in Honk Header 700 at 52px, white, letter-spacing -0.012em, line-height 1.23, split across 2 lines with 'Really,' flipped to #ffe400. Sub-headline in Honk Sans 400 at 19px white. 80px gap to sub-headline.
2. **Notification Banner**: White #ffffff panel, 16px border-radius, 20px vertical padding, full-width within the hero column. Top row: small Honk Sans 500 at 13px white-on-blue label 'Read Announcement ' sitting above a bold Honk Sans 600 at 16px #111111 message line. Yellow #ffe400 location-pin icon at the far right, 20px size.
3. **Phone Mockup with Game Screen**: Dark iPhone bezel, 45% of hero column width, right-aligned. Screen fill #3fcc6b green. Inside: white tic-tac-toe 3x3 grid with 80px cell squares, 2 circular avatar bubbles at the top in #ffffff, and a bottom row of 3 small white circular buttons (volume, mute grid icon, mic). No drop shadow.
4. **Speech Bubble Decoration**: White #ffffff rounded shape, 16-20px border-radius, 60-80px diameter, centered icon (heart, settings gear) in #111111 at 24px. Float 20-40px away from the phone mockup at varied sizes. Two to three per hero, never overlapping the headline.
5. **Footer Link Row**: Blue #008fff background, 24px vertical padding, Honk Sans 400 at 14px white. Links separated by 16px horizontal gap, no dividers, no bullet characters. Pure flat list, not a column grid.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
