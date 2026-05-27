---
keyword: PosPosTh
summary: Position-feedback threshold used with PosPosFlag to enter position mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 329
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# PosPosTh

Position-feedback threshold used with PosPosFlag to enter position mode.

## Overview

`PosPosTh` is the threshold position feedback (`Pos`) used together with [PosPosFlag](PosPosFlag.md) in the condition check to enter position operation mode. It is used only while the axis is in current or force operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 1 or 4).

## How it works

The comparison direction is selected by [PosPosFlag](PosPosFlag.md):

| PosPosFlag | Descriptions                                                  |
|------------|---------------------------------------------------------------|
| 0          | Axis remains in the existing current or force operation mode. |
| 1          | Axis switches to position operation mode if `Pos` < `PosPosTh`. |
| 2          | Axis switches to position operation mode if `Pos` > `PosPosTh`. |

## Examples

```text
PosPosTh=100000     ; position threshold (user units)
PosPosFlag=1        ; switch when Pos < PosPosTh
```

## See also

- [PosPosFlag](PosPosFlag.md) — selects the comparison direction
- [Current operation mode](../03-current-operation-mode/00-overview.md) — switching from current mode
- [Force operation mode](../04-force-operation-mode/00-overview.md) — switching from force mode
