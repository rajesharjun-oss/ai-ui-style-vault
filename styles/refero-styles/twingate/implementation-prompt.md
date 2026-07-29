# AI Implementation Prompt

Build a Twingate-inspired interface using this source-derived style bundle.

Reference site: https://twingate.com
Theme: dark
Category: Dev Tools
North star: Midnight control room with violet and chartreuse signal lights. The whole interface sits on a near-black void, with two accent colors pulsing like status LEDs across instrument-panel components - restrained, engineered, and slightly futuristic without being showy.

Use these palette anchors:

- Void Black `#000000` for Page canvas, hero backgrounds, full-bleed sections
- Obsidian `#0e0f11` for Card surfaces, elevated panels, content containers above the page
- Carbon `#141617` for Secondary surface layer, input fields, nested containers
- Graphite `#1d2023` for Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color
- Slate `#21223a` for Subtle violet-tinted surface for spotlight/featured cards
- Ash `#303438` for Hairline borders and dividers, very low-contrast separation
- Steel `#3a3d40` for Slightly stronger borders, subtle outer shadow tint
- Fog `#61626b` for Muted helper text, disabled labels, low-priority metadata
- Smoke `#8d8d96` for Secondary icons, inactive navigation items, tertiary text
- Cloud `#a1a1aa` for Body text secondary, link text in resting state, icon strokes
- Silver `#cfcfd3` for Body text default, paragraph copy, description text
- Bone `#999999` for Captions, fine print, decorative text
- Paper White `#ffffff` for Primary headings, button text on dark fills, high-emphasis text
- Signal Violet `#b6abff` for Brand accent - highlighted phrases, feature body text, link emphasis, inline brand moments
- Live Wire `#eef35f` for Green supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Circuit Teal `#00cbaa` for Decorative icon and illustration accent - network node strokes, lock/connection diagrams, graphic highlights

Use these typography anchors:

- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI
- TT Hoves Light `--font-tt-hoves-light` for Display and headline - all large hero/section headlines (48-68px) use weight 300 with tight negative tracking (-0.018em to -0.007em). The whisper-weight at huge sizes is the brand's signature: confidence through restraint, not volume.
- TT Hoves Medium `--font-tt-hoves-medium` for Subheadings, feature card titles, navigation, button labels - the workhorse of the system. 32px appears as a mid-tier section heading, 20px as card titles.
- TT Hoves Regular `--font-tt-hoves-regular` for Body text and long-form copy - paragraph text at 16px with generous 1.5-1.7 line-height, smaller annotations at 11-14px
- Basis Grotesque Mono Pro `--font-basis-grotesque-mono-pro` for Code snippets, terminal-style text, and technical labels - used sparingly as a technical accent, never for body copy
- Inter `--font-inter` for Secondary body text and supporting UI labels (appears as a fallback/supplement to TT Hoves Regular in some contexts)

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 32px.
- Element gap: 20px.

Build these component patterns where relevant:

- Primary CTA Button (Pill): Main conversion action - 'Try Twingate for Free'
- Secondary Text Link Button: Low-emphasis action - 'Request a Demo'
- Nav Pill Button (Header): Header actions - 'Request Demo', 'Try for Free'
- Feature Card: Mid-page feature/benefit block in 3-column grid
- Eyebrow Pill Badge: Small context label above headlines - 'New: Twingate MSP Portal'
- Testimonial Card: Customer quote in a grid layout
- G2 Review Widget (Floating): Social proof callout - '4.9 '
- Customer Logo Strip: Social proof band of customer logos
- Product Showcase Card: Product UI screenshot with branded surround
- Network Diagram (Hero Illustration): Decorative hero visual - privileged access network
- Onboarding Banner (Top Bar): Persistent utility strip above navigation
- Header Navigation Bar: Primary site navigation

Do:

- Use weight 300 (TT Hoves Light) for all display headlines 48px and above - the whisper-weight is the signature
- Use #eef35f (Live Wire) for the single primary CTA on any given screen, and for one emphasis word in the largest headline
- Apply tight negative letter-spacing on all large text: -0.018em at 68px, scaling to 0 at 14px
- Use 50px (pill) border-radius for all buttons, badges, and pill-shaped chips
- Use 12px radius for product cards and image containers; 8px for inputs and smaller interactive elements
- Distinguish surfaces through tonal stacking (#000000 #0e0f11 #141617 #1d2023) rather than drop shadows
- Reserve Signal Violet (#b6abff) for inline brand emphasis within body text and for the top onboarding utility bar

Avoid:

- Never use drop shadows for elevation - the system communicates depth through inset hairline highlights and stacked dark surfaces
- Never use more than one filled chartreuse CTA per viewport - it is a single-action accent
- Never set body text below 14px or use weight 300 for body - light weights are reserved for large displays
- Never add decorative gradients - the system is flat dark with chromatic accents, not glossy
- Never use pure black (#000000) text on dark surfaces - text on dark should always be white or a silver tone (#cfcfd3 minimum)
- Never break the 50px pill convention for buttons - outlined or ghost variants must also use the full pill radius
- Never introduce photography with a warm or colorful treatment - all imagery is monochrome, vector, or UI-screenshot

Source prompt cues:

**Quick Color Reference**
- text: #ffffff (primary) / #cfcfd3 (body) / #a1a1aa (secondary)
- background: #000000 (canvas) / #0e0f11 (card) / #1d2023 (elevated)
- border: #303438 (hairline) / #3a3d40 (stronger)
- accent: #b6abff (violet) / #00cbaa (teal)
- primary action: no distinct CTA color

**Example Component Prompts**

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

2. *Feature card grid (3-column):* Transparent background. No card container. Subheading at 20px TT Hoves Medium weight 500 white. Body at 16px TT Hoves Regular #cfcfd3, line-height 1.7, with one emphasis phrase in #b6abff. 20px gap between cards.

3. *Pill badge:* #1d2023 background, 50px radius, 6px 12px padding, white text at 12px TT Hoves Medium, 0.012em letter-spacing, trailing chevron icon in white.

4. *Testimonial card:* #0e0f11 surface, 12px radius, 32px padding. Quote at 16px TT Hoves Regular #cfcfd3. 40px circular avatar, name at 14px Medium white, role at 12px Regular #8d8d96. No border, no shadow.

5. *Product showcase card:* #eef35f at 15-20% opacity as panel background, 12px radius, containing a dark UI mockup (carbon #141617 fill, 8px radius input fields, white text, small avatar circle). Eyebrow label above in #eef35f at 12px Medium.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
