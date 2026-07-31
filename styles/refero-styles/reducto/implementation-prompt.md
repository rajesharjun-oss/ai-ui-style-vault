# AI Implementation Prompt

Build a Reducto-inspired interface using this source-derived style bundle.

Reference site: https://reducto.ai
Theme: light
Category: AI
North star: Magazine on warm paper

Use these palette anchors:

- Aubergine `#310632` for Primary text, headline color, nav active state, link accent, footer text - the deep plum that replaces black across the entire interface, giving body copy a warm violet cast instead of cold gray
- Magenta Pulse `#9d17a0` for Filled primary action background, selected nav indicator, brand icon color - the single vivid hue permitted on a CTA, used sparingly so the click target glows against the paper canvas
- Damson `#690f6b` for Outlined action border, secondary button outline - a darker shade of the action magenta, used when a ghost/outlined button needs chromatic weight without the filled fill
- Lilac Wash `#dcbffb` for Violet text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color
- Ochre `#a2541b` for Decorative icon accent, illustrative highlight - used inside product visualizations and tag chips to add warm contrast against the dominant magenta/plum palette
- Moss `#718613` for Decorative icon and illustration accent - secondary chromatic note for data visualization callouts, kept low-frequency
- Reed `#87a017` for Green text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color
- Paper `#fafaf9` for Page canvas, hero background, nav background - the warm off-white that defines the entire site's surface; never pure #ffffff at the top level
- Vellum `#f5f5f4` for Secondary surface, elevated card background, subtle section differentiation
- Snow `#ffffff` for Pure card surface, button text on dark/magenta fills, icon fill - only used as a surface lift or as foreground text, never as the page canvas
- Sand `#d7ccc1` for Primary border color, hairline dividers, card outlines - the warm beige border that replaces cold gray; the single most-used border token across the system
- Driftwood `#e7e5e4` for Subtle border, decorative separator, low-contrast outline - lighter than Sand for secondary dividers
- Stone `#d6d3d1` for Nav border, button border, body border - mid-tone warm gray for structural outlines where more contrast is needed than Sand provides
- Graphite `#292524` for Secondary body text, navigation labels, and subdued headings. Do not promote it to the primary CTA color
- Slate `#57534d` for Secondary heading text, icon stroke, strong body text - mid-dark warm gray for emphasis without going full black
- Pewter `#79716b` for Body text, nav text, button text on light backgrounds, helper text - the default readable text color, warm and low-contrast
- Bark `#44403b` for Neutral button treatment for secondary actions and selected controls.
- Ash `#a6a09b` for Muted helper text, disabled state, low-priority captions - the lightest readable neutral

Use these typography anchors:

- reductoSerif `--font-reductoserif` for Display and headline serif - the brand's signature voice. Set at 64-136px for hero/display, drops to 24-32px for section headings. Weight 470 is the workhorse (editorial body weight for a display face), weight 650 is reserved for stat numbers. The tight -0.01em tracking at every size is critical: it tightens the serif's natural rhythm into a modern, condensed look. Substituted with Playfair Display, Lora, or Source Serif Pro when unavailable.
- Inter `--font-inter` for Body and UI sans - the workhorse for nav links, buttons, descriptions, paragraphs, and form fields. Weight 400 for body, 500 for button labels and emphasized nav. Activates stylistic alternates 'salt' (single-storey 'a') and 'ss02' (open 'g') - these are essential to matching the brand; without them, Inter reads as generic.
- reductosans `--font-reductosans` for Compact UI sans for small labels, tag chips, micro-copy, and dense interface text where Inter feels too tall. Functionally overlaps with Inter but provides a tighter, more 'captured' rhythm for chrome.
- Reddit Mono `--font-reddit-mono` for Single-purpose display monospace for oversized stat numbers - the '2,000,000,000' counter. The -0.03em tracking pulls the mono's natural width inward so the number doesn't look like code, but a label. Substituted with JetBrains Mono or IBM Plex Mono.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 80px.
- Card padding: 24-32px.
- Element gap: 16-24px.

Build these component patterns where relevant:

