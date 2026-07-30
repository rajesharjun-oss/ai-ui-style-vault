# AI Implementation Prompt

Build a Wizz-inspired interface using this source-derived style bundle.

Reference site: https://wizzapp.com
Theme: light
Category: Other
North star: Neon pink highlighter on a black-and-white editorial - like a single fluorescent mark on a fashion magazine spread.

Use these palette anchors:

- Volt Pink `#ff3d9e` for Primary action buttons, section labels, active states, cookie accept - the sole chromatic brand color, carrying 100% of the accent weight in the interface
- Obsidian `#000000` for Page text, floating navigation bar, bold display headlines, cookie banner surface, icon fills
- Paper White `#ffffff` for Page canvas, section backgrounds, text on dark surfaces, card surfaces in light sections
- Ash `#dadada` for Hairline borders, card inset rings, subtle dividers, secondary text on light backgrounds
- Charcoal `#444444` for Input borders, secondary surface fills, muted UI elements
- Onyx `#292929` for Secondary button backgrounds, elevated surface tone
- Mist `#eeeeee` for Input field backgrounds, subtle fill surfaces

Use these typography anchors:

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- PolySans Bulky `--font-polysans-bulky` for Hero display headlines - the signature compressed ultra-bold weight; tight line-height (1.0) lets the letters stack like a logo mark rather than reading as paragraphs
- PolySans Median `--font-polysans-median` for Primary workhorse - nav links, section headings, the 86px display for page-openers, all-caps micro-labels with 0.05em tracking. The compressed line-heights (0.85-1.0) at large sizes are what give Wizz its editorial-magazine density
- PolySans Neutral `--font-polysans-neutral` for Body copy, paragraph text, descriptive content - generous line-height (1.5) creates reading rhythm distinct from the tight display set
- PolySans Slim `--font-polysans-slim` for Light-weight utility text, subtle links, fine-print detail - provides typographic contrast against heavier Median weights in the same layout
- Inter `--font-inter` for Inter - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: compact.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 16px.
- Element gap: 10px.

Build these component patterns where relevant:

- Floating Navigation Pill: Primary site navigation bar
- Primary CTA Button (Download / Accept / Our News): Main call-to-action
- News / Announcement Pill: Inline news banner
- Cookie Consent Card: Privacy compliance overlay
- App Store Download Badge Pair: App download CTAs
- Trust Indicator Strip: Social proof band
- Section Eyebrow Label: Category label above section headings
- Display Headline: Page-opener and section title
- Feature Row (Mission section): Mission statement with heading + body
- Phone Mockup Carousel: Product showcase with tilted device images
- Input Field: Form input
- Ghost / Secondary Button: Non-primary action

Do:

- Use Volt Pink (#ff3d9e) as the sole chromatic accent - for one primary action per view, for section eyebrow labels, and for the cookie Accept button. Never dilute it across multiple elements on the same screen.
- Set all-caps display headlines in PolySans Bulky or PolySans Median weight 700 at 72-86px with line-height 0.85-1.0 and near-zero letter-spacing. The compressed vertical rhythm is what makes the type feel editorial.
- Apply 999px border-radius to the floating navigation bar, news pills, and any tag/chip elements. Use 12px radius for buttons, cards, and inputs. Use 24px for image frames.
- Use black (#000000) for the floating nav surface, bold display text, and the cookie banner - and always pair it with white or pink text on top. This black-on-white framing is the system's structural backbone.
- Apply 0.05em letter-spacing to all-caps micro-labels and eyebrow text at 10-14px. This widens the optical density of the small type and makes the pink section labels feel deliberately stamped.
- Keep body copy in PolySans Neutral weight 400 at 16px with line-height 1.5 for reading comfort. Never use Median weights for paragraphs.
- Add the very faint shadow rgba(0,0,0,0.05) 0px 1px 10px to card surfaces and rgba(0,0,0,0.3) 0px 1px 30px to the primary CTA. These are the only two shadow depths in the system.

Avoid:

- Never introduce a second accent color. The entire brand identity depends on pink being the only chromatic signal in a black-and-white field.
- Never use decorative gradients on UI elements. The hero gradient is the only allowed multi-color surface - everything else is flat solid fills.
- Never use drop shadows heavier than the two defined values. The system is intentionally flat; heavy elevation breaks the editorial feel.
- Don't use system sans-serif for headings. PolySans Median and Bulky are the identity - fall back to Inter or Manrope only if the custom fonts are unavailable.
- Never place body copy below 14px. The compact density is created through tight spacing, not through microscopic type.
- Don't use sharp corners (<5px radius) on any interactive element. Every button, input, card, and nav must have at least 12px or fully pill-shaped radius.
- Never use the pink accent on body text longer than a few words. Pink is for labels, buttons, and emphasis - not for paragraphs or descriptions.

Source prompt cues:

**Quick Color Reference**
- Text: #000000 (primary), #444444 (muted)
- Background: #ffffff (page), #000000 (dark surfaces), #eeeeee (input fill)
- Border: #dadada (hairline), #444444 (input)
- Accent: #ff3d9e (Volt Pink - eyebrow labels, emphasis)
- primary action: #ff3d9e (filled action)

**Example Component Prompts**

1. **Hero Section**: Full-bleed gradient background (lavender coral sky blue amber). Centered stack: small black 'NEWS' pill at top, then 'MEET YOUR PEOPLE NOW' in PolySans Bulky 72px weight 700, color #000000, line-height 1.0, letter-spacing -0.72px. Below: two app store download badges side by side, each black (#000000) pill with white text and icon.

2. **Floating Navigation Bar**: Black (#000000) pill, 999px border-radius, max-width 1200px centered, padding 10px 20px. White Wizz logotype left, 5 nav links in white PolySans Median 14px weight 400 center, pink (#ff3d9e) 'Download' button (12px radius, 10px 20px padding) right.

3. **Section with Eyebrow Label**: White background, 80px vertical padding. Stack: pink (#ff3d9e) all-caps eyebrow 'REVOLUTIONIZING CONNECTION' in PolySans Median 600 at 13px, letter-spacing 0.05em. Below: bold body statement in PolySans Median 600 at 18px, color #000000. Below: paragraph in PolySans Neutral 400 at 16px, line-height 1.5, color #000000.

4. **Cookie Consent Card**: Fixed bottom-right, 320px wide. Black (#000000) background, 12px border-radius, padding 20px. Title 'Cookie Settings' in PolySans Median 700, 16px, white. Body in PolySans Neutral 400, 14px, white, line-height 1.5. Two buttons side by side: 'Reject' as dark ghost (#292929 fill, white text, 12px radius), 'Accept' as filled pink (#ff3d9e, white text, 12px radius).

5. **Phone Mockup Showcase Band**: White background, full-width row of 8-10 phone mockups. Each phone: 24px border-radius, rotated -8 to +8 alternating, slight overlap. Inside each phone: dark chat interface with pink/purple gradient. No shadows on phones; the rotation creates the visual energy.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
