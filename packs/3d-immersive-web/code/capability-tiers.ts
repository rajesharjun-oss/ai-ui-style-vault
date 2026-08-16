export type ExperienceTier = "static" | "basic-mobile" | "balanced" | "high";
export interface CapabilitySignals { webgl: boolean; webgl2: boolean; webgpu: boolean; reducedMotion: boolean; saveData: boolean; deviceMemoryGB?: number; hardwareConcurrency?: number; width: number; pointer: "coarse" | "fine" | "unknown"; }
export function chooseInitialTier(s: CapabilitySignals): ExperienceTier {
  if (!s.webgl || s.saveData) return "static";
  const mobile = s.pointer === "coarse" || s.width < 768;
  if (mobile && ((s.deviceMemoryGB ?? 4) <= 4 || (s.hardwareConcurrency ?? 4) <= 4)) return "basic-mobile";
  if (!mobile && s.webgl2 && (s.deviceMemoryGB ?? 8) >= 8 && (s.hardwareConcurrency ?? 8) >= 8 && !s.reducedMotion) return "high";
  return mobile ? "basic-mobile" : "balanced";
}
// Use a trusted server for protected content, price, availability and permissions; client tiers are progressive-enhancement hints only.
