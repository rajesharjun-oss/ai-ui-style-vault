# Motion

## Motion Principles

- Motion should feel like film playback, review timelines, and a quiet editing suite.
- Keep transitions cinematic and restrained.
- Avoid bouncy, playful, or colorful animation.

## Suggested Patterns

| Pattern | Timing | Use |
|---|---:|---|
| Product frame reveal | `500ms ease` | Hero mockup entrance |
| Gradient drift | `18s to 30s linear infinite` | Slow atmospheric background movement |
| Play button pulse | `2.4s ease-in-out infinite` | Video showcase focus |
| Pill hover | `140ms ease` | CTA invert or underline |
| Feature icon fade | `240ms ease` | Feature grid reveal |

## CSS Sketch

```css
@keyframes frameio-play-pulse {
  0%, 100% { opacity: 0.55; transform: scale(0.98); }
  50% { opacity: 0.9; transform: scale(1.04); }
}
```

