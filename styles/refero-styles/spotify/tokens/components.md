# Components

### Pill Button - Green Primary
**Role:** High-emphasis action button

Filled pill with #1ed760 background, #000000 text, weight 700 at 14px. 9999px border radius, 12px vertical / 32px horizontal padding. No border. Used for 'Log in' and confirmatory actions. Sits as the only chromatic button in the system.

### Pill Button - White Secondary
**Role:** Medium-emphasis action

Filled white pill (#ffffff) with #000000 text, weight 700 at 14px. 9999px radius, 12px 32px padding. Functions as the secondary CTA paired with the green primary - e.g. 'Sign up free' in the premium banner. High contrast against the dark canvas.

### Pill Button - Ghost Outline
**Role:** Low-emphasis action

Transparent fill with a 1px white border at reduced opacity, white text. 9999px radius. Used for secondary nav items and 'Create playlist' / 'Browse podcasts' CTAs inside the sidebar.

### Album Card
**Role:** Content tile for albums, singles, playlists

Square 1:1 album artwork on #121212 background, 6px border radius, 0px 8px 24px rgba(0,0,0,0.5) shadow. Title in #ffffff at 16px weight 400 below the image; artist/subtitle in #b3b3b3 at 14px. 12px padding around the text block. No border.

### Artist Card
**Role:** Circular artist portrait with name

1:1 image cropped to full circle (9999px radius) on transparent background. Artist name in #ffffff at 16px below, role label ('Artist') in #b3b3b3 at 14px. No card surface or shadow - the circular image floats directly on the void canvas.

### Sidebar Library Panel
**Role:** Left-rail persistent navigation container

#000000 background, full-height column, 8px horizontal padding. Houses 'Your Library' header with + icon, then scrollable list of playlist/artist shortcuts. No visible border between sidebar and main content - separation is achieved through the surface tier alone.

### Playlist Prompt Card
**Role:** Onboarding call-out inside the library

Rounded rectangle at 6px radius on #121212 with 0 8px 24px shadow. Bold heading in #ffffff at 16px, supporting copy in #b3b3b3 at 14px, and a pill ghost button below. 12px internal padding. Example patterns: 'Create your first playlist' and 'Let's find some podcasts to follow'.

### Top Navigation Bar
**Role:** Global header

Horizontal bar with #000000 background. Left cluster: home icon button, then search field. Right cluster: text nav links (Premium, Support, Download) at 14px weight 600 in #b3b3b3, vertical divider, 'Install App' link, 'Sign up' ghost button, and 'Log in' green pill. Search field is #1f1f1f with 9999px radius.

### Search Field
**Role:** Global search input

#1f1f1f background, 9999px radius (pill shape), #ffffff at low-opacity placeholder text, 14px SpotifyMixUI. Expands on focus. Left-aligned search icon in #b3b3b3. No visible border; the surface tier difference is the only separator.

### Content Rail Header
**Role:** Section title bar

Section name in #ffffff at 24px weight 700 (SpotifyMixUITitle), right-aligned 'Show all' link in #b3b3b3 at 14px weight 700. 12px vertical padding above the rail content. No background or border.

### Horizontal Content Rail
**Role:** Scrollable card row

Flex row of album or artist cards with 16px column gap. Overflow scrolls horizontally. Cards are fixed-width (albums ~180px, artists ~180px circles) with 6px radius for squares and full circle for portraits. No visible scrollbar.

### Premium Banner
**Role:** Full-width subscription promotion

Sticky bottom strip with 90deg linear-gradient from #af2896 to #509bf5. Left text block: 'Preview of Spotify' bold white + descriptive copy in white at reduced opacity. Right: 'Sign up free' white pill button at 9999px radius. No border or shadow - the gradient IS the visual weight.

### Language Selector
**Role:** Footer utility control

Ghost pill button at 9999px radius, #ffffff border, globe icon + 'English' label in #ffffff at 14px weight 700. 8px vertical / 12px horizontal padding. Sits in the bottom-left of the sidebar above the premium banner.
