# Landing Page Motion Guide

Use this guide when an AI agent is building a professional landing page, marketing site, product launch, portfolio, showroom site, or motion graphics website from the vault.

Motion should clarify the product, create hierarchy, and make the page feel alive. It should not hide content, slow the main task, or become a clone of a reference site.

## Motion Strategy

Choose one primary motion model before implementation.

| Model | Best For | Primary Technique |
|---|---|---|
| Quiet premium | luxury services, finance, B2B, healthcare | short fades, masked reveals, subtle parallax |
| Product story | SaaS, AI tools, web apps, dashboards | scroll-led UI states, sticky feature beats |
| Cinematic media | hospitality, weddings, restaurants, real estate, showrooms | full-bleed image/video hero, controlled transitions |
| Creative studio | portfolios, agencies, launch pages | kinetic type, layered media, playful pointer response |
| Technical motion | developer tools, APIs, dashboards | code/data reveals, timeline panels, precise easing |
| Immersive 3D | hardware, games, spatial products | Three.js/WebGL scene with static fallback |

## Professional Patterns

### 1. Kinetic Hero Type

Use for a landing page that needs a strong first line. Animate text entry once, then settle into a stable readable state.

Build notes:

- Use opacity, translate, scale, mask, clip-path, or blur sparingly.
- Keep the final headline static and readable.
- Do not animate every line forever.
- Respect `prefers-reduced-motion` by showing the final headline immediately.

### 2. Scroll Product Story

Use when the product needs explanation through stages.

Build notes:

- Use one pinned or sticky section at a time.
- Pair each visual state with real explanatory copy.
- Keep scrolling native; do not hijack wheel or touch behavior.
- Provide a static stacked layout on reduced motion.

### 3. Cinematic Media Hero

Use for photo/video-led websites.

Build notes:

- Use full-bleed media with stable hero dimensions.
- Add pause controls when autoplay exists.
- Do not rely on protected reference-site footage.
- Use owned, generated, user-provided, or clearly licensed media.

### 4. Animated Product UI Tour

Use for SaaS, AI tools, and dashboards where visitors need to understand workflow states.

Build notes:

- Prefer real DOM UI components over screenshots when possible.
- Animate state changes slowly enough to understand.
- Make labels and final values readable.
- Pause animation on hover/focus when useful.

### 5. Lottie Illustration System

Use for vector feature illustrations, empty states, and onboarding.

Build notes:

- Use only owned or clearly licensed `.json` or `.lottie` files.
- Keep loops short and purposeful.
- Do not place many looping animations in one viewport.
- Pair animations with text so meaning is not motion-only.

### 6. Rive Interactive Control

Use when animation should respond to user input or product state.

Build notes:

- Mirror every canvas interaction with accessible controls or labels.
- Keep state-machine names aligned to product states.
- Do not make canvas the only navigation surface.

### 7. Three.js Product Stage

Use when 3D inspection or atmosphere is central to the landing page.

Build notes:

- Make the 3D scene a real primary scene, not a tiny decorative card.
- Verify the canvas is nonblank on desktop and mobile.
- Add static poster/fallback content.
- Avoid high-poly or huge texture assets unless the product demands it.

### 8. Microinteraction System

Use on every professional site, even when the page is not motion-heavy.

Build notes:

- Define timing tokens for hover, press, focus, menu, modal, and route changes.
- Prefer transform and opacity.
- Keep form validation and error states fast and calm.
- Do not delay task completion with flourish.

### 9. Stateful UI Interactions

Use for auth cards, dropdowns, expanding menus, tabs, nav indicators, accordions, and other components where motion represents an explicit user state change.

Build notes:

- Do not autoplay login/signup, nav, menu, tab, or form-state transitions.
- Trigger movement only from click, hover, focus, valid scroll position, or a real product event.
- Make every moving state reversible where the user expects it, especially sign-in/create-account panels.
- Click-away, focus-away, or `Esc` should collapse sticky auth expansions after a mode switch.
- Remove source-video labels, tutorial headings, watermarks, and showcase copy before using the component in production.
- Prefer the specific Code Candy folder when the brief asks for premium auth transitions, expanding hover menus, or animated nav indicators: `motion/code-candy-auth-slanted-overlay/`, `motion/code-candy-hover-pill-menu/`, `motion/code-candy-floating-indicator-nav/`, or `motion/code-candy-auth-overlay-slide/`.
- Use motion/code-candy-hover-expanding-login/ when the brief asks for a dramatic neon auth surface that reacts to hover/focus and supports explicit login/signup switching.
- In reduced motion, change state instantly and keep focus order stable.
### 10. Ambient Eclipse Background

Use for a dark, cinematic, night-themed, wellness, sleep, astrology, astronomy, music, photography, luxury, or coming-soon page where a black moon disk and glowing rim can set the atmosphere.

Best options:

- Hero background: best default. Keep the moon full-screen or centered with minimal copy above or beside it.
- Ambient page background: best when the product has a calm/night/premium theme. Dim the glow behind cards or forms.
- Coming soon or waitlist: strong fit. Pair with one clear CTA and short launch copy.
- Login backdrop: strong fit when the auth card remains readable and the moon stays decorative.
- 404 or empty state: strong fit for lost-in-space, night, or quiet recovery pages.
- Loading screen: conditional. Use only when the product theme fits, keep it short, and do not block progress with decoration.
- Section divider: conditional. Use once as a cinematic pause between editorial sections.

Build notes:

