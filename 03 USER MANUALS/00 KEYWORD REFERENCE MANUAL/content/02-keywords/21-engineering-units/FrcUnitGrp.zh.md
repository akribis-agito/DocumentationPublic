---
keyword: FrcUnitGrp
summary: 属于力单位组的关键字的只读列表。
availability:
  standalone: []
  central-i:
  - v5
can_code: 811
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 9
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
# FrcUnitGrp

属于力单位组的关键字的只读列表。

## 概述

`FrcUnitGrp` 报告哪些关键字构成全局工程单位功能的**力**单位组。当通过 [FrcUnitFct](FrcUnitFct.md) 和 [FrcUnitUnt](FrcUnitUnt.md) 更改力工程单位时，这些与力相关的关键字的值将被统一重新解释。列表由固件固定；读取该关键字可以确认力单位变更具体影响哪些关键字。

该关键字仅在 central-i v5 中可用。

## 工作原理

`FrcUnitGrp` 是只读的非轴数组。固件以力组成员关键字的标识填充该数组；每个元素标识一个成员关键字。数组采用 1-indexed：元素 [1] 为第一个成员，元素 [0] 为保留项，不使用。

力组包含以下关键字：

| 索引 | 成员关键字 |
|---|---|
| 1 | ForceCmdVal |
| 2 | ForceRef |
| 3 | Force |
| 4 | ForceErr |
| 5 | MaxForceErr |
| 6 | ForceAInTh |
| 7 | ForceInTTol |
| 8 | MaxForceErrOL |

最高可用索引比数组大小小 1。

## 示例

```text
AFrcUnitGrp[1]      ; read the first member of the force unit group
AFrcUnitGrp[3]      ; read the member at index 3
```

## 另请参见

- [00-overview](00-overview.md) — 组 / 因子 / 单位模型
- [FrcUnitFct](FrcUnitFct.md) — 力缩放因子
- [FrcUnitUnt](FrcUnitUnt.md) — 力单位标签
- [UserUnitsEn](UserUnitsEn.md) — 主使能
- [PosUnitGrp](PosUnitGrp.md) · [VelUnitGrp](VelUnitGrp.md) · [AccUnitGrp](AccUnitGrp.md) — 其他物理量组
