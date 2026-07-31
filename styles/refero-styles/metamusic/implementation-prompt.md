# AI Implementation Prompt

Build a MetaMusic-inspired interface using this source-derived style bundle.

Reference site: https://metamusic.ca
Theme: mixed
Category: SaaS
North star: editorial cream broadsheet with sticker-flat accents - a warm-paper canvas where oversized type and hard-offset shadows replace all decoration.

Use these palette anchors:

- Brand Blue `#0066cc` for Primary action background, link underlines, heading accents, card fills on light surfaces - the single chromatic voice that powers CTAs, active states, and iconography
- Deep Indigo `#0e2575` for Dark section backgrounds (feature/why panels), hero image frames - the only place a full-bleed surface goes deep and saturated
- Midnight Card `#213680` for Elevated card surface when sitting on Deep Indigo backgrounds - one step lighter than the panel to separate without using shadow
- Charcoal Ink `#101820` for Body text and dark-surface secondary fills - slightly cooler than pure black, anchors reading text without harshness
- Paper Cream `#f4f1ea` for Primary page canvas - the warm base that gives the whole site its editorial, printed feel
- White `#ffffff` for Card surfaces, nav background, button text on blue, input fills - the clean highlight layer above cream
- Lavender Mist `#e6e0f8` for Neutral form states, badge text, and quiet UI feedback where color should stay understated. Do not promote it to the primary CTA color
- Ice Blue `#e9f4ff` for Alternate light surface wash, subtle card background variant - the cool counterpoint to Paper Cream
- Peach Blush `#f7e1d5` for Icon circle backgrounds in audience/feature cards - the only warm accent that breaks the cream-on-cream
- Ash Border `#d6d6d6` for Hairline dividers, subtle borders on neutral surfaces - the quietest structural line

Use these typography anchors:

- Maison Neue `--font-maison-neue` for The sole workhorse font across body, nav, headings, buttons, inputs, cards, and footers. Weight 400 carries body and UI labels; 500 steps up to subheadings and nav; 600 owns display sizes (56-120px). The type behaves like a neo-grotesque with humanist warmth - readable at 12px, monumental at 120px. Negative tracking tightens aggressively at display sizes (-0.03em at 120px, -0.02em at 56-80px, -0.01em at 32-40px) so headlines sit visually compact despite their scale.
- Spoof `--font-spoof` for Reserved for a single accent heading or card label at 22px / weight 500. Its ultra-tight 0.90 leading and -0.02em tracking create a display-quality mark at a mid size - used as a typographic exclamation point, never as a workhorse. Free substitute: GT America or a tight condensed sans like Druk Wide.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1280px.
- Section gap: 80px.
- Card padding: 40px.
- Element gap: 24px.

Build these component patterns where relevant:

- Display Headline: Hero and section-opening text
- Section Heading: Mid-page section titles
- Accent Eyebrow Label: Small blue label above section headings
- Primary CTA Button: Filled blue action button
- Outline Nav Button: Log-in / portal entry in header
- Ghost Arrow Button: Card continuation control
- Feature Card on Indigo: Numbered step card in dark sections
- Audience Card: Audience / "who's it for" card
- Text Input: Form fields
- Notification Banner: Top-of-page announcement bar
- Illustration Icon Circle: Decorative music/document icon
- Top Navigation Bar: Primary site navigation

Do:

- Use Maison Neue for all UI text; reserve Spoof for one accent heading at 22px per page maximum
- Apply the hard 4px black offset shadow only to interactive controls (buttons, nav items) - never to cards or images
- Stack the surface system in order: Paper Cream canvas White card Ice Blue wash Midnight Card on Deep Indigo; never mix more than two surface levels in one viewport
- Set display headlines at 80-120px with letter-spacing -0.02em to -0.03em; the tight tracking is what makes the oversized type feel intentional rather than bloated
- Use the 24px radius for all cards and the 9999px pill for all buttons and tags; 8px is reserved for inputs only
- Place Peach Blush icon circles only inside audience/feature cards - never on dark indigo surfaces where they would clash
- Use Card Padding 40px and Section Gap 80px as the rhythm; the 8px base unit governs all internal gaps

