---
keyword: VEncDelay
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 616
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
  - 25
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VEncDelay

**Definition:**

VEncDelay introduces a fixed delay between the source signal and the virtual encoder output. This can be used to compensate for latency in the feedback path or to synchronise the virtual encoder with an external process. It is an axis-related parameter saved to flash.

**See also:**

[VEncOn](VEncOn.md), [VEncSrc](VEncSrc.md), [VEncFact](VEncFact.md), [VEncFactDen](VEncFactDen.md)
