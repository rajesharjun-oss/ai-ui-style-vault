# Components

### Top Navigation Bar
**Role:** Minimal site-wide navigation

White (Paper) background, no border, no shadow. Left: 'VUCKO' wordmark at 17px Suisse weight 700 in Ink. Center: location/time text ('Toronto, Canada 20:34 pm') at 17px Suisse weight 400 in Ink. Right: nav links ('Projects, Approach, About, Contact') at 17px Suisse weight 400 in Ink, followed by a small 8px Ink dot indicator with 9999px radius. 56px horizontal padding, approximately 19px vertical padding. The dot serves as an ambient status indicator - it is not interactive.

### Hero Display Wordmark
**Role:** Primary brand statement on landing

The wordmark 'VUCKOTM' at 211px Suisse weight 700, color Ink, letter-spacing -12.03px, line-height 1.0. Sits directly on the Paper canvas with 56px left/right padding. The TM superscript is positioned at the baseline-right of the final O. The wordmark is intended to overflow or fill the viewport width - it is architecture, not text. No background, no border.

### Floating Showcase Card
**Role:** Featured project overlay on hero

A small card positioned absolutely in the upper-right of the hero, ~9.6px border-radius, with a vivid chromatic background (project content - yellow in current instance). Contains a bold black project title ('2023 Wrapped') at ~43px Suisse weight 700 and a small description below at 17px. The card itself is content, not a system component, but the container follows the 9.6px card radius token and 24px internal padding.

### Tagline Section
**Role:** Brand statement below hero

Left-aligned narrow column on Paper canvas. Headline at 19px Suisse weight 400 in Ink, line-height 1.5, max-width ~480px. Below the headline, an underlined text link 'Learn more about our approach' at 17px Suisse weight 400 in Ink with 1px Ink underline. At the far right of the same row, a '(Scroll)' indicator at 17px Suisse weight 400 in Ink. 58px top margin from the hero wordmark.

### Project Showcase Card (Full-bleed)
**Role:** Client work presentation in portfolio

Full-bleed card with 9.6px border-radius, filling the container width minus 56px horizontal padding. Background is a vivid gradient (project content - blue-to-purple in current instance). Centered display text at 55px Suisse weight 700 in Paper (white), letter-spacing -1.1px, with playful decorative elements. A pill button (9999px radius, white fill, black text at 17px) overlaid at the bottom, labeled with a project name. Card internal padding approximately 56px.

### Service Block (Media + Text)
**Role:** Individual service description in services section

Split layout. Left side: a black (Ink) square block, approximately 200px wide, serving as a video/image placeholder. Below the block, body text at 17px Suisse weight 400 in Ink describing the service, max-width ~200px. Right side contains the Service List Display. 23px gap between media and text.

### Service List Display
**Role:** Large-scale service category headings

Three stacked display headings at 55px Suisse weight 700, each on its own line, left-aligned. The first item ('IDENTITIES') in Ink (#000000); subsequent items ('SYSTEMS', 'GUIDELINES') in Steel (#888a8b) to create visual de-emphasis through tonal shift rather than size or weight change. Letter-spacing -1.1px, line-height 1.13. This tonal hierarchy - not size hierarchy - is what makes the list read as a menu rather than a stack of headlines.

### Pill Tag / Button
**Role:** Project labels, nav indicators, and pill-shaped interactive elements

9999px border-radius, white (Paper) background, 1px Ink border optional. Text at 17px Suisse weight 400 in Ink. Padding approximately 10px vertical, 15px horizontal. No shadow, no gradient. Used for project name tags and ambient UI marks. The pill shape is the only non-rectangular element in the system.

### Underline Text Link
**Role:** Primary text-based link style

Text at 17px Suisse weight 400 in Ink with a 1px Ink underline. No background, no border, no padding beyond the text's natural line height. This is the system's link and CTA equivalent - there are no filled buttons in the interface. Hover state may shift underline to a thinner weight or remove it.

### Scroll Indicator
**Role:** Navigation hint at hero boundary

Right-aligned text '(Scroll)' at 17px Suisse weight 400 in Ink. Functions as a passive navigation prompt at the bottom of the hero section. No underline, no decoration. 58px top margin from the tagline section.
