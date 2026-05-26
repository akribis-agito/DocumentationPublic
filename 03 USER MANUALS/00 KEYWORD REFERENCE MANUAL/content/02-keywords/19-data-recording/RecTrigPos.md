---
keyword: RecTrigPos
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 247
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 2
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 100
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RecTrigPos

**Definition:**

RecTrigPos defines the percentage of data points out of RecLength to capture before the trigger condition(s) activate. It is normally used for debugging process to allow monitoring of pre-trigger data.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

**Example:**

If RecLength\[1\] = 16384 and RecTrigPos\[1\] = 10, the first scope will have 1638 pre-trigger data points and 14746 post-trigger data points.
