# SVG Path Particle Reveal

Three.js and GSAP-inspired SVG path sampling pattern for turning an SVG path into a premium particle reveal.

Use this when a project needs a moon, eclipse, constellation, logo, route line, product mark, or icon to scatter from depth and assemble into a clean final shape. It works best for cinematic landing pages, loading backdrops, WebGL hero intros, and premium brand moments.

## Source Snippet

The captured code idea is:

```javascript
const path = document.querySelector("path");
const length = path.getTotalLength();
const vertices = [];

for (let i = 0; i < length; i += 0.1) {
  const point = path.getPointAtLength(i);
  const vector = new THREE.Vector3(point.x, -point.y, 0);

  vector.x += (Math.random() - 0.5) * 30;
  vector.y += (Math.random() - 0.5) * 30;
  vector.z += (Math.random() - 0.5) * 70;

  vertices.push(vector);

  tl.from(vector, {
    x: 600 / 2,
    y: -552 / 2,
    z: 0,
    ease: "power2.inOut",
    duration: "random(2, 5)"
  },
  i * 0.002
  );
}
```

## Agent Rules

- Use an owned, generated, open-source-permitted, or user-provided SVG path.
- Normalize the SVG viewBox before placing particles in 3D space. Do not assume `600 / 552` unless the SVG viewBox matches.
- For production Three.js, place sampled points into a `BufferGeometry` and render with `THREE.Points`; do not create one mesh per particle.
- Tune the sampling step for performance. The captured `0.1` step is dense and cinematic, but mobile pages usually need a larger step such as `0.75` to `2`.
- Keep this as a hero, loader, or atmospheric reveal. Do not block important business flows with a long animation.
- Keep readable text and CTAs away from the brightest particle area.
- Provide a static final-shape fallback for `prefers-reduced-motion` and when WebGL is unavailable.

## Files

- `index.html`: dependency-free canvas preview that mirrors the path-sampling choreography without showing code in the visual.
- `pattern.json`: machine-readable selector metadata.
- `verification-notes.md`: QA notes for agents before reuse.
