---
keyword: TorqCompMode
summary: Selects the source of the loop's current (torque) compensation in velocity/position mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 391
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
  - -1
  - 5
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# TorqCompMode

Selects the source of the loop's current (torque) compensation in velocity/position mode.

## Overview

`TorqCompMode` selects the source of the loop's current compensation. It is only applicable when [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) = 2 or 3 (velocity or position operation mode). When set to a fixed source it draws from the corresponding [TorqCompFix](TorqCompFix.md) entry; when set to 0 it uses an analog input. See [Control tuning – Feedforwards](../../11-control-tuning/05-feedforwards/00-overview.md) for the location of this compensation in the block diagram.

## How it works

| TorqCompMode | Current compensation value |
|----|----|
| -1 | 0 (no compensation) |
| 0 | Value from an analog input (see [AInMode](../../05-inputs-outputs/02-analog-inputs/AInMode.md), torque-compensation selection). |
| 1 | TorqCompFix[1] |
| 2 | TorqCompFix[2] |
| 3 | TorqCompFix[3] |
| 4 | TorqCompFix[4] |
| 5 | TorqCompFix[5] |

## Examples

```text
ATorqCompMode=-1     ; no compensation (default)
ATorqCompMode=1      ; use TorqCompFix[1]
ATorqCompMode=0      ; use analog-input torque compensation
```

## See also

- [TorqCompFix](TorqCompFix.md) — fixed compensation values selected by this mode
- [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) — must be 2 or 3 for this to apply
- [AInMode](../../05-inputs-outputs/02-analog-inputs/AInMode.md) — analog-input torque-compensation source