- Announcement Bar: Top-of-page product announcement strip
- Top Navigation: Sticky site navigation
- Contact Sales Button (Dark Filled): Primary dark CTA in nav
- Magenta Primary Button: Hero CTA, primary conversion action
- Ghost/Outlined Button: Secondary action, demo request
- Hero Headline: Above-the-fold page title
- Hero Subtext: Supporting paragraph under headline
- Customer Logo Strip: Social proof row
- Stat Display Number: Oversized metric counter
- Feature Card: 3-column feature grid card
- Section Header: Centered section title block
- Product Visualization: Decorative document/data illustration

Do:

- Set all hero/display headlines in reductoSerif weight 470 at 64-136px with -0.01em letter-spacing; never use a sans face for a display heading.
- Use #9d17a0 (Magenta Pulse) as the only filled chromatic action background; pair it with white text and 12px 24px padding.
- Color exactly one word in a hero headline in #9d17a0 to create emphasis; this accent-word pattern is the system's signature rhythm.
- Use #d7ccc1 (Sand) as the default border color for all cards, dividers, and outlines; avoid cool gray borders.
- Set body copy in Inter 17px weight 400 at line-height 1.5 with 'salt' and 'ss02' features enabled - these alternates are non-negotiable for brand fidelity.
- Maintain a paper-canvas base: page background must be #fafaf9, never #ffffff; lift cards with #ffffff over the warm canvas instead of using shadows.
- Use Reddit Mono with -0.03em tracking at 80px for oversized stat numbers; the mono face signals 'this is a measurement, not a word'.

Avoid:

- Don't use black (#000000) for body or heading text; use Graphite (#292524) or Aubergine (#310632) to keep the warm palette consistent.
- Don't apply drop shadows to cards or sections; depth must come from border color contrast or white-on-warm layering, not from blur shadows.
- Don't use cool gray (#6b7280, #94a3b8, etc.) for borders or text - every neutral in this system is warm (brown- or beige-tinted).
- Don't activate the magenta action color on more than one element per viewport section; if the CTA is magenta, the nav must stay neutral.
- Don't use the reductoSerif face for body copy or UI labels under 24px; it loses legibility below that and breaks the display/utility split.
- Don't introduce additional chromatic accent colors beyond Ochre, Moss, and Lilac; the palette intentionally restricts to plum-family + warm neutrals + 2-3 illustration accents.
- Don't use #0000ee or default browser link blue; all links must use Aubergine or Lilac Wash.

Source prompt cues:

**Quick Color Reference**
- text: #292524 (Graphite) for headings, #79716b (Pewter) for body
- background: #fafaf9 (Paper) canvas, #ffffff (Snow) for cards
- border: #d7ccc1 (Sand) default, #d6d3d1 (Stone) for nav
- accent: #9d17a0 (Magenta Pulse) for emphasis words and the announcement bar
- primary action: #9d17a0 (filled action)

**3-5 Example Component Prompts**

1. Create a Primary Action Button: #9d17a0 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. *Build a feature card grid (3-column)*: White #ffffff card surface on #fafaf9 canvas, 1px #d7ccc1 border, 8px radius, 32px padding. Card title in reductoSerif weight 470 at 24px, color #292524. Card body in Inter 16px weight 400, line-height 1.5, color #79716b. Illustration area at top of card: flat outlined document mockup with #d7ccc1 bounding-box overlay and one #dcbffb accent tag. 24px gap between cards.

3. *Build the stat counter section*: #fafaf9 background. Small centered label 'Over' in Inter 14px weight 500, color #79716b. Oversized number in Reddit Mono weight 400 at 80px, line-height 1.13, letter-spacing -0.03em, color #292524. Decorative pixelated mosaic of small color squares (in #a2541b, #718613, #dcbffb, #310632) scattered above the number at low opacity as a background pattern.

4. *Build the top navigation*: #fafaf9 background, 1px #d6d3d1 bottom border, 60px height, 24px horizontal padding. Logo (icon + 'reducto' wordmark) left, nav links center in 14px Inter weight 500, color #79716b, 24px gap between links. Right side: 'Log in' as plain text link in #79716b, then dark filled button 'Contact sales' with #44403b background, white text, 4px radius, 8px 16px padding.

5. *Build the announcement bar*: Full-width strip, #9d17a0 background, 2px vertical padding. Centered text in Inter 14px weight 400, color #ffffff. No border-radius.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
