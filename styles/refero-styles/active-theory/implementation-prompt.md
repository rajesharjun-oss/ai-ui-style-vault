# Implementation Prompt

Build a dark immersive WebGL-first interface inspired by Active Theory.

Use pure `#000000` as the page canvas and keep it absolute. Do not introduce gray page backgrounds, white cards, or light theme sections. The rendered scene is the design; UI chrome must be minimal, translucent, and quiet.

Use `#343755` as the only chromatic UI accent, reserved for a singular dominant filled pill CTA. Use `#ffffff` for primary text, `#4d4d4d` for card and divider borders, `#808080` and `#999999` for ghost borders, and `#c6c6c6` for tertiary text and inline links.

Use nbarchitekt or Space Grotesk for navigation, buttons, labels, and micro UI. Keep nav around `10px` to `12px` weight 400, and use `14px` weight 700 for button labels. Use Times or Times New Roman for body copy at `16px` with generous `1.88` line height.

Use transparent and translucent components: ghost buttons with `2px solid rgba(255,255,255,0.6)` borders, frosted cookie banners with `rgba(0,0,0,0.5)` background and `backdrop-filter: blur(4px)`, and project cards with transparent fill plus `1px #4d4d4d` borders. Use 5px radius for ghost rectangle controls, 12px for cards, and 500px for pill buttons or tags.

Do not use shadows, UI gradients, additional accent colors, solid white card backgrounds, or light-mode components. Motion should favor opacity fades and cinematic pacing: quick UI feedback at `0.2s` to `0.4s`, slower scene transitions around `0.8s` to `9s`.
