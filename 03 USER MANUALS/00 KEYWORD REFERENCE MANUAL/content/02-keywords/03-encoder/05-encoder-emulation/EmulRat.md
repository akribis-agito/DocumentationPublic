---
keyword: EmulRat
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 69
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
  - -65536
  - 65536
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EmulRat

**Definition:**

EmulRat sets the ratio between the feedback encoder counts and the quadrature pulses output on the encoder emulation interface. Setting this value to N causes the controller to emit one A/B quadrature step for every N feedback encoder counts, allowing the emulated output to match a downstream device's expected resolution. It is an axis-related parameter saved to flash.

**See also:**

[EmulFilter](EmulFilter.md), [EmulIndexType](EmulIndexType.md), [EncRes](../01-general-settings/EncRes.md)
