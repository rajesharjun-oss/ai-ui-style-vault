# Guidelines

### Do
- Use Poppins exclusively for all text; never substitute Inter, Roboto, or system fonts in production UI
- Set border-radius to 100px for all buttons, tags, and avatars to maintain the pill-shaped identity
- Use Iris Violet (#5562eb) as the single primary action color - never introduce a second blue or accent for CTAs
- Keep headlines at weight 300 or 400 - never bold (600+) display text, the whisper-weight is the signature
- Apply the violet-to-green gradient (linear-gradient(120deg, #5562eb 40%, #7ac17b 61%)) only to hero headline words, not to buttons or backgrounds
- Use the lavender canvas (#ebefff) as the page base - white-only pages break the brand atmosphere
- Reserve Focus Green (#7ac17b) for calendar time blocks and positive stat numbers, not for success toasts or status badges

### Don't
- Do not use drop shadows on cards - Reclaim uses border-radius and surface contrast instead of elevation
- Do not introduce a new accent color (orange, pink, teal) - the system is two-color: Iris Violet + Focus Green
- Do not use weight 700 or 800 for any text - Poppins tops out at 600 and most display text is 300-400
- Do not use 0px border-radius on any container - minimum 3px, standard 10px for cards
- Do not apply the violet-green gradient to buttons, backgrounds, or full headlines - only individual words in hero text
- Do not use pure white (#ffffff) as the page background - the lavender canvas is the brand base
- Do not use box-shadow for hover or focus states - use color shift to Sapphire Violet (#3451e8) instead

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
