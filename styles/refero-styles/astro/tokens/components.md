# Components

### Primary Pill Button
**Role:** Main call-to-action (e.g., 'Get Started')

Full pill shape at 9999px radius, background #ffffff, text #1f232 at 16px weight 600, padding 12px 24px. High contrast inverted style - white on dark. No border. The inversion (white bg, dark text) is the system's signature CTA pattern.

### Terminal Command Box
**Role:** CLI install command display

Background #060913 with 1px border at #1f232, 8px radius, padding 12px 16px. Contains monospace 14px text in #f2f6fa with a copy icon at right. Rounded corners are soft, not pill - the box should feel like a terminal window embedded in the page.

### Version Badge
**Role:** Release announcement pill (e.g., 'Astro 6.1')

Inline pill at 9999px radius, background #1f232 with 1px border #2c303b, padding 4px 12px. Text in #f2f6fa at 14px weight 500. Optionally preceded by a colored dot (Signal Blue #61dafb). Compact, instrument-panel aesthetic.

### Feature Icon Circle
**Role:** Icon container in feature columns

48px circle with 1px colored border (blue, pink, or amber), transparent background. Contains a small inline icon. The colored border is the only color in the feature row - makes the icon feel like a charged node.

### Theme Preview Card
**Role:** Showcase tile for theme marketplace

16px radius, background #17191, 1px border #1f232e. Internal image fills at 12px radius. Padding 0 (image bleeds to edges). Title and metadata appear below the image, not overlaid. The card sits on the void canvas with a barely-there border.

### Filter Tab Pill
**Role:** Category filter for grids (e.g., 'Trending', 'E-Commerce')

9999px radius, two states: active = background #1f232 + border #2c303b + white text; inactive = transparent + border transparent + #858b98 text. Padding 8px 16px, text 14px weight 500. Active state uses the border as the only visual differentiator.

### Logo Cloud Item
**Role:** Customer/partner logo display

Inverted to white (#f2f6fa) on the dark canvas. No container or border - logos float directly on the background. Sized to a consistent visual weight (~24-32px height). Arranged in a single row or two-row wrap.

### Section Header
**Role:** Eyebrow label + headline + description block

Eyebrow at 14px weight 600 in a chromatic accent (violet #acafff, teal #4bf3c8, or blue #54b9ff). Headline in Obviously 36px weight 300-400 in #f2f6fa. Description in body 16px weight 400 in #858b98. The colored eyebrow is the only chromatic punctuation in the section.

### Navigation Bar
**Role:** Top-level site navigation

Transparent background, sits on the void canvas. Logo (Astro mark) left, nav links center-right, GitHub icon far right. Nav text in #f2f6fa at 14px weight 500. No border or shadow - the nav is position-relative and disappears into the canvas.

### Hero Gradient Backdrop
**Role:** Atmospheric background glow behind hero content

Radial gradient blooming from center-top, combining the nebula blue (#3245ff at 30% opacity) blending into the void canvas (#1f232e). The gradient is positioned above the text layer with mix-blend-mode for a soft cosmic glow effect. No hard edges.

### Stats Bar
**Role:** Performance metric display (e.g., '% of real-world sites with good Core Web Vitals')

Horizontal bar chart on a #060913 background with 1px #1f232 border, 8px radius. Bars in the brand gradient (#3245ff #b845ed). Label in 14px monospace, value in 16px weight 600 #f2f6fa.
