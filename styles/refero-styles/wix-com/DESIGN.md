# wix.com Style Reference

> Daylight gallery wall with electric blue signposts: airy white canvas, oversized Madefor headlines, rounded product cards, and a single blue action color.

## Theme

Light.

wix.com uses a spacious, bright, creator-friendly system. The interface is mostly achromatic: white surfaces, black type, gray hairlines, and lightweight rounded cards. Electric Blue is reserved for primary actions. Color washes such as lime, lavender, lemon, and violet punctuate sections and marketing moments, but do not become a full color-coded UI system.

## Core Principles

1. Let white space and large type create confidence.
2. Use Electric Blue only for primary action buttons.
3. Use black filled pills as the alternate action style.
4. Keep color washes decorative and section-scoped.
5. Use Madefor Display for large editorial headlines.
6. Use Madefor Text for body, navigation, inputs, and descriptions.
7. Use 50px pill radius for interactive controls.
8. Use product mockups, browser frames, and template previews as the main visuals.

## Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Pure Canvas | `#ffffff` | `--color-pure-canvas` | Page canvas, form states, quiet UI feedback |
| Slate Mist | `#f1f5f9` | `--color-slate-mist` | Elevated surfaces, inputs, subtle panels |
| Carbon Ink | `#000000` | `--color-carbon-ink` | Primary text, icon strokes, borders, black buttons |
| Graphite | `#1c1d21` | `--color-graphite` | Slightly softened display headline text |
| Ash Border | `#d0d0d0` | `--color-ash-border` | Hairline dividers and card borders |
| Fog Border | `#e8e6e6` | `--color-fog-border` | Subtle borders on quieter elements |
| Electric Blue | `#166aea` | `--color-electric-blue` | Primary action button fill and selected nav indicator |
| Deep Violet | `#101585` | `--color-deep-violet` | Brand heading, link underline, decorative accent |
| Indigo Pulse | `#2c34af` | `--color-indigo-pulse` | Gradient endpoint and section heading accent |
| Lime Highlight | `#dff994` | `--color-lime-highlight` | Surface wash and decorative highlight zones |
| Lemon Note | `#fdf4a1` | `--color-lemon-note` | Soft text highlight and callout marker |
| Lavender Mist | `#bfc8e8` | `--color-lavender-mist` | Section gradient start and atmospheric wash |
| Input Blue | `#538ab6` | `--color-input-blue` | Input focus and active border |

## Typography

Use Wix Madefor when available. Use Inter, DM Sans, Space Grotesk, IBM Plex Sans, or Noto Sans as practical fallbacks depending on role.

| Role | Family | Fallback | Use |
| --- | --- | --- | --- |
| Display | madefor-display | Inter, DM Sans, Space Grotesk | Headlines from 21px to 184px |
| Body | madefor-text | Inter, IBM Plex Sans, Noto Sans | Body, nav, descriptions, inputs |
| Utility | Arial | system-ui, Arial | Micro labels and icon text at 10px to 13px |

## Type Scale

| Role | Size | Weight | Line Height | Letter Spacing |
| --- | --- | --- | --- | --- |
| Caption | 13px | 400 | 1.2 | -0.13px |
| Body | 16px | 400 | 1.5 | -0.16px |
| Subheading | 21px | 400 | 1.3 | -0.21px |
| Heading small | 31px | 400 | 1.2 | -0.62px |
| Heading | 48px | 400 | 1.1 | -0.96px |
| Heading large | 82px | 400 | 1.0 | -2.46px |
| Display | 104px | 400 | 0.95 | -3.12px |
| Hero super display | 184px | 400 | 0.85 to 1.3 | -0.03em |

Large display type should use tight leading and increasingly negative tracking. Do not let headline line-height drift above 1.2 at 48px and above.

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | comfortable |
| Base unit | 4px |
| Max width | 1200px |
| Section gap | 80px |
| Card padding | 24px |
| Element gap | 12px |
| Image radius | 8.9px |
| Small card radius | 8.9px |
| Tag radius | 20px |
| Card radius | 20px |
| Alternate button radius | 20px |
| Button radius | 50px |
| Nav pill radius | 50px |

The page should feel rounded and friendly, but not gooey. Use 50px pills for main interactive controls, 20px for cards, and 8.9px for product mockups.

## Layout

