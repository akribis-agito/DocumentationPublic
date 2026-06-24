---
keyword: TorqCompFix
summary: 用户自定义的固定环路电流补偿值数组，由 TorqCompMode 选择。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 390
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -5000
  - 5000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# TorqCompFix

用户自定义的固定环路电流补偿值数组，由 TorqCompMode 选择。

## 概述

`TorqCompFix` 是用于环路电流补偿的用户自定义固定值数组。所使用的条目取决于 [TorqCompMode](TorqCompMode.md) 的值（模式 1 选择 `TorqCompFix[1]`，模式 2 选择 `TorqCompFix[2]`，依此类推）。仅当 [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) = 2 或 3（速度或位置运行模式）且 [TorqCompMode](TorqCompMode.md) 为 1 至 5 时适用。

## 工作原理

当 [TorqCompMode](TorqCompMode.md) 设置为某个固定值模式（1 至 5）时，固件会在位置/速度控制环中将 `TorqCompFix[TorqCompMode]` 加到电流参考上——该值通过直接以模式编号索引此数组来选择。该项在电流参考由速度 PI 输出形成之后立即加到 [CurrRef](../02-motor-variables/CurrRef.md) 上，因此它在速度或位置模式下充当电流参考的恒定偏置。

数组维度使得索引 `1` 至 `5` 对应五种固定值模式；该数组为 1 索引（索引 `0` 不用作补偿源）。其值与电流参考采用相同单位，并受该关键字的范围限定。在 central-i v5 上其值为浮点数；在 v4 上为整数。

## 示例

```text
ATorqCompFix[1]=200  ; fixed compensation used when TorqCompMode=1
ATorqCompFix[2]=-150 ; fixed compensation used when TorqCompMode=2
```

## 另请参阅

- [TorqCompMode](TorqCompMode.md) — 选择使用哪个 TorqCompFix 条目
- [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) — 须为 2 或 3 时本项才适用
- [CurrRefOffset](CurrRefOffset.md) — 电流侧偏置（在链路中施加的位置晚于此环路侧补偿）
- [CurrRef](../02-motor-variables/CurrRef.md) — 所选条目偏置的电流参考
