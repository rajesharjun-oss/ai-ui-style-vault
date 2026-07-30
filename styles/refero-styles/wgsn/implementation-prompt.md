# AI Implementation Prompt

Build a WGSN-inspired interface using this source-derived style bundle.

Reference site: https://www.wgsn.com/en
Theme: light
Category: SaaS
North star: editorial monochrome showroom

Use these palette anchors:

- Paper White `#ffffff` for Primary canvas, card surfaces, button text, and the base against which every other neutral is measured. Carries ~21:1 contrast with deep charcoal for all body and display text
- Bone Warm `#f6f2eb` for Secondary surface wash - the system's only warm neutral. Used as a soft section background to break white-on-white monotony and evoke paper-stock texture. Contrasts 14.4:1 with charcoal text
- Ash Mist `#f5f5f5` for Input field backgrounds, inset card wells, and disabled surface states. The cool-gray complement to Bone Warm - use the warm tone for sections, the cool tone for form wells
- Graphite Border `#666666` for Default hairline border color (444 border usages - by far the most-used neutral in the system). Also used for muted helper text and icon outlines. The structural divider color of the entire UI
- Smoke Border `#999999` for Secondary hairline borders and placeholder text - used when #666666 would feel too heavy against a light surface
- Pearl Border `#cccccc` for Subtle dividers and very light borders in nav-adjacent contexts where separation should be nearly invisible
- Silver Border `#bdbdbd` for Light link borders, particularly for outlined navigation links that need separation without emphasis
- Slate Text `#333333` for Secondary body copy, link borders, and UI text that should recede from primary content. Pairs with Paper White for ~12.6:1 contrast
- Carbon Input `#495057` for Input field text color - a cool desaturated charcoal that feels typographic rather than aggressive, distinct from the warmer #333333 used elsewhere
- Obsidian `#212121` for Primary action fill, primary nav background, and the deepest neutral in the system. Used for the filled CTA button, sticky header band, and dark surface blocks. Contrasts 16.1:1 with white - strong enough for any text role
- Pure Black `#000000` for Maximum-emphasis text, heading borders, and accent strokes. Reserved for the most important typographic moments and thin rule lines - never used as a large fill surface (use Obsidian instead)

Use these typography anchors:

- DM Sans `--font-dm-sans` for Sole typeface across all UI, body, and display contexts. A geometric-humanist sans with optical-size-friendly proportions - its clean terminals and open counters let it survive at 12px metadata and 92px display equally well. Weight 400 carries all body and utility text; weight 500 handles button labels and emphasized inline text; weight 700 is reserved for headlines and section titles. The 92px display step is the system's signature - used for hero statements with tight tracking (letter-spacing: -0.0110em) to give display headlines a condensed, editorial authority. All-uppercase button and label text uses the wider 0.0560em tracking for letterform breathing room.

Use these layout rules:

- Base spacing: 4px.
- Density: comfortable.
- Page max-width: 1280px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 18px.

Build these component patterns where relevant:

- Pill Primary Button: The system's sole filled action - used for 'Request a demo', 'Log in', and high-intent CTAs.
- Pill Ghost Button: Secondary action - paired alongside the primary to offer a low-commitment alternative.
- Pill Nav Link: Top-bar navigation items and language switcher.
- Image Feature Card: Hero of content sections - editorial image with headline and body copy. Used in the 4-column grid for product offerings.
- Hero Panel: First-screen hero block with image collage and large display headline.
- Text Input: Form fields for email, search, and data entry.
- Top Navigation Bar: Primary site navigation - sticky on scroll.
- Dark Feature Band: Mid-page section that flips to dark surface for visual punctuation and contrast.
- Editorial Section Header: Subsection title that introduces a row of cards or a content block.
- Pill Badge / Tag: Inline metadata - category labels, region tags, article badges.
- Hairline Link: Inline and standalone text links - the most common interactive text element.
- Footer: Closing navigation and legal block.

Do:

