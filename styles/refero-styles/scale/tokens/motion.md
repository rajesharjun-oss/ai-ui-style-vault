# Motion

## Motion Principles

- Motion should feel like model systems and analytical instrumentation.
- Keep it restrained, precise, and slow.
- Use motion to reveal data, trace wireframes, or focus cards.
- Avoid bouncy consumer animation.

## Suggested Patterns

| Pattern | Timing | Use |
|---|---:|---|
| Wireframe trace | `3s ease-in-out` | Reveal model graph lines in black section |
| Node pulse | `2.4s ease-in-out infinite` | Tiny graph or evaluation status markers |
| Product card hover | `160ms ease` | Border darkening and minimal lift |
| Chart draw | `900ms ease` | First viewport entry for chart lines |
| Nav fade | `180ms ease` | Dark hero navigation transition |

## CSS Sketch

```css
@keyframes scale-node-pulse {
  0%, 100% { opacity: 0.45; transform: scale(0.96); }
  50% { opacity: 1; transform: scale(1.08); }
}
```

