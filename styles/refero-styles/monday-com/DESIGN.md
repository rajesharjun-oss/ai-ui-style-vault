# monday.com - Style Reference

## North Star

Build the UI like a bright productivity workshop: clean white surfaces, generous air, friendly rounded forms, one violet action color, and soft pastel cards that feel like organized sticky notes. Let real product mockups carry the proof.

## Theme

Light. The main page alternates between Snow and Cloud surfaces, with white cards and violet brand panels. The palette should feel playful but controlled: violet owns action, pastels own surfaces, and text stays warm near-black.

## Color Tokens

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Monday Violet | `#6161ff` | `--color-monday-violet` | Primary CTAs, brand panels, active states, gradient stops |
| Prism | `conic-gradient(from 270deg, rgb(129, 129, 255) 15%, rgb(51, 219, 219) 40%, rgb(51, 213, 142) 55%, rgb(255, 214, 51) 65%, rgb(252, 82, 125) 85%, rgb(129, 129, 255) 100%)` | `--color-prism` | Logo mark, dividers, loading states, small decorative accents |
| Mint | `#bcfe90` | `--color-mint` | Green wash for feature card surfaces and emphasis blocks |
| Sky | `#abf0ff` | `--color-sky` | Blue wash for highlight cards and decorative bands |
| Apricot | `linear-gradient(90deg, rgb(254, 129, 228), rgb(254, 129, 228) 31%, rgb(253, 169, 0) 88%)` | `--color-apricot` | Warm hero text gradient and soft accent wash |
| Lavender | `#eddff7` | `--color-lavender` | Decorative card background and category surface |
| Periwinkle | `#e7ecff` | `--color-periwinkle` | Light brand-tinted surface |
| Cornflower | `#93beff` | `--color-cornflower` | Secondary brand surface |
| Aqua | `#d1faff` | `--color-aqua` | Cyan card background and AI feature accent surface |
| Cotton Candy | `#e98dfe` | `--color-cotton-candy` | Playful card border accent and highlight stroke |
| Ultra Violet | `#9450fd` | `--color-ultra-violet` | Deep brand accent and saturated button alternative for product UI |
| Electric Cyan | `#3ac9ff` | `--color-electric-cyan` | AI or feature highlight |
| Forest | `#2a5c4e` | `--color-forest` | Teal action color for selected product UI moments |
| Peony | `#fcd0f8` | `--color-peony` | Soft pink fill and saturated product UI alternative |
| Periwinkle Wash | `#dbdbff` | `--color-periwinkle-wash` | Badge and tag background |
| Ink | `#333333` | `--color-ink` | Primary body text, headings, button labels |
| Slate | `#535768` | `--color-slate` | Secondary text, nav links, icon fills, footer copy |
| Iron | `#808080` | `--color-iron` | Muted helper text, disabled icons, tertiary borders |
| Fog | `#cacbcd` | `--color-fog` | Card borders and subtle dividers |
| Mist | `#d0d4e4` | `--color-mist` | Light card borders and elevated surfaces |
| Pebble | `#dddfeb` | `--color-pebble` | Badge borders, pill outlines, input borders |
| Shadow Dust | `#e6e7ea` | `--color-shadow-dust` | Soft lavender-tinted shadow support |
| Cloud | `#f5f6f8` | `--color-cloud` | Page canvas, section backgrounds, neutral button fills |
| Snow | `#ffffff` | `--color-snow` | Card surfaces, nav background, input fields, button text |

## Typography

Use Poppins as the single family. Fallback to Manrope, DM Sans, or Plus Jakarta Sans.

| Role | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- |
| Micro | 8px | 500 | 1.5 | 0.2em for uppercase labels |
| Caption | 12px | 400 | 1.45 | -0.12px |
| Body Small | 14px | 400 | 1.5 | 0 |
| Body | 16px | 400 | 1.5 | -0.16px |
| Body Large | 18px | 400 | 1.5 | -0.18px |
| Subheading | 20px | 400 | 1.4 | -0.22px |
| Heading Small | 24px | 400 | 1.3 | -0.36px |
| Heading | 36px | 400 | 1.2 | -0.54px |
| Heading Large | 48px | 300 | 1.15 | -0.96px |
| Display | 64px | 300 | 1.15 | -2.56px |

Rules:

