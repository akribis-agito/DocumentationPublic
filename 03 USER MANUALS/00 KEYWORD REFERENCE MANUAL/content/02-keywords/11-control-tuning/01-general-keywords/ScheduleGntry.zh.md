---
keyword: ScheduleGntry
availability:
  standalone: []
  central-i:
  - v5
can_code: 658
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
summary: 将增益调度与轴的龙门控制状态配对，选择调度作用于标准整定增益还是龙门整定增益。
---
# ScheduleGntry

将增益调度与轴的龙门控制状态配对，选择调度作用于标准整定增益还是龙门整定增益。

## 概述

当一个轴可在龙门（横梁）控制下运行时，它具有两套完整的整定增益：龙门控制关闭时使用的标准增益，以及龙门控制开启时使用的龙门增益。`ScheduleGntry` 告知调度器所配置的调度适用于哪种情况。它是一个轴作用域标志：

| 值 | 调度作用条件 |
|---|---|
| 0 | 龙门控制**关闭**（默认） |
| 1 | 龙门控制**开启** |

## 工作原理

每个调度周期，控制器检查轴当前的龙门控制状态是否与 `ScheduleGntry` 匹配：

- 若 `ScheduleGntry = 0` 且龙门控制关闭，**或** `ScheduleGntry = 1` 且龙门控制开启，则 [ScheduleMode](ScheduleMode.md) 选定的调度规则正常评估并驱动 [ScheduleSet](ScheduleSet.md)。
- 若状态不匹配（例如 `ScheduleGntry = 1` 但龙门控制当前关闭），则调度不生效，使用默认增益组 1。

当龙门控制**开启**时满足匹配条件，[ScheduleGains](ScheduleGains.md) 中的调度增益从龙门整定数组而非标准数组加载；对于基于范围的模式，调度量使用龙门反馈位置或龙门速度。当龙门控制**关闭**时满足匹配条件，使用标准整定数组和标准轴位置/速度。

## 示例

```text
AScheduleGntry=1             ; apply this axis's scheduling while gantry control is on
AScheduleGntry=0             ; apply scheduling while gantry control is off (default)
```

## 另请参阅

- [ScheduleMode](ScheduleMode.md) — 受此配对门控的调度规则
- [ScheduleGains](ScheduleGains.md) — 当前使用的增益（标准或龙门数组）
- [ScheduleSet](ScheduleSet.md) — 激活增益组，当龙门状态不匹配时强制为 1
