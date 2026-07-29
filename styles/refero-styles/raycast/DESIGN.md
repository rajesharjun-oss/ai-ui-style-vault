# Raycast - Style Reference

Theme: dark

Raycast's Refero style is a dark command-center system. The canvas is almost black, with subtle surface steps and tactile inset treatments that feel like pressed keyboard keys. Coral is a brand punctuation mark, not a broad action color. CTAs are neutral light-gray fills, while the product atmosphere comes from a dramatic red/blue hero composition and dark product mockups.

## Core Principles

- Keep the entire page dark.
- Use `#040506` as the page canvas.
- Make CTAs neutral, not chromatic.
- Reserve coral for logo, hero artwork, AI badge, and warm accent surfaces.
- Use Inter for body, nav, headings, and most UI.
- Use Geist Mono for technical metadata and command-like microcopy.
- Use inset highlights and rings for tactile depth.
- Avoid conventional drop shadows and light sections.

## Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| Void Black | `#040506` | `--color-void-black` | Page canvas and dominant background. |
| Ink | `#07080a` | `--color-ink` | Card surfaces, elevated blocks, product mockup backgrounds. |
| Obsidian | `#111214` | `--color-obsidian` | Recessed controls, input wells, pressed states. |
| Graphite | `#1b1c1e` | `--color-graphite` | Badge fills and understated UI feedback. |
| Slate | `#2f3031` | `--color-slate` | Dark button borders and labels on dark controls. |
| Iron | `#454647` | `--color-iron` | Text on neutral filled buttons and mid-gray borders. |
| Smoke | `#6a6b6c` | `--color-smoke` | Secondary copy, muted labels, footer metadata. |
| Ash | `#9c9c9d` | `--color-ash` | High-contrast captions and secondary nav labels. |
| Mist | `#e6e6e6` | `--color-mist` | Neutral filled action background. |
| Pure White | `#ffffff` | `--color-pure-white` | Headings and highest-emphasis text. |
| Coral Pulse | `#ff6363` | `--color-coral-pulse` | Brand mark, hero saturation, AI badge, tiny warm punctuation. |
| Ember Hush | `#452324` | `--color-ember-hush` | Warm-tinted card or accent surface. |
| Electric Sky | `#63a1ff` | `--color-electric-sky` | Hero illustration blue mid-tone only. |
| Cobalt Edge | `#143ca3` | `--color-cobalt-edge` | Hero illustration blue depth only. |
| Deep Space | `#02193b` | `--color-deep-space` | Darkest hero artwork blue only. |
| Info Blue | `#56c2ff` | `--color-info-blue` | Soft decorative highlight wash, not status blue. |
| Success Green | `#59d499` | `--color-success-green` | Soft decorative highlight wash, not status green. |

## Typography

### Fonts

- Primary: Inter.
- Primary fallback: system-ui, -apple-system, Helvetica Neue, Arial, sans-serif.
- Code/meta: GeistMono.
- Code fallback: JetBrains Mono, Menlo, Monaco, Courier, monospace.
- System glyphs and numeric callouts: SF Pro Text or system UI font.

### Type Scale

| Role | Size | Weight | Line Height | Tracking | Use |
| --- | --- | --- | --- | --- | --- |
| eyebrow | 11px | 500 | 0.91 | 0.8px | Uppercase technical labels. |
| body | 16px | 400 | 1.15 | 0 | Body copy and standard UI text. |
| body-lg | 18px | 400 | 1.15 | 0 | Larger explanatory copy. |
| subheading | 20px | 500 | 1.2 | 0.2px | Feature headings and supporting titles. |
| heading-sm | 24px | 500 | 1.15 | 0 | Small section headings. |
| heading | 32px | 500 | 1.15 | 0 | Standard section headings. |
| heading-lg | 56px | 400 | 1.17 | 0.22px | Hero headline signature size. |
| display | 64px | 600 | 1.1 | 0 | Rare display moments. |

## Spacing And Shape

| Purpose | Value |
| --- | --- |
| Density | comfortable |
| Base unit | 8px |
| Max width | 1200px |
| Section gap | 80-120px |
| Card padding | 24px |
| Element gap | 8-16px |

### Spacing Scale

