# Guidelines

### Do
- Use 9999px border-radius for every button, tag, and search field - the pill shape is non-negotiable for Spotify's identity.
- Apply 6px radius to all square content cards (albums, playlists) and 9999px for circular artist portraits - never mix radii within the same card type.
- Reserve #1ed760 for the single most important action per screen - log in, play, confirm. Never use it for secondary links, metadata, or decorative elements.
- Keep all text between 11px and 24px. The system is compact; no body copy should exceed 16px, and only section headings reach 24px.
- Use #000000 for the page canvas, #121212 for content cards, and #1f1f1f for interactive controls - maintain this three-tier surface hierarchy on every screen.
- Apply the 0px 8px 24px rgba(0,0,0,0.5) shadow only to content cards lifted off the canvas, never to navigation, buttons, or inputs.
- Let album artwork and artist photography supply all chromatic color in the interface. The chrome itself should remain monochrome with #ffffff and #b3b3b3 as the only text colors.

### Don't
- Do not introduce a new chromatic accent color. The entire system runs on one green (#1ed760) plus the magenta-to-cobalt gradient for premium promotions.
- Do not use sharp corners (<4px radius) on any interactive element. Pills and soft 6px squares are the only acceptable shapes.
- Do not set body text below 11px or above 16px. The 4px size band is deliberate and compact.
- Do not use #1ed760 for hover states on white or dark buttons - green is exclusively a primary action fill, never a state indicator.
- Do not apply the premium magenta-to-cobalt gradient outside of subscription/promotional contexts. It is reserved for upsell moments.
- Do not use white or light backgrounds for any surface. The system is dark-first; even elevated cards stay at #1f1f1f or below.
- Do not add multi-layer shadow stacks, colored glows, or neumorphic effects. The single rgba(0,0,0,0.5) drop shadow is the only elevation treatment.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
