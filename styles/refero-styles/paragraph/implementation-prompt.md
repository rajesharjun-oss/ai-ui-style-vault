# AI Implementation Prompt

Build a Paragraph-inspired interface using this source-derived style bundle.

Reference site: https://mirror.xyz
Theme: light
Category: Crypto
North star: Editorial letterpress on warm parchment - a literary journal where the only color is ink-blue and every border is a page edge

Use these palette anchors:

- Page Parchment `#dbd5d2` for Primary border color for all containers, cards, nav, body, and links - warm taupe that reads as paper edge, not digital gray
- Ink Black `#271f1b` for All text, icons, and heading strokes - warm near-black with brown undertone, never pure #000
- Sheet White `#ffffff` for Primary page canvas and white card surfaces. Do not promote it to the primary CTA color
- Felt Gray `#ededed` for Secondary surface for badges, subtle panel backgrounds, and inactive card states
- Margin Gray `#888786` for Muted helper text, secondary metadata, and inactive nav items
- Periwinkle Action `#4a83f5` for Violet wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Cornflower Wash `#b1cafb` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Dusk Periwinkle `#cedaf3` for Inset border and subtle blue-tinted edge on elevated or focused elements

Use these typography anchors:

- IvyOra `--font-ivyora` for Display and heading serif - used at 64px for hero headlines, 24px for section titles, and 18px for card titles. Weight stays at 400 across all sizes: the serif's contrast and tight tracking (-0.03em at display) do the visual work, not boldness.
- Google Sans Flex `--font-google-sans-flex` for Body, navigation, buttons, and utility text. Stays compact (14-18px) and invisible - its job is legibility, not personality. Weight 500 for nav active states, 400 for body, 600 reserved for button labels.

Use these layout rules:

- Base spacing: 8px.
- Density: compact.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 20px.
- Element gap: 8px.

Build these component patterns where relevant:

- Filled Action Button: Primary CTA - navigation, sign-in, collect actions
- Ghost Text Link: Secondary navigation - 'Start reading', inline links
- Navigation Pill: Top-bar navigation container
- Top Header Bar: Site-wide header with brand, nav, and CTA
- Hero Section (Split): Landing page hero
- Feature Card: Explains product capabilities in the 'Why Paragraph?' section
- Article Card: Content discovery card in feed/grid
- Carousel Pagination Dots: Hero slide indicator
- Section Heading (Centered Serif): Section title between content bands
- Tag/Badge: Source labels, category tags on article cards
- Product Preview Card (Phone Frame): Hero product mockup
- Source/Author Row: Byline strip on article cards and preview

Do:

- Use IvyOra (or serif substitute) for all headings and display text at 18px, 24px, and 64px only - never at body sizes or below 18px
- Apply letter-spacing of -0.03em to 64px display, -0.022em to 24px headings, -0.02em to 18px serif subheadings
- Use #dbd5d2 (warm taupe) for all borders - never cold gray; the warmth is the identity
- Reserve #4a83f5 for filled action buttons only; the accent's power comes from scarcity
- Set card and button radii to 20-28px; sharp corners would break the handwritten feel
- Center section headings and allow 80px vertical gaps between content bands
- Use Google Sans Flex weight 500 for active states and button labels, weight 400 for body

Avoid:

- Do not introduce gradients anywhere - the system is flat by design
- Do not use bold (600+) weights in the serif - IvyOra stays at 400 always
- Do not use pure black (#000000) for text - always #271f1b for warmth
- Do not place chromatic color on non-action elements; blue is reserved for buttons
- Do not use cold grays (#e5e7eb, #d1d5db) for borders - always the warm #dbd5d2
- Do not add box-shadows to content cards - the 1px border is the only elevation
- Do not set hero or section headlines above 64px; restraint is the editorial voice

Source prompt cues:

**Quick Color Reference**
- Text: #271f1b
- Background: #ffffff
- Border: #dbd5d2
- Muted text: #888786
- Accent: #4a83f5
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

2. **Article Card Grid:** 4-column grid, 20px gap, max-width 1200px. Each card: white #ffffff bg, 20px radius, 1px solid #dbd5d2 border, no shadow. Cover image at 16px radius fills top 60%. Below: source/date row (Google Sans Flex 14px, #888786) at 8px row gap, then IvyOra 18px heading-sm title (ls -0.36px), then Google Sans Flex 16px body excerpt in #271f1b at 2-3 line clamp.

3. **Feature Card:** White bg, 20px radius, 1px #dbd5d2 border, 20px padding. 16px line-art icon in #271f1b stroke at top-left. IvyOra 18px heading-sm title at 12px gap below icon. Google Sans Flex 16px body description at 8px gap below title.


5. **Centered Section Heading:** Pure white bg, 80px top/bottom padding. IvyOra 24px heading centered in #271f1b with -0.528px letter-spacing. Google Sans Flex 16px subheading centered in #888786 at 12px gap below.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
