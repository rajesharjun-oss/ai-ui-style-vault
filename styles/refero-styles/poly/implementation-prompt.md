# AI Implementation Prompt

Build a Poly-inspired interface using this source-derived style bundle.

Reference site: https://poly.app
Theme: light
Category: SaaS
North star: Ember on porcelain - one warm gradient ember floating on an otherwise pure white editorial page, surrounded by quiet serif headlines and full-bleed photography.

Use these palette anchors:

- Ember Gradient `#f4824d` for Brand mark, Poly logo, the sole chromatic accent - warm orange fading to signal red, used only on identity, never on body UI
- Porcelain `#f4f4f4` for Page canvas, card surfaces, inverted text on dark photo backgrounds
- Onyx `#000000` for Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color
- Graphite `#292930` for Secondary text, hairline borders, icon fills, the slight warmth that keeps near-black from feeling clinical
- Ash `#cccccc` for Shadow tone used in the soft-etched link treatment, muted dividers

Use these typography anchors:

- Haffer Variable `--font-haffer-variable` for Primary display serif for headlines at 30-53px. Weight 450 is anti-convention - most product sites push display to 600-700, but Haffer at 450 keeps headlines warm and editorial rather than commanding. Activating liga and ss04 unlocks the alternative g and stylised letterforms that give the wordmark its personality.
- Bogue `--font-bogue` for Companion serif at regular weight, used for badge labels and secondary serif moments where Haffer 450 would feel too heavy. Tighter tracking at -0.03em distinguishes it from Haffer.
- Haffer `--font-haffer` for Static fallback for small serif text - 15px badges, 24px sub-serial moments
- Inter `--font-inter` for All UI, body, nav, button labels, helper text. Inter at 400 handles body, 600 carries subheadings and button text. The -0.02em tracking matches the serif family, keeping the type system visually unified.

Use these layout rules:

- Base spacing: .
- Density: comfortable.
- Page max-width: 1200px.
- Section gap: 48-69px.
- Card padding: 24px.
- Element gap: 12px.

Build these component patterns where relevant:

- Gradient Brand Mark: The Poly logo wordmark and cube icon
- Primary Dark Filled Button: Main conversion action (Join waitlist, Watch Video)
- Ghost Outlined Button: Secondary action on dark photo backgrounds (Download Poly)
- Top Navigation Bar: Persistent header across all pages
- Hero Photo Section: First-screen brand statement
- Section Headline: In-page heading at 30-45px
- Feature Card: Product feature or use-case block
- Photo Content Band: Mid-page editorial break
- Text Link: Inline navigation and footer links
- Badge / Tag: Status labels, category markers
- Body Text Block: Long-form description and paragraph copy
- Footer: Site-wide links and legal

Do:

- Use the Ember Gradient (#f4824d #f42919) only on the brand mark and logo - never on body UI, illustrations, or button fills
- Set every border-radius to 8px, including cards, buttons, tags, and image containers
- Use Haffer Variable at weight 450 for every display headline at 30-53px, with font-feature-settings: 'liga' on, 'ss04' on
- Separate regions with hairline Graphite (#292930) borders, not with drop shadows
- Apply -0.02em letter-spacing across the entire type system to unify serif and sans families
- Keep section gaps in the 48-69px range to preserve the editorial breathing rhythm
- Use full-bleed warm photography (natural light, natural materials) for hero and section breaks

Avoid:

- Don't introduce any chromatic color outside the Ember Gradient - the palette is monochrome by design
- Don't use drop shadows for card or surface elevation - borders carry separation
- Don't set display type in Inter; display belongs to Haffer at 450, never below 30px
- Don't use border-radius values other than 8px - no pills, no sharp corners, no 12px or 16px variants
- Don't apply the Ember Gradient to buttons, backgrounds, or hover states - it is brand-identity only
- Don't lighten Onyx text below #292930 for body copy - contrast must stay above 9:1 on Porcelain
- Don't break the photo/Porcelain alternation - every content section should sit on Porcelain, never on a tinted background

Source prompt cues:

**Quick Color Reference**
- text: #292930 (Graphite) or #000000 (Onyx)
- background: #f4f4f4 (Porcelain)
- border: #292930 (Graphite), 1px
- accent: Ember Gradient (#f4824d #f42919) - logo only
- primary action: no distinct CTA color

**3-5 Example Component Prompts**
1. *Hero section*: Full-bleed warm desk photograph with a 45% Onyx overlay. Centered Haffer Variable 450 headline at 53px in Porcelain, letter-spacing -1.06px, line-height 1.1. Inter 400 subtext at 15px in Porcelain below. Two buttons side by side, gap 12px: ghost outlined (1.5px Porcelain border, 8px radius, Inter 600 15px) and filled dark (Onyx background, Porcelain text, 8px radius, Inter 600 15px, padding 12px 24px). Top nav floats over the image: gradient brand mark left, Login (Inter 400 Graphite) + Onyx filled Join waitlist button right.

2. *Feature card*: Porcelain surface (#f4f4f4), 1px Graphite border, 8px radius, 24px padding. Headline in Haffer Variable 450 at 30px Onyx, tracking -0.6px. Body in Inter 400 at 15px Graphite, line-height 1.5, max-width 680px.

3. *Section band*: Full-bleed photograph edge to edge, no border-radius. Optional 24px section padding inside for a max-width 1200px text block in Porcelain over the dark overlay.

4. *Footer*: Porcelain background, 1px Graphite border-top, three columns of Inter 400 at 15px Graphite links, brand mark in Ember Gradient on the left.

5. *Badge/Tag*: No fill, Bogue or Haffer 400 at 12px Graphite text, 8px radius, 6px 12px padding, optional 1px Graphite hairline border.

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
