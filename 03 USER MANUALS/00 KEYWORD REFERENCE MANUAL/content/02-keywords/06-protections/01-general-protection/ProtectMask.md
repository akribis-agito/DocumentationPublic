---
keyword: ProtectMask
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 97
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
# ProtectMask

**Definition:**

ProtectMask is a bit-field that selects which hardware protection conditions are enabled and will trigger a fault. Setting a bit to 1 enables the corresponding protection; clearing it disables that protection. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[HWProtectBits](HWProtectBits.md)
