---
keyword: VEncOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 613
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
# VEncOn

**Definition:**

VEncOn enables or disables the virtual encoder for the axis. When set to a non-zero value, the controller uses the software-generated virtual encoder position (defined by VEncSrc, VEncType, VEncFact, VEncFactDen, and VEncDelay) as the encoder feedback source. It is an axis-related parameter saved to flash.

**See also:**

[VEncSrc](VEncSrc.md), [VEncType](VEncType.md), [VEncFact](VEncFact.md), [VEncFactDen](VEncFactDen.md), [VEncDelay](VEncDelay.md)
