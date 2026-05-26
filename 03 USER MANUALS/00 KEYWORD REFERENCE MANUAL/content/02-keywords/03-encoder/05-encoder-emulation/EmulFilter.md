---
keyword: EmulFilter
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 403
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
  - 15
  default: 3
  scaling: 1.0
  implemented: final
overrides: {}
---
# EmulFilter

**Definition:**

EmulFilter sets the digital filter applied to the encoder emulation output signal. A higher value applies more filtering to reduce high-frequency noise on the emulated quadrature output. It is an axis-related parameter saved to flash.

**See also:**

[EmulRat](EmulRat.md), [EmulIndexType](EmulIndexType.md)
