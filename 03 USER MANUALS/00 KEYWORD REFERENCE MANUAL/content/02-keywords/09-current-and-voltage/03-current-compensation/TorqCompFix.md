---
keyword: TorqCompFix
summary: User-defined array of fixed loop current-compensation values, selected by TorqCompMode.
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
---
# TorqCompFix

User-defined array of fixed loop current-compensation values, selected by TorqCompMode.

## Overview

`TorqCompFix` is a user-defined array of fixed values for the loop's current compensation. The entry used depends on the [TorqCompMode](TorqCompMode.md) value (mode 1 selects `TorqCompFix[1]`, mode 2 selects `TorqCompFix[2]`, and so on). It is only applicable when [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) = 2 or 3 (velocity or position operation mode) and [TorqCompMode](TorqCompMode.md) is 1 to 5.

## Examples

```text
ATorqCompFix[1]=200  ; fixed compensation used when TorqCompMode=1
ATorqCompFix[2]=-150 ; fixed compensation used when TorqCompMode=2
```

## See also

- [TorqCompMode](TorqCompMode.md) — selects which TorqCompFix entry is used
- [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) — must be 2 or 3 for this to apply
