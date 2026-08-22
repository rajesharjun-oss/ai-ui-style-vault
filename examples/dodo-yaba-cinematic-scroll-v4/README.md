# Dodo Yaba Cinematic Scroll V4.2

Reference implementation for the `3d-immersive-web` capability pack.

## What this demonstrates

- pinned scroll-scrub product storytelling;
- one masked canvas coordinate system for dough, sauce, cheese and toppings;
- target-mapped ingredient arrivals constrained to the pizza topping zone;
- inertial scroll interpolation for smoother motion;
- a clean raw-assembly to baked-pizza handoff;
- **standardized live build-your-own pizza canvas** that begins with a cheese base and adds/removes selected toppings;
- the same builder hierarchy used across the main 3D experience and the Classic page in the downloadable build;
- pizza preview on the left, controls on the right;
- curated topping placement with lower density and more even distribution;
- compact topping summary instead of an oversized label;
- size, crust and quick-combo controls with live price updates;
- semantic DOM commerce UI and cart persistence;
- Dodo Yaba business context as a working demonstration rather than a design to clone.

## Run

From this folder:

```bash
python -m http.server 8765
```

Then open `http://localhost:8765/`.

## Asset note

The pizza and ingredient media are generated concept assets for this demonstration, not official Dodo product photography.
