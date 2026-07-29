# Dylanbrouwer Design Reference

## North Star

Build a brutalist portfolio that behaves like a moving exhibition poster. It should feel oversized, confident, slightly abrasive, and carefully restrained: huge warped display type, hard project imagery, concrete-white surfaces, black ink, and one ember-orange signal color.

The design is not trying to feel cozy or corporate. It should feel like a designer staking a claim.

## Theme

- Mode: mixed light and dark.
- Light canvas: concrete and bone whites.
- Dark canvas: black or near-black panels.
- Text: black on light, bone white on dark.
- Accent: one ember orange.
- Elevation: none.
- Shape: sharp by default; pills only for tiny controls.

## Color System

Core colors:

- Cinder Black: `#161616` for main ink, borders, nav text, and inverted surfaces.
- Bone White: `#f7f7f7` for light cards, footer text, and soft foreground on dark sections.
- Concrete Mist: `#efefee` for the primary page field and neutral gallery sections.
- Ember Orange: `#f7601b` for accent tags, hover fills, special capsules, and brand flashes.
- Utility Gray: `#777777` for metadata, counters, inactive nav, and secondary text.
- Ash Line: `#d5d5d5` for subtle dividers on light sections.
- Deep Field: `#000000` for full black transition panels and image-backed overlays.

Ember Orange is the only vivid color. Keep it rare so it feels intentional.

## Typography

Display: Tilt Warp.  
Body: Sohne or a clean grotesk fallback.  
Accent families: ABC Gravity and Die Grotesk B may appear as supporting brand references, but do not turn the page into a font sampler.

Type scale:

- Mega display: 288px, line-height 0.85, letter-spacing -14.4px, weight 400, uppercase.
- Display: 144px, line-height 0.88, letter-spacing -7.2px, weight 400.
- Headline: 76px, line-height 0.92, letter-spacing -3.04px, weight 400.
- Title: 44px, line-height 1.0, letter-spacing -1.76px, weight 400.
- Body: 18px, line-height 1.35, letter-spacing -0.36px, weight 400.
- Body small: 14px, line-height 1.3, letter-spacing -0.14px, weight 400.
- Nav: 13px, line-height 1.2, letter-spacing -0.13px, uppercase.
- Metadata: 12px, line-height 1.2, letter-spacing 0.24px, uppercase.

The signature is the huge warped display type. Do not tame it into normal hero text.

## Layout

- Base unit: 6px.
- Max width: 1200px.
- Section gap: 144px.
- Card padding: 24px.
- Element gap: 18px.
- Gallery rhythm: large blocks with very hard edges.
- Desktop: oversized hero and project grids.
- Mobile: reduce display type sharply, but keep the graphic punch.

Use whitespace as a dramatic pause. Do not fill every area with content.

## Shape

- Global radius: 0px.
- Project cards: 0px.
- Media frames: 0px.
- Large containers: 0px.
- Tags, chips, and nav pills: 9999px.

This contrast matters. Large objects are sharp. Small controls are pills.

## Imagery

Use hard-edged project imagery:

- Portfolio screenshots.
- Cropped case-study images.
- Editorial spreads.
- Website captures.
- Black and white or low-saturation work samples.

Avoid soft lifestyle photography, mockup-heavy SaaS scenes, and rounded device frames.

## Components

The page should use a small set of highly opinionated components:

- Poster masthead.
- Sticky pill navigation.
- Project gallery card.
- Work index row.
- Accent capsule.
- Metadata strip.
- Full-bleed dark panel.
- Sharp media frame.

## Motion

Motion can be confident but not playful:

- Hover fills on pills.
- Fast project thumbnail reveal or slide.
- Text mask or marquee when it supports the poster feel.
- No bouncy springs, floating blobs, or soft fade-heavy motion.

## AI Build Notes

When implementing this style, start with scale and contrast. If the page feels too plain, make the type larger or the composition sharper before adding extra decoration.

