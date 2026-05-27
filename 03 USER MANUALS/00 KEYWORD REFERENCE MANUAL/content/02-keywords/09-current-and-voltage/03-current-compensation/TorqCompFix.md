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

## How it works

When [TorqCompMode](TorqCompMode.md) is set to a fixed-value mode (1 to 5), the firmware adds `TorqCompFix[TorqCompMode]` to the current reference in the position/velocity control loop — the value is selected by indexing this array directly with the mode number. The term is added to [CurrRef](../02-motor-variables/CurrRef.md) right after it is formed from the velocity-PI output, so it acts as a constant current-reference bias in velocity or position mode.

The array is dimensioned so that index `1` through `5` map to the five fixed-value modes; the array is 1-indexed (index `0` is not used as a compensation source). Values are in the same units as the current reference, and are bounded to the keyword's range. On central-i v5 the values are floating-point; on v4 they are integer.

## Examples

```text
ATorqCompFix[1]=200  ; fixed compensation used when TorqCompMode=1
ATorqCompFix[2]=-150 ; fixed compensation used when TorqCompMode=2
```

## See also

- [TorqCompMode](TorqCompMode.md) — selects which TorqCompFix entry is used
- [OperationMode](../../08-axis-operation/01-general-keywords/OperationMode.md) — must be 2 or 3 for this to apply
