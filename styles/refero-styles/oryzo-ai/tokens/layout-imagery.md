# Layout & Imagery

## Layout

Full-bleed throughout - no max-width container, every section spans 100vw. Hero: full-viewport top-down photograph with a massive ORYZO wordmark (51px+) in the upper-left, tagline above, fixed minimal nav upper-right, vertical sidebar label running down the right edge, semi-transparent info card lower-left, video thumbnail lower-right. Subsequent sections: full-viewport Walnut Shadow canvas with a centered 3D product render flanked by left-aligned heading and right-aligned body copy - a three-column grid (text / object / text) with generous 18px gutters. Section transitions are seamless dark-on-dark; the only breaks are hairline dashed dividers. Navigation is fixed, transparent, and 4 items max. No sidebar, no footer chrome, no cards-within-cards - every screen is a single statement.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Walnut Shadow | `#100904` | Full-bleed page canvas and section background |
| 1 | Bark Brown | `#382416` | Filled button surface, the only elevated solid |
| 2 | Cork Border | `#40372` | Hairline borders, dashed dividers, card outlines |
| 3 | Warm Cream | `#ffedd7` | Foreground text, navigation, interactive borders |

## Elevation

The system rejects shadow-based elevation entirely. Depth is achieved through a two-step surface stack: #100904 (canvas) #382416 (elevated solid). There are no blur, no offset, no opacity-based shadows - only a 1-2 value luminance step. This keeps the interface flat and editorial, letting the 3D product renders provide all visual depth in void-mode sections.

## Imagery

Photography is editorial, top-down, and in-context: the cork coaster sits on a green cutting mat surrounded by pencils, a craft knife, and a paperclip - tools of the craft visible in frame. The green cutting mat (#445231) is a hero-only element, not a UI token. 3D renders dominate the product reveal sections: the cork coaster is shown isolated against Walnut Shadow, lit from the upper right with a warm rim light, rotating from top-down to 3/4 angle between sections. No lifestyle photography, no people, no stock imagery - the object is the hero and the tools are its context. Images are full-bleed, sharp-edged (no rounded masks), and treated with high contrast and warm grading.
