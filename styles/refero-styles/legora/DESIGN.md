# Legora - Style Reference

Legora is a warm legal-editorial design system. It reads more like a legal journal than a SaaS landing page: parchment canvas, fine serif headlines, humanist body copy, black hairline structure, and pastel wash product panels. The brand feels authoritative because it removes nearly all chromatic decoration.

## Theme

- Theme mode: light with a dark photographic hero.
- Visual temperature: warm parchment, black ink, muted legal-document washes.
- Surface logic: parchment canvas, sage wash panels, slate mist product cards, black hairlines.
- Energy: editorial, restrained, legal, formal, premium.

## Core Principles

1. Use the parchment canvas everywhere outside the hero.
2. Use Rhymes Display 300 for opening headlines.
3. Use Suisse-style sans for body and UI copy.
4. Use one solid black CTA per viewport.
5. Use pale accent washes as broad surfaces, never as small accent chips.
6. Separate surfaces with hairlines, not drop shadows.
7. Keep partner logos monochrome.
8. Use one full-bleed cinematic hero photo at most.

## Color System

| Name | Value | Role |
| --- | --- | --- |
| Parchment | `#fefefc` | Page canvas, card surfaces, light-section backgrounds |
| Ink | `#000000` | Solid CTA fill, dark borders, inverted UI separators |
| Graphite | `#0a0a0a` | Body text, heading strokes, dark surface accents |
| Iron | `#444444` | Tertiary text and intermediate dividers |
| Smoke | `#6b6b6b` | Secondary body copy, subdued borders, captions |
| Verdigris Wash | `#ebf5ed` | Sage-tinted product panels and calm active washes |
| Slate Mist | `#bdd4f0` | Cool product-preview panels and background links |
| Pewter Haze | `#98a7aa` | Disabled fills, placeholders, empty illustration frames |

## Typography

Display type is Rhymes Display. Use the 300 weight for hero and section-opening headlines. Fallbacks for prototypes: Playfair Display 400 or Cormorant Garamond Light.

Primary UI/body type is Suisse Intl or Suisse Intl Book. Fallbacks: Inter 400/500 or Sohne. For long neutral paragraphs, Aktiv Grotesk VF can be used as a secondary sans, but the core voice remains Suisse plus Rhymes.

OpenType features used in the source system: `blwf`, `cv03`, `cv04`, `cv09`, `cv11`.

Recommended scale:

| Token | Family | Size | Weight | Line Height | Letter Spacing |
| --- | --- | ---: | ---: | ---: | ---: |
| Caption | Suisse Intl | 11px | 450 | 0.8 | 0.1px |
| UI Small | Suisse Intl | 13px | 500 | 1.0 | -0.01em |
| Body Small | Suisse Intl | 14px | 450 | 1.3 | -0.01em |
| Body | Suisse Intl | 16px | 450 | 1.25 | -0.01em |
| Body Long | Aktiv Grotesk | 15px | 400 | 1.3 | 0 |
| Heading Small | Aktiv Grotesk | 20px | 400 | 1.3 | 0 |
| Heading | Rhymes Display | 32px | 300 | 1.1 | -0.32px |
| Display | Rhymes Display | 88px | 300 | 0.95 | -1.76px |

Rules:

- Never use bold or semibold display weights.
- Use Rhymes Display 300 for all opening display moments.
- Body copy should sit at 14px to 16px with tight tracking.
- Do not replace body type with a default system font in production.
- Keep display headlines to one or two lines.

## Spacing And Shape

- Density: compact.
- Max content width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 10px.
- Spacing values: 4, 6, 8, 10, 12, 16, 20, 24, 32, 36, 40, 48, 56, 64, 80, 160.

Radius:

- Tags: 2px.
- Buttons: 2px.
- Cards: 8px.
- Inputs: 8px.
- Avoid 0px button radius and fully rounded pill buttons.

## Elevation

Legora has no shadow-based elevation.

- Do not use drop shadows.
- Do not use raised card stacks.
- Use 1px hairlines in Ink or Graphite.
- Use Verdigris Wash and Slate Mist as full-surface panels.
- Product UI can sit flat on tinted cards.

## Layout

- Hero breaks containment: full-bleed dark cinematic photograph.
- Hero headline is centered/lower-third, set in parchment text.
- Below hero, return to a centered 1200px parchment column.
- Use a partner logo bar with monochrome logos at 60 to 70 percent opacity.
- Use a narrow editorial intro paragraph, around 60 percent of content width.
- Use a three-column feature grid with tall pastel product cards.
- Use wider two-column text and image sections with 55/45 proportions.
- Keep 80px vertical rhythm between sections.

## Imagery

Preferred imagery:

- One full-bleed dark cinematic still in the hero.
- Pastel product UI mockups in Slate Mist or Verdigris Wash.
- Document lists, search overlays, legal document surfaces.
- Monochrome partner logos.
- Thin monochrome line icons.

Avoid:

- Multiple full-bleed photos.
- Stock lifestyle photography.
- Decorative illustration.
- Saturated colors.
- Native-color partner logos.
- Shadowed product cards.

## Motion

Motion should be nearly invisible.

- Use restrained hover states on buttons and links.
- Input focus can switch border color to Verdigris Wash.
- Avoid parallax, animated gradients, photo reveals, and dramatic transitions.