Use a 1200px centered content rail with full-bleed gradient or color-wash sections. Hero sections can be centered or left-aligned, with a large Madefor Display headline, subtitle, CTA, and product mockup. Sections alternate between white canvas and color-wash backgrounds.

Recommended flow:

1. Horizontal nav with logo, links, login, and blue Get Started pill.
2. Hero headline at 82px to 104px with subtitle and CTA.
3. Product mockup or browser editor screenshot.
4. Lavender gradient section.
5. Two-column feature section with headline and supporting text.
6. Template preview gallery in a 4-column grid.
7. Lime or lemon callout wash.
8. Footer with simple link groups.

## Components

### Primary Action Button

Electric Blue fill, white text, 50px radius, Madefor Text 16px, compact horizontal padding. Use one per section maximum.

### Secondary Action Button

Carbon Ink fill, white text, 50px radius, Madefor Text 16px. Use beside or instead of the blue primary action, especially on bright sections.

### Ghost Button

Transparent background, 1px contextual border, Madefor Text 15px to 16px, 50px radius. Use for tertiary actions or over strong color-wash sections.

### Rounded Button

20px radius variant for compact card actions. Use the same blue, black, or ghost color system.

### Template Preview Card

20px card radius, 8.9px inner image radius, no visible border, minimal or no shadow. Image dominates the card with a small label below. Works well in 4-column desktop grids.

### Product Mockup Card

8.9px radius product UI screenshot, subtle border or no border. Often includes browser chrome, editor panels, URL bars, or AI prompt UI.

### Navigation Bar

Transparent or white background. Wix logo left, nav links centered, utilities right. Get Started is a blue 50px pill. Login is a ghost text link. Dropdown indicators should stay simple.

### Input Field

Pure Canvas or Slate Mist background, 1px border, focus border in Input Blue, Madefor Text 15px to 16px, 8px to 12px radius. Placeholder in a light gray.

### Hero Headline Block

Madefor Display at 82px to 104px, line-height 0.95 to 1.0, tight negative tracking. Subtitle in Madefor Text 18px to 21px. CTA sits 24px to 32px below.

### Section Heading

Madefor Display 48px, line-height 1.1, -0.96px tracking. Pair with supporting copy to the right or below.

### Gradient Section Background

Full-bleed Lavender Mist to white gradient. Use for atmospheric rhythm between white sections, not as a busy background.

### Badge Or Tag

20px radius pill or small tag with Madefor Text 13px to 14px. Usually ghost or lightly filled. Use for template categories and metadata.

### Side Panel

White 20px-radius panel with subtle border or soft shadow. Use for contextual tools such as an AI assistant or editor sidebar. Fixed or collapsible on wide screens.

## Surfaces

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 0 | Canvas | `#ffffff` | Primary page and section background |
| 1 | Mist | `#f1f5f9` | Panels, input fields, subtle section differentiation |
| 2 | Lime Wash | `#dff994` | Accent section or callout surface |
| 3 | Lavender Fade | `#bfc8e8` | Gradient section atmosphere |

## Elevation

Keep elevation minimal. Avoid visible card and button shadows. Use hairline borders, flat surfaces, rounded shapes, and layout spacing. The navigation bar can use a very subtle structural line only.

## Imagery

Use product screenshots, Wix editor mockups, AI prompt interfaces, browser-framed templates, and template photography such as commerce, portfolio, interiors, fashion, and architecture. Gradients should stay smooth and atmospheric.

## Do

- Use Madefor Display at 48px to 104px for headlines.
- Reserve Electric Blue for primary action buttons.
- Use 50px radius for buttons and nav pills.
- Use 80px section gaps.
- Use Lavender Mist to white gradients for full-bleed section breaks.
- Use 8.9px radius on product mockups and images.
- Pair blue filled buttons with black filled buttons as the two-tier action system.

## Don't

- Do not use Deep Violet or Indigo Pulse for action buttons.
- Do not add visible drop shadows to cards or buttons.
- Do not use sharp corners below 8px on cards or below 20px on buttons.
- Do not set headline line-height above 1.2 at 48px and above.
- Do not apply Lime Highlight or Lemon Note to long text blocks.
- Do not add new accent colors.
- Do not center long body paragraphs.

## AI Builder Notes

If the page feels generic, increase display scale and whitespace before adding decoration. The Wix feeling comes from airy confidence: big display type, pill actions, soft section color, and product/editor imagery.