- Use pill radius (40px) for every button, tag, and nav link - pill geometry is the system's strongest signature shape.
- Use 16px radius for all images, image cards, and image containers - keep this consistent across the entire site.
- Use 8px radius for inputs only - a deliberate contrast with the pill buttons that signals interactivity without softness.
- Reach for #f6f2eb (Bone Warm) as the section background between two white bands - the warm tint is the only way this achromatic system creates rhythm.
- Set display headlines at 48-92px in DM Sans weight 700 with letter-spacing -0.0110em ( -0.53px at 48px, -1.01px at 92px) - tight tracking is what makes the type feel editorial rather than corporate.
- Use uppercase labels and button text with letter-spacing 0.0560em for breathing room - never use uppercase without expanding the tracking.
- Use hairline 1px borders in #666666 for all dividers and interactive affordances instead of shadows - the system deliberately avoids elevation in favor of line.

Avoid:

- Never introduce chromatic color - the system is 0% colorful by design, and any accent hue would break the editorial monochrome logic.
- Never use shadows for elevation - the only shadow pattern in the system is the 1px inset border on links; do not add drop shadows to cards or buttons.
- Never use #000000 as a large filled surface - use #212121 (Obsidian) for dark backgrounds and reserve pure black for text and thin accent strokes only.
- Never use sharp 0px corners on images or cards - everything that contains an image uses 16px radius; flat-cornered images would feel foreign.
- Never use display-weight tracking on body text - the -0.0110em is calibrated for 40px+ sizes; applying it to 16px body copy will over-condense letters and hurt readability.
- Never use uppercase for body copy - uppercase is reserved for eyebrows, badges, and button labels where the 0.0560em tracking provides necessary letter spacing.
- Never use the warm Bone Warm (#f6f2eb) for form fields or interactive surfaces - it is a sectional wash only; form wells should use the cool Ash Mist (#f5f5f5) to signal input.

Source prompt cues:

**Quick Color Reference**
- text: #212121 (Obsidian) for body and headings, #333333 (Slate) for secondary
- background: #ffffff (Paper White) for canvas, #f6f2eb (Bone Warm) for section wash, #212121 (Obsidian) for dark bands
- border: #666666 (Graphite) for hairlines, #999999 (Smoke) for subtle, #212121 (Obsidian) for emphasis
- accent: no chromatic accent - system is 0% colorful
- primary action: #212121 (filled action)

**Example Component Prompts**

1. *Hero section*: White canvas. Display headline at 92px DM Sans weight 700, #212121, letter-spacing -0.0110em ( -1.01px). Eyebrow above at 14px weight 500, #999999, uppercase, letter-spacing 0.0560em. Body subtext at 18px weight 400, #333333. Filled CTA button: #212121 background, white text, DM Sans weight 500 at 14px, padding 12px 18px, border-radius 40px. Supporting image collage to the right with 3-4 images at 16px border-radius.

2. *Feature card grid (4-column)*: White card surface, no border, no shadow. Top: image at 16px border-radius. Below: 24px padding, heading at 20px DM Sans weight 600 #212121, body at 16px weight 400 #333333. Gap between cards: 18px. Section above grid has 28-32px heading and ~48px gap to cards.

3. *Dark feature band*: #212121 background, full-bleed, 80px vertical padding. Two-column layout: left column has 40-48px display headline in white DM Sans weight 700 with -0.0110em tracking, body in 18px weight 400 white at 80% opacity. Right column has a single image at 16px border-radius. Ghost button below the text: transparent fill, #666666 border, white text, 40px radius.

4. *Pill tag/badge*: Transparent or #f5f5f5 background, #666666 1px border, #212121 text, DM Sans weight 500 at 12px, uppercase, letter-spacing 0.0560em, border-radius 40px, padding 4px 12px.

5. *Top navigation bar*: White #ffffff background, 1px bottom border in #666666, height 64px, padding 0 16px. Logo (DM Sans weight 700, 24px, #212121) on left. Center: pill nav links with #333333 text, 8px 13px padding, 40px radius, transparent fill. Right: language switcher + ghost 'Log in' link (#333333 text, no border) + filled 'Request a demo' button (#212121 fill, white text, 40px radius).

The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
