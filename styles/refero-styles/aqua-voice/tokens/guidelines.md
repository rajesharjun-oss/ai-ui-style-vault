# Guidelines

### Do
- Use weight 200 for all display and headline text in PP Neue Montreal - the ultra-light cut is the brand's visual signature.
- Use Sky Signal (#67beff) only for the filled primary CTA and the live-status dot; never extend it to backgrounds, illustrations, or decorative fills.
- Set headline line-height to 1.00-1.10 - the tight leading is essential to the whisper aesthetic and prevents the light weight from looking fragile.
- Keep card padding in the 20-24px range and radii at 12-20px; tighter and it feels cramped, wider and it competes with the generous page-level spacing.
- Use Ghost buttons (transparent + Slate text) for all secondary actions; reserve the filled Sky Signal button exclusively for the single primary action on each screen.
- Apply the hairline Linen (#e5e8ec) border pattern with rgba(0,0,0,0.02) shadow for elevated surfaces - the system uses depth in millimeters, not millimeters turned into centimeters.
- Center text blocks at max-width 680px for readability; let the surrounding negative space carry the page rhythm.

### Don't
- Do not use weights above 500 for PP Neue Montreal - the Medium 500 is already the upper bound; 600+ destroys the whisper character of the system.
- Do not add color to body copy, headings, or backgrounds beyond the Inkstone/Slate/Pewter neutral scale - chromatic text breaks the monochrome contract.
- Do not apply large or saturated shadows; the system intentionally operates at rgba(0,0,0,0.02) to rgba(0,0,0,0.1) depth only.
- Do not use pill shapes (9999px radius) for primary buttons - 8px is the button radius; pill shapes are reserved for tags and status chips.
- Do not introduce gradients, glassmorphism, or heavy blur effects - the design language is flat, matte, and paper-like.
- Do not set headline letter-spacing to negative values - PP Neue Montreal is already optically balanced; additional tracking adjustment creates inconsistency with the font's native rhythm.
- Do not use Electric Iris (#4288ff) as a fill - it is an outline/link/ghost action color only; Sky Signal owns the filled action role.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
