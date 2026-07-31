# Guidelines

### Do
- Use the 180px condensed serif only for the hero statement - it's the loudest voice in the system and should appear once per page
- Apply #26d862 (Lime Pulse) filled buttons sparingly - one primary action per viewport, never stack two green buttons side by side
- Set letter-spacing explicitly: -5.4px at 180px, -3.12px at 104px, -0.48px at 32px, scaling proportionally through the type ramp
- Use the surface color difference (#f7f5f2 #eae6df) for card separation instead of box-shadows - the system is intentionally flat
- Let full-bleed flower imagery sit edge-to-edge in 8px-radius cards with no captions - the image is the content
- Anchor any dark moment to the Forest Depths #1d3023 - never use pure black, the warm green undertone is what makes it feel like a room rather than a void
- Pick one weight tier per size: weight 300 for 104-180px display, weight 400 for 20-48px mid-headlines, weight 350 only at 32px subheadings, weight 400 everywhere else

### Don't
- Don't introduce a new font family - the system runs on exactly two custom serifs (Arizona Flare and Arizona Flare Condensed) and the contrast between them is the signature
- Don't use Lime Pulse #26d862 for body text, borders, or decorative fills - it is exclusively an action and link color
- Don't apply box-shadows to cards or buttons - separation comes from the two-tone cream surface and 8px radius
- Don't mix line-height styles within a size - 0.85 for display (48px+), 1.08 for subheadings (20-32px), 1.18-1.50 for body (12-18px)
- Don't center-align body paragraphs longer than 2 lines - left-align at max-width 720px for readability
- Don't use the Peaacock Teal #0e634f outside of numerical data contexts - it is reserved for stat numbers and data emphasis
- Don't place colored text on the dark Forest Depths hero unless it's Bone Linen #f7f5f2 - the contrast math is tuned for cream-on-forest, not green-on-forest

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
