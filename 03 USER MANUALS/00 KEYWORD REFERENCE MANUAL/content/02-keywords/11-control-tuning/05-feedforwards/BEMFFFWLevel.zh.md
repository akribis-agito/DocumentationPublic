---
keyword: BEMFFFWLevel
summary: 应用于反电动势电压前馈贡献量的百分比级别。
availability:
  standalone: []
  central-i:
  - v5
can_code: 848
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0.0
  - 200.0
  default: 0.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# BEMFFFWLevel

应用于反电动势电压前馈贡献量的百分比级别。

> 从 central-i v5 起可用。

## 概述

`BEMFFFWLevel` 对电压前馈中的反电动势项进行缩放。反电动势电压由电机常数 [BEMFConst](BEMFConst.md) 和实际电机速度计算得出；`BEMFFFWLevel` 是一个百分比，设定该计算电压中实际施加的比例。该参数允许在不更改物理常数的情况下，施加全部建模反电动势电压（100%）、部分电压或不施加。

反电动势项是交轴前馈输出 [VqFFW](VqFFW.md) 的一部分，仅在 [VoltageFFWOn](VoltageFFWOn.md) 启用电压前馈时才生效。

## 工作原理

`BEMFFFWLevel` 的单位为百分比（%）。反电动势前馈电压为建模反电动势（由 [BEMFConst](BEMFConst.md) 和实际电机速度计算）乘以 `BEMFFFWLevel`/100：

- `0` — 无反电动势前馈（默认）；
- `100` — 施加全部建模反电动势电压；
- 最大值以内的其他值允许对建模项进行过补偿或欠补偿。

有效范围为 0 至 200（%），默认值为 0。`BEMFFFWLevel` 为闪存存储参数，可在电机使能或运动中设置；更改在下一个控制周期生效。当 `BEMFFFWLevel` 或 [BEMFConst](BEMFConst.md) 任一为 0 时，反电动势项为零。

## 示例

```text
ABEMFFFWLevel=100    ; 施加全部建模反电动势电压
ABEMFFFWLevel        ; 读取已配置的级别
ABEMFFFWLevel=0      ; 禁用反电动势前馈项
```

## 另请参阅

- [BEMFConst](BEMFConst.md) — 该级别所缩放的电机反电动势常数
- [VqFFW](VqFFW.md) — 承载反电动势项的 q 轴前馈输出
- [VoltageFFWOn](VoltageFFWOn.md) — 电压前馈的主使能开关
- [RmFFWLevel](RmFFWLevel.md) / [LmFFWLevel](LmFFWLevel.md) — 阻性项和感性项的级别缩放
