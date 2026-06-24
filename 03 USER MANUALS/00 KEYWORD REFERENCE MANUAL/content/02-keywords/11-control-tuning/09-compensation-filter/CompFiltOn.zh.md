---
keyword: CompFiltOn
summary: 启用补偿滤波器，将测量力与位置预测力进行融合。
availability:
  standalone: []
  central-i:
  - v5
can_code: 834
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CompFiltOn

启用补偿滤波器，将测量力与位置预测力进行融合。

## 概述

`CompFiltOn` 控制轴的补偿滤波器的开启或关闭。启用后，控制器不再直接使用原始模拟力反馈值，而是根据补偿表从当前位置预测期望力，再通过互补滤波器将测量力与预测力融合（参见 [00-overview](00-overview.md)）。融合结果作为力控制所使用的力值。

该关键字从 v5（Central-i v5）起可用。

## 工作原理

| 值 | 含义 |
|----|----|
| 0 | 补偿滤波器关闭；力控制直接使用测量力（默认值） |
| 1 | 补偿滤波器开启；测量力与表预测力进行融合 |

当关键字设置为 1 时，滤波器仅在轴位置位于由 [CompTbleInit](CompTbleInit.md)、[CompTbleGap](CompTbleGap.md) 和 [CompTbleEnd](CompTbleEnd.md) 定义的表域范围内时有效。超出该范围后，直接使用测量力，滤波器内部状态被重置，以便下次进入表域范围时能够干净地启动。

互补滤波器的截止频率由 [CompFiltFreq](CompFiltFreq.md) 设置，期望力值由 [CompFiltTble](CompFiltTble.md) 设置，每单位位置偏移由 [CompTbleCrrct](CompTbleCrrct.md) 设置。

## 示例

启用轴的补偿滤波器：

```
ACompFiltOn[1]=1
```

读回当前状态：

```
ACompFiltOn[1]
```

再次禁用：

```
ACompFiltOn[1]=0
```

## 另请参阅

- [CompFiltFreq](CompFiltFreq.md)
- [CompFiltTble](CompFiltTble.md)
- [CompTbleInit](CompTbleInit.md)
- [CompTbleEnd](CompTbleEnd.md)
- [CompTbleGap](CompTbleGap.md)
- [CompTbleCrrct](CompTbleCrrct.md)
- [Force](../../08-axis-operation/04-force-operation-mode/Force.md)
