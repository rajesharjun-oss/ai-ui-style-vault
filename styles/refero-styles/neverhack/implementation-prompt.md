# AI Implementation Prompt

Build a NEVERHACK-inspired interface using this source-derived style bundle.

Reference site: https://neverhack.com/en
Theme: light
Category: SaaS
North star: encrypted command terminal on cold marble

Use these palette anchors:

- Sovereign Ink `#0a0f1f` for Primary text, headlines, nav, core UI - near-black with a barely-perceptible blue cast that separates it from pure black and lets violet accents feel native
- Signal White `#ffffff` for Card surfaces, elevated panels, button text on dark fills
- Mist Surface `#f6f7fc` for Page canvas, soft card backgrounds, subtle wash sections
- Cool Hairline `#e5e7eb` for Borders, dividers, input outlines, structural separators - the single neutral that holds the whole UI together
- Shadow Lichen `#d8d7e2` for Card inset shadow tint, quiet elevation layer
- Carbon Gray `#4e4e4e` for Secondary text, supporting copy, muted labels
- Ash Gray `#999999` for Button shadow tint, disabled affordances, tertiary text
- Violet Wash `#afa9fd` for Tinted backgrounds for AI-adjacent surfaces, soft highlight washes, capability tags
- Cyber Cyan `#28d3fe` for Blue wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Crimson Glow `#f4baba` for Red supporting accent for decorative details and low-frequency emphasis. Use as a supporting accent, not as a status color
- Info Blue `#2563eb` for Informational badges, neutral data callouts, non-critical status indicators

Use these typography anchors:

- Roobert `--font-roobert` for Single-family system. Roobert's geometric-humanist forms handle the full scale from 11px micro-labels to 72px display headlines. The custom face's slightly condensed proportions and subtle stroke contrast make headlines feel like terminal readouts rather than marketing copy. Weight 400 carries most UI; weight 500 is reserved for nav items, button labels, and emphasis. Letter-spacing tightens aggressively as size grows: -0.03em at 72px down to neutral at body sizes; micro-labels and ALL-CAPS badges open up to +0.08-0.12em for legibility

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 32px.
- Element gap: 12px.

Build these component patterns where relevant:

- Primary Filled Button (Dark): Default CTA for key actions: 'Ask PROMETHEUS', 'How we work', 'Explore capabilities'
- Ghost Outlined Button: Secondary CTA, paired alongside primary dark button
- Nav Pill Button (Active State): Active nav highlight, as seen on 'Cyber AI' in header
- Alert Emergency Button: Reserved for CERT/crisis actions only - 'Activate emergency response'
- Capability Card: Three-up feature cards in 'End-to-end cyber coverage' section
- Highlight Card (Capability Expanded): Larger 'Technology Resale' style card with sub-list and visual treatment
- Principle Card: Three-column principle cards in 'Three principles, one operating standard'
- Chat Surface (AI Interaction): Hero chat widget showing AI conversation
- Eyebrow Label / Tag: ALL-CAPS section identifiers: 'SOVEREIGN CYBERSECURITY & AI', 'CAPABILITIES'
- Category Badge: Tag above capability card titles: 'AI', 'MSP', 'CRITICAL'
- Sector Ticker Bar: Horizontal scrolling industry sector labels: 'Finance, Health, Industry, Telecoms...'
- Top Banner (Notification): Slim announcement bar at very top of page

Do:

- Use 9999px radius for all interactive elements: buttons, badges, chat input, nav pills
- Set the primary CTA to Sovereign Ink (#0a0f1f) on Signal White text - never let Alert Crimson become the default action
- Apply the purple-tinted shadow stack (rgba(40,30,93,*) values) to all elevated cards and chat surfaces for brand-coherent depth
- Tighten letter-spacing aggressively at large sizes: -0.03em at 72px, -0.025em at 52px, -0.02em at 40px
- Open letter-spacing on ALL-CAPS eyebrows and badges: +0.08 to +0.12em for legibility at small sizes
- Reserve Alert Crimson (#dc2626) exclusively for CERT, crisis, emergency, and hazard contexts - its rarity is the signal
- Use Sovereign Violet (#6b2bea) as the AI signature: chat responses, brand dots, capability tags, decorative strokes

Avoid:

- Don't use Alert Crimson for non-critical actions, marketing copy, or decorative emphasis - it loses meaning through overuse
- Don't pair Sovereign Violet with Alert Crimson in the same component - the two chromatic accents must stay in separate semantic lanes
- Don't add shadows to text, icons, or small UI elements - elevation belongs only on cards, chat surfaces, and the primary CTA
- Don't use 72px or 52px display sizes for sub-headings or section intros - those are hero-only; step down to 32-40px for section openers
- Don't introduce new chromatic colors beyond the defined palette - the 5% colorfulness is the brand contract
- Don't use pure black (#000000) for body text - Sovereign Ink (#0a0f1f) is the only acceptable text color; black is reserved for nav border accents and button micro-details
- Don't apply soft radius (6-14px) to buttons or interactive controls - only cards, inputs, and nested elements use measured radii

Source prompt cues:

**Quick Color Reference**
- text: #0a0f1f (Sovereign Ink)
- background: #f6f7fc (Mist Surface)
- card: #ffffff (Signal White)
- border: #e5e7eb (Cool Hairline)
- accent: #6b2bea (Sovereign Violet)
- primary action: #dc2626 (filled action)

**Example Component Prompts**
1. Create a Primary Action Button: #dc2626 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
2. *AI Chat Card*: 18px radius, #ffffff fill, shadow rgba(40,30,93,0.25) 0px 30px 45px -30px + rgba(0,0,0,0.1) 0px 18px 36px -18px. User message bubble: #e5e7eb fill, #0a0f1f text, 14px. AI response bubble: #6b2bea fill, #ffffff text, 14px weight 500. Input: pill 999px radius, 1px #e5e7eb border, 14px placeholder in #4e4e4e.
3. *Capability Card*: 14px radius, #ffffff fill, 1px #e5e7eb border, shadow rgba(40,30,93,0.04) 0px 4px 12px -4px + rgba(0,0,0,0.03) 0px 1px 2px. Category badge: 6px radius, 10px 12px padding, 11px ALL-CAPS weight 500, #6b2bea on #afa9fd wash. Heading 24px weight 500 #0a0f1f. Body 16px weight 400 #4e4e4e. 'Learn more ' link in #6b2bea, 15px weight 500.
4. *Critical Alert Card*: 14px radius, #ffffff fill, 1px #e5e7eb border. Badge: 9999px radius, #dc2626 fill, 11px ALL-CAPS #ffffff weight 500. Heading 24px weight 500 #0a0f1f. CTA: 9999px radius, #dc2626 fill, #ffffff text, 12px 24px padding, 15px weight 500, shadow with warm red tint.
5. *Principle Column*: No border, no background. Top accent: 2px tall x 24px wide colored bar (use #6b2bea, #2563eb, or #28d3fe). Heading 24px weight 500 #0a0f1f. Body 16px weight 400 #4e4e4e, line-height 1.60.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
