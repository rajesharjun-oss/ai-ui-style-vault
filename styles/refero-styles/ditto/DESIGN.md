# Ditto - Style Reference

Theme: light

Ditto's Refero style is a sunlit compliance SaaS language. It uses a warm cream page canvas, green-tinted card surfaces, deep violet ink, and bright yellow pill CTAs. Organic blobs in green, fuchsia, yellow, and violet soften the B2B context, but those decorative colors are tightly separated from functional UI.

## Core Principles

- Use warm cream and Soft Meadow surfaces instead of sterile white/gray.
- Use Deep Ink for primary text and structure.
- Use Hi-Yellow as the only primary filled CTA color.
- Pair yellow CTAs with dark Deep Ink pills for hierarchy.
- Keep buttons, inputs, nav links, tags, and icons pill-shaped.
- Use Hedvig Letters Serif for headings and Inter for everything functional.
- Keep cards lightweight with surface contrast rather than shadows.
- Use organic blobs only as decorative atmosphere behind product visuals.

## Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Deep Ink | `#130e30` | `--color-deep-ink` | Primary text, heading ink, borders, and secondary dark pill fill. |
| Hi-Yellow | `#ffe228` | `--color-hi-yellow` | Primary CTA fill, action highlight, and decorative yellow blob. |
| Moss Green | `#59e25d` | `--color-moss-green` | Decorative organic blob only. |
| Fuchsia | `#e261e5` | `--color-fuchsia` | Decorative organic blob only. |
| Slate | `#5f5c6e` | `--color-slate` | Muted helper text, secondary information, subtle icons. |
| Canvas | `#f9fbf2` | `--color-canvas` | Main page background and lightest surface. |
| Soft Meadow | `#eff2e5` | `--color-soft-meadow` | Card, nav, hero backdrop, and elevated surface. |
| Charcoal | `#222222` | `--color-charcoal` | Secondary dark text and dark button support. |
| Onyx | `#000000` | `--color-onyx` | Logo mark, input borders, and fine high-contrast details. |

## Typography

### Fonts

- Display/headings: Hedvig Letters Serif.
- Heading fallback: DM Serif Display, Source Serif 4, Libre Caslon Text, Georgia, serif.
- Body/UI: Inter.
- UI fallback: Inter, system-ui, sans-serif.

### Type Scale

| Role | Size | Weight | Line Height | Tracking | Use |
| --- | --- | --- | --- | --- | --- |
| caption | 10px | 500 | 1.2 | -0.2px | Small caps labels and case-study links. |
| body-sm | 14px | 400 or 500 | 1.5 | -0.14px | Author metadata, small UI copy. |
| body | 16px | 400 | 1.5 | -0.16px | Body copy, forms, standard UI. |
| subheading | 18px | 400 | 1.5 | -0.18px | Testimonial copy or small section support. |
| heading-sm | 22px | 400 or 700 | 1.25 | -0.22px | Card headings. |
| heading | 32px | 700 | 1.15 | -0.32px | Section headings. |
| heading-lg | 48px | 700 | 1.1 | -0.48px | Hero or large section heading. |
| display | 64px | 700 | 1 | -0.64px | Main hero headline. |

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | comfortable |
| Base unit | 8px |
| Max width | 1200px |
| Section gap | 48-80px |
| Card padding | 24-48px |
| Element gap | 12-16px |

### Spacing Scale

`8px`, `16px`, `24px`, `32px`, `48px`, `64px`, `96px`

### Radius

| Element | Value |
| --- | --- |
| nav | 1440px |
| tags | 1440px |
| icons | 1440px |
| buttons | 1440px |
| cards | 24px |
| images | 24-48px |

## Components

### Primary CTA Button Filled Yellow

Hi-Yellow fill, Deep Ink or Charcoal text, Inter 500 at 16px, full pill radius, 12px by 24px padding, no shadow. Use one yellow primary CTA per viewport.

### Secondary Button Dark Pill

Deep Ink fill, white text, Inter 500 at 16px, full pill radius, 12px by 22px padding. Use alongside yellow buttons for action hierarchy.

### Email Input Field

White fill, 1px Onyx border, Deep Ink text, Slate placeholder, Inter 16px, full pill radius, 12px by 22px padding. Pair directly with a pill CTA for a capsule form.

### Logo Lockup

Organic mark plus wordmark in Deep Ink. Use inside nav or footer, not as a standalone decorative motif.

### Nav Bar

Soft Meadow background, logo left, Inter 500 nav links centered, CTA pair on right, optional dropdown chevrons and language icon. No shadow.

### Hero Card Product Mockup Container

White product card on top of organic colored blobs. Product card has 24px radius. Blobs use Moss Green, Fuchsia, Hi-Yellow, and Deep Ink only as backdrop atmosphere.

### Feature Card

Soft Meadow surface, 24px radius, 24-48px padding, serif heading, Inter body copy, no border and no shadow.

### Customer Logo Card

Soft Meadow surface, 24px radius, centered monochrome logo, and a tiny case-study link underneath.

### Testimonial Card

Soft Meadow surface, 24px radius, 32px padding, quote text, author avatar/name/title block, carousel-friendly layout.

### Pagination Dot

Inactive marker in Slate. Active marker is a Hi-Yellow pill or elongated dot.

### Small Caps Label

Inter 500 at 10-12px, uppercase, tight tracking, in Slate or Deep Ink. Use sparingly as taxonomy.

### Hero Headline

Hedvig Letters Serif, weight 700, 48-64px, tight tracking, Deep Ink, left column of a two-column hero.

## Surfaces

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 0 | Canvas | `#f9fbf2` | Page background and outermost layer. |
| 1 | Soft Meadow | `#eff2e5` | Card surface, nav, hero backdrop, and elevated panels. |
| 2 | Hi-Yellow Accent | `#ffe228` | Primary action surface and highlight pill. |
| 3 | Deep Ink | `#130e30` | Dark contrast surface and secondary pill fill. |

## Imagery

Product UI screenshots are the main visual asset, usually in a white card floating over flat organic blobs. Section photography may appear as warm outdoor divider imagery, but the core identity is abstract organic shapes plus product UI. Customer logos should be monochrome. Avoid 3D renders and people illustrations.

## Layout

Use a 1200px centered container with generous side padding. Hero is two-column: text/form/trust badge on left, product mockup with organic blobs on right. Sections alternate Canvas and Soft Meadow bands, with 48-80px vertical gaps. Feature grids can use three equal columns. Testimonials use a horizontal carousel with multiple cards visible.

## Do

- Use pill radius on buttons, inputs, nav links, tags, and icon containers.
- Pair yellow primary CTA with a dark pill secondary action.
- Use Hedvig Letters Serif for headings at 22px and larger.
- Use Inter for body, nav, labels, forms, and cards.
- Use Deep Ink for primary text instead of pure black.
- Preserve the Canvas to Soft Meadow surface stack.
- Use organic blobs only behind hero/product visuals.
- Tighten heading letter spacing to about -0.01em and small caps to about -0.02em.

## Don't

- Do not use sharp corners on buttons, inputs, or nav items.
- Do not turn Moss Green or Fuchsia into UI colors.
- Do not use pure white as a card surface when Soft Meadow is intended.
- Do not place two yellow primary CTAs in the same viewport.
- Do not use Inter for display headlines or Hedvig for UI labels.
- Do not add drop shadows to cards or buttons.
- Do not use Slate for primary body text.

