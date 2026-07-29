# Antimetal - Style Reference

> Editorial observatory on cream paper: quiet technical authority carried by regular serif headlines, warm gray surfaces, dashed dividers, and one tiny chartreuse signal.

**Theme:** light

Antimetal uses a restrained print-inspired SaaS language. The design feels closer to a research journal than a normal software landing page: warm canvas, cream panels, serif headlines, pull-quote pacing, tracked mono section markers, dashed separators, and calm CTA rhythm. Color is nearly absent. The only chromatic note is a small muted chartreuse accent used as punctuation.

## Tokens - Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Bistre | `#1a1614` | `--color-bistre` | Primary text, dark CTA fill, active strokes |
| Ash | `#2a2724` | `--color-ash` | Dark hover state, video timestamp chips |
| Slate | `#53504c` | `--color-slate` | Tertiary labels and quiet emphasis |
| Graphite | `#66635f` | `--color-graphite` | Secondary body copy, nav labels, support text |
| Flint | `#a8a7a1` | `--color-flint` | Muted helper text, disabled chrome, low-emphasis strokes |
| Parchment | `#d7d7d0` | `--color-parchment` | Dominant page canvas and warm gray field |
| Quill | `#e3e3de` | `--color-quill` | Hairline dividers, ghost borders, nav capsule fill |
| Cream | `#f7f6f3` | `--color-cream` | Primary surfaces, FAQ rows, section bands |
| Bone | `#fdfcfa` | `--color-bone` | Elevated card surfaces with faint warmth |
| Chartreuse Whisper | `#e2e67d` | `--color-chartreuse-whisper` | Sole accent for dots, badges, or tiny highlights |

## Tokens - Typography

- Display family: `Test Signifier`, fallback `Noto Serif`, `Georgia`, serif.
- Body/UI family: `Geist`, fallback `Inter`, system sans.
- Code/meta family: `Geist Mono`, fallback `JetBrains Mono`, ui-monospace.
- Display behavior: regular weight only, tight tracking at large sizes.
- UI behavior: Geist 400/500, small negative tracking.
- Mono behavior: uppercase, tracked, section-number style.

| Role | Size | Weight | Line height | Letter spacing | Use |
|------|------|--------|-------------|----------------|-----|
| Caption | 10px | 400 | 1.2 | 1px | Mono markers and tiny labels |
| Body Small | 14px | 400-500 | 1.5 | -0.01em | Buttons, nav, utility copy |
| Body | 16px | 400 | 1.5 | -0.01em | Main body copy |
| Subheading | 20px | 400 | 1.5 | 0 | Serif subheads |
| Heading Small | 24px | 400 | 1.2 | 0 | FAQ rows and compact serif headers |
| Heading | 36px | 400 | 1.1 | 0 | Section headings |
| Heading Large | 48px | 400 | 1.1 | -1.008px | Large section headings |
| Display | 54px | 400 | 1.1 | -1.998px | Hero display |

## Tokens - Spacing And Shape

| Purpose | Value |
|---------|-------|
| Density | comfortable |
| Base unit | 4px |
| Max width | 1200px |
| Section gap | 120px |
| Card padding | 40px |
| Element gap | 16px |
| Spacing scale | 4, 8, 12, 16, 20, 24, 28, 32, 40, 48, 64, 80, 100, 120, 240px |
| Cards | 4px radius |
| Buttons | 9999px radius |
| Nav capsule | 82px radius |
| Large pills | 999px radius |

## Components

- Dark pill button: one primary CTA per viewport, `#1a1614` fill, cream text, full pill radius, Geist 14px/500.
- Ghost outlined button: transparent secondary CTA, solid outline, square rhythm, always paired with the dark pill.
- Liquid-glass nav capsule: floating 82px capsule, warm translucent fill, blur/saturation filter, subtle inset depth.
- FAQ accordion row: cream background, dashed 1px separators, Test Signifier 24px question text, Geist body copy when expanded.
- Section header marker: Geist Mono 10-11px uppercase marker, formatted like `05 - FAQ`, with tracked letters.
- Drop cap body paragraph: editorial first-letter treatment for long-form copy.
- Pull quote block: large serif quote with quiet attribution, no card background.
- Video thumbnail card: restrained image, circular play control, small dark timestamp chip.

## Layout And Imagery

Use a 1200px centered page. Keep sections spacious and editorial. Pair long text blocks with quiet media, video thumbnails, or typographic moments. Avoid dense product dashboards. Let the typography carry hierarchy.

## Do

- Set all headings in Test Signifier weight 400.
- Use dashed 1px dividers in low-opacity Bistre for content separators.
- Pair a dark pill CTA with a secondary ghost button.
- Number major sections with tracked Geist Mono markers.
- Keep the canvas at `#d7d7d0` and surfaces at `#f7f6f3`.
- Reserve `#e2e67d` for one small accent at a time.
- Use 82px radius for nav and 9999px for buttons.

## Do Not

- Do not bold headings.
- Do not use solid borders for internal content separators.
- Do not use pure white or pure black as the dominant system color.
- Do not spread chartreuse across large surfaces.
- Do not make cards overly rounded.
- Do not use loud SaaS-blue CTAs.
- Do not add decorative gradients or heavy shadows.
