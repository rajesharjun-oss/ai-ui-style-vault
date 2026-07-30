# Guidelines

### Do
- Use #019d91 fill + #ffffff text for every primary action button (Get started, Sign up, Explore, See all).
- Apply border-radius 8px to buttons and inputs, 16px to standard cards, 24px to feature/hero panels, 48px to oversized dark hero panels.
- Headlines 32px and above must use DM Sans weight 500 with the matching negative letter-spacing: -0.0300em at 32px, -0.0400em at 48-64px, -0.0500em at 96px.
- Body, navigation, buttons, and small UI copy use Inter only - never mix DM Sans into utility text below 24px.
- Set page background to #f4f4f5 and place raised white cards (#ffffff) on top with 24px or 32px padding.
- Use 1px solid #e4e4e7 or #f2f2f3 as the only border treatment - never thicker than 1px on standard UI.
- Place colorful illustrations and animation thumbnails on the warm-gray canvas with no card chrome - let the artwork be the visual, not a wrapper.

### Don't
- Never use #000000 pure black as a card or surface fill - use #09090b or #18181b instead so surfaces feel ink-toned, not harsh.
- Never apply weight 700 or 800 to headlines - the system uses weight 500 even at 96px display sizes.
- Never use a drop shadow on cards - the elevation language is built from background contrast and rounded corners, not shadows.
- Never combine #019d91 with bold gradients, glassmorphism, or neon glow - the teal must read as a flat, confident fill.
- Never use #ff6900 (ember) for decoration or branding - it is reserved for warning/attention states.
- Never put body copy below 14px - captions stop at 12px and labels at 10px, and always use weight 500 for non-body sizes under 16px.
- Never break the spacing rhythm: gaps inside components are 4-8px, component-internal padding is 16-24px, between sections is 80px.

## Accessibility Notes

- Verify contrast for every text and action pairing.
- Preserve keyboard focus states even if the source visual language is quiet.
- Keep target sizes comfortable on mobile and desktop.
