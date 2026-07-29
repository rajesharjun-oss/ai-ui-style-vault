# Typography

## Font Families

| Role | Font | Token | Fallback |
| --- | --- | --- | --- |
| Primary | Inter | `--font-inter` | system-ui, -apple-system, Helvetica Neue, Arial, sans-serif |
| Code/meta | GeistMono | `--font-geistmono` | JetBrains Mono, Menlo, Monaco, Courier, monospace |
| System glyph | SF Pro Text | `--font-sf-pro-text` | system-ui, -apple-system, Helvetica Neue, Arial, sans-serif |
| System support | SF Pro | `--font-sf-pro` | system-ui, -apple-system, Helvetica Neue, Arial, sans-serif |

## Type Scale

| Role | Size | Weight | Line Height | Tracking | Token |
| --- | --- | --- | --- | --- | --- |
| eyebrow | 11px | 500 | 0.91 | 0.8px | `--text-eyebrow` |
| body | 16px | 400 | 1.15 | 0 | `--text-body` |
| body-lg | 18px | 400 | 1.15 | 0 | `--text-body-lg` |
| subheading | 20px | 500 | 1.2 | 0.2px | `--text-subheading` |
| heading-sm | 24px | 500 | 1.15 | 0 | `--text-heading-sm` |
| heading | 32px | 500 | 1.15 | 0 | `--text-heading` |
| heading-lg | 56px | 400 | 1.17 | 0.22px | `--text-heading-lg` |
| display | 64px | 600 | 1.1 | 0 | `--text-display` |

## Mono Scale

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| command-micro | 10px | 400 | 1 | 0.05em |
| metadata | 12px | 400 | 1.6 | 0.017em |
| code-label | 14px | 500 | 1.2 | 0 |

## Rules

- Body copy is Inter, never SF Pro Text.
- Hero headline uses Inter 56px regular weight.
- Use small medium Inter for nav and button labels.
- Use Geist Mono for version strings, platform requirements, install commands, and terminal cues.
- Use positive tracking on large type and uppercase micro labels.

