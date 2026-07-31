# Typography

### SF Pro Display - Display and heading typography - the choice of SF Pro Display signals a premium, iOS-adjacent system voice. Weights 500-600 (never 700+) keep headings from feeling heavy; the brand's authority comes from size, not weight. Display sizes escalate to 184px, creating poster-scale type that dominates every section. Line-height tightens to 0.95 at the largest sizes, making individual letters feel monumental and architectural. - `--font-sf-pro-display`
- **Substitute:** Inter, system-ui, -apple-system
- **Weights:** 500, 600
- **Sizes:** 16, 21, 36, 44, 78, 109, 148, 184
- **Line height:** 0.95, 1.00, 1.10, 1.20, 1.25
- **Letter spacing:** -0.007em, -0.01em, -0.012em, -0.023em, -0.026em, -0.027em, -0.034em
- **Role:** Display and heading typography - the choice of SF Pro Display signals a premium, iOS-adjacent system voice. Weights 500-600 (never 700+) keep headings from feeling heavy; the brand's authority comes from size, not weight. Display sizes escalate to 184px, creating poster-scale type that dominates every section. Line-height tightens to 0.95 at the largest sizes, making individual letters feel monumental and architectural.

### Arial - Body, links, card text, button labels - deliberately a system fallback so it stays invisible. While SF Pro Display headlines shout at 184px, Arial whispers at 14px in the background. This split (premium display + neutral body) is a deliberate hierarchy choice: the display type does all the emotional work, the body text just delivers information. - `--font-arial`
- **Substitute:** system-ui, -apple-system, Helvetica Neue, sans-serif
- **Weights:** 400, 500
- **Sizes:** 14
- **Line height:** 1.43
- **Letter spacing:** -0.034em
- **Role:** Body, links, card text, button labels - deliberately a system fallback so it stays invisible. While SF Pro Display headlines shout at 184px, Arial whispers at 14px in the background. This split (premium display + neutral body) is a deliberate hierarchy choice: the display type does all the emotional work, the body text just delivers information.

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption | 14px | 1.43 | -0.48px | `--text-caption` |
| body | 16px | 1.25 | 0.43px | `--text-body` |
| subheading | 21px | 1.25 | -0.15px | `--text-subheading` |
| heading-sm | 36px | 1.2 | -0.36px | `--text-heading-sm` |
| heading | 44px | 1.1 | -0.53px | `--text-heading` |
| heading-lg | 78px | 1 | -1.79px | `--text-heading-lg` |
| display | 109px | 1 | -2.83px | `--text-display` |
| display-lg | 148px | 1 | -4px | `--text-display-lg` |
| display-xl | 184px | 0.95 | -6.26px | `--text-display-xl` |
