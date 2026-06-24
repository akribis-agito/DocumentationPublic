---
keyword: PosUnitGrp
summary: 属于位置单位组的关键字只读列表。
availability:
  standalone: []
  central-i:
  - v5
can_code: 802
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 40
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
# PosUnitGrp

属于位置单位组的关键字只读列表。

## 概述

`PosUnitGrp` 报告构成全局工程单位功能中**位置**单位组的关键字。这些与位置相关的关键字，在通过 [PosUnitFct](PosUnitFct.md) 和 [PosUnitUnt](PosUnitUnt.md) 更改位置工程单位时，其值会被统一重新解释。该列表由固件固定；读取它可确认位置单位更改所影响的具体关键字。

此关键字仅在 central-i v5 中可用。

## 工作原理

`PosUnitGrp` 是一个只读的非轴数组。固件用位置组成员关键字的标识填充该数组；每个元素标识一个成员关键字。数组从 1 开始索引：元素 [1] 是第一个成员，元素 [0] 保留且不使用。

位置组包含以下关键字：

| 索引 | 成员关键字 |
|---|---|
| 1 | Pos |
| 2 | PosErr |
| 3 | PosRef |
| 4 | MasterPos |
| 5 | IndexPos |
| 6 | ModRev |
| 7 | RevPLim |
| 8 | FwdPLim |
| 9 | MaxPosErr |
| 10 | InjectPosAmp |
| 11 | AbsTrgt |
| 12 | RelTrgt |
| 13 | SetPosition |
| 14 | PosBeforeMap |
| 15 | AccShapeDist |
| 16 | RefOffsetStep |
| 17 | SchedulePos |
| 18 | InTargetTol |
| 19 | PosPosTh |
| 20 | CurrPosErrTh |
| 21 | SpeedChgPos |
| 22 | Targets |
| 23 | MaxPosErrOL |
| 24 | EncAbsVal |
| 25 | CurrPosTh |
| 26 | ModeSwitchPos |
| 27 | BuffPos |
| 28 | ForcePosErrTh |
| 29 | SpringPLow |
| 30 | SpringPHigh |
| 31 | RetractTarget |
| 32 | GantryFdbk |
| 33 | GantryOffset |
| 34 | FIFOPosTrgt |
| 35 | FIFOPosPosOf |
| 36 | DualEncSwapOn |
| 37 | DualEncRange |
| 38 | SpringTableGp |
| 39 | CompTbleGap |

最高可用索引比数组大小少一。

## 示例

```text
APosUnitGrp[1]      ; read the first member of the position unit group
APosUnitGrp[9]      ; read the member at index 9
```

## 另请参阅

- [00-overview](00-overview.md) — 组 / 系数 / 单位模型
- [PosUnitFct](PosUnitFct.md) — 位置比例系数
- [PosUnitUnt](PosUnitUnt.md) — 位置单位标签
- [UserUnitsEn](UserUnitsEn.md) — 主使能
- [VelUnitGrp](VelUnitGrp.md) · [AccUnitGrp](AccUnitGrp.md) · [FrcUnitGrp](FrcUnitGrp.md) — 其他量的单位组
