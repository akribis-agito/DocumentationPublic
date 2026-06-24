---
keyword: CompFiltTble
summary: 补偿表，存储各均匀间隔表位置处的期望力。
availability:
  standalone: []
  central-i:
  - v5
can_code: 836
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 64
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CompFiltTble

补偿表，存储各均匀间隔表位置处的期望力。

## 概述

`CompFiltTble` 是补偿滤波器的数据数组。每个元素存储轴处于对应表位置时控制器应期望的力值。当使用 [CompFiltOn](CompFiltOn.md) 启用滤波器时，每个控制周期都会读取该表以从当前位置预测力，互补滤波器再将其与测量力融合（参见 [00-overview](00-overview.md)）。

该关键字从 v5（Central-i v5）起可用。

## 工作原理

该表是一个以表格点为索引的一维数组。各点的位置不存储在表中，而是由 [CompTbleInit](CompTbleInit.md)（第一个点的位置）和 [CompTbleGap](CompTbleGap.md)（各点之间的位置间距）单独定义。索引 1 对应第一个点，索引 2 对应沿轴方向再偏移一个间距的下一个点，以此类推。

运行时，控制器将当前位置转换为小数表索引，然后在相邻两个表项之间进行线性插值，以获得期望力。只有索引 1 至 [CompTbleEnd](CompTbleEnd.md) 所设索引范围内的条目参与查表。

该数组为 1-indexed：索引 1 是第一个可用点，最高可用索引为 63。（索引 0 为内部保留，不可访问。）

| 索引 | 元素 |
|----|----|
| 1 | 第一个表位置处的期望力 |
| 2 | 再偏移一个间距处的期望力 |
| ... | ... |
| 63 | 最后一个可用表位置处的期望力 |

## 示例

将期望力写入前三个表格点：

```
ACompFiltTble[1]=0.0
ACompFiltTble[2]=1.5
ACompFiltTble[3]=3.1
```

读回第二个表格点：

```
ACompFiltTble[2]
```

## 另请参阅

- [CompTbleInit](CompTbleInit.md)
- [CompTbleGap](CompTbleGap.md)
- [CompTbleEnd](CompTbleEnd.md)
- [CompFiltOn](CompFiltOn.md)
- [00-overview](00-overview.md)
