---
keyword: CompTbleCrrct
summary: 每单元接触点修正值，沿位置轴平移补偿表。
availability:
  standalone: []
  central-i:
  - v5
can_code: 840
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
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
# CompTbleCrrct

每单元接触点修正值，沿位置轴平移补偿表。

## 概述

补偿表通常在参考单元上进行一次标定，但各物理单元的实际接触位置可能略有不同。`CompTbleCrrct` 允许控制器平移整个表，使其与当前单元的接触点对齐，而无需重新测量 [CompFiltTble](CompFiltTble.md) 中的力值。

该关键字从 v5（Central-i v5）起可用。

## 工作原理

该关键字存储两个接触点位置，单位为主编码器计数。每个控制周期，控制器在查表前将两者之差叠加到测量位置上，等效于将整个表平移相同的量。所施加的平移量为建表时记录的接触点减去当前单元的实际接触点。

该数组为 1-indexed：索引 1 和索引 2 为可用元素（索引 0 为内部保留，不可访问）。

| 索引 | 元素 |
|----|----|
| 1 | 建表时记录的接触点位置 |
| 2 | 当前单元的实际接触点位置 |

两个元素的默认值均为 0，即不产生平移。

## 示例

记录参考接触点和当前单元的接触点：

```
ACompTbleCrrct[1]=10000
ACompTbleCrrct[2]=10120
```

读回当前单元的接触点：

```
ACompTbleCrrct[2]
```

## 另请参阅

- [CompTbleInit](CompTbleInit.md)
- [CompFiltTble](CompFiltTble.md)
- [CompFiltOn](CompFiltOn.md)
- [Pos](../../10-motion/01-kinematics-status/Pos.md)
