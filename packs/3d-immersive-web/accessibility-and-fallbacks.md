# Accessibility and Fallback Standard

A canvas is never the only interface. Keep headings, copy, links, forms, status and primary actions in semantic DOM.

Design the fallback first: complete DOM experience, responsive stills, optional controlled video/image sequence, lightweight viewer, then full real-time scene.

Every hotspot has a DOM control/list counterpart. Keyboard and pointer selection share state. Camera motion pauses or shortens while users read or use forms. Dialogs, fullscreen and XR restore focus.

Reduced motion disables scroll camera travel, parallax, particles, auto-rotation and decorative loops while retaining selection and feedback. Check WebGL/WebGPU, reduced motion, save-data, capability hints and measured sustained frame time before heavy downloads.

Implement loading phases, unsupported, low-power, model/texture/shader error, context loss/restoration and a first-class fallback. Test keyboard, high zoom, mobile touch, slow network, WebGL disabled and XR unsupported.
