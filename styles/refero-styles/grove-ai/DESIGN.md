# Grove AI Design Reference

## North Star

clinical journal in morning light a single green word anchors a page of measured prose

## Theme

light style for AI interfaces.

## Color System

- Forest Grove `#0b835c` for Primary brand color used for the logo mark, the signature word in serif headlines, accent borders on tags and announcement pills, and small icon highlights. A deep, slightly desaturated green that reads as clinical and t...
- Pine Shadow `#1c2b27` for Secondary dark surface a near-black green-tinted shade for inverted buttons and dark surface moments where #000 would feel too harsh against the green accent
- Ink Black `#1c1c1e` for Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color
- Graphite `#303033` for Secondary text and dividers a mid-dark gray for body copy de-emphasis, subtle borders, and metadata
- Slate Mid `#676768` for Muted helper text, inactive labels, and tertiary metadata sits at a comfortable AA contrast against white
- Mist Gray `#eff1f6` for Card surface and the only neutral fill color in the system. Creates a single elevated tier above the white canvas without introducing a new hue
- Pure White `#ffffff` for Page canvas, card-internal backgrounds, and inverse text on dark fills
- Shadow Smoke `#bfbfbf` for Box-shadow base color for the soft elevation that sits behind cards and the floating product mockup on the right side of the hero

Use the listed source colors as the authoritative palette. Keep the most saturated or highest-contrast color for primary action moments unless the component notes say otherwise.

## Typography

- sans-serif sans-serif detected in extracted data but not described by AI `--font-sans-serif`
- Libre Caslon Text Display serif used exclusively for hero-level headlines and the signature brand word. The italic-leaning contrast strokes give "Grace" and "Meet" a humanized, editorial voice that contrasts with the precise Geist below. The choice is anti-SaaS: most clinical-tech sites use a geometric sans for the hero; this serif makes the brand feel like a respected medical publication. `--font-libre-caslon-text`
- Geist Primary interface and body typeface. Covers body copy (16/24px, 400), subheadings (1820px, 500), card titles (2024px, 600), and large stat numbers (3240px, 500/600). The negative letter-spacing tightens as size grows, creating density at body size and breathing room at display. `--font-geist`
- Geist Mono Monospaced variant for code-like or technical callouts in body content where alignment matters. `--font-geist-mono`

Use the source font pairing to preserve the visual voice. When custom fonts are not available, choose close substitutes with similar weight, width, and editorial character.

## Layout And Spacing

- Base unit: 4px
- Density: comfortable
- Page max-width: 1200px
- Section gap: 80px
- Card padding: 24px
- Element gap: 10px

## Components

- Top Announcement Banner: Full-width dark green strip pinned to the very top of the page above the nav.
- Sticky Navigation Bar: Primary site nav that persists on scroll.
- Announcement Pill: Highlighted category tag sitting above the hero headline.
- Hero Headline: The signature brand statement that opens the page.
- Hero Subhead: One-sentence positioning statement directly under the headline.
- Floating Product Mockup Card: Right-side hero asset showing the AI agent in a phone/video call UI.
- Filled Dark Button: Primary action the strongest interactive element on the page.
- Outlined Button: Secondary action paired with the filled button.

## Implementation Guidance

- Set the hero headline in Libre Caslon Text 92px, reserving the green #0b835c for the single product name (e.g. "Grace") while the rest of the headline stays #1c1c1e.
- Use 9999px radius on all buttons, tags, and pills to keep the interaction language soft and pill-shaped throughout.
- Reserve the forest green #0b835c for three jobs only: the brand word in serif headlines, small-caps section labels, and icon/directional accents (arrows, lightning). Never use it a...
- Pair a Filled Dark Button (#1c1c1 fill, white text) with an Outlined Button (transparent, #1c1c1 border) as the canonical CTA pair on any page section.
- Use Mist Gray (#eff1f6) as the only card surface color; cards are never white-on-white when they need to group content.
- Type all small-caps category labels at 12px Geist with 0.1em tracking the wide tracking is what makes them read as clinical-trial section headers.
- Keep body copy left-aligned and capped at ~520px width to maintain the editorial reading column.

## Guardrails

- Do not use Geist or any sans-serif for the hero headline the serif Libre Caslon Text is the brand's signature and must stay in the display slot.
- Do not apply drop shadows greater than 12px of blur; the system rejects heavy elevation in favor of hairline halos.
- Do not introduce new accent colors; the palette is monochrome plus one green, and adding blue/red/purple would dilute the clinical authority.
- Do not use #0b835c for filled buttons the dark filled button is always #1c1c1, and green is reserved for accent and small-caps labels.
- Do not center-align body paragraphs; the system reads as an editorial layout and left-alignment is non-negotiable below the hero.
- Do not use radii between 14px and 18px the system commits to either 8/12px (tight elements), 20/24px (cards), or 9999px (pills), with nothing in between.
- Do not pair the serif with bright or saturated colors other than #0b835c; any other chromatic color on the serif text breaks the signature.
