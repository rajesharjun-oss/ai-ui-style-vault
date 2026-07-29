# Components

### Sign Up Pill Button
**Role:** Primary registration CTA in navigation

9999px border-radius pill. Background: oklch green tint at 20% opacity (#004f3b equivalent). Text: #00bc7d bright green (oklch 0.979 0.021 166.113). Border: white at 10% opacity. Padding: 8px 20px. Font: JetBrains Mono 14px. Shadow: rgba(0,0,0,0.1) 0px 4px 6px -1px, rgba(0,0,0,0.1) 0px 2px 4px -2px. The translucent jewel-tint approach makes it read as a specimen label rather than a traditional CTA button.

### Log In Pill Button
**Role:** Secondary auth action in navigation

9999px border-radius. Background: dark red tint (~#8b0836 at 20% opacity). Text: near-white #fff1f2. Border: white 10% opacity. Padding: 8px 20px. JetBrains Mono 14px. Double soft shadow.

### Explore Pill Button
**Role:** Navigation action for main product discovery

9999px border-radius pill. Background: amber/orange tint at 20% opacity (#733e0a base). Text: #fefce8 warm cream (oklch 0.987 0.026 102.212). Border: white at 10% opacity. Padding: 8px 20px. Font: JetBrains Mono 14px. Third specimen-color variant completing the red/green/amber triad in navigation.

### Documentation Tab
**Role:** Navigation label for technical docs section

Flat tab style: background transparent (rgba 0,0,0,0), no border-radius (0px), no padding (0px all sides). Text: #63b3ed Portal Blue at 16px JetBrains Mono. Acts as a plain text link styled to match the terminal aesthetic - no affordance chrome, relies entirely on color for identification.

### Section Heading with Icon
**Role:** Page section titles (About, Projects, Careers)

JetBrains Mono 30px weight 400, #ffffff text. Preceded by a small colored icon ( in amber #f0b100 for Projects, in amber for About) at 16px. Icon and label sit on the same horizontal baseline with ~8px gap. No text-transform, no letter-spacing override. The monospace weight-400 at 30px is deliberately un-bold - headings do not shout.

### Project Image Card
**Role:** Visual showcase grid for AI-generated imagery

Square-aspect image tiles arranged in a 4-column grid with 8px gap. 8px border-radius on each image. Images are monochromatic blue-violet renders of anatomical/symbolic subjects (eye, brain, heart, hand) - no text overlay, no hover badge. Border: #e5e7eb Fog at low opacity as a subtle stroke. Cards function as pure image containers without any UI chrome.

### Sticky Navigation Bar
**Role:** Primary site navigation across all pages

Full-width bar with #1d293d Steel Navy background. Left side: Documentation (flat text link, #63b3ed) and Explore (amber pill) tabs. Right side: Sign Up (green pill) and Log In (red pill). All items use JetBrains Mono 14px. Vertical padding: 8px. Horizontal padding: ~48px on outer edges. Pill buttons float with translucent tinted backgrounds creating a specimen-tray organization.

### Hero ASCII Animation Background
**Role:** Full-viewport hero visual

Fills the entire first viewport with dense ASCII/generative text rendered in #cad5e2 Mist at very low opacity against the #06051d Cosmic Void background. The text forms a spherical/elliptical visual mass centered in the frame. Logo 'Midjourney' overlaid at center in a stylized typeface at approximately 36-40px. Three navigation pill buttons overlay the bottom of the hero. No image or photograph - the generative text IS the hero visual.

### Inline Body Link
**Role:** Hyperlinks within prose content

Inline text at 16px JetBrains Mono weight 400. Color: #63b3ed Portal Blue - the only chromatic accent color used in body text. No underline by default (transparent borderTopColor in the raw data). Sits at zero padding/margin within the text flow. 'community-funded research' example demonstrates usage.

### Background Gradient Surface
**Role:** Full-page atmospheric depth layer

CSS gradient: linear-gradient(0deg, #06051d 30%, #061434). Transitions from pure Cosmic Void at the bottom to a slightly lighter deep navy at the top, creating a sense of depth in a dark environment. Applied as the base layer beneath all content - not visible as a discrete element but sets the atmospheric depth of the entire page.
