# AI Implementation Prompt

Build a Reclaim-inspired interface using this source-derived style bundle.

Reference site: https://reclaim.ai
Theme: light
Category: Productivity
North star: lavender productivity workshop with violet ink

Use these palette anchors:

- Lavender Canvas `#ebefff` for Page background, hero section wash, footer background - the base atmosphere that distinguishes Reclaim from generic white SaaS
- White Surface `#ffffff` for Card surfaces, product mockup containers, button text on dark fills - pure white provides the resting layer above the lavender canvas
- Midnight Ink `#181d25` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color
- Pure Black `#000000` for Dark supporting neutral for text, icons, and strong contrast. Do not promote it to the primary CTA color
- Graphite `#111111` for Body copy and card text on light surfaces - sits just above pure black for slightly softer reading weight
- Slate `#474747` for Muted helper text, secondary descriptions, footer text - the workhorse for non-headline copy
- Charcoal `#2b2b2b` for Subheadings and emphasized body - bridges Midnight Ink headings and Slate body text
- Stone `#333333` for Tertiary text, breadcrumb-style labels
- Mist `#ececec` for Hairline dividers, decorative strokes, subtle separators
- Iris Violet `#5562eb` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Sapphire Violet `#3451e8` for Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Lavender Mist `#c2caf9` for Soft tints for product card highlights, decorative violet washes, outlined button borders - the muted cousin of Iris Violet
- Periwinkle `#96a0f3` for Disabled or secondary violet state, ghost button text on violet themes
- Indigo Depth `#151f8b` for Dark mode gradient anchor, deep accent for special promotional sections
- Focus Green `#7ac17b` for Green supporting accent for decorative details and low-frequency emphasis
- Mint Whisper `#daf0db` for Light supporting surface for subtle backgrounds and section separation
- Forest Edge `#14532d` for Dark green gradient stop for special promotional banners
- Brick `#5a1a1a` for Red supporting accent for decorative details and low-frequency emphasis. Use as a supporting accent, not as a status color

Use these typography anchors:

- Poppins `--font-poppins` for Exclusive brand typeface used for every text element. The 300-weight whisper at 70-90px for hero headlines is the signature move - most productivity apps use bold display weights, but Reclaim's thin Poppins headlines float above the page rather than punch through it. Letter-spacing is consistently tightened at -0.01em across all sizes, giving the rounded Poppins letterforms a slightly more compact, intentional feel rather than the default airy spacing.
- Inter `--font-inter` for Secondary fallback used only in 24 specific UI spots - effectively negligible. Treat as legacy or data-table context, not a design system font.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 32px.
- Element gap: 20px.

Build these component patterns where relevant:

- Pill Primary Button (Violet): Main call-to-action - 'Get started free', primary conversion actions
- Pill Ghost Button: Secondary CTA - 'Book a demo' on lavender canvas
- Dark Pill Button (Nav): High-contrast nav action - 'Get Started' in the top right
- Outlined Nav Button: Secondary nav action - 'Book a Demo' in top right
- Announcement Bar: Top-of-page promotional strip
- Top Navigation: Primary site navigation
- Product Mockup Card: Hero product screenshot container
- Calendar Time Block: Functional UI element inside the product - represents scheduled focus time
- Stat Number Block: Large metric display in the social-proof band
- Trust Badge Row: Social proof microcopy under hero CTAs
- Feature Card: Mid-page feature highlights
- Gradient Hero Text: Signature hero headline treatment

Do:

- Use Poppins exclusively for all text; never substitute Inter, Roboto, or system fonts in production UI
- Set border-radius to 100px for all buttons, tags, and avatars to maintain the pill-shaped identity
- Use Iris Violet (#5562eb) as the single primary action color - never introduce a second blue or accent for CTAs
- Keep headlines at weight 300 or 400 - never bold (600+) display text, the whisper-weight is the signature
- Apply the violet-to-green gradient (linear-gradient(120deg, #5562eb 40%, #7ac17b 61%)) only to hero headline words, not to buttons or backgrounds
- Use the lavender canvas (#ebefff) as the page base - white-only pages break the brand atmosphere
- Reserve Focus Green (#7ac17b) for calendar time blocks and positive stat numbers, not for success toasts or status badges

Avoid:

- Do not use drop shadows on cards - Reclaim uses border-radius and surface contrast instead of elevation
- Do not introduce a new accent color (orange, pink, teal) - the system is two-color: Iris Violet + Focus Green
- Do not use weight 700 or 800 for any text - Poppins tops out at 600 and most display text is 300-400
- Do not use 0px border-radius on any container - minimum 3px, standard 10px for cards
- Do not apply the violet-green gradient to buttons, backgrounds, or full headlines - only individual words in hero text
- Do not use pure white (#ffffff) as the page background - the lavender canvas is the brand base
- Do not use box-shadow for hover or focus states - use color shift to Sapphire Violet (#3451e8) instead

Source prompt cues:

**Quick Color Reference**
- text: #181d25 (primary), #474747 (muted)
- background: #ebefff (canvas), #ffffff (cards)
- border: #ececec (hairline), #5562eb (interactive)
- accent (text/gradient word): #5562eb #7ac17b gradient
- primary action: no distinct CTA color

**3 Example Component Prompts**

1. *Hero headline with gradient accent word*: Render a headline at 90px Poppins weight 300, #181d25, letter-spacing -0.9px. The second word in the headline uses a linear-gradient(120deg, #5562eb 40%, #7ac17b 61%) text fill. Below: Poppins 16px weight 400, #474747 subtitle. CTAs: Iris Violet (#5562eb) pill button (100px radius, white text, Poppins 14px weight 500, 16px/24px padding) and a ghost pill button (100px radius, transparent fill, 1.5px #5562eb border, #5562eb text). Canvas: #ebefff.

2. *Product mockup card*: White (#ffffff) surface, 10px border-radius, no shadow, 32px internal padding, placed on a #ebefff lavender canvas. Inside: a simplified calendar grid with day headers (MON/TUE/WED) in Poppins 11px weight 500, #474747, and Focus Green (#7ac17b) 3px-radius time blocks with white Poppins 12px text.

3. *Stat number band*: Four columns separated by 1px #ececec vertical dividers. Each column: Focus Green (#7ac17b) at 90px Poppins weight 300 for the number, with a Slate (#474747) Poppins 14px weight 400 label below. Background: white or lavender canvas. Section sits inside a max-width 1200px container.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
