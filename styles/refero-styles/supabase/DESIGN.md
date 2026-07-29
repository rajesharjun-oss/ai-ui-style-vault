# Supabase Style Reference

## Summary

Supabase is a midnight IDE with phosphor green punctuation. The interface is 99 percent grayscale: a #121212 canvas, pale text, low-contrast borders, line-art illustrations, and one sharp green pulse. It feels fast, technical, and quiet.

The system should disappear behind the product. Use border contrast, code-editor spacing, thin icon strokes, and restrained green emphasis. Do not add soft SaaS gradients, bright extra colors, or conventional card shadows.

## Theme

Dark.

## Personality

- Developer-native
- Terminal-like
- Quiet
- Technical
- Flat
- Border-driven
- Monochrome-first
- Green-punctuated

## Color System

Use a tight grayscale ladder plus four greens. Phosphor Green is the high-signal accent. Mint Pulse is a quieter text/link green. Forest Depth and Midnight Emerald are for state depth, not new accent systems.

| Name | Value | Token | Use |
| --- | --- | --- | --- |
| Phosphor Green | `#3ecf8e` | `--color-phosphor-green` | Primary CTA fill, emphasized headline words, logo mark, active state, focus border |
| Mint Pulse | `#00c573` | `--color-mint-pulse` | Inline links and quieter text accents |
| Forest Depth | `#1f4b37` | `--color-forest-depth` | Hover or pressed borders on green controls |
| Midnight Emerald | `#006239` | `--color-midnight-emerald` | Deep green brand-tinted wash or disabled-brand state |
| Snow | `#fafafa` | `--color-snow` | Primary text, button labels, icon strokes |
| Silver Mist | `#b4b4b4` | `--color-silver-mist` | Secondary text, nav links, body emphasis |
| Smoke | `#898989` | `--color-smoke` | Captions, helper text, muted icon fills |
| Graphite | `#4d4d4d` | `--color-graphite` | Icon outlines, low-emphasis dividers, line-art strokes |
| Slate | `#393939` | `--color-slate` | Input borders and subtle separators |
| Charcoal | `#2e2e2e` | `--color-charcoal` | Card and component borders |
| Ash | `#242424` | `--color-ash` | Nested cards, hover surfaces, popovers |
| Obsidian | `#121212` | `--color-obsidian` | Page canvas and default card fill |
| Void | `#0d0d0d` | `--color-void` | Illustration wells and embedded dark visual areas |

## Typography

Circular is the main typeface. It uses regular weight for most display and body text, with weight 500 reserved for emphasis. Do not use bold weights.

| Role | Font | Size | Weight | Line Height | Tracking |
| --- | --- | --- | --- | --- | --- |
| Display | Circular | 72px | 400 | 1 | -0.504px |
| Heading | Circular | 36px | 400 | 1.2 | -0.252px |
| Heading Small | Circular | 24px | 500 | 1.33 | -0.168px |
| Subheading | Circular | 18px | 400 | 1.38 | -0.126px |
| Body | Circular | 16px | 400 | 1.5 | -0.112px |
| Body Small | Circular | 14px | 400 | 1.43 | -0.098px |
| Caption | Circular | 12px | 400 | 1.5 | -0.084px |
| Code | Source Code Pro | 12px | 400 | 1.33 | 0.1em |

## Font Rules

- Use Circular for nav, body, buttons, headings, and display.
- Use Circular 400 as the default voice.
- Use Circular 500 only for button labels, card headings, handles, and emphasis.
- Do not use Circular 600 or 700.
- Use `letter-spacing: -0.007em` across normal UI text.
- Use Source Code Pro only for code snippets and terminal-like fragments.

## Spacing And Shape

- Base unit: 4px
- Page max width: 1200px
- Section gap: 64px to 96px
- Card padding: 24px
- Element gap: 8px to 16px
- Button radius: 9999px
- Tag radius: 9999px
- Card radius: 16px
- Input radius: 8px
- Nav height: 64px

## Surfaces

| Level | Surface | Value | Role |
| --- | --- | --- | --- |
| 0 | Obsidian Canvas | `#121212` | Page background and default component surface |
| 1 | Ash Card | `#242424` | Nested or elevated card and popover surface |
| 2 | Charcoal Border | `#2e2e2e` | Edge definition for cards and components |
| 3 | Void Well | `#0d0d0d` | Illustration wells and product visual backgrounds |

