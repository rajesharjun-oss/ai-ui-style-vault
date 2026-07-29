# ChatGPT - Style Reference

## Positioning

ChatGPT reads as restrained utility software. The interface exists to frame conversation text, not to decorate around it. It is grayscale, compact, native-feeling, and quiet. The product should feel like a dependable writing surface rather than a promotional brand page.

## Theme

- Theme: light
- Mood: graphite ink on warm paper
- Best fit: chat products, AI workspaces, document tools, command interfaces, writing environments, notes apps, internal tools, knowledge systems

## Visual Principles

1. Keep the UI achromatic.
2. Use system fonts only.
3. Let text and layout provide hierarchy.
4. Use hairline borders instead of shadows.
5. Use 10px radius for most interactive chrome.
6. Use hover veil for feedback, not colored states.
7. Keep display type modest.

## Color System

| Token | Value | Role |
| --- | --- | --- |
| Sidebar Mist | `#f9f9f9` | Sidebar and secondary surface backgrounds |
| Pure White | `#ffffff` | Main canvas, panels, and elevated surfaces |
| Graphite Ink | `#0d0d0d` | Primary text, headings, and icon fills |
| Mid Ash | `#5d5d5d` | Secondary text, icons, labels, metadata |
| Hollow | `#8f8f8f` | Tertiary text, disabled states, helper copy |
| Hairline | `#0000001a` | 1px borders and dividers |
| Hover Veil | `#0000000d` | Hover state wash |
| Ink Press | `#000000` | Pressed or inverted surfaces, tooltips, scrims |
| Deep Charcoal | `#00000080` | Modal scrim overlay |
| Edge Gray | `#e6e6e6` | Stronger divider or inactive surface |

## Typography

Use the system UI stack for the entire interface. Do not load custom fonts. Body copy sits at 16px with a comfortable 1.5 line height. Captions and sidebar rows sit around 14px. The only display tier is 24px and should be reserved for welcome headings or compact page headers.

Recommended stack:

```css
font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
```

### Type Scale

| Role | Size | Line Height | Weight | Tracking |
| --- | ---: | ---: | ---: | ---: |
| Caption | 14px | 1.43 | 400 | normal |
| Body | 16px | 1.5 | 400 | normal |
| Heading | 24px | 1.33 | 600 | normal |

## Spacing And Shape

- Density: compact
- Page max width: 1200px
- Conversation max width: 720px to 768px
- Sidebar width: 260px to 280px
- Header strip: 52px
- Section gap: 24px
- Card padding: 16px
- Element gap: 6px
- Nav, cards, and buttons: 10px radius
- Links: 16px radius
- Badges/chips: 0px radius
- Log In CTA: full pill radius

## Layout

Use a two-column shell. The left rail is Sidebar Mist and contains the header, navigation actions, chat history, and footer CTA stack. The main column is Pure White and centers the conversation thread at a comfortable reading width. Avoid a global top navigation bar; the product chrome should stay vertical and quiet.

## Imagery

Use no decorative imagery. No photography, no illustrations, no product screenshots, and no abstract graphics. The conversation text and user content are the visual content. Icons should be monochrome line icons around 16px.

## Components

### Sidebar Item

Transparent by default, Graphite Ink icon and text, 10px radius, 6px vertical padding, 10px horizontal padding. Hover fills with Hover Veil. Active state should be subtle and should not introduce color.

### Compact Icon Button

Transparent fill, 10px radius, 6px vertical and 8px horizontal padding, 16px Graphite Ink icon. Hover uses Hover Veil.

### Pill Primary Button

Used for the Log In account entry action. Pure White fill, Graphite Ink text, 1px Hairline border, full pill radius, 0px vertical and 16px horizontal padding, 14px weight 500.

### Sidebar Footer Block

Vertical stack with no background, 10px row gap, and a Hairline top divider separating it from the chat list.

### Helper Text Block

Hollow 12px to 14px regular text with 1.43 line height. No background. Used for secondary explanations under links or account prompts.

### Conversation Card

Recent chat row with transparent default, 10px radius, 6px vertical padding. Hover fills with Hover Veil. Title uses Graphite Ink at 14px weight 500; preview uses Hollow at 13px.

### Hairline Divider

1px solid Hairline. The only structural divider. No double rules and no shadows.

### Surface Card

Pure White surface, 10px radius, 1px Hairline border. Used for menus, popovers, and floating panels. Elevation comes from the border.

### Tooltip

Ink Press fill, white text, small radius, compact padding. No arrow ornament required.

### Scrim Overlay

Deep Charcoal backdrop at 50% black. Single-layer and no blur.

### Badge Or Chip

Sidebar Mist background, Graphite Ink text, 0px radius, low prominence. Do not use color status chips.

## Rules

- Use Graphite Ink for primary text and icons.
- Reserve pure black for pressed/inverted surfaces, tooltips, and scrims.
- Keep the interface fully achromatic.
- Use 6px element gaps and 24px section gaps.
- Use 10px radius for buttons, sidebar items, and cards.
- Use a full pill radius only for the Log In CTA.
- Use system fonts only.
- Express elevation with 1px Hairline borders, never shadows.
- Use Hover Veil for hover states.
- Do not use text larger than 24px.
- Do not load custom webfonts.
- Do not add decorative imagery.
