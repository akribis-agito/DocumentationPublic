---
keyword: CompTbleEnd
summary: 当前使用的最高补偿表索引，限定表域范围。
availability:
  standalone: []
  central-i:
  - v5
can_code: 839
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 2
  - 63
  default: 2
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CompTbleEnd

当前使用的最高补偿表索引，限定表域范围。

## 概述

[CompFiltTble](CompFiltTble.md) 中的补偿表最多可容纳 63 个点，但某一配置可能只填充其中部分点。`CompTbleEnd` 告知控制器当前使用的最后一个表索引，使超出已填充区域的位置被视为表域之外，不施加补偿。

该关键字从 v5（Central-i v5）起可用。

## 工作原理

每个控制周期，控制器将当前位置转换为小数表索引。仅当该索引不小于 1 且小于 `CompTbleEnd` 时才施加补偿。由于查表时在计算所得索引处与高一位的下一个点之间进行插值，存储在索引 `CompTbleEnd` 处的点用作最后一个插值段的上端点；因此，有效位置域在该点的位置处结束。

该值范围为 2 至 63，默认值为 2。默认值为 2 时，仅索引 1 与 2 之间的段有效。

## 示例

使用表格点 1 至 10（共 9 个插值段）：

```
ACompTbleEnd[1]=10
```

读回已配置的结束索引：

```
ACompTbleEnd[1]
```

## 另请参阅

- [CompTbleInit](CompTbleInit.md)
- [CompTbleGap](CompTbleGap.md)
- [CompFiltTble](CompFiltTble.md)
- [CompFiltOn](CompFiltOn.md)
