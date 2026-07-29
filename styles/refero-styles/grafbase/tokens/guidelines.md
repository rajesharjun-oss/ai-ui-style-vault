# Guidelines

### Do
- Use Graphite Ink (#1b1b1b) for all primary text and all primary action buttons - never introduce a chromatic brand color for CTAs.
- Set display headlines at 90px Inter 600 with letter-spacing -4.5px; headings at 40px Inter 500 with -1px tracking. The negative tracking is the signature - do not normalize it.
- Apply 6px radius to all rectangular buttons, 40px to any pill-shaped button, and 20px to all cards and large content panels.
- Keep the interface fully monochromatic on white #ffffff and #eaeaea surfaces. Reserve the forest-to-teal gradient exclusively for the announcement bar.
- Use Steel (#60646c) for subtext and helper copy, Ash (#7c7c7c) for tertiary metadata - do not invent new grays.
- Build product mockups and integration tiles in the cool triad (Mint Signal, Moss, Sky) so the chromatic identity lives inside the product, not on the marketing chrome.
- Use the single shadow rgba(0,0,0,0.15) 0px 4px 20px 0px on primary buttons and elevated preview panels only - do not stack multiple shadow levels.

### Don't
- Do not add saturated accent colors to the interface - the system is intentionally 99% achromatic.
- Do not use pure black (#000000); use Graphite Ink (#1b1b1b) which is softer against the cool gray canvas.
- Do not introduce a second typeface - Inter is the system, used at every size from 13px caption to 90px display.
- Do not set letter-spacing to 0 on display and heading text - the -4.5px / -1px tracking is what makes the large type feel engineered rather than webby.
- Do not add drop shadows to ghost buttons, cards, or nav - the shadow belongs only on the primary action button and the hero preview panel.
- Do not create button variants with new colors for hover/active states - swap to a slight opacity reduction or a subtle bg-gray-100 treatment instead.
- Do not place the green-to-teal gradient anywhere other than the top announcement bar - it is a one-shot signal, not a reusable surface.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
