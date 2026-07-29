# Components

### Primary CTA Button
**Role:** Filled dark pill - the only dense visual element on the page

Background #181d27, white text (#ffffff), border-radius 32px (or 9999px for full pill), padding 12px 32px, font Geist 16px weight 500, letter-spacing -0.01em. Tight dark shadow ring (0 1px 2px rgba(10,13,18,0.8), 0 0 0 1px #0a0d12) gives it a pressed, pressed-into-page quality. Used for 'Sign up' and the single hero action.

### Secondary CTA Button
**Role:** Smaller filled pill for inline actions

Background #181d27, white text, border-radius 16px, padding 8px 16px, Geist 14px weight 500. Compact variant of the primary.

### Ghost Nav Link
**Role:** Header navigation text

No background, Geist 16px weight 500, color inherits from #0a0d12 or #535862, no underline, no hover background fill. Sits on the canvas as plain typography.

### Feature Card (32px radius)
**Role:** Primary content card - FAQ, testimonial, feature block

Background #fafdff (bone white), border-radius 32px, padding 40px on all sides, no visible border, no shadow. The card relies on the color shift from canvas (#ebf5ff) to surface (#fafdff) and the 32px radius to define itself.

### Pastel Category Tile
**Role:** Colored feature block - style library, category cards

Solid pastel background (#f1e6ff lavender, #d3f6e3 mint, #cce7ff powder blue, #fff2be solar), border-radius 32px, generous padding, no border. Each tile is a flat wash of color - no gradients on the tile itself, though some use gradient fills (#c2e9ff, #e4ccff, #ffd1b8).

### Testimonial Card
**Role:** Masonry-style horizontal card in the social-proof section

Background #fafdff, border-radius 32px, padding 40px, contains a pull-quote at Geist 18px #535862, a divider, then avatar + name (Geist 16px weight 500 #0a0d12) + role (Geist 14px #93979f) and a brand logo on the right. Cards bleed off the edges of the viewport in a continuous horizontal marquee.

### FAQ Accordion Row
**Role:** Expandable question/answer block

Background #fafdff, border-radius 32px, padding 40px. Question in Geist 18-20px weight 500 #0a0d12, answer in Geist 16px #93979f. Animated open/close using grid-template-rows transition at 0.65s ease.

### Pill Tag / Chip
**Role:** Category labels and status indicators

Border-radius 9999px, Geist 12-14px weight 500, padding 4px 12px. Appears in pastel-tinted backgrounds for category labels.

### Marquee Logo Strip
**Role:** Endlessly scrolling brand logo wall

Continuous horizontal marquee animation (no visible container). Logos are monochrome or brand-colored, float in the sky canvas with no card wrapper. Uses linear(0 0%, 0.55 7.5%, ...) timing function for the scroll.

### Hero Gradient Banner
**Role:** Decorative border/frame around hero artwork

Thin border using the iris gradient (linear-gradient(71,157,255 11.43%, 0,105,224 78.2%)) with 3px solid weight and border-radius 90px. The only place a gradient border appears - it frames the hero illustration like a polaroid edge.

### 3D Illustration Asset
**Role:** Whimsical floating objects - clouds, crayons, envelopes, smiley faces, flowers

Rounded, dimensional, pastel-colored 3D renders. They float in the canvas as isolated objects with no background container. Colors come from the pastel palette (#cce7ff, #f1e6ff, #d3f6e3, #ffd1b8) plus a vivid iris blue accent. Sized large and given room to breathe - they are the brand personality, not decoration.

### Section Header
**Role:** Centered display headline + supporting subhead

Aeonik 48-72px weight 500 in #0a0d12, centered, with a Geist 18px subhead in #535862 below. The 148px hero variant is reserved for the first screen. Letter-spacing tightens with size (-0.96px at 48px, -1.44px at 72px, -2.96px at 148px).
