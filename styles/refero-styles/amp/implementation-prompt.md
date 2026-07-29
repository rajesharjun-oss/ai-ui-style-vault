# AI Implementation Prompt

Build a amp-inspired interface using this source-derived style bundle.

Reference site: https://ampfit.com
Theme: light
Category: E-commerce
North star: warm orange pill on cool white. The design feels like a premium fitness product photographed in a sunlit loft: one object, one accent, one confident typeface doing all the work.

Use these palette anchors:

- Amp Orange `#ff6105` for Primary action fill, active step badge, accent rule, and brand strokes - the only chromatic color in the interface. Used at high contrast on white surfaces (7.0:1 against #ffffff) and as a warm border tint on cards and inputs
- Amp Glow `#ffa069` for Orange supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color
- Peach Wash `#ffdfcd` for Soft highlight surface for featured cards and step accents. A near-gray peach that stays quiet while adding warmth to a card stack
- Ink `#0a0a0a` for Primary text, logo mark, button text. 19.8:1 against white - the highest-contrast neutral in the stack
- Carbon `#292b2a` for Secondary text and nav links, slightly softer than Ink. Icon strokes also draw from this level
- Slate `#7a7b7b` for Neutral form states, badge text, and quiet UI feedback where color should stay understated.
- Ash `#a2a3a2` for Disabled link text and placeholder-level text - the quietest text tone before disappearing
- Graphite Hairline `#e5e5e5` for The dominant border color across the site - dividers, card borders, button outlines, and structural rules. By far the most-used neutral (1628+ borderColor occurrences)
- Fog `#dfe0df` for Soft border for cards and body blocks where #e5e5e5 reads as too crisp against off-white
- Bone `#e5e7eb` for Neutral button fill (88 occurrences) - the ghost/secondary button background. A light step above canvas
- Canvas White `#ffffff` for Page background, card surfaces, button text on dark and orange fills. The base of the surface stack
- Linen `#f3f4f3` for Off-white alt surface - secondary button fills and surface tints where pure white is too clinical
- Charcoal `#202120` for Dark elevated surface for cards, headers, and contained panels.
- Smoke `#3c3e3d` for Heading underline accent in dark sections, heavier than Carbon

Use these typography anchors:

- PublicaSans `--font-publicasans` for The only typeface in the system. Light 300 for display headlines, Regular 400 for body and UI, Medium 500 for buttons and emphasis. Tracking tightens with size: -0.036em at 72-78px, -0.030em at 48px, -0.020em at 32px, -0.010em at 16-18px, near-zero at body. The progressive tightening gives display sizes a magazine-cover feel while body text stays open and readable.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 16px.
- Element gap: 5-8px.

Build these component patterns where relevant:

- Primary Pill Button: The single CTA on most pages - Buy Now, Get Started.
- Secondary Pill Button: Lower-emphasis action when a primary exists on the same surface.
- Nav Buy Now Button: Persistent top-right CTA across all pages.
- Step Indicator Row: Onboarding step list with active state.
- Press Logo Strip: As-row, grayscale media logos under 'FEATURED ON' label.
- Editorial Section Heading: Large section title with accent rule underneath.
- Dark Feature Band: Full-bleed atmospheric section over a darkened product photo.
- Featured Card (Peach): Highlighted callout in a stack - e.g. the app onboarding card.
- Ghost Card: Default card surface in a feature grid.
- Announcement Bar: Thin top bar below the nav with a time-sensitive message.
- Top Navigation: Persistent header across all pages.
- Input Field (Pill): Single-line input in onboarding and form contexts.

Do:

- Use #ff6105 only for the primary CTA fill, the active step badge, the accent rule, and key brand strokes - never for body text or large background washes.
- Set display headlines at 48-78px in weight 300 with tracking between -0.030em and -0.036em; this is the signature editorial moment of the system.
- Round the primary CTA to 50px, secondary buttons to 24px, and cards to 5px - the radius ladder (5 / 8 / 24 / 32 / 50) defines component hierarchy.
- Apply the two-layer shadow stack (orange glow + neutral 1px lift) only to the primary CTA - no other element should carry elevation.
- Stack the surface ladder in this order: #ffffff #f3f4f3 #e5e7eb #ffdfcd #202120. Each step should feel like a deliberate lift, not a tint shift.
- Keep body copy in PublicaSans 16px weight 400 at line-height 1.5 with -0.01em tracking; reserve weight 500 for buttons, step titles, and short labels.
- Use the 2-3px #ff6105 accent rule beneath editorial headlines at roughly one-third of the heading width - it is the visual punctuation mark of the brand.

Avoid:

- Don't introduce a second accent color or a secondary brand hue - the system is monochrome + one orange, and any chromatic addition breaks the rationing.
- Don't use weight 600 or 700 in PublicaSans; the system tops out at 500. Heavier weights are not part of the type scale.
- Don't apply shadows to cards, images, or non-primary buttons. Flat-with-hairline-border is the default; elevation is a privilege, not a default.
- Don't use the 50px radius on anything except the primary CTA and inputs. 24px is the cap for secondary buttons, 5px for cards.
- Don't set display text in all-caps or with positive letter-spacing. Tracking only tightens as size grows; never loosens.
- Don't fill large areas with #ff6105. The orange is a punctuation mark - let it punctuate, not paint.
- Don't mix rounded and square corner systems on the same page. Pick from the 5 / 8 / 24 / 32 / 50 ladder and stay on it.

Source prompt cues:

**Quick Color Reference**
- text primary: #0a0a0a
- text secondary: #292b2a
- text muted: #7a7b7b
- background: #ffffff
- surface alt: #f3f4f3
- border hairline: #e5e5e5
- primary action: #ff6105 (filled action)

**Example Component Prompts**

1. *Primary CTA pill*: Fill #ff6105, white text, 50px border-radius, padding 16px vertical / 32px horizontal. PublicaSans weight 500, 16px, letter-spacing -0.01em. Box-shadow: rgba(255,97,5,0.6) 1px 6px 14px 0, rgba(0,0,0,0.06) 0 1px 4px 0. Optional trailing chevron in white.

2. *Editorial section heading*: PublicaSans weight 300, 48px, color #0a0a0a, letter-spacing -0.030em, line-height 1.2. Below the text, a 2px tall, 120px wide accent rule in #ff6105, aligned to the start of the heading. Section padding 80px top, 80px bottom.

3. *Featured onboarding card*: Fill #ffdfcd, 5px border-radius, padding 24px. Contains a phone mockup on the right (200px wide, 8px radius image frame). Step badge: orange pill #ff6105, white text 'Step 1', 8px radius, 12px / 12px padding. Step title in PublicaSans 18px weight 500 #0a0a0a with a 2px #e5e5e5 underline rule.

4. *Dark feature band*: Full-bleed background #202120 with a darkened product photo overlay at 65% opacity. White headline in PublicaSans weight 300, 48px, letter-spacing -0.030em, centered. A 60px wide, 2px tall #ff6105 accent rule centered below. Vertical padding 120px.

5. *Press logo strip*: Single horizontal row, logos rendered in #0a0a0a at 24-28px height, spaced 60px apart. Above the row, a 12px uppercase tracked label 'FEATURED ON' in #7a7b7b. Background #ffffff, padding 40px vertical.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
