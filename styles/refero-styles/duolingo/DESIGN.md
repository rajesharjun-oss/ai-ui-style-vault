# Duolingo - Style Reference

> Playful classroom mascot on white paper

**Theme:** light

Duolingo reads like a playful learning storybook: white paper canvas, chubby rounded display type, saturated green progress signals, blue interactive text, chunky 12px radii, and thick sticker-like borders. Body copy stays calm in mid-gray so green headings, green actions, and blue secondary controls can carry the emotional weight.

The UI should feel friendly and learnable, not corporate. Components are simple, rounded, and tactile. Illustrations carry the broader secondary palette while the UI chrome itself stays disciplined: green for progress and large display moments, blue for links and secondary CTAs, gray for body and borders, white for the page.

## Tokens - Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Eager Green | `#58cc02` | `--color-eager-green` | Green accent for progress, display headings, primary CTA fills, and footer band. |
| Storybook Green | `#d7ffb8` | `--color-storybook-green` | Soft green wash for highlighted footer labels and light surface tints. |
| Spark Blue | `#1cb0f6` | `--color-spark-blue` | Interactive links and outlined secondary CTAs. |
| Fresh Leaf | `#a5ed6e` | `--color-fresh-leaf` | Secondary green link tone inside footer or green-band contexts. |
| Night Ink | `#000437` | `--color-night-ink` | Deep violet-blue accent for emphasis text and dark surfaces. |
| Paper White | `#ffffff` | `--color-paper-white` | Page canvas, card surfaces, and text on green or dark fills. |
| Charcoal | `#4b4b4b` | `--color-charcoal` | Hero headings and primary dark copy. |
| Pencil Gray | `#777777` | `--color-pencil-gray` | Body paragraphs and secondary descriptive text. |
| Faded Gray | `#afafaf` | `--color-faded-gray` | Button borders, disabled states, and low-emphasis nav labels. |

## Tokens - Typography

### Feather

- **Token:** `--font-feather`
- **Substitute:** Feather Bold, Nunito Black, rounded extra-bold sans
- **Weights:** 700
- **Sizes:** 48px, 64px
- **Line height:** 1.20
- **Letter spacing:** -0.0200em
- **Role:** Rounded display face for section titles and high-emotion marketing headings. Do not use below 48px.

### Duolingo Sans

- **Token:** `--font-duolingo-sans`
- **Substitute:** DIN Next, Inter, Nunito Sans, ui-sans-serif
- **Weights:** 500, 700
- **Sizes:** 13px, 14px, 15px, 17px, 19px, 32px
- **Line heights:** 1.15, 1.18, 1.20, 1.21, 1.23, 1.33, 1.40, 1.41, 1.47
- **Role:** Body, nav, labels, subheadings, links, and smaller emphasis text.

### Type Scale

| Role | Size | Line Height | Weight | Letter Spacing | Token |
|------|------|-------------|--------|----------------|-------|
| caption | 13px | 1.23 | 700 | 0 | `--text-caption` |
| nav-label | 15px | 1.33 | 700 | 0.795px | `--text-nav-label` |
| body | 17px | 1.18 | 500 | 0 | `--text-body` |
| subheading | 19px | 1.4 | 700 | 0 | `--text-subheading` |
| heading-sm | 32px | 1.2 | 700 | 0 | `--text-heading-sm` |
| heading | 48px | 1.2 | 700 | -0.96px | `--text-heading` |
| display | 64px | 1.2 | 700 | -1.28px | `--text-display` |

## Tokens - Spacing And Shapes

**Base unit:** 4px

**Density:** comfortable

| Purpose | Value |
|---------|-------|
| Max width | 1200px |
| Section gap | 80-120px |
| Card padding | 16-24px |
| Element gap | 12px |
| Section height | 800-900px |
| Body max width | 480px |
| Footer vertical padding | 48px |

### Spacing Scale

| Name | Value | Token |
|------|-------|-------|
| 8 | 8px | `--spacing-8` |
| 12 | 12px | `--spacing-12` |
| 16 | 16px | `--spacing-16` |
| 24 | 24px | `--spacing-24` |
| 32 | 32px | `--spacing-32` |
| 40 | 40px | `--spacing-40` |
| 48 | 48px | `--spacing-48` |
| 64 | 64px | `--spacing-64` |
| 80 | 80px | `--spacing-80` |
| 96 | 96px | `--spacing-96` |
| 120 | 120px | `--spacing-120` |

### Radius

| Element | Value | Token |
|---------|-------|-------|
| links | 12px | `--radius-links` |
| buttons | 12px | `--radius-buttons` |
| nav-items | 12px | `--radius-nav-items` |
| pills | 12px | `--radius-pills` |

## Components

