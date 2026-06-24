---
keyword: CompTbleGap
summary: 相邻补偿表格点之间的位置间距，单位为编码器计数。
availability:
  standalone: []
  central-i:
  - v5
can_code: 837
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
# CompTbleGap

相邻补偿表格点之间的位置间距，单位为编码器计数。

## 概述

补偿表的各格点沿位置轴均匀分布。`CompTbleGap` 设置相邻两个表格点之间的间距，单位为主编码器计数。与设置第一个点位置的 [CompTbleInit](CompTbleInit.md) 共同决定 [CompFiltTble](CompFiltTble.md) 中每个点的位置。

该关键字从 v5（Central-i v5）起可用。

## 工作原理

为确定当前轴位置对应的表位置，控制器计算当前位置与 [CompTbleInit](CompTbleInit.md) 所设起始点之间的距离，再除以 `CompTbleGap`。商的整数部分确定所在表段，小数部分用于在 [CompFiltTble](CompFiltTble.md) 相邻两个条目之间进行线性插值。

间距越小，格点越密集，在更短的跨度内提供更高的位置分辨率；间距越大，相同数量的格点覆盖更宽的跨度。间距值更改时，其倒数会被预计算，因此更新无需禁用滤波器即可生效。

该值范围为 1 至 2147483647，默认值为 1。

## 示例

将表格点间距设置为 500 计数：

```
ACompTbleGap[1]=500
```

读回已配置的间距：

```
ACompTbleGap[1]
```

## 另请参阅

- [CompTbleInit](CompTbleInit.md)
- [CompTbleEnd](CompTbleEnd.md)
- [CompFiltTble](CompFiltTble.md)
- [00-overview](00-overview.md)
