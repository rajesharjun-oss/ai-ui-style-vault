# Metaview Style Reference

Metaview is a dark bioluminescent AI product system. The canvas is almost black with a green undertone, product cards sit one step above it, and a single electric mint signal marks the places where the interface is alive: primary action, active tabs, status, and selected states.

## Theme

Dark, AI product, recruiting, instrument panel, bioluminescent, precise, product-first.

## Color System

| Name | Value | Token | Role |
|---|---:|---|---|
| Deep Forest | `#000a06` | `--color-deep-forest` | Page background, hero canvas, sections, and footer. |
| Pine Bark | `#0a1a14` | `--color-pine-bark` | Cards, product mockup containers, nested panels, and dark secondary buttons. |
| Charcoal | `#161818` | `--color-charcoal` | Elevated card surface, modals, popovers, and overlaid containers. |
| Abyssal Indigo | `#01051b` | `--color-abyssal-indigo` | Borders, outlined action edges, linked labels, and lightweight interactive emphasis. |
| Paper White | `#ffffff` | `--color-paper-white` | Primary text, inverted button text, icons, and dark-theme reading copy. |
| Ash Gray | `#5e6262` | `--color-ash-gray` | Muted body text, helper copy, and secondary descriptions. |
| Smoke | `#828282` | `--color-smoke` | Tertiary text and subdued labels. |
| Silver | `#d9d9d9` | `--color-silver` | Light borders, dividers, and hairline rules on mid-tone surfaces. |
| Pure Black | `#000000` | `--color-pure-black` | Maximum contrast text, outline borders, and baseline dark value. |
| Electric Mint | `#7affb4` | `--color-electric-mint` | Primary CTA, selected navigation, active tabs, and live status indicators. |
| Mint Whisper | `#e3ffef` | `--color-mint-whisper` | Pale selected-tab backgrounds, decorative borders, and subtle highlight washes. |
| Bioluminescent Bloom | `radial-gradient(circle, rgba(0, 100, 70, 0.4) 0%, rgba(0, 60, 40, 0.2) 30%, rgba(0, 30, 20, 0.08) 55%, rgba(0, 0, 0, 0) 75%)` | `--gradient-bioluminescent-bloom` | Full-bleed product showcase atmosphere only. |
| Pine To Abyss | `linear-gradient(rgb(15, 58, 43) 0%, rgb(0, 10, 7) 100%)` | `--gradient-pine-to-abyss` | Footer and secondary atmospheric transitions. |

## Typography

### Euclid Circular A

Use as the sole UI typeface for headlines, navigation, body text, buttons, cards, and labels.

- Token: `--font-euclid-circular-a`
- Fallback: Inter, DM Sans, Space Grotesk
- Weights: 300, 400, 500, 700
- Sizes: 12px to 72px
- Signature: large text compresses with negative tracking; small text breathes with slight positive tracking.

### Onsite SemiMono

Use for numeric and technical micro-copy.

- Token: `--font-onsite-semimono`
- Fallback: JetBrains Mono, IBM Plex Mono, Geist Mono
- Weight: 400
- Sizes: 12px and 16px
- Letter spacing: 0.01em

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|---|---:|---:|---:|---|
| Caption | 12px | 1.48 | 0.12px | `--text-caption` |
| Body SM | 14px | 1.42 | 0.14px | `--text-body-sm` |
| Body | 16px | 1.50 | -0.16px | `--text-body` |
| Subheading | 20px | 1.34 | -0.40px | `--text-subheading` |
| Heading SM | 28px | 1.20 | -0.56px | `--text-heading-sm` |
| Heading | 36px | 1.16 | -1.08px | `--text-heading` |
| Heading LG | 48px | 1.10 | -1.92px | `--text-heading-lg` |
| Display | 68px | 1.04 | -4.08px | `--text-display` |

## Spacing And Shape

- Density: comfortable.
- Base unit: 8px.
- Max width: 1200px.
- Section gap: 80px.
- Card padding: 24px.
- Element gap: 8px.