Avoid:

- Do not use soft, blurred drop shadows - the hard 4px solid offset is the only elevation language in this system
- Do not introduce new chromatic colors; Brand Blue and Deep Indigo are the only saturated voices, and they must not share a surface
- Do not set display type without negative letter-spacing; positive tracking at 56px+ destroys the editorial feel
- Do not use 8px radius on cards or 24px radius on inputs - the three-tier radius system (24px / 9999px / 8px) is strict
- Do not place text directly on Peach Blush or Lavender Mist without checking contrast - both are surface washes, not text backgrounds
- Do not add a second outlined pill button to the same view; the Log-in outline is a one-per-header accent
- Do not center body text longer than a single line; the editorial system relies on left-aligned, ragged-right reading

Source prompt cues:

Quick Color Reference:
- Text: #101820 (Charcoal Ink) on cream, #ffffff on indigo
- Background: #f4f1ea (Paper Cream) for pages, #0e2575 (Deep Indigo) for dark sections
- Border: #d6d6d6 (Ash) for hairlines, #0066cc (Brand Blue) for interactive borders
- Accent: #0066cc (Brand Blue) - the only chromatic voice
- Icon wash: #f7e1d5 (Peach Blush) circles for decorative icons
- primary action: #0066cc (outlined action border)

Example Component Prompts:

1. Create a hero section: Paper Cream (#f4f1ea) background, max-width 1280px centered. Accent eyebrow 'Discover MetaMusic' in Brand Blue (#0066cc) Maison Neue 500 at 16px. Headline 'Take control of your music metadata' in Charcoal Ink (#101820) Maison Neue 600 at 80px, lineHeight 1.05, letter-spacing -1.6px. Two cards below at 40px padding, 24px radius: left card is Brand Blue (#0066cc) background with white text 'Create a MetaMusic Beta account' plus a 40px Black circular arrow button; right card is White background with 1px Ash Border, Charcoal Ink text, same arrow button.

2. Create an audience section: Paper Cream background, 2-column layout. Left column: Accent eyebrow 'Who's it for?' in Brand Blue 16px, then 'MetaMusic is for everyone involved in local music!' in Charcoal Ink Maison Neue 600 at 56px, lineHeight 1.05, letter-spacing -1.12px. Right column: 4 stacked White cards, each 40px padding, 24px radius, containing a 48px Peach Blush (#f7e1d5) circle with a Brand Blue line-icon, a 19px Maison Neue 500 title, and 16px body text.

3. Create a dark feature section: Deep Indigo (#0e2575) full-width background, white text. Centered heading 'Why use MetaMusic?' in White Maison Neue 600 at 56px, with a Brand Blue link 'Discover MetaMusic's metadata management tool ' below. 4-column grid of Midnight Card (#213680) cards, 40px padding, 24px radius. Each card has a 32px Brand Blue circle with a white numeral (1-4) top-left, a White Maison Neue 500 title at 22px, and White body at 16px.

4. Create a text input: White background, 1px Lavender Mist (#e6e0f8) border, 8px radius, 16px padding, Maison Neue 400 at 16px, Charcoal Ink text. Focus state: border becomes Brand Blue (#0066cc), no shadow change.

5. Create the top navigation: White background, 64px height, Ash Border (#d6d6d6) 1px bottom hairline. Left: Brand Blue mark + Maison Neue 600 wordmark. Center-left: nav links (Discover the Tool, Help and training sessions, Resources, News, Contact us) in Maison Neue 500 at 16px Charcoal Ink. Right: Outline Nav Button - White background, 1px Black border, Charcoal Ink 'Log-in to the portal' text, 9999px radius, 12px 24px padding, 0px 4px 0px 0px #000000 shadow. Far right: globe icon + 'Fr' in Maison Neue 400 at 14px.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
