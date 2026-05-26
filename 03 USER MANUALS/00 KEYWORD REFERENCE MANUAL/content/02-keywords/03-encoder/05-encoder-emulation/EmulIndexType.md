---
keyword: EmulIndexType
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 402
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EmulIndexType

**Definition:**

EmulIndexType selects the type of index pulse generated on the encoder emulation output. The options typically include a single pulse per revolution at a fixed position or a gated index. It is an axis-related parameter saved to flash.

**See also:**

[EmulRat](EmulRat.md), [EmulFilter](EmulFilter.md)
