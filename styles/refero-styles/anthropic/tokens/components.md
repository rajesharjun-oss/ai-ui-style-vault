# Components

## Text Link Button

- **Role:** Navigation and inline action.
- **Style:** Transparent background, Slate Dark text, no border, no radius, text-style padding.
- **Behavior:** Underline appears on hover for button-like links; inline editorial links stay underlined persistently.

## Filled Ivory Button

- **Role:** Primary action on light surfaces when using neutral chrome.
- **Style:** Ivory Light fill, Slate Dark text, bottom-only `8px` radius, sharp top corners, no border, no shadow.
- **Rule:** The bottom-only radius makes it feel like a paper tab, not a generic button.

## Outlined Dark Button

- **Role:** Secondary action on dark utility bands or consent UI.
- **Style:** Transparent background, white text, `1px #87867f` border, `12px` radius, compact padding.

## Clay Filled Button

- **Role:** The single chromatic CTA.
- **Style:** Clay fill, light or dark high-contrast text depending on context, `8px` radius, no shadow.
- **State:** Deepens to Clay Deep on hover or pressed state.
- **Rule:** Use only for the most consequential action.

## Featured Hero Card

- **Role:** Large editorial feature or story highlight.
- **Style:** Manilla surface, `24px` radius, no shadow, no border, generous padding.
- **Content:** Large serif display text and warm scientific or editorial illustration.

## Release Card

- **Role:** Compact latest-release or article card.
- **Style:** Ivory Light surface, `24px` radius, optional `1px Stone` border, around `24px` padding.
- **Type:** Sans title or serif title, serif body, persistent underlined link.

## Top Navigation Bar

- **Role:** Sticky site navigation.
- **Style:** Transparent or Ivory Medium background, logo left, small sans nav links, right-side neutral action.
- **Behavior:** Muted nav text moves toward Slate Dark on hover.
- **Rule:** No blur, shadow, or decorative nav container.

## Footer

- **Role:** Dark closing section.
- **Style:** Full-bleed Slate Dark, Ivory Light text, multi-column link grid.
- **Type:** Sans `12px` headings and links, muted link color for hierarchy.
- **Rule:** This is the main inversion surface.

## Hero Heading Block

- **Role:** First-screen editorial composition.
- **Style:** Two-column layout with a bold sans declarative heading on one side and serif supporting paragraph on the other.
- **Detail:** Inline links can appear inside the heading with persistent underline.

## Inline Underlined Link

- **Role:** Link embedded in paragraph or heading copy.
- **Style:** Inherits text color and always shows a thin underline.
- **Rule:** Persistent underline is part of the editorial print convention.

## Badge Or Inline Label

- **Role:** Category or metadata marker.
- **Style:** Transparent, no border, no background fill, no badge container.
- **Rule:** Treat it as weighted inline text, not a chip.

## Cookie Consent Bar

- **Role:** Bottom-pinned consent prompt.
- **Style:** Slate Dark band with readable body text and a compact button group.
- **Buttons:** Filled Ivory Button for accept; Outlined Dark Button for secondary choices.

## Skip Link

- **Role:** Keyboard accessibility utility.
- **Style:** Ivory Light surface, Slate Dark text, small padding, visible on focus.

