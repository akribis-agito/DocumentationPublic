---
keyword: PosPosFlag
summary: Trigger direction for the position-feedback check to enter position mode.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 328
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
  - 0
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# PosPosFlag

Trigger direction for the position-feedback check to enter position mode.

## Overview

`PosPosFlag` defines the trigger direction for the position feedback check (`Pos`) used to switch into position operation mode. It is used only while the axis is in current or force operation mode ([OperationMode](../01-general-keywords/OperationMode.md) = 1 or 4), together with the threshold [PosPosTh](PosPosTh.md). Once the feedback check is fulfilled, `PosPosFlag` is cleared to 0, so the user must reconfigure its value for the next switch.

## How it works

| PosPosFlag | Descriptions |
|---|---|
| 0 | Axis remains in the existing current or force operation mode. |
| 1 | Axis switches to position operation mode if `Pos` < `PosPosTh`. |
| 2 | Axis switches to position operation mode if `Pos` > `PosPosTh`. |

## Examples

```text
APosPosTh=100000     ; position threshold
APosPosFlag=2        ; switch to position mode when Pos > PosPosTh
```

## See also

- [PosPosTh](PosPosTh.md) — position threshold compared against Pos
- [Current operation mode](../03-current-operation-mode/00-overview.md) — switching from current mode
- [Force operation mode](../04-force-operation-mode/00-overview.md) — switching from force mode
