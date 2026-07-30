# AI Implementation Prompt

Build a Scheduling-inspired interface using this source-derived style bundle.

Reference site: https://glossgenius.com
Theme: light
Category: SaaS
North star: Editorial ink on cream paper

Use these palette anchors:

- Gloss Black `#17150e` for Primary text, dark card surfaces, footer background, pill button fill - a warm near-black that reads softer than pure #000 and makes the large display type feel printed rather than digital; 1.5px borders and dividers - uses the same warm-black as text to keep all structural lines tonally unified
- Gloss White `#f0f7f6` for Page tint sections, card surfaces, badge fills, button text on dark - a barely-green-tinted off-white that warms the interface and creates gentle contrast bands against pure white
- Pure White `#ffffff` for Primary page canvas, card surface, dark-button text, nav link color - used wherever maximum contrast is needed without any color temperature
- Solar Yellow `#cccc25` for Yellow action color for filled buttons, selected navigation states, and focused conversion moments; Soft yellow-to-pale-yellow gradient used as decorative wash behind hero copy and section transitions
- Soft Charcoal `#272b30` for Secondary dark surface, deep section backgrounds - cooler alternative to Gloss Black for variant cards and panels
- Mid Grey `#949494` for Muted helper text, secondary labels - reserved for non-essential copy where readability is still required
- Light Coral `#ff7780` for Accent tint for decorative illustrations and marketing gradient washes - never used for UI states
- Apricot `#ffe5d6` for Soft accent fill for illustration blocks and feature card backgrounds in the marketing surface
- Apricot Glow `#ffb36a` for Warm illustration accent - pairs with Light Coral in editorial gradient compositions
- Lavender Mist `#c0c8f6` for Cool illustration accent balancing the warm Coral/Apricot pair in product showcase gradients
- Periwinkle Fade `#9fa6ff` for Periwinkle-to-lavender gradient used in product feature illustrations and decorative dividers

Use these typography anchors:

- Basel Grotesk Book `--font-basel-grotesk-book` for Workhorse for all UI: nav, body, buttons, badges, card copy, h2-h6 headings, and the 72px section headlines. Weight 500 is the default (heavier than typical body text) which gives the interface a confident, almost magazine-pull-quote density. The slight geometric warmth keeps it from feeling clinical.
- Basel Classic Book `--font-basel-classic-book` for Reserved exclusively for display/editorial statements at 96px+ and the 40px h1 variant. Its sharper, slightly more serifed terminals distinguish hero-level copy from section headlines - a deliberate two-voice system that signals "this is the big idea" vs "this is the next thought." Weight stays at 400 even at 144px because the tight 0.8 line-height and -0.03em tracking already create visual mass.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 16px.

Build these component patterns where relevant:

- Primary Pill Button (Dark): Highest-emphasis action - trial sign-up, primary conversion
- Primary Pill Button (Yellow Accent): Hero CTA - demo request, primary conversion on dark hero photo
- Ghost Outline Button: Secondary action over imagery or dark surfaces
- Text Nav Link: Top navigation items
- Feature Card (Mint): Product screenshot showcase blocks on white sections
- Dark Feature Card: High-contrast product showcase or testimonial blocks
- Stat Block: Hero metrics in the social-proof band - 26%, 75%, 40hrs
- Filled Badge: Status tags, count indicators, notification pills
- Ghost Badge: Section labels, filter tags, eyebrow text
- Carousel Arrow Control: Section navigation between feature cards or testimonials
- Announcement Bar: Top-of-page promotional strip
- Chat Widget: Persistent customer support trigger

Do:

- Use Basel Classic Book only at 96px+; reserve it for the single biggest statement on a page
- Set all heading line-height to 1.0 or below; the tight stacking is signature and not optional
- Apply -0.03em letter-spacing on any text 40px or larger; 0 tracking at body sizes
- Alternate section backgrounds between #ffffff and #f0f7f6 to create the magazine-spread cadence
- Use #cccc25 (Solar Yellow) for exactly one element per view - hero CTA, a single stat chip, or a gradient wash - never as a general accent
- Set border-radius to 1440px on every button and 8px on every standard card; mixing the two within a component family breaks the system
- Use 1.5px borders (not 1px) for all dividers and ghost elements - the slightly heavier line reads as intentional ink rather than CSS default

Avoid:

- Don't introduce drop shadows on standard cards; the system is flat by design and shadows undermine the editorial feel
- Don't use #000000 for text or fills - always warm it to #17150 to preserve the printed-ink quality
- Don't pair Basel Classic with anything below 96px; the contrast in voice collapses at smaller sizes
- Don't place yellow buttons on yellow gradient backgrounds - the CTA loses all emphasis
- Don't add a third display weight (e.g. 600) to either font; the system only uses 400 and 500
- Don't use the decorative illustration colors (Coral, Apricot, Lavender) for UI states, text, or borders - they are gradient art only
- Don't add hover shadows to buttons; use background-color or border-color transitions exclusively

Source prompt cues:

**Quick Color Reference**
- text: #17150e (warm near-black)
- background: #ffffff (canvas) / #f0f7f6 (tint sections)
- border: 1.5px solid #17150e
- accent: #cccc25 (Solar Yellow) - charts, metric chips, gradient washes
- card surface: #f0f7f6 with 8px radius, no shadow
- primary action: no distinct CTA color

**Example Component Prompts**
No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

2. **Stat band**: Mint #f0f7f6 section background, 80px vertical padding. Three columns. Each column: display number at 96px Basel Classic weight 400, #17150e, line-height 0.95, letter-spacing -2.88px, with a superscript '+' in the same style. Caption beneath in Basel Grotesk 16px weight 500, #17150e.

3. **Feature card with product mockup**: White section background. Card: #f0f7f6 fill, 8px radius, 24px padding, no shadow, no border. Contains a product screenshot filling 100% card width with 8px radius clip. Heading above card at 40px Basel Classic weight 400, #17150e.

4. **Ghost badge / eyebrow label**: Transparent fill, 1.5px solid #17150e border, 8px radius, 12px padding. Text in Basel Grotesk 16px weight 500, #17150e, letter-spacing 0.063em, uppercase optional.

5. **Carousel navigation**: Two 40x40px square buttons flush-right of section heading. Transparent fill, 1.5px solid #17150e border, 8px radius, #17150e arrow glyph centered. Gap of 4px between arrows.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
