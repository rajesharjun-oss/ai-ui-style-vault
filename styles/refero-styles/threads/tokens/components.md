# Components

### Feed Container
**Role:** Central scrollable surface that holds all posts

Max-width 640px, centered on a #fafafa page. Rounded 18px corners. Background Paper White (#fafafa). Subtle elevation via box-shadow: 0 0 12px rgba(0,0,0,0.04) with a 48px spread halo in Paper White to create a soft lift off the #efefef plane beneath. The container is the only elevated element on the page

### Log In Button
**Role:** Primary authentication action in the top-right

Pill shape (border-radius 1000px), background Ink Black (#000000), text Paper White (#fafafa), system-ui 15px/600, padding 8px 16px. No border. Fills the role of a dark filled button on an otherwise borderless surface

### Post Card
**Role:** Individual feed entry

Flat, no card background - sits directly on Feed Container Paper White. Separated from neighbors by a 1px Cloud Gray (#d5d5d5) bottom border. Internal padding 16px. Three-zone vertical layout: header (avatar + username + timestamp + menu), body (text and/or media), engagement bar

### Circular Avatar
**Role:** User identity mark in post headers and sidebar

Border-radius 1000px (full circle). Default 40px diameter in feed posts, 24px in engagement sub-lists. No border. Image fill only

### Verified Badge
**Role:** Identity confirmation next to usernames

Small circular icon filled with Meta Blue (#385898), white checkmark inside. Sits inline after the username. The only place where the brand blue is used as a fill

### Post Engagement Bar
**Role:** Like, comment, repost, share actions beneath each post

Horizontal row of four line icons (heart, comment bubble, circular arrow, paper plane). Icons are Ash Gray (#969696) at rest, Ink Black on interaction. Counts in 13px/400 system-ui, Graphite (#424242). Touch targets ~40px. No button backgrounds or borders

### Link Preview Card
**Role:** Embedded article preview within a post

Full-width within post body, border 1px Cloud Gray (#d5d5d5), border-radius 8px, no shadow. Internal layout: optional image top (full-width, no radius override), then site name in 13px/400 Graphite, then headline in 15px/400 Ink Black. Padding 12px on the text zone

### Sidebar Icon Button
**Role:** Navigation targets in the left rail

Square 48px touch target with a centered 24px line icon. No background, no border. Icon color Ash Gray (#969696) at rest, Ink Black when active. The Threads wordmark logo sits at the top of the same rail, ~56px square

### Compose Button
**Role:** Quick post creation entry from sidebar

Larger square icon-button in the sidebar with a plus glyph. Ink Black icon, no fill. 48px target. Sits mid-rail between navigation icons

### Top Header Bar
**Role:** Page-level title and entry to authentication

Full-width, ~53px tall, background Paper White. Centered 'Home' label in 15px/600 Ink Black. Right-aligned Log In button. No visible bottom border - separation is implied by whitespace

### Post Overflow Menu Trigger
**Role:** Per-post action menu

Three-dot icon, Ash Gray (#969696), 20px square, top-right of every post header. No background until hover, then a very faint #efefef fill

### Inline Hashtag / Mention
**Role:** Interactive text within post body

Same system-ui 15px/400 as body text, color Meta Blue (#385898). No underline by default; underline appears on hover. Functions as a text link, not a button
