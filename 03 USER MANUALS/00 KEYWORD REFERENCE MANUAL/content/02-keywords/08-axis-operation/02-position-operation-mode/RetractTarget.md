---
keyword: RetractTarget
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 609
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RetractTarget

**Definition:**

RetractTarget is the absolute target used in the point-to-point motion upon entry to the position operation mode, subject to BeginOnToPos flag and RelTrgt value. If RelTrgt is not zero, the target position will be RelTrgt relative to the position reference upon position operation mode entry.
