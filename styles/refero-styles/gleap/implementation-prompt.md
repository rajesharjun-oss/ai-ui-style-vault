# AI Implementation Prompt

Build a Gleap-inspired interface using this source-derived style bundle.

Reference site: https://gleap.io
Theme: light
Category: SaaS
North star: warm cream-paper workspace with graphite accents - a studio where matte-black ink dots float over linen architecture.

Use these palette anchors:

- Linen Canvas `#edede8` for Page background, section surfaces - warm off-white that pushes the whole system toward paper rather than screen
- Frosted White `#ffffff` for Card surfaces, elevated panels, glass overlays - clean white floats above the linen canvas for primary content
- Warm Stone `#dbdbd2` for Secondary card fills, secondary button backgrounds, accent surface - sage-tinted beige gives neutral elements warmth without becoming chromatic
- Pebble `#c0c0c0` for Circular accent tiles, muted card backgrounds - cool gray that sits one step back from stone for de-emphasized surfaces
- Graphite Ink `#141414` for Primary action button background, dark text on light surfaces - near-black with a hair of warmth, anchors every CTA
- Charcoal Body `#292929` for Primary body and heading text - readable but softer than pure black, keeps long-form copy from feeling harsh
- Slate Caption `#6f6f6e` for Secondary body, helper text, descriptive copy - carries the most volume of any text color
- Ash Subheading `#8f8f8e` for Subtle labels, muted headings, decorative type - sits between caption and hairline
- Iron Nav `#353535` for Secondary body text, navigation labels, and subdued headings. Do not promote it to the primary CTA color
- Onyx Border `#000000` for Hairline borders, strong dividers, selected-state outlines - used at 1-2px to outline cards, buttons, and focus rings
- Quartz `#d0d0c8` for Quietest surface tint, reserved for low-contrast dividers and hover-state hints
- Lime Pulse `#4cc02b` for Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color

Use these typography anchors:

- Switzer `--font-switzer` for Primary typeface for all UI, body, headings, and buttons. Weight 400 dominates even at display sizes - headlines whisper rather than shout, which gives the brand authority through restraint. The Minor Third scale (1.2) is unusually compressed for a SaaS site, so sizes cluster more tightly than a Major Third or Perfect Fourth system would produce.
- system-ui `--font-system-ui` for Icon-internal text and OS-native labels - minimal usage, mostly decorative
- sans-serif `--font-sans-serif` for sans-serif - detected in extracted data but not described by AI

Use these layout rules:

- Base spacing: 6px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 18px.
- Element gap: 9px.

Build these component patterns where relevant:

- Pill Button - Dark (Primary): Primary CTA
- Pill Button - Stone (Secondary): Secondary action, pricing CTA
- Pill Button - Ghost (Tertiary): Inline link, low-emphasis action
- Square White Button: Consent dialog action
- Feature Card - Warm Stone: Feature highlight, de-emphasized panel
- Feature Card - White: Primary content panel
- Glass Overlay Panel: Floating widget, sticky chat
- Circular Accent Tile: Category icon container, decorative dot
- Navigation Bar: Top-level site navigation
- Pricing Card: Pricing tier display
- Trust Bar: Social proof row
- Status Dot: Online indicator, success pulse

Do:

- Use 200px border-radius on every button and pill - the capsule shape is non-negotiable for brand recognition
- Set primary CTAs to #141414 fill with white text; use the stone (#dbdbd2) capsule as the default for any non-purchase action
- Keep headlines at weight 400 Switzer with -0.01em tracking at 64px and below, -0.02em at 80px display - never bold a headline above body weight
- Use the linen canvas (#edede8) as the base; place white (#ffffff) cards on top for contrast, and step down to stone (#dbdbd2) for de-emphasized content
- Apply backdrop-filter blur(12px) to any panel that floats over imagery or gradient backgrounds
- Use #4cc02b Lime Pulse only as a status dot or checkmark - never as a button fill, page accent, or decorative color
- Pair the 6px base unit for inline gaps with 18px card padding and 80px section gaps to maintain the comfortable density

Avoid:

- Don't introduce a brand-colored CTA - the system is intentionally chromatic-free; colored buttons would break the architectural language
- Don't use bold (600+) on headlines - weight 400 at display sizes is the signature; heavier weights belong in buttons and badges only
- Don't stack more than three surface tones in one screen (canvas white stone); the palette is rationed to preserve warmth
- Don't use drop shadows as decoration - if depth is needed, shift surface tone from white to stone to graphite instead
- Don't apply sharp corners to feature cards or panels - 12px is the floor for content surfaces; only consent dialogs may use 3.75px
- Don't add gradients to UI elements - the gradient zone is reserved for the hero product screenshot backdrop only
- Don't use letter-spacing wider than -0.01em on body copy; positive tracking breaks the tight architectural feel

Source prompt cues:

**Quick Color Reference**
- Text primary: #292929
- Text secondary: #6f6f6e
- Background (canvas): #edede8
- Surface (card): #ffffff
- Border (hairline): #0000001f
- Accent (status only): #4cc02b
- primary action: #141414 (filled action)

**Example Component Prompts**

1. *Create a hero section*: Linen canvas (#edede8) background, centered max-width 1200px. Display headline at 80px Switzer weight 500, color #292929, letter-spacing -1.6px. Sub-headline at 45px weight 400, color #292929. Body description at 19px weight 400, color #6f6f6e, line-height 1.4. Two CTAs centered: dark pill (#141414 fill, white text, 200px radius, 0 18px padding, 16px Switzer 400) followed by stone pill (#dbdbd2 fill, #292929 text, 200px radius, 0 24px padding).

2. Create a Primary Action Button: #141414 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

3. *Create a feature card*: White surface (#ffffff), 12px radius, 18px padding, no shadow. Optional 1px #0000001f border. Heading at 27px Switzer 400 in #292929. Body text at 16px Switzer 400 in #6f6f6e, line-height 1.5. Optional circular accent tile (background #c0c0c0, 50% radius, 40px diameter) at top of card containing an outlined icon in #353535.

4. *Create a floating chat widget*: Glass panel (rgba(255,255,255,0.7) with backdrop-filter blur(12px)), 6px radius, 18px padding, shadow rgba(0,0,0,0.3) 0 32px 68px 0. Header text at 16px Switzer 400 in #292929. Status indicator: 8px Lime Pulse (#4cc02b) circle to the left of any 'online' label. Position fixed bottom-right.

5. *Create a navigation bar*: Transparent background over linen canvas, height 60px, max-width 1200px centered. Logo at left in #292929 at 16px Switzer 500. Center nav links at 14px Switzer 400 in #353535 with 24px horizontal gap. Right cluster: Login link in #353535 + dark pill CTA (#141414 fill, white text, 200px radius, 0 18px padding).

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
