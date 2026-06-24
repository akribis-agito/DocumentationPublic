---
keyword: IbErr
summary: 只读的 B 相电流误差（IbRef − Ib），单位为毫安。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 21
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
# IbErr

只读的 B 相电流误差（IbRef − Ib），单位为毫安。

## 概述

`IbErr` 是计算得出的 B 相电流误差，单位为毫安——即 B 相参考 [IbRef](IbRef.md) 与测得 B 相电流 [Ib](Ib.md) 之差。它用于三相 abc 域电流控制（当 [ControlMode](ControlMode.md) 位 1 置位时）以及步进相电流控制。对于单相（有刷）电机，B 相无电流，`IbErr` 保持为 0。

## 工作原理

$$
\text{IbErr}\ \lbrack mA\rbrack\  = \ \text{IbRef}\ \lbrack mA\rbrack\  - \ \text{Ib}\ \lbrack mA\rbrack
$$

在 B 相电流环激活的情况下，`IbErr` 是 B 相 PI 调节器的输入：它由积分增益（[CurrKi](../../11-control-tuning/06-current-control/CurrKi.md)）进行积分，并与由环路增益（[CurrGain](../../11-control-tuning/06-current-control/CurrGain.md)）缩放的比例项求和，以产生 B 相电压指令 [Vb](Vb.md)。对于以 dq0（矢量）模式运行的无刷电机，控制环改为作用于 [IqErr](IqErr.md)/[IdErr](IdErr.md)，而 `IbErr` 仍被计算以供监测。

## 示例

```text
AIbErr              ; read phase B current error (mA)
```

## 另请参阅

- [IbRef](IbRef.md) — B 相电流参考
- [Ib](Ib.md) — 测得 B 相电流
- [IaErr](IaErr.md) — A 相电流误差
- [Vb](Vb.md) — 由该误差经 PI 环产生的 B 相电压指令
