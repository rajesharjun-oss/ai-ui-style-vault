# Guidelines

### Do
- Use Signal Red #e32735 exclusively for the single primary action per surface - never as a decorative or background fill
- Set all corners to 4px radius - no exceptions, no pill shapes, no zero-radius hard edges
- Separate dark sections with 80px vertical padding and rely on background-value shift rather than dividers or shadows
- Use Archivo 500 (not 700) for headings 40px and above to keep weight restrained and consistent
- Apply -0.02em letter-spacing to all Archivo type at all sizes for tight industrial density
- Stamp step numbers, serial codes, and technical labels in Space Mono 12px - never Archivo for these
- Define card and panel edges with 1px #382e30 borders on dark, never with box-shadow or background tint shifts

### Don't
- Don't introduce drop shadows, glows, or blur-based elevation - structure is line-based only
- Don't use #e32735 for body text, icons, or secondary UI - it's an action color, rationed
- Don't round corners beyond 4px - no 8px, 12px, 16px, or pill radii anywhere
- Don't set headings in bold (700+); weight 500 Archivo at 40-56px is the maximum voice
- Don't alternate between light and dark sections within a single content flow - the page is dark-dominant after the hero
- Don't use Archivo for numeric step counters, product codes, or instrumentation labels - those are Space Mono territory
- Don't add gradient fills to buttons or cards - the one gradient in the system (white red) is reserved for the hero-to-content transition

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
