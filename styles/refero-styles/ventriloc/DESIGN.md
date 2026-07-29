# Ventriloc - Style Reference

> Editorial data observatory on warm paper, with one orange ember punctuating monochrome precision.

**Theme:** light

Ventriloc speaks in a quiet data-editorial voice: warm paper canvas, flat data cards, careful typography, and a single orange accent used like a highlighter on a printed report. The system pairs PolySans-style headings at weight 400 with Inter body and UI text. It avoids loud SaaS gradients and standard card shadows in favor of surface bands, whitespace, and tight typographic control.

The signature geometry is split into three dialects: square buttons, asymmetric featured cards, and fully rounded pill navigation. Color is rationed. Pages should feel about 95 percent achromatic, with Ember Orange used only for link underlines, chart highlights, tags, and tiny icon accents.

## Tokens - Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Graphite | `#202020` | `--color-graphite` | Primary text, headings, nav links, icon strokes, and button fills. |
| Canvas White | `#ffffff` | `--color-canvas-white` | Page background, bright cards, and icon fills. |
| Ash | `#efefef` | `--color-ash` | Primary card and section background, plus nav pill containers. |
| Fog | `#f5f5f5` | `--color-fog` | Nested surfaces and secondary containers. |
| Ivory | `#ebe6dd` | `--color-ivory` | Warm accent background wash for featured editorial blocks. |
| Steel | `#4d4d4d` | `--color-steel` | Secondary body text and long-form paragraphs. |
| Slate | `#828282` | `--color-slate` | Helper text, tertiary nav, inactive controls, and footer utility text. |
| Mist | `#e8e8e8` | `--color-mist` | Hairline dividers and subtle nav fills. |
| Ember Orange | `#ff682c` | `--color-ember-orange` | Link underline, chart highlight, tag accent, and small icon accent. |
| Brass | `#816729` | `--color-brass` | Muted warm secondary accent for chart strokes, decorative data lines, and captions. |

## Tokens - Typography

### PolySans

- **Token:** `--font-polysans`
- **Substitute:** Inter Tight or Space Grotesk at weight 400
- **Weights:** 400
- **Sizes:** 12px, 13px, 16px, 32px, 40px, 66px
- **Line height:** 0.91-1.38
- **Letter spacing:** -0.0200em
- **Role:** Headings, display text, nav items, and button labels. Never bold it.

### Inter

- **Token:** `--font-inter`
- **Substitute:** system-ui or Roboto
- **Weights:** 400, 500, 600
- **Sizes:** 12px, 13px, 14px, 15px, 16px, 18px
- **Line height:** 1.15-1.50
- **Role:** Body copy, captions, metadata, helper text, and UI labels.

### Type Scale

| Role | Size | Line Height | Weight | Letter Spacing | Token |
|------|------|-------------|--------|----------------|-------|
| micro | 13px | 1.2 | 500 | 0 | `--text-micro` |
| caption | 14px | 1.43 | 500 | 0 | `--text-caption` |
| ui | 15px | 1.33 | 500 | 0 | `--text-ui` |
| body | 16px | 1.5 | 400 | 0 | `--text-body` |
| subheading | 18px | 1.25 | 400 | 0 | `--text-subheading` |
| heading | 32px | 1.19 | 400 | -0.64px | `--text-heading` |
| heading-lg | 40px | 1.2 | 400 | -0.8px | `--text-heading-lg` |
| display | 66px | 0.91 | 400 | -1.32px | `--text-display` |

## Tokens - Spacing And Shapes

**Base unit:** 4px

**Density:** comfortable

| Purpose | Value |
|---------|-------|
| Max width | 1200px |
| Section gap | 80px |
| Card padding | 40px |
| Element gap | 20px |
| Asymmetric card top padding | 70px |
| Asymmetric card left padding | 60px |
| Large layout gap | 140px |

### Spacing Scale

| Name | Value | Token |
|------|-------|-------|
| 8 | 8px | `--spacing-8` |
| 12 | 12px | `--spacing-12` |
| 16 | 16px | `--spacing-16` |
| 20 | 20px | `--spacing-20` |
| 36 | 36px | `--spacing-36` |
| 40 | 40px | `--spacing-40` |
| 60 | 60px | `--spacing-60` |
| 80 | 80px | `--spacing-80` |
| 140 | 140px | `--spacing-140` |

### Radius

| Element | Value | Token |
|---------|-------|-------|
| buttons | 0px | `--radius-buttons` |
| asymmetric-card | 6px 0px 0px | `--radius-asymmetric-card` |
| cards | 8px | `--radius-cards` |
| data-widgets | 20px | `--radius-data-widgets` |
| tags | 20px | `--radius-tags` |
| nav-pills | 200px | `--radius-nav-pills` |

## Components

### Primary CTA Button