### Spacing Scale

`8, 16, 24, 32, 40, 48, 56, 80, 112`

### Radius Scale

| Element | Radius |
|---|---:|
| Icons | 4px |
| Inputs | 8px |
| Nested elements | 8px |
| Cards | 16px |
| Badges | 100px |
| Buttons | 999px |

## Components

### Pill Primary Button

Electric Mint fill, Deep Forest text, 999px radius, 8px vertical by 16px horizontal padding, Euclid 14px/500. This is the only filled chromatic button and the main use of vivid mint.

### Outlined Ghost Button

Transparent fill, 1px Paper White border, Paper White text, 999px radius, 8px by 16px padding, Euclid 14px/500. Pair with the mint primary CTA.

### Dark Secondary Button

Pine Bark fill, 1px Abyssal Indigo border, Paper White text, 16px radius, 8px by 16px padding. Use for in-card actions where a full pill would feel too loud.

### Top Navigation Bar

Deep Forest background, full width, about 80px tall. Use wordmark left, nav links center, and sign-in plus ghost and mint CTAs right. No drop shadow.

### Announcement Banner

Full-width strip above nav, Deep Forest background, centered 14px Paper White text, 8px vertical padding, no border.

### Hero Section

Deep Forest canvas, centered 1200px content, display headline at 68px/300 with -4.08px tracking, Ash Gray support text, and two-button row: mint primary plus ghost secondary with 8px gap.

### Product Showcase Card

Place on Bioluminescent Bloom radial gradient. Card uses Pine Bark, 1px Abyssal Indigo border, 16px radius, 24px padding, no heavy shadow. Inside, use a narrow 60px feature rail and a wide chat/product panel.

### Side Icon Nav Rail

Vertical stack of feature tabs. Active tab uses Mint Whisper background and Paper White text; inactive tabs use Ash Gray text. 4px radius for active item.

### Chat Interface Panel

Pine Bark background, subtle inner border, 8px-radius input, 16px padding, circular submit button using Abyssal Indigo background and Paper White icon. Use Onsite SemiMono for candidate counts and numeric data.

### Tab Pill Group

Horizontal pill tabs with 100px radius. Active tab uses Mint Whisper background and Deep Forest text. Inactive tabs are transparent with Paper White at reduced opacity.

### Filter Bar

Segmented chips at 28px height, 12px/500 labels, 1px Abyssal Indigo border, 4px radius. Counts should be Onsite SemiMono.

### Feature Card

Pine Bark background, 1px Abyssal Indigo border, 16px radius, 24px padding. Icon at 24px in Electric Mint or Paper White. Heading 20px/500, body 16px/400 in Ash Gray.

## Layout

Use max-width 1200px centered content with full-bleed atmospheric sections. Rhythm: announcement bar, nav, centered dark hero, product showcase on green bloom backdrop, then alternating product-first content sections. Sections use 80px vertical gaps and no visible dividers.

## Imagery

Use actual product screenshots or realistic product mockups as the main visuals. The decorative motif is the green radial bloom behind product sections. Avoid lifestyle photos, stock illustration, and 3D renders.

## Do

- Use Electric Mint only for primary CTA, active tab, and live status indicators.
- Set all display headlines at weight 300 with tight negative tracking.
- Use 999px radius for buttons and tab pills.
- Use 16px radius for cards and 8px for inputs.
- Use Bioluminescent Bloom only behind product mockup sections.
- Render counts, metrics, IDs, and technical labels in Onsite SemiMono.
- Pair each mint CTA with a ghost secondary button.

## Don't

- Do not use 600 or 700 for display headlines.
- Do not apply Electric Mint to large surfaces or body text.
- Do not use drop shadows for card elevation.
- Do not introduce new accent colors or gradients.
- Do not use Ash Gray for headings above 16px.
- Do not use non-pill buttons for main actions.
- Do not use light card surfaces on the dark canvas.
