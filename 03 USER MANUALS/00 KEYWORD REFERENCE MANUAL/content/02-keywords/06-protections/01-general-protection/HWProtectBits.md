---
keyword: HWProtectBits
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 74
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# HWProtectBits

**Definition:**

HWProtectBits is a read-only bit-field that reports the current state of the hardware protection inputs detected by the controller. Each bit corresponds to a specific hardware protection condition (such as over-current, over-voltage, or hardware enable signals). It is an axis-related status variable that is not saved to flash.

**See also:**

[ProtectMask](ProtectMask.md)