- Prefer CSS: black circular disk, white pseudo-element/radial gradient behind it, soft layered `box-shadow`, and gentle opacity/transform keyframes.
- Keep text and CTAs away from the bright rim.
- Do not add GSAP, Three.js, or video unless the scene genuinely needs choreography beyond a simple eclipse loop.
- Support `prefers-reduced-motion` by freezing the moon and removing continuous pulse/drift.

### 11. SVG Path Particle Reveals

Use `motion/svg-path-particle-reveal/` when a moon, eclipse, constellation, logo, route line, product mark, or icon should scatter from depth and assemble into a premium shape.

Build notes:

- Start from an owned, generated, open-source-permitted, or user-provided SVG path.
- Sample with `getTotalLength()` and `getPointAtLength()`, then map the points into a normalized scene.
- In production Three.js, render points with `BufferGeometry` and `THREE.Points`.
- Tune point density by device; the captured `0.1` path step is cinematic but often too dense for mobile.
- Use as a hero reveal, short loader, transition, or ambient brand moment. Do not block forms, checkout, or important task flows.
- Provide a static final-path fallback for `prefers-reduced-motion` and WebGL failure.

### 12. Screenshot-Derived UI Motion Entries

Use these local entries when a site or app needs reusable interaction patterns from the screenshot library. Treat them as original reconstructions for product UI, not as video clones.

- Use `motion/team-carousel-slider/` for dark editorial people/profile sections. Autoplay is acceptable only with previous, next, pause controls, keyboard access, and reduced-motion fallback.
- Use `motion/modern-timed-destination-cards/` for travel, hospitality, campaign, or editorial heroes where cards promote into a featured stage. Include visible progress, manual card selection, and pause/play.
- Use `motion/responsive-hover-sidebar/` for dashboards and app shells. Labels must reveal on hover, focus, explicit toggle, and mobile; every nav target must be clickable.
- Use `motion/glass-theme-pill-nav/` for compact warm consumer navigation. The active pill moves only after user selection and must recalculate on resize/theme changes.
- Use `motion/animated-delete-button/` for destructive microinteractions. Animate on click only, disable duplicate clicks while pending, and show permanent success only after backend confirmation.
- Keep source-video headings, tutorial labels, watermarks, and visible code panels out of the preview UI. The code belongs in the files and metadata, not inside the design preview.
- Use owned, generated, user-provided, open-source-permitted, or clearly licensed images, icons, and media in production.
## Library Choice

| Need | Prefer |
|---|---|
| Simple hover, reveal, loading, menu, or button states | CSS transitions/keyframes |
| React/Next.js component animation | Motion for React |
| Advanced timeline, scroll scenes, or creative choreography | GSAP |
| Vector illustration animation | LottieFiles/dotLottie |
| Interactive state-machine animation | Rive |
| 3D/WebGL product or environment scenes | Three.js |
| Lightweight JavaScript timelines outside React | Anime.js |

Use the smallest tool that can deliver the motion safely. Do not add a heavy animation library for one opacity transition.

## Timing Tokens

Recommended default timing system:

```css
:root {
  --motion-fast: 120ms;
  --motion-base: 180ms;
  --motion-slow: 320ms;
  --motion-page: 520ms;
  --ease-standard: cubic-bezier(0.2, 0, 0, 1);
  --ease-emphasized: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-entrance: cubic-bezier(0, 0, 0.2, 1);
  --ease-exit: cubic-bezier(0.4, 0, 1, 1);
}
```

Use shorter durations for controls and longer durations for page or hero transitions. Keep easing consistent across the site.

## Reduced Motion Contract

Every motion graphics website must support reduced motion.

Required behavior:

- Stop autoplaying decorative loops.
- Replace scroll-driven pinning with static stacked sections.
- Remove parallax and large translate movements.
- Keep opacity-only fades when helpful and brief.
- Preserve all content and controls.

CSS baseline:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    scroll-behavior: auto !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Performance Rules

- Do not block first paint with large animation assets.
- Lazy-load offscreen animation files.
- Use poster images for video and 3D scenes.
- Avoid layout-thrashing properties such as `top`, `left`, `width`, and `height` in continuous animation.
- Prefer transform and opacity.
- Compress images and videos before using them.
- Test mobile CPU/GPU behavior, not desktop only.

## Agent Workflow

1. Run `scripts/select-vault-style.ps1` for the visual style.
2. Run `scripts/select-motion-references.ps1` for motion direction.
3. Read `motion/motion-catalog.json`, `motion/MOTION_REFERENCES.md`, and this guide.
4. Pick one primary motion model and 2 to 5 patterns.
5. Choose implementation libraries based on the target stack, not trendiness.
6. Implement original motion with owned or licensed assets only.
7. Test desktop, mobile, keyboard, reduced motion, loading, and performance.

## Do

- Use motion to explain hierarchy and product state.
- Keep primary content readable before, during, and after animation.
- Build pause/reduced-motion behavior for autoplay and looping motion.
- Use vault references for pacing, tone, composition, and token logic.
- Keep final UI original and tailored to the target product.

## Do Not

- Do not copy reference-site videos, exact animation sequences, logos, or proprietary layouts.
- Do not hide essential copy inside animation-only states.
- Do not create scroll hijacking or inaccessible canvas-only pages.
- Do not add heavy motion libraries without a clear product reason.
- Do not allow animation to cause layout shift or text overlap.

### 11. Code Candy screenshot-derived auth effect

- Use `motion/code-candy-hover-expanding-login/` for hover/focus auth cards with neon conic-gradient borders and explicit login/signup state switching.
- Treat this as a reconstructed reference from a partial screenshot. Rebuild them as original code in the target app and tune performance, contrast, and reduced motion before shipping.
