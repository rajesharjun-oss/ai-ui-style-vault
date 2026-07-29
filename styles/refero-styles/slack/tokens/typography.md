# Typography

## Fonts

- Salesforce-Avant-Garde Display and heading face geometric, wide, compressed. Carries every headline from 21px subheads up to 96px hero display. The 400-weight at 76px is anti-convention: Slack trusts its letterforms enough to let headlines whisper rather than shout. Tracking tightens progressively from -0.004em at body sizes to -0.012em at 64px+ `--font-salesforce-avant-garde`
- Salesforce-Sans Workhorse body and UI face handles nav, body copy, buttons, captions, and labels. The 12px/700 with 0.057em tracking (uppercase) is the eyebrow-label pattern used for section tags. Body sits at 16px/1.5 generous enough for reading, compact enough for dense product cards `--font-salesforce-sans`

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- |
| eyebrow | 12px | 1.5 | 0.68px | `--text-eyebrow` |
| caption | 14px | 1.56 | -0.03px | `--text-caption` |
| body-sm | 16px | 1.5 | -0.16px | `--text-body-sm` |
| body | 18px | 1.56 | -0.22px | `--text-body` |
| subheading | 32px | 1.25 | -0.26px | `--text-subheading` |
| heading-sm | 50px | 1 | -0.6px | `--text-heading-sm` |
| heading | 64px | 1.12 | -0.77px | `--text-heading` |
| heading-lg | 76px | 1.2 | -0.91px | `--text-heading-lg` |
| display | 96px | 1.08 | -1.15px | `--text-display` |

## Notes

- Preserve the extracted type hierarchy before inventing new sizes.
- Use fallback fonts with similar proportions if the source fonts are unavailable.
