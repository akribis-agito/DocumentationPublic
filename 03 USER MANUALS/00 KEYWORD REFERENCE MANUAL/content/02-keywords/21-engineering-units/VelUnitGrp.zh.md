---
keyword: VelUnitGrp
summary: 只读列表，列出属于速度单位组的关键字。
availability:
  standalone: []
  central-i:
  - v5
can_code: 805
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 17
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
# VelUnitGrp

只读列表，列出属于速度单位组的关键字。

## 概述

`VelUnitGrp` 报告哪些关键字构成全局工程单位功能的**速度**单位组。这些关键字的值在通过 [VelUnitFct](VelUnitFct.md) 和 [VelUnitUnt](VelUnitUnt.md) 更改速度工程单位时统一重新解释。该列表由固件固定；读取它可确认速度单位更改影响的确切关键字。

本关键字仅适用于 central-i v5 及以上版本。

## 工作原理

`VelUnitGrp` 是一个只读非轴数组。固件将速度组成员关键字的标识填入其中；每个元素标识一个成员关键字。数组从 1 开始索引：元素 [1] 为第一个成员，元素 [0] 为保留项，不可使用。

速度组包含以下关键字：

| 索引 | 成员关键字 |
|---|---|
| 1 | Vel |
| 2 | VelErr |
| 3 | VelRef |
| 4 | MaxVel |
| 5 | MaxVelErr |
| 6 | InjectVelAmp |
| 7 | Speed |
| 8 | dPosRef |
| 9 | DualStuckVel |
| 10 | InTargetVelTh |
| 11 | SpeedChgNew |
| 12 | AutoGVelTh |
| 13 | MaxVelErrOL |
| 14 | RetractSpeed |
| 15 | FIFOPosVelOf |
| 16 | StuckVel |

最高可用索引比数组大小小 1。

## 示例

```text
AVelUnitGrp[1]      ; 读取速度单位组的第一个成员
AVelUnitGrp[7]      ; 读取索引 7 处的成员
```

## 另请参阅

- [00-overview](00-overview.md) — 组 / 因子 / 单位模型
- [VelUnitFct](VelUnitFct.md) — 速度比例因子
- [VelUnitUnt](VelUnitUnt.md) — 速度单位标签
- [UserUnitsEn](UserUnitsEn.md) — 主使能
- [PosUnitGrp](PosUnitGrp.md) · [AccUnitGrp](AccUnitGrp.md) · [FrcUnitGrp](FrcUnitGrp.md) — 其他量的组
