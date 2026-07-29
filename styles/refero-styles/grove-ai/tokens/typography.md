# Typography

## Fonts

- sans-serif sans-serif detected in extracted data but not described by AI `--font-sans-serif`
- Libre Caslon Text Display serif used exclusively for hero-level headlines and the signature brand word. The italic-leaning contrast strokes give "Grace" and "Meet" a humanized, editorial voice that contrasts with the precise Geist below. The choice is anti-SaaS: most clinical-tech sites use a geometric sans for the hero; this serif makes the brand feel like a respected medical publication. `--font-libre-caslon-text`
- Geist Primary interface and body typeface. Covers body copy (16/24px, 400), subheadings (1820px, 500), card titles (2024px, 600), and large stat numbers (3240px, 500/600). The negative letter-spacing tightens as size grows, creating density at body size and breathing room at display. `--font-geist`
- Geist Mono Monospaced variant for code-like or technical callouts in body content where alignment matters. `--font-geist-mono`

## Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- |
| caption | 12px | 1.5 | 1.2px | `--text-caption` |
| body-sm | 14px | 1.5 | -0.28px | `--text-body-sm` |
| body | 16px | 1.5 | -0.32px | `--text-body` |
| subheading | 20px | 1.25 | -0.4px | `--text-subheading` |
| heading-sm | 24px | 1.25 | -0.6px | `--text-heading-sm` |
| heading | 32px | 1.2 | -0.9px | `--text-heading` |
| heading-lg | 40px | 1.2 | -1.44px | `--text-heading-lg` |
| display | 92px | 1.2 | -1.01px | `--text-display` |

## Notes

- Preserve the extracted type hierarchy before inventing new sizes.
- Use fallback fonts with similar proportions if the source fonts are unavailable.
