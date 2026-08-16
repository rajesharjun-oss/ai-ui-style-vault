# Mobile 3D Guidance

Mobile is a separate art direction and interaction tier: DOM task first, smaller assets, fewer lights/effects, bounded touch controls, guided camera presets and an immediate static/video fallback.

Do not conflict with page scroll. Pause when hidden, offscreen or idle. Limit DPR and downgrade after sustained frame-time problems. Test low/mid-range devices, orientation changes, browser back, interruption/resume, slow 4G, reduced motion and context loss.
