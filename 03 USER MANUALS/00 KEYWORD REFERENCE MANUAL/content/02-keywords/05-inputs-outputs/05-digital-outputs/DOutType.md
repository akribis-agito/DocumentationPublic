---
keyword: DOutType
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 209
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
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DOutType

**Definition:**

DOutType configures the digital outputs to operate in either sink or source mode, in 0-based indexing form.

| Bit’s value | Mode        |
|-------------|-------------|
| 0           | Sink mode   |
| 1           | Source mode |

**Example:**

If DOutType = 9 (binary 00000000 00000000 00000000 00001001), output 1 and 4 are in source mode, while all other outputs are in sink mode.

**Note:**

This keyword is applicable only for single ended digital outputs with configurable sink/source types. Please refer to individual product manual for more information.
