# AI Implementation Prompt

Build a Whop-inspired interface using this source-derived style bundle.

Reference site: https://whop.com
Theme: light
Category: SaaS
North star: Bold sticker on cream paper - a minimal light canvas with a single orange button that casts a hard burnt-orange shadow.

Use these palette anchors:

- Ember Orange `#fa4616` for Orange wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Ember Shadow `#b62600` for Hard 3px offset shadow beneath Ember Orange buttons - a deeper burnt orange instead of a soft drop shadow
- Carbon `#202020` for Primary text, heading strokes, heavy borders, icon fills
- Snow `#ffffff` for Card surfaces, button text on dark fills, the elevated layer above the page canvas
- Mist `#f9f9f9` for Page canvas - the near-white background that all sections sit on
- Silver `#e1e4e8` for Hairline dividers, card borders, subtle structural separators
- Slate `#646464` for Muted body text, secondary links, inactive nav items, mid-weight borders
- Ash `#838383` for Tertiary text, placeholder text, disabled labels
- Pearl `#bbbbbb` for Light borders, icon outlines, low-emphasis strokes
- Obsidian `#0a0a0a` for Dark surface variant for inverted cards or code-editor panels

Use these typography anchors:

- acidGrotesk `--font-acidgrotesk` for Display and section headlines - used at near-mega sizes (128px) for hero, 56px for section titles. Line-height locked to 1.00, tracking at -0.03em creates a compressed, poster-like quality. This is a custom geometric face; no system font replicates its personality.
- Inter `--font-inter` for All functional UI: body copy, links, buttons, nav, footer, card text, labels. Weight 400 for body, 500 for buttons and emphasized text, 600-700 for subheadings and strong labels. Tracking tightens as size increases (-0.016em at 20px down to -0.006em at 13px).
- Geist Mono `--font-geist-mono` for Code snippets, terminal prompts, technical metadata, version labels. Generous line-height (1.70) for multi-line code blocks. Normal letter-spacing - mono fonts don't need optical tightening.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 64-80px.
- Card padding: 24px.
- Element gap: 24px.

Build these component patterns where relevant:

- Primary CTA Button: The singular high-emphasis action - the only chromatic button in the system
- Ghost/Secondary Button: Low-emphasis action paired with the primary CTA
- Top Navigation Bar: Persistent site header
- Display Headline: Hero and section-level titles
- Phone Mockup Card: Product showcase tile in horizontal scroll galleries
- Tab Navigation (Pill Group): Switches between embed component examples (Checkout, Wallet, Chat)
- Code Editor Panel: Shows code snippets for embed components
- Footer: Minimal site footer
- Category Label (Showcase Section): Labels above each phone mockup (Agency, Game, Service business, etc.)
- Hero Section: Full-viewport above-the-fold area

Do:

- Use Ember Orange (#fa4616) exclusively for the single primary action on any screen - never for decorative elements, tags, or secondary buttons
- Apply the hard burnt-orange offset shadow (rgb(182,38,0) 0px 3px 0px 0px) only to primary CTA buttons
- Set display headlines in acidGrotesk at 56px or 128px with line-height 1.00 and letter-spacing -0.03em - never use Inter for display sizes
- Use 24px border-radius for all card-like containers and 8px for all buttons - this size ratio is non-negotiable
- Keep the page canvas #f9f9f9 and card surfaces #ffffff - never invert this hierarchy
- Use 64-80px vertical gaps between major sections to maintain the spacious rhythm
- Use Geist Mono exclusively for code, terminal prompts, and technical metadata - never for UI labels or body text

Avoid:

- Don't use Ember Orange for any element that isn't the primary action button on that screen
- Don't apply soft drop shadows, blur, or opacity-based shadows to any element - the system is flat
- Don't use display sizes (56px+) in Inter - Inter is for 13-20px functional UI only
- Don't add gradients - the system is entirely flat color
- Don't use neutral grays for decorative accents or illustrations - the palette is near-black to near-white with one orange
- Don't set border-radius values outside the four tokens: 4px, 8px, 12px, 16px, 24px
- Don't place multiple orange buttons on the same screen - one primary action per view

Source prompt cues:

**Quick Color Reference:**
- Background: #f9f9f9 (Mist) - page canvas
- Card surface: #ffffff (Snow) - elevated containers
- Text: #202020 (Carbon) - primary
- Muted text: #646464 (Slate) - secondary
- Border: #e1e4e8 (Silver) - hairline dividers
- primary action: no distinct CTA color

**Example Component Prompts:**

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

2. **Phone Mockup Card**: White surface #ffffff, border-radius 24px, padding 24px, containing a phone screenshot at full width. Label above: 'Agency' in Inter 14px weight 500, #202020, centered. 24px gap between cards in a horizontal row.

3. **Tab Navigation**: Pill container with #e1e4e8 background, border-radius 8px. Three tabs: 'Checkout' (active: white background, #202020 text, Inter 600 14px), 'Wallet' (inactive: transparent, #646464 text), 'Chat' (inactive: transparent, #646464 text). 12px horizontal padding per tab.

4. **Code Editor Panel**: Dark surface #0a0a0a, border-radius 12px, padding 24px. Terminal prompt '$ npm install @whop/checkout' in Geist Mono 14px weight 500, #ffffff text. No border, no shadow.

5. **Top Navigation**: White #ffffff background, full-width. Left: 'Whop' logo (mark + wordmark in #202020). Right: 'For enterprise', 'API', 'Sign in' in Inter 14px weight 500, #646464, 24px gap between links. No border, no shadow.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
