# Components

### Gradient Primary CTA
**Role:** The hero action - invites the visitor into the documentation.

Filled button with linear-gradient(to right, #3898ff, #7a70ff), white text at 16px SFRounded weight 500, letter-spacing 0.27px. Padding 12px 24px. Radius 9999px (pill). White inset border highlight at rgba(255,255,255,0.12) for edge definition. On elevation: two-layer soft shadow.

### Solid Blue Pill Button
**Role:** Secondary CTAs and persistent nav actions like 'Connect Wallet'.

Background #0e76fd, white text, 16px SFRounded weight 500. Padding 6px 16px. Radius 9999px. Sits in the top-right of the nav. Compact, high-contrast, unmistakable.

### Ghost Nav Button (Logo + Version)
**Role:** Brand identification in the nav bar with version metadata.

Rainbow gradient icon (app-style) followed by 'RainbowKit' text in white at 14px weight 600, with a small version badge (1.3.10) using Pewter background, white text at 11px, radius 9999px, padding 1px 5px.

### Terminal Code Block
**Role:** Copy-paste installation command in the hero.

Dark surface (#1b1c1 or near-black) with a subtle white border. Contains monospace text (SFMono 14px) showing npm command. Includes a small copy-icon button on the right side. Padding ~12px 18px. Radius 12px.

### Wallet Connection Modal
**Role:** The product showcase - the actual RainbowKit component floating on the landing page.

Card at 24px radius, Obsidian surface (#1b1c1e), heavy shadow (rgba(0,0,0,0.4) 0px 8px 24px). Header row with title 'Connect a Wallet' and close X icon. Body has a 'Popular' label, then a list of wallet items (Rainbow, Coinbase Wallet, MetaMask, WalletConnect) with brand icons and right-arrow chevrons. A 'More' section below with Ledger Live. All text white at 16px SFRounded weight 500.

### Wallet List Item
**Role:** Selectable option inside the connection modal.

Row with: circular wallet brand icon (32px), wallet name in white 16px weight 500, optional right chevron. Subtle hover state would lift the row background. Padding ~12px vertical, 16px horizontal.

### What-is-a-Wallet Info Card
**Role:** Educational companion card explaining wallets next to the connection modal.

Same Obsidian surface and shadow as the modal. Contains a heading 'What is a Wallet?' in white 20px, followed by short paragraphs of body text (14-16px) and small inline feature icons. Functions as a secondary educational surface beside the primary action.

### Mobile Preview Card
**Role:** Showcases the wallet UI on a phone frame, demonstrating responsive behavior.

Vertical phone frame with rounded corners, displaying the same 'Connect a Wallet' modal scaled down. Background slightly lighter to separate from the canvas. Acts as a visual product screenshot, not an interactive component.

### Section Heading Block
**Role:** Centered section titles with supporting copy.

Centered text block. Main heading in white 20-24px SFRounded weight 600. Supporting paragraph in Fog (#95979c) 16px weight 400. Generous vertical spacing above and below. Used to introduce the partner grid.

### Partner Logo Grid Item
**Role:** Brand trust marker - a 6xn grid of partner logos.

Circular logo container (radius 9999px) with the brand's actual logo. Below: brand name in white 14px weight 500. Gap between items 40-60px horizontally. No background fill - the logo floats on Void. Logos are full-color brand assets, not monochrome.

### Inset Highlight Border
**Role:** The defining visual signature of interactive elements on dark surfaces.

1px inset border in rgba(255,255,255,0.12) applied to buttons and elevated cards. Creates a subtle lit-edge effect that mimics light catching the top of a physical surface - the only reason buttons read as 'raised' in a fully dark UI.

### Gradient Brand Wordmark
**Role:** The 'RainbowKit' hero title.

Text rendered with the aurora gradient (#3898ff #7a70ff) as a CSS background-clip:text fill, at 40-52px SFRounded weight 700, letter-spacing 1.3px. The gradient is applied to the entire word, not individual letters.
