# Typography

## Fonts

- Serif (custom resembles a high-contrast modern editorial serif like Reckless Neue, GT Sectra, or PP Editorial New) All display and heading copy. Used at poster sizes (6496px) for hero headlines and product section titles. The weight 300 at 96px is the signature move whisper-thin strokes at near-poster scale create authority through restraint, not volume. Tight tracking (-0.05em) at all sizes; line-heights under 1.1 let letterspacing do the vertical work `--font-serif-custom-resembles-a-high-contrast-modern-editorial-serif-like-reckless-neue-gt-sectra-or-pp-editorial-new`
- Mono (custom clean geometric monospace) All UI text: navigation, buttons, labels, body copy, metadata, footer links. The mono choice is deliberate it makes every UI element feel like terminal output or code annotation, contrasting the serif's editorial softness. Weight 400 dominates; 500 for button text; 300 reserved for large mono headings (2848px range) `--font-mono-custom-clean-geometric-monospace`

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- |
| caption | 12px | 17 | -0.8px | `--text-caption` |
| body-sm | 14px | 19 | -0.94px | `--text-body-sm` |
| body | 16px | 24 | -1.07px | `--text-body` |
| subheading | 20px | 30 | -0.5px | `--text-subheading` |
| heading-sm | 24px | 24 | -1.2px | `--text-heading-sm` |
| heading | 32px | 32 | -1.6px | `--text-heading` |
| heading-lg | 48px | 54 | -2.4px | `--text-heading-lg` |
| display-sm | 64px | 64 | -3.2px | `--text-display-sm` |
| display | 96px | 90 | -4.8px | `--text-display` |

## Notes

- Preserve the extracted type hierarchy before inventing new sizes.
- Use fallback fonts with similar proportions if the source fonts are unavailable.
