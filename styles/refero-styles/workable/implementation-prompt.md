# AI Implementation Prompt

Build a Workable-inspired interface using this source-derived style bundle.

Reference site: https://www.workable.com
Theme: light
Category: SaaS
North star: warm newsroom with teal ink

Use these palette anchors:

- Workable Ink `#0f161e` for Headlines, body copy, icon fills, dark UI surfaces - near-black with a blue-ink undertone, softer than pure black
- Page Canvas `#fbfaf8` for Default page background and warm card surface - slightly cream-tinted off-white that gives the whole site a paper-like warmth
- Pure White `#ffffff` for Elevated card surfaces on warm canvas, nav background - true white used sparingly for crisp product panels against the cream page
- Body Graphite `#3d3e45` for Body paragraph text, secondary link color - softened dark gray for readable prose without the weight of ink-black
- Muted Slate `#6f7073` for Eyebrow labels, helper text, metadata - medium gray for de-emphasized copy like section kickers and timestamps
- Hairline Gray `#efefef` for Disabled button background, subtle dividers - the lightest neutral surface
- Forest Teal `#004038` for Teal text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color
- Midnight Violet `#1d0953` for Secondary action (Check it out pill), stat callout headings - deep indigo-violet used sparingly for the announcement bar and number highlights
- Lavender Wash `#e5d3f7` for Soft feature card background - pastel lavender for the most prominent colored card surface, gives sections a calm purple identity
- Peach Cream `#fef1e1` for Section background wash, hero-adjacent panels - warm peach-cream used as a large surface band, the dominant chromatic neutral
- Butter Yellow `#fde8ce` for Card background for warm-themed feature panels - muted butter for secondary colored cards
- Periwinkle `#c6c4f4` for Violet wash for highlight backgrounds, decorative bands, and soft emphasis behind content.
- Sky Tint `#bee9f4` for Cool-tone card background - pale sky blue for variety in the pastel card rotation

Use these typography anchors:

- Proxima Nova `--font-proxima-nova` for Single sans family carries all UI - bold 700 at 56-72px with tight 1.14 line-height creates editorial display weight, while 400 at 18-20px with 1.56-1.67 line-height keeps body comfortable. The Minor Third scale (1.2 ratio, 16px base) produces a restrained 8-step hierarchy.

Use these layout rules:

- Base spacing: 8px.
- Density: spacious.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 32px.
- Element gap: 8px.

Build these component patterns where relevant:

- Primary Teal CTA (Filled): Main conversion button - Request a demo
- Ghost Outline Button: Secondary action - Start a free trial, Log in
- Underline Link Button: Tertiary action - Start a free trial (text link variant)
- Midnight Pill (Announcement): Top-bar release announcement - Check it out
- White Product Card: Feature showcase card on white canvas
- Lavender Feature Card: Pastel card for AI/agent feature blocks
- Peach Feature Card: Warm-tone card for evaluation/HR feature blocks
- Butter Feature Card: Secondary warm card
- Top Navigation Bar: Sticky header with brand wordmark and primary actions
- Announcement Banner: Lavender pill above nav for product news
- Section Eyebrow Label: Kicker text above section headings
- Hero Product Visual: Right-side product screenshot with gradient framing

Do:

- Use #004038 Forest Teal as the only filled CTA color - buttons are either teal-filled (primary) or teal-outlined (ghost), never a third color
- Set card border-radius to 16px and button border-radius to 8px consistently - the 8px difference is intentional, cards feel soft, buttons feel crisp
- Apply the warm #fbfaf8 canvas to all section backgrounds and let #ffffff cards float on top - the cream-to-white surface contrast creates depth without shadows
- Use display weight 700 at 56-72px with tight 1.14-1.22 line-height for headlines - heavy weight + tight leading is the editorial signature
- Set body copy at 18px with 1.56 line-height in #3d3e45 Body Graphite - never use #0f161 ink for long-form paragraphs, the contrast is too aggressive
- Rotate pastel cards through #e5d3f7, #fef1e1, #fde8ce, #c6c4f4, #bee9f4 within a grid - the pastel rotation signals feature grouping without needing borders
- Use 12px all-caps #6f7073 Muted Slate for section eyebrow labels with 8px margin to the heading below

Avoid:

- Don't add drop shadows to cards or buttons - the system is intentionally flat, depth comes from surface color contrast only
- Don't use #1d0953 Midnight Violet as a general CTA - it's reserved for the announcement bar pill and number callouts, not buttons
- Don't apply the teal lime violet gradient to buttons, backgrounds, or text - it's only for the Workable 'w' app icon and AI-agent visuals
- Don't use #0f161 ink for body paragraphs - reserve it for headlines, icons, and UI chrome; use #3d3e45 for readable prose
- Don't introduce additional saturated accent colors - the system is built on teal + pastel rotation; adding a new hue breaks the restrained palette
- Don't use sharp 0px or 4px radius on cards - the 16px softness is a signature, all elevated surfaces should feel rounded
- Don't set body line-height below 1.5 - the generous 1.56 line-height at 18px is what makes the dense type feel airy

Source prompt cues:

**Quick Color Reference**
- text: #0f161e (Workable Ink)
- background: #fbfaf8 (Page Canvas) / #ffffff (cards)
- border: #efefef hairline / #004038 chromatic
- accent: #004038 (Forest Teal)
- primary action: #1d0953 (filled action)

**Example Component Prompts**

1. Create a Primary Action Button: #1d0953 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. **Create a ghost outline button**: transparent background, text and border #004038, 1px border, 8px radius, 16pxx24px padding, Proxima Nova 700 at 16px. Use for secondary CTAs in nav bars and hero sections (e.g. 'Start a free trial').


4. **Create a pastel feature card**: fill #e5d3f7 lavender (or rotate through #fef1e1, #fde8ce, #c6c4f4), 16px border-radius, 32px padding all sides, no shadow. Heading at 24px Proxima Nova 400 in #0f161e, body at 16px in #3d3e45. Use in 2-column or 3-column card grids.

5. **Create a white product card on cream canvas**: fill #ffffff, 16px radius, 32px padding, optional 1px #efefef border. This is the cleanest product preview surface - use for UI screenshots, feature showcases, and the talent CRM panels.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
