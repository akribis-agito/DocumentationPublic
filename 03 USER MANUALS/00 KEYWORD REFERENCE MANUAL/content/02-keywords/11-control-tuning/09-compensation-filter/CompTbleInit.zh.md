---
keyword: CompTbleInit
summary: 补偿表第一个点的位置，以编码器计数为单位。
availability:
  standalone: []
  central-i:
  - v5
can_code: 838
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2251799813685248
  - 2251799813685247
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CompTbleInit

补偿表第一个点的位置，以编码器计数为单位。

## 概述

`CompTbleInit` 定义补偿表在位置轴上的起始位置。它是以主编码器计数表示的位置，对应 [CompFiltTble](CompFiltTble.md) 中的表索引 1。与 [CompTbleGap](CompTbleGap.md)（设置各点之间的间距）配合使用，可将每个表索引映射到实际物理位置。

本关键字从 v5（central-i v5）起可用。

## 工作原理

每个控制周期，控制器计算相对于此起始点的位置，除以 [CompTbleGap](CompTbleGap.md) 给出的点间距，并将结果作为 [CompFiltTble](CompFiltTble.md) 的小数索引使用。测量位置等于 `CompTbleInit` 时，映射到第一个表点；低于 `CompTbleInit` 的位置超出表域范围，不施加补偿。

在计算索引之前，位置会先由 [CompTbleCrrct](CompTbleCrrct.md) 的单元接触点校正量进行偏移，因此表的有效起点会跟随当前单元的接触点移动。

该值为有符号 64 位位置，默认值为 0。

## 示例

将表起始位置设置为 10000 计数：

```
ACompTbleInit[1]=10000
```

读回已配置的起始位置：

```
ACompTbleInit[1]
```

## 另请参阅

- [CompTbleGap](CompTbleGap.md)
- [CompTbleEnd](CompTbleEnd.md)
- [CompFiltTble](CompFiltTble.md)
- [CompTbleCrrct](CompTbleCrrct.md)
- [Pos](../../10-motion/01-kinematics-status/Pos.md)
