---
summary: 设置为 1 时，将 CNC 步进模式推进至下一段。
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# CNCADoStep/CNCBDoStep

设置为 1 时，将 CNC 步进模式推进至下一段。

## 概述

`CNCADoStep`（以及第二个 CNC 引擎上的 `CNCBDoStep`）在 CNC 引擎以步进模式运行时释放下一段。它是 [CNCAStepMode/CNCBStepMode](CNCAStepMode-CNCBStepMode.md) 的配套关键字：当 CNCA 路径激活且步进模式开启（`CNCAStepMode = 1`）时，引擎在每段结束时暂停，设置 `CNCADoStep = 1` 将指示引擎执行恰好一段。该参数作用于整个 CNC 引擎（而非单个成员轴），不保存至闪存，可在任何时候写入，包括运动过程中。

在步进模式之外，该值无效——无论 `CNCADoStep` 为何值，引擎均连续运行。该关键字仅接受 `0` 和 `1`。

## 工作原理

在步进模式下，引擎在当前段结束时查询 `CNCADoStep`。若为 `1`，引擎执行下一段；若为 `0`，引擎等待，不沿路径继续前进。引擎响应请求后——只在当前段完成后发生——会自动将 `CNCADoStep` 清零为 `0`。这种自清零特性使每次写入仅释放*一段*：当下一段结束时，标志已复位为 `0`，控制器无法连续执行超过一段。

当 CNCA 路径启动（`Begin` 指令）时，`CNCADoStep` 根据步进模式状态预置，以保证第一段行为的一致性：

- 若 `CNCAStepMode` 为 `0`，`CNCADoStep` 清零为 `0`，以备在运动过程中切换为步进模式时使用。
- 若 `CNCAStepMode` 为 `1`，`CNCADoStep` 置为 `1`，从而在引擎暂停并等待下次释放之前执行第一段。

## 示例

```text
ACNCADoStep=1        ; 在步进模式下释放下一段
```

逐段执行路径的方法：设置 `ACNCAStepMode=1`，启动运动，然后对每个需要推进的段写入 `ACNCADoStep=1`。

## 另请参阅

- [CNCAStepMode/CNCBStepMode](CNCAStepMode-CNCBStepMode.md) — 启用 CNC 步进模式
- [CNCAPause/CNCBPause](CNCAPause-CNCBPause.md) — 沿路径暂停/恢复，而非逐段步进
- [StopCNCA](StopCNCA.md) — 停止 CNC 运动（强制关闭步进模式）
