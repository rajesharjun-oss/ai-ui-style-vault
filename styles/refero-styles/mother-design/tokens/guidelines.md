# Guidelines

### Do
- Set display type at 226px with -0.04em letter-spacing and line-height 1.0 - the extreme scale is the signature, not an exception.
- Use only the five colors: #f4f4f4 canvas, #ffffff surface, #000000 text and rules, #808080 secondary, #306f09 as the only chromatic note.
- Structure all layout with 1px Press Black rules - vertical, horizontal, and as borders on interactive cells. Never use shadows or fills to separate regions.
- Use Basis Mono with +0.06em tracking for metadata, labels, and the news ticker. Reserve Basis for everything else; bring in Times only for the occasional editorial annotation.
- Keep card and thumbnail padding at 0px. Let raw images sit edge-to-edge in their grid cells with no chrome, border, or radius.
- Anchor the nav with a 1px-bordered segmented control: brand mark cell + tab group on the left, theme toggle cluster on the right. Bone White fill, no radius.
- Treat whitespace as a structural element - large vertical gaps (160-200px) between the portfolio grid and the next section are part of the system, not negative space to be filled.

### Don't
- Do not introduce additional colors. Any new hue, even a desaturated one, will dilute the broadsheet identity. The green is a printer's mark, not a palette swatch.
- Do not add box-shadows, blurs, or any form of elevation. The system has no z-axis - depth is typographic.
- Do not round corners. Every border, button, and cell stays at 0px radius. Curvature would betray the printed-page metaphor.
- Do not cap display type at conventional web sizes (48-72px). The 226px / 110px scale is the point - shrinking it to 'feel more modern' removes the signature.
- Do not use weight 700 or 800. Basis 600 is the heaviest weight in the system; 400 does the work at display sizes because the size itself provides weight.
- Do not add icons inside buttons or cards. Icons live only in the theme toggle cluster and the brand mark cell.
- Do not center body copy or set paragraphs to a narrow max-width. The manifesto reads full-bleed; column width is controlled by the grid, not by a content container.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
