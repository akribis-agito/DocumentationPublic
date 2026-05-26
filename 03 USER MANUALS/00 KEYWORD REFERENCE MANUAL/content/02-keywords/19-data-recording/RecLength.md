---
keyword: RecLength
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 241
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
  - 16500
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RecLength

**Definition:**

RecLength is an array that defines the number of data points to capture per parameter, thereby determining the period of the recording.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

The period of data recording is as shown.

$$
Period\ of\ recording\ for\ scope\ x\ \lbrack s\rbrack = \frac{RecLength\lbrack x\rbrack \bullet RecGap\lbrack x\rbrack}{Controller\ cycle\ rate\ \lbrack Hz\rbrack}
$$
