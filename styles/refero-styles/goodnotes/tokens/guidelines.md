# Guidelines

### Do
- Use #57d2ee exclusively for the primary filled CTA button - no other UI element should share this fill color, keeping it as the sole chromatic action signal.
- Apply Roobert at weight 700 with letter-spacing -0.05em (-2.4px) for all 48px display headlines; tighten tracking proportionally down the scale to -0.016em at 20-22px.
- Define card and container edges with 0.5-1px solid #bebebe or #e8e8e8 borders - never use box-shadow for surface elevation.
- Use 10px border-radius universally across buttons, cards, inputs, and UI chrome; reserve 4px only for focus/link rings.
- Keep body copy at #565656 or #666666 on white cards - reserve #000000 for headings and primary labels only.
- Use #f2e6b3 as an inline background highlight on emphasized text spans - apply it flat (no radius) to mirror a physical highlighter stroke.
- Separate section content with 80px vertical gaps on desktop; use 24px element gap within card grids and between grouped UI elements.

### Don't
- Never add box-shadow to cards, modals, or buttons - all surface separation must come from borders, not elevation.
- Never use a second chromatic fill color for buttons; ghost (#1e1e1 border) and tinted-teal (rgba(87,210,238,0.1)) variants must stay visually subordinate to the cyan CTA.
- Never set headline letter-spacing to 0 or positive values at sizes above 24px - the negative tracking is the signature of the display voice.
- Never substitute a different typeface for Roobert; if the custom font fails to load, fall back to Plus Jakarta Sans or DM Sans - not Inter or system-ui.
- Never use #0299e0 (Sky Link) as a button fill or a section color - it is reserved for inline hyperlinks and "Learn more" text in white-background contexts only.
- Never apply the teal tinted button (rgba(87,210,238,0.1)) with a border-radius - it is a 0px radius tab control, not a pill or rounded button.
- Never center-align body copy paragraphs beyond 600px width - long centered text breaks readability; left-align body text in two-column feature sections.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
