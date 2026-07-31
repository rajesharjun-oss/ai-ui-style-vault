# AI Implementation Prompt

Build a Daniel Sun-inspired interface using this source-derived style bundle.

Reference site: https://danielsun.space
Theme: light
Category: Agency
North star: Solar monolith on a white gallery wall - one yellow beam, one obsidian name, all the breathing room in the world.

Use these palette anchors:

- Solar Beam `#ffd500` for The system's only chromatic color - hero gradient beam, handwritten underline accent, and the pill-shaped highlight button inside the dark nav capsule. This is the single note of warmth in an otherwise achromatic composition; its presence transforms monochrome blocks into a sunlit moment
- Obsidian `#000000` for Primary text, display headlines, nav capsule background, and dominant typographic mass. Sets the highest-contrast tone for the condensed display name and grounds the floating nav pill
- Paper White `#ffffff` for Card surfaces, portfolio thumbnails, and the base of the white canvas. Provides the surface that the yellow beam and obsidian type play against
- Concrete `#f5f5f5` for Page canvas and the lightest card/section background. Warmer than pure white, creates the gallery-wall feel beneath the hero
- Graphite `#808080` for Body text, secondary metadata, and muted UI labels. The mid-neutral that bridges the obsidian headlines and the lighter ash tones
- Ash `#a6a6a6` for Muted helper text, tertiary body copy, and the soft end of the text scale. Sits beneath Graphite for non-essential information
- Fog `#999999` for Subdued heading and label color. Slightly cooler than Ash; used for section labels that need to recede behind the primary type
- Silver `#b8b8b8` for Subtle shadow tint and the softest hairline border. Carries the single shadow pattern that gives portfolio cards their barely-there lift
- Soft Shadow `#cfcfcf` for Drop shadow and elevation wash. The companion to Silver for the card shadow rgba(0,0,0,0.12) - never seen directly, only felt as depth

Use these typography anchors:

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- Reddit Sans Condensed `--font-reddit-sans-condensed` for Display headlines - the name 'DANIEL SUN' at 246px and section titles like 'MY LATEST WORK' at 88px. Ultra-condensed, ultra-black; the type is the architecture. Tracking tightens as size grows (-6.9px at 246px) to keep the massive letterforms visually unified. Substitute: Bebas Neue or Anton for the condensed impact, though no free font fully matches the geometry.
- Inter Display `--font-inter-display` for Section headings and larger body text. The medium weight (not bold) is deliberate - Inter Display 500 sits between the whisper of system text and the shout of the display face, creating a quiet middle register. Used for the 26-30px subheadings and the 18-20px lead paragraphs.
- Inter `--font-inter` for Body copy, navigation labels, and inline text. The 14px body-sm and 20px subheading sizes are the everyday workhorses; the 128px outlier is a decorative/typographic moment. Consistent 500 weight keeps the text system cohesive without ever feeling bold.
- Caveat `--font-caveat` for Handwritten personal asides - 'From 2020 til today,' date stamps, signature-style annotations. The only script in the system; its presence signals intimacy and breaks the architectural severity of the condensed display type. Use sparingly - one or two instances per section maximum.
- System Sans `--font-system-sans` for Smallest UI text - copyright lines, micro-labels, and inline metadata. Stays quiet and never competes with the display system.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80-120px.
- Card padding: 32-40px.
- Element gap: 8-16px.

Build these component patterns where relevant:

- Nav Capsule: Primary navigation container
- Nav Highlight Button: Primary call-to-action within the nav capsule
- Display Name: Hero identity - the designer's name as architecture
- Hero Gradient Beam: Signature visual element - the single chromatic accent
- Section Title: Section-level display heading
- Handwritten Annotation: Personal timestamp or intimate label
- Portfolio Card: Project/work showcase container
- Lead Paragraph: Introductory body text below display headlines
- Portfolio Preview Frame: Image container within a portfolio card

Do:

- Use Reddit Sans Condensed 900 at 88-246px for every display-level headline; the condensed geometry is the brand.
- Set the name/hero display at exactly 246px with letter-spacing -6.89px - this scale is the signature, not optional.
- Place exactly one yellow gradient beam per hero; it is the only chromatic element in the system.
- Use Caveat 700 at 28px for personal timestamps above section titles, colored Graphite (#808080) so it recedes behind the display face.
- Use the nav capsule (110px radius, #1f1f1f background) for all top-level navigation - never replace it with a flat horizontal bar.
- Round portfolio cards and images at 14px; round buttons at 32px (pill); round the nav at 110px (fully rounded). These three radii are the system's geometry.
- Keep body text in Inter 500 at 18-20px with line-height 1.30; never use weight 400 - the medium weight is non-negotiable for readability against the massive display type.

Avoid:

- Do not add chromatic colors beyond #ffd500 - the system is monochrome with one solar accent; introducing a second hue breaks the gallery metaphor.
- Do not set the display name below 88px or above 246px - the extreme scale is the point; intermediate sizes lose impact.
- Do not use shadows on buttons, nav elements, or text blocks; the single shadow pattern is reserved for portfolio cards only.
- Do not replace Reddit Sans Condensed with a non-condensed display face; the compressed letterforms are what make the 246px headline read as a single mass.
- Do not use Caveat for anything longer than a date range or one-line aside; the script loses intimacy when it carries real content.
- Do not add gradients other than the single yellow beam; the system is flat surfaces and one light source - multi-color gradients destroy the restraint.
- Do not use weight 700+ for body or subheading text; the 500 weight is the system's voice - bolding it creates visual noise against the 900-weight display face.

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
