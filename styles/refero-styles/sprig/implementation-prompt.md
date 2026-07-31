# AI Implementation Prompt

Build a Sprig-inspired interface using this source-derived style bundle.

Reference site: https://sprig.com
Theme: light
Category: SaaS
North star: editorial research notebook on warm paper - quiet, almost inkless, with warm light leaking in at the edges

Use these palette anchors:

- Abyssal Ink `#0b2330` for Primary text, nav links, borders, icon strokes - the workhorse near-black with a whisper of navy. Carries every reading surface in the system
- Bone `#faf9f8` for Page canvas, card surfaces, button text on dark fills - a warm off-white, never pure #fff
- Obsidian `#141312` for Headings, display text, strong UI fills - slightly warmer than Abyssal, used where headings need a touch more warmth
- Espresso `#272420` for Filled button background (primary action), dark surface sections - the primary CTA color, a warm near-black
- Carbon `#000000` for Absolute dark for SVG fills and the strictest contrast moments - used sparingly where true black is needed
- Ash `#f3f3f3` for Card surfaces, badge backgrounds, subtle elevated panels - the first step up from the canvas
- Mist `#e8e7e6` for Borders, dividers, secondary surface fills - a warm gray that defines edges without drawing attention
- Vapor `#dddcd9` for Lightest visible border, ghost button outlines - the quietest edge in the system
- Pebble `#c4c4bc` for Muted body text, subdued metadata, tertiary information
- Fog `#9a9a91` for Disabled text, placeholder text, very subdued heading accents
- Smoke `#8f8d8b` for Mid-tone surface fills, pressed button states
- Graphite `#6e6d6a` for Tertiary text, subtle borders, icon strokes in secondary contexts
- Slate `#575653` for Body text, nav borders, link underlines - the mid-neutral for readable secondary information
- Coffee `#322e2a` for Deep dark surface, image borders, the second-darkest fill - used in footer-adjacent surfaces and image frames
- Ember `#eba370` for Gradient mid-stop - coral-orange transition in the signature sunset gradient
- Twilight `#7d7a8f` for Gradient end - muted purple-gray closing the sunset gradient

Use these typography anchors:

- TT Commons Pro `--font-tt-commons-pro` for Functional UI typeface - nav links, button labels, badge text, small labels. Single weight 400 is a deliberate choice: the interface whispers instead of shouts. Used at 16-18px for UI chrome and at 40px for one rare editorial moment.
- ABC Diatype `--font-abc-diatype` for Editorial typeface - display headings at 40px weight 500, section headings at 32px weight 500, subheadings at 24px weight 400, body at 16px. The geometric construction gives the system its quiet authority; the weight 500 (not 600-700) for headings is the anti-convention choice that defines Sprig's restraint.

Use these layout rules:

- Base spacing: 8px.
- Density: spacious.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 48px.
- Element gap: 8px.

Build these component patterns where relevant:

- Primary Filled Button: The sole filled button in the system. Used for the primary conversion action on every page.
- Ghost/Outline Button: Secondary actions, nav-adjacent controls, less prominent conversion paths.
- Top Announcement Banner: Site-wide thin bar above the navigation, used for launches, events, or product announcements.
- Primary Navigation Bar: Main site navigation - logo left, center nav links, sign-in and CTA right.
- Large Product Preview Card: Hero or feature-section visual - the product UI shown inside a gradient frame.
- Event/Content Card: Cards in the events section and similar content grids - image or gradient background with overlay text.
- Logo Bar: Social proof section - trusted-by logos in a single horizontal row.
- Badge / Tag: Small category labels, event types, or metadata pills.
- Section Heading Block: Editorial-style section openers - large text, generous space, minimal ornament.
- Hairline Divider: Section separator, structural edge between content bands.
- Feature Highlight Section: Alternating two-column sections - text on one side, visual on the other.
- CTA Card / End-of-Page Banner: Closing conversion section with a large headline and primary action.

Do:

- Use #272420 (Espresso) as the only filled button background - never introduce blue, red, or green for buttons
- Set all filled and ghost buttons to 32px border-radius (full pill) with 12px horizontal x 6px vertical padding
- Use ABC Diatype at weight 500 for all headings 24px and above - never go to weight 600 or 700
- Set large feature cards to 100px border-radius and special hero cards to 1600px - the curvature is the system's signature
- Apply the Dusk Ember Twilight gradient (linear) only as a backdrop for product UI or as event card backgrounds - never on text, borders, or controls
- Keep the page canvas at #faf9f8 (Bone) with 1px Mist (#e8e7e6) dividers instead of alternating background bands
- Left-align all text content - body, headings, and CTAs - never center body copy or section openers

Avoid:

- Do not add drop shadows to any component - use surface tone shifts and curvature instead
- Do not introduce a secondary brand color - the system is monochrome plus warm gradient, and adding blue, green, or red breaks the editorial register
- Do not center body text or feature descriptions - left-alignment is structural, not stylistic
- Do not use border-radius below 4px on any visible element - the system commits to soft, never sharp
- Do not apply the warm gradient to text, icons, or UI controls - it is reserved for image backdrops and large decorative cards
- Do not use bold (weight 700) anywhere - ABC Diatype 500 is the maximum, TT Commons Pro is weight 400 only
- Do not alternate between light and dark section backgrounds to create rhythm - use hairline dividers and generous spacing instead

Source prompt cues:

**Quick Color Reference**
- text: #0b2330 (Abyssal Ink)
- background: #faf9f8 (Bone)
- border: #e8e7e6 (Mist)
- accent: warm gradient (Dusk #efdcb6 Ember #eba370 Twilight #7d7a8f)
- primary action: #272420 (filled action)

**Example Component Prompts**

1. Create a Primary Action Button: #272420 background, #faf9f8 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.


3. **Event Card Grid**: 4 cards in a horizontal row, each 100px border-radius, variable aspect ratio ~3:4. First card: warm gradient background (Dusk Ember) with Bone text overlay. Second card: solid dark background (#141312) with Bone text. Third card: full-bleed photography of a person. Fourth card: light gradient (warm beige) with Abyssal Ink text. No borders, no shadows between cards. 24px gap between cards.

4. **Feature Section (text + visual)**: Two-column layout at 1200px max-width, left-aligned text in left column, visual in right column. 80px section gap above. Text: 40px ABC Diatype weight 500 heading in #0b2330, 16px body in #575653, 24px gap between heading and body. Visual: product screenshot inside 100px-radius card on Dusk Twilight gradient.

5. **Logo Bar**: Full-width row, no container, no border. 6-8 client logos (Microsoft, Figma, DoorDash, Clay, Notion, Ramp style) evenly spaced in a single horizontal line, each in their native brand color. 48px vertical padding above and below.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
