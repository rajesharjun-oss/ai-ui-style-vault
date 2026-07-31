# Components

### Filled Action Button
**Role:** Primary CTA - navigation, sign-in, collect actions

Pill-shaped, 24px radius, filled with #4a83f5, white text, Google Sans Flex 14px weight 500, 8px 16px padding, no border. The only element that carries chromatic fill - its rarity is the point.

### Ghost Text Link
**Role:** Secondary navigation - 'Start reading', inline links

No background, no border. Text in #271f1b at 14px Google Sans Flex weight 500, often followed by a arrow ( ) in the same color. Hover state is not a color shift - the arrow translates 4px right.

### Navigation Pill
**Role:** Top-bar navigation container

A single rounded container (28px radius) housing nav items ('Our Story', 'Explore', 'Agents', 'Docs'), 1px #dbd5d2 border, subtle dual-shadow: rgba(0,0,0,0.05) 0 1px 2px + rgba(0,0,0,0.02) 0 0 4px. The pill grouping makes nav feel like a single control, not scattered links.

### Top Header Bar
**Role:** Site-wide header with brand, nav, and CTA

White background, logo left (sparrow glyph + 'Paragraph' wordmark in Ink Black), centered nav pill, CTA right. 80px total height. No sticky behavior needed - content is sparse enough to scroll naturally.

### Hero Section (Split)
**Role:** Landing page hero

Left half: centered vertical stack - 64px IvyOra display headline (e.g. 'Where Ideas Thrive'), 18px subheading in #888786, filled blue CTA + ghost text link side by side. Right half: phone mockup device frame showing the product UI. Max-width 1200px, 80px vertical padding, generous left-aligned text block.

### Feature Card
**Role:** Explains product capabilities in the 'Why Paragraph?' section

White card, 20px radius, 1px #dbd5d2 border, 20px padding. Icon (16px, Ink Black stroke) top-left, IvyOra 18px heading-sm title, Google Sans Flex 16px body description below. No shadow - the border does the elevation work.

### Article Card
**Role:** Content discovery card in feed/grid

White surface, 20px radius, 1px #dbd5d2 border. Cover image fills top at 16px corner radius (independent from card radius). Below: source label and date row (Google Sans Flex 14px, #888786), IvyOra 18px title, Google Sans Flex 16px excerpt excerpting 2-3 lines. 4-column grid on desktop, 16-20px gap between cards.

### Carousel Pagination Dots
**Role:** Hero slide indicator

Five small circles centered below the hero. Active dot is Ink Black filled; inactive dots are #dbd5d2. 6px diameter, 6px gap. No text labels - position is the language.

### Section Heading (Centered Serif)
**Role:** Section title between content bands

IvyOra 24px heading, weight 400, centered, letter-spacing -0.022em. Optional subheading in Google Sans Flex 16px at #888786, centered, 12px gap below title. 48-64px padding above and below the heading block.

### Tag/Badge
**Role:** Source labels, category tags on article cards

Google Sans Flex 12px weight 500, #271f1b text on #ededed background, 24px radius (pill), 4px 8px padding. No border. Functions as quiet metadata punctuation.

### Product Preview Card (Phone Frame)
**Role:** Hero product mockup

Dark device frame (rounded rectangle, ~300x600px, 28px radius) containing a simulated app UI with white inner card, gradient hero banner, author avatar, social row, and filled blue Collect button. The dark frame contrasts the white page to draw the eye.

### Source/Author Row
**Role:** Byline strip on article cards and preview

Horizontal flex row: 24px circular avatar, source name (Google Sans Flex 14px weight 500, Ink Black), separator dot, date (14px, #888786). 8px gap between elements.
