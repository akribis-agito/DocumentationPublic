---
keyword: IaErr
summary: 只读的 A 相电流误差 (IaRef − Ia)，单位为毫安。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 20
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range: null
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# IaErr

只读的 A 相电流误差 (IaRef − Ia)，单位为毫安。

## 概述

`IaErr` 是计算得到的 A 相电流误差，单位为毫安——即 A 相参考 [IaRef](IaRef.md) 与实测 A 相电流 [Ia](Ia.md) 之差。它用于单相（有刷）电机电流控制、三相 abc 域电流控制（当 [ControlMode](ControlMode.md) 位 1 置位时）以及步进电机相电流控制。

## 工作原理

$$
\text{IaErr}\ \lbrack mA\rbrack\  = \ \text{IaRef}\ \lbrack mA\rbrack\  - \ \text{Ia}\ \lbrack mA\rbrack
$$

在 A 相电流环激活时，`IaErr` 是 A 相 PI 调节器的输入：它用积分增益 ([CurrKi](../../11-control-tuning/06-current-control/CurrKi.md)) 进行积分，并与按环路增益 ([CurrGain](../../11-control-tuning/06-current-control/CurrGain.md)) 缩放的比例项相加，从而产生 A 相电压指令 [Va](Va.md)。对于以 dq0（矢量）模式运行的无刷电机，该环路改为作用于 [IqErr](IqErr.md)/[IdErr](IdErr.md)，而 `IaErr` 仍会被计算以供监测。

## 示例

```text
AIaErr              ; read phase A current error (mA)
```

## 另请参阅

- [IaRef](IaRef.md) — A 相电流参考
- [Ia](Ia.md) — 实测 A 相电流
- [IbErr](IbErr.md) — B 相电流误差
- [Va](Va.md) — 由该误差经 PI 环产生的 A 相电压指令
