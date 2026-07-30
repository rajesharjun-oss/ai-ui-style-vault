# Guidelines

### Do
- Use the hard offset shadow (8px 8px 0px 0px #f1f1f1) exclusively on primary pill buttons - never apply blur or diffusion to elevation
- Set Inter Display at weight 400 only; let size and -0.03em tracking carry hierarchy, never switch to bold
- Reserve #855cf7 for the logo gradient and the active tab underline - every other accent must be the muted #dacefd lavender
- Pair every primary CTA with a ghost secondary button of identical 35px radius and padding
- Use 100px between major sections, 10-12px between inline elements, 24px inside cards
- Treat photography as full-bleed and unbordered - let the white canvas frame it like a gallery wall
- Apply Aux Mono 14px -0.04em to all eyebrow labels, timestamps, and tab headings

### Don't
- Do not introduce additional brand colors or saturated fills - the system is 99% achromatic by design
- Do not use soft blurred shadows on buttons; the signature is hard, solid, paper-cutout offsets
- Do not bold headlines or use weight 500+ in Inter Display - the single-weight hierarchy is intentional
- Do not round the active tab into a pill background; the 2px violet underline is the only acceptable indicator
- Do not add gradient backgrounds to sections or cards - gradients are reserved for the brand mark
- Do not use border-radius values outside the defined scale (35/20/14/9/2px)
- Do not center-align body paragraphs longer than two lines - the system is left-aligned with a centered display headline only

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
