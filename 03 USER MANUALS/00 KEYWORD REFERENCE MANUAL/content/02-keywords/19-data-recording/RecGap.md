---
keyword: RecGap
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 242
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
  - 1
  - 2147483647
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# RecGap

**Definition:**

RecGap is an array that defines the down sampling factors on the controller cycle frequency, thereby determining the data recording frequencies.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

The data recording frequency is as shown.

$$
Data\ recording\ frequency\ of\ scope\ x\ \lbrack Hz\rbrack = \frac{Controller\ cycle\ rate\ \lbrack Hz\rbrack}{RecGap\lbrack x\rbrack}
$$