Graphite fill, Canvas White text, square 0px corners, PolySans-style 16px weight 400, -0.02em tracking, 10px vertical and 20px horizontal padding. No shadow and no radius.

### Ghost Outlined Button

Transparent fill, 1px Graphite border, Graphite text, 0px radius, 10px vertical and 20px horizontal padding, PolySans-style 16px weight 400.

### Navigation Pill Container

Ash background, 200px border radius, 8px vertical and 18px horizontal padding, with PolySans-style 16px links inside. This is the soft rounded counterpoint to the square buttons.

### Language Toggle Link

Plain Slate text, PolySans-style 16px, no fill, no border, and no underline.

### Asymmetric Radius Card

Ash background, radius `6px 0px 0px`, generous padding, and no shadow. Use it for featured editorial content and report-like panels.

### Data Dashboard Card

Canvas White surface, 20px radius, 40px padding, no shadow. Use Ember Orange and Brass for chart lines, rings, or active data accents.

### Hero Headline Block

PolySans-style 66px weight 400, Graphite, line-height 0.91, -1.32px tracking. Follow with 18px Inter in Steel.

### Partner Logo Strip

Monochrome Graphite logo row on white canvas. Use a small Brass caption such as a partner/trust note above the logo row.

### Text-Style Nav Link

Graphite PolySans-style 16px text with a small chevron if needed. No underline or background by default.

### Link With Orange Underline

Base text color with a 1px Ember Orange underline offset 2-3px below baseline. Use sparingly.

### Section Divider

No visible rule. Separate sections with 80px vertical whitespace and alternating Canvas White and Ash surface bands.

### Cookie Preferences Link

Small Slate text, PolySans-style 13px, no decoration, footer placement.

## Do's And Don'ts

### Do

- Use PolySans-style headings only at weight 400.
- Use -0.02em tracking on every PolySans-style text element.
- Keep Ember Orange as punctuation, not a filled CTA color.
- Use Inter for body copy, captions, metadata, and helper text.
- Use square buttons, asymmetric featured cards, and pill nav intentionally.
- Use 20px element gaps and 80px section gaps.
- Separate sections through white and Ash surface bands.
- Keep data cards flat, with charts as the main visual content.

### Don't

- Do not bold PolySans-style headings.
- Do not use Ember Orange as a button background.
- Do not add box shadows to cards or buttons.
- Do not make all cards symmetrically rounded.
- Do not introduce blue, green, purple, or extra accent colors.
- Do not set display line-height above 1.25.
- Do not crowd the layout with decorations.

## Surfaces

| Level | Name | Value | Purpose |
|-------|------|-------|---------|
| 0 | Page Canvas | `#ffffff` | Brightest base layer. |
| 1 | Ash Surface | `#efefef` | Card and section panels. |
| 2 | Fog Surface | `#f5f5f5` | Nested containers and secondary surfaces. |
| 3 | Ivory Surface | `#ebe6dd` | Warm accent wash for editorial blocks. |

## Elevation

No shadows. Data cards and nav pills are flat. Depth comes from surface contrast, geometry, and whitespace.

## Imagery

Imagery is data-driven: line charts, circular progress indicators, stat cards, dashboard widgets, and monochrome partner logos. Use Ember Orange and Brass for thin chart strokes. Avoid lifestyle photography, stock imagery, and decorative hero illustrations.

## Layout

Use a 1200px centered max-width container and 80px section gaps. The hero is a two-column split: headline, subtext, and dual CTAs on the left; overlapping dashboard cards on the right. Below the hero, use a partner logo strip. Subsequent sections alternate white and Ash bands with data cards as the main visual punctuation.

## Agent Prompt Guide

### Quick Color Reference

- Text: `#202020`
- Body text: `#4d4d4d`
- Background: `#ffffff`
- Card/section surface: `#efefef`
- Divider: `#e8e8e8`
- Accent: `#ff682c`
- Secondary accent: `#816729`

### Example Component Prompts

1. Hero section: white canvas, 66px PolySans-style headline at weight 400, line-height 0.91, -1.32px tracking, Steel subtext, square Graphite primary button, square outlined secondary button.
2. Asymmetric card: Ash background, radius `6px 0px 0px`, 70px top padding, 60px left padding, Inter body text, no shadow.
3. Data dashboard card: white surface, 20px radius, 40px padding, chart strokes in Ember Orange and Brass, no shadow.
4. Navigation bar: centered Ash pill container with 200px radius, 16px PolySans-style links, 20px gaps, language toggle in Slate.
5. Partner logo strip: white background, Brass 13px caption, Graphite monochrome logos, 20px gaps, no containers.

## Similar Reference Families

- Stripe style editorial restraint with one warm highlight.
- Linear style sharp buttons against softened surfaces.
- Plaid style data-product card imagery on warm neutral surfaces.
- Figma Config style sparse poster-like typography.

