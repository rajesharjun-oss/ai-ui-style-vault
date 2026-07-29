# Implementation Prompt

Build a light developer-product interface in the Cursor style.

Use a warm parchment canvas (`#f7f7f4`) and warm ink text (`#26251e`). Avoid pure white and pure black as foundational colors. Cards and product mockups should use Bone (`#f2f1ed`) with 1px warm hairline borders and soft warm paper shadows. Use Linen (`#e6e5e0`) for secondary buttons and logo tiles. Use Ember (`#f54e00`) only for inline links, tags, and short emphasis. Do not use Ember as a CTA background or large surface.

Typography is the signature. Use CursorGothic or a close Inter/system fallback for UI, headings, navigation, and body. Headings must stay weight 400, never bold. Apply tighter tracking as text grows: around 22px use about -0.11px, 26px use about -0.312px, 36px use about -0.72px, and 72px use about -2.16px. Use EB Garamond only for selected editorial subheads or prose. Use berkeleyMono at 12px or 13px for code, file paths, model names, CLI snippets, and metadata.

Keep spacing compact on a 4px base unit. Use 1300px max width, 24px page padding, 64px to 96px section gaps, 24px card padding, and 8px internal rhythm. Shape is strict: 4px radius for cards, buttons, inputs, and tiles; 8px for modals only. Avoid pills.

Expected components:

- Transparent 52px nav with logo left, compact links center, and sign-in/contact/download actions right.
- Primary filled button: Ink background, Parchment text, 4px radius, CursorGothic 14px/400.
- Secondary button: Linen background, Ink text, 4px radius.
- Ghost text button: transparent, muted Ink, no border, underline on hover.
- Product mockup card: Bone background, 4px radius, warm hairline border, 24px padding, soft warm shadow.
- Window mockup frame: macOS-style dots, centered title, file tabs, IDE/code content, berkeleyMono labels.
- Terminal input: Bone or transparent background, 1px warm border, 4px radius, berkeleyMono 12px.
- Logo trust strip: one row of Linen tiles with monochrome logos.

The page should feel calm, precise, editorial, and developer-native. Product screenshots, IDE windows, terminal panels, and code views should carry the visual weight. Avoid lifestyle photos, decorative blobs, gradients, oversized rounded corners, and loud marketing color.
