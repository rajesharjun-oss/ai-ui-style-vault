# Typography

## Primary Typeface

Inter Variable is the system voice. Use it for body, navigation, headings, buttons, links, lists, and footer UI.

- Fallback: Inter, system-ui, sans-serif.
- Weights: 400, 500, 510, 590.
- Signature: 510 for headings and active controls; 590 for emphasis.
- Avoid: default 600/700 bold when variable weights are available.

## Monospace Typeface

Berkeley Mono is a quiet technical accent.

- Fallback: JetBrains Mono, IBM Plex Mono, ui-monospace.
- Weights: 400, 590.
- Sizes: usually 13px to 15px, occasionally 21px for a feature command.
- Use for: inline code, command cards, keyboard hints, metadata, technical callouts.
- Avoid using it for long paragraphs, nav, or main headings.

## Type Scale

| Role | Size | Line Height | Letter Spacing | Weight |
| --- | --- | --- | --- | --- |
| Caption | 12px | 1.6 | -0.12px | 400 |
| Body | 15px | 1.5 | -0.15px | 400 |
| Heading Small | 24px | 1.33 | -0.288px | 510 |
| Heading | 32px | 1.2 | -0.416px | 510 |
| Display | 48px | 1.13 | -1.056px | 590 |

## Implementation Notes

- Keep prose compact and readable rather than huge and editorial.
- Use text color changes for emphasis before reaching for heavy weight.
- Let Snow text and tight spacing carry hierarchy.
- Keep the monospace accent sparse enough that it still feels intentional.
