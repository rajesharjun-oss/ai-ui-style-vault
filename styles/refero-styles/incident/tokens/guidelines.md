# Guidelines

### Do
- Use Times (or Source Serif Pro as substitute) for all body copy, headings, nav items, and hero text - the serif face is the brand voice
- Set the page canvas to #efefef (Concrete) and let cards sit in #ffffff (Paper) above it - never invert to a white page with gray cards
- Use #000000 for all structural borders and hairline rules - borderColor is the dominant role of pure black in this system
- Use Signal Orange (#f25533) only for brand marks, logo elements, decorative fills, and file-type illustrations - never for action buttons or functional UI
- Set button background to #efefef with a 1px black border, 4px radius, and 1px/6px padding - buttons should feel like labeled frames, not filled actions
- Keep the type scale tight: 13px (Arial micro-labels), 16px (Times body), 19px (Times body-lg), 24px (Times heading-sm), 32px (Times heading) - do not introduce sizes outside this range
- Use status-tinted card borders (red for critical, amber for warning) to communicate severity - the border color does the semantic work, not a colored background fill

### Don't
- Do not use sans-serif (Inter, system-ui) for body copy or headings - replacing Times breaks the editorial identity
- Do not add colored button fills (blue, orange, green) for primary actions - the system uses neutral concrete buttons with black borders
- Do not use gradients - no gradient was detected in the source and the flat editorial aesthetic rejects them
- Do not use heavy drop-shadows for elevation - shadows are reserved for image containers at 2-4% opacity only
- Do not introduce blue or green as brand or accent colors - the chromatic palette is exclusively warm (orange family and amber)
- Do not round buttons beyond 4px or use pill shapes - the slightly squared button geometry reinforces the broadsheet feel
- Do not use color to indicate active or selected states - rely on weight (400 700) and underline affordances within the serif system

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
