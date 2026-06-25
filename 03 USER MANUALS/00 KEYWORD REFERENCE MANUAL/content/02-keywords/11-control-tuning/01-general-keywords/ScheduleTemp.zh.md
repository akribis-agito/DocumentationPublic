---
keyword: ScheduleTemp
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 273
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
  - -20
  - 120
  default: 25
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 基于温度区间的增益调度所用的电机温度阈值数组。
---
# ScheduleTemp

将温度范围划分为若干区间，用于基于温度的增益调度的电机温度阈值。

## 概述

当 [ScheduleMode](ScheduleMode.md) 为 `8`（按温度区间）时，`ScheduleTemp` 保存电机温度区间边界值。值的单位为摄氏度，且必须随数组索引单调递增。

## 工作原理

控制器将测量到的电机温度与各阈值进行比较，并选择对应的增益组：

- 温度 ≤ `ScheduleTemp[1]` 时，选择增益组 1
- `ScheduleTemp[1]` < 温度 ≤ `ScheduleTemp[2]` 时，选择增益组 2
- `ScheduleTemp[2]` < 温度 ≤ `ScheduleTemp[3]` 时，选择增益组 3
- `ScheduleTemp[3]` < 温度 ≤ `ScheduleTemp[4]` 时，选择增益组 4
- 温度 > `ScheduleTemp[4]` 时，选择增益组 5

（`ScheduleTemp[5]` 是数组的组成部分，但不用作上边界——超过第四个阈值的温度均映射到增益组 5。）

## 示例

```text
AScheduleTemp[1]=30; AScheduleTemp[2]=45; AScheduleTemp[3]=60; AScheduleTemp[4]=80
AScheduleMode=8            ; select temperature-band scheduling
```

## 另请参阅

- [ScheduleMode](ScheduleMode.md) — 模式 8 使用这些阈值
- [ScheduleSet](ScheduleSet.md) — 当前选中的区间
- [SchedulePos](SchedulePos.md) / [ScheduleVel](ScheduleVel.md) — 其他区间模式的类似阈值（区间映射示意图见 [ScheduleVel](ScheduleVel.md)）
