---
keyword: AccUnitGrp
summary: 属于加速度单位组的关键字的只读列表。
availability:
  standalone: []
  central-i:
  - v5
can_code: 808
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 8
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1023
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# AccUnitGrp

属于加速度单位组的关键字的只读列表。

## 概述

`AccUnitGrp` 报告哪些关键字构成全局工程单位功能的**加速度**单位组。当通过 [AccUnitFct](AccUnitFct.md) 和 [AccUnitUnt](AccUnitUnt.md) 更改加速度工程单位时，这些与加速度相关的关键字的值将被统一重新解释。列表由固件固定；读取该关键字可以确认加速度单位变更具体影响哪些关键字。

该关键字仅在 central-i v5 中可用。

## 工作原理

`AccUnitGrp` 是只读的非轴数组。固件以加速度组成员关键字的标识填充该数组；每个元素标识一个成员关键字。数组采用 1-indexed：元素 [1] 为第一个成员，元素 [0] 为保留项，不使用。

加速度组包含以下关键字：

| 索引 | 成员关键字 |
|---|---|
| 1 | MaxAcc |
| 2 | Accel |
| 3 | Decel |
| 4 | EmrgDec |
| 5 | AutoGAccTh |
| 6 | JerkInAcc |
| 7 | JerkInDec |

最高可用索引比数组大小小 1。

## 示例

```text
AAccUnitGrp[1]      ; read the first member of the acceleration unit group
AAccUnitGrp[3]      ; read the member at index 3
```

## 另请参见

- [00-overview](00-overview.md) — 组 / 因子 / 单位模型
- [AccUnitFct](AccUnitFct.md) — 加速度缩放因子
- [AccUnitUnt](AccUnitUnt.md) — 加速度单位标签
- [UserUnitsEn](UserUnitsEn.md) — 主使能
- [PosUnitGrp](PosUnitGrp.md) · [VelUnitGrp](VelUnitGrp.md) · [FrcUnitGrp](FrcUnitGrp.md) — 其他物理量组
