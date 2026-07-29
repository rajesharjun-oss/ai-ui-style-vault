# Guidelines

### Do
- Keep the canvas pure white (#ffffff) - the illustrations provide all color, the UI must not compete
- Use Times 14px for body, captions, and labels; switch to UniversalSans 425 only for headings or emphasized runs
- Frame every image with a 1px #000000 hairline - the black border IS the visual device, not shadows
- Round interactive elements (buttons, pills) to 48px for full pill shape; round image cards to 10px
- Use #f2f2f2 exclusively for the floating pill nav and soft tag chips - never for page sections
- Set body and caption text at exactly 14px / 1.2 line-height / -0.14px letter-spacing - the compactness is deliberate
- Let the Rza wordmark appear exactly once, in the header - it is the only display moment in the system

### Don't
- Do not introduce any chromatic UI color - green, red, blue, or accent hues - the palette is black/white/gray by design
- Do not add box-shadows to illustration cards; the single shadow allowed is the floating pill nav (rgba(0,0,0,0.1) 0px 4px 4px)
- Do not use Times for headings at large sizes; it is a 14px label face, not a display face
- Do not mix Rza into body copy or labels - it lives only in the brand wordmark
- Do not use #9b9b9b for body text on white - it fails contrast (2.8:1); reserve it for meta/tags on black or as a hairline border
- Do not add padding or chrome around illustration images - the image fills its grid cell edge-to-edge
- Do not create filled buttons; every interactive element is ghost/outlined (#000000 border, no fill)

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
