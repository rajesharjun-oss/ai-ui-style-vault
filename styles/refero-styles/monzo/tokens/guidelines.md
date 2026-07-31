# Guidelines

### Do
- Use 500px border-radius for all interactive pills - buttons, nav toggles, tag chips, and the search bar. This is the system's defining shape.
- Keep the interface 95% achromatic. Let Hot Coral (#ff4f40) appear only on the logo, links, headings, icons, and the card product - never as a background fill for UI controls.
- Use MonzoSansDisplay 600-800 for all headings at 36px and above. The heavier weight range is non-negotiable for display type.
- Apply -0.05em letter-spacing to all MonzoSansText usage. This is a brand-defining typographic detail, not optional.
- Layer surfaces on the mint canvas (#f2f8f3 #ffffff #e3ebe4) instead of using shadows. Elevation is communicated by color stepping, not by drop shadows.
- Set body text at 20px with 1.4 line-height for descriptive paragraphs. Monzo's text size runs larger than typical SaaS - 16px is the floor, not the default.
- Use 64px border-radius on all large containers - hero cards, product showcases, section panels. This generous rounding is as recognizable as the coral.

### Don't
- Don't use Hot Coral as a button background fill. It is for text, icons, logos, and the card product only - never for a solid CTA surface.
- Don't add drop shadows to cards or buttons. The system uses a single rgba(0,0,0,0.1) 0px 0px 10px shadow sparingly; most separation comes from surface color stepping on the mint canvas.
- Don't use system fonts or non-brand sans-serifs. Always specify MonzoSansText for body and MonzoSansDisplay for headings.
- Don't use letter-spacing other than -0.05em on MonzoSansText or normal on MonzoSansDisplay. Deviating breaks the brand's typographic fingerprint.
- Don't mix red and dark navy as a gradient or color pair on the same element. Coral is the accent; navy is the ground. They alternate, they don't blend.
- Don't use square or 8px radii on primary buttons or large containers. 500px pills and 64px containers are the two shape languages - anything between looks generic.
- Don't set body text below 16px or headlines below 32px. The type scale is deliberately generous; small text breaks the warm, spacious feel.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