## Elevation

Do not use shadows. Supabase separates surfaces with 1px borders:

```css
border: 1px solid #2e2e2e;
```

Inputs use:

```css
border: 1px solid #393939;
```

Focused inputs use:

```css
border-color: #3ecf8e;
```

No glow ring. The green border is the focus indicator.

## Components

### Pill Primary Button

Phosphor Green fill, Snow text, 1px Phosphor Green border, 9999px radius, 8px vertical and 16px horizontal padding, Circular 500 at 14px. On hover, shift the border toward Forest Depth.

### Pill Ghost Button

Transparent fill, 1px Slate border, Snow text, 9999px radius, 8px by 16px padding, Circular 400 at 14px. Hover may use Graphite border and a very subtle white-alpha fill.

### GitHub Stars Pill

Ash fill, 1px Charcoal border, Snow text, 9999px radius, 6px by 10px padding, GitHub icon in Snow, Circular 400 at 12px. It is social proof, not a CTA.

### Feature Card

Obsidian fill, 1px Charcoal border, 16px radius, 24px padding. Use a Phosphor Green icon, Snow heading at Circular 500 18px, and Silver Mist body text at Circular 400 14px. Lower visual wells can use Void background with Graphite wireframe line art.

### Product Showcase Card

Larger feature card using the same Obsidian fill, Charcoal border, 16px radius, and 24px padding. The visual area should show dark product UI, wireframe geometry, database grids, or technical diagrams with a few green dots.

### Testimonial Card

Obsidian fill, 1px Charcoal border, 16px radius, 20px padding. Avatar at 40px, handle in Snow Circular 500 14px, quote in Silver Mist Circular 400 14px. Use a masonry grid so cards can vary in height.

### Announcement Pill

Ash fill, 1px Charcoal border, 9999px radius, 6px by 16px padding, Silver Mist Circular 400 12px, optional chevron icon.

### Logo Cloud Item

Monochrome logo in Smoke, around 24px high, no border, no background. Keep logo strip quiet.

### Top Navigation Bar

Full-width, about 64px height, transparent or Obsidian on scroll. Left logo uses green mark plus Snow wordmark. Center nav links are Silver Mist Circular 400 14px. Right side has GitHub pill, sign-in ghost button, and green start button. Use a 1px Charcoal bottom border.

### Input Field

Obsidian background, 1px Slate border, 8px radius, 8px by 12px padding. Text in Snow, placeholder in Smoke, Circular 400 14px. Focus shifts border to Phosphor Green with no glow.

## Layout

Use a full-width dark page with centered 1200px content. The hero is centered:

1. Announcement pill.
2. 72px Circular headline.
3. Second headline line or keyword in Phosphor Green.
4. 16px Silver Mist subtitle.
5. Two side-by-side pill buttons.

Below the hero, use a logo cloud strip, centered text blocks, 2x2 card grids, 4-column feature layouts, and masonry testimonial grids. Maintain 64px to 96px section gaps. Avoid visible dividers between sections; let spacing and border-based cards create rhythm.

## Imagery

Use diagrammatic developer-tool imagery:

- Wireframe illustrations.
- 3D geometric cubes rendered as line art.
- Database grids.
- Network nodes.
- Product screenshots in dark frames.
- Terminal and code snippets.
- Thin stroke icons at about 1.5px.

Use Graphite strokes on Void wells, with tiny Phosphor Green dots or active highlights. Avoid photography, lifestyle imagery, glossy 3D, gradients, and generic abstract blobs.

## Do

- Use Phosphor Green only for CTAs, logo, active states, focus borders, and emphasized keywords.
- Keep the page canvas at Obsidian.
- Use Snow for primary text.
- Use Silver Mist and Smoke for quieter text.
- Separate surfaces with 1px Charcoal borders.
- Keep buttons and tags fully pill-shaped.
- Keep cards at 16px radius.
- Keep inputs at 8px radius.
- Use Circular 400 and 500 only.
- Use Source Code Pro only for code fragments.

## Do Not

- Do not add colors outside the green and grayscale palette.
- Do not use Circular weights above 500.
- Do not add card shadows, glows, or gradient fills.
- Do not use a non-Obsidian page canvas.
- Do not place Phosphor Green on large section backgrounds.
- Do not use radius values outside 9999px, 16px, and 8px for normal UI.
- Do not use photography or lifestyle imagery.
