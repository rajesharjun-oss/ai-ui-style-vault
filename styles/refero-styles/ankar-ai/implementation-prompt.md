# AI Implementation Prompt

Build a Ankar AI-inspired interface using this source-derived style bundle.

Reference site: https://ankar.ai
Theme: light
Category: AI
North star: Patent vault opening into white atelier - a darkroom hero with a single illuminated manuscript, dissolving into generous editorial whitespace.

Use these palette anchors:

- Obsidian `#000000` for Primary text, hairline borders, icon strokes
- Paper White `#ffffff` for Page canvas, card surfaces, text on dark
- Ink `#171717` for Filled button background, dark card surfaces, hero base
- Charcoal `#1f1f1f` for Dark feature card surfaces, elevated dark panels
- Graphite `#515151` for Secondary text, muted labels
- Slate `#979797` for Muted helper text, disabled labels, logo grayscale
- Ash `#b9b9b9` for Soft surface tint, placeholder backgrounds
- Fog `#cfcfcf` for Dividers, input borders, ghost button fills
- Mist `#c5c5c5` for Light borders on muted backgrounds

Use these typography anchors:

- Switzer Variable `--font-switzer-variable` for Switzer Variable - detected in extracted data but not described by AI
- Kibitz Pro Light `--font-kibitz-pro-light` for Display and heading serif - used at all H1-H4 sizes. Weight 300 is anti-convention: most SaaS uses 600-700 for authority, this whisper-weight conveys authority through restraint. Tight line-heights (0.98-1.06) let large sizes feel carved from a single block rather than stacked lines.
- Switzer `--font-switzer` for Primary UI and body sans-serif. Weight 400 for body and 500 for nav labels and emphasis. Geometric humanist construction keeps it neutral so the serif can lead.
- Space Mono `--font-space-mono` for Monospace for labels, tags, metadata, and code-adjacent micro-copy. Adds technical credibility to the editorial voice.
- System sans-serif `--font-system-sans-serif` for Fallback utility text - secondary nav micro-copy and fallbacks. Lowest in the hierarchy; should not appear on hero or feature content.

Use these layout rules:

- Base spacing: .
- Density: compact.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 20px.
- Element gap: 10px.

Build these component patterns where relevant:

- Primary Filled Button: Main conversion action - 'Book a demo', 'Learn more'
- Outlined Ghost Button: Secondary action on dark surfaces - nav-level 'Book a demo' on hero
- Feature Card: Showcases a platform capability with icon, title, and description
- Testimonial Card: Displays a customer quote with portrait, attribution, and CTA
- Navigation Bar: Top-level site navigation
- Carousel Arrow Control: Pagination control for testimonial or feature carousels
- Section Heading Block: Opens a content section with eyebrow, title, and optional subtext
- Logo Bar Item: Client or partner logo in social-proof strip
- Hero Light-Burst Canvas: Full-bleed dark hero with cinematic radial light burst
- Platform Tag: Section identifier above a heading - 'Our Platform'
- Icon Container (Pill): Circular badge wrapping a feature icon

Do:

- Use Kibitz Pro Light at weight 300 for all display and heading text - never bold it to compensate for hierarchy; use size instead
- Set letter-spacing to -0.01em on every serif size from 24px upward
- Use #171717 as the filled button background, not pure #000000 - the slightly lifted black reads as Ink, not a void
- Keep border-radius at 4px for all rectangular UI (buttons, nav items, links) - reserve 100px only for icon containers
- Set section gap to 80px and constrain content to a 1200px max-width centered column
- Use Space Mono 12px for technical labels, metadata, and eyebrow tags - never for body paragraphs
- Let dark surfaces (#1f1f1f, #171717) create visual hierarchy instead of adding drop shadows

Avoid:

- Don't introduce chromatic accent colors - the system is strictly monochrome and any color breaks the editorial voice
- Don't use bold (600+) weights for the serif - the whisper-weight is the signature; going heavier flattens the hierarchy
- Don't apply line-height above 1.10 on display sizes - the carved, tight leading is what makes 48-64px feel architectural
- Don't add drop shadows to cards, buttons, or nav - the design is intentionally flat and shadow kills the editorial feel
- Don't use pill-shaped (fully rounded) buttons - 4px corners read as precise and professional, pills would feel consumer/playful
- Don't use the system sans-serif fallback for any user-facing content beyond utility micro-copy
- Don't center-align body paragraphs or long-form descriptions - left-align with a max-width column

Source prompt cues:

**Quick Color Reference**
- text: #171717 (on white) or #ffffff (on dark)
- background: #ffffff (pages) / #171717 (hero, dark panels)
- border: #000000 (hairline) / #cfcfcf (dividers, inputs)
- accent: none - strictly monochrome
- muted text: #515151 secondary, #979797 tertiary
- primary action: #171717 (filled action)

**3-5 Example Component Prompts**

1. *Hero section*: Full-bleed #000000 background with a soft radial light burst gradient (warm white center muted orange red blue black at edges). Centered 1200px column. Headline in Kibitz Pro Light weight 300 at 64px, #ffffff, line-height 1.00, letter-spacing -0.64px: 'Stronger Patents, at Scale'. Subtext in Switzer 16px weight 400, #cfcfcf. Filled white button below: #ffffff background, #171717 text, Switzer 500 14px, padding 10px 16px, radius 4px.

2. *Feature card grid*: 4-column grid, 20px gap, on #ffffff page. Each card is a #1f1f1f dark surface with subtle radial gradient wash, 4px radius, 24px padding. White 24px icon top-center. Title in Switzer 500 16px #ffffff. Description below the card (outside the dark surface) in Switzer 400 14px #515151, max 2 lines.

3. *Section heading*: Left-aligned within 1200px column. Optional eyebrow tag: small icon + 'Our Platform' in Switzer 500 13px #171717. Main title in Kibitz Pro Light 300 at 40px, #171717, line-height 1.00, letter-spacing -0.40px. Subtext in Switzer 400 16px #515151, max-width 640px.

4. *Testimonial card*: White surface, 16:9 contained photo at top, 4px radius. Quote in Switzer 400 16px #171717, 1.58 line-height. Attribution row: 32px circular avatar, name in Switzer 500 14px #171717, role in Space Mono 12px #979797. Dark filled 'Learn more' button below: #171717 bg, #ffffff text, Switzer 500 14px, padding 10px 16px, radius 4px.

5. *Navigation bar*: Transparent background over hero, white text. Logo 'ANKAR' left in Switzer 500 16px #ffffff with small geometric mark. Centered nav: 'Product Company Customers Security Resources Community' in Switzer 400 14px #ffffff, 24px gap between items. Right-aligned ghost button: 1px border #ffffff, transparent bg, #ffffff text, padding 10px 16px, radius 4px, 'Book a demo'.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
