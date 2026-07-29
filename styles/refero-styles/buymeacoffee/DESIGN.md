# Buymeacoffee Design Reference

## North Star

Cream-paper caf scrapbook with floating polaroid testimonials

## Theme

light style for SaaS interfaces.

## Color System

- Cream Paper `#faf8f0` for Page canvas, section backgrounds the warm off-white ground that softens every interface layer and gives the whole product its caf-on-paper atmosphere
- Card White `#ffffff` for Card surfaces, modal backgrounds, raised panels pure white floats above the cream canvas to create depth through luminance contrast rather than color
- Hairline Gray `#e5e7eb` for Borders, dividers, icon outlines, badge outlines used at 1146+ occurrences as the universal hairline separator across cards, buttons, and inputs
- Ink Black `#000000` for Primary text, filled icon strokes, high-contrast UI elements the dominant text and icon color across the entire product
- Charcoal `#222222` for Body and heading text, filled SVG strokes slightly softer than pure black for sustained reading in longer copy blocks
- Fog Gray `#717171` for Muted helper text, secondary metadata, small caps labels the quietest text voice for timestamps, supporter counts, and contextual hints
- Marigold `#ffdd00` for Yellow wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color
- Buttercup `#f7d046` for Yellow wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color

Use the listed source colors as the authoritative palette. Keep the most saturated or highest-contrast color for primary action moments unless the component notes say otherwise.

## Typography

- ui-sans-serif ui-sans-serif detected in extracted data but not described by AI `--font-ui-sans-serif`
- Circular Bold Display and hero headlines Circular Bold at 96px with -0.042em letter-spacing carries the 'Fund your creative work' headline; the extreme size and tight tracking make the wordmark feel monumental. Also used for button labels and emphasized short-form copy. `--font-circular-bold`
- Circular Medium Subheadings, card titles, and emphasis within body copy the bridge weight between Bold displays and Regular body, used where hierarchy needs weight without volume `--font-circular-medium`
- Circular Regular Body copy, descriptions, conversational text the workhorse weight for everything from supporter messages to card body descriptions, with a 16px baseline for body text `--font-circular-regular`

Use the source font pairing to preserve the visual voice. When custom fonts are not available, choose close substitutes with similar weight, width, and editorial character.

## Layout And Spacing

- Base unit: 4px
- Density: comfortable
- Page max-width: 1200px
- Section gap: 80px
- Card padding: 24px
- Element gap: 16px

## Components

- Marigold Pill CTA: Primary creator signup action
- Terracotta Support Button: Primary supporter payment action
- Ghost Outline Button: Secondary action
- Creator Profile Card: Social proof, creator showcase
- Support Modal: Coffee purchase interaction
- Coffee Count Selector: Quantity picker for support
- Supporter Notification Card: Activity feed, social proof
- Star Rating Row: Social proof header

## Implementation Guidance

- Use #faf8f0 as the universal page background every screen should feel like cream paper beneath white cards
- Reserve #ffdd00 exclusively for the creator-facing 'Start my page' / 'Sign up' CTA this yellow should appear nowhere else
- Use #d8573f only for supporter payment actions like 'Support $3' never for navigation, links, or informational elements
- Apply 9999px radius to all buttons, tags, and pill inputs the pill shape is the system's signature interaction form
- Set hero and display headlines to Circular Bold 64-96px with letter-spacing between -2.7px and -4.0px the tight tracking makes large text feel monumental
- Use the three-layer shadow stack (2px close blur + 40px ambient + 5px medium) on all floating cards and modals this is the system's only shadow recipe
- Write section labels as uppercase Circular Bold 12px with 0.125em tracking the wide-spaced small caps are the system's typographic signature for section dividers

## Guardrails

- Don't use #ffdd00 or #d8573f for body text, links, borders, or decorative fills these are action-only colors
- Don't apply sharp corners (0-4px radius) to cards or buttons the system requires generous rounding (8px minimum, 24px+ preferred for cards)
- Don't use colored shadows or glows all elevation comes from the neutral black-alpha three-layer stack
- Don't introduce new accent colors beyond Marigold, Terracotta, and Blush Border the palette is intentionally two-color (plus warm cream)
- Don't set body text below 14px or above 18px the reading range is narrow by design
- Don't use bold or black weights for long-form body copy Circular Regular or Book at 14-16px is the standard for paragraphs
- Don't fill the cream canvas with pure white sections alternate cream bands with white cards, not cream white cream
