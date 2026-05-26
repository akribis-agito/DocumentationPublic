---
keyword: PosPosTh
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

**Condition:**

It is used only while axis is in current or force operation mode (OperationMode = 1 or 4).

**Definition:**

PosPosTh is the threshold position feedback (Pos) used together with PosPosFlag in the condition check to enter position operation mode.

| PosPosFlag | Descriptions                                                  |
|------------|---------------------------------------------------------------|
| 0          | Axis retains in the existing current or force operation mode. |
| 1          | Axis switches to position operation mode if Pos \< PosPosTh.  |
| 2          | Axis switches to position operation mode if Pos \> PosPosTh   |

See [Current operation mode](../../../02-keywords/08-axis-operation/03-current-operation-mode/00-overview.md) and [Force operation mode](../../../02-keywords/08-axis-operation/04-force-operation-mode/00-overview.md) for more information.
