---
keyword: SchedulePos
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 264
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 2147483647
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
    default: 2251799813685247
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
summary: 将行程划分为若干分段的位置阈值，用于基于位置的增益调度。
---
# SchedulePos

将行程划分为分段的位置阈值，用于基于位置的增益调度。

## 概述

`SchedulePos` 存储当 [ScheduleMode](ScheduleMode.md) 为 `5`（步进，按位置范围）或 `10`（插值，按位置范围）时使用的位置分段边界。数值以用户位置单位表示，且必须随数组索引单调递增。

## 工作原理

控制器将轴位置与阈值比较并选择增益组：

- 若位置 ≤ `SchedulePos[1]`，则为增益组 1
- 若 `SchedulePos[1]` < 位置 ≤ `SchedulePos[2]`，则为增益组 2
- 若 `SchedulePos[2]` < 位置 ≤ `SchedulePos[3]`，则为增益组 3
- 若 `SchedulePos[3]` < 位置 ≤ `SchedulePos[4]`，则为增益组 4
- 若位置 > `SchedulePos[4]`，则为增益组 5

（元素 `SchedulePos[5]` 是数组的一部分，但不用作上边界——高于第四个阈值的任何值均映射至增益组 5。）

在步进模式（`ScheduleMode = 5`）下，增益阶跃至所选增益组。在插值模式（`ScheduleMode = 10`）下，增益在各分段内线性混合而非阶跃；这要求前四个阈值严格递增，否则调度将被禁用，使用增益组 1，[ScheduleSet](ScheduleSet.md) 报告 `-1`。

当轴处于龙门配对调度下时，龙门反馈位置而非轴位置与这些阈值进行比较（参见 [ScheduleGntry](ScheduleGntry.md)）。

## 示例

```text
ASchedulePos[1]=100000; ASchedulePos[2]=200000; ASchedulePos[3]=300000; ASchedulePos[4]=400000
AScheduleMode=5            ; select position-band scheduling
```

## 另请参阅

- [ScheduleMode](ScheduleMode.md) — 模式 5 和 10 使用这些阈值
- [ScheduleSet](ScheduleSet.md) — 当前选定的分段
- [ScheduleVel](ScheduleVel.md) / [ScheduleTemp](ScheduleTemp.md) — 其他范围模式的类似阈值（分段映射图见 [ScheduleVel](ScheduleVel.md)）
