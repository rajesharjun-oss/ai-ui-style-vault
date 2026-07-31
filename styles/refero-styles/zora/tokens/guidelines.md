# Guidelines

### Do
- Use #00df00 exclusively for purchase/buy actions - never for decoration, tags, or non-transactional UI
- Set all text at -0.015em letter-spacing; the tight tracking is part of the system's visual identity, not optional
- Keep card padding at 12px and element gaps at 8px or 4px - the compact density is intentional, not cramped
- Use 9999px border-radius for all social actions (Follow) and 8px for transactional actions (Buy, Log In) - the radius difference signals intent
- Reserve #ff00f0 for time-sensitive or live-status indicators (countdown timers, live auctions, real-time pulses)
- Place all navigation icons in a persistent 56px left rail with no labels - icon-only navigation is part of the gallery-tool language
- Use MonumentGrotesk weight 500 for all interactive elements and weight 410/450 for body metadata to create subtle hierarchy without weight contrast

### Don't
- Don't add shadows to cards - surfaces sit flat against the canvas, elevation is expressed by background contrast only
- Don't introduce additional accent colors beyond #00df00 and #ff00f0 - the two-color neon system is deliberately limited
- Don't use weights above 600 - the type system is calibrated for label density, not editorial display
- Don't center-align body text or card titles - left-align everything except hero headlines
- Don't use border-radius values other than 8px (buttons/inputs), 12px (cards), or 9999px (pills) - mixing radii breaks the system
- Don't add gradients to UI chrome - the gray gradient is reserved for skeleton/loading states only
- Don't use color to indicate state on form inputs - use border color shift (#cacaca #121212) instead of fills

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