- Use weight 300 for large display headlines.
- Use weight 400 for body and standard headings.
- Use weight 500 to 700 for nav labels, buttons, badges, and product UI labels.
- Tighten display type more as it gets larger.
- Use positive tracking only for tiny uppercase labels.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | Comfortable |
| Base unit | 8px |
| Max width | 1200px |
| Section gap | 64px |
| Card padding | 24px |
| Element gap | 8px |

Spacing scale: 8, 16, 24, 32, 40, 48, 64, 80, 96.

Radius scale:

- Nav, badges, inputs: 6px.
- Images: 12px.
- Cards: 24px.
- Buttons and CTAs: 160px.
- Avatars: fully circular.

Elevation:

- Board mockup: `rgba(205, 208, 223, 0.4) 0px 2px 48px 0px`.
- Featured card: `rgba(0, 0, 0, 0.15) 0px 5px 45px 0px`.
- Active AI card: `rgba(0, 0, 0, 0.15) 0px 4px 40px 0px`.
- Inset emphasis: `rgb(0, 0, 0) 0px -2px 0px 0px inset`.

## Components

### Primary Pill Button

Use Monday Violet fill, Snow text, Poppins 16px at 500 weight, 160px radius, 13px vertical padding, 24px horizontal padding, and an inline arrow icon when appropriate.

### Outlined Pill Button

Use transparent fill, 1px Slate border, Ink text, 160px radius, 13px vertical padding, 20px horizontal padding. Pair with the primary CTA for lower-commitment paths.

### Text Link Button

Use no fill, no border, Slate text, 500 weight, and compact 8px to 10px horizontal padding. Often paired with a dropdown chevron in navigation.

### Pastel Feature Card

Use Mint, Sky, Apricot, Lavender, Periwinkle, or Aqua as a soft surface. Apply 24px radius, 24px padding, a small monochrome icon, and a Poppins 16px 500-weight label. Works well as the standard feature or exploration tile.

### Board Mockup Card

Use Snow surface, 1px Mist border, 16px to 24px radius, and soft lavender-tinted shadow. Include board rows, colored status pills, avatar stacks, and product-like controls.

### AI Prompt Card

Use Snow surface, 6px radius, 12px to 16px padding, a brand-colored icon on the left, Slate placeholder copy, and mic/send icons on the right. Hover or active states may use the active AI card shadow.

### Brand Gradient Panel

Use Monday Violet as a full-height brand panel, often in a 50/50 split. Place a white product mockup card above it with 24px radius.

### Status Pill

Use 6px radius, tinted status background, Poppins 12px to 13px 500-weight label, and compact 2px vertical by 8px horizontal padding.

### Avatar Stack

Use circular avatars at 24px to 32px diameter, 2px Snow border, and slight negative margin.

### Logo Strip

Use a centered social-proof row with monochrome black wordmarks at roughly 60 percent opacity, generous horizontal spacing, and no cards or dividers.

### Exploration Grid Card

Use Snow surface, 1px Mist border, 6px radius, small square icon, and a two-line Poppins label in a 3-column grid.

### Navigation Bar

Use sticky Snow background, monday.com wordmark on the left, links in the center, and dual CTAs on the right. Nav items use compact 8px vertical and 16px horizontal padding.

## Layout And Imagery

- Center content in a 1200px max-width container.
- Let product board mockups break out of the container or peek above section edges.
- Use a centered single-column hero with a large display headline, gradient text accent, and one primary CTA.
- Follow with logo strip, then alternating 2-column text-plus-product sections.
- Use a 50/50 AI feature split with a violet panel and product card.
- Use Cloud bands to break up white sections.
- Show product UI, not lifestyle photography.

## Do

- Use 160px radius for all buttons and CTAs.
- Reserve Monday Violet for primary actions and brand panels.
- Apply pastel accent backgrounds to feature cards, not body text or icons.
- Set display headlines at 48px to 64px with weight 300 and negative tracking.
- Use 24px radius for cards and 6px for badges and inputs.
- Use the prism gradient only for logo marks, dividers, and loading states.
- Use pink-to-orange or cyan-to-violet gradient text only in hero headlines.

## Do Not

- Do not use square or tiny-radius buttons.
- Do not apply pastel accent colors to body text, borders, or icons.
- Do not use weight 300 for body text or UI labels.
- Do not use pure black for large text blocks; use Ink.
- Do not stack more than three or four pastel colors in adjacent cards.
- Do not use heavy drop shadows.
- Do not introduce new chromatic CTA colors.
