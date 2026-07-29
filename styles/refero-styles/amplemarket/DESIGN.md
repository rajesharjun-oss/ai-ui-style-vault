# Amplemarket - Style Reference

Amplemarket feels like a bright sales workspace made softer: white and cream surfaces, dense ink typography, flat pastel product taxonomy cards, a vivid orange brand accent, and dark bands used only when the page needs contrast.

**Theme:** light

## Summary

Build this style with a clean product-marketing rhythm. The default page should feel airy and white, with Cream Wash used for quiet section breaks. Use Labil Grotesk Variable everywhere. Large headings are restrained at weight 400 until the rare poster moment, where weight 900 uppercase display type becomes the signature.

## Tokens - Colors

| Name | Value | Token | Role |
|---|---:|---|---|
| Phoenix Orange | `#e8400d` | `--color-phoenix-orange` | Brand accent, hero gradient origin, marketing highlights |
| Midnight Indigo | `#10054d` | `--color-midnight-indigo` | Deep brand surface, feature cards, dark contrast |
| Charcoal | `#272625` | `--color-charcoal` | Secondary dark surface, testimonial cards, footer panels |
| Ink | `#111111` | `--color-ink` | Primary text, heading color, filled action button background |
| Canvas White | `#ffffff` | `--color-canvas-white` | Main page background, cards, text on dark surfaces |
| Cream Wash | `#f6f5f3` | `--color-cream-wash` | Soft section fill and secondary card background |
| Ash | `#6d6c6b` | `--color-ash` | Muted body text, labels, helper copy |
| Stone | `#b1b1af` | `--color-stone` | Hairline borders, subtle dividers, placeholders |
| Pearl | `#ecebea` | `--color-pearl` | Subtle button fills and hover states |
| Petal Pink | `#ffd7f0` | `--color-petal-pink` | Flat category tile color |
| Mint Green | `#b7efb2` | `--color-mint-green` | Flat category tile color |
| Canary Yellow | `#ffef99` | `--color-canary-yellow` | Flat category tile color |
| Soft Violet | `#e2ddfd` | `--color-soft-violet` | Flat category tile color |
| Aqua | `#99fff9` | `--color-aqua` | Hero highlight wash and gradient endpoint |
| Indigo Deep | `#2e2460` | `--color-indigo-deep` | Dark form/input surface inside indigo sections |

## Typography

Use `Labil Grotesk Variable` as the whole system. The personality comes from using the same geometric grotesque for nav, body, cards, and display, then changing weight, size, and tracking rather than switching typefaces.

| Role | Size | Weight | Line Height | Tracking | Notes |
|---|---:|---:|---:|---:|---|
| Eyebrow | 10px | 500 | 1.0 | 0.3px | Small labels and metadata |
| Caption | 12px | 400 | 1.0 | 0 | Tight captions |
| Body small | 14px | 400 | 1.3 | 0 | Body support and helper text |
| Body | 16px | 400 | 1.0 | 0 | Main UI/body baseline |
| Body large | 20px | 400 | 1.3 | -0.4px | Intro and large body copy |
| Subheading | 28px | 400 | 1.1 | -0.476px | Feature titles |
| Heading small | 36px | 400 | 1.1 | -1.08px | Compact section titles |
| Heading | 44px | 400 | 1.1 | -1.76px | Default section heading |
| Heading large | 56px | 400 | 1.0 | -2.8px | Large calm headings |
| Display | 84px | 900 | 0.8 | -2.52px | Poster headline, uppercase only |

## Spacing And Shape

- Page max width: 1200px
- Section gap: 80-120px
- Card padding: 20px
- Element gap: 8-12px
- Button radius: 8px
- Card radius: 12px
- Input radius: 12px
- Badge radius: 9999px
- Small radius: 4px

## Components

**Primary Filled Button**

Ink background, Canvas White text, no border, 8px radius, 12px 16px padding. Use 16px Labil Grotesk weight 400. This is the dominant action pattern.

**Ghost Navigation Button**

Transparent background, 8px radius, 12px 16px padding. On dark sections use softened white text; on light sections use Ink.

**Neutral Filled Button**

Pearl background, Ink text, no border, 8px radius, 12px 16px padding. Use when a secondary action needs more weight than a ghost link.

**White Pill Badge**

White badge with Ink text, 12px radius, compact padding, and optional icon. Use for logo lockups and small brand marks.

**Email Capture Input**

White input, 1px rgba(17,17,17,0.08) border, 12px radius, 48px height, 16px horizontal padding. It often joins inline with a filled Ink button.

**Pastel Category Card**

Flat fill from Petal Pink, Mint Green, Canary Yellow, or Soft Violet. Use 12px radius and 16px 20px padding. Do not add shadows or borders; the color is the taxonomy.

**Dark Testimonial Card**

Charcoal background, 12px radius, compact padding, white quote text, Ash metadata, and a small avatar. Keep the card quiet and inset-like.

**Light Feature Card**

White background, 12px radius, 16px 20px padding. Use minimal hairline borders or a very soft ambient shadow only when separation is necessary.

**Logo Grid Card**

Transparent or white card in a clean grid. Center the logo, then place an Ash caption beneath it.

**Sticky Navigation Bar**

About 62px tall. Logo at left, centered nav links, and a right-side action cluster. It can shift from transparent to white with backdrop blur while scrolling.

**Hero Video Container**

Black or very dark frame, 12px radius, near full container width, 16:9 aspect ratio, and centered play control.

**Dark Section Panel**

Full-bleed Charcoal or Midnight Indigo with 80-120px vertical padding. Use white text and Ash secondary copy for testimonials and footer moments.

## Layout And Imagery

- Start with a centered hero: headline, support copy, email capture, and soft radial gradient behind it.
- Use white and Cream Wash as the dominant section surfaces.
- Introduce dark bands for testimonials, footer, or strong product proof.
- Use 3-4 column grids for pastel feature/category cards.
- Use monochrome logo grids on white.
- Use hand-drawn line illustration, rocket/spaceship motifs, gradient washes, and dark-framed product video/screenshots.

## Implementation Rules

Use color as structure, not decoration. Pastel cards should communicate categories. Orange should remain a brand and hero accent. Let shape stay disciplined: 8px buttons, 12px cards, 12px inputs.
