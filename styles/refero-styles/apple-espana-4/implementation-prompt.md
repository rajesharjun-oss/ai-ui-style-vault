# AI Implementation Prompt

Build a Apple (Espana)-inspired interface using this source-derived style bundle.

Reference site: https://www.apple.com/ipad-air
Theme: light
Category: E-commerce
North star: white gallery vitrine

Use these palette anchors:

- Pure White `#ffffff` for Page canvas, card surfaces, nav background, icon fills
- Fog Mist `#f3f6f6` for Footer surface, secondary card tint, alternating section backgrounds
- Paper Gray `#fafafc` for Opened nav menu surface - barely-distinguished from white canvas
- Silver Smoke `#e8e8ed` for Tertiary surface, subtle dividers, chip backgrounds
- Ash Border `#dedfe2` for Hairline separators, disabled button backgrounds
- Graphite `#6e6e73` for Secondary body text, captions, helper labels
- Charcoal `#444545` for Nav text, secondary nav and link text
- Steel `#313131` for Nav icon fills, button text on light surfaces, dark surface tint
- Near Black `#1d1d1f` for Headlines, primary body text, all editorial copy - the dominant ink
- True Black `#000000` for Icon fills, input underline, maximum-emphasis headings
- Apple Blue `#0071e3` for Primary action fill - the only chromatic button color, also nav hover and focus ring
- Link Blue `#0066cc` for Inline text link color, secondary link accent
- Ember `#b64400` for Orange state accent for badges, validation surfaces, and short status labels.

Use these typography anchors:

- SF Pro Text `--font-sf-pro-text` for Body, navigation, micro-copy, and smaller headings. 17px/400 for primary body (line-height 1.47), 14px/600 for eyebrow labels and small link lists, 12px/400 for legal and fine print, 44px/400 for nav bar text, 34px/600 for card sub-headings.
- SF Pro Display `--font-sf-pro-display` for Display and editorial headlines - 80px hero, 56px section opener, 48px feature, 28px sub-feature, 21px large body. Negative letter-spacing tightens as size increases (-0.015em at 80px down to 0.011em at 21px). The only family used at sizes 40px.
- Arial `--font-arial` for Arial - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1440px.
- Section gap: 80px.
- Card padding: 40px.
- Element gap: 10px.

Build these component patterns where relevant:

- Hero Product Spotlight: Full-bleed product reveal section
- Primary Blue Pill Button: Single primary action per section
- Text-Link Button: Secondary or tertiary action - Apple's default
- Outlined Pill Link: Tertiary navigation-style action
- Feature Card (White): Product or feature showcase panel
- Feature Card (Tinted): Secondary feature panel with subtle surface tint
- Global Navigation Bar: Persistent top navigation
- Section Header Block: Editorial section title with optional inline link
- Eyebrow Label: Small uppercase or sentence-case category label above headlines
- Inline Text Link: Hyperlink within paragraph copy
- Price Block: Starting price display
- Badge (New / Limited): Product freshness indicator

Do:

- Use #0071e3 (Apple Blue) as the only filled button color - one per section maximum, never two blue buttons side by side.
- Set all card radii to 28px and pair with zero border, zero shadow - let container background tint create separation.
- Set hero headlines at SF Pro Display 80px weight 600 with letter-spacing -1.2px and line-height 1.05.
- Anchor all body copy in SF Pro Text 17px weight 400 at line-height 1.47 with letter-spacing -0.37px.
- Use 980px border-radius on every pill-shaped button so it renders fully round regardless of width.
- Maintain minimum 80px vertical gap between editorial sections; hero sections get 160px+ breathing room.
- Reserve #0066cc exclusively for inline text links within paragraph copy; never as a standalone chip.

Avoid:

- Do not use any chromatic color other than #0071e3 for buttons - no orange, green, or red CTAs.
- Do not add borders or drop-shadows to cards; separation must come from surface tint or whitespace alone.
- Do not use sans-serif weights below 400 or decorative typefaces; the system is two families (SF Pro Display, SF Pro Text) only.
- Do not place two filled buttons in the same row - pair a single filled button with a text-link or an outlined pill.
- Do not use letter-spacing wider than 0.011em on any size; the system is always tight or normal tracking.
- Do not introduce background colors other than #ffffff, #fafafc, #f3f6f6, and #e8e8ed for surfaces.
- Do not use radius values other than 12px (small), 28px (card), 32px (nav pill), or 980px+ (full pill) - no 4px or 8px rounded corners.

Source prompt cues:

Quick Color Reference:
- text: #1d1d1f
- background: #ffffff
- border: #dedfe2
- accent: #0071e3
- link: #0066cc
- primary action: #0071e3 (filled action)

Example Component Prompts:
1. Hero section: #ffffff background, no card chrome. Headline 'iPad Air' in SF Pro Display 80px weight 600, color #1d1d1f, letter-spacing -1.2px, line-height 1.05, centered. Subtitle in SF Pro Display 28px weight 600 #1d1d1f centered below. Product render centered with 160px vertical breathing room above and below.
2. Feature card: #ffffff background, border-radius 28px, no border, no shadow, 40px internal padding. Headline SF Pro Display 48px weight 600 #1d1d1f. Body SF Pro Text 17px weight 400 #6e6e73. Text-link button below body: transparent fill, color #0066cc, with right-arrow , zero padding.
3. Create a Primary Action Button: #0071e3 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
4. Section header: left-aligned SF Pro Display 56px weight 600 #1d1d1f letter-spacing -0.28px. Right-aligned text link 'Ver el video' in SF Pro Text 17px weight 400 #0066cc on the same baseline. 80px vertical gap to following content.
5. Inline text link within paragraph: SF Pro Text 17px weight 400 body copy in #6e6e73, with one inline link in #0066cc no underline at rest, underline on hover. Sits mid-paragraph with zero padding and no chrome.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
