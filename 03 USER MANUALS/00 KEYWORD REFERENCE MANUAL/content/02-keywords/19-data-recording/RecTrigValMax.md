---
keyword: RecTrigValMax
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 293
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 4
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
# RecTrigValMax

**Condition:**

RecTrigValMax is only applicable if the corresponding trigger activation logic is range-related (RecTrigTyp = 9, 10, 11 or 12).

**Definition:**

RecTrigValMax stores the maximum value for the selected trigger activation logics. Each index refers to a different trigger.

| Index | Scope no. | Trigger |
|---|---|---|
| 1 | 1 (First) | 1 |
| 2 | 1 (First) | 2 |
| 3 | 1 (First) | 3 |
| 4 | 2 (Second) | 1 |
| 5 | 2 (Second) | 2 |
| 6 | 2 (Second) | 3 |

Please refer to RecTrigTyp on how the maximum value is used.
