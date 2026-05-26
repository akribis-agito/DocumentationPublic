---
keyword: RecTrigSrc
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 243
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
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RecTrigSrc

**Definition:**

RecTrigSrc defines the [complex CAN code](../../01-keyword-usage-and-syntax/complex-can-code.md) of the trigger source variable. Each index refers to a different trigger.

| Index | Scope no. | Trigger |
|---|---|---|
| 1 | 1 (First) | 1 |
| 2 | 1 (First) | 2 |
| 3 | 1 (First) | 3 |
| 4 | 2 (Second) | 1 |
| 5 | 2 (Second) | 2 |
| 6 | 2 (Second) | 3 |

It is possible to use the same variable as trigger source and recorded variable at the same time.

**Example:**

RecTrigSrc\[4\] = 2 will mean APos is to be used as trigger source for trigger 1 of the second scope.