### Primary CTA Button

Use Eager Green fill, Paper White text, duolingo-sans style type at 15px/700, uppercase, 0.0530em tracking, 12px radius, and 16px horizontal padding. No border required when the fill is green on white.

### Outlined Account Button

Transparent fill, Spark Blue text, duolingo-sans style type at 14px/700, 12px radius, 16px horizontal padding, and 2px solid Faded Gray border. Use as a calm secondary action under or near the green primary.

### Nav Language Pill

Transparent fill, Pencil Gray uppercase text at 15px/700, 0.0530em tracking, 12px radius, 10px vertical padding, 16px horizontal padding, and 2px solid Faded Gray border.

### Section Headline

Feather-style display at 48-64px, weight 700, line-height 1.2, letter-spacing -0.0200em, and Eager Green color. Use for section titles such as value propositions and learning claims.

### Hero Headline

Duolingo-sans style type at 32px/700 in Charcoal. Keep it neutral so the CTA below carries the green.

### Body Paragraph

Duolingo-sans style type at 17px/500, line-height 1.18, Pencil Gray, max width around 480px.

### Footer Background

Full-width Eager Green band with generous 48px vertical padding. Use Paper White and Storybook Green labels. This is the strongest colored surface on the page.

### Footer Link Item

Small duolingo-sans style text. Use Fresh Leaf for links on green, and Paper White for section headers.

### Language Flag Pill

Inline language selector with circular flag or icon plus uppercase language name, 15px/700 type, 10-12px gaps, and no background fill.

### App Store Badge

Dark rectangular badge with white icon/text and Charcoal support text. Keep it as a visual anchor on white sections.

### Section Feature Illustration

Large flat mascot or character-style illustration beside text, no containing card, no background panel, and no UI chrome color leakage.

## Do's And Don'ts

### Do

- Use Eager Green for progress, section headings, CTA fills, and the footer band.
- Use Spark Blue for interactive links and outlined secondary CTAs.
- Set display headlines at 48-64px in Feather-style rounded weight 700.
- Keep body text Pencil Gray at 17px/500.
- Use 12px radius on every button, pill, tag, and nav item.
- Pair outlined controls with 2px borders.
- Reserve uppercase 15px with 0.0530em tracking for nav and language labels.
- Build sections as white-on-white with a text block and one large illustration.

### Don't

- Do not put colored text inside body paragraphs.
- Do not use sharp corners.
- Do not introduce gradients, shadows, or glass effects.
- Do not use Feather-style display below 48px.
- Do not apply mascot secondary colors to UI chrome.
- Do not use green for small body text or dense link text.
- Do not place green and blue actions on green backgrounds without contrast checks.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Paper White | `#ffffff` | Page canvas and default section surface. |
| 1 | Storybook Green | `#d7ffb8` | Soft highlighted tint. |
| 2 | Eager Green | `#58cc02` | Footer band and primary CTA fill. |
| 3 | Night Ink | `#000437` | Deep accent surface for dark emphasis. |

## Imagery

Use illustration-driven storybook language: flat 2D mascot or character-style figures, rounded geometric shapes, bold outlines, and a broader secondary palette that remains inside the art. Photography should be absent. Illustrations sit beside text on pure white with no containers.

## Layout

Use single-column full-width sections stacked vertically. Center content in a 1200px max-width track. Most sections pair text on the left with one large illustration on the right. Keep vertical spacing generous at 80-120px between sections, with section heights around 800-900px when the page is marketing-oriented. The footer is a full-bleed green band.

## Agent Prompt Guide

### Quick Color Reference

- Heading text: `#58cc02`
- Body text: `#777777`
- Hero dark text: `#4b4b4b`
- Page background: `#ffffff`
- Footer background: `#58cc02`
- Outlined control border: `#afafaf`
- Interactive link: `#1cb0f6`

### Example Component Prompts

1. Primary CTA: Eager Green fill, white uppercase 15px/700 text, 12px radius, 16px horizontal padding, no shadow, no gradient.
2. Outlined secondary button: transparent fill, Spark Blue text, 2px Faded Gray border, 12px radius, 14px/700 type.
3. Section headline: Feather-style 48px rounded display, weight 700, line-height 1.2, -0.0200em tracking, Eager Green.
4. Marketing section: left text block max 480px, green headline, gray paragraph, CTA stack, large flat character illustration on the right.
5. Footer: full-bleed Eager Green band with white headers, Fresh Leaf links, and spacious link groups.

## Similar Reference Families

- Headspace style mascot-led illustration systems.
- Babbel style light-mode language learning pages.
- Khan Academy Kids style rounded educational UI.
- Memrise style white canvas and green learning accent.
- ClassDojo style playful classroom interaction patterns.

