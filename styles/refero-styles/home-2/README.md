# Home

Source: [Refero Style](https://styles.refero.design/style/606d4af9-9d8c-41ea-a122-f515f38f20e5)
Reference site: [https://www.fluidtouch.biz](https://www.fluidtouch.biz)
Captured: 2026-07-30
Refero published: 2026-04-30T03:22:04.669Z
Refero modified: 2026-06-05T12:50:06.304Z
Theme: dark
Category: Productivity

## Style Summary

Explore Home's dark Productivity design system: Hot Magenta #ed1672, Midnight Ink #121318 colors, Poppins, Muli typography, and DESIGN.md for AI agents.

North star: Stargazer's dark observatory

## What To Borrow

- Hot Magenta `#ed1672` for Active nav links, primary CTA fills, decorative accent dots - the only chromatic voice in the system, reserved so each occurrence reads as signal
- Midnight Ink `#121318` for Page canvas, hero background, footer - the deep-space base layer everything floats on
- Deep Space `#191c26` for Elevated card surfaces, section backgrounds one step above canvas
- Slate Edge `#212529` for Hairline borders, image frame rules, subtle structural dividers
- Pure White `#ffffff` for Primary text, headline color, nav links, button text - the only color competing with the magenta accent
- Void Black `#000000` for Supporting palette color for small decorative accents when the core palette needs contrast. Do not promote it to the primary CTA color

- Poppins `--font-poppins` for Display headlines at 700 weight dominate at 110px - the geometric bold reads as monumental and confident, the kind of type that fills a dark page like a billboard. At 400 it's used for nav and small UI labels where it stays unobtrusive.
- Muli `--font-muli` for Body and nav body text. Weight 300 is the signature choice - a humanist sans at near-thin weight against the Poppins 700 display creates a call-and-response rhythm: the headline shouts, the body whispers. Muli's softer curves (vs Poppins' geometric strictness) warm the dark page.

## Avoid

- Don't introduce a second accent color - the entire brand voice is one magenta against monochrome
- Don't apply drop shadows to any element; depth comes from surface lightness steps only
- Don't use Poppins 400 for headlines or Muli 400 for display - weight roles are fixed
- Don't reduce the 110px hero size for 'mobile friendliness' without a deliberate type-scale override
- Don't add border-radius to cards, images, or inputs - only buttons and tags get the 100px pill
- Don't use #ed1672 for body text or small labels - it fails contrast (4.4:1) and the pink must remain large or decorative
- Don't stack multiple saturated elements on one screen - the dark canvas is the brand, keep it 97% achromatic

## Bundle Contents

- [DESIGN.md](DESIGN.md): full source-derived implementation reference.
- [implementation-prompt.md](implementation-prompt.md): ready-to-paste prompt for an AI builder.
- [style.json](style.json): structured style metadata and token summary.
- [tokens/colors.md](tokens/colors.md): palette and surface rules.
- [tokens/typography.md](tokens/typography.md): type scale and font rules.
- [tokens/spacing-shape.md](tokens/spacing-shape.md): spacing and radius rules.
- [tokens/components.md](tokens/components.md): component recipes.
- [tokens/guidelines.md](tokens/guidelines.md): do and do-not guidance.
- [tokens/layout-imagery.md](tokens/layout-imagery.md): layout and imagery direction.
- [code/css-variables.css](code/css-variables.css): CSS variable starter.
- [code/tailwind-v4.css](code/tailwind-v4.css): Tailwind v4 token starter.
- [code/design-tokens.json](code/design-tokens.json): portable token JSON.
- [screenshots/README.md](screenshots/README.md): source media references.
