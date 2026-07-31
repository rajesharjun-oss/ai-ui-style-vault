# Components

### Primary CTA - Ember Button
**Role:** The single filled action on any screen (Pre-order, Buy).

Background #f45500, white text at 16px GT-Flexa 400, 20px radius, horizontal padding 16px, vertical padding 1px (sits visually low and wide). Always wrapped in the 30px rgba(245,86,0,0.6) outer glow. The thin vertical padding is intentional - the button reads as a glowing bar, not a pill.

### Secondary CTA - White Ghost Button
**Role:** Companion to the Ember button when two actions sit side by side.

Transparent background, 1px #ffffff border at 20px radius, white text. Mirrors the primary CTA's dimensions but carries a softer 30px rgba(255,255,255,0.3) glow - like the orange button's monochrome echo.

### Lavender Outlined Action
**Role:** Tertiary or nav-level action (e.g. About, Updates in the header).

1px #9e9eff border, 20px radius, lavender text. Functions as a quiet link-button - never used for purchase. The violet border separates navigation actions from the orange commerce action.

### Inline Lavender Link
**Role:** Anchor text inside paragraphs or feature captions.

Color #9e9eff, no underline by default, GT-Flexa 400 16px. The only inline accent in the type system - it carries affordance without weight.

### Video / Media Card
**Role:** Hero film or product video frame.

Charcoal (#202020) background matching the canvas, 20px radius, 1px #9d9d9d or #ffffff border, contains a centered product render with a floating 20px-radius Play pill button in the lower third. No shadow - the border is the edge.

### Feature Card
**Role:** 2x2 or 3x2 grid cell in the Key Features section.

Charcoal canvas (no surface lift), 20px radius, 1px #9d9d9d border, 24px internal padding, top half is a square product detail photograph with no internal padding (bleeds to the card edge, clipped by the 20px radius), bottom half holds a two-line caption in Tobias-light 32px (-1.5px tracking) or GT-Flexa 24px 400.

### Hero Headline Block
**Role:** Opening product announcement that fills the first scroll.

GT-Flexa weight 200, 68-86px, line-height 1.0-1.06, color #ffffff. No text-align override needed - left-aligned by default, tracking normal, line-height tight enough that multi-line headlines stack into a single column of light. Sits directly below the video card with a 48px gap.

### Section Header (Tobias Voice)
**Role:** Delineates major sections (e.g. KEY FEATURES).

Tobias-light 400 at 42px, letter-spacing -0.062em (-2.6px), all caps in the visual system, color #ffffff. Provides an architectural label that contrasts with the weight-200 GT-Flexa body headlines.

### Editorial Paragraph
**Role:** Body copy under hero or in product descriptions.

Times 400 16px, line-height 1.2, color #ffffff. Serif body on dark background - a deliberate humanist counterpoint to the geometric display fonts. Never grows past 16px; rarity is the point.

### Top Navigation Bar
**Role:** Persistent header across all pages.

Transparent over the charcoal canvas, no background fill, no border. Left: brand mark ' Electronic Materials Office(R)' in white with a small orange dot prefix. Right: two ghost links (About, Updates) in #9e9eff + 1px border, then the Ember CTA. Vertical padding ~24px, sits flush to the viewport edges with internal page padding.

### Footer
**Role:** Closing block of the page.

128px top margin from the last content block, charcoal background, Tobias-light wordmark or GT-Flexa 200 at 68px as a closing statement. No card surfaces, no borders - the footer is defined by the gap above it.

### Play Overlay Button
**Role:** Centered trigger over video frames.

White fill, #000000 text reading 'Play film', 20px radius, ~16px horizontal padding. The only white-filled button in the system - functions as the inverse of the Ember CTA.
