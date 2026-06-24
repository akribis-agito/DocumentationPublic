---
keyword: AnomDtctGap
summary: 检测器推进之前每个限值表点所跨越的控制周期数，按被监测运动分别设置。
availability:
  standalone: []
  central-i:
  - v5
can_code: 796
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 2147483647
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# AnomDtctGap

检测器推进之前每个限值表点所跨越的控制周期数，按被监测运动分别设置。

## 概述

`AnomDtctGap` 控制检测器在被监测运动期间遍历 [AnomDtctUL](AnomDtctUL.md) / [AnomDtctLL](AnomDtctLL.md) 限值表的速度。每个表点覆盖固定数量的控制周期；`AnomDtctGap` 即为该数量。较大的 gap 将相同数量的表点拉伸到更长的运动上，因此它设定预期分段曲线的时间分辨率。

每个被监测运动有一个 gap 值，因此慢速运动和快速运动可使用不同的分辨率。

该关键字自 v5（central-i）起可用。

## 工作原理

当一个被监测运动处于活动状态时，检测器将当前限值表点保持 `AnomDtctGap` 个控制周期，然后步进到下一个点。滤波信号与分段的比较在每个 gap 窗口开始时进行一次。一旦到达块的最后一个点，检测器将保持在该最后点上，直到运动结束。

该数组是 1-indexed（索引 0 为保留）。每个可用索引对应一个被监测运动：

| 索引 | 被监测运动 |
| --- | --- |
| 1 | 运动 0 |
| 2 | 运动 1 |
| 3 | 运动 2 |
| 4 | 运动 3 |

最小值为 1（每个控制周期推进一次），默认值为 1。每个运动有 256 个点，gap 乘以 256 大致设定曲线跨越多少个控制周期；选取该值以使表覆盖所监测运动的持续时间。

## 示例

```text
AAnomDtctGap[1]=10      ; motion 0: hold each limit point for 10 control cycles
AAnomDtctGap[2]=4       ; motion 1: faster motion, finer time resolution
AAnomDtctGap[1]         ; read the gap for motion 0
```

## 另请参阅

- [AnomDtctUL](AnomDtctUL.md) / [AnomDtctLL](AnomDtctLL.md) — 此值据以推进的限值表
- [AnomDtctCnfg](AnomDtctCnfg.md) — 监测源和运动选择
- [AnomDtctSt](AnomDtctSt.md) — 活动运动和限值
