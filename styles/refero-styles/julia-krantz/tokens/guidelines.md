# Guidelines

### Do
- Use #000000 for all backgrounds - the CSS token --bg: #000 is absolute; never substitute dark gray or near-black
- Set all ClashDisplay display headings (44px tile codes) at weight 300 with letter-spacing -0.04em - the ultra-light setting against photography is the signature move
- Apply 1px solid rgba(248,248,248,0.12) for every structural border: tile separators, section dividers, column rules
- Keep all interactive hover states to color/filter transitions only - color: rgba(248,248,248,0.45) for links, filter: brightness(0.82) for image tiles, 0.2s ease
- Use 0px border-radius on every element - tiles, any containers, any interactive elements. The sharp-corner rule is absolute
- Maintain DM Sans weight 300 for all body, nav, and label text - no bold text anywhere in the UI layer
- Express secondary hierarchy through #707070 (section labels, numbers, category tags) - never through size increases or weight changes

### Don't
- Never add any color to the UI chrome - buttons, links, labels, borders must remain in the #f8f8f8 / #707070 / rgba opacity system only
- Never round corners - no border-radius on tiles, containers, or any interactive element; 0px is non-negotiable
- Never use font weight above 500 - ClashDisplay 500 is the ceiling and used only for the name logotype; DM Sans stays at 300
- Never add box-shadows or elevation - the design has zero shadow tokens; depth comes from contrast with the black canvas only
- Never add hover backgrounds or button fills - interactive states change text opacity or image brightness only, never add a background color
- Never introduce gradients, overlays, or tinted backgrounds - the CSS tokens confirm no gradient system exists; #000 is the only background
- Never separate the category label from its tile project code with more than 4px margin - the tight stacking (4px marginBottom between elements) is the spatial rhythm

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
