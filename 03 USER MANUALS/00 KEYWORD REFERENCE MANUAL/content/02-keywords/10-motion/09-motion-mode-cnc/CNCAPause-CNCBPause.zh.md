---
summary: 设置为 1 时暂停 CNC 运动（减速至零矢量速度）。
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# CNCAPause/CNCBPause

设置为 1 时暂停 CNC 运动（减速至零矢量速度）。

## 概述

`CNCAPause`（以及第二 CNC 引擎上的对应参数 `CNCBPause`）在不结束运动或干扰已入队段的情况下临时保持 CNC 路径。这相当于暂停零件程序：刀具沿编程路径减速至停止，然后从完全相同的位置恢复。该参数适用于整个 CNC 引擎（而非单个成员轴），不保存至闪存，可随时写入，包括运动期间。

该关键字仅接受两个值：

| 值 | 含义 |
|----|----|
| 0（默认） | 正常运行。若路径已暂停，引擎加速回到活动段的所需矢量速度并继续沿路径运行。 |
| 1 | 暂停——指令路径（矢量）速度被强制为零，运动沿路径减速至静止并等待。 |

这与 [StopCNCA](StopCNCA.md) 不同，后者会中止运动：暂停保留运动及其队列以便恢复，而停止则结束运动。

## 工作原理

CNC 引擎在每个控制周期计算路径曲线时读取 `CNCAPause`。当标志为 `1` 时，沿路径的指令矢量速度保持为零，引擎使用活动段的减速度斜降，组在路径上停止。内部暂停产生与待处理停止请求相同的零速度指令，但可保持：当 `CNCAPause` 恢复为 `0` 时，指令速度恢复为活动段的所需矢量速度（经配置的速度因子——参见 [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) 和 [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md)），引擎加速并继续运行。由于目标和队列保持不变，所有成员轴在恢复后继续运动至原始终点。

与步进模式不同，暂停不在段边界停止——它在标志被设置时路径所在的任意位置停止。引擎不会自动清除 `CNCAPause`：它保持上次写入的值，因此请记得将其重置为 `0` 以恢复运动。CNCA 路径活动期间，轴通过 [MotionStat](../05-motion-status/MotionStat.md) 报告该状态（CNCA 为位 11 / 掩码 `0x800`，CNCB 为位 14 / 掩码 `0x4000`）。

## 示例

```text
ACNCAPause=1         ; 暂停：沿路径减速至零矢量速度
ACNCAPause=0         ; 恢复：加速回到活动段的矢量速度
```

## 另请参阅

- [StopCNCA](StopCNCA.md) — 终止（而非暂停）队列 A 的 CNC 运动
- [CNCAStepMode/CNCBStepMode](CNCAStepMode-CNCBStepMode.md) — 每次前进一段路径
- [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) — 暂停后恢复的所需矢量速度
- [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) — 实时速度/加速度缩放
- [MotionStat](../05-motion-status/MotionStat.md) — 报告活动的 CNCA/CNCB 运动（位 11 和 14）
