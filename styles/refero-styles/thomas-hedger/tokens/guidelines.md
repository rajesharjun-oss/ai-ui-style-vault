# Guidelines

### Do
- Use the full 3-column edge-to-edge mosaic for all portfolio work - pageMaxWidth is null, the grid bleeds to the viewport.
- Set every corner radius to 0px - no rounded surfaces anywhere in the UI.
- Use Diatype Variable at 26px 500/700 for all navigation and section headings; reserve 700 for the designer's name and active emphasis.
- Use Diatype 400 at 19px for body and 9px for copyright/footer - the 9px caption is a signature scale choice.
- Keep internal tile padding at 3px and inter-tile gaps at 0-3px for a print-flat-file feel.
- Let project images supply all color - never introduce accent or brand color into chrome elements.
- Pair Carbon Plum (#29242b) with Ink Black (#000000) only when you need editorial warmth in headings; otherwise stay in pure Ink Black.

### Don't
- Do not add shadows, gradients, or border-radius to any component - the design is intentionally flat.
- Do not introduce accent, brand, or semantic colors (no success green, no error red) - the palette is a closed two-tone system.
- Do not use a serif or display font for navigation - Diatype Variable is the only allowed heading voice.
- Do not add hover backgrounds, underlines, or animation to nav links - text alone is the interactive surface.
- Do not wrap the grid in a centered max-width container - the mosaic must reach the viewport edges.
- Do not use type sizes outside the 9/13/19/26 scale - interpolation breaks the editorial rhythm.
- Do not add card surfaces, elevated panels, or modal containers - if it needs a container, the project image should fill it directly.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
