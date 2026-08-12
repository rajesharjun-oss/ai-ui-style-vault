# TikTok Code Candy Verification Notes

Verified on 2026-08-04.

## Source-video verified

- Ref 1: `7652792918511521046` - Login / Signup Animation
  - Downloaded source clip.
  - Matched visible `.overlay-panel` `clip-path`, `900ms cubic-bezier(.77, 0, .18, 1)`, active `translateX(-100%)`, active polygon, and login form fade/blur behavior.
- Ref 2: `7650285351411420418` - Hover-only pill menu
  - Downloaded source clip.
  - Matched visible `.menu-item`, `.menu-item:hover`, `.menu-label`, `160px` hover width, `999px` radius, `.45s cubic-bezier(.22, 1, .36, 1)`, `rgba(255, 255, 255, 0.12)`, and cyan glow.
- Ref 3: `7666101227729489174` - Click-only navigation bar
  - Downloaded source clip.
  - Matched visible `.nav`, `.indicator`, `#25262b`, `#29fd53`, `63px` indicator, `top: -28px`, `translateY(-40px)`, and `.58s cubic-bezier(.34, 1.45, .64, 1)` movement. Library adaptation starts inactive and waits for click before showing or moving the indicator.
- Ref 4: `7662161881750113538` - Login/signup overlay slide
  - Downloaded source clip.
  - Matched the source composition, then adapted the motion to a clean 2D `translateX(-100%)` overlay slide to prevent rendering artifacts over the create-account form. State changes only on explicit click.

## Limit

The local gallery now matches the code values visible in the video frames. Hidden code that never appears in the clips cannot be guaranteed exact without the original files or a full source link.