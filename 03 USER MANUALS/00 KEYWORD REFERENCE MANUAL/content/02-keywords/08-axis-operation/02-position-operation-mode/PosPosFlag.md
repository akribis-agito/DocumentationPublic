---
keyword: PosPosFlag
availability:
  standalone:
  - v4
  central-i:
  - v4
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

**Condition:**

It is used only while axis is in current or force operation mode (OperationMode = 1 or 4).

**Definition:**

PosPosFlag defines the trigger direction for the position feedback check (Pos) to enter position operation mode. If position feedback check is fulfilled, PosPosFlag is cleared to 0. User needs to reconfigure its value for next switch.

See [PosPosTh](../../../02-keywords/08-axis-operation/02-position-operation-mode/PosPosTh.md), [Current operation mode](../../../02-keywords/08-axis-operation/03-current-operation-mode/00-overview.md) and [Force operation mode](../../../02-keywords/08-axis-operation/04-force-operation-mode/00-overview.md) for more information.
