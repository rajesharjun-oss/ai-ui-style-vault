# Components

### Top Navigation Bar
**Role:** Primary site navigation

Full-width white bar, 64-72px tall, sticky. Left: Gamma monogram logo + pill-shaped search input (999px radius, #e9e9ec border). Center: text nav links (Explore, Charts, Create, Learn) with dropdown carets, 14px weight 400 #0c0c0d. Right: 'Connect' filled black pill button (999px radius, #0c0c0d bg, #ffffff text, 16-20px horizontal padding, 8-10px vertical). Bottom border: 1px #e9e9ec.

### Search Input (Pill)
**Role:** Global collection/artist search

Rounded pill at 999px, 1px #e9e9ec border, #ffffff background, 36-40px tall. Placeholder text in #808080, search icon left in #808080. Focus state: border darkens to #0c0c0d.

### Connect Button (Filled Pill)
**Role:** Primary action - wallet connection

999px radius, #0c0c0d background, #ffffff text, 14-15px weight 600 Gamma Sans Display, 18-20px horizontal padding, 8-10px vertical padding. No border, no shadow. This is the only filled dark element in the system - it earns its weight by being the only call to action.

### Nav Link (Ghost)
**Role:** Section navigation

Transparent background, #0c0c0d text, 14px weight 400, no underline, small dropdown caret. Hover: text remains #0c0c0d (no color shift - restraint).

### Hero Feature Banner
**Role:** Showcase for the top curated drop

Full-bleed image container, 4px corner radius, with the featured artwork bleeding edge-to-edge. Overlaid massive display text ('LIGHT' at 72px weight 300) sits directly on the artwork in #0c0c0d, with no text background or scrim - the type is allowed to compete with the art. Below the image, a meta row: collection title (20-24px weight 400), creator description (16px #808080), mints claimed count with progress bar, BTC mint price in mono-weight, and a 'View Drop' outlined pill button.

### Collection Card (Grid)
**Role:** Featured drop in 2-column grid

Large rectangular card, 4px image radius on top (artwork is the visual), white surface below image, no padding between image and meta. Meta block: title (18-20px weight 400), description (14px #808080, 2 lines clamp), mints-claimed progress bar (#0c0c0d fill on #e9e9ec track), price label, 'View Drop' button. No card border, no shadow - the image edge defines the card.

### Numbered Collection List Item
**Role:** Compact ranked list of drops

Horizontal row: large ordinal number (1, 2, 3...) in 24px weight 300 #808080 on the far left, 64-80px square thumbnail (4px radius), then title (18px weight 400 #0c0c0d) and meta line (14px #808080: minted count - mint price). No card background, just whitespace separation; subtle bottom border in #e9e9ec or no border at all.

### View Drop Button (Outlined Pill)
**Role:** Secondary action on collection cards

999px radius, transparent background, 1px #0c0c0d border, #0c0c0d text, 13-14px weight 400, 16px horizontal padding, 8px vertical. Ghost/inverse of the Connect button - same shape, opposite fill, signals 'explore further' rather than 'commit'.

### Print Product Card
**Role:** Section product showcase (Prints / Editions)

Full-bleed image with a 12-20px radius depending on artwork, pink/violet gradient wash background (the Blush-to-Violet gradient), title and artist meta stacked on the left, sale status and edition count on the right with a dot indicator. A subtle white download/original chip sits at the bottom right.

### Mints Claimed Progress Bar
**Role:** Scarcity / progress indicator

Thin 2-3px tall bar, #e9e9ec track, #0c0c0d fill. Sits directly under the mints-claimed label (e.g. '44% - 432 / 1,410'). No border, no radius (or 2px max).

### Metadata Label
**Role:** Caption-level info (price, counts, dates)

14px weight 400 in #808080, often inline with a '-' separator. Numeric values may be slightly heavier (weight 600) in #0c0c0d to lift them from the label.

### Section Header with Inline Link
**Role:** Section title bar

Large section title (24-32px weight 600) with a small inline icon to its left, short descriptive subhead in 14px #808080 on the same line, and a ghost/text action link ('Explore prints') right-aligned. No divider, no background - just spacing.
