# AI Implementation Prompt

Build a Daylit-inspired interface using this source-derived style bundle.

Reference site: https://www.daylit.com
Theme: light
Category: Fintech
North star: Burgundy ink on cream parchment - a modern ledger rewritten for the AI era.

Use these palette anchors:

- Wine Ink `#4d1520` for Primary text, primary filled button background, active states, heading color, card borders, and dominant brand stroke - the single chromatic anchor of the entire system
- Midnight Wine `#360912` for Darkest surface for footer bands and inverted panels
- Lemon Whisper `#faffa7` for Decorative accent fill and border - used in illustration blocks, testimonial card outlines, icon highlights, and soft highlight washes
- Blush Rust `#662f3d` for Softened brand fill for secondary surfaces and SVG illustration shading
- Citrine Pop `#e6b800` for Rare saturated accent for micro-detail and decorative strokes
- Mauve Ash `#825b63` for Muted body text and subtle borders when full brand ink would be too loud
- Parchment `#fbf9f6` for Primary page canvas - the warm ivory that replaces cold white throughout
- Pure White `#ffffff` for Card surfaces, input fields, elevated panels - the brightest neutral layer above the parchment canvas
- Linen Beige `#f2eee7` for Hairline borders, dividers, ghost button outlines, and subtle UI separators
- Sandstone `#d3cac3` for Muted borders and secondary divider lines on cards and links
- Driftwood `#aaa49f` for Lowest-contrast neutral for decorative borders and inactive link text
- Slate Smoke `#717182` for Body secondary text, icon strokes, and helper copy - the only cool-leaning neutral
- Charcoal Ink `#101828` for Occasional dark text and info-toned badge borders when Wine Ink would be too warm
- Butter Cream `#feffe1` for Ultra-soft warm fill for highlight zones and subtle surface washes
- Dawn Glow `#e9e3d8` for Warm card background tint used sparingly for warm-on-warm contrast
- Rose Whisper `#d7a0a0` for Soft card border accent for warm-toned testimonial and content cards
- Plum Echo `#906c7b` for Badge and pill background for muted tag variants

Use these typography anchors:

- Tt Commons Pro Variable `--font-tt-commons-pro-variable` for Primary typeface across all contexts - headings, body, nav, buttons, cards. The variable weight axis (400-600) and extreme size range (9px micro-labels to 85px display) make it the sole workhorse. Display sizes use aggressive negative tracking (-0.04em at 76-85px) for a sculptural editorial feel; body sizes stay near normal tracking. The 600 weight carries emphasis without ever feeling bold-shouty.
- Geist Mono `--font-geist-mono` for Monospace accent for badge labels, inline code, and small caps-style tags like '+ AI AGENTS FOR ACCOUNTS RECEIVABLE'. Normal letter-spacing - not tracked like the primary face.
- Open Sans `--font-open-sans` for Open Sans - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 8px.

Build these component patterns where relevant:

- Primary Filled Button: Main call-to-action - used for 'Book a Demo' and all conversion actions
- Ghost / Text Button: Secondary action - 'Meet our AI agents', 'Learn more' links
- Navigation Link: Top nav menu items - Product, Capital, Industries, Resources, About
- Announcement Banner: Top-of-page news strip
- Hero Headline: Section-defining display text - 'Get paid on time. Every time.'
- Testimonial Card: Customer quote card in the social proof section
- Logo Bar Card: Trusted-by logo row in a single horizontal band
- Pill Badge / Tag: Category labels - '+ AI AGENTS FOR ACCOUNTS RECEIVABLE'
- Illustration Panel: Hero visual and decorative graphic blocks
- Card Surface: Generic content card base
- Body Text Block: Paragraph and helper copy
- Top Navigation Bar: Sticky or static header with brand and primary nav

Do:

- Use #4d1520 as the default text color and primary button fill - it is the system's single chromatic anchor and should appear in every screen
- Set page canvas to #fbf9f6 parchment, not pure white - the warm ivory is what makes the burgundy sing
- Use 6px radius for all cards, buttons, and inputs as the default; reserve 1440px for pill badges only
- Use Tt Commons Pro at weight 400 for display headings 44px and above - the whisper-weight at large size is a signature
- Apply the wine-tinted shadow rgba(77,21,32,0.16) 19px 32px 73px only on hero-scale elevated cards, never on small UI elements
- Use #faffa7 lemon as a decorative accent fill in illustration blocks and badge backgrounds - never as a text color on dark surfaces
- Center content within a 1200px max-width column with 24-40px horizontal padding for comfortable reading rhythm

Avoid:

- Do not introduce cold grays (#e5e7eb, #f3f4f6, #6b7280) - the entire system is warm-toned and cool neutrals will clash
- Do not use 8px or 12px border-radius on cards or buttons - the 6px radius is part of the system's distinctive geometry
- Do not set body or heading text to weight 600 or 700 - the system maxes out at 600 for emphasis and prefers 400-500
- Do not use pure black (#000000) for text - use #4d1520 wine ink instead, even for body copy
- Do not add drop shadows to buttons, nav items, or small interactive elements - shadows are reserved for hero-scale elevation
- Do not use blue, green, or standard semantic colors for status - the system communicates state through opacity, position, and the single brand hue
- Do not center-align body paragraphs longer than two lines - left-align for readability; center only for headlines and short CTAs

Source prompt cues:

**Quick Color Reference**
- text/headings: #4d1520
- background: #fbf9f6
- card surface: #ffffff
- border/hairline: #f2eee7
- accent fill: #faffa7
- primary action: #4d1520 (filled action)

**Example Component Prompts**

1. Create a Primary Action Button: #4d1520 background, #fbf9f6 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. *Testimonial card*: White background, 1px border in #f2eee7, 6px radius, 24px padding. Company name in Tt Commons Pro 600 at 14px, #4d1520. Quote body in Tt Commons Pro 400 at 15px, #4d1520, line-height 1.6. Author line at bottom: 32px circular avatar + name in weight 500 at 14px, #4d1520 + role in #717182.

3. *Pill badge*: Background #faffa7, text #4d1520, 1440px radius, padding 4px 12px, Geist Mono 500 at 12px, uppercase. Optional left '+' icon in #4d1520.

4. *Navigation bar*: Full-width, #fbf9f6 background, 72px height. Left: wordmark logo in #4d1520. Center-right: 5 nav links in Tt Commons Pro 500 at 15px, #4d1520, 32px gap between items, each with a small 12px caret. Far right: 'Login' text link, 'Capital' text link, then filled 'Book a Demo' button with #4d1520 background, white text, 6px radius, 10px 18px padding, plus a small yellow 2x2 grid icon trailing the label.

5. *Logo bar*: Full-width section on #fbf9f6. Left label 'Trusted by' in Tt Commons Pro 400 at 14px, #717182. Right: 6-8 grayscale logos at 40px height, evenly spaced with 8px gaps, flexbox row, center-aligned vertically.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
