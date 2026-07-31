# AI Implementation Prompt

Build a IKEA-inspired interface using this source-derived style bundle.

Reference site: https://www.ikea.com
Theme: light
Category: E-commerce
North star: sunlit Swedish flat-pack showroom

Use these palette anchors:

- IKEA Yellow `#ffdb00` for Primary CTA fills, featured card backgrounds, hero accent panels, the singular chromatic workhorse of the system
- Ink Black `#111111` for Primary text, body copy, headings, dominant borders (851 occurrences), icon strokes
- Pure White `#ffffff` for Page background, card surfaces, nav background, button text on dark fills
- Warm White `#fffefb` for Slightly off-white surface variant for buttons and cards - barely warmer than pure white, breaks digital coldness
- Steel Gray `#818181` for Secondary text, muted borders, disabled icon states
- True Black `#000000` for SVG icon fills, input borders, true-black accents where maximum contrast is needed
- Link Blue `#0159a3` for Text link color, used extensively across navigation and body links - the only blue in the system
- Soft Pink `#ffa6da` for Occasional decorative highlight, used sparingly on select link elements or promotional accents

Use these typography anchors:

- Noto IKEA `--font-noto-ikea` for Sole typeface - custom IKEA-branded Noto variant. Two-weight system (regular 400, bold 700) is deliberate restraint: no italics, no medium weight, no light. The 700 headlines at 36-51px carry the entire brand voice; body at 16px stays neutral. Letter-spacing tightens as size grows, giving display text a compressed, architectural quality.

Use these layout rules:

- Base spacing: 8px.
- Density: comfortable.
- Page max-width: 1440px.
- Section gap: 80px.
- Card padding: 20px.
- Element gap: 24px.

Build these component patterns where relevant:

- Top Navigation Bar: Site header
- Hero Media Card: Primary featured content card
- Yellow CTA Card: Primary action panel
- Image Story Card: Editorial content card
- Circular Media Control: Play/pause button
- Arrow Link Button: Inline navigation action
- Store Selector Footer: Utility footer
- Timeline Section Block: Historical/year display

Do:

- Use #ffdb00 exclusively for primary CTAs and featured accent cards - never as a background for body text or informational content
- Set all corners to 8px - there is exactly one border radius in the system
- Use weight 700 for every headline and weight 400 for every body element - never introduce medium, semibold, or light weights
- Apply gradient-to-black overlays at 30-60% opacity on all image cards that contain text overlays
- Use the circular black arrow button (Ink Black fill, white arrow, 8px or 50% radius) as the universal 'navigate' affordance
- Keep body text at 16px with 1.57 line-height - IKEA's body line-height is generous, not tight
- Use #0159a3 exclusively for text links, never for buttons or backgrounds

Avoid:

- Do not introduce shadows, elevation, or any depth effects - the system is entirely flat
- Do not use more than one border radius - 8px everywhere, no exceptions
- Do not add additional font weights (300, 500, 600) - the binary 400/700 system is the constraint
- Do not place body text directly on photography without a gradient overlay
- Do not use the blue #0159a3 as a CTA button fill - it is link-only, not action
- Do not soften the letter-spacing - the negative tracking is structural, not decorative
- Do not add accent gradients or color transitions - the system rejects all gradient fills on surfaces

Source prompt cues:



The finished UI should feel faithful to the reference style while being implemented as production-ready, accessible, responsive application UI.
