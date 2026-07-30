# Components

### Ghost Nav Button
**Role:** Top navigation items

Transparent background, #1c1c1c text at 15px weight 400, no border, 0px border-radius, padding 4px 0px 4px 6px. On hover, text color shifts subtly. No background change. These are nearly invisible as buttons - they read as plain text links.

### Outlined Pill Button
**Role:** Secondary actions like 'Log in'

Transparent background, #1c1c1c text, 1px solid #eceae4 border, border-radius 9999px (full pill), padding 6px 10px. The warm beige border makes it feel softer than a typical outlined button.

### Dark Pill Button
**Role:** Primary action ('Get started')

Background rgba(0,0,0,0.88) (#1c1c1c at 88% opacity), text #fcfbf8, border-radius 9999px. Padding 6px 10px minimum, scales with content. The slight transparency prevents the button from feeling like a harsh black block against the warm canvas.

### Frosted Pill Button
**Role:** Overlay actions on the hero gradient

Background rgba(255,255,255,0.8), text #1c1c1c, border-radius 9999px, no visible border. The translucency lets the hero gradient bleed through, tying the button to its context.

### Chat Input Card
**Role:** Hero prompt area where users type their app idea

Background #f7f4ed, border-radius 24px, padding 24px 20px. Contains placeholder text at 16px weight 400 in #5f5f5d, a '+' icon, and a 'Build' dropdown with a circular send button. The send button is a small circle (approx 28px) with a gradient fill matching the hero. Inner shadow: oklch(0 0 0 / 0.25) 0px 0px 0px 0.5px inset. Elevated shadow: oklab(0 0 0 / 0.08) 0px 0px 0px 1px, rgba(0,0,0,0.1) 0px 20px 25px -5px, rgba(0,0,0,0.1) 0px 8px 10px -6px.

### Template Preview Card
**Role:** Template gallery items in the 'Discover templates' grid

Transparent background (sits on page canvas), no border, no shadow, 0px padding on outer wrapper. Contains a screenshot image with 12px border-radius, followed by a title at 16px weight 480 in #1c1c1c and a description at 14px weight 400 in #5f5f5d. Spacing between image and text is 8px.

### Warm Surface Card
**Role:** Feature explanation panels, content containers

Background #f7f4ed, border-radius 24px, padding 24px 20px, no shadow, no border. Used for the chat prompt mockup and feature illustrations. Content inside maintains 6-8px element gaps.

### Logo Bar
**Role:** Social proof strip showing company logos

Full-width strip on #fcfbf8 background. Logos rendered in monochrome #1c1c1c, evenly spaced in a horizontal row. Preceded by a muted label at 14px weight 400 in #5f5f5d.

### Section Heading
**Role:** Major content section titles like 'Meet Lovable', 'Discover templates'

Text at 48px weight 480, color #1c1c1c, line-height 1.1, letter-spacing -1.2px. Left-aligned, no decoration. Followed by a subtitle or description at 16-18px weight 400 in #5f5f5d with 8px gap.

### Feature Step
**Role:** Numbered feature explanations ('Start with an idea', 'Watch it come to life')

Stacked text-only layout. Heading at 36px weight 480 #1c1c1c, body at 16px weight 400 #5f5f5d. Steps are stacked vertically with ~32px gap between them. No icons, no numbers, no decorative elements - relies entirely on typography weight contrast.

### View All Link
**Role:** Secondary navigation to full listings

Text link at 15px weight 400, color #030303, with an outlined pill border: 1px solid #eceae4, border-radius 9999px, padding 6px 10px. Functions as a soft secondary action.

### Sticky Navigation Bar
**Role:** Top-of-page persistent navigation

Full-width, height ~48px, background transparent or rgba(255,255,255,0.8) with backdrop-filter blur(4px) when scrolled. Contains logo on left, nav links center, 'Log in' (outlined pill) and 'Get started' (dark pill) on right. Bottom border: 1px solid #eceae4.
