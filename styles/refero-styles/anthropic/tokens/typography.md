# Typography

## Type System

Use a serif for editorial voice and body text. Use a sans-serif for chrome, navigation, buttons,
footers, badges, and decisive display statements. Use mono only for code or technical snippets.

## Fonts

| Font | Token | Substitutes | Weights | Sizes | Line Height | Letter Spacing | Role |
|---|---|---|---|---|---|---|---|
| Anthropic Serif | `--font-anthropic-serif` | Georgia, Source Serif Pro, Charter | 400, 600 | 14px, 18px, 20px, 24px, 68px | 1.10, 1.40, 1.43 | normal | Editorial body, display heading, card titles, and supporting paragraphs. |
| Anthropic Sans | `--font-anthropic-sans` | Inter, system-ui, Arial | 400, 500, 600, 700 | 12px, 15px, 16px, 20px, 24px, 61px | 1.00 to 1.40 | Tight UI tracking | UI chrome, nav, buttons, footers, badges, and 61px declarative display. |
| Anthropic Mono | `--font-anthropic-mono` | JetBrains Mono, SF Mono, Menlo | 400 | 16px | 1.40 | normal | Code and technical snippets only. |

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| caption | `12px` | `1.4` | `-0.24px` | `--text-caption` |
| body-sm | `16px` | `1` | `-0.08px` | `--text-body-sm` |
| body | `20px` | `1.4` | normal | `--text-body` |
| subheading | `24px` | `1.3` | `-0.05px` | `--text-subheading` |
| heading | `61px` | `1.1` | `-0.12px` | `--text-heading` |
| display | `68px` | `1.1` | normal | `--text-display` |

## Rules

- Use Serif at `20px` for body copy.
- Use Sans at `12px` to `16px` for UI chrome.
- Use Sans `61px` weight `700` for declarative statements.
- Use Serif `68px` weight `400` for editorial display.
- Keep body copy out of sans when the publication voice matters.
- Reserve Mono for code or technical snippets.
- Use tight tracking in small sans labels and captions.

