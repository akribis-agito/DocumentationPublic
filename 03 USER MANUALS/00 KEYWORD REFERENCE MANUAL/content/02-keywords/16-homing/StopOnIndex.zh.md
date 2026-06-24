---
keyword: StopOnIndex
summary: 在下一个编码器索引脉冲时自动停止轴运动。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 167
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# StopOnIndex

在下一个编码器索引脉冲时自动停止轴运动。

## 概述

`StopOnIndex` 用于使能索引停止功能。设置为非零值时，下一个编码器索引将使轴停止，适用于参考编码器索引位置的回零过程——参见 [HomingDef](HomingDef.md) 中的"点动至索引"步骤。其工作方式与 [StopOnHome](StopOnHome.md) 类似（`StopOnHome` 在原点数字量输入时停止）。该参数为轴作用域，不保存至闪存，可随时修改。

## 工作原理

`StopOnIndex` 仅在点动或速度控制运动期间由运动规划器进行评估。每个控制周期，若 `StopOnIndex` 为非零值且当前检测到编码器索引（[IndexStat](../03-encoder/02-index-detection/IndexStat-AuxIndexStat.md) 有效），运动规划器将：

1. 置位停止请求位，使运动减速至停止；
2. 将运动结束原因设置为"索引"（由 [MotionReason](../10-motion/05-motion-status/MotionReason.md) 报告，值为 11）；
3. 将 `StopOnIndex` 清零至 `0`。

由于固件会自动清零，`StopOnIndex` 属于一次性使能：读回 `0` 即可确认停止已触发，然后等待 [MotionStat](../10-motion/05-motion-status/MotionStat.md) 显示轴已不再运动。

需注意，置位停止请求位将触发正常减速停止，因此轴在索引位置*之后*经过减速距离后停止——并非精确停在索引处。确切的索引位置由 [IndexPos](../03-encoder/02-index-detection/IndexPos-AuxIndexPos.md) 单独捕获。这也是回零需要两个步骤的原因："点动至索引"步骤使能 `StopOnIndex` 以在索引后不远处停止运动，"移动至索引位置"步骤再执行点到点运动，精确到达记录的 [IndexPos](../03-encoder/02-index-detection/IndexPos-AuxIndexPos.md)。第二步直接以捕获位置为目标，因此不使用 `StopOnIndex`。

## 示例

```text
AStopOnIndex=1       ; 使能在下一个编码器索引时停止
AStopOnIndex        ; 0 = 已禁用 / 已触发，1 = 已使能
```

## 另请参见

- [StopOnHome](StopOnHome.md) — 在原点数字量输入时停止的等效功能
- [IndexStat](../03-encoder/02-index-detection/IndexStat-AuxIndexStat.md) — 该标志所响应的索引检测
- [IndexPos](../03-encoder/02-index-detection/IndexPos-AuxIndexPos.md) — "移动至索引位置"步骤使用的已记录索引位置
- [MotionReason](../10-motion/05-motion-status/MotionReason.md) — 报告"索引"运动结束原因
- [HomingDef](HomingDef.md) — 参考索引的回零步骤
