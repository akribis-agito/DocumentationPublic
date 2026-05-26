---
keyword: LimitsStat
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 49
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
overrides: {}
---
# LimitsStat

**Definition:**

LimitsStat reflects the current status of the limit switches. If the bit is set ("1"), limit is activated. If the bit is cleared ("0"), limit is not activated.

| LimitsStat, Bit # | 0 | 1 | 2-31 |
|---|---|---|---|
| Axis | RLS (Reverse Limit Switch) | FLS (Forward Limit Switch) | Unused |

**Example:**

LimitsStat == 1 indicate that RLS is active.

LimitsStat == 2 indicate that FLS is active.
