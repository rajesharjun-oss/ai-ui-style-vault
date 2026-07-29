# Motion

## Motion Principles

- Motion should imply live market infrastructure, not a playful marketing carousel.
- Prefer slow glow pulses, subtle data movement, terminal cursor blink, and gentle card elevation.
- Avoid large page-wide animation or constantly shifting backgrounds behind important data.

## Suggested Patterns

| Pattern | Timing | Use |
|---|---:|---|
| Map node pulse | `2.6s ease-in-out infinite` | Live exchange, liquidity, or region status |
| Ticker drift | `24s to 40s linear infinite` | Market rail movement |
| CTA hover | `160ms ease` | Small lift plus stronger blue glow |
| Card hover | `180ms ease` | Border brightening and faint cyan wash |
| Terminal cursor | `1s steps(2) infinite` | Command-line or API examples |

## CSS Sketch

```css
@keyframes auros-pulse {
  0%, 100% { opacity: 0.55; transform: scale(0.92); }
  50% { opacity: 1; transform: scale(1.08); }
}

@keyframes auros-ticker {
  from { transform: translateX(0); }
  to { transform: translateX(-50%); }
}
```

