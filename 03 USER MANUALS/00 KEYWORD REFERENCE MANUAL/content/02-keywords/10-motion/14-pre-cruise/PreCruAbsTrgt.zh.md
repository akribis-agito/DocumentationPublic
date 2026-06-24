---
keyword: PreCruAbsTrgt
summary: 正弦点到点运动中预巡航目标的绝对位置（用户单位）。
availability:
  standalone: []
  central-i:
  - v5
can_code: 841
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2251799813685248
  - 2251799813685247
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# PreCruAbsTrgt

正弦点到点运动中预巡航目标的绝对位置（用户单位）。

本关键字从 **v5（仅 central-i）** 起可用。

## 概述

`PreCruAbsTrgt` 以用户单位设置**预巡航目标**的绝对位置——轴在到达此点之前以较快的 [PreCruiseSpd](PreCruiseSpd.md) 运行，之后降至正常巡航速度完成运动的其余部分。它适用于正弦点到点模式（[MotionMode](../02-motion-configuration/MotionMode.md) `= 20` 和 `= 21`）；阶段组合概念请参见[预巡航概述](00-overview.md)。

它是 [PreCruRelTrgt](PreCruRelTrgt.md) 的绝对对应量，后者以运动起点的距离表示同一目标点。运动的最终目的地仍由 [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) 设定。

## 工作原理

在正弦点到点模式下发出 [Begin](../04-motion-command/Begin.md) 时，控制器以与解析主目标相同的方式解析预巡航目标：

- 若 [PreCruRelTrgt](PreCruRelTrgt.md) **非零**，预巡航目标取为相对于运动起点的距离，`PreCruAbsTrgt` 在该次运动中被忽略。
- 若 `PreCruRelTrgt` 为 `0`，预巡航目标即为 `PreCruAbsTrgt`。在取模模式（[ModRev](../../03-encoder/04-modulo-mode/ModRev.md)、[ModShort](../../03-encoder/04-modulo-mode/ModShort.md)）下，绝对目标与主绝对目标一样被调整至有效参考帧内。

从运动起点到此目标的距离为**预巡航行程**。仅当预巡航速度高于巡航速度且已定义预巡航行程时，才会执行预巡航阶段；否则运动为普通正弦点到点曲线。控制器在 `Begin` 时验证几何条件，若条件不满足则拒绝运动：

| 条件 | 失败时的效果 |
|---|---|
| 预巡航目标与最终目标方向相同 | 被拒绝——总行程与预巡航行程必须方向相同（错误 381） |
| 最终目标超过预巡航目标 | 被拒绝——总行程必须长于预巡航行程（错误 383） |
| 预巡航行程足以从静止加速至巡航速度 | 被拒绝——预巡航行程不足（错误 384） |
| 预巡航目标之后的剩余行程足以从巡航速度减速至静止 | 被拒绝——制动行程不足（错误 385） |

## 示例

快速运行至位置 200000，然后以较平稳的速度巡航至最终目标 500000：

```text
AMotionMode=20         ; sine point-to-point
ASpeed=300000          ; cruise speed (used after pre-cruise)
APreCruiseSpd=800000   ; faster pre-cruise speed
APreCruRelTrgt=0       ; use the absolute pre-cruise target below
APreCruAbsTrgt=200000  ; run fast up to here
AAbsTrgt=500000        ; final destination
ABegin                 ; start the move
APreCruAbsTrgt         ; read back the pre-cruise target
```

## 另请参阅

- [PreCruRelTrgt](PreCruRelTrgt.md) — 以运动起点距离表示的同一目标
- [PreCruiseSpd](PreCruiseSpd.md) — 预巡航行程中保持的速度
- [预巡航概述](00-overview.md) — 各阶段的组合方式
- [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md) / [RelTrgt](../13-motion-mode-ptp/RelTrgt.md) — 运动的最终目标
- [MotionMode](../02-motion-configuration/MotionMode.md) — 模式 20 和 21 选择正弦点到点运动
- [Begin](../04-motion-command/Begin.md) — 验证并启动运动
