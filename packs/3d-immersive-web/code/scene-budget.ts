export interface SceneMetrics { transferBytes: number; visibleTriangles: number; drawCalls: number; maxTextureDimension: number; estimatedGpuMemoryMB: number; averageFrameTimeMs?: number; }
export interface SceneBudget { totalSceneTransferMax: number; visibleTrianglesMax: number; drawCallsMax: number; maxTextureDimension: number; estimatedGpuMemoryMBMax: number; targetFps: number; }
export function exceedsBudget(m: SceneMetrics, b: SceneBudget): string[] {
  const errors: string[] = [];
  if (m.transferBytes > b.totalSceneTransferMax) errors.push("transferBytes");
  if (m.visibleTriangles > b.visibleTrianglesMax) errors.push("visibleTriangles");
  if (m.drawCalls > b.drawCallsMax) errors.push("drawCalls");
  if (m.maxTextureDimension > b.maxTextureDimension) errors.push("maxTextureDimension");
  if (m.estimatedGpuMemoryMB > b.estimatedGpuMemoryMBMax) errors.push("estimatedGpuMemoryMB");
  if (m.averageFrameTimeMs && 1000 / m.averageFrameTimeMs < b.targetFps) errors.push("targetFps");
  return errors;
}
