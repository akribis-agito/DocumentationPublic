---
keyword: ECAMCycCount
summary: 当前 ECAM 凸轮曲线重复循环的只读索引。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 307
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# ECAMCycCount

当前 ECAM 凸轮曲线重复循环的只读索引。

## 概述

`ECAMCycCount` 跟踪 ECAM 运动期间凸轮曲线重复循环的索引。它是一个包含 10 个凸轮曲线的数组，每个曲线对应一个元素。ECAM 运动开始时其值从 `1` 起计，并根据主变量和 [ECAMGap](ECAMGap.md) 的符号递增或递减。通过该值可以追踪 ECAM 在 [ECAMCycles](ECAMCycles.md) 所设定循环中的执行进度。

## 工作原理

当 ECAM 运动开始（[Begin](../04-motion-command/Begin.md)）时，`ECAMCycCount` 针对活动曲线（[ECAMTableNum](ECAMTableNum.md)）被置为 `1`。每当主轴跨越一个循环边界——即从当前循环的重复段移入下一个循环——控制器按主轴运动方向将计数步进一次：

- 当主轴前进越过当前循环末端（`ECAMEndCyc` 边界）时，`ECAMCycCount` 增大。
- 当主轴后退低于当前循环起始（`ECAMStartCyc` 边界）时，`ECAMCycCount` 减小。

主轴*方向*与计数方向的对应关系取决于 [ECAMGap](ECAMGap.md) 的符号，因为负的间距值会反转主轴读数的作用方式。对于双向曲线（`ECAMCycles < 0`），计数因此可能为负，范围为 `-ECAMCycles + 1 … ECAMCycles`；对于仅正向曲线（`ECAMCycles > 0`），范围为 `1 … ECAMCycles`。在无限循环模式下，每次主轴窗口滚动时计数持续步进。

尽管该关键字以数组形式存储（每个曲线对应一个计数），但在运动过程中只有活动曲线的计数会递进。其值不保存至闪存，因此每次启动时都会重置。

## 示例

```text
AECAMCycCount[1]    ; 读取凸轮曲线 1 的当前循环索引
```

有关更多信息，请参阅 [运动模式——电子凸轮（ECAM）](00-overview.md) 中的图示。

## 另请参阅

- [ECAMCycles](ECAMCycles.md) — 曲线重复次数
- [ECAMGap](ECAMGap.md) — 其符号决定递增/递减方向
- [ECAMTableNum](ECAMTableNum.md) — 选择活动凸轮曲线
