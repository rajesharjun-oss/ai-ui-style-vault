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