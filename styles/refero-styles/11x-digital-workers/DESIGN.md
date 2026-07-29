# 11x Digital Workers Design Reference

## North Star

Cinematic editorial desert full-bleed terrain photography against monumental serif headlines, where the page reads like a luxury magazine spread.

## Theme

mixed style for AI interfaces.

## Color System

- Obsidian `#000000` for Primary action buttons on light surfaces, body text, headlines, card borders the universal ink of the system
- Paper White `#ffffff` for Page canvas on light sections, card surfaces, text on dark backgrounds, button text on filled buttons
- Deep Teal `#0b252a` for Dark section backgrounds the only large chromatic surface, used for narrative bands between editorial spreads
- Bone `#f6f5f5` for Card surfaces and hairline borders on light sections the warm off-white that prevents starkness
- Sandstone `#f5ece5` for Warm card surface tint, section backgrounds in cream/peach areas desert-hour warmth
- Ash Blush `#ede2d7` for Soft warm card surface, secondary peach accent on portrait cards
- Stone `#d7cecc` for Muted neutral footer and section dividers warm mid-gray grounding color
- Iron `#e1dad9` for Button and link background tint, card surface for outlined controls

Use the listed source colors as the authoritative palette. Keep the most saturated or highest-contrast color for primary action moments unless the component notes say otherwise.

## Typography

- ES Allianz Primary typeface for all UI text a high-contrast didone-influenced serif used at dramatic display sizes (74152px) for headlines, and at body sizes (1619px) for running text. The tight letter-spacing (-0.045em at display, -0.02em at body) tightens the serifs into a modern editorial stance. Weight 400 carries most copy; 700 for hero impact; 500 for navigation and subheadings. This serif does the heavy lifting that a sans-serif system would spread across three families. `--font-es-allianz`

Use the source font pairing to preserve the visual voice. When custom fonts are not available, choose close substitutes with similar weight, width, and editorial character.

## Layout And Spacing

- Base unit: 8px
- Density: compact
- Page max-width: 1200px
- Section gap: 48-80px
- Card padding: 16-24px
- Element gap: 8-16px

## Components

- Primary Pill Button (Light): Filled CTA on white/light surfaces
- Primary Pill Button (Dark): Filled CTA on dark teal sections
- Navigation Bar: Top-level site navigation
- Announcement Bar: Top-most notification strip
- Hero Section (Full-Bleed): Cinematic landing hero
- Portrait Worker Card: Featured digital worker profile
- Status Badge: Worker status indicator on cards
- Feature Tag Pill: Platform capability tag on dark sections

## Implementation Guidance

- Use the ES Allianz serif at 74px+ weight 700 for hero and section headlines the oversized serif is the brand's primary visual signature
- Set pill buttons to exactly 999px border-radius with 12px 24px padding, in either black-on-white or white-on-black
- Use the four pastel card tints (Dusty Sky, Mist Mint, Wisteria, Desert Clay) as the only color punctuation on light sections never introduce new chromatic UI colors
- Alternate between white editorial spreads and Deep Teal (#0b252a) full-bleed bands to maintain the magazine-spread rhythm
- Use full-bleed landscape photography as section backgrounds the imagery must be warm-toned, cinematic, and high-resolution
- Set letter-spacing to -0.045em at display sizes (74px+) and -0.02em at body sizes for the modern editorial stance
- Use the Slate Teal (#406e7a) feature tag pills exclusively on the Deep Teal dark sections never on light backgrounds

## Guardrails

- Do not use sans-serif typefaces anywhere the serif is non-negotiable and defines the editorial identity
- Do not use blue, red, green, or yellow as functional UI colors the palette is restricted to neutrals, deep teal, and the four muted pastels
- Do not add drop shadows to cards or buttons elevation is communicated through tonal contrast and 1px hairline borders only
- Do not use sharp corners (under 8px radius) on interactive elements pills, rounded cards, and soft radii are the norm
- Do not center-align body paragraphs longer than two lines left-align running text for editorial readability
- Do not introduce gradients on UI components the only gradient is a subtle warm fade (#f8f9f7 #d7cecd) used minimally
- Do not stack more than one pastel card tint adjacent to another alternate pastel cards with white space to preserve the airy feel
