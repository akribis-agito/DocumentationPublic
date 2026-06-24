---
summary: 紧急停止时使用的 CNC 路径减速度。
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# CNCAEmrgDec/CNCBEmrgDec

紧急停止时使用的 CNC 路径减速度。

## 概述

`CNCAEmrgDec`（以及第二个 CNC 组上的 `CNCBEmrgDec`）是触发**紧急停止**时 CNC 路径速度曲线所使用的减速度，单位为用户单位每秒平方。通常将其设置为大于每段减速度，以便快速将路径制动至静止。该参数为非轴参数，可在任何时候设置。

当组内任意成员轴到达行程限位时触发紧急停止：硬件反向/正向限位开关，或软件位置限位（`RevPLim`/`FwdPLim`）。

## 工作原理

当成员轴在组运动过程中触碰限位时，控制器向整个组请求沿路径停止，并将路径速度曲线从正常减速度 [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md) 切换为 `CNCAEmrgDec` 以完成制动。由于所有成员轴共享同一路径速度，各成员轴沿路径同步制动，在停止过程中保持几何形状不变。

有效紧急减速度按实时时间缩放因子 [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) 的平方进行缩放，与正常减速度的缩放方式相同：有效减速度 = `CNCAEmrgDec × (CNCAPercents/100)²`。

停止过程也在成员轴上可见：

- [MotionStat](../05-motion-status/MotionStat.md) 在停止期间显示结束状态（组 A 为位 12，组 B 为位 15）。
- [MotionReason](../05-motion-status/MotionReason.md) 记录原因：组 A 为 `23`（成员触碰硬件限位开关）或 `24`（成员触碰软件位置限位）；组 B 分别为 `26` 或 `27`。

### CNCB 说明

`CNCBEmrgDec` 是独立的第二个 CNC 组的相同紧急停止减速度。

## 示例

```text
ACNCAEmrgDec=2000000 ; 组 A 的紧急停止路径减速度
ACNCBEmrgDec=2000000 ; 组 B 的紧急停止路径减速度
```

## 另请参阅

- [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md) — 正常活动段减速度
- [StopCNCA](StopCNCA.md) / [StopCNCB](StopCNCB.md) — 请求受控停止组
- [MotionReason](../05-motion-status/MotionReason.md) — 限位触发停止的代码 23/24（组 A）、26/27（组 B）
- [MotionStat](../05-motion-status/MotionStat.md) — 组结束位 12（A）/ 15（B）
