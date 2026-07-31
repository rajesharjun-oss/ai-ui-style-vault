# Guidelines

### Do
- Use #4d1520 as the default text color and primary button fill - it is the system's single chromatic anchor and should appear in every screen
- Set page canvas to #fbf9f6 parchment, not pure white - the warm ivory is what makes the burgundy sing
- Use 6px radius for all cards, buttons, and inputs as the default; reserve 1440px for pill badges only
- Use Tt Commons Pro at weight 400 for display headings 44px and above - the whisper-weight at large size is a signature
- Apply the wine-tinted shadow rgba(77,21,32,0.16) 19px 32px 73px only on hero-scale elevated cards, never on small UI elements
- Use #faffa7 lemon as a decorative accent fill in illustration blocks and badge backgrounds - never as a text color on dark surfaces
- Center content within a 1200px max-width column with 24-40px horizontal padding for comfortable reading rhythm

### Don't
- Do not introduce cold grays (#e5e7eb, #f3f4f6, #6b7280) - the entire system is warm-toned and cool neutrals will clash
- Do not use 8px or 12px border-radius on cards or buttons - the 6px radius is part of the system's distinctive geometry
- Do not set body or heading text to weight 600 or 700 - the system maxes out at 600 for emphasis and prefers 400-500
- Do not use pure black (#000000) for text - use #4d1520 wine ink instead, even for body copy
- Do not add drop shadows to buttons, nav items, or small interactive elements - shadows are reserved for hero-scale elevation
- Do not use blue, green, or standard semantic colors for status - the system communicates state through opacity, position, and the single brand hue
- Do not center-align body paragraphs longer than two lines - left-align for readability; center only for headlines and short CTAs

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