`8px`, `16px`, `24px`, `32px`, `40px`, `48px`, `56px`, `64px`, `80px`, `96px`, `120px`, `224px`

### Radius

| Element | Value |
| --- | --- |
| badges | 6px |
| inputs | 8px |
| buttons | 8px |
| cards | 16px |
| large cards | 20px |
| pills | 9999px |
| icon containers | 99999px |

## Shadow And Depth

The important treatment is not a floating shadow. It is an inset key treatment:

```css
box-shadow:
  rgba(255, 255, 255, 0.05) 0 1px 0 0 inset,
  rgba(255, 255, 255, 0.25) 0 0 0 1px,
  rgba(0, 0, 0, 0.2) 0 -1px 0 0 inset;
```

Use this on elevated cards and feature blocks. It should feel tactile and pressed, not like a floating material card.

## Components

### Glass Navigation Bar

Floating pill nav over the dark hero. Use backdrop blur around 48px, 1px `#363739` border, 8px radius, transparent dark fill, white brand mark, Ash nav links, and a neutral Mist download button.

### Neutral Filled Button

Primary action button. Use Mist fill, Iron text, Inter 13-14px medium, 8px radius, 8px 12px padding, and optional small platform icon. Do not use coral, blue, or green as CTA fills.

### Ghost Nav Link

Transparent link with Ash text at 13-14px. Hover to Pure White. No individual border or fill.

### Feature Card With Key Shadow

16px radius, 24px padding, dark or transparent surface, and the key-shadow stack. Content typically includes a circular icon container, 20px subheading, and 16px muted body copy.

### Edge-Highlight Card

16-20px radius with a 1px `#363739` edge and inset highlight. Use when a card should be defined by its edge rather than by a solid fill.

### Inset Input Field

8px radius, subtle white-tinted fill, 8px 12px padding, white input text, and Ash placeholder text. The field should feel recessed into the dark surface.

### Badge Tag

Graphite fill, white text, 6px radius, tight horizontal padding. Use for versions, beta labels, categories, and compact metadata.

### Circular Icon Container

Full-circle backing with dark fill, 20px padding, and a 24-32px glyph or product icon. It should feel like a dock icon container.

### Hero Gradient Banner

The one intentionally loud visual moment: full-bleed dark hero with red/coral diagonal geometry and blue atmospheric gradients behind centered copy. After the hero, return to austere dark surfaces.

### Footer Meta Strip

Centered Geist Mono 12px metadata row in Smoke, separated by vertical pipe characters. Use for version, platform, install command, and technical details.

### App Window Mockup

Dark product mockup with rounded command bar and result list. Use Coral Pulse only for a selected state or tiny highlight.

## Surfaces

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 0 | Canvas | `#040506` | Default page background. |
| 1 | Card | `#07080a` | Elevated content blocks and mockup backdrops. |
| 2 | Recessed | `#111214` | Inputs, pressed wells, and inset states. |
| 3 | Badge | `#1b1c1e` | Dense tag surfaces and compact tiles. |
| 4 | Accent Tint | `#452324` | Warm coral-tinted sections or cards. |

## Imagery

Use abstract red/blue hero geometry and product UI mockups. Avoid photography and generic lifestyle imagery. Below the hero, show dark command bars, extension tiles, product screenshots, and compact app-like previews.

## Layout

The hero and atmospheric artwork can be full-bleed, but content sections sit in a centered 1200px container. Use large vertical rhythm, typically 80-120px between sections. Card grids can be 3-column for compact tiles or 2-column for larger feature blocks. Do not introduce light theme bands.

## Do

- Use `#040506` as the page background.
- Keep filled actions neutral with Mist fill and Iron text.
- Keep coral tightly limited to brand and hero moments.
- Use Inter at 56px/400 for the hero headline.
- Use key-shadow inset treatment for tactile card depth.
- Use Geist Mono for version and technical metadata.
- Keep all spacing on the 8px grid.

## Don't

- Do not use coral as general body text, link color, icon color, or CTA fill.
- Do not use chromatic CTA buttons.
- Do not add conventional drop shadows to cards.
- Do not introduce light sections.
- Do not combine many accent colors in one surface.
- Do not use SF Pro Text for body copy.
- Do not break the 8px spacing grid.

